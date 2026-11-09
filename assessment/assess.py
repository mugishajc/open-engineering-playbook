#!/usr/bin/env python3
"""Open Engineering Playbook maturity assessment.

Reads a question bank and an answers file, both TOML. Works out the level
each practice area has reached, compares it with the target level for your
profile and overlays, and lists the next actions to take.

Usage:
  python3 assessment/assess.py --questions assessment/questions.toml \\
      --answers my-answers.toml [--format markdown|json] [--output report.md]

  python3 assessment/assess.py --questions assessment/questions.toml \\
      --init [--profile startup] [--output my-answers.toml]

Exit codes:
  0  report written
  1  --check was given and at least one area is below its target
  2  the input files are invalid

Profiles can skip whole areas, keep their target when an overlay applies,
and put some areas first in the next actions. The rules live in the question
bank under [profiles.<name>]. A question can also carry only_profiles or
skip_profiles, so a profile such as SME gets questions written for it.

Standard library only. Python 3.11 or later (uses tomllib).
"""
from __future__ import annotations

import argparse
import difflib
import json
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any

try:
    import tomllib
except ModuleNotFoundError:  # pragma: no cover
    sys.exit(
        "assess.py needs Python 3.11 or later (it uses tomllib); this is Python "
        + ".".join(str(n) for n in sys.version_info[:3])
        + ".\nRun it with a newer Python if you have one: python3.12 or python3.11 on "
        "macOS and Linux, py -3 on Windows.\nOtherwise install the current release "
        "from https://www.python.org/downloads/ or your package manager."
    )

LEVELS = ("foundation", "standard", "assured")
LEVEL_RANK = {"none": 0, "foundation": 1, "standard": 2, "assured": 3}
LEVEL_LABEL = {
    "none": "Below Foundation",
    "foundation": "Foundation",
    "standard": "Standard",
    "assured": "Assured",
}
PROFILE_TARGET = {
    "solo": "foundation",
    "sme": "foundation",
    "startup": "foundation",
    "scale-up": "standard",
    "enterprise": "standard",
}
PROFILE_PAGE = "profiles/{profile}.md"
PROFILE_LABEL = {
    "solo": "Solo",
    "sme": "SME",
    "startup": "Startup",
    "scale-up": "Scale-up",
    "enterprise": "Enterprise",
}
OVERLAYS = ("public-sector", "regulated")
OVERLAY_LABEL = {"public-sector": "Public sector", "regulated": "Regulated"}
OVERLAY_TARGET = "assured"

SLUG = r"[a-z0-9]+(?:-[a-z0-9]+)*"
ID_RE = re.compile(rf"^{SLUG}\.{SLUG}$")
AREA_RE = re.compile(rf"^{SLUG}$")
DEFAULT_QUESTIONS = Path(__file__).with_name("questions.toml")
DEFAULT_ACTIONS = 5
REPO_ROOT = Path(__file__).resolve().parent.parent
# Used for report links when the answers file lives outside this repository,
# where links relative to the playbook root would be broken.
PUBLIC_LINK_BASE = "https://github.com/mugishajc/open-engineering-playbook/blob/main/"


class AssessError(Exception):
    """Invalid input. The message is shown to the user as is."""


@dataclass(frozen=True)
class Area:
    id: str
    title: str
    index: int


@dataclass(frozen=True)
class Question:
    id: str
    area: str
    level: str
    text: str
    action: str
    link: str
    index: int
    only_profiles: tuple[str, ...] = ()
    skip_profiles: tuple[str, ...] = ()

    def applies_to(self, profile: str) -> bool:
        if self.only_profiles and profile not in self.only_profiles:
            return False
        return profile not in self.skip_profiles


@dataclass(frozen=True)
class ProfileRule:
    """How one profile differs from the default scoring."""

    skip_areas: tuple[str, ...] = ()
    area_order: tuple[str, ...] = ()
    overlays_raise_target: bool = True


NO_RULE = ProfileRule()


