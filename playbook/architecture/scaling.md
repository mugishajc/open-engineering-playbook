# Scaling

"The system slows down every month-end, and the proposed fix is to split it into microservices." Scale in a fixed order: measure first, fix the slow query or code path, then cache, queue or scale out (whichever the measurement points to), and only then partition data or split services. Each stage is cheaper and less risky than the next. Most systems never need the last two steps, and a well-structured modular monolith serves many organisations better than a fleet of services they cannot operate.

## Outcomes

Starting points. Tune them to your organisation.

- Every user-facing service has a load test that runs at least monthly and before major releases, at 2 times the highest observed peak.
- Capacity forecasts cover the next 12 months and are reviewed every quarter. No capacity-related incident comes as a surprise to the forecast.
- Services keep enough headroom to carry forecast peak with one failure domain (zone or node pool) lost. Autoscaling covers growth, not this headroom.
- Every scaling change is justified by a measurement taken before it and checked by one taken after it.
- Latency SLOs (see [service levels](../reliability/service-levels.md)) hold at peak load.

## The order of operations

| Step | What to do | Typical cost |
|---|---|---|
| 1. Measure | Find where time goes: traces, database slow query logs, profiles. See [observability](observability.md). Guessing wastes weeks. | Hours |
| 2. Fix the query or code path | Add the missing index, remove N+1 queries, fetch less data, fix the algorithm, add pagination. | Days |
| 3. Cache | Cache expensive reads close to the caller: HTTP caching, an in-memory cache, a shared cache such as Redis or Valkey. See the caching rules below. | Days to weeks |
| 4. Queue | Move slow or bursty work out of the request path onto a queue. Return quickly, process in the background, make consumers idempotent. Cap retries with backoff, send poison messages to a dead-letter queue with an alert, alert on the age of the oldest message (not only on depth), and slow producers when consumers fall behind. See [events and messaging](events-and-messaging.md). | Weeks |
| 5. Scale out | Run more stateless instances behind a load balancer. Add read replicas for read-heavy databases. Autoscale on a signal that tracks load. For a stateless tier this is often a configuration change and can come before steps 3 and 4. | Days to weeks |
| 6. Partition | Split data by tenant, region or key (sharding), or split a component into its own service with its own data. | Months, and permanent operating cost |

Steps 3 to 5 can come in any order: pick by measurement. Scaling up (a bigger machine) is a valid step at any point. It is often the cheapest fix for a database, and it buys time to do the next step properly.

Caching rules:

- Key every entry by tenant and permission scope as well as by the request. If the answer depends on who asks, the key says who asks.
- Set a time to live on every entry, and decide per data set what users may see stale, and for how long.
- Protect against stampedes on expiry with request coalescing or early refresh with jitter.
- Size so a cold cache (after a restart or flush) does not take down the database behind it. Test it.

## Load testing

- Model real traffic: the mix of endpoints, data sizes and user behaviour from production logs, not a single endpoint in a loop.
- Test against a production-like environment with production-sized data. Small test databases hide the slow queries.
- Run three kinds of test: load (expected peak), stress (find the breaking point) and soak (normal load for hours to find leaks).
- Tools such as k6, Gatling, Locust and Apache JMeter can all run from CI and on-premises.
- Record results in the repository. A result without the date, build version and environment is not useful later.

## Capacity planning

- Forecast from business drivers (users, transactions, tenants, seasonal events), not only from last month's graph. Ask the business what is coming.
- Know the limiting resource for each service: CPU, memory, connections, disk I/O, a third-party rate limit, or a licence.
- On-premises and air-gapped, hardware lead times are long. Forecast at least 2 procurement cycles ahead.
- Protect the system when demand exceeds capacity: see overload protection below.

### Capacity maths

