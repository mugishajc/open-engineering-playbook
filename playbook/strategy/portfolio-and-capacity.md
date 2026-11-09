# Portfolio and capacity

Most engineering organisations commit to more work than they can finish, spend capacity on reliability and debt without saying so, and present roadmaps as promises. Set an explicit investment mix and capacity split, plan in quarters inside the annual budget, publish roadmaps as forecasts with confidence levels, and stop work on purpose when the evidence says so. The aim is fewer things in progress, finished sooner, with the trade-offs visible to finance and the board.

## Outcomes

Starting points. Tune them to your organisation.

- Actual capacity spent per category (features, reliability, debt, platform) is within 5 percentage points of the planned split each quarter.
- Work in progress at portfolio level is capped, for example no more than one major initiative per 2 to 3 teams at a time.
- At least 80% of items forecast at 85% confidence land by their forecast date.
- At least one initiative is stopped or shrunk at each quarterly review, or the review records why none should be.
- Every initiative above an agreed size links to a [technical strategy](technical-strategy.md) action and a [business case](business-case.md).

## Investment mix: run, grow, transform

Classify every funded initiative into one of three groups and show the mix to finance and the board.

| Group | Meaning | Examples | Typical share (starting point) |
|---|---|---|---|
| Run | keep current services working, safe and compliant | patching, support, licence renewals, regulatory changes, capacity | 50% to 70% |
| Grow | improve and extend current products and services | new features, new markets, performance work | 20% to 35% |
| Transform | change the business model or the way of building software | new products, a [transition](transition-playbook.md), a new platform | 5% to 20% |

Run that keeps rising year on year is a warning: it usually means debt and complexity are growing faster than they are retired. Report the trend, not only the current split.

## Capacity allocation inside teams

Planning only features hides real work. Agree an explicit split for each team or group and track it.

| Category | Covers | Starting split |
|---|---|---|
| Features | new user-facing value | 55% to 70% |
| Reliability | SLO work, incident follow-ups, [postmortem](../reliability/postmortems.md) actions, on-call load | 10% to 20% |
| Technical debt | refactoring, upgrades, removing dead code, see [technical debt](../architecture/technical-debt.md) | 10% to 20% |
| Platform and runway | shared tooling, [architecture runway](../architecture/architecture-practice.md), developer experience | 5% to 15% |

Adjust the split with evidence:

- if the error budget is spent (see [service levels](../reliability/service-levels.md)), move capacity to reliability until it recovers;
- if change lead time or change fail rate is getting worse (see [metrics](../measurement/metrics.md)), raise the debt share for the next quarter;
- if three or more teams build the same infrastructure, fund the platform share centrally.

Track allocation from labels on work items. A rough split from labels is better than an exact one nobody maintains.

## Annual and quarterly planning

| Cycle | When | Inputs | Outputs | Who |
|---|---|---|---|---|
| Annual | aligned to the budget year; start 3 to 4 months before it | strategy, horizon scan, run cost trend, business cases | investment mix, team funding, top 5 to 10 initiatives | CTO, finance, product leadership |
| Quarterly | 2 to 3 weeks before each quarter | last quarter's results, throughput data, risk register | capacity split per team, committed and forecast items | engineering and product leads with teams |
| Monthly | first week of the month | progress, blockers | rebalancing within the quarter | portfolio owner |

Fund teams, not projects, for anything that will run for more than a year. Project funding ends at launch and leaves the service without owners.

Public sector bodies often cannot carry money between budget years. Plan so that each year ends at a usable state, and ask for multi-year funding for platforms and live services. See [public sector](../compliance/public-sector.md).

## Roadmaps as forecasts

A roadmap is a forecast, not a promise. Show it that way.

- Use three columns: **Now** (committed, this quarter), **Next** (planned, 1 to 2 quarters), **Later** (direction only). This matches the horizons in the [technical strategy](technical-strategy.md).
- For dated items, forecast from measured throughput (items finished per week), not from story point velocity. Run a Monte Carlo simulation over past throughput and report dates at 50% and 85% confidence. See [planning and forecasting](../ways-of-working/planning-and-forecasting.md).
- State the confidence on every date. "85% likely by 30 June" is honest. "Due 30 June" invites a surprise.
- Re-forecast every 2 weeks. Report changes as soon as the 85% date moves by more than two weeks.

## Wardley mapping for situational awareness

A Wardley map, developed by Simon Wardley, places the components of a service on two axes: visibility to the user (from the user need down to underlying infrastructure) and evolution (Genesis, Custom-built, Product, Commodity). Use it before large investment decisions:

- components in Genesis or Custom-built that differentiate you are candidates to build;
- components that have moved to Product or Commodity are candidates to buy or adopt (see [build, buy, adopt or partner](build-buy-adopt.md));
- building a commodity in-house is a common and expensive mistake that the map makes visible.

Maps are a thinking tool. Draw one in 2 hours with the people who know the service. Do not maintain them as formal documents.

## How to stop work

Stopping is a decision, not a failure. Make it routine.

1. Every initiative has stop conditions written at the start: a measure, a threshold and a date.
2. At each quarterly review, ask for each initiative: would we start this today, knowing what we know now? If not, stop or shrink it.
3. Ignore money already spent. Decide only on remaining cost and remaining value.
4. When stopping, release the team to the next priority within two weeks, archive the work and write a short decision record of what was learned.
5. Celebrate good stops in public. If people are punished for stopping, they will hide failing work.

## Portfolio review cadence

| Review | Frequency | Time box | Questions |
|---|---|---|---|
| Portfolio review | quarterly | half a day | Is the mix right? What do we stop? What do we start? Are capacity splits being kept? |
| Forecast check | every 2 weeks | 30 minutes | Have 85% dates moved? Which risks are rising? |
| Benefits review | 6 and 12 months after delivery | 1 hour per initiative | Did the business case hold? |
| Run cost review | twice a year | 2 hours | Is run growing? Which services cost most per user? |

## Practice

### Foundation

Solo and Startup. One list of priorities, ranked. Limit work in progress to one or two initiatives. Keep about 20% of time for reliability and debt and write it down. Forecast from how many items you finish per week.

### Standard

Scale-up and Enterprise. The run, grow and transform mix, capacity splits per team, quarterly planning inside the annual budget, roadmaps with confidence levels, and quarterly portfolio reviews with stop decisions. A named portfolio owner keeps the data.

### Assured

Regulated and Public sector. Everything in Standard, plus mandatory work (regulation, audit findings, end-of-life risks) shown as a separate, protected line, approval records for the annual mix, links from initiatives to the risk register, and reports to the audit committee or departmental board on the mix and its trend.

## Cloud, on-premises and air-gapped

On-premises and air-gapped estates carry hardware refresh, data centre and import work in the run budget. Show it separately so the run trend is understood. Cloud estates make run costs variable: link the portfolio review to the cost review in [FinOps](../platform/finops.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| 100% of capacity planned for features | Explicit split for reliability, debt and platform. |
| Roadmap dates without confidence | Forecast from throughput; show 50% and 85% dates. |
| Starting everything, finishing little | Cap portfolio work in progress. |
| Initiatives that never stop | Stop conditions at the start; "would we start this today?" each quarter. |
| Project funding for long-lived services | Fund persistent teams. |

## Templates

- [Strategy one-pager](../../templates/strategy/strategy-one-pager.md)
- [Business case](../../templates/strategy/business-case.md)
- [Risk register](../../templates/strategy/risk-register.csv)
- [Tech debt register](../../templates/docs/tech-debt-register.csv)

## Sources

- Simon Wardley, "Wardley Maps" (book published openly): https://medium.com/wardleymaps
- Donald G. Reinertsen, "The Principles of Product Development Flow", Celeritas Publishing, 2009.
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
- Google SRE Workbook, error budget policy: https://sre.google/workbook/error-budget-policy/
