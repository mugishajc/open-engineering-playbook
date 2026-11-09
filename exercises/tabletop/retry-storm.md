# Tabletop: retry storm

A 2-second database failover turns into a 40-minute outage because every layer retries, the autoscaler adds more callers, and the load stays high after the database has recovered. This scenario tests load shedding, retry limits, safe recovery and the urge to "turn it all back on now". It is the kind of incident that tabletops about security and deploys never reach.

| | |
|---|---|
| Audience | Service owners and on-call engineers for the user-facing services and their database, platform or SRE engineers, the incident commander rotation, a product owner |
| Time | 90 minutes (10 brief, 60 play, 20 debrief) |
| Read first | [Scaling: overload protection](../../playbook/architecture/scaling.md#overload-protection), [incident management](../../playbook/reliability/incident-management.md), [rollbacks](../../playbook/reliability/rollbacks.md), [resilience testing](../../playbook/reliability/resilience-testing.md) |
| Facilitator notes | [Facilitator guide](facilitator-guide.md) |

## Setup

The organisation runs a food delivery marketplace in five cities, with 70 engineers. A request from the mobile app passes through an API gateway, an orders service and a pricing service before it reaches the shared PostgreSQL cluster. The mobile app retries failed requests 3 times. The gateway, the orders service and the pricing service each retry 3 times as well, with a fixed 100 ms wait. Each service autoscales on CPU, up to 40 pods. Each pod opens a pool of 20 database connections.

It is Friday at 19:00, the busiest hour of the week. All organisations, people and numbers here are fictional.

## Injects

### T+0 (19:04): a short blip

The database primary fails over to its replica. The failover takes 2 seconds, as designed. One minute later, the fast-burn SLO alert fires for ordering: 35% of requests fail with timeouts. Database CPU is at 100% and the connection count is at its limit.

**Decide:**
- Severity and incident commander.
- The database is healthy by every check. Why is it still at 100%?
- What is your first lever?

### T+15 (19:19): autoscaling makes it worse

The orders and pricing services have scaled from 12 to 40 pods each, because their CPU is high waiting on retries. Each new pod opens 20 more connections. Requests reaching the database are up about 20 times on a normal Friday. Customers keep pressing "Place order" in the app.

**Decide:**
- Do you cap or reverse the autoscaler? Who can do it, and through Git or by hand?
- Which requests do you shed first? Do you have priorities for them?
- Can you turn off retries without a deploy?

### T+30 (19:34): the obvious restart

An engineer proposes restarting every pod of every service "to clear the bad state". Another proposes failing back to the original database primary.

**Decide:**
- What happens if every pod restarts at once, with cold caches and empty connection pools?
- What is the order to bring traffic back, and how do you know each step held?

### T+45 (19:49): "turn it all back on"

Load shedding is working: 30% of traffic is rejected with a polite message and the rest succeeds. The product owner asks to turn everything back on now because restaurants are calling.

**Decide:**
- What has to be true before you admit the next 20% of traffic?
- What do you tell restaurants and customers in the meantime?

### Optional injects

- **T+10:** The dashboards for the orders service are 4 minutes behind, because the metrics backend is also struggling.
- **T+25:** The mobile app has no server-side switch for its retry count. The fix needs an app store release.

## Discussion questions

1. How many layers retry in your busiest request path, and how many attempts reach the database for one user tap?
2. Do you have a retry budget, and does any client respect `Retry-After`?
3. Can you shed low-priority traffic without a deploy?
4. Does your autoscaler scale on a signal that rises when a dependency is slow?
5. Have you ever tested recovery from overload, not only the failover itself?

## What good looks like

- SEV1 declared within 15 minutes, with the IC asking "what keeps the load high?" rather than "what broke?" ([incident management](../../playbook/reliability/incident-management.md)).
- Load shed early by priority, with 503 and `Retry-After`, before anyone debugs ([scaling](../../playbook/architecture/scaling.md#overload-protection)).
- Autoscaling capped for services whose bottleneck is the database; more callers do not help a saturated dependency.
- Retries cut to one layer, through configuration or a flag.
- Traffic brought back in steps (for example 20% at a time, holding 5 minutes each), not by restarting everything at once.
- The postmortem lists the retry design, the autoscaling signal and the missing priorities as contributing factors, not the 2-second failover ([postmortems](../../playbook/reliability/postmortems.md)).

## Scoring rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Diagnosis | Treated as a database fault | Saw the retries late | Named the retry and autoscaling feedback loop by T+15 |
| Load shedding | None | Shed late or at random | Shed by priority, early, with a message to users |
| Autoscaling | Let it run | Capped late | Capped by T+20, with the reason logged |
| Recovery | Restarted everything at once | Stepwise but with no checks | Stepwise, with a measure for each step |
| Communication | Silent to customers and restaurants | Late or vague | Cadence kept; product owner given a clear rule for reopening |
| Learning | "The database failed" | Some factors | Retry design, autoscaling signal and priorities all listed |

Maximum 12.

## Follow-up actions

- Retry at one layer only, with backoff, jitter and a retry budget; remove the others ([scaling](../../playbook/architecture/scaling.md#overload-protection)).
- Add request priorities and a load-shedding switch the IC can turn on.
- Scale on a signal that does not rise when a dependency is slow, and cap the database connections all pods can open together.
- Add a server-side setting for client retry counts in the mobile app.
- Run a game day that fails over the database at peak-like load in staging ([resilience testing](../../playbook/reliability/resilience-testing.md)).
