#!/usr/bin/env python3
"""Plain-language check for the Open Engineering Playbook and for any repository that adopts it.

Fails when a text file contains:
  * an em dash (U+2014) or en dash (U+2013)
  * a phrase listed in tools/plain-language.txt
  * an emoji in a Markdown file

Usage:
  python3 tools/plain_lint.py [PATH ...]

With no paths it scans the current directory. Exit code 1 means findings.
Standard library only, Python 3.9 or later.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Iterable, Iterator, List, Sequence

TEXT_SUFFIXES = {".md", ".yml", ".yaml", ".toml", ".txt", ".json", ".sh", ".py", ".csv", ".tf"}
SKIP_DIRS = {".git", "node_modules", ".venv", "venv", "__pycache__", "dist", "build", ".terraform"}
DEFAULT_WORDLIST = Path(__file__).with_name("plain-language.txt")

DASHES = {"—": "em dash", "–": "en dash"}
# Common emoji blocks. Not exhaustive, but catches what people actually paste.
EMOJI = re.compile(
    "[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F000-\U0001F2FF\U0001F900-\U0001F9FF]"
)


@dataclass(frozen=True)
class Finding:
    path: Path
    line: int
    column: int
    message: str

    def __str__(self) -> str:
        return f"{self.path}:{self.line}:{self.column}: {self.message}"


def load_phrases(wordlist: Path) -> List[str]:
    phrases = []
    for raw in wordlist.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        if line and not line.startswith("#"):
            phrases.append(line.lower())
    return phrases


def compile_phrases(phrases: Sequence[str]) -> List[re.Pattern]:
    # \b does not work next to apostrophes or hyphens in the way we want,
    # so build explicit non-word lookarounds.
    return [
        re.compile(r"(?<![\w-])" + re.escape(p) + r"(?![\w-])", re.IGNORECASE)
        for p in phrases
    ]


IGNORE_FILE_MARKER = "plain-lint: ignore-file"


def check_text(path: Path, text: str, patterns: Sequence[re.Pattern]) -> Iterator[Finding]:
    # A file can opt out in its first five lines, for pages that must quote
    # the banned words (the style guide itself, for example).
    if any(IGNORE_FILE_MARKER in line for line in text.splitlines()[:5]):
        return
    is_markdown = path.suffix == ".md"
    for lineno, line in enumerate(text.splitlines(), start=1):
        for ch, name in DASHES.items():
            col = line.find(ch)
            if col >= 0:
                yield Finding(path, lineno, col + 1, f"{name}: use a comma, colon, full stop or 'to'")
        for pat in patterns:
            m = pat.search(line)
            if m:
                yield Finding(path, lineno, m.start() + 1, f"avoid '{m.group(0)}': see STYLE.md")
        if is_markdown:
            m = EMOJI.search(line)
            if m:
                yield Finding(path, lineno, m.start() + 1, "emoji in Markdown")


def iter_files(paths: Iterable[Path], exclude: Sequence[Path]) -> Iterator[Path]:
    excluded = {p.resolve() for p in exclude}
    for root in paths:
        if root.is_file():
            if root.resolve() not in excluded:
                yield root
            continue
        for dirpath, dirnames, filenames in os.walk(root):
            dirnames[:] = [d for d in dirnames if d not in SKIP_DIRS]
            for name in filenames:
                p = Path(dirpath) / name
                if p.suffix in TEXT_SUFFIXES and p.resolve() not in excluded:
                    yield p


def run(paths: Sequence[Path], wordlist: Path) -> List[Finding]:
    patterns = compile_phrases(load_phrases(wordlist))
    findings: List[Finding] = []
    # The word list and this script necessarily contain the words they ban.
    exclude = [wordlist, Path(__file__)]
    for f in iter_files(paths, exclude):
        try:
            text = f.read_text(encoding="utf-8")
        except (UnicodeDecodeError, OSError):
            continue
        findings.extend(check_text(f, text, patterns))
    return findings


def main(argv: Sequence[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument("paths", nargs="*", type=Path, default=[Path(".")])
    parser.add_argument("--wordlist", type=Path, default=DEFAULT_WORDLIST)
    args = parser.parse_args(argv)

    missing = [p for p in args.paths if not p.exists()]
    if missing:
        for p in missing:
            print(f"{p}: no such file or directory", file=sys.stderr)
        return 2

    findings = run(args.paths, args.wordlist)
    for f in findings:
        print(f)
    if findings:
        print(f"\n{len(findings)} finding(s). See STYLE.md.", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