@dataclass(frozen=True)
class Bank:
    areas: tuple[Area, ...]
    questions: tuple[Question, ...]
    rules: tuple[tuple[str, ProfileRule], ...] = ()

    def by_id(self) -> dict[str, Question]:
        return {q.id: q for q in self.questions}

    def rule(self, profile: str) -> ProfileRule:
        return dict(self.rules).get(profile, NO_RULE)

    def areas_for(self, profile: str | None = None) -> list[Area]:
        """Areas assessed for a profile, in bank order. None means all."""
        if profile is None:
            return list(self.areas)
        skip = set(self.rule(profile).skip_areas)
        return [a for a in self.areas if a.id not in skip]

    def in_area(self, area_id: str, profile: str | None = None) -> list[Question]:
        """Questions in one area, lowest level first, then bank order."""
        qs = [
            q
            for q in self.questions
            if q.area == area_id and (profile is None or q.applies_to(profile))
        ]
        return sorted(qs, key=lambda q: (LEVEL_RANK.get(q.level, 0), q.index))

    def questions_for(self, profile: str) -> list[Question]:
        assessed = {a.id for a in self.areas_for(profile)}
        return [q for q in self.questions if q.area in assessed and q.applies_to(profile)]


@dataclass(frozen=True)
class Answers:
    profile: str
    overlays: tuple[str, ...]
    values: dict[str, bool]


# ------------------------------------------------------------------ loading


def _read_toml(path: Path, what: str) -> dict[str, Any]:
    try:
        with path.open("rb") as fh:
            return tomllib.load(fh)
    except FileNotFoundError:
        raise AssessError(f"{what} file not found: {path}") from None
    except tomllib.TOMLDecodeError as exc:
        raise AssessError(f"{what} file {path} is not valid TOML: {exc}") from None


def parse_bank(data: dict[str, Any]) -> Bank:
    errors: list[str] = []
    areas: list[Area] = []
    seen_areas: set[str] = set()
    for i, raw in enumerate(data.get("areas", [])):
        area_id = raw.get("id", "")
        if not AREA_RE.match(area_id):
            errors.append(f"areas[{i}]: id {area_id!r} must be lower case words joined by hyphens")
            continue
        if area_id in seen_areas:
            errors.append(f"areas[{i}]: duplicate area id {area_id!r}")
            continue
        seen_areas.add(area_id)
        areas.append(Area(area_id, raw.get("title", area_id), len(areas)))

    questions: list[Question] = []
    seen_ids: set[str] = set()
    for i, raw in enumerate(data.get("questions", [])):
        qid = raw.get("id", "")
        where = f"questions[{i}] ({qid or 'no id'})"
        if not ID_RE.match(qid):
            errors.append(f"{where}: id must look like 'area.short-name'")
            continue
        if qid in seen_ids:
            errors.append(f"{where}: duplicate question id")
            continue
        seen_ids.add(qid)
        area_id = qid.split(".", 1)[0]
        if area_id not in seen_areas:
            errors.append(f"{where}: area {area_id!r} is not listed under [[areas]]")
        level = raw.get("level", "")
        if level not in LEVELS:
            errors.append(f"{where}: level must be one of {', '.join(LEVELS)}")
        for field in ("text", "action", "link"):
            if not isinstance(raw.get(field), str) or not raw[field].strip():
                errors.append(f"{where}: missing {field}")
        only = _profile_list(raw, "only_profiles", where, errors)
        skip = _profile_list(raw, "skip_profiles", where, errors)
        if only and skip:
            errors.append(f"{where}: use only_profiles or skip_profiles, not both")
        questions.append(
            Question(
                id=qid,
                area=area_id,
                level=level,
                text=str(raw.get("text", "")).strip(),
                action=str(raw.get("action", "")).strip(),
                link=str(raw.get("link", "")).strip(),
                index=len(questions),
                only_profiles=only,
                skip_profiles=skip,
            )
        )

    for area in areas:
        if not any(q.area == area.id for q in questions):
            errors.append(f"area {area.id!r} has no questions")
    if not areas:
        errors.append("no [[areas]] defined")

    rules = _parse_rules(data.get("profiles", {}), seen_areas, errors)
    bank = Bank(tuple(areas), tuple(questions), tuple(sorted(rules.items())))
    if not errors:
        # Every area a profile assesses must be able to reach Foundation.
        for profile in PROFILE_TARGET:
            for area in bank.areas_for(profile):
                if not any(q.level == "foundation" for q in bank.in_area(area.id, profile)):
                    errors.append(
                        f"profile {profile!r}: area {area.id!r} has no Foundation question; "
                        "add one or skip the area for this profile"
                    )
    if errors:
        raise AssessError("Invalid question bank:\n  " + "\n  ".join(errors))
    return bank


