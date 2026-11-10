# Launch review

Review every new service and every major feature against a short checklist before it takes real traffic. Most launch-day incidents come from gaps that a one-hour review would have found: no runbook, no alerting, no rollback plan, no load test, no data classification. A launch review is not a gate to slow teams down. It is a fast check that the team has done the work they already know they should do.

Launch reviews are different from [change management](change-management.md), which covers individual changes to running systems. A launch review covers a new service or a large new capability end to end, before it goes live for the first time.

## Outcomes

Starting targets. Tune them after one quarter of data.

| Signal | Starting target |
|---|---|
| New services or major features launched without a completed review | Zero |
| Time from review request to review complete | Median under 3 working days |
| Launch-day incidents traceable to a gap the review checklist covers | Trending to zero |
| Review waivers granted | Tracked, reviewed quarterly, trending down |
| Post-launch issues discovered within 7 days that the checklist would have caught | Under 10% of launches |

## Practice

### Foundation

#### The checklist

Every launch review checks the same categories. The team fills in the checklist; the reviewer verifies it.

| Category | What to check |
|---|---|
| Ownership | Named owning team, on-call rotation, escalation path, responsible person for the service |
| SLOs | At least one availability and one latency SLO, with an error budget. See [SLOs](slos.md) |
| Monitoring | Dashboards for the four golden signals (latency, traffic, errors, saturation). See [observability](../architecture/observability.md) |
| Alerting | Alerts on SLO burn rate or error thresholds, paging the on-call, tested end to end |
| On-call | Rotation set up, at least 2 people, handoff documented, escalation path tested |
| Runbooks | At least: restart, rollback, data recovery, common failure modes. See [documentation](../people/documentation.md) |
| Rollback | Rollback tested in staging. Time to rollback measured. See [rollbacks](rollbacks.md) |
| Load testing | Tested at expected peak plus headroom (at least 2x). Capacity plan for the next 6 months. See [capacity planning](capacity-planning.md) |
| Security | Threat model reviewed, authentication and authorisation verified, secrets managed, dependencies scanned. See [secure development](../security/secure-development.md) |
| Data classification | Data the service stores or processes classified (public, internal, confidential, restricted). Retention and deletion policy set. See [data governance](../data/data-governance.md) |
| Dependencies | Upstream and downstream services identified. Failure modes for each dependency documented. Circuit breakers or fallbacks in place for critical paths |
| Backups and recovery | Backup schedule, tested restore, recovery time objective documented |

Use the [production readiness review template](../../templates/docs/production-readiness-review.md) as the starting point.

#### Tiered reviews

Not every launch needs the same depth. Match the review to the risk.

| Tier | What qualifies | Review format | Who reviews |
|---|---|---|---|
| 1 - Internal tool | Internal-only, not on the critical path, limited data | Self-review against the checklist, posted for the team to see | The owning engineer, reviewed by one peer |
| 2 - Team-facing service | Used by other teams, on a non-critical path, or stores internal data | Peer review meeting, 30 to 60 minutes | The owning team plus one engineer from a consuming team |
| 3 - Customer-facing or payment | Serves external users, handles payments, stores personal data, or is on the critical path | Formal review panel, 60 to 90 minutes | The owning team, SRE or platform team, security, and a senior engineer not on the team |

Default to Tier 2 when unsure. Promote to Tier 3 when the service handles money, personal data, or is in the critical path of a Tier 1 business process.

#### What blocks launch

A launch review results in one of three outcomes:

1. **Approved.** All checklist items are satisfied or have an accepted plan with a date.
2. **Approved with conditions.** Minor gaps exist (for example, a runbook for one failure mode is missing) with a plan to close them within 2 weeks. The team tracks the conditions and the reviewer follows up.
3. **Not approved.** A critical gap exists (no rollback plan, no alerting, no security review, no data classification for personal data). The team addresses the gap and requests a re-review. Re-reviews are fast because the reviewer already knows the service.

A reviewer cannot block a launch indefinitely. If the team and the reviewer disagree, the decision escalates to the engineering director or equivalent within 2 working days.

### Standard

#### Running the review

**Before the review:**
1. The team fills in the production readiness checklist at least 3 working days before the target launch date.
2. The team shares the completed checklist with the reviewer(s) and gives them 1 working day to read it.
3. The team books the review meeting (Tier 2 or 3) or posts the self-review (Tier 1).

**During the review:**
1. The team walks through each checklist category. For Tier 3, demonstrate the monitoring dashboard, the rollback procedure and at least one runbook.
2. The reviewer asks questions and checks evidence (links to dashboards, test results, security scan output, load test report).
3. Decisions are recorded in the review document, not in a separate channel.

