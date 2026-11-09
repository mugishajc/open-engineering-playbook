"""Tests for assessment/assess.py. Standard library only.

Run from the repository root:
  python3 -m unittest discover -s assessment/tests
"""
from __future__ import annotations

import contextlib
import io
import json
import sys
import tempfile
import tomllib
import unittest
from pathlib import Path

HERE = Path(__file__).resolve().parent
ASSESSMENT = HERE.parent
REPO = ASSESSMENT.parent
sys.path.insert(0, str(ASSESSMENT))
sys.path.insert(0, str(REPO / "tools"))

import assess as ka  # noqa: E402
import plain_lint  # noqa: E402

QUESTIONS = ASSESSMENT / "questions.toml"
EXAMPLE = ASSESSMENT / "example-answers.toml"
AREAS = (
    "strategy", "operating-model", "ways-of-working", "delivery", "quality",
    "reliability", "security", "data", "ai", "architecture", "platform",
    "people", "measurement", "compliance",
)


def small_bank() -> ka.Bank:
    """Two areas, one question per level each."""
    data = {
        "areas": [{"id": "alpha", "title": "Alpha"}, {"id": "beta", "title": "Beta"}],
        "questions": [],
    }
    for area in ("alpha", "beta"):
        for level in ka.LEVELS:
            data["questions"].append(
                {
                    "id": f"{area}.{level}-check",
                    "level": level,
                    "text": f"Is the {level} check in {area} done?",
                    "action": f"Do the {level} check in {area}.",
                    "link": f"playbook/{area}.md",
                }
            )
    return ka.parse_bank(data)


def answers(bank: ka.Bank, true_ids=(), profile="startup", overlays=()) -> ka.Answers:
    values = {q.id: q.id in true_ids for q in bank.questions}
    return ka.Answers(profile, tuple(overlays), values)


def run_cli(*argv: str) -> tuple[int, str, str]:
    out, err = io.StringIO(), io.StringIO()
    with contextlib.redirect_stdout(out), contextlib.redirect_stderr(err):
        code = ka.main(list(argv))
    return code, out.getvalue(), err.getvalue()


class LevelCalculation(unittest.TestCase):
    def setUp(self):
        self.bank = small_bank()
        self.qs = self.bank.in_area("alpha")

    def level(self, *true_ids):
        return ka.area_level(self.qs, {i: True for i in true_ids})

    def test_nothing_true_is_below_foundation(self):
        self.assertEqual(self.level(), "none")

    def test_each_level_needs_all_lower_levels(self):
        self.assertEqual(self.level("alpha.foundation-check"), "foundation")
        self.assertEqual(self.level("alpha.foundation-check", "alpha.standard-check"), "standard")
        self.assertEqual(
            self.level("alpha.foundation-check", "alpha.standard-check", "alpha.assured-check"),
            "assured",
        )

    def test_higher_level_without_lower_does_not_count(self):
        self.assertEqual(self.level("alpha.standard-check", "alpha.assured-check"), "none")
        self.assertEqual(self.level("alpha.foundation-check", "alpha.assured-check"), "foundation")

    def test_every_question_at_a_level_must_be_true(self):
        data = {
            "areas": [{"id": "alpha", "title": "Alpha"}],
            "questions": [
                {"id": "alpha.one", "level": "foundation", "text": "t", "action": "a", "link": "l"},
                {"id": "alpha.two", "level": "foundation", "text": "t", "action": "a", "link": "l"},
            ],
        }
        qs = ka.parse_bank(data).questions
        self.assertEqual(ka.area_level(list(qs), {"alpha.one": True, "alpha.two": False}), "none")
        self.assertEqual(ka.area_level(list(qs), {"alpha.one": True, "alpha.two": True}), "foundation")


class TargetLevel(unittest.TestCase):
    def test_profiles(self):
        self.assertEqual(ka.target_level("solo"), "foundation")
        self.assertEqual(ka.target_level("startup"), "foundation")
        self.assertEqual(ka.target_level("scale-up"), "standard")
        self.assertEqual(ka.target_level("enterprise"), "standard")

    def test_any_overlay_means_assured(self):
        for profile in ka.PROFILE_TARGET:
            self.assertEqual(ka.target_level(profile, ["public-sector"]), "assured")
            self.assertEqual(ka.target_level(profile, ["regulated"]), "assured")
            self.assertEqual(ka.target_level(profile, ["public-sector", "regulated"]), "assured")

    def test_sme_profile_targets_foundation(self):
        self.assertEqual(ka.target_level("sme", []), "foundation")
        self.assertEqual(ka.target_level("sme", ["regulated"]), "assured")

    def test_unknown_profile(self):
        with self.assertRaises(ka.AssessError):
            ka.target_level("huge")

    def test_gap_uses_target(self):
        bank = small_bank()
        foundation_only = {"alpha.foundation-check", "beta.foundation-check"}
        r = ka.assess(bank, answers(bank, foundation_only, "startup"))
        self.assertEqual([a["gap"] for a in r["areas"]], [0, 0])
        r = ka.assess(bank, answers(bank, foundation_only, "enterprise"))
        self.assertEqual([a["gap"] for a in r["areas"]], [1, 1])
        r = ka.assess(bank, answers(bank, foundation_only, "startup", ["regulated"]))
        self.assertEqual([a["gap"] for a in r["areas"]], [2, 2])
        self.assertEqual(r["summary"]["areas_at_target"], 0)


