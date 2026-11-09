# Exploratory testing charter and session notes

<!--
How to use: write the charter before the session. Run one session of 60 to 90 minutes against it,
uninterrupted, alone or in a pair. Take notes as you go. Hold a 10 to 15 minute debrief with the
developer or the team straight after. Turn each defect that could recur into an automated test.
Charter form from Elisabeth Hendrickson, Explore It! (2013).
Guidance: playbook/quality/exploratory-and-acceptance-testing.md
-->

## Charter

Explore **[target: feature, flow or area]**
with **[resources: data, roles, devices, tools, assistive technology, network conditions]**
to discover **[information: the risk or question this session answers]**.

Example: Explore the refund flow with two staff accounts in two browsers on the same order to discover what happens when two people refund at once.

| Field | Value |
|---|---|
| Linked risk (from the test strategy) | [R-number, score] |
| Tester(s) | [names] |
| Date and start time | [YYYY-MM-DD HH:MM] |
| Time box | [60 / 90 minutes] |
| Build and environment | [version, environment] |

## Prompts (pick the ones that fit)

- Variables: what can change here, and what happens at its limits?
- Data: zero, one, many, maximum; apostrophes, non-Latin scripts, very long input; leap day, time zone, rounding.
- Interruptions: back, refresh, double submit, network drop, timeout.
- State: illegal moves, cancel halfway, resume later, undo.
- Concurrency: two users or tabs on the same record.
- People: first-time user, expert in a hurry, wrong role, screen reader, low-cost phone on a slow network.
- Integrations: third party slow, down, or returning something odd.
- Past incidents in this area.

## Session notes

| Time | What I tried | What happened | Follow-up |
|---|---|---|---|
| | | | |

## Defects

| ID | Summary | Severity | Steps to reproduce (short) | Automated test possible (Yes/No) |
|---|---|---|---|---|
| | | | | |

## Questions and issues

Things that are not defects but need an answer, and anything that blocked testing (environment, data, access).

- [ ]

## Debrief

| Item | Notes |
|---|---|
| Covered | [what the session reached] |
| Not covered | [what it did not, and why] |
| Found | [defects, surprises, risks] |
| Blocked by | [obstacles] |
| Next | [charters for follow-up sessions] |
| Time split (rough %) | Testing ___ / Investigating defects ___ / Setup and obstacles ___ |
