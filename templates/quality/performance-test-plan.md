# Performance test plan: [service] [test type] [YYYY-MM-DD]

<!--
How to use: fill in sections 1 to 6 and get them reviewed before the run. Do not change the pass
criteria after seeing results; if they were wrong, record that in section 9 and plan another run.
Commit the completed plan and results to the service repository.
Guidance: playbook/quality/performance-testing.md and playbook/architecture/scaling.md
-->

| Field | Value |
|---|---|
| Service | [name] |
| Tier | [Tier 1 / Tier 2 / Tier 3] |
| Test owner | [name] |
| Build version and artifact digest | [version, sha256:...] |
| Environment | [name; link to parity list] |
| Planned date and time window | [YYYY-MM-DD HH:MM to HH:MM, time zone] |
| Stop person (for tests in production or shared environments) | [name] |

## 1. The question

One question this test answers. Pick the test type that answers it.

- Question: [Can we carry forecast peak for month-end with one zone lost?]
- Test type: [load / stress / spike / soak / failover under load / benchmark / capacity / volume]

## 2. Workload model

Taken from production logs and traces for [date range], plus business forecast.

| Transaction | Share of traffic | Peak arrival rate (per second) | Payload or data notes |
|---|---|---|---|
| [view account] | [%] | | |
| [make payment] | [%] | | |
| [export statement (rare, expensive)] | [%] | | |

- Load model: [open (arrival rate) / closed (fixed users), with reason]. Closed only: users = arrival rate × (response time + think time) = [ ]
- Peak used: [highest observed peak per second, date]; multiplier: [2 times, or forecast]
- Sessions and think time: [distribution taken from real sessions, not one fixed value]
- Data shape: [record counts, large tenants, hot keys, file sizes]
- Background jobs running during the test: [ ]
- Third parties: [stubbed with latency distribution from ___ / provider sandbox with written agreement]

## 3. Load profile

| Phase | Duration | Arrival rate or users |
|---|---|---|
| Warm-up (reported, not judged) | | |
| Ramp | | |
| Hold | | |
| [Steps, spike or failover event] | | |
| Ramp down and recovery | | |

## 4. Pass criteria (tied to SLOs)

| Measure | Threshold | Source |
|---|---|---|
| 95th percentile latency, [transaction] | Under ___ ms | Latency SLO |
| 99th percentile latency, [transaction] | Under ___ ms | Latency SLO |
| Error rate | Under ___% | Availability SLO |
| Throughput achieved | At least ___ per second (the planned rate) | Workload model |
| Requests the tool skipped or sent late (dropped iterations) | Zero | Load tool |
| Samples per transaction in the measured window | At least 10,000 for a 99th percentile | |
| CPU, memory, connection pools, queue age | Below safe limits: ___ | Capacity plan |
| Soak only: trend over the run | No upward trend in memory, connections, latency | |
| Stress only: behaviour past the limit | Sheds load with 503 and Retry-After; recovers within ___ minutes | Overload protection |

## 5. Data and environment

- Data set: [synthetic at volume / masked copy, approval link, deletion date]
- Environment matches production in: [instance types, versions, configuration, topology]. Differences: [ ]
- Shared parts tested at full production load (database, cache, queues, third-party limits): [Yes / No, so their limit is unknown]
- Load generators: [tool, version, location, count]; generator CPU kept under 70%; latency measured from the intended send time: [Yes/No]

## 6. Monitoring and abort criteria

- Dashboards open during the run: [links]
- Abort if: [error rate above ___ for ___ minutes; SLO burn rate above ___; any effect on real users]
- People informed: [on-call, dependent teams, cloud or CDN provider if their rules require]

## 7. Results

| Run | Date | Build | Samples | 50th / 95th / 99th / max latency | Error rate | Throughput | Limiting resource | Pass (Yes/No) |
|---|---|---|---|---|---|---|---|---|
| 1 | | | | | | | | |
| 2 | | | | | | | | |
| 3 | | | | | | | | |

Raw results and graphs: [link]

## 8. Capacity statement

[One instance holds the 99th percentile under ___ ms up to ___ requests per second (safe limit). At forecast peak of ___ with ___ zones and one lost, we need ___ instances.]

Instances per zone = forecast peak ÷ (zones minus 1) ÷ safe limit per instance, rounded up. Total = that × zones. Worked example in [performance testing](../../playbook/quality/performance-testing.md#from-results-to-capacity).

## 9. Findings and actions

| Finding | Action | Owner | Due |
|---|---|---|---|
| | | | |
