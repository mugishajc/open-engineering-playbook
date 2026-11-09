# Decision records

Write a short architecture decision record (ADR) for every decision that is expensive to reverse, and keep it in the repository next to the code it shapes. An ADR captures the context, the choice and its consequences on one or two pages. It lets a new engineer, a successor or an auditor learn why the system looks the way it does without finding the person who decided.

## Outcomes

Starting points. Tune them to your organisation.

- Every decision that passes the test below has an accepted ADR within 5 working days of the decision.
- A new engineer finds the ADR behind any major component in under 5 minutes.
- 100% of ADRs carry a status and a date. Every superseded ADR links to its replacement.
- At Standard and above, every accepted ADR older than 24 months has a recorded review.

## When to write one

Write an ADR when a decision meets at least one of these tests.

| Test | Examples |
|---|---|
| Undoing it would take more than about 2 engineer-weeks | Database engine, message broker, primary language for a service family |
| It affects more than one team or service | Shared event schema, API versioning scheme, tenancy model |
| It adds an external dependency, vendor or hosting model | Managed database, SaaS identity provider, move from cloud to on-premises |
| It departs from a golden path, a playbook default or a radar ring | Running a service outside the platform, using a Hold technology |
| It has security, privacy or compliance impact | Data residency region, who holds encryption keys, logging of personal data |
| It accepts a known risk | Single region for a critical service, skipping a control for a deadline |

Do not write ADRs for formatting, naming, patch upgrades or anything a linter or a standard already decides. Too many trivial records bury the ones that matter.

## Format

Two formats are in common use. Both work.

| Format | Sections | Use when |
|---|---|---|
| Michael Nygard (2011) | Title, Status, Context, Decision, Consequences | Most decisions. One page. |
| MADR 4.0 | Front matter (status, date, decision-makers, consulted, informed), Context and Problem Statement, Decision Drivers, Considered Options, Decision Outcome, Consequences, Confirmation, Pros and Cons of the Options | Decisions with several real options, or where an auditor will read it |

The playbook's [ADR template](../../templates/docs/adr.md) follows MADR 4.0 and marks the optional sections, so a Foundation team can fill in the Nygard core in 20 minutes.

Write the consequences honestly. A record that lists only benefits is a sales pitch, not a decision record. Name what gets harder, what it costs and what you will watch.

## Statuses

| Status | Meaning |
|---|---|
| Proposed | Open for review. Not yet binding. |
| Accepted | Binding. Implementations follow it. |
| Rejected | Considered and declined. Keep it: it stops the same idea coming back every year without new facts. |
| Deprecated | No longer applies, and nothing replaces it (the component was removed). |
| Superseded by ADR-NNNN | A newer ADR replaces it. Link both ways. |

Once an ADR is accepted, do not edit its decision or context. Change only the status line and the links. To change the decision, write a new ADR that supersedes the old one. The history of how thinking changed is part of the value.

## Practice

### Foundation

- Create `docs/decisions/` in each repository. Name files `NNNN-short-title.md` with a four-digit sequence number, for example `0007-use-postgresql.md`.
- Copy the [ADR template](../../templates/docs/adr.md) as `0000-template.md` so authors start from it.
- Open the ADR in a pull request. It gets the same review as code: at least one reviewer who did not write it.
- Merge the ADR with status Accepted before, or in the same pull request as, the first code that depends on it.
- Link the ADR from the README section that describes the affected component.

### Standard

- Decision-makers for each type of decision come from [decision rights](../operating-model/decision-rights.md). The ADR names them in its front matter.
- Decisions that span teams live in one central decisions repository (or in the platform repository) with its own sequence. Service repositories link to them.
- Generate an index of all ADRs (title, status, date, owner) in CI and publish it with the internal docs. Tools such as `adr-tools` or a 30-line script both work.
- When a pull request implements an ADR, the description links it. Reviewers check that the code matches the decision.
- An architecture forum reviews cross-team ADRs once a week (see [architecture practice](architecture-practice.md) for how the forum works). The target is a decision within 10 working days of the ADR being proposed.
- Review accepted ADRs older than 24 months. Mark each one "still valid", "superseded" or "deprecated", with reviewer and date. Review any ADR named as a contributing factor in a [postmortem](../reliability/postmortems.md) within 30 days of that postmortem.

### Assured

- Approval is recorded through pull request approvals from named decision-makers. The author cannot be the only approver.
- ADRs that accept risk cite the risk register entry and the risk owner. See the [risk register template](../../templates/strategy/risk-register.csv).
- ADRs that touch personal data, authentication, cryptography or data residency carry a security and privacy sign-off and link the [threat model](../../templates/docs/threat-model.md).
- Retain ADRs for the life of the system plus the period your records policy requires. Because they live in git, retention means keeping the repository and its history, not exporting PDFs.
- Map ADRs to controls in [control mapping](../compliance/control-mapping.md). They are direct evidence for ISO/IEC 27001:2022 Annex A 8.27 (secure system architecture and engineering principles) and support 8.32 (change management).

## Cloud, on-premises and air-gapped

ADRs are Markdown files in git, so the practice is identical everywhere. Two things change on isolated networks.

- Readers cannot follow internet links. Copy the key parts of external documents (vendor limits, standard clauses, benchmark results) into the ADR or into an internal docs store, and record the version and retrieval date.
- Record the hosting model itself as an ADR: why this workload runs on public cloud, on-premises or air-gapped, and what would make you move it. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| ADRs written months later to justify a choice already made | Merge the ADR before or with the first dependent code. Reviewers block code that needs an ADR and has none. |
| ADRs kept in a wiki that drifts away from the code | Store them in the repository. Link from the wiki if people search there. |
| Ten-page ADRs | Move the analysis to an [RFC](rfcs.md). The ADR states the decision and links the RFC. |
| Editing an accepted ADR to match what was built | Write a superseding ADR. The gap between plan and reality is useful information. |
| A record for every small choice | Apply the test above. If nobody would ask "why?" in a year, skip it. |
| Consequences section lists only benefits | Reviewers reject ADRs without at least one cost or risk. |

## Templates

- [ADR template (MADR 4.0)](../../templates/docs/adr.md)
- [RFC template](../../templates/docs/rfc.md), for decisions that need wider discussion first
- [Threat model](../../templates/docs/threat-model.md), for security-relevant decisions

## Sources

- Michael Nygard, "Documenting Architecture Decisions" (2011): https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- MADR, Markdown Any Decision Records, version 4.0: https://adr.github.io/madr/
- Architecture decision record community site and tooling list: https://adr.github.io/
- ISO/IEC 27001:2022, Information security management systems: https://www.iso.org/standard/27001
