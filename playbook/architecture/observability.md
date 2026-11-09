# Observability

Instrument every service with OpenTelemetry for traces, metrics and logs, send the data through an OpenTelemetry Collector, and make every log line and trace carry the same correlation identifiers. Use open formats so you can change backends without re-instrumenting code, and set a cardinality budget so the bill stays predictable. Done this way, you learn about problems from your alerts, not from your users.

## Outcomes

Starting points. Tune them to your organisation.

- At least 80% of user-facing incidents are detected by alerts before a user reports them.
- 100% of production services meet the minimum signals list below before launch (checked in the [production readiness review](../reliability/production-readiness.md)).
- An on-call engineer can go from an alert to the relevant traces and logs for a failing request in under 5 minutes.
- Each service stays within its metric cardinality budget. Alerts fire at 80% of budget.
- Zero secrets and zero unmasked personal data in logs, checked by sampling every quarter.

## Minimum signals every service exposes

| Signal | Requirement |
|---|---|
| Resource attributes | `service.name`, `service.version`, `deployment.environment.name` on every span, metric and log, following OpenTelemetry semantic conventions |
| Health | Liveness and readiness endpoints. Readiness fails when a hard dependency is unavailable. |
| Request metrics | Rate, errors and duration (as a histogram) for every inbound endpoint, labelled by route template, not by raw URL |
| Dependency metrics | The same three for every outbound call: databases, queues, other services |
| Saturation | CPU, memory, connection pool use, queue depth: the resources that run out first |
| SLI metrics | The exact metrics your [service level objectives](../reliability/service-levels.md) are computed from |
| Build info | A metric or resource attribute with version and commit, so dashboards show which build is running |
| Traces | Spans for every inbound request and outbound call, with W3C Trace Context propagation |
| Logs | Structured JSON with the fields below, including `trace_id` and `span_id` |
| Dashboards and alerts | One dashboard from the golden path template. Alerts on SLO burn rate, not on every cause. |

These map to the four golden signals in the Google SRE book (latency, traffic, errors, saturation). For request-driven services the RED view (rate, errors, duration) covers the first three. For resources such as hosts and disks, use Brendan Gregg's USE method (utilisation, saturation, errors).

## Structured logging

Every log line is one JSON object with at least these fields.

| Field | Content |
|---|---|
| `timestamp` | RFC 3339 in UTC, with milliseconds |
| `severity` | One of `DEBUG`, `INFO`, `WARN`, `ERROR`, `FATAL` |
| `message` | Human-readable, constant text. Put variable data in fields. |
| `service.name`, `service.version` | Same values as the resource attributes |
| `trace_id`, `span_id` | From the active span, so logs and traces join |
| `event` | A stable, machine-readable name for the event, for example `payment.declined` |

- Log at `INFO` for business events and state changes, `WARN` for handled problems, `ERROR` for failures that need a human. Production runs at `INFO`.
- Never log secrets, tokens, full card numbers or passwords. Mask personal data by default and log identifiers rather than names. Enforce it with a logging library filter, not with good intentions.
- Audit events (who did what, when) go to a separate audit stream with its own retention and access controls.

## Correlation identifiers

- Propagate the W3C `traceparent` header on every HTTP call and the equivalent attribute on every message. OpenTelemetry instrumentation does this for supported libraries.
- When a request enters from outside, start a trace at the edge. Return the trace ID to the caller in error responses (see the Problem Details example in [API standards](api-standards.md)).
- For batch jobs and asynchronous flows, link spans across the queue so one business transaction is traceable from start to end.

## Cardinality budgets

Each unique combination of metric name and label values is a separate time series. Unbounded labels multiply series until the metrics system slows down or the bill grows sharply.

- Never use user IDs, email addresses, request IDs, raw URLs or timestamps as metric labels. Put them in traces and logs instead.
- Start with a budget of 10,000 active series per service instance group and adjust from measured use.
- Measure series per service in the metrics backend. Alert the owning team at 80% of budget. Review the top 10 series producers every month.
- Use the Collector to drop or aggregate labels before data leaves the cluster.

## Sampling and retention