def _profile_list(raw: dict[str, Any], field: str, where: str, errors: list[str]) -> tuple[str, ...]:
    value = raw.get(field, [])
    if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
        errors.append(f"{where}: {field} must be a list of profile names")
        return ()
    for name in value:
        if name not in PROFILE_TARGET:
            errors.append(f"{where}: unknown profile {name!r} in {field}")
    return tuple(value)


def _parse_rules(raw: Any, area_ids: set[str], errors: list[str]) -> dict[str, ProfileRule]:
    if not isinstance(raw, dict):
        errors.append("[profiles] must be a table, for example [profiles.sme]")
        return {}
    rules: dict[str, ProfileRule] = {}
    for name, table in raw.items():
        where = f"profiles.{name}"
        if name not in PROFILE_TARGET:
            errors.append(f"{where}: unknown profile; allowed: {', '.join(PROFILE_TARGET)}")
            continue
        if not isinstance(table, dict):
            errors.append(f"{where}: must be a table")
            continue
        unknown = sorted(set(table) - {"skip_areas", "area_order", "overlays_raise_target"})
        if unknown:
            errors.append(f"{where}: unknown keys {', '.join(unknown)}")
        lists: dict[str, tuple[str, ...]] = {}
        for key in ("skip_areas", "area_order"):
            value = table.get(key, [])
            if not isinstance(value, list) or not all(isinstance(v, str) for v in value):
                errors.append(f"{where}: {key} must be a list of area ids")
                value = []
            for area_id in value:
                if area_id not in area_ids:
                    errors.append(f"{where}: unknown area {area_id!r} in {key}")
            lists[key] = tuple(value)
        if area_ids and set(lists["skip_areas"]) >= area_ids:
            errors.append(f"{where}: skip_areas cannot skip every area")
        raise_target = table.get("overlays_raise_target", True)
        if not isinstance(raise_target, bool):
            errors.append(f"{where}: overlays_raise_target must be true or false")
            raise_target = True
        rules[name] = ProfileRule(lists["skip_areas"], lists["area_order"], raise_target)
    return rules


def load_bank(path: Path) -> Bank:
    return parse_bank(_read_toml(path, "Questions"))


def _flatten(table: dict[str, Any], prefix: str = "") -> dict[str, Any]:
    """Turn {"delivery": {"x": true}} and {"delivery.x": true} into one form."""
    flat: dict[str, Any] = {}
    for key, value in table.items():
        full = f"{prefix}.{key}" if prefix else key
        if isinstance(value, dict):
            flat.update(_flatten(value, full))
        else:
            flat[full] = value
    return flat


def parse_answers(data: dict[str, Any], bank: Bank, allow_missing: bool = False) -> Answers:
    errors: list[str] = []

    profile = data.get("profile")
    if profile not in PROFILE_TARGET:
        errors.append(
            f"profile is {profile!r}; set it to one of: {', '.join(PROFILE_TARGET)}"
        )

    overlays_raw = data.get("overlays", [])
    if not isinstance(overlays_raw, list):
        errors.append("overlays must be a list, for example overlays = [\"regulated\"]")
        overlays_raw = []
    overlays: list[str] = []
    for item in overlays_raw:
        if item not in OVERLAYS:
            errors.append(f"unknown overlay {item!r}; allowed: {', '.join(OVERLAYS)}")
        elif item not in overlays:
            overlays.append(item)

    raw_answers = data.get("answers")
    if not isinstance(raw_answers, dict):
        errors.append("no [answers] table found")
        raw_answers = {}
    flat = _flatten(raw_answers)

    known = bank.by_id()
    values: dict[str, bool] = {}
    unknown = sorted(k for k in flat if k not in known)
    for key in unknown:
        hint = difflib.get_close_matches(key, known.keys(), n=1)
        suffix = f" (did you mean {hint[0]!r}?)" if hint else ""
        errors.append(f"unknown question id {key!r}{suffix}")
    for key, value in flat.items():
        if key not in known:
            continue
        if not isinstance(value, bool):
            errors.append(f"answer for {key!r} must be true or false, not {value!r}")
            continue
        values[key] = value

    # Only the questions this profile is asked count as missing. Answers to
    # questions the profile skips are accepted and ignored, so a team can
    # change profile without deleting lines.
    asked = bank.questions_for(profile) if profile in PROFILE_TARGET else list(bank.questions)
    missing = [q.id for q in asked if q.id not in flat]
    if missing and not allow_missing:
        errors.append(
            f"{len(missing)} question(s) have no answer: {', '.join(missing)}. "
            "Add them, or pass --allow-missing to count them as false."
        )
    for qid in missing:
        values[qid] = False
    for q in bank.questions:
        values.setdefault(q.id, False)

    if errors:
        raise AssessError("Invalid answers file:\n  " + "\n  ".join(errors))
    return Answers(str(profile), tuple(overlays), values)


