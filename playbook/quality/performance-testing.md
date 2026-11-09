# Performance testing

The problem: "The load test passed. On launch day the service fell over at a third of the tested load." That usually means the test answered the wrong question: one endpoint in a loop, a small database, averages instead of percentiles, and a tool that slowed down when the system did. Start every performance test from a written question, build the workload from production data, drive load by arrival rate, and judge the result in percentiles against the service's SLOs. Capacity maths and overload protection are in [scaling](../architecture/scaling.md); this page is about testing them.

## Outcomes

Starting points. Tune them to your services.

| Signal | Starting target |
|---|---|
| User-facing Tier 1 and Tier 2 services load tested at 2 times the highest observed peak | Monthly and before major releases, as in [scaling](../architecture/scaling.md) |
| Test plans that state the question, workload model and pass criteria before the run | 100% |
| Results stored with date, build version, environment and workload model | 100% |
| 95th and 99th percentile latency at tested peak | Within the latency SLO threshold, with errors within the error budget rate |
| Soak test before major releases of Tier 1 services | At least 4 hours, and long enough to cover every scheduled job and cache expiry cycle |
| Hot code paths with a benchmark in CI | Fail on a regression of more than 10% against the stored baseline |

## Start from a question

Each test type answers a different question. Write the question in the [performance test plan](../../templates/quality/performance-test-plan.md) before you write the script.

| Question | Test | Load shape | Passes when |
|---|---|---|---|
| Can we carry the forecast peak? | Load | Ramp to 2 times the highest observed peak (or the forecast peak if higher), hold 30 to 60 minutes | Latency percentiles and error rate inside SLO thresholds; no resource above its safe limit |
| Where does it break, and how? | Stress | Step up by 10% to 20% every few minutes until an SLO fails | Breaking point recorded; the service sheds load with 503 and `Retry-After`, does not crash, and recovers when load drops |
| Does it survive a sudden burst? | Spike | Jump from normal to 3 to 5 times normal in under a minute | Errors stay within budget during scale-out; queues drain; time to recover recorded |
| Does it degrade over time? | Soak (endurance) | Normal to peak load for 4 to 24 hours | No upward trend in memory, connections, file handles, disk, queue age or latency |
| Can we carry peak with a zone lost? | Failover under load | Peak load, then remove one zone or node pool | Remaining capacity holds the SLO; see [resilience testing](../reliability/resilience-testing.md) |
| Is this change slower? | Benchmark or regression | Fixed, small load in CI | Within 10% of the stored baseline |
| How much does one instance carry? | Capacity | Increase load on a single instance until the SLO fails | Safe limit per instance recorded and fed into the capacity plan |
| Does it cope with a year of data? | Volume | Production-sized or forecast data, normal load | Queries, batch jobs and reports finish inside their windows |

## The workload model

The workload model decides whether the test means anything. Build it from production logs and traces, and from what the business says is coming.

