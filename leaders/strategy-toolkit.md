# Strategy toolkit

Strategists and planners do not need more frameworks. They need a small set of tools that each answer one question, run in a single working session and produce something a decision can be based on. Use the seven tools below, pick the one that matches the question in front of you, and feed every output into the [technical strategy](../playbook/strategy/technical-strategy.md) and the [portfolio review](../playbook/strategy/portfolio-and-capacity.md). A tool whose output does not change a decision within one quarter was the wrong tool, or was run at the wrong time.

## When to use this

| The question you face | Tool | Session length | Output |
|---|---|---|---|
| What should we build ourselves, and what should we buy or adopt? | Wardley mapping | about 100 minutes | one map, three decisions |
| Where does the business need technology investment most? | Business capability mapping | about 2 hours | capability heat map |
| We run too many applications and the run cost keeps rising | Application portfolio rationalisation (TIME) | about 2 hours per 30 to 40 applications | one decision per application |
| What could change the ground under us in 3 to 5 years? | Scenario planning | about 2 hours | four scenarios, no-regret moves, signposts |
| How do teams know what the strategy asks of them this quarter? | OKRs | about 90 minutes per team | 1 to 3 objectives with measurable key results |
| Everything is a priority | Cost of delay prioritisation | 60 to 90 minutes | a ranked list with the reasoning visible |
| Should we build, buy, adopt open source or partner? | [Build, buy or adopt](../playbook/strategy/build-buy-adopt.md) | 2 to 3 hours | weighted scores and a decision record |

Run each tool with the people who know the subject, not only with managers. Five to eight people is the right size. Write the output on one page the same day.

## Wardley mapping

**When to use it.** Before a large build or buy decision, a platform investment, or an argument about what to outsource. A Wardley map, developed by Simon Wardley, shows the components a user need depends on and how evolved each one is.

**How to run it (about 100 minutes).**

| Minutes | Step |
|---|---|
| 10 | Name one user and one user need. Write it at the top. |
| 20 | List the components that need depends on: services, data, platforms, skills, suppliers. |
| 15 | Arrange them as a chain. Visible to the user at the top, infrastructure at the bottom. |
| 25 | Place each component on the evolution axis: Genesis, Custom-built, Product (and rental), Commodity (and utility). Argue about placement. The arguments are the value. |
| 15 | Mark what will move to the right in the next 2 to 3 years. |
| 15 | Write three decisions: what to build, what to buy or adopt, what to stop doing. |

**Reading the map.** Components in Genesis or Custom-built that set you apart are candidates to build. Components in Product or Commodity are candidates to buy or adopt. Custom-built components that should be commodities are where money leaks.

**Limits.** Placement is judgement, and two groups will place the same component differently. The map gives no numbers, so pair it with a [business case](../playbook/strategy/business-case.md). Do not maintain maps as formal documents. Redraw one when the question changes.

## Business capability mapping

**When to use it.** Before a reorganisation, a systems consolidation, a merger, or an annual investment round. A business capability is what the organisation does, such as "manage customer accounts" or "collect payments", described without saying who does it or which system does it. Capabilities change slowly. Org charts and systems change often.

**How to run it (about 2 hours).**

1. Before the session, draft 8 to 15 level 1 capabilities from the annual report, the service catalogue and the budget lines.
2. In the session, agree level 1 (20 minutes), then split each into 3 to 8 level 2 capabilities (40 minutes).
3. Rate each level 2 capability: business criticality (high, medium, low) and current maturity from 1 to 5 (25 minutes).
4. Map the systems that support each one (20 minutes).
5. Mark the heat map: high criticality with maturity of 2 or less means invest; three or more systems for one capability means consolidate (15 minutes).

**Limits.** Stop at level 2 or 3. Level 4 maps are expensive to keep and rarely change a decision. Watch for a capability map that copies the org chart: if every capability has exactly one department, rename them by what is done, not who does it. Maturity scores are opinions until you attach evidence such as incident counts, change lead time or manual steps.

## Application portfolio rationalisation (TIME)

**When to use it.** When run cost rises every year, when nobody can list every application, or before a cloud migration. Gartner's TIME model sorts each application into one of four decisions.

