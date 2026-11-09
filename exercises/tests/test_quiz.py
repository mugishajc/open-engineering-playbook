"""Tests for exercises/quiz.py. Standard library only.

Run from the repository root:
  python3 -m unittest discover -s exercises/tests
"""
from __future__ import annotations

import contextlib
import io
import sys
import tempfile
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
EXERCISES = HERE.parent
REPO = EXERCISES.parent
sys.path.insert(0, str(EXERCISES))
sys.path.insert(0, str(REPO / "tools"))

import plain_lint  # noqa: E402
import quiz  # noqa: E402

AREAS = (
    "strategy", "operating-model", "ways-of-working", "delivery", "quality",
    "reliability", "security", "data", "ai", "architecture", "platform",
    "people", "measurement", "compliance", "leaders",
)


def statement(area: str, slug: str, level: str = "foundation", answer: bool = True, **extra) -> dict:
    data = {
        "id": f"{area}.{slug}",
        "area": area,
        "level": level,
        "statement": f"Statement {slug} in {area}.",
        "answer": answer,
        "explanation": f"This is why {slug} holds. Read the page to learn more.",
        "link": f"playbook/{area}.md",
    }
    data.update(extra)
    return data


def small_data() -> dict:
    return {
        "areas": [
            {"id": "alpha", "title": "Alpha", "intro": "Alpha intro."},
            {"id": "beta", "title": "Beta", "intro": "Beta intro."},
        ],
        "statements": [
            statement("alpha", "one", "foundation", True),
            statement("alpha", "two", "standard", False),
            statement("alpha", "three", "assured", True, link="playbook/other.md"),
            statement("beta", "one", "foundation", False),
            statement("beta", "two", "standard", True),
        ],
    }


def small_bank() -> quiz.Bank:
    return quiz.parse_bank(small_data())


def scripted(*replies: str):
    """An ask() that returns the replies in order, then behaves like end of input."""
    queue = list(replies)

    def ask(prompt: str) -> str:
        if not queue:
            raise EOFError
        return queue.pop(0)

    return ask


def run_cli(*argv: str, stdin: str = "") -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    old_stdin = sys.stdin
    sys.stdin = io.StringIO(stdin)
    try:
        with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
            code = quiz.main(list(argv), ask=input)
    finally:
        sys.stdin = old_stdin
    return code, out.getvalue(), err.getvalue()