def load_answers(path: Path, bank: Bank, allow_missing: bool = False) -> Answers:
    return parse_answers(_read_toml(path, "Answers"), bank, allow_missing)


# ------------------------------------------------------------------ scoring


def target_level(
    profile: str,
    overlays: tuple[str, ...] | list[str] = (),
    rule: ProfileRule = NO_RULE,
) -> str:
    if profile not in PROFILE_TARGET:
        raise AssessError(f"unknown profile {profile!r}")
    if overlays and rule.overlays_raise_target:
        return OVERLAY_TARGET
    return PROFILE_TARGET[profile]


def area_level(questions: list[Question], values: dict[str, bool]) -> str:
    """Highest level whose questions, and all questions below it, are true.

    A level with no questions in the area is never reached: an area cannot
    claim a level it has no evidence for.
    """
    reached = "none"
    for level in LEVELS:
        at_level = [q for q in questions if q.level == level]
        if at_level and all(values.get(q.id, False) for q in at_level):
            reached = level
        else:
            break
    return reached


def assess(bank: Bank, answers: Answers, max_actions: int = DEFAULT_ACTIONS) -> dict[str, Any]:
    profile = answers.profile
    rule = bank.rule(profile)
    target = target_level(profile, answers.overlays, rule)
    target_rank = LEVEL_RANK[target]
    values = answers.values
    assessed = bank.areas_for(profile)
    asked = bank.questions_for(profile)

    areas: list[dict[str, Any]] = []
    area_rank: dict[str, int] = {}
    area_share: dict[str, float] = {}
    for area in assessed:
        qs = bank.in_area(area.id, profile)
        reached = area_level(qs, values)
        yes = sum(1 for q in qs if values.get(q.id))
        area_rank[area.id] = LEVEL_RANK[reached]
        area_share[area.id] = yes / len(qs)
        areas.append(
            {
                "id": area.id,
                "title": area.title,
                "reached": reached,
                "target": target,
                "gap": max(0, target_rank - LEVEL_RANK[reached]),
                "yes": yes,
                "total": len(qs),
                "open": [q.id for q in qs if not values.get(q.id)],
            }
        )

    # A profile's area_order puts its most important areas first; the other
    # areas follow in bank order.
    first = {a: i for i, a in enumerate(rule.area_order)}
    area_index = {a.id: first.get(a.id, len(first) + a.index) for a in assessed}

    def priority(q: Question) -> tuple:
        # Lowest level first, then the weakest area, then area order, then file order.
        return (LEVEL_RANK[q.level], area_rank[q.area], area_share[q.area], area_index[q.area], q.index)

    open_qs = [q for q in asked if not values.get(q.id)]
    within = sorted((q for q in open_qs if LEVEL_RANK[q.level] <= target_rank), key=priority)
    beyond = sorted((q for q in open_qs if LEVEL_RANK[q.level] > target_rank), key=priority)
    titles = {a.id: a.title for a in bank.areas}
    actions = [
        {
            "id": q.id,
            "area": q.area,
            "area_title": titles[q.area],
            "level": q.level,
            "action": q.action,
            "link": q.link,
            "beyond_target": LEVEL_RANK[q.level] > target_rank,
        }
        for q in (within + beyond)[: max(0, max_actions)]
    ]

    lowest_rank = min(area_rank.values())
    lowest = next(k for k, v in LEVEL_RANK.items() if v == lowest_rank)
    in_scope = [q for q in asked if LEVEL_RANK[q.level] <= target_rank]
    total_yes = sum(1 for q in asked if values.get(q.id))
    assessed_ids = {a.id for a in assessed}
    return {
        "profile": profile,
        "overlays": list(answers.overlays),
        "target": target,
        "overlays_raise_target": rule.overlays_raise_target,
        "skipped_areas": [{"id": a.id, "title": a.title} for a in bank.areas if a.id not in assessed_ids],
        "summary": {
            "areas_total": len(areas),
            "areas_at_target": sum(1 for a in areas if a["gap"] == 0),
            "lowest_level": lowest,
            "lowest_areas": [a["id"] for a in areas if LEVEL_RANK[a["reached"]] == lowest_rank],
            "questions_total": len(asked),
            "questions_yes": total_yes,
            "target_questions_total": len(in_scope),
            "target_questions_yes": sum(1 for q in in_scope if values.get(q.id)),
        },
        "areas": areas,
        "next_actions": actions,
    }


