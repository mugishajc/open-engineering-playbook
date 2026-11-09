import importlib.util
import tempfile
import unittest
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
spec = importlib.util.spec_from_file_location("check_structure", ROOT / "tools" / "check_structure.py")
cs = importlib.util.module_from_spec(spec)
spec.loader.exec_module(cs)

GOOD_PRACTICE = """# Page

Do this, because that.

## Outcomes

- A measurable thing.

## Practice

### Foundation

Text.

### Standard

Text.

### Assured

Text.

## Cloud, on-premises and air-gapped

Text.

## Anti-patterns

Text.

## Templates

Text.

## Sources

Text.
"""

GOOD_LEADERS = """# Page

Do this.

## When to use this

Text.

## Common mistakes

Text.

## Templates

Text.

## Sources

Text.
"""


def write(text: str) -> Path:
    path = Path(tempfile.mkdtemp()) / "page.md"
    path.write_text(text, encoding="utf-8")
    return path


class PracticePages(unittest.TestCase):
    def test_complete_page_passes(self):
        self.assertEqual(cs.check_practice(write(GOOD_PRACTICE)), [])

    def test_missing_level_is_reported(self):
        page = GOOD_PRACTICE.replace("### Assured\n\nText.\n\n", "")
        self.assertIn("missing '### Assured' under Practice", cs.check_practice(write(page)))

    def test_missing_sources_is_reported(self):
        page = GOOD_PRACTICE.replace("## Sources\n\nText.\n", "")
        self.assertIn("missing '## Sources'", cs.check_practice(write(page)))

    def test_outcomes_must_come_first(self):
        page = GOOD_PRACTICE.replace("## Outcomes\n\n- A measurable thing.\n\n", "") + "\n## Outcomes\n\nText.\n"
        self.assertIn("'## Outcomes' must come before '## Practice'", cs.check_practice(write(page)))

    def test_headings_inside_code_blocks_are_ignored(self):
        page = "# Page\n\n```\n## Outcomes\n## Practice\n### Foundation\n```\n"
        problems = cs.check_practice(write(page))
        self.assertIn("missing '## Outcomes'", problems)

    def test_cloud_section_is_required(self):
        page = GOOD_PRACTICE.replace("## Cloud, on-premises and air-gapped\n\nText.\n\n", "")
        self.assertIn("missing the cloud, on-premises and air-gapped section", cs.check_practice(write(page)))


class LeadersPages(unittest.TestCase):
    def test_complete_page_passes(self):
        self.assertEqual(cs.check_leaders(write(GOOD_LEADERS)), [])

    def test_missing_common_mistakes_is_reported(self):
        page = GOOD_LEADERS.replace("## Common mistakes\n\nText.\n\n", "")
        self.assertIn("missing '## Common mistakes'", cs.check_leaders(write(page)))


class RepositoryPages(unittest.TestCase):
    def test_every_page_in_the_repository_follows_the_layout(self):
        self.assertEqual(cs.main([]), 0)


if __name__ == "__main__":
    unittest.main()
