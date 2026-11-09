# Contributing to PROJECT_NAME

Thank you for helping. This page tells you how to propose a change and what happens next. Replace `PROJECT_NAME`, team names and links with your own.

## Before you start

- For a bug, open an issue with the bug form so we can reproduce it.
- For a new feature or a large change, open an issue first and wait for a maintainer to agree on the approach. This saves you writing code we cannot merge.
- To report a security vulnerability, do not open an issue. Follow [SECURITY.md](SECURITY.md).

## Set up

```bash
git clone https://example.com/your-org/PROJECT_NAME.git
cd PROJECT_NAME
make setup        # install toolchain and dependencies
pre-commit install
make test         # should pass before you change anything
```

If `make setup` fails on a clean machine, that is a bug. Please report it.

## Make a change

1. Create a branch from `main`. Keep it short-lived: aim to merge within 2 days.
2. Keep the change small: aim for under about 400 changed lines. Split refactoring from behaviour change.
3. Add or update tests. A bug fix starts with a test that fails without the fix.
4. Run `make lint test` locally.
5. Open a pull request using the template. Fill in every section, or say why a section does not apply.

## Pull request titles

We squash merge, so the pull request title becomes the commit message on `main`. Titles follow [Conventional Commits 1.0.0](https://www.conventionalcommits.org/en/v1.0.0/), and CI checks them:

```
type(optional-scope): short description in the imperative
```

| Type | Use for | Version effect |
|---|---|---|
| `feat` | New behaviour for users | Minor |
| `fix` | Bug fix | Patch |
| `feat!` or `fix!` | Breaking change. Explain it in the description. | Major |
| `docs`, `test`, `refactor`, `perf`, `build`, `ci`, `chore`, `style`, `revert` | Everything else | None |

Before version 1.0.0, a breaking change bumps the minor version, not the major (the `bump-minor-pre-major` setting in `release-please-config.json`).

Examples: `feat(export): add CSV export`, `fix(auth): reject expired tokens`, `docs: explain local setup on Windows`.

## Review

- A code owner reviews every pull request. Expect a first response within one working day.
- Reviewers label comments: `blocking:`, `question:`, `suggestion:`, `nit:`, `praise:`, `follow-up:`. Only `blocking:` and unanswered `question:` comments stop a merge.
- Reply to every comment. Push fixes as new commits during review; they are squashed on merge.
- You own every line you submit, including code produced with tools or code assistants. Be ready to explain any line.

## Releases

Releases are automated. Merged changes appear in the next release pull request with a generated changelog. Maintainers merge the release pull request to publish.

## Code of conduct

Be respectful and specific. Comment on the code, not the person. Maintainers may remove comments or contributors that do not follow this.