| Data | Starting point |
|---|---|
| Traces | Keep 100% of error and slow traces (tail sampling in the Collector), 10% of the rest. Retain 7 to 14 days. |
| Metrics | Full resolution for 30 days, downsampled for 13 months to allow year-on-year comparison |
| Application logs | 30 days searchable. Longer only for a stated reason. |
| Audit logs | As long as your regulator or records policy requires, often 1 year or more, in tamper-evident storage |

## Practice

### Foundation

- Add the OpenTelemetry SDK with automatic instrumentation for your language. Export over OTLP.
- Use a single managed backend or a single self-hosted stack. Do not run two.
- Structured JSON logs with trace IDs. Health endpoints. One dashboard and one SLO burn-rate alert per user-facing service.

### Standard

- The [golden path](../platform/golden-paths.md) service template ships with OpenTelemetry, structured logging, health endpoints, a dashboard and default alerts already wired.
- An OpenTelemetry Collector runs as an agent per node and as a gateway per cluster or site. Services never send data straight to a vendor.
- Cardinality budgets are set per service and monitored.
- Dashboards and alert rules are stored as code in git and reviewed like code.
- The platform team owns the observability stack, with its own SLOs.

### Assured

- Logs that are evidence (audit, access, security events) are shipped off-host within 1 minute, stored write-once or hash-chained, and access to them is itself logged. This supports ISO/IEC 27001:2022 Annex A 8.15 (logging) and 8.16 (monitoring activities).
- Retention periods are written down per log type and enforced by the storage system, not by manual deletion.
- Personal data in telemetry has a documented legal basis, a retention period and a masking rule, under the data protection law that applies to you (for example EU GDPR or the Kenya Data Protection Act 2019).
- Clock synchronisation is monitored. Timestamps are evidence, and evidence with drifting clocks is weak.

## Cloud, on-premises and air-gapped

| Layer | Public cloud | On-premises or private cloud | Air-gapped |
|---|---|---|---|
| Instrumentation | OpenTelemetry SDKs | Same | Same, installed from internal mirrors |
| Pipeline | OpenTelemetry Collector | Same | Same. Only internal exporters. |
| Metrics | Managed Prometheus-compatible service or vendor | Prometheus with Thanos or Mimir for long-term storage | Same as on-premises |
| Logs | Managed log service or vendor | Loki, OpenSearch or Elasticsearch | Same as on-premises |
| Traces | Managed tracing or vendor | Tempo or Jaeger | Same as on-premises |
| Dashboards and alerts | Grafana or vendor UI | Grafana, Alertmanager | Grafana, Alertmanager, with paging through internal channels only |

In air-gapped networks, check every component for telemetry or licence checks that call home and turn them off. Run internal time servers, because trace timing and log ordering depend on synchronised clocks.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Alerts on every CPU spike, so on-call ignores them | Alert on symptoms users feel (SLO burn rate). Use cause metrics for diagnosis on dashboards. |
| User ID as a metric label | Move it to traces and logs. Enforce with a Collector rule. |
| Free-text logs that need regular expressions to search | Structured JSON with stable field names. |
| Each team picks its own vendor SDK | OpenTelemetry everywhere. Change backends at the Collector. |
| Logs full of personal data "for debugging" | Mask by default. Debug access to raw data goes through an approved, logged process. |
| Instrumentation added after the first incident | It is part of the service template and the readiness review. |

## Templates

- [Production readiness review](../../templates/docs/production-readiness-review.md)
- [Runbook](../../templates/docs/runbook.md)
- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml), which links dashboards and runbooks

## Sources

- OpenTelemetry documentation: https://opentelemetry.io/docs/
- OpenTelemetry semantic conventions: https://opentelemetry.io/docs/specs/semconv/
- W3C Trace Context: https://www.w3.org/TR/trace-context/
- Google SRE book, "Monitoring Distributed Systems": https://sre.google/sre-book/monitoring-distributed-systems/
- Google SRE Workbook, "Alerting on SLOs": https://sre.google/workbook/alerting-on-slos/
- Prometheus instrumentation practices: https://prometheus.io/docs/practices/instrumentation/
- Brendan Gregg, The USE Method: https://www.brendangregg.com/usemethod.html
