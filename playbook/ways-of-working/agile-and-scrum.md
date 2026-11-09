# Agile and Scrum

The problem: "We do all the Scrum ceremonies and nothing improves." Stand-ups become status reports, retrospectives produce the same complaints, and velocity charts become targets. Keep the parts of agile that create fast feedback (small batches, working software shown to real users, retrospectives that change something) and drop the rituals that do not. Pick the method that fits the work: Scrum, Kanban or Shape Up are all valid; cargo-culting any of them is not.

When code becomes cheap to produce, the bottleneck moves to framing the problem, review, verification and learning from users. [Agile in the AI era](agile-in-the-ai-era.md) explains how planning and ceremonies change as a result.

## Outcomes

Starting targets. They measure feedback and flow, not ceremony attendance.

| Signal | Starting target |
|---|---|
| Working software shown to real users or their proxies | At least every 2 weeks |
| Retrospective actions completed by the next retrospective | At least 70% |
| Cycle time for a typical work item (start to done), 85th percentile | Under 10 working days |
| Work in progress per team | No more items in progress than people on the team |
| Time in recurring team meetings per engineer | Under 10% of the working week, as a starting point |
| Change lead time (DORA) | Under 1 week, trending down |

## What the sources actually say

- The **Agile Manifesto** (2001) is four values and twelve principles. It names no ceremonies, no roles and no tools. Its principles include delivering working software frequently, welcoming changing requirements, sustainable pace and regular reflection.
- The **Scrum Guide** (2020 edition, Schwaber and Sutherland) defines three accountabilities (Product Owner, Scrum Master, Developers), five events (the Sprint, Sprint Planning, Daily Scrum, Sprint Review, Sprint Retrospective) and three artifacts, each with a commitment (Product Backlog and Product Goal, Sprint Backlog and Sprint Goal, Increment and Definition of Done). It sets time-boxes: Sprints of one month or less, a 15-minute Daily Scrum, and maxima of 8 hours for planning, 4 hours for review and 3 hours for the retrospective in a one-month Sprint. **It does not mention story points or velocity.**
- **Kanban** manages flow: visualise work, limit work in progress, measure and improve cycle time and throughput. The Kanban Guide adds a service level expectation: how long items usually take.
- **Shape Up** (Basecamp, 2019) uses six-week cycles followed by a two-week cool-down, shapes work to a fixed time "appetite" rather than estimating it, and has a betting table decide what goes into each cycle.

## Keep and drop

| Keep | Why | Drop or change | Why |
|---|---|---|---|
| Short cycles with a clear goal | Forces small batches and frequent feedback | Sprint "commitment" to a list of tickets | Turns a forecast into a promise and hides learning |
| Showing working software to users | The only reliable test of value | Demo of slides or tickets moved | No feedback on the product |
| Retrospectives with one or two owned actions | The improvement engine | Retros that list complaints with no owner | Same complaints every time, and cynicism |
| A single ordered backlog | One place to say what matters most | A backlog of 500 items | Nobody reads it. Archive anything older than 6 months. |
| Daily sync on the goal and blockers | Coordination | Round-robin status reports to a manager | Use the board. Talk about blockers and the goal. |
| Definition of done | Shared quality bar | Hardening or "stabilisation" sprints | A sign that done did not mean done |
| WIP limits | Finishes work instead of starting more | Velocity as a performance target | Points inflate. See [planning and forecasting](planning-and-forecasting.md). |
| Product owner who makes decisions | Fast trade-offs | Product owner who only writes tickets | See [product partnership](product-partnership.md) |

## Practice

### Foundation

- **Pick a cadence.** Plan every 1 or 2 weeks, show the result, reflect, repeat. A solo engineer or a two-person startup can do this in 30 minutes on a Friday.
- **One board** with columns that match how work really flows, and a WIP limit on "in progress".
- **Retrospective rule.** Every retrospective ends with at most 2 actions, each with an owner and a date. The next retrospective starts by checking them.
- **Working agreement.** Write how the team works (hours, review times, definition of done, meetings) in the [team working agreement](../../templates/docs/team-working-agreement.md) and revisit it every quarter.

### Standard

- **Choose the method by the work.**

| Work type | Fits best |
|---|---|
| Product team with a stable goal and a steady stream of features | Scrum or Scrum with Kanban flow metrics |
| Platform, support or operations team with unplanned work | Kanban with a service level expectation |
| Product team that needs room to solve bigger problems without micro-planning | Shape Up style cycles |
| Several teams on one product | Shared goals and a joint review every cycle. Add a scaling framework only after simpler coordination has failed, and only the parts you need. |

- **Measure flow, not ceremonies.** Track cycle time, throughput, WIP and work item age. Look at the oldest items in progress at every daily sync.
- **Protect the goal.** Unplanned work goes through one person (a rotating interrupt handler) so the rest of the team keeps focus.
- **Engineers in discovery.** At least one engineer joins user research and shaping. See [product partnership](product-partnership.md).
- **Keep meetings short and few.** If total recurring meetings exceed about 10% of the week, cut or shorten one at the next retrospective.

### Assured

Agile methods work in regulated and public-sector settings. Evidence comes from the delivery system, not from extra documents:

- Requirements and decisions live in the backlog and [decision records](../architecture/decision-records.md), linked to pull requests and releases.
- The definition of done includes the controls auditors test (review, tests, security checks, change record).
- Public-sector teams follow the service standard that applies to them, for example the UK Government Service Standard (which expects iterative delivery by a multidisciplinary team) or the US Digital Services Playbook. See [public sector](../compliance/public-sector.md).
- For fixed-price or fixed-scope procurement, agree outcomes and a cadence of review with the buyer, and contract for capacity over time rather than a complete specification up front where the rules allow.

## Cloud, on-premises and air-gapped

The method does not change. Teams in air-gapped networks need their board, wiki and chat tools hosted inside the network, and should plan for slower dependency imports in their cycle length.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Agile transformation" that renames roles and adds meetings | Start from outcomes in the table above. Measure flow. |
| Velocity compared across teams | Points are team-local. Use throughput and cycle time, and do not compare teams. |
| Sprint goal is "finish tickets 101 to 117" | Write a goal a user would recognise. |
| Retros held, no action ever finished | Max 2 actions, owners, checked next time. |
| Hardening sprint every fourth sprint | Fix the definition of done. |
| Scaling framework installed before teams can ship on their own | Get one team shipping every week first. |

## Templates

- [Team working agreement](../../templates/docs/team-working-agreement.md)

## Sources

- Manifesto for Agile Software Development (2001): https://agilemanifesto.org/
- Principles behind the Agile Manifesto: https://agilemanifesto.org/principles.html
- The Scrum Guide (2020): https://scrumguides.org/scrum-guide.html
- The Kanban Guide: https://kanbanguides.org/
- Ryan Singer, Shape Up (Basecamp, 2019): https://basecamp.com/shapeup
- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
- US Digital Services Playbook: https://playbook.cio.gov/
