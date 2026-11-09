# Status reporting

A project that is green until two weeks before go-live and then red was never green: the bad news existed, and the reports hid it. Set red, amber and green by written rules that compare the forecast with the tolerance, not by how the project manager feels. Report dates and cost as ranges with a confidence level and a trend, build the numbers from team systems, and take every report to a steering group that exists to decide. People report what their sponsor rewards, so make an early red the safest thing anyone can say.

## Outcomes

Starting points. Tune them to your organisation.

- 100% of status reports set red, amber and green by the written rules below.
- Every date and cost in the report is a range with a confidence level, compared with the baseline and the tolerance, with a trend since the last report.
- At least 80% of the measures in the report come from systems of record (work tracker, continuous integration (CI) and test results, finance, the risks, assumptions, issues and dependencies (RAID) log), and each shows the date of its data.
- No project moves from green to red in one reporting period without a written note of what the earlier reports missed. Track the count across the portfolio; the target is zero unexplained jumps.
- A change is reported to the steering group as soon as an 85% date moves by more than two weeks, without waiting for the next report.
- Every steering meeting records its decisions. Pre-reads go out at least 2 working days before. Requested decisions are made in the meeting or within 5 working days.
- Producing the report takes the project manager under 1 hour each cycle.

## Why reports go green outside and red inside

| Cause | Fix |
|---|---|
| Red is punished, so people wait until they can no longer hide it | The sponsor thanks the first person to report red, and judges project managers on how accurate their reports were, not on how green |
| Status chosen by opinion | Red, amber and green set by written rules |
| Progress shown as percent complete of a task list | Accepted increments, a burn-up with the scope line, and a forecast range |
| The supplier's report passed on as your status | Reconcile it with your own data and independent tests before every meeting |
| Each management layer softens the report on its way up | One report goes to every level unchanged; summaries are added, not rewritten |
| Dates held until moving them is unavoidable | Report as soon as the 85% date moves by more than two weeks |
| A single overall colour hides one red dimension | A colour per dimension, plus an overall delivery confidence |
| Work not yet tested is counted as fine | No current evidence means the dimension cannot be green |
| Nobody checks the claims | The project management office (PMO) traces one or two claims per report back to the source system each cycle |

## Define red, amber and green by rule

Use the tolerances in the [charter](../../templates/project/project-charter.md). Tolerances are the limits within which the project manager may act without asking the steering group, an idea PRINCE2 calls management by exception.

| Status | Rule |
|---|---|
| Green | The 85% forecast for date, cost and Must have scope is inside tolerance, and every risk above tolerance has a funded response. |
| Amber | The forecast is at risk of breaking tolerance, or a top risk has no response, and recovery is within the project manager's authority. The report gives the recovery actions with dates. |
| Red | The forecast is outside tolerance, or recovery needs a decision above the project manager (money, scope, date or people). The project manager raises an exception to the steering group within 5 working days, with options. |

Two more rules close the usual gaps:

- **No evidence, no green.** A dimension whose key evidence is missing or older than the reporting period is amber at best. An untested payment run, an unrun migration rehearsal or a supplier figure nobody has checked is unknown, and unknown is not green.
- **Count passes, not activity.** "92% of tests executed" says nothing about quality. Report the share passed, and the defect arrival and fix rates.

Give a status for each dimension: date, cost, scope, quality, risk and benefits. PRINCE2 (7th edition) also sets tolerances for sustainability; add it where your organisation sets sustainability targets. Add one overall **delivery confidence**: a judgement of how likely the project is to deliver its outcome, as high, medium or low, with the trend (better, same, worse) and what would raise it. Confidence and status are different: a project can be green today with low confidence because the riskiest work is still ahead.

A status that moves from green straight to red is a reporting failure as well as a delivery one. Ask what signal was available earlier and add it to the rules.

## What goes in the report

One page, every 2 weeks, plus an exception report whenever red is reached. Use the [status report template](../../templates/project/status-report.md).

| Section | Content |
|---|---|
| Summary | three sentences: what changed since the last report, what worries the project manager, what the project needs from the steering group |
| Status and confidence | colour per dimension, overall delivery confidence, trend |
| Forecast | date at 50% and 85% confidence against baseline and tolerance; estimate at completion as a range against budget |
| Contingency | contingency remaining against the money exposure of open risks |
| Scope | Must haves accepted out of the total; scope added and removed since baseline |
| Burn-up | work accepted over time against total scope, with the scope line drawn so growth is visible |
| Quality | open defects by severity and their trend; go/no-go criteria met so far |
| Top risks and issues | the top 5 from the RAID log with owner, next action and date |
| Decisions needed | each with options, a recommendation, the deadline and the cost of delay |

Confidence levels and trends are what make a report honest. "85% likely between 10 and 24 March, moved two weeks later since the last report because test environment availability halved" lets a sponsor act. "On track" does not.

## Measure from systems, not opinion

