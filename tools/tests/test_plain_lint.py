"""Tests for tools/plain_lint.py. Standard library only.

Run from the repository root:
  python3 -m unittest discover -s tools/tests

This file is itself scanned by the check, so it never spells out a banned
character or phrase. Dashes and emoji are written as escapes, and phrases
come from a test word list or are read from the real list at run time.
"""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

TOOLS = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(TOOLS))

import plain_lint  # noqa: E402

EM_DASH = "\u2014"
EN_DASH = "\u2013"
EMOJI = "\U0001F680"
MARKER = plain_lint.IGNORE_FILE_MARKER
TEST_WORDS = ["frobnicate", "widget-ish", "very shiny thing"]


def findings(text: str, name: str = "page.md", words=TEST_WORDS):
    patterns = plain_lint.compile_phrases([w.lower() for w in words])
    return list(plain_lint.check_text(Path(name), text, patterns))


class Dashes(unittest.TestCase):
    def test_em_dash(self):
        found = findings(f"Ship it {EM_DASH} today.")
        self.assertEqual(len(found), 1)
        self.assertIn("em dash", found[0].message)
        self.assertEqual((found[0].line, found[0].column), (1, 9))

    def test_en_dash(self):
        found = findings(f"Pages 1{EN_DASH}5.")
        self.assertEqual(len(found), 1)
        self.assertIn("en dash", found[0].message)

    def test_dashes_flagged_in_every_text_type(self):
        for name in ("a.md", "a.py", "a.yml", "a.toml"):
            self.assertEqual(len(findings(f"x {EM_DASH} y", name)), 1, name)

    def test_hyphen_is_fine(self):
        self.assertEqual(findings("A well-known, 1-to-5 range."), [])


class Phrases(unittest.TestCase):
    def test_case_insensitive(self):
        self.assertEqual(len(findings("We FROBNICATE the cache.")), 1)
        self.assertEqual(len(findings("Frobnicate first.")), 1)

    def test_whole_words_only(self):
        # A longer word that starts or ends with a banned word is allowed.
        self.assertEqual(findings("Frobnicateness is fine."), [])
        self.assertEqual(findings("Unfrobnicate is fine."), [])

    def test_hyphen_counts_as_part_of_the_word(self):
        # The lookarounds treat a hyphen like a letter, so hyphenated
        # compounds of a banned word are not flagged.
        self.assertEqual(findings("A non-frobnicate step."), [])
        self.assertEqual(findings("A frobnicate-free step."), [])

    def test_punctuation_ends_a_word(self):
        self.assertEqual(len(findings("Then frobnicate.")), 1)
        self.assertEqual(len(findings("(frobnicate)")), 1)
        self.assertEqual(len(findings("'frobnicate'")), 1)

    def test_hyphenated_and_multi_word_phrases(self):
        self.assertEqual(len(findings("It is widget-ish.")), 1)
        self.assertEqual(len(findings("A Very Shiny Thing.")), 1)
        self.assertEqual(findings("A very shiny thingamajig."), [])

    def test_real_word_list_whole_word_behaviour(self):
        phrases = plain_lint.load_phrases(plain_lint.DEFAULT_WORDLIST)
        self.assertTrue(phrases)
        self.assertFalse(any(p.startswith("#") for p in phrases))
        word = next(p for p in phrases if p.isalpha())
        patterns = plain_lint.compile_phrases(phrases)
        hit = list(plain_lint.check_text(Path("a.md"), f"We {word.upper()} it.", patterns))
        self.assertGreaterEqual(len(hit), 1)
        miss = list(plain_lint.check_text(Path("a.md"), f"We {word}zzz it.", patterns))
        self.assertEqual(miss, [])

    def test_one_finding_per_phrase_per_line(self):
        self.assertEqual(len(findings("frobnicate and frobnicate again")), 1)


class Emoji(unittest.TestCase):
    def test_flagged_in_markdown(self):
        found = findings(f"Launch {EMOJI}", "page.md")
        self.assertEqual([f.message for f in found], ["emoji in Markdown"])

    def test_ignored_outside_markdown(self):
        for name in ("a.py", "a.yml", "a.txt"):
            self.assertEqual(findings(f"Launch {EMOJI}", name), [], name)


class IgnoreMarker(unittest.TestCase):
    def test_marker_in_first_five_lines_skips_file(self):
        text = "\n".join(["# Title", "", "", f"<!-- {MARKER} -->", f"x {EM_DASH} y"])
        self.assertEqual(findings(text), [])

    def test_marker_after_line_five_is_ignored(self):
        text = "\n".join(["a", "b", "c", "d", "e", f"<!-- {MARKER} -->", f"x {EM_DASH} y"])
        self.assertEqual(len(findings(text)), 1)


class CommandLine(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.wordlist = self.root / "words.txt"
        self.wordlist.write_text("# comment line\nfrobnicate\n", encoding="utf-8")

    def tearDown(self):
        self.tmp.cleanup()

    def run_main(self, *paths: Path) -> tuple[int, str, str]:
        out, err = io.StringIO(), io.StringIO()
        argv = [str(p) for p in paths] + ["--wordlist", str(self.wordlist)]
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = plain_lint.main(argv)
        return code, out.getvalue(), err.getvalue()

    def test_clean_tree_exits_zero_and_prints_nothing(self):
        (self.root / "ok.md").write_text("Plain words only.\n", encoding="utf-8")
        code, out, err = self.run_main(self.root)
        self.assertEqual((code, out, err), (0, "", ""))

    def test_findings_exit_one_with_location(self):
        bad = self.root / "docs" / "bad.md"
        bad.parent.mkdir()
        bad.write_text(f"Fine.\nWe frobnicate {EM_DASH} daily.\n", encoding="utf-8")
        code, out, err = self.run_main(self.root)
        self.assertEqual(code, 1)
        self.assertIn(f"{bad}:2:", out)
        self.assertIn("2 finding(s)", err)

    def test_word_list_is_not_scanned(self):
        # The word list contains every banned phrase by design.
        code, _, _ = self.run_main(self.root)
        self.assertEqual(code, 0)

    def test_skipped_dirs_and_unknown_suffixes(self):
        nm = self.root / "node_modules"
        nm.mkdir()
        (nm / "bad.md").write_text("frobnicate\n", encoding="utf-8")
        (self.root / "image.svg").write_text("frobnicate\n", encoding="utf-8")
        code, _, _ = self.run_main(self.root)
        self.assertEqual(code, 0)

    def test_explicit_file_path_is_checked_whatever_its_suffix(self):
        odd = self.root / "notes.svg"
        odd.write_text("frobnicate\n", encoding="utf-8")
        code, _, _ = self.run_main(odd)
        self.assertEqual(code, 1)


if __name__ == "__main__":
    unittest.main()
