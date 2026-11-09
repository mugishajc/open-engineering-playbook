#!/usr/bin/env python3
"""Check that every playbook and leaders page follows the layout in STYLE.md.

Playbook practice pages (playbook/<area>/<page>.md) must have, in order:
  # Title, an opening paragraph, ## Outcomes, ## Practice with
  ### Foundation, ### Standard and ### Assured, and ## Sources.
  A section on cloud, on-premises and air-gapped use, ## Anti-patterns and
  ## Templates are expected; a page may omit one only by keeping the heading
  and saying in one line why it does not apply.

Leaders pages (leaders/<page>.md, except README.md) must have:
  # Title, an opening paragraph, ## When to use this, ## Common mistakes,
  ## Templates and ## Sources.

Usage:
  python3 tools/check_structure.py [--warn-only]

Exit code 1 when a required section is missing. Standard library only.
"""
from __future__ import annotations

import argparse
import re
import sys
from pathlib import Path
from typing import List, Sequence

ROOT = Path(__file__).resolve().parent.parent

PRACTICE_REQUIRED = ["Outcomes", "Practice", "Sources"]
PRACTICE_LEVELS = ["Foundation", "Standard", "Assured"]
PRACTICE_EXPECTED = ["Anti-patterns", "Templates"]
LEADERS_REQUIRED = ["When to use this", "Common mistakes", "Templates", "Sources"]

H2 = re.compile(r"^## (.+?)\s*$")
H3 = re.compile(r"^### (.+?)\s*$")


def headings(text: str):
    """Return (h2 list, h3 list) ignoring fenced code blocks."""
    h2: List[str] = []
    h3: List[str] = []
    in_code = False
    for line in text.splitlines():
        if line.startswith("```"):
            in_code = not in_code
            continue
        if in_code:
            continue
        m = H2.match(line)
        if m:
            h2.append(m.group(1))
            continue
        m = H3.match(line)
        if m:
            h3.append(m.group(1))
    return h2, h3


def starts_with(names: Sequence[str], wanted: str) -> bool:
    return any(n.lower().startswith(wanted.lower()) for n in names)


def check_practice(path: Path) -> List[str]:
    text = path.read_text(encoding="utf-8")
    problems = []
    if not text.startswith("# "):
        problems.append("first line must be the page title (# Title)")
    h2, h3 = headings(text)
    for name in PRACTICE_REQUIRED:
        if not starts_with(h2, name):
            problems.append(f"missing '## {name}'")
    for level in PRACTICE_LEVELS:
        if not starts_with(h3, level):
            problems.append(f"missing '### {level}' under Practice")
    for name in PRACTICE_EXPECTED:
        if not starts_with(h2, name):
            problems.append(f"missing '## {name}' (keep the heading and say why it does not apply)")
    if not any(("on-prem" in n.lower() or "air-gap" in n.lower() or "cloud" in n.lower()) for n in h2):
        problems.append("missing the cloud, on-premises and air-gapped section")
    order = [n for n in h2 if any(n.lower().startswith(w.lower()) for w in ("Outcomes", "Practice"))]
    if len(order) >= 2 and not order[0].lower().startswith("outcomes"):
        problems.append("'## Outcomes' must come before '## Practice'")
    return problems


def check_leaders(path: Path) -> List[str]:
    text = path.read_text(encoding="utf-8")
    problems = []
    if not text.startswith("# "):
        problems.append("first line must be the page title (# Title)")
    h2, _ = headings(text)
    for name in LEADERS_REQUIRED:
        if not starts_with(h2, name):
            problems.append(f"missing '## {name}'")
    return problems


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("--warn-only", action="store_true", help="report but always exit 0")
    args = parser.parse_args(argv)

    failures = 0
    for path in sorted((ROOT / "playbook").glob("*/*.md")):
        for p in check_practice(path):
            print(f"{path.relative_to(ROOT)}: {p}")
            failures += 1
    for path in sorted((ROOT / "leaders").glob("*.md")):
        if path.name == "README.md":
            continue
        for p in check_leaders(path):
            print(f"{path.relative_to(ROOT)}: {p}")
            failures += 1
    if failures:
        print(f"\n{failures} layout problem(s). See STYLE.md.", file=sys.stderr)
        return 0 if args.warn_only else 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
