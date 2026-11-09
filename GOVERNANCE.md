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

Recommendations need evidence. "We did this at my company" is welcome as context, but a change to a default needs a source someone else can check.

## Releases

The playbook uses calendar versions (`YYYY.MM`). Each release has a changelog entry listing pages added, removed, or whose recommendation changed. Adopters can pin a release and diff against the next one.

## Neutrality

The playbook names tools as examples, never as requirements. Every practice must be achievable with open source tools that run on-premises. Vendors may contribute, but a page cannot depend on a single commercial product.

## Maintainers

- Mugisha Jean Claude ([@mugishajc](https://github.com/mugishajc))