class RealBankTest(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.bank = quiz.load_bank(quiz.DEFAULT_BANK)

    def test_areas_are_the_fourteen_plus_leaders(self):
        self.assertEqual(tuple(a.id for a in self.bank.areas), AREAS)

    def test_about_ten_statements_per_area(self):
        self.assertGreaterEqual(len(self.bank.statements), 140)
        for area in AREAS:
            with self.subTest(area=area):
                self.assertGreaterEqual(len(self.bank.in_area(area)), 8)

    def test_every_area_mixes_true_and_false(self):
        for area in AREAS:
            answers = {s.answer for s in self.bank.in_area(area)}
            self.assertEqual(answers, {True, False}, area)

    def test_answering_always_false_does_not_win(self):
        share_true = sum(s.answer for s in self.bank.statements) / len(self.bank.statements)
        self.assertGreater(share_true, 0.35)
        self.assertLess(share_true, 0.65)

    def test_every_level_is_used(self):
        self.assertEqual({s.level for s in self.bank.statements}, set(quiz.LEVELS))

    def test_statements_are_unique(self):
        texts = [s.text.lower() for s in self.bank.statements]
        self.assertEqual(len(texts), len(set(texts)))

    def test_links_and_exported_pages_are_current(self):
        self.assertEqual(quiz.check(self.bank, REPO, quiz.DEFAULT_EXPORT), [])

    def test_bank_and_pages_pass_plain_language_check(self):
        paths = [quiz.DEFAULT_BANK] + [quiz.DEFAULT_EXPORT / n for n in quiz.expected_pages(self.bank)]
        findings = plain_lint.run(paths, plain_lint.DEFAULT_WORDLIST)
        self.assertEqual([str(f) for f in findings], [])


class ParseBankTest(unittest.TestCase):
    def assertInvalid(self, data: dict, fragment: str):
        with self.assertRaises(quiz.QuizError) as ctx:
            quiz.parse_bank(data)
        self.assertIn(fragment, str(ctx.exception))

    def test_small_bank_loads(self):
        bank = small_bank()
        self.assertEqual([a.id for a in bank.areas], ["alpha", "beta"])
        self.assertEqual(len(bank.statements), 5)
        self.assertEqual(bank.area("beta").title, "Beta")

    def test_duplicate_id(self):
        data = small_data()
        data["statements"].append(statement("alpha", "one"))
        self.assertInvalid(data, "duplicate statement id")

    def test_area_must_match_id(self):
        data = small_data()
        data["statements"][0]["area"] = "beta"
        self.assertInvalid(data, "must match the id prefix")

    def test_unknown_area(self):
        data = small_data()
        data["statements"].append(statement("gamma", "one"))
        self.assertInvalid(data, "not listed under [[areas]]")

    def test_bad_level(self):
        data = small_data()
        data["statements"][0]["level"] = "expert"
        self.assertInvalid(data, "level must be one of")

    def test_answer_must_be_boolean(self):
        data = small_data()
        data["statements"][0]["answer"] = "true"
        self.assertInvalid(data, "answer must be true or false")

    def test_missing_fields(self):
        data = small_data()
        del data["statements"][0]["link"]
        data["areas"][0]["intro"] = ""
        self.assertInvalid(data, "missing link")
        self.assertInvalid(data, "missing intro")

    def test_explanation_length(self):
        data = small_data()
        data["statements"][0]["explanation"] = "Too short."
        self.assertInvalid(data, "explanation has 1 sentence(s)")
        data["statements"][0]["explanation"] = "One. Two. Three. Four. Five."
        self.assertInvalid(data, "explanation has 5 sentence(s)")

    def test_decimals_are_not_sentence_ends(self):
        self.assertEqual(quiz.count_sentences("A 99.9% SLO allows 40 minutes. See SemVer 2.0.0 for more."), 2)

    def test_link_must_be_relative_markdown(self):
        for link in ("/playbook/a.md", "https://example.org/a.md", "playbook/a.txt"):
            data = small_data()
            data["statements"][0]["link"] = link
            self.assertInvalid(data, "link must be a relative path")

    def test_area_without_statements(self):
        data = small_data()
        data["areas"].append({"id": "empty", "title": "Empty", "intro": "Nothing here."})
        self.assertInvalid(data, "area 'empty' has no statements")

    def test_missing_file(self):
        with self.assertRaises(quiz.QuizError):
            quiz.load_bank(Path("does-not-exist.toml"))


class SelectTest(unittest.TestCase):
    def setUp(self):
        self.bank = small_bank()

    def test_filter_by_area(self):
        chosen = quiz.select(self.bank, areas=["beta"], count=0, seed=1)
        self.assertEqual({s.area for s in chosen}, {"beta"})
        self.assertEqual(len(chosen), 2)

    def test_filter_by_level(self):
        chosen = quiz.select(self.bank, level="standard", count=0, seed=1)
        self.assertEqual(sorted(s.id for s in chosen), ["alpha.two", "beta.two"])

    def test_count_and_all(self):
        self.assertEqual(len(quiz.select(self.bank, count=3, seed=1)), 3)
        self.assertEqual(len(quiz.select(self.bank, count=0, seed=1)), 5)
        self.assertEqual(len(quiz.select(self.bank, count=50, seed=1)), 5)

    def test_seed_repeats_order(self):
        first = [s.id for s in quiz.select(self.bank, count=0, seed=42)]
        again = [s.id for s in quiz.select(self.bank, count=0, seed=42)]
        self.assertEqual(first, again)

    def test_unknown_area_suggests(self):
        with self.assertRaises(quiz.QuizError) as ctx:
            quiz.select(self.bank, areas=["alpah"])
        self.assertIn("did you mean 'alpha'", str(ctx.exception))

    def test_nothing_matches(self):
        with self.assertRaises(quiz.QuizError):
            quiz.select(self.bank, areas=["beta"], level="assured")


class ScoringTest(unittest.TestCase):
    def setUp(self):
        self.bank = small_bank()
        self.by_id = {s.id: s for s in self.bank.statements}

    def result(self, sid: str, correct: bool) -> quiz.Result:
        s = self.by_id[sid]
        return quiz.Result(s, s.answer if correct else not s.answer)

    def test_parse_reply(self):
        for word in ("t", "T", "true", "y", "yes", " Yes "):
            self.assertIs(quiz.parse_reply(word), True, word)
        for word in ("f", "false", "n", "no", "NO"):
            self.assertIs(quiz.parse_reply(word), False, word)
        for word in ("q", "quit", "exit"):
            self.assertEqual(quiz.parse_reply(word), quiz.QUIT)
        for word in ("", "maybe", "tf"):
            self.assertIsNone(quiz.parse_reply(word))

    def test_score_by_area(self):
        results = [
            self.result("beta.one", True),
            self.result("alpha.one", True),
            self.result("alpha.two", False),
        ]
        rows = quiz.score_by_area(self.bank, results)
        self.assertEqual(
            [(r["id"], r["right"], r["total"]) for r in rows],
            [("alpha", 1, 2), ("beta", 1, 1)],
        )

    def test_next_pages_ranks_by_misses_then_order(self):
        results = [
            self.result("alpha.three", False),  # playbook/other.md
            self.result("beta.one", False),     # playbook/beta.md
            self.result("beta.two", False),     # playbook/beta.md
            self.result("alpha.one", False),    # playbook/alpha.md
            self.result("alpha.two", True),
        ]
        self.assertEqual(
            quiz.next_pages(results),
            [("playbook/beta.md", 2), ("playbook/other.md", 1), ("playbook/alpha.md", 1)],
        )
        self.assertEqual(quiz.next_pages(results, limit=1), [("playbook/beta.md", 2)])

    def test_summary(self):
        results = [self.result("alpha.one", True), self.result("beta.one", False)]
        text = quiz.render_summary(self.bank, results)
        self.assertIn("Final score: 1 of 2 (50%)", text)
        self.assertIn("1. playbook/beta.md (1 missed)", text)
        self.assertIn("No misses", quiz.render_summary(self.bank, results[:1]))
        self.assertIn("No answers recorded", quiz.render_summary(self.bank, []))


class RunQuizTest(unittest.TestCase):
    def setUp(self):
        self.bank = small_bank()
        self.statements = quiz.select(self.bank, count=0, seed=3)

    def test_scores_answers_and_shows_running_score(self):
        replies = ["t" if s.answer else "f" for s in self.statements]
        replies[0] = "f" if self.statements[0].answer else "t"
        out = io.StringIO()
        results = quiz.run_quiz(self.bank, self.statements, ask=scripted(*replies), out=out)
        self.assertEqual(len(results), 5)
        self.assertEqual(sum(r.correct for r in results), 4)
        text = out.getvalue()
        self.assertIn("Not quite.", text)
        self.assertIn("Right.", text)
        self.assertIn("Score: 4 of 5", text)
        self.assertIn(f"Read: {self.statements[0].link}", text)

    def test_reprompts_on_unclear_reply(self):
        out = io.StringIO()
        results = quiz.run_quiz(self.bank, self.statements[:1], ask=scripted("maybe", "yes"), out=out)
        self.assertEqual(len(results), 1)
        self.assertTrue(results[0].reply)
        self.assertIn("Please type t or f", out.getvalue())

    def test_q_stops_early(self):
        out = io.StringIO()
        results = quiz.run_quiz(self.bank, self.statements, ask=scripted("t", "q", "t"), out=out)
        self.assertEqual(len(results), 1)
        self.assertIn("Stopping here.", out.getvalue())

    def test_end_of_input_stops(self):
        results = quiz.run_quiz(self.bank, self.statements, ask=scripted("n", "n"), out=io.StringIO())
        self.assertEqual(len(results), 2)


class ExportAndCheckTest(unittest.TestCase):
    def setUp(self):
        self.bank = small_bank()
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        for name in ("alpha", "beta", "other"):
            (self.root / "playbook").mkdir(exist_ok=True)
            (self.root / "playbook" / f"{name}.md").write_text("# Page\n", encoding="utf-8")
        self.out = self.root / "exercises" / "true-or-false"

    def tearDown(self):
        self.tmp.cleanup()

    def test_export_writes_one_page_per_area_and_an_index(self):
        written = quiz.export(self.bank, self.out)
        self.assertEqual(sorted(p.name for p in written), ["README.md", "alpha.md", "beta.md"])
        page = (self.out / "alpha.md").read_text(encoding="utf-8")
        self.assertTrue(page.startswith(quiz.MARKER))
        self.assertIn("# True or false: Alpha", page)
        self.assertIn("Alpha intro.", page)
        self.assertEqual(page.count("<details><summary>Answer</summary>"), 3)
        self.assertIn("**True.**", page)
        self.assertIn("**False.**", page)
        self.assertIn("[playbook/alpha.md](../../playbook/alpha.md)", page)
        self.assertIn("--area alpha", page)
        index = (self.out / "README.md").read_text(encoding="utf-8")
        self.assertIn("[Beta](beta.md) | 2 |", index)

    def test_check_passes_after_export(self):
        quiz.export(self.bank, self.out)
        self.assertEqual(quiz.check(self.bank, self.root, self.out), [])

    def test_check_finds_missing_and_stale_pages(self):
        problems = quiz.check(self.bank, self.root, self.out)
        self.assertEqual(sum("missing; run --export" in p for p in problems), 3)
        quiz.export(self.bank, self.out)
        (self.out / "beta.md").write_text("edited by hand\n", encoding="utf-8")
        problems = quiz.check(self.bank, self.root, self.out)
        self.assertEqual(len(problems), 1)
        self.assertIn("beta.md: out of date", problems[0])

    def test_check_finds_page_for_removed_area(self):
        quiz.export(self.bank, self.out)
        (self.out / "gamma.md").write_text(quiz.MARKER + "\n# Old\n", encoding="utf-8")
        (self.out / "notes.md").write_text("# Hand-written notes\n", encoding="utf-8")
        problems = quiz.check(self.bank, self.root, self.out)
        self.assertEqual(len(problems), 1)
        self.assertIn("gamma.md: generated page for an area that no longer exists", problems[0])

    def test_check_finds_broken_link(self):
        quiz.export(self.bank, self.out)
        (self.root / "playbook" / "other.md").unlink()
        problems = quiz.check(self.bank, self.root, self.out)
        self.assertEqual(problems, ["alpha.three: link playbook/other.md does not exist"])

    def test_html_in_statements_is_escaped(self):
        data = small_data()
        data["statements"][0]["statement"] = "A <script> tag is fine."
        page = quiz.render_area_page(quiz.parse_bank(data), quiz.parse_bank(data).area("alpha"))
        self.assertIn("A &lt;script&gt; tag is fine.", page)


class CliTest(unittest.TestCase):
    def test_check_passes_on_repository(self):
        code, out, err = run_cli("--check")
        self.assertEqual(code, 0, err)
        self.assertIn("pages up to date", out)

    def test_list(self):
        code, out, _ = run_cli("--list")
        self.assertEqual(code, 0)
        for area in AREAS:
            self.assertIn(area, out)

    def test_piped_answers(self):
        code, out, _ = run_cli("--area", "security", "--count", "3", "--seed", "1", stdin="t\nf\nmaybe\ntrue\n")
        self.assertEqual(code, 0)
        self.assertIn("[1/3] Security", out)
        self.assertIn("Please type t or f", out)
        self.assertIn("Final score:", out)
        self.assertIn("of 3", out)

    def test_quit_immediately(self):
        code, out, _ = run_cli("--count", "2", stdin="q\n")
        self.assertEqual(code, 0)
        self.assertIn("No answers recorded", out)

    def test_bad_area_exits_2(self):
        code, _, err = run_cli("--area", "securty")
        self.assertEqual(code, 2)
        self.assertIn("did you mean 'security'", err)

    def test_bad_bank_exits_2(self):
        with tempfile.TemporaryDirectory() as tmp:
            bad = Path(tmp) / "bank.toml"
            bad.write_text("this is = = not toml", encoding="utf-8")
            code, _, err = run_cli("--bank", str(bad), "--list")
        self.assertEqual(code, 2)
        self.assertIn("not valid TOML", err)


if __name__ == "__main__":
    unittest.main()