| Measure | Source |
|---|---|
| Throughput, accepted items, scope added | the work tracker |
| Forecast range | a Monte Carlo over throughput, as in [planning and forecasting](../ways-of-working/planning-and-forecasting.md#standard) |
| Test results, open defects by severity | the pipeline and the defect tracker |
| Actual cost | finance, monthly; time and supplier invoices weekly where available |
| Top risks, issues and dependencies | the [RAID log](risks-raid-and-stage-gates.md) |
| Supplier progress | the supplier's repositories and pipeline, checked against your own acceptance tests |

A burn-up chart with the total scope line drawn is the most useful single picture. It shows progress, scope growth and the forecast in one view. Most reports hide scope growth by showing only work completed.

## Steering groups that decide

A steering group exists to make decisions the project manager cannot. If it only reads reports, replace it with the report.

**Membership.** Three to six people. PRINCE2's project board is a good model:

| Role | Who | Brings |
|---|---|---|
| Sponsor (chair) | the one person accountable for the outcome and the money | the final decision |
| Senior user | the business owner who receives the change | the users' needs and readiness |
| Senior supplier | the head of the engineering teams, and the systems integrator's (SI's) accountable lead where there is one | the delivery capacity and its limits |
| Project manager | attends, presents, does not decide | the facts and the options |
| Independent assurance | observes on large projects | a view that does not report to the sponsor |

**Rules.**

1. The agenda is decisions and exceptions, not reading the report aloud. Members read the report before the meeting.
2. Send the pre-read at least 2 working days before. Each decision request has options, a recommendation, the consequences of each option and a deadline.
3. Delegate tolerances so the group sees only exceptions. Within tolerance, the project manager acts.
4. Keep a decision log: date, decision, options considered, who decided, reason.
5. Meet monthly, at each gate, and within 5 working days of an exception.
6. If three meetings in a row make no decision, change the meeting: make it shorter, less frequent, or merge it with another.
7. Settle disagreements through [decision rights](../operating-model/decision-rights.md), within 5 working days.
8. When an SI sits on the group, hold commercial decisions (change requests, payments, claims, contract remedies) in a client-only part of the meeting. The SI's lead has a commercial interest and should not be asked to decide on it.

## Reporting upward

Major programmes appear on the board scorecard as two rows: forecast cost to complete against the approved budget, and the forecast date range at 85% confidence against the plan. Use the same numbers and colours as the project report. See [board and executive reporting](../../leaders/board-and-executive-reporting.md#the-one-page-scorecard).

## Practice

### Foundation

Solo, Startup and SME. A short written update every 2 weeks to whoever funds the work: the date range, what changed, what is in the way, what you need. Say "I do not know yet, I will know by" when that is the truth.

### Standard

Scale-up and Enterprise. The one-page report every 2 weeks, colours set by rule, ranges with confidence and trend, a burn-up with the scope line, measures pulled from systems. A steering group of three to six with a decision log. Exception reports within 5 working days of red.

### Assured

Regulated and Public sector. Everything in Standard, plus independent assurance reviews at the major gates, each with its own delivery confidence rating reported next to the project's. Keep reports as records. Use the same figures in reports to the audit committee, regulators or the departmental board. Public bodies follow any national reporting rules for major projects; see [public sector](../compliance/public-sector.md).

## Cloud, on-premises and air-gapped

Reporting works the same everywhere. In air-gapped sites, the data for the report may need to be exported from the secure network; automate the export of the few measures the report needs, rather than retyping them.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Green outside, red inside | Colours by rule; reconcile supplier reports with your own data. |
| Percent complete | Accepted increments, a burn-up and a forecast range. |
| A report that hides scope growth | Draw the scope line. |
| One overall colour | A colour per dimension and an overall delivery confidence with trend. |
| Status rewritten at each level | One report to every level; add summaries, do not rewrite. |
| Steering meetings that only listen | Decisions and exceptions on the agenda; a decision log. |
| The messenger punished for red | Thank the first red; judge reports by accuracy. |
| Green because nothing has been tested yet | No current evidence, no green. |
| Commercial decisions taken with the SI in the room | A client-only part of the meeting for commercial items. |

## Templates

- [Status report](../../templates/project/status-report.md)
- [RAID log](../../templates/project/raid-log.csv)
- [Board engineering report](../../templates/leaders/board-engineering-report.md)

## Sources

- AXELOS (PeopleCert), Managing Successful Projects with PRINCE2, 7th edition, 2023 (management by exception, tolerances, the project board).
- Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK Guide), 8th edition, 2025; the 7th edition (2021) covered progress measurement in its measurement performance domain: https://www.pmi.org/standards/pmbok
- Daniel S. Vacanti, "Actionable Agile Metrics for Predictability", 2015.
- UK Government Functional Standard GovS 002, Project delivery: https://www.gov.uk/government/publications/project-delivery-functional-standard
