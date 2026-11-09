# Security policy

The playbook is mostly documentation, but it also ships scripts and CI templates that other organisations copy into their pipelines. A mistake in a template can spread.

## Reporting

If you find a template or script that would weaken the security of a repository that adopts it (for example an over-privileged workflow token, an unpinned action, or a script that can be tricked into overwriting files), report it privately through [GitHub private vulnerability reporting](https://github.com/mugishajc/open-engineering-playbook/security/advisories/new).

Please do not open a public issue for these.

## What to expect

- Acknowledgement within 3 working days
- A fix or a documented mitigation within 30 days for anything that affects adopters
- Credit in the release notes, unless you ask not to be named

## Scope

In scope: everything under `templates/`, `tools/` and `assessment/`, and any recommendation in `playbook/` that would lead an adopter to an insecure setup.

Out of scope: third-party actions, tools and services that the playbook links to. Report those to their maintainers.
