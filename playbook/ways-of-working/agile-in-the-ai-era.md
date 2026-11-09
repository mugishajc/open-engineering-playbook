# Agile in the AI era: beyond Scrum theatre

Many teams still run two-week sprints, estimate in story points and hold every ceremony, although an assistant can now draft the code for some tasks in hours. Keep the Agile Manifesto values, drop the rituals built around estimating how long people take to type, and move to continuous flow with work-in-progress limits, shaped bets, specs and evaluations written before code, and weekly reviews of real usage data. Plan capacity for review and verification on purpose, because that is where the bottleneck moves, and treat any speed-up as a hypothesis to test against your own baseline: the public evidence is mixed.

## Outcomes

Starting points. Tune them after a quarter of data.

| Signal | Starting target |
|---|---|
| Change lead time (DORA) | Under 1 week, trending down. Teams that already meet it set their next target from their own baseline. |
| Rework rate and change fail rate | At or below the team's baseline from before the change |
| Cycle time from idea to change in users' hands, 85th percentile | Under 10 working days |
| Outcome goals reviewed with real usage data | Every week |
| Recurring meeting time per engineer | Under 10% of the working week |
| Team survey: "I know what we are trying to achieve and why" | At least 80% agree |

## What the evidence says

Evidence on AI and delivery speed is mixed, so do not plan headcount or dates on an assumed gain.

- A randomised controlled trial by METR (July 2025) with 16 experienced open source developers, using early-2025 tools on their own repositories, found they took about 19% longer with AI tools, while believing they had been about 20% faster.
- DORA's 2024 report found that each 25% increase in AI adoption was associated with an estimated 1.5% fall in delivery throughput and a 7.2% fall in delivery stability.
- DORA's 2025 report found the association with throughput had turned positive, while the association with instability had not. It describes AI as an amplifier of the organisation's existing strengths and weaknesses.

Use these as reasons to measure, not as forecasts. Record your own baseline before rollout and compare against it (see [leading in the AI era](../../leaders/leading-in-the-ai-era.md)).

## Why Scrum as commonly practised is struggling

Be fair to Scrum first. The Scrum Guide (2020) is short, asks for a goal per Sprint, inspection and adaptation, and does not mention story points or velocity. Many teams use it well. The problem is cargo-cult practice that grew around it:

- **Rituals sized around human implementation effort.** Planning poker estimates how long people will take to write code. When an assistant can draft the code for a task in an hour, the estimate measures the wrong thing. The real time goes on understanding, review and release.
- **Two-week batches when code can be drafted in hours.** A fixed batch makes finished work wait for the next review and makes new learning wait for the next planning session.
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
| Set a WIP limit below the number of people on the team (for example team size minus one) and lower it if items age | Start a new item whenever an assistant is idle |
| Count every open agent pull request as work in progress, with a named human owner | Let agents open pull requests nobody has agreed to review |
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

### Agree it with finance before you stop estimating

Many firms use story points or timesheets as evidence for capitalising software development cost, under IAS 38 internationally or ASC 350-40 in the US (amended by ASU 2025-06, which removes the project-stage model for annual periods beginning after 15 December 2027). Dropping that data without a replacement can create an audit finding.

- Before the change, ask finance which records support capitalisation today and get the external auditor's view.
- A common replacement: label every work item by product and as capitalisable or not, and record team time per product from rosters or a light weekly allocation. Throughput then replaces points for forecasting.
- Change the time-recording rule and the planning method on the same date, so one quarter is not left without evidence.

See [technology budget and cost](../strategy/technology-budget-and-cost.md).

### If you run a scaling framework

Many large organisations run SAFe or a similar framework with release trains and program increments.

- **Keep** the shared cadence, the joint review across teams and the dependency board.
- **Drop** fixed program increments of committed features. Replace the commitment with outcome goals per train and a throughput forecast given as a range.
- **Shorten** big-room planning to dependency and risk work. Teams do their own detailed planning.
- **Check after two increments** whether cycle time and change fail rate improved. Keep what moved the numbers.

### Roles that change

| Role today | What changes | Where it usually goes |
|---|---|---|
| Scrum Master | Fewer ceremonies to run | Flow or delivery lead for several teams, engineering manager, or product operations |
| Agile coach | Less ceremony training | Coaching on flow metrics, specs and review practice, for a fixed period |
| Release manager | Releases become continuous | Platform team owning the delivery pipeline and its controls |
| Tester | More generated code to check | Quality engineering: test design, evaluation sets, exploratory testing |

Write a plan per person before you change the role, agreed with HR. Where employee representatives exist, consult them before the change, not after (see [transition playbook](../strategy/transition-playbook.md)).

### Supplier contracts priced in effort

If suppliers bill in person-days, a faster way of working can raise your cost per outcome or hand the gain to the supplier. At renewal, move to capacity or outcome pricing and make the supplier work to the same definition of done. See [suppliers and contracts](../strategy/suppliers-and-contracts.md).

## A 90-day transition from ceremonies to flow

| Weeks | Change | Check |
|---|---|---|
| 1 to 2 | Record baselines: lead time, cycle time, rework rate, change fail rate, one user outcome, a team survey. Map the board to how work really flows. Agree with finance how capitalisation evidence will be kept. | Baseline dashboard exists; finance has agreed in writing |
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
- Finance has agreed how development cost is recorded for capitalisation before estimation or time recording changes.

### Assured

- Specs, decisions and evaluation results linked to pull requests and releases, so the audit trail comes from the delivery system.
- The definition of done includes the controls auditors test. See [agile and Scrum](agile-and-scrum.md) for regulated and public-sector settings.
- The external auditor has reviewed the replacement for story points or timesheets as capitalisation evidence before the change.
- Where employee representatives have rights over monitoring systems, the delivery dashboard and assistant telemetry are agreed with them before collection starts.

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
- METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", July 2025: https://arxiv.org/abs/2507.09089
- DORA, "Accelerate State of DevOps Report 2024": https://dora.dev/research/2024/dora-report/
- IFRS Foundation, IAS 38 Intangible Assets: https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/
- FASB, ASU 2025-06, Intangibles, Goodwill and Other, Internal-Use Software (Subtopic 350-40): https://www.fasb.org
