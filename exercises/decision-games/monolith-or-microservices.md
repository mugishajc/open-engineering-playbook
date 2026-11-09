# Decision game: monolith or microservices

You are the CTO. The application is slow at month-end, deployments are painful, five teams trip over each other, and a new VP of Engineering has a plan to split everything into fourteen microservices. The board likes the plan because it sounds modern. Choose a path, then open the consequences. There is a second decision after the first.

| | |
|---|---|
| Who | CTOs, VPs of engineering, principal engineers and architects. Play alone, or as a leadership group that must agree on one option. |
| Time | 20 to 30 minutes alone; 45 minutes as a group |
| Practice it teaches | [Scaling](../../playbook/architecture/scaling.md), [architecture practice](../../playbook/architecture/architecture-practice.md), [legacy modernisation](../../playbook/architecture/legacy-modernisation.md), [decision making](../../leaders/decision-making.md) |

## The situation

The company sells field-service scheduling software to 1,800 business customers. It has 35 engineers in five product teams. The product is one web application on one database, nine years old. All organisations, people and numbers here are fictional.

- In the last two days of each month, when customers run invoicing, p95 response time rises from 400 ms to 6 seconds across the whole product.
- A deployment takes 50 minutes, runs twice a week, and about one in five causes a rollback.
- Teams wait for each other's changes. Two teams edit the same "jobs" module in most sprints.
- Nobody has profiled the month-end slowdown. The monitoring shows the database at 95% CPU.
- The new VP proposes 14 services on Kubernetes in 12 months, with a platform team of 4 hired for it. The board has approved the headcount in principle.
- Revenue depends on shipping two large features this year that customers have been promised.

## Round 1: what do you do?

**A. Extract invoicing now.** Invoicing is where the month-end pain is. Give it its own service and database, run it on its own hardware, and leave the rest of the product alone. One extraction, aimed at the problem, done in a quarter.

**B. Buy time with hardware.** The database is at 95% CPU. Move it to a machine twice the size this week. It costs money, not engineering time, and the two promised features stay on track.

**C. Approve the 14-service plan.** Five teams cannot keep sharing one deployable. Build the platform, then carve out services so each team deploys on its own. The board has funded the headcount, and every quarter of delay makes the split harder.

**D. Keep one application and restructure it.** Spend a week profiling month-end and fix what it finds. Then split the code into modules that own their tables, with a CI rule against crossing them, and cut the pipeline time. Revisit services in 6 months.

Pick one before you open the consequences.

<details>
<summary>Consequences of A: extract invoicing now</summary>

Better aimed than C, but before anyone measured. The extraction takes 5 months, because invoicing reads tables owned by jobs, customers and pricing, and every one of those reads becomes an API call or a copied data set. Month-end improves a little, because invoicing runs on its own hardware, but the root problem (the N+1 query) moved with the code. The team now runs two deployables, two databases and the data synchronisation between them. One promised feature slips.

Extraction is the right tool once you know a component needs very different scale, data separation or independent deployment. Here, nobody knew yet. See the decision table in [scaling](../../playbook/architecture/scaling.md#modular-monolith-or-microservices).

</details>

<details>
<summary>Consequences of B: bigger database</summary>

It works, for a while. Month-end p95 drops to 2.5 seconds, and nothing else changes. The bill for the database doubles. Deployments are still 50 minutes, teams still collide, and in eight months the customer base has grown enough that month-end is back to 5 seconds.

Scaling up is a valid step, and the [scaling](../../playbook/architecture/scaling.md#the-order-of-operations) page says so: it is often the cheapest fix and it buys time. The mistake is using the time for nothing. Combined with D, B is a good first week.

</details>

<details>
<summary>Consequences of C: approve the 14-service plan</summary>

The platform takes 7 months instead of 3, because the team is learning Kubernetes, service mesh and distributed tracing at the same time. The first three services are carved out along the old code's folder structure, not along the business domain, so they call each other synchronously and must deploy together: a distributed monolith. Month-end gets worse, not better: the invoicing run now makes thousands of network calls where it made database joins. The two promised features slip into next year. At month 12, five services are live, the monolith still exists, and the team now runs both.

Nobody profiled the slowdown, so nobody knew the system needed a fix, not a new architecture. This is the first anti-pattern on the [scaling](../../playbook/architecture/scaling.md#anti-patterns) page.

</details>

<details>
<summary>Consequences of D: restructure one application</summary>

Two engineers spend a week profiling the month-end run. They find one report that loads every job for a customer and then queries each job's line items one by one (an N+1 query), plus a missing index on the invoice lines table. The fix ships in the third week. Month-end p95 drops to 900 ms.

Over the next quarter, the teams draw module boundaries around jobs, scheduling, invoicing, customers and reporting. A CI architecture test fails any change where one module reads another's tables. The two teams that fought over "jobs" now own separate modules with an interface between them. Splitting the test suite and caching dependencies cuts the pipeline from 50 to 14 minutes, and deployments go daily. Both promised features ship.

The VP's platform headcount is redirected: two people improve CI and observability, and two join product teams. The VP is unhappy for a month. Go to round 2.

</details>

## Round 2: six months later

You chose D (or you are now catching up to it). The modular monolith works. Then a new requirement arrives: a large customer group in the health sector wants the product, but its contracts require that patient-related job notes are stored in a separate system, in-country, with separate access controls and audit. That data is 3% of the product.

**E. Keep everything in the monolith** and add encryption and access rules for the notes.

**F. Extract the notes module** into its own service and database, deployable per region, with its own access control.

<details>
<summary>Consequences of E and F</summary>

**E** fails the contract: the requirement is separate storage and separate access, not only encryption. Every engineer with access to the main database is now in scope of the health customers' audits.

**F** is the right extraction, for the right reason. "Regulatory or security separation required" is one of the factors in the [scaling](../../playbook/architecture/scaling.md#modular-monolith-or-microservices) table that favours a separate service. Because the notes module already had a clean boundary and owned its own tables, the extraction takes 6 weeks, not 6 months. Record the decision in an [ADR](../../templates/docs/adr.md) that names the driver, so nobody later uses it to justify splitting everything else.

</details>

## What the playbook recommends, and why

Measure, fix, then structure: **D in round 1, F in round 2.** The [scaling](../../playbook/architecture/scaling.md) page sets an order of operations: measure, fix the query or code path, then cache, queue or scale out as the measurement shows, and only then partition. Each stage is cheaper and less risky than the next. A modular monolith with enforced boundaries gives most of the team-independence benefits of services without the network calls, distributed data and operational load. It also makes a later extraction a deployment change instead of a rewrite.

Separate services pay off when a component needs very different scale, separate failure isolation, separate compliance scope, or independent deployment by many teams, and when the organisation already has automated deployment, tracing and on-call per service. Name the reason in an ADR each time.

For the leadership part (telling a new VP and a board that the exciting plan is not the first step), see [decision making](../../leaders/decision-making.md) and [architecture practice](../../playbook/architecture/architecture-practice.md).

## Debrief questions

1. What evidence would you have needed to choose C with confidence?
2. Which of your systems has a known slow path that nobody has profiled?
3. If you split a system into services in the past, which of them always deploy together?
