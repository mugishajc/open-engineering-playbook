# Status report: [project name], [date]

<!--
How to use: one page, every 2 weeks, plus an exception report as soon as any dimension turns red.
Set each colour by the rules below, never by feel. Pull the numbers from the work tracker, CI and
test results, finance and the RAID log. Send it to every level unchanged; add summaries, do not
rewrite. Square brackets mark your own data; never invent figures.
Guidance: playbook/project-management/status-reporting.md
-->

| Field | Value |
|---|---|
| Project manager | [name] |
| Sponsor | [name] |
| Reporting period | [YYYY-MM-DD to YYYY-MM-DD] |
| Baseline version | [v1, approved YYYY-MM-DD; earlier baselines listed in section 8] |
| Purpose of this report | [regular / exception] |

## 1. Summary

- **What changed since the last report:** [one sentence]
- **What worries me:** [one sentence]
- **What I need from the steering group:** [one sentence, or "nothing this period"]

## 2. Status and confidence

Rules. Green: the 85% forecast is inside tolerance and every risk above tolerance has a funded response. Amber: at risk of breaking tolerance, or a top risk has no response, and recovery is within the project manager's authority. Red: outside tolerance, or recovery needs a decision above the project manager. A dimension with no current evidence (data older than this period, or a test not yet run) is amber at best.

| Dimension | Status | Last report | Trend (better, same, worse) | Reason in one line |
|---|---|---|---|---|
| Date | | | | |
| Cost | | | | |
| Scope | | | | |
| Quality | | | | |
| Risk | | | | |
| Benefits | | | | |

**Overall delivery confidence:** [high / medium / low], trend [better / same / worse]. What would raise it: [...]

If any dimension went from green to red since the last report, say what signal was available earlier: [...]

## 3. Forecast

| | Baseline | Tolerance | 50% forecast | 85% forecast | Change since last report |
|---|---|---|---|---|---|
| Release or go-live date | [...] | [...] | [...] | [...] | [...] |
| Estimate at completion | [...] | [...] | [...] | [...] | [...] |

Forecast method: [Monte Carlo over the last [N] weeks of throughput / three-point estimates with reference class adjustment].

## 4. Contingency

| Contingency at baseline | Drawn to date | Remaining | Money exposure of open risks | Gap |
|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] |

Money exposure is the sum of probability (as a percentage) times money impact for each open risk, from the RAID log. Do not add up 1 to 5 scores. Management reserve (held by the sponsor): [...]; released to date: [...].

Draws this period, with RAID references: [...]

## 5. Scope and progress

- Must haves accepted: [x] of [y]
- Items added since baseline: [n]; removed: [n]
- Burn-up chart with the total scope line drawn: [link or image]

## 6. Quality and readiness

| Measure | This report | Data as of | Last report | Go/no-go criterion |
|---|---|---|---|
| Open severity 1 defects | | | | 0 |
| Open severity 2 defects | | | | [agreed limit] |
| Defects opened and fixed per week | | | | [fixed at least as fast as opened] |
| End-to-end tests passed (not only executed) | | | | [...] |
| Latest migration rehearsal reconciliation | | | | [100% for money; agreed rate for other records] |
| Performance test at peak plus margin | | | | [passed] |
| Cutover rehearsals completed and timed | | | | [2, inside the window] |
| Users trained | | | | [...] |

## 7. Top risks, issues and dependencies

From the risks, assumptions, issues and dependencies (RAID) log.

| ID | Title | Owner | Next action | Due | Trend |
|---|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] | [...] |

Full log: [link to the RAID log]

## 8. Decisions needed

| Decision | Options and consequences | Recommendation | Needed by | Cost of delay |
|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] |

## 9. Baseline history

| Version | Approved by | Date | Reason | Date and cost at that baseline |
|---|---|---|---|---|
| v1 | [...] | [...] | original | [...] |
