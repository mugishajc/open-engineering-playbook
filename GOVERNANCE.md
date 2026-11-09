# Governance

The Open Engineering Playbook is maintained in the open. This page says who decides what and how the playbook changes.

## Roles

- **Maintainers** review and merge changes, cut releases and keep the plain-language check green. The current maintainer list is in [MAINTAINERS](#maintainers) below.
- **Contributors** are anyone who opens an issue or a pull request.
- **Area reviewers** are contributors with deep experience in one area (for example security or public sector) who are asked to review changes there. Any maintainer can invite one.

## How the playbook changes

| Change | Process |
|---|---|
| Typo, broken link, clearer wording | Pull request, one maintainer approval |
| New template or a new section in an existing page | Pull request, one maintainer approval, CI green |
| New page, a changed recommendation, or a changed target number | Pull request with a short rationale and at least one primary source. Open for comment for 7 days. Two approvals. |
| Change to the principles, levels or profiles | An RFC in an issue using [the RFC template](templates/docs/rfc.md). Open for 14 days. Maintainer consensus. |

Until there are two maintainers, the second approval comes from an area reviewer for the area the change touches, and "maintainer consensus" means the maintainer plus at least one area reviewer, with the RFC left open for the full 14 days.

Recommendations need evidence. "We did this at my company" is welcome as context, but a change to a default needs a source someone else can check.

## Releases

The playbook uses calendar versions (`YYYY.MM`). A further release in the same month adds a number: `2026.11.1`. Each release has a changelog entry listing pages added, removed, or whose recommendation changed. Adopters can pin a release and diff against the next one.

## Neutrality

The playbook names tools as examples, never as requirements. Every practice must be achievable with open source tools that run on-premises. Vendors may contribute, but a page cannot depend on a single commercial product.

## Continuity

A playbook that one person keeps alive is a key-person risk, the same risk the [skills gap](playbook/people/skills-gap.md) page asks you to fix.

- **Target.** At least 3 maintainers from at least 2 organisations. Until then, area reviewers cover the second approval.
- **Becoming a maintainer.** Ask in an issue after several merged contributions. The maintainers decide within 30 days and say why.
- **If the maintainers stop.** If no maintainer merges a pull request or answers an issue for 6 months, any area reviewer may open an issue to take over. The licences let anyone fork and keep the work going at any time.
- **Pinning.** Every release is tagged, so adopters can keep using a version whatever happens to the project.

## Maintainers

- Mugisha Jean Claude ([@mugishajc](https://github.com/mugishajc))
