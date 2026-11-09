# For business executives and board members

You do not need to understand the technology to govern it well. Ask a small set of questions every quarter, insist on answers backed by a few trend numbers, and fund technology the way you fund any other capability that the business depends on: persistent teams with clear outcomes, not one-off projects that end at launch. The goal is not to second-guess your technology leader. It is to know early when speed, safety or cost is drifting, while the fix is still cheap.

## When to use this

This page is for CEOs, CFOs, COOs, non-executive directors and board members in any sector: banks, health, telecoms, retail, manufacturing, energy, public bodies and NGOs.

- You approve technology budgets and are not sure what good value looks like.
- A major outage, breach or failed programme surprised the board.
- You are hiring or reviewing a CTO, CIO or head of technology.
- Your organisation is about to make a large technology bet: a new core system, a cloud move, an AI programme, an acquisition.

Use it with [board and executive reporting](board-and-executive-reporting.md), which your technology leader uses to prepare the report you receive.

## Ten questions to ask your technology leader

Ask them once a quarter. A strong leader answers most of them with a number, a trend and a named owner. The [question sheet](../templates/leaders/questions-for-your-technology-leader.md) lists what good and worrying answers sound like.

| # | Question | Why it matters | Playbook page |
|---|---|---|---|
| 1 | Which three business outcomes is technology working on this quarter, and how will we know they moved? | spending should map to outcomes the business already measures | [technical strategy](../playbook/strategy/technical-strategy.md) |
| 2 | How long does it take for a small, approved change to reach customers, and is that getting shorter? | speed of change is how fast the business can respond | [metrics](../playbook/measurement/metrics.md) |
| 3 | How often do changes cause problems for customers, and how fast do we recover? | speed without stability is borrowed time | [metrics](../playbook/measurement/metrics.md) |
| 4 | Which services are most important to customers, what reliability have we promised, and are we meeting it? | reliability targets turn "it should not go down" into a decision with a cost | [service levels](../playbook/reliability/service-levels.md) |
| 5 | When did we last restore our most important systems from backup, and how long did it take? | an untested backup is a hope, not a control | [backup and recovery](../playbook/reliability/backup-and-recovery.md) |
| 6 | What are our top five technology risks, and who owns each? | risks without owners are not managed | [IT governance](../playbook/operating-model/it-governance.md) |
| 7 | Which suppliers could stop the business if they failed, and could we leave them? | a supplier's outage or breach becomes yours | [third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) |
| 8 | What share of engineering time goes to running and fixing existing systems, and is it rising? | a rising share means less capacity for new work each year | [portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md) |
| 9 | Where are we using AI, with what data, and who approved it? | AI brings legal, data and reputational risk as well as value | [AI governance](../playbook/ai/ai-governance.md) |
| 10 | Which people could we not afford to lose, and what are we doing about it? | knowledge held by one or two people is a single point of failure | [skills gap](../playbook/people/skills-gap.md) |

