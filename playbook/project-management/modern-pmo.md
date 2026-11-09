# A modern PMO

Many project management offices (PMOs) collect templates and chase status that teams already hold in their own tools. Teams work around them, and leaders get data that is late and softened. Run the PMO as a service to the teams and to the people who decide. It owns the portfolio data, the forecasting method and reference classes, the dependency and gate calendar, and assurance. It measures itself by better decisions and by time given back to teams. Scale governance to the size and risk of the work, and generate reports from systems instead of asking people to fill them in.

## Outcomes

Starting points. Tune them to your organisation.

- Each team spends under 1 hour per 2 weeks on PMO requests, measured by a short survey or a time sample each quarter.
- At least 80% of portfolio data comes from systems of record, not from manual returns.
- The project outcome register has an entry (estimate at each gate and actual result) for every closed project above the threshold.
- Forecast calibration is reported once a year: the share of projects that finished inside their 85% range. The target is about 85%.
- Teams and sponsors rate the PMO's usefulness twice a year. Measure a baseline first, then set the target.
- The PMO retires at least one template, report or meeting a year, or records why none should go.

## What the PMO is for

| Service | What it gives | Used by |
|---|---|---|
| Portfolio data | one list of projects and products with their stage, forecast, cost and capacity, kept current from systems | the portfolio owner and finance; see [portfolio and capacity](../strategy/portfolio-and-capacity.md) |
| Forecasting help | Monte Carlo tools, the project outcome register as a reference class, coaching on ranges | project managers and sponsors; see [planning fixed scope and budget](planning-fixed-scope-and-budget.md) |
| Dependency and calendar map | release dates, change freezes, contract end dates, budget deadlines, gate dates, on one calendar | teams and steering groups |
| Gate and assurance calendar | gates booked in advance, independent reviewers found from other programmes | sponsors |
| Risk roll-up | top project risks above tolerance passed to the enterprise risk register, with themes across projects | the risk function and the board |
| Finance link | actuals, forecasts and capitalisation evidence by product and project | finance; see [technology budget and cost](../strategy/technology-budget-and-cost.md) |
| Supplier performance | delivery data for each supplier across projects, and the change request log with cumulative change value against contract and procurement limits | supplier owners and procurement; see [suppliers and contracts](../strategy/suppliers-and-contracts.md) |
| Benefits tracking | the benefits register after go-live: owners, baselines, 6 and 12 month review results, fed back into business cases | sponsors, benefit owners and finance; see [benefits after go-live](projects-and-products.md#benefits-after-go-live) |
| Report checks | one or two claims per report traced back to the source system each cycle | sponsors and steering groups |
| Lessons learned | a searchable library, used at the start of each new project, not only filed at the end | new project teams |
| Coaching | help for first-time project managers and sponsors | people running projects |

A PMO can serve one programme, the whole organisation's portfolio, or act as a centre of practice that coaches and keeps methods. Larger organisations often run all three. Whatever the scope, write the services down with their users, as a platform team would. See [developer platform](../platform/developer-platform.md).

## Scale governance to the work

Set thresholds once a year with finance and risk: money, number of teams, suppliers involved, effect on customers, regulatory impact. Each project starts in the lightest class that fits.

| Class | Typical shape | Governance |
|---|---|---|
| Small | one team, internal, low risk, a few months | one-page charter, start and close only, status from the team's board |
| Medium | several teams or one supplier, or a customer-facing change | charter, risks, assumptions, issues and dependencies (RAID) log, 3 to 4 gates, status every 2 weeks, steering group |
| Large or high-risk | many teams and suppliers, regulated, or above the money threshold | everything in Medium, plus independent assurance at alpha and go/no-go, a quantified risk analysis and, where the contract requires it, earned value |

A project moves up a class when it crosses a threshold, and the PMO says so within a week. Most projects should be Small. If most of yours are Large, the thresholds are wrong or the work is not split small enough.

## Serve agile teams, do not translate them

- **Read from the teams' tools.** The PMO pulls throughput, accepted items, defects and pipeline results through application programming interfaces (APIs) or exports. Teams do not enter the same data twice.
- **Do not demand task-level plans** from teams that forecast from throughput. A Monte Carlo range is a better forecast than a task list, and it costs the team nothing.
- **Plan at team level.** Capacity is the number of funded teams and their split (for example 60% features, 20% reliability, 15% debt, 5% platform), not person-hours per task. See [portfolio and capacity](../strategy/portfolio-and-capacity.md#capacity-allocation-inside-teams).
- **Use the same horizons.** Now, Next (the following 1 to 3 quarters) and Later, as the [technical strategy](../strategy/technical-strategy.md) does.
- **Join the teams' events** rather than calling new ones: a sprint review or demo is a better progress check than a status meeting.

## What to stop doing

| Stop | Start |
|---|---|
| Weekly manual status templates | Reports generated from systems, with a short written commentary |
| Percent complete | Accepted increments and forecast ranges |
| The project manager picks the colour | Colours set by rule; see [status reporting](status-reporting.md#define-red-amber-and-green-by-rule) |
| The same template set for every project | Governance by class; most projects are Small |
| The PMO as gatekeeper of method | The PMO as coach, with a few rules that matter |
| Resource plans by named person and hour | Capacity by funded team |
| Lessons learned filed and never read | Lessons read at the start of the next similar project |

## Skills in the PMO

- A portfolio analyst who can pull and join data from work trackers, finance and the RAID logs, and run forecasts.
- Experienced project and programme managers who coach and run assurance reviews, drawn in rotation from live programmes so the advice stays current.
- A link to finance for capitalisation and actuals, and to risk for escalation.
- Enough technical understanding to read a pipeline report and a burn-up, and to ask what is behind them.

## Practice

### Foundation

Solo, Startup and SME. No PMO. One person, often the CTO or an operations lead, keeps a single list of active projects with their dates, owners and dependencies, and reviews it monthly.

### Standard

Scale-up and Enterprise. A small PMO with written services, governance by class, portfolio data drawn from systems, a project outcome register, and a calendar of gates, releases, freezes and contract dates. It reports its own measures twice a year.

### Assured

Regulated and Public sector. Everything in Standard, plus assurance reviewers who are independent of the projects they review, and gate and decision records kept for audit. The people who compile a programme's reports do not also give its independent assurance; keep the two roles in different reporting lines. Report the risk roll-up to the audit committee or departmental board. Write down the project management method, tailored from a recognised standard: ISO 21502, PRINCE2, the PMBOK Guide, or a national standard such as the UK GovS 002. EU financial entities map the method to their ICT project management policy under the EU DORA regulation. See [risks, RAID logs and stage gates](risks-raid-and-stage-gates.md#assured).

## Cloud, on-premises and air-gapped

The PMO's work is the same everywhere. Where teams work in air-gapped networks, agree a regular, automated export of the few measures the portfolio needs, and keep the calendar of hardware deliveries and import windows in the dependency map.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A PMO that collects templates | Publish services with users and measures; retire unused templates. |
| Double entry of team data | Read from team tools. |
| Full governance for small projects | Governance by class; most projects are Small. |
| Assurance by people who report to the sponsor | Independent reviewers from other programmes. |
| Lessons learned that nobody reads | Read them at the start of the next similar project. |
| A PMO judged by compliance with its process | Judge it by time given back to teams and forecast calibration. |
| A PMO that reports benefits nobody measured | A business owner and a baseline for each benefit, or leave it out. |
| The same PMO compiles the report and assures it | Separate reporting and assurance lines. |

## Templates

- [Project charter](../../templates/project/project-charter.md)
- [Status report](../../templates/project/status-report.md)
- [RAID log](../../templates/project/raid-log.csv)
- [Stage gate checklist](../../templates/project/stage-gate-checklist.md)
- [Lessons learned](../../templates/project/lessons-learned.md)
- [Operating rhythm calendar](../../templates/leaders/operating-rhythm-calendar.md)

## Sources

- Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK Guide), 8th edition, 2025: https://www.pmi.org/standards/pmbok
- AXELOS (PeopleCert), Portfolio, Programme and Project Offices (P3O), 2013.
- ISO 21502:2020, Project, programme and portfolio management: Guidance on project management. International Organization for Standardization.
- UK Government Functional Standard GovS 002, Project delivery: https://www.gov.uk/government/publications/project-delivery-functional-standard
- Bent Flyvbjerg and Dan Gardner, "How Big Things Get Done", Currency, 2023.
- Mik Kersten, "Project to Product", IT Revolution, 2018.