class NextActions(unittest.TestCase):
    def test_foundation_gaps_come_before_standard(self):
        bank = small_bank()
        # alpha has foundation, beta has nothing.
        r = ka.assess(bank, answers(bank, {"alpha.foundation-check"}, "scale-up"))
        ids = [a["id"] for a in r["next_actions"]]
        self.assertEqual(ids[0], "beta.foundation-check")
        # Then standard gaps, weakest area (beta, below Foundation) first.
        self.assertEqual(ids[1:3], ["beta.standard-check", "alpha.standard-check"])
        # Then assured gaps, flagged as beyond the target.
        self.assertEqual(ids[3:5], ["beta.assured-check", "alpha.assured-check"])
        self.assertEqual([a["beyond_target"] for a in r["next_actions"]], [False, False, False, True, True])

    def test_lowest_area_first_within_a_level(self):
        bank = small_bank()
        r = ka.assess(
            bank,
            answers(bank, {"beta.foundation-check", "alpha.foundation-check", "beta.standard-check"}, "enterprise"),
        )
        self.assertEqual(r["next_actions"][0]["id"], "alpha.standard-check")

    def test_limit(self):
        bank = small_bank()
        self.assertEqual(len(ka.assess(bank, answers(bank), max_actions=5)["next_actions"]), 5)
        self.assertEqual(len(ka.assess(bank, answers(bank), max_actions=2)["next_actions"]), 2)

    def test_all_true_gives_no_actions(self):
        bank = small_bank()
        all_ids = {q.id for q in bank.questions}
        r = ka.assess(bank, answers(bank, all_ids, "enterprise", ["regulated"]))
        self.assertEqual(r["next_actions"], [])
        self.assertEqual(r["summary"]["areas_at_target"], 2)


class InitRoundTrip(unittest.TestCase):
    def test_init_parses_and_scores(self):
        bank = ka.load_bank(QUESTIONS)
        text = ka.render_init(bank, "scale-up")
        data = tomllib.loads(text)
        parsed = ka.parse_answers(data, bank)
        self.assertEqual(parsed.profile, "scale-up")
        self.assertEqual(parsed.overlays, ())
        self.assertEqual(set(parsed.values), {q.id for q in bank.questions})
        self.assertFalse(any(parsed.values.values()))
        result = ka.assess(bank, parsed)
        self.assertTrue(all(a["reached"] == "none" for a in result["areas"]))

    def test_init_has_question_text_as_comments(self):
        bank = ka.load_bank(QUESTIONS)
        text = ka.render_init(bank)
        for q in bank.questions:
            self.assertIn(f"# [{q.level}] {q.text}", text)
            self.assertIn(f'"{q.id}" = false', text)

    def test_init_cli_writes_to_stdout_without_output(self):
        code, out, err = run_cli("--questions", str(QUESTIONS), "--init")
        self.assertEqual((code, err), (0, ""))
        self.assertEqual(out, ka.render_init(ka.load_bank(QUESTIONS)))
        tomllib.loads(out)

    def test_init_cli_refuses_to_overwrite(self):
        with tempfile.TemporaryDirectory() as tmp:
            target = Path(tmp) / "answers.toml"
            target.write_text("keep me", encoding="utf-8")
            code, _, err = run_cli("--questions", str(QUESTIONS), "--init", "--output", str(target))
            self.assertEqual(code, 2)
            self.assertIn("already exists", err)
            self.assertEqual(target.read_text(encoding="utf-8"), "keep me")
            code, _, _ = run_cli("--questions", str(QUESTIONS), "--init", "--output", str(target), "--force")
            self.assertEqual(code, 0)
            self.assertIn("[answers]", target.read_text(encoding="utf-8"))

    def test_nested_tables_are_accepted(self):
        bank = small_bank()
        data = {
            "profile": "solo",
            "answers": {
                "alpha": {"foundation-check": True, "standard-check": False, "assured-check": False},
                "beta.foundation-check": True,
                "beta.standard-check": False,
                "beta.assured-check": False,
            },
        }
        parsed = ka.parse_answers(data, bank)
        self.assertTrue(parsed.values["alpha.foundation-check"])
        self.assertTrue(parsed.values["beta.foundation-check"])