# ---------------------------------------------------------------- rendering


def _gap_text(gap: int) -> str:
    if gap == 0:
        return "Met"
    return f"{gap} level" + ("s" if gap > 1 else "")


def _percent(part: int, whole: int) -> str:
    return f"{round(100 * part / whole)}%" if whole else "0%"


def render_markdown(result: dict[str, Any], bank: Bank, link_base: str = "") -> str:
    by_id = bank.by_id()
    s = result["summary"]
    titles = {a["id"]: a["title"] for a in result["areas"]}
    profile = PROFILE_LABEL[result["profile"]]
    overlays = ", ".join(OVERLAY_LABEL[o] for o in result["overlays"]) or "none"
    target = LEVEL_LABEL[result["target"]]

    def link(path: str) -> str:
        return f"[{path}]({link_base}{path})"

    skipped = result.get("skipped_areas", [])
    if skipped:
        scope = f"{target} in the {s['areas_total']} areas this profile assesses."
    else:
        scope = f"{target} in every area."
    out: list[str] = [
        "# Maturity report",
        "",
        f"Profile: {profile}. Overlays: {overlays}. Target: {scope}",
    ]
    if skipped:
        out.append(
            f"Not assessed for this profile: {', '.join(a['title'] for a in skipped)}. "
            f"See {link(PROFILE_PAGE.format(profile=result['profile']))} for when to add them."
        )
    if result["overlays"] and not result.get("overlays_raise_target", True):
        out.append(
            f"Overlays do not raise the target for the {profile} profile. "
            "Use the short section for this profile on each overlay page instead."
        )
    out += [
        "",
        "## Summary",
        "",
        f"- Areas at or above target: {s['areas_at_target']} of {s['areas_total']}.",
        f"- Lowest level reached: {LEVEL_LABEL[s['lowest_level']]} "
        f"({', '.join(titles[a] for a in s['lowest_areas'])}).",
        f"- Questions answered yes, up to the target level: {s['target_questions_yes']} of "
        f"{s['target_questions_total']} ({_percent(s['target_questions_yes'], s['target_questions_total'])}).",
        f"- Questions answered yes, all levels: {s['questions_yes']} of {s['questions_total']} "
        f"({_percent(s['questions_yes'], s['questions_total'])}).",
        "",
        "## Areas",
        "",
        "| Area | Reached | Target | Gap | Yes |",
        "|---|---|---|---|---|",
    ]
    for a in result["areas"]:
        out.append(
            f"| {a['title']} | {LEVEL_LABEL[a['reached']]} | {LEVEL_LABEL[a['target']]} "
            f"| {_gap_text(a['gap'])} | {a['yes']} of {a['total']} |"
        )

    actions = result["next_actions"]
    out += ["", f"## Next {len(actions)} actions" if actions else "## Next actions", ""]
    if not actions:
        out.append("Every question is answered yes. Check the evidence, then tune the targets in your fork.")
    for i, act in enumerate(actions, start=1):
        stretch = " Beyond your target level." if act["beyond_target"] else ""
        out.append(
            f"{i}. **{act['area_title']}, {LEVEL_LABEL[act['level']]}.** {act['action']}{stretch} "
            f"See {link(act['link'])}."
        )

    out += ["", "## Open questions by area", ""]
    any_open = False
    for a in result["areas"]:
        if not a["open"]:
            continue
        any_open = True
        out += [f"### {a['title']}", ""]
        for qid in a["open"]:
            q = by_id[qid]
            out.append(f"- {LEVEL_LABEL[q.level]}: {q.text} (`{q.id}`, {link(q.link)})")
        out.append("")
    if not any_open:
        out += ["None.", ""]
    return "\n".join(out).rstrip() + "\n"


