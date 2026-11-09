# Postmortem: <short title>

<!--
How to use: copy to postmortems/YYYY-MM-DD-short-title.md. Draft within 5 working days
of resolution; hold the review within 10 working days. Write it blameless: describe what
people knew and why their actions made sense at the time. Delete these comments when done.
Guidance: playbook/reliability/postmortems.md and playbook/reliability/root-cause-analysis.md
-->

| Field | Value |
|---|---|
| Incident ID | INC-YYYY-NNN |
| Severity | SEV1 / SEV2 / SEV3 / SEV4 or near miss |
| Status | Draft / In review / Final |
| Author | |
| Incident commander | |
| Review date | |
| Services affected | |
| Impact started (UTC) | YYYY-MM-DD HH:MM |
| Detected (UTC) and how | YYYY-MM-DD HH:MM; alert / customer / staff |
| Declared (UTC) | YYYY-MM-DD HH:MM |
| Mitigated (UTC) | YYYY-MM-DD HH:MM |
| Resolved (UTC) | YYYY-MM-DD HH:MM |
| Regulatory report needed? | No / Yes: which regime, deadline, owner |

## Summary

Three to five sentences a non-engineer can follow. What happened, who was affected, for how long, and what stopped it.

## Impact

Use numbers.

- Users or customers affected:
- Duration of user impact:
- Failed requests, transactions or jobs:
- Error budget spent (share of the 28-day budget):
- Data lost or exposed (records, classes of data):
- Financial, contractual or regulatory impact:
- Support tickets received:

## Timeline (UTC)

Start from the first signal, not the first page. Include decisions and who made them.

| Time | Event |
|---|---|
| HH:MM | Change X deployed to production |
| HH:MM | First error in logs (no alert) |
| HH:MM | Customer report received by support |
| HH:MM | Incident declared SEV2; IC: name |
| HH:MM | Rollback started |
| HH:MM | Error rate back to normal; mitigated |
| HH:MM | Resolved |

## Contributing factors

List every condition that made the incident possible, worse or longer. Usually 3 to 7. Tag each one.

| # | Factor | Phase | Tag |
|---|---|---|---|
| 1 | | Trigger / Detection / Response / Recovery | e.g. change-config, alerting-gap, runbook-gap, capacity, dependency, access, knowledge |
| 2 | | | |
| 3 | | | |

## How it made sense at the time

For each human decision that contributed: what did the person know, what were they trying to do, and what made the action look reasonable?

## What went well

-

## Where we got lucky

-

## Action items

Specific, testable, one owner each. Address classes of failure where possible ("all configuration pipelines"), not only this bug.

| # | Action | Factor # | Type | Priority | Owner | Due | Ticket |
|---|---|---|---|---|---|---|---|
| 1 | | | Detect / Mitigate / Prevent | P1 (2 weeks) / P2 (6 weeks) / P3 (next quarter) | | YYYY-MM-DD | |
| 2 | | | | | | | |

## Customer-facing summary (SEV1 and customer-visible SEV2)

What happened, impact, what we are changing. No internal names. No blame on suppliers.

## Appendix

- Incident channel or log:
- Dashboards and graphs (stored copies, not live links):
- Related changes (pull requests, deployments):
- Supplier incident reports:
