# Agile in the AI era: beyond Scrum theatre

"We still run two-week sprints, estimate in story points and hold every ceremony. But code now takes hours, not days, and the sprint plan is out of date by Wednesday." Keep the Agile Manifesto values and drop the rituals built around estimating how long people take to type. Move to continuous flow with work-in-progress limits, shaped bets for bigger work, specs and evaluations written before code, and weekly reviews of real usage data. Plan capacity for review and verification on purpose, because that is where the bottleneck moves when code gets cheap.

## Outcomes

Starting points. Tune them after a quarter of data.

| Signal | Starting target |
|---|---|
| Change lead time (DORA) | Under 2 working days for a typical change, trending down |
| Rework rate and change fail rate | At or below the team's baseline from before the change |
| Cycle time from idea to change in users' hands, 85th percentile | Under 10 working days |
| Outcome goals reviewed with real usage data | Every week |
| Recurring meeting time per engineer | Under 10% of the working week |
| Team survey: "I know what we are trying to achieve and why" | At least 80% agree |

## Why Scrum as commonly practised is struggling

Be fair to Scrum first. The Scrum Guide (2020) is short, asks for a goal per Sprint, inspection and adaptation, and does not mention story points or velocity. Many teams use it well. The problem is cargo-cult practice that grew around it:

- **Rituals sized around human implementation effort.** Planning poker estimates how long people will take to write code. When an assistant drafts the code in an hour, the estimate measures the wrong thing. The real time goes on understanding, review and release.
- **Two-week batches when code takes hours.** A fixed batch makes finished work wait for the next review and makes new learning wait for the next planning session.
- **Velocity and story points as targets.** Once they are targets, they inflate. With AI, output can rise while value does not, so points measure even less.
- **Ceremonies that outlive their purpose.** A stand-up that is a status report, a review that is a slide deck, a retrospective with no finished actions.

## Why the Manifesto values matter more now

| Agile Manifesto value (2001) | Why it matters more now |
|---|---|
| Individuals and interactions | Agents produce code; people still decide what is worth building and whether it is right |
| Working software | Generated code that does not run, or does the wrong thing, is cheap to produce and expensive to find |
| Customer collaboration | Faster output without user contact means building the wrong thing faster |
| Responding to change | If code is cheap, plans should change as soon as evidence does |

## Where the bottleneck moves

| Constraint | Why it binds now | What to do |
|---|---|---|
| Problem framing and specs | A vague request now produces a lot of wrong code quickly | Write the problem, acceptance examples and non-goals first |
| Review and verification | Volume rises; generated code reads well even when wrong | Reserve review time in capacity planning; keep pull requests under 400 lines |
| Integration and release | Many small changes collide if they wait | Trunk-based development, continuous delivery, feature flags |
| Operating in production | More change means more chances to break things | SLOs, canary releases, fast rollback |
| Learning from users | Shipping is no longer the slow part; knowing what worked is | Instrument outcomes and review them weekly |

Make review and verification a named line in the team's capacity plan. A starting point is about a quarter of team time, tuned from the data on review wait times and rework.

## What fast and efficient looks like

- **Small cross-functional teams** that own an outcome, not a list of tickets. See [product partnership](product-partnership.md).
- **Continuous flow** with WIP limits (Kanban), not fixed batches. Pull the next item when one finishes.
- **Shaped bets with an appetite** (Shape Up) for work bigger than a few days: decide how much time the problem is worth, then shape a solution to fit.
- **Spec-first and eval-first.** Acceptance examples and, for AI features, evaluation sets exist before the code. See [AI engineering practices](../ai/ai-engineering-practices.md).
- **Trunk-based development and continuous delivery**, with [feature flags](../delivery/feature-flags.md) to separate deploy from release.
- **Outcome goals reviewed weekly** against real usage data.
- **Forecasts from throughput**, given as ranges. See [planning and forecasting](planning-and-forecasting.md).
- **Fewer, shorter meetings**, with written updates for status.

## Teams: do and don't

| Do | Don't |
|---|---|
| Write the spec and acceptance examples before generating code | Prompt first and work out what you wanted during review |
| Keep pull requests small and review within a working day | Let generated pull requests of thousands of lines queue up |
| Limit work in progress to about the number of people on the team | Start a new item whenever an assistant is idle |
| Ship behind flags and watch the change in production | Treat "merged" as "done" |
| Review usage data every week and change the plan when it says so | Hold a demo of tickets moved |
| Track rework rate and change fail rate as a team | Celebrate how much code was generated |

## Decision makers: do and don't

| Do | Don't |
|---|---|
| Fund outcomes and persistent teams, not headcount-hours | Set code-generation quotas or usage targets |
| Protect review and testing capacity explicitly | Cut testers and reviewers to pay for tools |
| Measure rework rate and change fail rate alongside speed | Report speed alone |
| Keep product discovery and user research funded | Replace discovery with faster output |
| Measure teams against their own baseline | Measure or rank individuals |
| Ask for forecasts as ranges with confidence | Turn a forecast into a fixed promise |

See [leading in the AI era](../../leaders/leading-in-the-ai-era.md) for the wider leadership view.

## What to keep from Scrum, and what to drop or change

| Keep | Drop or change |
|---|---|
| A clear goal per cycle that a user would recognise | Sprint commitment to a fixed list of tickets |
| A short retrospective with at most 2 owned actions | Hour-long retrospectives with no finished actions |
| One person who owns priorities and decides quickly | A product owner who only writes tickets |
| A definition of done that includes tests, review and release | Estimation meetings in story points; use throughput |
| Showing working software to users | Fixed two-week batches for release; release continuously |
| A short daily check on the goal and blockers | A round-robin status report; use the board and written updates |

## A 90-day transition from ceremonies to flow

| Weeks | Change | Check |
|---|---|---|
| 1 to 2 | Record baselines: lead time, cycle time, rework rate, change fail rate, one user outcome, a team survey. Map the board to how work really flows. | Baseline dashboard exists |
| 3 to 4 | Add WIP limits. Stop story point estimation; count items finished per week. Write specs with acceptance examples for all new work. | WIP limit respected most days |
| 5 to 8 | Release continuously behind flags. Replace sprint review with a weekly outcome review using usage data. Reserve review capacity. | Lead time falling; review wait time stable |
| 9 to 10 | Shape one larger piece of work as a bet with a fixed appetite. Move status updates to writing and shorten the daily check. | Meeting time under 10% of the week |
| 11 to 13 | Compare with the baseline. Keep what moved the numbers, revert what did not, and agree the next experiment. | Written review shared with the team and its leader |

Stop and rethink if rework rate or change fail rate rises for 4 weeks in a row, or if the team survey shows people no longer know the goal.

### Metrics to watch

| Metric | Source | Good direction |
|---|---|---|
| Change lead time and cycle time | Git host, CD tool, board | Down |
| Rework rate and change fail rate | Deployment and incident records ([metrics](../measurement/metrics.md)) | Flat or down |
| User outcome measure (task success, adoption, complaints) | Product analytics and support data | Toward the goal |
| Review wait time | Git host | Under 1 working day |
| Team survey (goal clarity, pace, tool usefulness) | Quarterly survey | Up |

## Practice

### Foundation

- A board with WIP limits, a weekly goal, a 30-minute retrospective every two weeks. Specs with acceptance examples before generating code.
- Track lead time and rework rate from your git host and deployment records.

### Standard

- Continuous flow for most work, shaped bets for larger work. Weekly outcome review with usage data.
- Review capacity planned explicitly. Forecasts from throughput as ranges.
- Quarterly review of DORA metrics and the team survey against the baseline. See [code assistants](../people/code-assistants.md).

### Assured

- Specs, decisions and evaluation results linked to pull requests and releases, so the audit trail comes from the delivery system.
- The definition of done includes the controls auditors test. See [agile and Scrum](agile-and-scrum.md) for regulated and public-sector settings.

## Cloud, on-premises and air-gapped

The method does not change. Teams in air-gapped networks plan for slower imports of models and dependencies, and host their board, wiki and assistants inside the network.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Points per sprint doubled after adopting assistants, and leaders celebrate | Look at rework rate, change fail rate and user outcomes instead |
| "AI-native agile" that adds a new ceremony | Remove a meeting before adding one |
| Sprints shortened to one week, same rituals | Move to flow; keep the goal and the retrospective |
| Review treated as overhead to be cut | Plan it as capacity, like any other work |

## Templates

- [Team working agreement](../../templates/docs/team-working-agreement.md)
- [OKR template](../../templates/leaders/okr-template.md)
- [Pull request template](../../templates/github/PULL_REQUEST_TEMPLATE.md)

## Sources

- Manifesto for Agile Software Development (2001): https://agilemanifesto.org/
- The Scrum Guide (2020): https://scrumguides.org/scrum-guide.html
- The Kanban Guide: https://kanbanguides.org/
- Ryan Singer, Shape Up (Basecamp, 2019): https://basecamp.com/shapeup
- DORA research programme and reports: https://dora.dev/research/
- DORA metrics guide: https://dora.dev/guides/dora-metrics-four-keys/