def render_json(result: dict[str, Any]) -> str:
    return json.dumps(result, indent=2) + "\n"


def render_init(bank: Bank, profile: str = "startup") -> str:
    if profile not in PROFILE_TARGET:
        raise AssessError(f"unknown profile {profile!r}; allowed: {', '.join(PROFILE_TARGET)}")
    out = [
        "# Maturity assessment answers for the Open Engineering Playbook.",
        "# Set an answer to true only when you can point to the evidence.",
        "# Commit this file and repeat the assessment every quarter.",
        "",
        "# One of: " + ", ".join(PROFILE_TARGET) + ".",
        "# The questions below are the ones this profile is asked. If you change",
        "# the profile, run --init again or score with --allow-missing.",
        f'profile = "{profile}"',
        "# Add " + " and/or ".join(f'"{o}"' for o in OVERLAYS) + " when they apply.",
        "overlays = []",
    ]
    skipped = [a.title for a in bank.areas if a not in bank.areas_for(profile)]
    if skipped:
        out.append(f"# Not assessed for the {PROFILE_LABEL[profile]} profile: {', '.join(skipped)}.")
    out += ["", "[answers]"]
    for area in bank.areas_for(profile):
        out += ["", f"# {area.title}"]
        for q in bank.in_area(area.id, profile):
            out.append(f"# [{q.level}] {q.text}")
            out.append(f'"{q.id}" = false')
    return "\n".join(out) + "\n"


# ---------------------------------------------------------------------- cli


def _write(text: str, output: Path | None, force: bool = True) -> None:
    if output is None:
        sys.stdout.write(text)
        return
    if output.exists() and not force:
        raise AssessError(f"{output} already exists; pass --force to replace it")
    output.write_text(text, encoding="utf-8")
    print(f"Wrote {output}", file=sys.stderr)


def _inside(path: Path, root: Path) -> bool:
    try:
        path.resolve().relative_to(root)
        return True
    except ValueError:
        return False


def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(
        description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter
    )
    p.add_argument("--questions", type=Path, default=DEFAULT_QUESTIONS, help="question bank (TOML)")
    p.add_argument("--answers", type=Path, help="your answers file (TOML)")
    p.add_argument("--format", choices=("markdown", "json"), default="markdown")
    p.add_argument("--output", type=Path, help="write here instead of standard output")
    p.add_argument("--init", action="store_true", help="write a blank answers file and exit")
    p.add_argument("--profile", default="startup", help="profile for --init (default: startup)")
    p.add_argument("--force", action="store_true", help="let --init replace an existing --output file")
    p.add_argument("--allow-missing", action="store_true", help="count unanswered questions as false")
    p.add_argument("--actions", type=int, default=DEFAULT_ACTIONS, help="how many next actions to list")
    p.add_argument(
        "--link-base",
        default=None,
        help="prefix for playbook links, for example a repository URL ending in /. "
        "Default: none when the answers file is inside this repository, the public "
        "repository URL when it is not",
    )
    p.add_argument("--check", action="store_true", help="exit 1 when any area is below its target")
    return p


def main(argv: list[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    try:
        bank = load_bank(args.questions)
        if args.init:
            _write(render_init(bank, args.profile), args.output, force=args.force)
            return 0
        if args.answers is None:
            raise AssessError("pass --answers FILE, or --init to create one")
        answers = load_answers(args.answers, bank, args.allow_missing)
        result = assess(bank, answers, args.actions)
        if args.format == "json":
            text = render_json(result)
        else:
            link_base = args.link_base
            if link_base is None:
                link_base = "" if _inside(args.answers, REPO_ROOT) else PUBLIC_LINK_BASE
            text = render_markdown(result, bank, link_base)
        _write(text, args.output)
    except AssessError as exc:
        print(f"error: {exc}", file=sys.stderr)
        return 2
    if args.check and result["summary"]["areas_at_target"] < result["summary"]["areas_total"]:
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
