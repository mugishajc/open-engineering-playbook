# Scaling

"The system slows down every month-end, and the proposed fix is to split it into microservices." Scale in a fixed order: measure first, fix the slow query or code path, add caching, move work onto queues, scale out, and only then partition data or split services. Each step is cheaper and less risky than the next. Most systems never need the last two steps, and a well-structured modular monolith serves many organisations better than a fleet of services they cannot operate.

## Outcomes

Starting points. Tune them to your organisation.

- Every user-facing service has a load test that runs at least monthly and before major releases, at 2 times the highest observed peak.
- Capacity forecasts cover the next 12 months and are reviewed every quarter. No capacity-related incident comes as a surprise to the forecast.
- Services keep at least 30% headroom at forecast peak, or can scale out automatically within 5 minutes.
- Every scaling change is justified by a measurement taken before it and checked by one taken after it.
- Latency SLOs (see [service levels](../reliability/service-levels.md)) hold at peak load.

## The order of operations

| Step | What to do | Typical cost |
|---|---|---|
| 1. Measure | Find where time goes: traces, database slow query logs, profiles. See [observability](observability.md). Guessing wastes weeks. | Hours |
| 2. Fix the query or code path | Add the missing index, remove N+1 queries, fetch less data, fix the algorithm, add pagination. | Days |
| 3. Cache | Cache expensive reads close to the caller: HTTP caching, an in-memory cache, a shared cache such as Redis or Valkey. Decide expiry and invalidation per data set. | Days to weeks |
| 4. Queue | Move slow or bursty work out of the request path onto a queue. Return quickly, process in the background, make consumers idempotent. | Weeks |
| 5. Scale out | Run more stateless instances behind a load balancer. Add read replicas for read-heavy databases. Autoscale on a signal that tracks load. | Weeks |
| 6. Partition | Split data by tenant, region or key (sharding), or split a component into its own service with its own data. | Months, and permanent operating cost |

Scaling up (a bigger machine) is a valid step at any point. It is often the cheapest fix for a database, and it buys time to do the next step properly.

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
- Protect the system when demand exceeds capacity: rate limits, load shedding of low-priority work, timeouts and circuit breakers. The Google SRE book's chapters on handling overload and cascading failures describe these.

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

Martin Fowler's "MonolithFirst" and "Microservice Prerequisites" set out the same reasoning: services add network calls, distributed data and operational load, and need monitoring, fast provisioning and automated deployment before they pay off. Enforce module boundaries in CI with architecture tests, so that splitting a module out later is a deployment change, not a rewrite. Record the decision in an [ADR](decision-records.md). For how architects run these trade-offs, see [architecture practice](architecture-practice.md).

## Practice

### Foundation

- Measure before changing. Use the order of operations. Scale up before you scale out.
- One load test for the busiest user flow, run before major releases.
- A modular monolith with clear module folders and no cross-module database access.

### Standard

- Load tests in CI on a schedule, against a production-like environment, with results stored and compared over time.
- Quarterly capacity review per service: forecast, limiting resource, headroom, planned changes.
- Autoscaling for stateless services, with tested minimum and maximum limits.
- Overload protection on every service: timeouts, retries with backoff, rate limits, circuit breakers.
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
- Martin Fowler, "MonolithFirst": https://martinfowler.com/bliki/MonolithFirst.html
- Martin Fowler, "Microservice Prerequisites": https://martinfowler.com/bliki/MicroservicePrerequisites.html