| Decision | Business value | Technical fit | What it means |
|---|---|---|---|
| Invest | high | high | fund improvements; it is part of the future |
| Tolerate | low | high | keep running at minimum cost; no new features |
| Migrate | high | low | keep the function, move it to a better platform or product |
| Eliminate | low | low | retire it on a date, with an owner |

**How to run it.** Preparation matters more than the workshop. Pull the inventory from licence spend, single sign-on logs, cloud and data centre bills and the service catalogue. Record owner, users and annual run cost for each application. In the session, score business value and technical fit from 1 to 5, using 3.5 as the line between low and high (a starting point). With a prepared inventory, a group can score 30 to 40 applications in 2 hours. Split larger estates by business area.

**Rules that make it stick.** Every Eliminate gets a target quarter and an owner. Every Migrate gets a target platform. Review the portfolio twice a year and report the run-cost trend to the [portfolio review](../playbook/strategy/portfolio-and-capacity.md).

**Limits.** Scores are opinions; ask the owner and a user for evidence. The model ignores dependencies, so check integrations before retiring anything. Retiring an application does not retire its data: check records retention and data protection duties first (see [data governance](../playbook/data/data-governance.md)).

## Scenario planning for 3 to 5 years

**When to use it.** During the annual strategy refresh, before commitments that last longer than three years (a data centre lease, a five-year supplier contract, a core platform), and when regulation, AI or sovereignty rules could change the plan.

**How to run it (about 2 hours).**

| Minutes | Step |
|---|---|
| 15 | List driving forces. Start from the [horizon scan](../playbook/strategy/horizon-scan.md). |
| 20 | Rate each force for impact and uncertainty. Certain forces go straight into the plan. |
| 10 | Pick the two forces with the highest impact and uncertainty. They become the two axes. |
| 30 | Write four scenarios, one per quadrant. Give each a name and one paragraph describing year 4. |
| 30 | Test the current strategy against each scenario: what breaks, what still holds. |
| 15 | Write no-regret moves (good in all four), options (cheap bets that keep a door open) and signposts (events that show which scenario is unfolding), each with an owner. |

Example axes: "data must stay in-country" against "data may move freely", crossed with "AI tools are cheap and reliable" against "AI tools are costly or restricted".

**Limits.** Scenarios are not forecasts. Do not assign probabilities, and do not plan only for the scenario you think is most likely. Four scenarios is the most people remember. Without signposts and owners, the exercise produces a document and no change.

## OKRs done properly

**When to use it.** To turn the strategy into a few measurable outcomes per team per quarter. Andy Grove described objectives and key results in "High Output Management" (1983). John Doerr's "Measure What Matters" (2018) describes how they spread.

**The rules.**

- 1 to 3 objectives per team per quarter, each with 2 to 4 key results.
- An objective is qualitative and says why it matters. A key result is a number with a baseline, a target and a data source.
- Key results measure outcomes, a change in what users or systems do. They do not list tasks.
- Business-as-usual work does not need an OKR. Track it with [service levels](../playbook/reliability/service-levels.md) and [metrics](../playbook/measurement/metrics.md).
- Keep OKRs out of performance ratings and pay, or people will set targets they know they can hit.

| Task list (avoid) | Outcome-based key result (illustrative) |
|---|---|
| Launch the new onboarding flow | New customers who complete setup within one day rise from 40% to 60% |
| Migrate to the new CI system | Median change lead time falls from 5 days to 2 days |
| Run security training | Critical vulnerabilities older than 30 days fall from 12 to 0 |

**How to run it (about 90 minutes).** 15 minutes to read the strategy actions for this quarter. 30 minutes to draft objectives. 30 minutes to draft key results and find the baseline for each. 15 minutes to cut: if there are more than three objectives, drop one.

**Limits.** Outcome measures lag, so pair each with one leading signal. Not everything important fits an OKR; do not force it. OKRs set by leaders and handed down without discussion become a task list with numbers.

## Cost of delay prioritisation

**When to use it.** When the backlog or portfolio has more "top priorities" than teams. Cost of delay is the value lost for each week an item is not done. Donald Reinertsen sets out the method in "The Principles of Product Development Flow" (2009).

**How to run it (60 to 90 minutes).**