- **Size for one failure domain lost (N+1).** With N zones carrying equal load, losing one raises the load on the rest by N / (N - 1): 2 times for 2 zones, 1.5 times for 3. So target utilisation at peak is at most (N - 1) / N of the safe limit: 50% for 2 zones, about 67% for 3. With a safe limit of 80% CPU and 3 zones, set the autoscaling target near 50% CPU.
- **Set the safe limit from a load test,** not at 100%. Latency rises sharply as utilisation approaches 100% because requests queue; the knee is often at 70% to 80% CPU.
- **Do not count on autoscaling during a zone or region event.** The remaining zones are often short of capacity at that moment, and scale-out takes minutes.
- **Size queues and pools with Little's law:** items in the system = arrival rate × time in the system. At 200 requests per second and 50 ms per database call, a service needs about 10 connections busy on average; set the pool above that with headroom, and below what the database can serve for all instances together.

### Overload protection

- **Deadlines.** Every network call has a timeout shorter than the caller's remaining deadline, and the remaining deadline is passed downstream.
- **Retries.** Retry at one layer only, with exponential backoff and full jitter, at most 3 attempts, and a retry budget: retries stay under 10% of requests to that dependency. Three layers each retrying 3 times send up to 27 times the load to the bottom layer. Do not retry an overload response (429, or 503 with `Retry-After`) before the time the header gives.
- **Priorities and load shedding.** Give every request a priority (for example critical, default, sheddable). When saturation passes a set level, measured by queue time or concurrency rather than CPU, reject sheddable requests first with 503 and `Retry-After`.
- **Degraded modes.** Define one for each Tier 1 user journey (cached prices, read-only mode, writes queued for later), behind a flag the incident commander can turn on. Test it in a game day (see [resilience testing](../reliability/resilience-testing.md)).
- **Recovery.** After an overload, bring traffic back in steps. A system can stay overloaded after the trigger has gone, because retries and cold caches keep the load high.

## Modular monolith or microservices

Start with a modular monolith unless you have a clear reason not to. It is one deployable unit with strict internal module boundaries: each module owns its data and exposes an interface, and other modules may not reach into its tables.

| Factor | Modular monolith fits | Separate services fit |
|---|---|---|
| Team size | One to a few teams | Many teams that need to deploy independently |
| Scaling needs | Components scale together | One component needs very different scale or hardware |
| Operations maturity | Limited on-call, monitoring and platform | Automated deploys, tracing, on-call per service already in place |
| Domain understanding | Boundaries still moving | Boundaries stable and well understood |
| Failure isolation | Acceptable to share a process | A failure in one part must not touch another |
| Regulatory or security separation | Not required | Different data classes or compliance scopes must be separated |

Decision rule (starting points). Split a module out when at least one is true for two quarters: its team is blocked by other modules' releases more than twice a month; a load test shows it needs different scaling or hardware; a regulator or data class requires separation. Merge two services when at least one is true: more than 30% of changes touch both; they must deploy together; one request makes more than 3 synchronous calls between them; they share tables. Record either move in an ADR.

Martin Fowler's "MonolithFirst" and "Microservice Prerequisites" set out the same reasoning: services add network calls, distributed data and operational load, and need monitoring, fast provisioning and automated deployment before they pay off. Enforce module boundaries in CI with architecture tests, so that splitting a module out later is a deployment change, not a rewrite. Record the decision in an [ADR](decision-records.md). For how architects run these trade-offs, see [architecture practice](architecture-practice.md).

## In the AI era

Model calls add a scaling dimension that CPU graphs do not show: each request has a token cost, takes seconds rather than milliseconds, and is limited by a provider's quotas or by GPU capacity you own. Plan them like any other scarce dependency (see [building with AI](../ai/building-with-ai.md) and [AI architecture patterns](../ai/ai-architecture-patterns.md)).

