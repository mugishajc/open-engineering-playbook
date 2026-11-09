# Contributing

Thank you for helping. The playbook gets better when people who run real systems tell us what works.

## Good first contributions

- A template you already use that is missing here
- An on-premises or air-gapped detail for a practice
- A primary source for a claim that lacks one
- A clearer sentence

## Before you open a pull request

1. Read [STYLE.md](STYLE.md). Every page follows the same layout and the same writing rules.
2. Run the checks:

   ```bash
   python3 tools/plain_lint.py
   python3 -m unittest discover -s assessment/tests
   python3 -m unittest discover -s tools/tests
   ```

3. Keep the pull request small. One page or one template per pull request is ideal.
4. If you change a recommendation or a target number, add the source and say why in the description.

## Commit messages

Use [Conventional Commits](https://www.conventionalcommits.org/en/v1.0.0/): `docs(delivery): add review turnaround target`, `feat(templates): add GitLab release job`, `fix(assessment): handle empty answers file`.

## What we will not merge

- Pages that require a specific commercial product
- Claims without a source someone else can check
- Marketing copy
- Text that fails the plain-language check

See [GOVERNANCE.md](GOVERNANCE.md) for how decisions are made and [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for how we treat each other.
