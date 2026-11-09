# FinOps

"The cloud bill doubled and nobody can say which product or team caused it." Make cost visible to the teams who create it, tag every resource to an owner, track cost per unit of business value (per order, per customer, per transaction), and review it on a fixed cadence. Use the FinOps Foundation's three phases, Inform, Optimize and Operate, and treat cost as an engineering metric next to latency and reliability. The same discipline applies on-premises, where the cost is hardware, power, space and people rather than a monthly invoice.

## Outcomes

Starting points. Tune them to your organisation.

- At least 95% of cloud spend is allocated to an owning team and a product through tags or account structure.
- Every team sees its own cost at least weekly, with a dashboard that is no more than 2 days behind.
- Cost per unit (for example per 1,000 transactions or per active customer) is tracked for each major product and reviewed monthly.
- Budget alerts exist for every account or project. Anomalies over 20% of expected daily spend are investigated within 2 working days.
- Idle and unattached resources are below 5% of monthly spend.

## The three phases

| Phase | What it means | Typical actions |
|---|---|---|
| Inform | Know what you spend, who spends it and on what | Tagging policy, account structure, cost dashboards per team, showback |
| Optimize | Spend less for the same outcome | Rightsizing, shutting down idle resources, storage tiers, commitment discounts, architecture changes |
| Operate | Keep it that way through process and ownership | Budgets, anomaly alerts, cost review in design and readiness reviews, monthly cost meetings |

Organisations move through the phases repeatedly, one product or service at a time.

## Techniques

### Allocation

- Tag every resource with at least `owner` (team), `product`, `environment` and `cost-centre`. Enforce tags with policy as code at creation (see [infrastructure as code](../delivery/infrastructure-as-code.md)). Untagged resources are flagged daily.
- Shared costs (platform, networking, support) are split by a published rule, for example proportional to compute use. Keep the rule simple and stable.
- Showback (teams see their cost) comes before chargeback (teams pay from their budget). Many organisations never need chargeback.

### Billing data

- Use the FOCUS specification (FinOps Open Cost and Usage Specification) as the common format where your providers support it, so cost data from several clouds and SaaS vendors can be combined.
- For Kubernetes, allocate cluster cost to namespaces and workloads with a tool such as OpenCost (a CNCF project).
- Allocate telemetry (log, trace and metric ingest) like compute, by owner tag. It is often a large line on the bill; see [observability](../architecture/observability.md#telemetry-cost) for ingest budgets.

### Optimisation, in order of effort

1. Delete what nobody uses: idle instances, unattached disks, old snapshots, forgotten test environments.
2. Schedule non-production environments to stop outside working hours.
3. Rightsize from measured use. Review requests and limits on Kubernetes (see [cloud native](cloud-native.md)).
4. Use storage lifecycle rules to move old data to cheaper tiers, within your retention rules.
5. Buy commitment discounts for the stable baseline only, after rightsizing.
6. Change the architecture where cost per unit stays high: caching, batching, a different data store. See [scaling](../architecture/scaling.md).

### Engineering decisions

- Every [RFC](../architecture/rfcs.md) includes run cost per month. Every [production readiness review](../reliability/production-readiness.md) checks tags, budgets and alerts.
- Engineers can see the cost of their own services without asking finance.

## Practice

### Foundation

- One budget alert per account or project. A monthly look at the bill by service.
- Tag `owner` and `environment` on everything. Delete unused resources monthly.

### Standard

- Tagging policy enforced at creation. Showback dashboards per team, updated daily.
- Unit cost metrics per product, reviewed monthly by engineering and product leads together.
- Anomaly detection with alerts to the owning team.
- A named FinOps lead (part-time in a scale-up) who works with finance and engineering.
- Commitment purchases reviewed quarterly against actual use.

### Assured

- Cost allocation rules, budgets and approvals are documented and auditable. Large commitments follow procurement rules.
- Public sector: spend controls and value-for-money reviews required by government apply to cloud consumption as well as to contracts.
- Cost and concentration risk on single providers is recorded in the risk register, with the exit plan (see [cloud, on-premises and air-gapped](cloud-on-prem-air-gapped.md)).

## Cloud, on-premises and air-gapped

- Public cloud: cost changes with every deployment. Tags, budgets and dashboards are the core tools.
- On-premises and air-gapped: cost is mostly fixed and paid up front. Track total cost of ownership per service: hardware amortised over its life, power and cooling, space, licences, support contracts and staff time. Show teams the capacity they use, so on-premises capacity is not treated as free.
- Hybrid: use the same allocation keys (owner, product, environment) in both, so leaders can compare.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Finance sees the bill, engineers never do | Daily showback per team. |
| One-off cost-cutting drive, then drift back | Operate phase: budgets, alerts, monthly review. |
| Buying commitments before rightsizing | Rightsize first, then commit only to the stable baseline. |
| Optimising total spend while the business grows | Track cost per unit, not only total cost. |
| On-premises capacity treated as free | Show total cost of ownership per service. |

## Templates

- [Business case](../../templates/strategy/business-case.md)
- [RFC template](../../templates/docs/rfc.md), with its cost section

## Sources

- FinOps Foundation, FinOps Framework: https://www.finops.org/framework/
- FOCUS, FinOps Open Cost and Usage Specification: https://focus.finops.org/
- OpenCost: https://www.opencost.io/