- **Budget per request.** Set a cost and a p95 latency budget for each AI-backed flow before load testing. Load-test with realistic prompt and response sizes; token counts, not request counts, drive cost and provider limits.
- **Provider rate limits are capacity.** Record each provider's requests-per-minute and tokens-per-minute quotas next to your other limiting resources. Alert at 70% of quota (starting point). Ask for quota increases weeks before a launch, not on the day.
- **Cache before you scale.** Cache identical requests and stable answers; use the provider's prompt caching for long, repeated system prompts and documents. Measure the hit rate and the saving per hit, and remove caches that do not pay for their storage and invalidation work.
- **Batch what can wait.** Classification, summarisation and embedding jobs that do not need an answer within seconds go on a queue and use batch interfaces where the provider offers them, which are usually cheaper.
- **Route by difficulty.** Send simple requests to a smaller model and escalate only when evaluations show the smaller one fails. Re-run evaluations whenever routing changes.
- **Degrade, do not fail.** When the provider is slow or quota is exhausted, shed or queue low-priority AI work, fall back to a cached answer or a non-AI path, and keep the core transaction working. Set timeouts on every model call and cap agent loop iterations.
- **Self-hosted models** turn the problem into GPU capacity planning: measure tokens per second per GPU at your target latency, and remember that GPU lead times on-premises can be months.

## Practice

### Foundation

- Measure before changing. Use the order of operations. Scale up before you scale out.
- One load test for the busiest user flow, run before major releases.
- A modular monolith with clear module folders and no cross-module database access.

### Standard

- Load tests in CI on a schedule, against a production-like environment, with results stored and compared over time.
- Quarterly capacity review per service: forecast, limiting resource, headroom, planned changes.
- Autoscaling for stateless services, with tested minimum and maximum limits.
- Overload protection on every service as set out above: deadlines passed downstream, retries at one layer with jitter and a retry budget, rate limits, circuit breakers, load shedding by priority.
- An [RFC](rfcs.md) before any partitioning or service split.

### Assured

- Capacity plans for critical services are approved by the service owner and kept as records.
- Stress test results show behaviour beyond peak, including graceful degradation, for systems that support critical or important functions.
- Recovery after overload is tested as part of disaster recovery exercises (see [backup and recovery](../reliability/backup-and-recovery.md)).

## Cloud, on-premises and air-gapped

- Public cloud makes scaling out fast but not free. Set budget alerts with autoscaling (see [FinOps](../platform/finops.md)).
- On-premises and air-gapped capacity is fixed between hardware purchases. Plan headroom and procurement earlier, and favour efficient code and caching over adding nodes.
- Load-testing tools and their scripts must be installed from internal mirrors in air-gapped networks.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Splitting into microservices to fix a slow query | Measure, then fix the query. |
| Caching without an invalidation plan | Decide expiry and invalidation per data set before adding the cache. |
| Shared cache keyed only on the request | Add tenant and permission scope to every key. |
| Retries at every layer with no budget | Retry at one layer, with jitter, under a 10% retry budget. |
| 70% CPU target across two zones | Size for one zone lost: at most half the safe limit for 2 zones, two thirds for 3. |
| Load tests with tiny data sets | Production-sized data, anonymised where needed. |
| Autoscaling with no upper limit | Set maximums and budget alerts. |
| Distributed monolith: services that must deploy together | Merge them back, or fix the boundaries. |

## Templates

- [ADR template](../../templates/docs/adr.md)
- [RFC template](../../templates/docs/rfc.md)
- [Kubernetes service baseline](../../templates/platform/k8s-service-baseline.yaml), with autoscaling and disruption budget

## Sources

- Google SRE book, "Handling Overload": https://sre.google/sre-book/handling-overload/
- Google SRE book, "Addressing Cascading Failures": https://sre.google/sre-book/addressing-cascading-failures/
- AWS Builders' Library, "Timeouts, retries, and backoff with jitter": https://aws.amazon.com/builders-library/timeouts-retries-and-backoff-with-jitter/
- Martin Fowler, "MonolithFirst": https://martinfowler.com/bliki/MonolithFirst.html
- Martin Fowler, "Microservice Prerequisites": https://martinfowler.com/bliki/MicroservicePrerequisites.html