- **Transaction mix.** The endpoints or user actions that make up about 90% of peak traffic, with their share, plus the rare expensive ones: reports, exports, searches with wide filters, bulk uploads.
- **Arrival rate** per transaction at the peak minute, not the daily average. The peak minute can be far above the hourly average; measure yours.
- **Sessions and think time** for user flows, so caches, sessions and connection pools see realistic reuse. Take think time from the gaps between requests in real sessions, as a distribution, not one fixed value. A fixed think time makes every virtual user act in step and creates load waves that real users do not.
- **Data shape.** Realistic cardinality and skew: a few very large tenants, hot keys, long lists, large files. Requests spread across many records, not the same ID every time.
- **Background work** that runs at the same moment in production: batch jobs, imports, backups, cache rebuilds.
- **Business events.** Salary day, month-end, tax deadlines, enrolment periods, campaigns. Ask the business; see [capacity planning](../architecture/scaling.md#capacity-planning).
- **Third-party calls.** Stub them with response times drawn from their real latency distribution. Never load test someone else's service without their written agreement.

## Open and closed load models

A closed model runs a fixed number of virtual users, each waiting for a response before sending the next request. When the system slows, the users send less, so the tool reduces the load exactly when the system is struggling. The requests that would have been sent during a stall are never sent, so their long waits are never measured. Gil Tene named this coordinated omission. It makes the 99th percentile look far better than users experience.

Real users of internet-facing services do not wait for each other. Use an open model, where you set the arrival rate and the tool keeps sending at that rate however slow the responses are. k6 (arrival-rate executors) and Gatling (open injection profiles) support it directly; check how your tool does it. Two checks make an open model honest:

- **Measure from the intended send time**, not from when the request actually left. A tool that falls behind its schedule hides the delay otherwise. wrk2 and HdrHistogram correct for this; check what your tool does.
- **Watch for dropped requests.** If the tool runs out of virtual users or connections, it skips requests (k6 reports these as `dropped_iterations`). Any skipped requests mean the test did not deliver the planned rate, so it has not passed.

Use a closed model only for systems with a fixed user population, such as a call centre application with a known number of agents. Then size it with Little's law: users = arrival rate × (response time + think time). For 50 requests per second, 0.5 seconds response time and 9.5 seconds think time, you need 500 users. If response time grows to 2.5 seconds, the same 500 users send only about 42 requests per second (500 / 12): the test quietly stopped testing peak.

## Measuring correctly

- **Percentiles, not averages.** Report the 50th, 95th and 99th percentiles and the maximum. An average hides the slow requests that users notice. A page that makes 20 backend calls meets the backend's 99th percentile on about 18% of page loads (1 minus 0.99 to the power 20), so the tail is what users see.
- **Enough samples for the percentile.** The 99th percentile of 1,000 requests rests on the slowest 10. Collect at least 10,000 requests per transaction in the measured window before you judge a 99th percentile (starting point), and say how many you had.
- **Never average percentiles** across instances or time windows. Compute them from histograms or raw samples.
- **Report latency with throughput and error rate.** A fast error is not good latency. Count only successful requests in the latency SLI, and count every timeout and error against the error rate, so slow failures do not drop out of both numbers.
- **Measure where the user does**: at the load balancer or gateway, as in [service levels](../reliability/service-levels.md), and on the client for front ends.
- **Watch every resource** for utilisation, saturation and errors (Brendan Gregg's USE method): CPU, memory, connection pools, threads, disk, network, queue depth and age, third-party rate limits.
- **Check the load generator.** Keep its CPU under 70% (starting point) and run it close to where users connect from. A saturated generator reports its own slowness as yours.
- **Exclude warm-up from pass criteria but report it.** Cold caches and just-in-time compilation are real after every deploy.
- **Repeat.** Run each load test at least 3 times (starting point) and compare. One run is an anecdote.

## Environment and data

- **Production-like**: the same instance types, configuration, versions and topology as production. Record every difference on the parity list in the plan.
- **Do not scale results linearly.** If you test at a fraction of production, test one complete instance or cell at full load and extrapolate only the parts that scale out. Shared parts (the database, caches, queues, the network, third-party rate limits) do not shrink with the test, so test them at full production load or treat their limit as unknown.
- **Production-sized data**, generated synthetically at volume or masked through an approved process. See [test data and environments](test-data-and-environments.md). Small databases hide slow queries.
- **Testing in production** answers questions no copy can, but needs the safety rules from [resilience testing](../reliability/resilience-testing.md#standard): a low-traffic window, synthetic accounts marked as test traffic and excluded from business reports, abort criteria tied to the SLO, a named stop person, and on-call informed.
- **Tell your providers.** Read your cloud provider's and content delivery network's rules on load testing. Large tests can trigger denial-of-service protection or breach terms.

## Front ends and mobile

Server latency is only part of what users wait for.

- **Core Web Vitals** measure loading (Largest Contentful Paint), responsiveness (Interaction to Next Paint) and visual stability (Cumulative Layout Shift). Google's "good" thresholds are 2.5 seconds, 200 milliseconds and 0.1, at the 75th percentile of page loads.
- **Budgets in CI.** Set budgets for page weight, script size and lab metrics, and check them on each pull request (for example with Lighthouse CI). Confirm with real-user monitoring, which shows field data at the 75th percentile.
- **Test on the devices and networks your users have.** Many users have low-cost phones and slow or expensive mobile data. Test on a throttled network profile and a low-end device, not only on an engineer's laptop.
- **Mobile apps:** measure cold start time, frame rendering and battery and data use on representative devices.

## Performance checks in the pipeline

| When | What | Budget |
|---|---|---|
| Every pull request | Micro-benchmarks for hot code paths; front-end budgets | Inside the 10-minute pipeline budget |
| Merge to `main` or nightly | A short load test (5 to 10 minutes) at fixed arrival rate against an ephemeral or staging environment | Alert the owning team on a regression of more than 10% |
| Monthly and before major releases | Full load, stress and spike tests | Results stored and compared with the last run |
| Before major releases of Tier 1 services | Soak test | 4 to 24 hours |

## From results to capacity

Turn each result into a capacity statement the business can use. Example: "One instance holds the 99th percentile under 400 ms up to 180 requests per second, its safe limit below the knee. Forecast peak is 2,000 requests per second. With 3 zones and one lost, 2 zones must carry 2,000, so each zone needs 6 instances (1,000 divided by 180, rounded up): 18 in total." The maths behind this, including Little's law for pools and queues, is in [scaling](../architecture/scaling.md#capacity-maths).

## In the AI era

Features that call language models scale on tokens, not requests, and are limited by provider quotas. Set cost and latency budgets per flow and load-test with realistic prompt and response sizes, as [scaling](../architecture/scaling.md#in-the-ai-era) sets out. Do not load test a model provider beyond your quota or without agreement: stub the model with recorded latency and token distributions for most runs, and run a small real test inside your quota to confirm the stub.

## Practice

### Foundation

- One load test for the busiest user flow, run before major releases, with an arrival-rate model.
- Pass criteria written before the run, in percentiles.
- Results committed to the repository with date, build and environment.
- Front-end budgets for page weight and Core Web Vitals on the main pages.

### Standard

- A workload model per service from production data, reviewed every 6 months and before known peak events.
- Load, stress, spike and soak tests on the schedule above, against a production-like environment with production-sized data.
- Short load tests and benchmarks in the pipeline, with stored baselines and alerts on regression.
- Capacity statements from test results feed the quarterly capacity review in [scaling](../architecture/scaling.md#standard).

### Assured

- Stress tests show how systems that support critical or important functions degrade and recover beyond peak. Keep the plans and results as records.
- For EU financial entities, performance testing is one of the tests listed for the digital operational resilience testing programme in Regulation (EU) 2022/2554 (EU DORA), Article 25.
- Capacity plans for critical services are approved by the service owner, using tested safe limits.

## Cloud, on-premises and air-gapped

- **Cloud:** load generators in the cloud cost money and egress. Generate load from the same region as users, or from several regions if users are spread out, and tear generators down after the run.
- **On-premises:** run generators inside the network on separate hardware from the system under test. A performance lab that matches production hardware is expensive; if you cannot have one, test in production with the safety rules above.
- **Air-gapped:** install load tools and their scripts from internal mirrors. Capacity is fixed between hardware purchases, so test results drive procurement 2 cycles ahead.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| One endpoint in a loop | Workload model from production: mix, rates, data shape, background jobs. |
| 100 virtual users with think time, called "peak" | Open model at the measured peak arrival rate. |
| Average latency in the report | 50th, 95th and 99th percentiles and maximum, with error rate. |
| Pass criteria decided after seeing the results | Write them in the plan, tied to SLOs, before the run. |
| A small test database | Production-sized synthetic or masked data. |
| One performance test, the week before launch | Short tests in the pipeline; full tests monthly. |
| A saturated load generator | Watch its resources; add generators. |
| A half-size environment, results multiplied by two | Test one full instance at full load; test shared parts at production load. |
| A 99th percentile from a few hundred requests | At least 10,000 requests per transaction, or report a lower percentile. |
| Load testing a third party's API without asking | Stubs with real latency, or a written agreement. |

## Templates

- [Performance test plan](../../templates/quality/performance-test-plan.md)
- [Production readiness review](../../templates/docs/production-readiness-review.md), capacity and performance section
- [Test strategy](../../templates/quality/test-strategy.md)

## Sources

- Grafana k6, open and closed models: https://grafana.com/docs/k6/latest/using-k6/scenarios/concepts/open-vs-closed/
- Gil Tene, wrk2 and coordinated omission: https://github.com/giltene/wrk2
- HdrHistogram: https://hdrhistogram.github.io/HdrHistogram/
- Gatling documentation: https://docs.gatling.io/
- Apache JMeter: https://jmeter.apache.org/
- Locust documentation: https://docs.locust.io/
- Google SRE book, "Service Level Objectives" (percentiles): https://sre.google/sre-book/service-level-objectives/
- Brendan Gregg, the USE method: https://www.brendangregg.com/usemethod.html
- John D. C. Little, "A Proof for the Queuing Formula: L = λW", Operations Research 9(3), 1961.
- web.dev, Web Vitals: https://web.dev/articles/vitals
- Lighthouse CI: https://github.com/GoogleChrome/lighthouse-ci
- Regulation (EU) 2022/2554 (EU DORA): https://eur-lex.europa.eu/eli/reg/2022/2554/oj