1. Estimate cost of delay per week in money. This is Reinertsen's method. When you cannot, a common shortcut, used in the Scaled Agile Framework (SAFe), scores three parts on a relative scale (1, 2, 3, 5, 8, 13): value to users or the business, time criticality (a regulatory date, a contract end, a market window) and risk reduction. Reinertsen's method and the relative shortcut can rank items differently, so move to money estimates for the top items.
2. Estimate duration or size on the same relative scale.
3. Divide cost of delay by duration. Do the highest ratio first. Reinertsen calls this "weighted shortest job first".

The table uses the relative shortcut.

| Item (illustrative) | Value | Time criticality | Risk reduction | Cost of delay | Size | Ratio |
|---|---|---|---|---|---|---|
| Reporting change required by a regulator next quarter | 3 | 13 | 5 | 21 | 5 | 4.2 |
| Replace a database version that leaves support in 6 months | 2 | 8 | 8 | 18 | 8 | 2.3 |
| New self-service dashboard for sales | 8 | 2 | 1 | 11 | 5 | 2.2 |

**Limits.** Relative scores are rough; use them to order, not to promise. Large items sink to the bottom forever, so split them. The ratio ignores dependencies. Deadlines with legal penalties are a step change, not a slope: treat them as constraints first.

## Build, buy or adopt

Once a Wardley map or a capability map shows where to invest, use the weighted matrix and total cost of ownership method in [build, buy or adopt](../playbook/strategy/build-buy-adopt.md). Record the outcome as a [decision record](../playbook/architecture/decision-records.md).

## How the tools feed strategy and portfolio

| Tool output | Goes into | Where |
|---|---|---|
| Scenarios, signposts, horizon scan | Diagnosis and the Later horizon | [Technical strategy](../playbook/strategy/technical-strategy.md) |
| Wardley map, capability heat map | Guiding policy: what to build, buy, consolidate | [Technical strategy](../playbook/strategy/technical-strategy.md), [build, buy or adopt](../playbook/strategy/build-buy-adopt.md) |
| TIME decisions and run-cost trend | Run share of the investment mix, stop list | [Portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md) |
| Cost of delay ranking | Quarterly order of work | [Portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md), [planning and forecasting](../playbook/ways-of-working/planning-and-forecasting.md) |
| OKRs | Now horizon actions, team goals | [Technical strategy](../playbook/strategy/technical-strategy.md) |

A suggested yearly calendar: scenarios and capability map before the annual budget; TIME review twice a year; Wardley maps before each large investment; OKRs and cost of delay every quarter.

## Common mistakes

| Mistake | Fix |
|---|---|
| Running every tool every year | Run a tool when its question is live. Most years need two or three. |
| Workshops with only managers | Invite the engineers and operators who know the systems. |
| Beautiful outputs, no decisions | End each session with written decisions, owners and dates. |
| Capability maps at level 4 | Stop at level 2 or 3. |
| TIME scores with no cost data | Collect owner, users and run cost before the session. |
| Scenarios treated as forecasts | Plan for all four with no-regret moves and options. |
| OKRs that list tasks | Rewrite each key result as a change in a measured outcome. |
| Prioritising by who shouts loudest | Score cost of delay in the open and publish the ranking. |

## Templates

- [OKR template](../templates/leaders/okr-template.md)
- [Capability map](../templates/leaders/capability-map.csv)
- [Application portfolio (TIME)](../templates/leaders/application-portfolio.csv)
- [Trade-off matrix](../templates/leaders/trade-off-matrix.md)
- [Strategy one-pager](../templates/strategy/strategy-one-pager.md)
- [Business case](../templates/strategy/business-case.md)

## Sources

- Simon Wardley, "Wardley Maps" (free online book): https://learnwardleymapping.com/
- Gartner, TIME model for application portfolio rationalisation (Tolerate, Invest, Migrate, Eliminate).
- Andy Grove, "High Output Management", Random House, 1983.
- John Doerr, "Measure What Matters", Portfolio, 2018.
- Donald G. Reinertsen, "The Principles of Product Development Flow", Celeritas Publishing, 2009.
- Scaled Agile Framework, "Weighted Shortest Job First": https://framework.scaledagile.com/wsjf
- Richard Rumelt, "Good Strategy Bad Strategy", Crown Business, 2011.