If your organisation has no software team of its own and an IT provider runs everything, questions 2, 3 and 8 do not apply. Use the [questions to ask your IT provider](for-small-and-medium-businesses.md#questions-to-ask-your-it-provider-every-year) instead.

## How to read the numbers

You will see two families of numbers. Read the trend over 4 quarters, not a single value, and never compare teams with each other on them.

| Number | Plain meaning | Better when | Ask if |
|---|---|---|---|
| Deployment frequency | how often changes go live | higher, with stable failure rate | it falls for two quarters |
| Change lead time | time from a finished change to customers using it | shorter | it is measured in weeks or months |
| Change fail rate | share of changes that cause a problem needing immediate action | lower | it rises while speed rises |
| Failed deployment recovery time | how fast a bad change is undone or fixed | shorter | it is measured in days |
| Rework rate | share of changes made only to fix problems in production | lower | it rises after a new tool or process |
| Service level objective (SLO) attainment | share of the time a service met the reliability target agreed for it | at or above target, not far above | targets are missed and nothing changes, or always met by a wide margin (target too loose) |
| Error budget | the amount of unreliability the target allows in a period | spent deliberately | it is exhausted and releases continue as normal |

The first five are the DORA software delivery metrics, from a long-running research programme (unrelated to the EU DORA regulation for financial firms). DORA's research found that speed and stability move together: good teams improve both. Their 2025 report stopped publishing "elite" thresholds, so do not set targets by copying another company's numbers. Ask for improvement against your own baseline.

Be wary of any single number used as a target. Once people are paid or ranked on it, they find ways to move the number without moving the outcome.

## How to judge a technology investment

| Check | What good looks like |
|---|---|
| Problem | stated in business terms, with evidence (cost, incidents, lost sales, risk) |
| Options | at least three, including "do nothing" and a smaller first step |
| Benefit | in money, time or risk, with low, expected and high cases; the low case still pays back |
| First release | something real in use within 3 to 6 months, not a plan to deliver everything in year three |
| Stop points | named gates where the investment can be stopped or reshaped, with criteria agreed in advance |
| Running cost | the cost to run and maintain after launch, every year, not only the build cost |
| Exit | how to leave the chosen supplier or platform, and what it would cost |
| Owner | one named executive accountable for the benefit, not only the delivery |

Use the [business case](../playbook/strategy/business-case.md) method and check benefits at 6 and 12 months. For an acquisition or a large supplier choice, use [technical due diligence](technical-due-diligence.md).

## How to fund technology

- **Fund teams, not projects.** A persistent team that owns a service keeps improving it. A project team that disbands at launch leaves a system nobody understands.
- **Fund outcomes in stages.** Release money at each gate based on evidence, not on the original plan.
- **Make the capacity split explicit.** Agree each year what share of engineering goes to new features, reliability, technical debt and platforms. Starting point from [portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md): 10 to 20% each for reliability and for technical debt, and 5 to 15% for platform work. Review it each quarter.
- **Fund platforms as shared services.** A platform that many teams use (identity, hosting, data, payments) saves money only if it is funded once and adopted widely. See [developer platform](../playbook/platform/developer-platform.md).
- **Count technical debt as a cost.** Ask for the [debt register](../templates/docs/tech-debt-register.csv): what each item costs today in time, incidents or risk, and what fixing it costs. See [technical debt](../playbook/architecture/technical-debt.md).
- **Watch running costs.** Cloud costs grow with use. Ask for cost per customer or per transaction, not only the total bill. See [FinOps](../playbook/platform/finops.md).

## Red flags

| You notice | It may mean | Ask for |
|---|---|---|
| Releases happen a few times a year and need weekend work | changes are large, manual and risky | the plan to release smaller changes more often |
| Every major outage is blamed on one person or one supplier | the organisation is not learning from failure | the last three postmortems and their completed actions |
| "We have backups" without a restore date | the backup has never been proven | the date and duration of the last full restore test |
| The same programme has been "90% done" for two quarters | scope, estimates or ownership are broken | a forecast as a range, and what has been cut |
| Most of the budget goes to one supplier with no exit plan | lock-in and concentration risk | the exit plan, its cost and when it was last tested |
| Two or three engineers are needed for every problem | key-person risk | a skills matrix and a plan to spread knowledge |
| Security is reported only as "no incidents" | absence of evidence, not evidence of control | overdue critical vulnerabilities and the last test of incident response |
| Technology reports are mostly activity (projects started, tickets closed) | no link to outcomes | the outcome measures from question 1 |

## What good looks like

- The technology leader brings a short report each quarter with 8 to 12 measures, trends and two or three decisions for the board. See [board and executive reporting](board-and-executive-reporting.md).
- Small changes reach customers in days, and the change fail rate is stable or falling.
- Important services have reliability targets agreed with the business, and the board sees attainment.
- Restores and failovers of critical systems are tested on a schedule, with measured times.
- Major incidents lead to a written review within 5 working days and actions that get done.
- Every critical supplier has an owner and an exit plan.
- The board has rehearsed a serious cyber incident at least once a year. The UK NCSC Board Toolkit is a good starting point. See also [crisis leadership](crisis-leadership.md).

## Common mistakes

| Mistake | Fix |
|---|---|
| Asking only "is it on time and on budget?" | Ask the ten questions; on time and on budget says nothing about value or risk. |
| Approving a large programme as one decision | Approve in stages with stop points. |
| Cutting maintenance to fund new features | Agree a protected share for reliability and debt. |
| Comparing teams on delivery metrics | Use metrics to find where to help, not to rank. |
| Treating cyber security as an IT issue | Own the risk appetite at board level; delegate the controls. |
| Hiring a technology leader and then giving them no seat where decisions are made | Include them in strategy, not only in delivery reviews. |

## Templates

- [Questions for your technology leader](../templates/leaders/questions-for-your-technology-leader.md)
- [Board engineering report](../templates/leaders/board-engineering-report.md)
- [Business case](../templates/strategy/business-case.md)
- [Risk register](../templates/strategy/risk-register.csv)
- [Tech debt register](../templates/docs/tech-debt-register.csv)

## Sources

- DORA, software delivery performance metrics: https://dora.dev/guides/dora-metrics-four-keys/
- DORA research programme and reports: https://dora.dev/research/
- Google, Site Reliability Engineering books (SLOs and error budgets): https://sre.google/books/
- UK NCSC, Board Toolkit: https://www.ncsc.gov.uk/collection/board-toolkit
- Nicole Forsgren, Jez Humble and Gene Kim, Accelerate, IT Revolution Press, 2018.
