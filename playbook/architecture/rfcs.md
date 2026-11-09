# RFCs and design documents

Write a request for comments (RFC) before building anything large, cross-team or hard to undo. The RFC puts the design in front of everyone it affects while changing it still costs a document edit rather than a rewrite. Every RFC ends in a recorded decision by a named person, and the decisions it produces are kept as [decision records](decision-records.md).

## Outcomes

Starting points. Tune them to your organisation.

- Median time from "open for comment" to decision is 15 working days or less.
- 100% of RFCs end in a recorded state: Accepted, Rejected or Withdrawn. None sit in Draft for more than 30 days without an update.
- Every accepted RFC links to its implementation work and to the ADRs it produced.
- At least 80% of RFCs that affect other teams receive written comments from those teams before the decision.

## RFC, ADR or neither

| Situation | Write |
|---|---|
| Change stays inside one team and can be undone within one sprint | Nothing beyond the pull request description |
| One decision with a few options, affecting one or two teams | An [ADR](decision-records.md) |
| New system, major redesign, or more than about 4 engineer-weeks of work | An RFC, then ADRs for its decisions |
| New public or partner API, or a breaking change to one | An RFC that includes the API description (see [API standards](api-standards.md)) |
| Change to authentication, cryptography, personal data handling or data residency | An RFC with a [threat model](../../templates/docs/threat-model.md) |
| Change to a shared platform or golden path that every team will feel | An RFC |

The RFC holds the proposal and the discussion. The ADR holds the decision in a short, durable form. An accepted RFC usually yields 1 to 5 ADRs. Each ADR links back to the RFC for the full analysis.

## What public processes teach

Large open source projects have run written proposal processes for years, in public. Three are worth reading before you design your own.

| Process | What to copy |
|---|---|
| Rust RFCs | Proposals are pull requests to one repository. A team member proposes a final comment period, the team signs off, and the period gives late objectors a last, time-boxed chance. |
| Kubernetes Enhancement Proposals (KEPs) | Each proposal has an owning group, tracks stages (alpha, beta, stable) and must pass a production readiness review before it graduates. |
| Python Enhancement Proposals (PEPs), PEP 1 | Clear statuses (Draft, Accepted, Rejected, Withdrawn, Deferred, Final, Superseded) and a single named decision-maker or delegate for each proposal. |

The common lessons: one numbered document per change, stored in version control, a fixed comment window, a named decider, and a recorded outcome even when the answer is no.

## Lifecycle

| Stage | What happens | Time box (starting point) |
|---|---|---|
| Draft | Author writes the RFC with 1 or 2 early readers. Not yet open to everyone. | Up to 30 days |
| Open for comment | Pull request is announced to affected teams. Anyone may comment inline. | 10 working days (5 for a Startup) |
| Final comment period | Approver states the intended decision. Last objections only. | 5 working days |
| Accepted, Rejected or Withdrawn | Approver records the decision and the reasons in the RFC. Merge it either way. | Same day |
| Implemented or Superseded | Status updated when the work ships or a later RFC replaces it. | When it happens |

The author answers every comment in writing: changed, declined with a reason, or deferred to a named follow-up. Discussions held in meetings get a short written summary in the RFC within 1 working day, or they did not happen.

## Who approves

- The approver is named in the RFC header before it opens for comment. Use [decision rights](../operating-model/decision-rights.md) to pick them.
- Default: the lead of the owning team, plus the lead of each team that must change its own systems.
- Cross-organisation changes: the architecture forum or the head of engineering. See [architecture practice](architecture-practice.md) for review triggers.
- Security, privacy or compliance impact: add the security lead as a required approver.
- Approval means "we accept this design and its costs". It does not need everyone to agree. People who disagree say so in writing, and the decision stands.

## Practice

### Foundation

- Keep RFCs in `docs/rfcs/NNNN-short-title.md` in the main repository, or skip RFCs entirely if you are one team and ADRs cover your decisions.
- Use the [RFC template](../../templates/docs/rfc.md). Fill in Problem, Goals and non-goals, Proposal, Alternatives (always including "do nothing") and Rollout.
- Comment period: 5 working days. The tech lead decides.

### Standard

- One RFC repository for the whole engineering organisation, with a sequence number and an index generated in CI.
- Announce each RFC that opens for comment in one agreed channel, with the closing date.
- Required sections add Security and privacy, Operability (SLOs, alerts, on-call impact, see [service levels](../reliability/service-levels.md)), Cost and Migration.
- A weekly 30-minute slot exists for RFCs that need live discussion. It is optional, not a gate.
- Track open RFCs and their age. Escalate any RFC past its time box to the approver's manager.

### Assured

- Approvals are recorded as pull request approvals by the named approvers. The author is never the only approver.
- RFCs that change systems in scope for audit include a threat model, a data protection impact note where personal data is involved, and a [production readiness](../reliability/production-readiness.md) section.
- Link each accepted RFC to the change record when the implementation is deployed (see [change management](../reliability/change-management.md)).
- Keep the full comment history. In git-based tools this means keeping the merged pull request and its review threads, so export them to the archive if the tool can purge them.

## Cloud, on-premises and air-gapped

- RFCs are plain text in git, so the process is the same everywhere. Host the RFC repository on the same internal git server as the code.
- On classified or isolated networks, write the RFC on the network where the system lives. If people outside the enclave must comment, share a reviewed summary that leaves out sensitive detail, and record which version they saw.
- Vendors and integrators often cannot reach the internal git server. Export the RFC for them, collect comments by email or document, and paste them into the pull request so the record stays complete.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| RFC written after the code, as approval theatre | Code that needs an RFC does not merge until the RFC is accepted. |
| Comment period that never ends | Fixed time boxes. The approver decides on the last day with the information available. |
| Design by committee | One named approver. Consensus is welcome, not required. |
| RFC for small, reversible changes | Use the table above. Most changes need an ADR or nothing. |
| No non-goals | Reviewers ask for non-goals first. Most scope arguments come from missing ones. |
| Decisions made in a meeting and never written down | Written summary in the RFC within 1 working day. |

## Templates

- [RFC template](../../templates/docs/rfc.md)
- [ADR template](../../templates/docs/adr.md)
- [Threat model](../../templates/docs/threat-model.md)
- [Production readiness review](../../templates/docs/production-readiness-review.md)

## Sources

- Rust RFC process: https://github.com/rust-lang/rfcs
- Kubernetes Enhancement Proposals: https://github.com/kubernetes/enhancements
- PEP 1, PEP Purpose and Guidelines: https://peps.python.org/pep-0001/
- Michael Nygard, "Documenting Architecture Decisions" (2011): https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