**After the review:**
1. The review outcome (approved, approved with conditions, not approved) is recorded and linked to the service's entry in the service catalogue.
2. Conditions are tracked as tickets with owners and due dates.
3. The team launches.

#### Waivers

Sometimes a launch must happen before every checklist item is complete. A waiver records:

- Which items are incomplete.
- The risk of launching without them.
- Who accepted the risk (by name and role, not "the team").
- The date by which the items will be completed.
- What happens if the date is missed (the waiver expires and the service is reviewed again).

Track waivers. Review them quarterly. If the same item is waived repeatedly, the problem is in the process, not in the team. Either the item is not important (remove it) or teams need more support to complete it (provide tooling or templates).

#### Launch review as culture

The goal is a culture where teams want the review because it catches things they missed, not a culture where teams dread the review because it delays them.

- Keep reviews fast. A Tier 1 review takes 15 minutes. A Tier 2 takes under an hour. A Tier 3 takes under 90 minutes. If reviews routinely take longer, the checklist is too long or the team is not preparing.
- Celebrate good reviews. When a review catches a real gap that would have caused a launch-day incident, share the story (without blame) so other teams see the value.
- Make the checklist a living document. Add items when post-incident reviews show a gap the checklist missed. Remove items when they are always met and never catch anything.

### Assured

#### Launch review as a control

In regulated environments, launch reviews produce audit evidence.

- The completed checklist is retained for the records retention period.
- The reviewer's approval is a formal sign-off, recorded with the reviewer's name, role and date.
- Waivers require approval from a person at least one level above the team lead, and the risk acceptance is documented.
- Critical services (Tier 3) require a second review if the service design changes substantially after the initial review.
- The review checks regulatory requirements specific to the service: data residency, retention, access logging, encryption at rest and in transit, and any sector-specific obligations. See [regulated industries](../compliance/regulated-industries.md) and the [regional guides](../compliance/regions/).

This gives evidence for ISO/IEC 27001:2022 Annex A 8.29 (security testing in development and acceptance), SOC 2 CC8.1 (change management) and NIST SSDF PW.9 (configure the software to have secure settings by default). See [control mapping](../compliance/control-mapping.md).

## Cloud, on-premises and air-gapped

| Environment | Notes |
|---|---|
| Cloud | Load testing is straightforward (spin up synthetic traffic). Monitoring uses the cloud provider's tools or a SaaS observability platform. Security review includes IAM policies, network exposure and encryption configuration. |
| On-premises | Load testing may need dedicated hardware or a shared performance environment. Monitoring uses self-hosted tools (Prometheus, Grafana, Zabbix). Add physical infrastructure checks: rack capacity, power, cooling, network bandwidth. |
| Air-gapped | All dependencies must be available inside the network. Check that container images, packages and model weights are present and verified. Alerting must page through an internal system (no external paging service). Recovery procedures must work without internet access. |

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "It is just an internal tool" used to skip the review | Internal tools become critical. The billing system nobody outside finance uses is the most important system in the company on the last day of the month. Default to Tier 2 for all services. |
| Deadline pressure used to skip the review | The review takes 1 to 3 days. If the team cannot spare 3 days, they started too late. Build the review into the project plan from the start. |
| The review becomes a design review | The launch review checks readiness, not design. Design reviews happen earlier, in [RFCs](../architecture/rfcs.md) and design docs. If the reviewer questions the design at launch review, something went wrong upstream. |
| The same reviewer does every review and becomes a bottleneck | Spread reviewers across the SRE and platform teams. Any senior engineer can review a Tier 1 or Tier 2 service. |
| The checklist grows to 50 items and reviews take half a day | Keep the checklist under 15 categories. Each category is one question, not ten. Add detail in the linked pages, not in the checklist. |
| Reviews happen but nobody follows up on conditions | Track conditions as tickets. Alert the reviewer if a condition is overdue. Include condition closure rate in the quarterly review of the process. |

## Templates

- [Production readiness review](../../templates/docs/production-readiness-review.md)

## Sources

- Google SRE book, Chapter 32, Evolving SRE Engagement Model: https://sre.google/sre-book/evolving-sre-engagement-model/
- Google SRE workbook, Chapter 21, Managing Load: https://sre.google/workbook/managing-load/
- Google SRE book, Chapter 27, Reliable Product Launches at Scale: https://sre.google/sre-book/reliable-product-launches/
- Charity Majors, "I test in production": https://charity.wtf/
- Will Larson, An Elegant Puzzle, Chapter 5, Culture: https://lethain.com/elegant-puzzle/
