# Kata: write the ADR

Read a short scenario, then write an architecture decision record (ADR) for it using the playbook's template, in 30 minutes. The scenario has a tempting popular answer and a less exciting one that fits the constraints better. The point is not to pick the "right" technology. It is to write down the context, the options, the choice and its costs so clearly that someone joining in two years understands why.

| | |
|---|---|
| Who | One engineer or a pair. Good practice for anyone who will propose an ADR or review one. |
| Time | 45 minutes: 30 to write, 15 to compare with the model answer |
| Practice it teaches | [Decision records](../../playbook/architecture/decision-records.md), [ADR template](../../templates/docs/adr.md), [cloud, on-premises and air-gapped](../../playbook/platform/cloud-on-prem-air-gapped.md) |

## The scenario

A scale-up of 70 engineers sells route-planning software for delivery fleets. Most customers use the SaaS version on a public cloud. Nine large customers run it on-premises, and two of those run it on air-gapped networks. Every installation, cloud or on-premises, runs the same release built from the same code.

The team is building a notifications service. When a delivery's estimated arrival time changes, the service sends an SMS or email to the recipient. Facts the team has gathered (all fictional):

- Expected load: 40 jobs per second on average, 300 per second at the morning peak, across all SaaS tenants. On-premises sites are much smaller.
- A job must not be lost if a process restarts. Sending a message twice is annoying but acceptable; never sending it is not.
- The job is created in the same database transaction that updates the delivery's ETA. Today the team does this with a "dual write" (update the database, then publish to a queue), and twice last quarter a crash between the two steps lost notifications.
- Every installation already runs PostgreSQL, operated by the customer's DBAs on-premises.
- The platform team has 5 engineers and supports all 9 on-premises customers. On-premises customers must approve any new component, which takes 3 to 6 months.
- An engineer has proposed Apache Kafka. Another suggests the cloud provider's managed queue. A third suggests RabbitMQ.
- In a staging test, a PostgreSQL table used as a job queue, with workers claiming jobs using `SELECT ... FOR UPDATE SKIP LOCKED`, handled 1,200 jobs per second on the current database size.

## Your task

1. Copy the [ADR template](../../templates/docs/adr.md). Name the file `0014-job-queue-for-notifications.md`.
2. Fill in: context and problem statement, decision drivers, considered options (at least three, plus "do nothing"), decision outcome, consequences (at least one cost), confirmation, and pros and cons.
3. Keep it under two pages. Link nothing you have not read.
4. Before you open the model answer, check your draft against this list:
   - Does the context state facts and constraints, not the conclusion?
   - Would someone who disagrees with your choice agree that the options were described fairly?
   - Does the consequences section name what gets harder?
   - Does "confirmation" say how you will know the decision still holds, with a number?
   - Is there a condition that would make you revisit it?

<details>
<summary>Model answer</summary>

```markdown
---
status: accepted
date: 2026-11-09
decision-makers: [notifications tech lead, platform team lead]
consulted: [two on-premises customer DBAs, security champion, SaaS operations]
informed: [all engineering, customer success for on-premises accounts]
---

# 0014. Use a PostgreSQL table as the job queue for notifications

## Context and problem statement

The notifications service must send a message when a delivery's ETA changes.
The job is created when the ETA is updated. Today we update the database and
then publish to a queue, and twice last quarter a crash between the two steps
lost notifications. The same release runs on our cloud SaaS and at 9 on-premises
customers, 2 of them air-gapped, all of which already run PostgreSQL. Adding a
new component on-premises needs customer approval, which takes 3 to 6 months.
Peak load is 300 jobs per second for all SaaS tenants combined.

## Decision drivers

- No lost jobs, including on process crash (at-least-once delivery)
- Job created atomically with the ETA update (no dual write)
- Same design on cloud, on-premises and air-gapped
- Operable by a 5-person platform team across 9 customer sites
- Headroom of at least 3 times current SaaS peak (900 jobs per second)

## Considered options

- A. PostgreSQL table as queue, workers claim jobs with SELECT ... FOR UPDATE SKIP LOCKED, using a maintained library
- B. RabbitMQ, with a transactional outbox table to avoid the dual write
- C. Apache Kafka, with a transactional outbox table
- D. Cloud provider's managed queue
- E. Do nothing: keep the dual write

## Decision outcome

Chosen option: A, because it is the only option that creates the job in the
same transaction as the ETA update without an extra outbox relay, runs
everywhere we ship today without a new component, and handled 1,200 jobs per
second in staging, 4 times current peak.

### Consequences

- Good, because lost notifications from the dual write stop.
- Good, because on-premises and air-gapped customers need no new component and no approval cycle.
- Bad, because queue load lands on the main database. Job rows churn, so we must
  watch table bloat and vacuum, and keep the queue table small by deleting
  completed jobs.
- Bad, because it is a work queue, not an event stream. If other services later
  need to consume ETA events independently, this design does not serve them.
- Neutral, because consumers must be idempotent under any option; we key each
  send on (delivery ID, ETA version).

### Confirmation

- Load test at 900 jobs per second runs monthly in CI against a production-sized database.
- Dashboards: queue depth, oldest job age, database CPU. Alert if the oldest job is older than 2 minutes.
- Revisit if sustained SaaS load exceeds 600 jobs per second, if database CPU
  from the queue exceeds 20%, or if a second consumer of ETA events appears.

Review date: 2028-11-09

## Pros and cons of the options

### A. PostgreSQL queue
- Good: transactional enqueue; no new component; known to every DBA we work with.
- Bad: shares capacity with the main database; lower ceiling than a dedicated broker.

### B. RabbitMQ with outbox
- Good: mature, purpose-built work queue; higher ceiling.
- Bad: new component at 9 sites and 3 to 6 months of approvals; outbox relay still needed.

### C. Kafka with outbox
- Good: event stream that many consumers can replay; very high throughput.
- Bad: far more capacity than we need; the heaviest component to operate on-premises and air-gapped; outbox relay still needed.

### D. Managed cloud queue
- Good: no operations work for SaaS.
- Bad: unavailable on-premises and air-gapped, so we would maintain two designs.

### E. Do nothing
- Bad: notifications keep getting lost on crashes.

## More information

- Related: ADR-0009 (PostgreSQL as the primary data store)
- Incident postmortems for the two lost-notification incidents last quarter
```

**What makes it good:** the context states facts, not the conclusion. Each option is described fairly, including the strengths of the ones not chosen. Two real costs are named. The confirmation section has numbers and three conditions that would reopen the decision. Kafka is not wrong in general; it is wrong for these drivers, and the ADR says which drivers.

**Common gaps in first drafts:**
- The air-gapped and on-premises constraint is missing, so the managed queue looks attractive.
- No mention of the dual write, which is the real reason a decision is needed now.
- Consequences list only benefits.
- No revisit condition, so the decision is never questioned again even when load grows.

</details>

## Going further

- Ask a colleague who prefers Kafka to review your ADR in a pull request, using the labels from [code review](../../playbook/delivery/code-review.md#comment-labels). If they agree the options are fair, even while disagreeing with the choice, the ADR did its job.
- Write the superseding ADR for the day load passes 600 jobs per second. What changes in the context?
- Find a decision in your own system that nobody can explain, and write its ADR now, marked with today's date and "recorded after the fact".