class Errors(unittest.TestCase):
    def setUp(self):
        self.bank = small_bank()
        self.complete = {q.id: False for q in self.bank.questions}

    def test_unknown_id(self):
        data = {"profile": "startup", "answers": {**self.complete, "alpha.foundaton-check": True}}
        with self.assertRaises(ka.AssessError) as ctx:
            ka.parse_answers(data, self.bank)
        msg = str(ctx.exception)
        self.assertIn("unknown question id 'alpha.foundaton-check'", msg)
        self.assertIn("did you mean 'alpha.foundation-check'", msg)

    def test_missing_answers(self):
        partial = dict(self.complete)
        del partial["beta.assured-check"]
        with self.assertRaises(ka.AssessError) as ctx:
            ka.parse_answers({"profile": "startup", "answers": partial}, self.bank)
        self.assertIn("beta.assured-check", str(ctx.exception))
        parsed = ka.parse_answers({"profile": "startup", "answers": partial}, self.bank, allow_missing=True)
        self.assertFalse(parsed.values["beta.assured-check"])

    def test_bad_profile_overlay_and_value(self):
        data = {
            "profile": "medium",
            "overlays": ["military"],
            "answers": {**self.complete, "alpha.foundation-check": "yes"},
        }
        with self.assertRaises(ka.AssessError) as ctx:
            ka.parse_answers(data, self.bank)
        msg = str(ctx.exception)
        self.assertIn("profile is 'medium'", msg)
        self.assertIn("unknown overlay 'military'", msg)
        self.assertIn("must be true or false", msg)

    def test_cli_unknown_id_exit_code(self):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "a.toml"
            text = ka.render_init(ka.load_bank(QUESTIONS)) + '"delivery.not-a-question" = true\n'
            path.write_text(text, encoding="utf-8")
            code, out, err = run_cli("--questions", str(QUESTIONS), "--answers", str(path))
            self.assertEqual(code, 2)
            self.assertEqual(out, "")
            self.assertIn("unknown question id 'delivery.not-a-question'", err)

    def test_invalid_bank(self):
        with self.assertRaises(ka.AssessError):
            ka.parse_bank({"areas": [{"id": "alpha"}], "questions": [
                {"id": "alpha.x", "level": "expert", "text": "t", "action": "a", "link": "l"},
                {"id": "gamma.y", "level": "standard", "text": "t", "action": "a", "link": "l"},
            ]})


class Formats(unittest.TestCase):
    def test_json_format(self):
        code, out, _ = run_cli("--questions", str(QUESTIONS), "--answers", str(EXAMPLE), "--format", "json")
        self.assertEqual(code, 0)
        data = json.loads(out)
        self.assertEqual(data["profile"], "startup")
        self.assertEqual(data["target"], "foundation")
        self.assertEqual([a["id"] for a in data["areas"]], list(AREAS))
        self.assertEqual(len(data["next_actions"]), 5)
        for key in ("areas_at_target", "lowest_level", "questions_yes", "questions_total"):
            self.assertIn(key, data["summary"])

    def test_markdown_passes_plain_language_check(self):
        code, out, _ = run_cli("--questions", str(QUESTIONS), "--answers", str(EXAMPLE))
        self.assertEqual(code, 0)
        self.assertTrue(out.startswith("# Maturity report"))
        self.assertIn("## Next 5 actions", out)
        patterns = plain_lint.compile_phrases(plain_lint.load_phrases(plain_lint.DEFAULT_WORDLIST))
        findings = list(plain_lint.check_text(Path("report.md"), out, patterns))
        self.assertEqual(findings, [], "\n".join(str(f) for f in findings))

    def test_output_file_and_check_flag(self):
        with tempfile.TemporaryDirectory() as tmp:
            report = Path(tmp) / "report.md"
            code, out, _ = run_cli(
                "--questions", str(QUESTIONS), "--answers", str(EXAMPLE), "--output", str(report), "--check"
            )
            self.assertEqual(code, 1)  # the example has areas below target
            self.assertEqual(out, "")
            self.assertIn("| Delivery |", report.read_text(encoding="utf-8"))


class QuestionBank(unittest.TestCase):
    """Guards the shipped question bank against drift."""

    def setUp(self):
        self.bank = ka.load_bank(QUESTIONS)

    def test_fourteen_areas_in_order(self):
        self.assertEqual(tuple(a.id for a in self.bank.areas), AREAS)

    def test_four_to_six_questions_per_area_covering_every_level(self):
        for area in AREAS:
            qs = self.bank.in_area(area)
            self.assertTrue(4 <= len(qs) <= 6, f"{area} has {len(qs)} questions")
            self.assertEqual({q.level for q in qs}, set(ka.LEVELS), area)

    def test_links_point_at_playbook_pages(self):
        for q in self.bank.questions:
            self.assertRegex(q.link, r"^playbook/[a-z-]+/[a-z0-9-]+\.md$", q.id)

    def test_shipped_text_passes_plain_language_check(self):
        patterns = plain_lint.compile_phrases(plain_lint.load_phrases(plain_lint.DEFAULT_WORDLIST))
        text = ka.render_init(self.bank)
        findings = list(plain_lint.check_text(Path("answers.md"), text, patterns))
        self.assertEqual(findings, [], "\n".join(str(f) for f in findings))


if __name__ == "__main__":
    unittest.main()
