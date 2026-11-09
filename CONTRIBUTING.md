# Contributing

Thank you for helping. The playbook gets better when people who run real systems tell us what works.

## Good first contributions

- A template you already use that is missing here
- An on-premises or air-gapped detail for a practice
- A primary source for a claim that lacks one
- A clearer sentence

## Before you open a pull request

1. Read [STYLE.md](STYLE.md). Every page follows the same layout and the same writing rules.
2. Run the checks. They need Python 3.11 or later (`python3 --version`; use `python3.12` or `py -3` on Windows if `python3` is older):

   ```bash
   python3 tools/plain_lint.py
   python3 tools/check_structure.py
   python3 exercises/quiz.py --check
   python3 -m unittest discover -s assessment/tests
   python3 -m unittest discover -s tools/tests
   python3 -m unittest discover -s exercises/tests
   ```

   If you edit `exercises/true-or-false/questions.toml`, run `python3 exercises/quiz.py --export` before `--check`.

3. Keep the pull request small. One page or one template per pull request is ideal.
4. If you change a recommendation or a target number, add the source and say why in the description.

## Translations

Many readers use English as a second language, so translations help more than new English pages. Start with the pages owners and officials read first: [for small and medium businesses](leaders/for-small-and-medium-businesses.md), [for business executives](leaders/for-business-executives.md), [for government](leaders/for-government.md), the [SME profile](profiles/sme.md) and the [glossary](GLOSSARY.md).

- Put a translated page next to the English one with a language suffix, for example `for-small-and-medium-businesses.fr.md`.
- Start the page with the release it was translated from, for example "Translated from 2026.11.1". When the English page changes, the next release lists translations to update.
- A second fluent speaker reviews each translation before it merges. Keep numbers, links and section order the same as the English page.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): `docs(delivery): add review turnaround target`, `feat(templates): add GitLab release job`, `fix(assessment): handle empty answers file`.

## What we will not merge

- Pages that require a specific commercial product
- Claims without a source someone else can check
- Marketing copy
- Text that fails the plain-language check

See [GOVERNANCE.md](GOVERNANCE.md) for how decisions are made and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for how we treat each other.
