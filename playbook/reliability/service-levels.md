# Service levels

Give every production service two or three service level objectives (SLOs) that describe what its users experience, and page people only when those objectives are at risk. Without SLOs, teams argue about reliability from anecdotes, alert on every CPU spike, and cannot say when it is safe to ship faster. An SLO with an agreed error budget turns "is it reliable enough?" into a number that product and engineering read the same way.

## Outcomes

Starting points. Tune them to your services and risk appetite.

- Every Tier 1 and Tier 2 service (tiers defined in [production readiness](production-readiness.md)) has 2 or 3 SLOs, each with a named owner.
- At least 80% of pages come from SLO burn-rate alerts, not from cause-based alerts such as CPU or disk.
- On-call engineers handle no more than 2 incidents per 12-hour shift on average, the limit in the Google SRE book (see [on-call](on-call.md)).
- SLOs and the error budget policy are reviewed every quarter, and the review is recorded.
- When a service exhausts its error budget, the error budget policy is applied within 1 working day.

## Terms

| Term | Meaning | Example |
|---|---|---|
| SLI (indicator) | A ratio of good events to valid events, measured as close to the user as you can | Share of checkout requests that return a non-5xx response in under 800 ms |
| SLO (objective) | A target for the SLI over a time window | 99.9% of checkout requests are good over a rolling 28 days |
| Error budget | The share of events allowed to fail: 1 minus the SLO | 0.1% of requests, about 40 minutes of full outage in 28 days |
| Burn rate | How fast the budget is being spent, relative to spending exactly all of it by the end of the window | Burn rate 1 spends the whole budget in 28 days; burn rate 14.4 spends 2% of a 30-day budget in 1 hour |
| SLA (agreement) | A contract with customers that carries penalties | 99.5% monthly availability with service credits |

Set the SLO tighter than the SLA so the team acts before a contract is breached. Never set an SLO of 100%: it leaves no budget for change, and no dependency you rely on achieves it.

Error budget for common targets over a 28-day window (full outage equivalent):

| SLO | Budget | Downtime equivalent |
|---|---|---|
| 99% | 1% | about 6 h 43 min |
| 99.5% | 0.5% | about 3 h 22 min |
| 99.9% | 0.1% | about 40 min |
| 99.95% | 0.05% | about 20 min |
| 99.99% | 0.01% | about 4 min |

## Practice

### Foundation

1. Pick the one user journey that matters most (sign in, checkout, submit a form, run a payment).
2. Write two SLIs for it: **availability** (share of requests that succeed) and **latency** (share of requests faster than a threshold). Measure them at the load balancer, API gateway or ingress, not inside the application.
3. Set targets from the last 4 weeks of data. Start slightly below what you already achieve, then tighten.
4. Add one external uptime probe that runs from outside your network every 1 to 5 minutes.
5. Review the numbers once a month in a 15-minute meeting with whoever decides priorities.

### Standard

1. **Two or three SLOs per service, no more.** Typical set: availability, latency, and one of freshness (data pipelines), correctness (financial or search results) or throughput (batch jobs). More SLOs dilute attention.
2. **Rolling 28-day windows** for alerting and operations. Calendar months are fine for reporting to customers.
3. **Multi-window, multi-burn-rate alerts.** Use the parameters from the SRE Workbook chapter "Alerting on SLOs". Each alert fires only when both the long and the short window exceed the burn rate, so it pages fast on real problems and resets quickly once fixed.

   | Budget spent (of a 30-day budget) | Long window | Short window | Burn rate | Action |
   |---|---|---|---|---|
   | 2% | 1 hour | 5 minutes | 14.4 | Page |
   | 5% | 6 hours | 30 minutes | 6 | Page |
   | 10% | 3 days | 6 hours | 1 | Ticket |

   Example Prometheus rule for a 99.9% availability SLO (fast-burn page):

   ```yaml
   - alert: CheckoutErrorBudgetFastBurn
     expr: |
       (
         sum(rate(http_requests_total{service="checkout",code=~"5.."}[1h]))
         / sum(rate(http_requests_total{service="checkout"}[1h]))
       ) > (14.4 * 0.001)
       and
       (
         sum(rate(http_requests_total{service="checkout",code=~"5.."}[5m]))
         / sum(rate(http_requests_total{service="checkout"}[5m]))
       ) > (14.4 * 0.001)
     labels:
       severity: page
     annotations:
       runbook_url: https://runbooks.example.internal/checkout#error-budget-burn
   ```

   Generate these rules from an SLO definition rather than writing them by hand. Open-source generators such as Sloth and Pyrra produce Prometheus rules; OpenSLO is a vendor-neutral format for the definitions.
4. **Error budget policy, agreed in writing** by the engineering lead and the product owner before it is needed. Starting point:
   - Budget remaining: ship as normal.
   - Budget exhausted over the last 28 days: pause feature releases for that service. Only fixes, security patches and reliability work ship until the SLO is met again.
   - A single incident spends more than 20% of the budget: it gets a [postmortem](postmortems.md) with at least one action item that has a priority equal to the top feature work.
   - Disagreements go to the named escalation owner (for example the CTO), who decides within 2 working days.
5. **SLOs for internal platforms.** Platform teams publish SLOs to the teams that depend on them. Examples to start from:

   | Platform | SLI | Starting target |
   |---|---|---|
   | CI | Pipelines that start within 5 minutes of a push | 95% |
   | CI | Pipeline runs that do not fail for infrastructure reasons | 99% |
   | Artifact registry | Successful pulls | 99.9% |
   | Deployment pipeline | Deployments that complete without platform error | 99% |
   | Identity provider | Successful sign-in requests | 99.95% |

   An internal SLO tells product teams what to design around. A service cannot promise users more than its critical dependencies deliver, unless it adds redundancy or graceful degradation.
6. **Quarterly review.** Check whether the SLO matches user complaints. If users were unhappy while the SLO was green, the SLI measures the wrong thing. If the SLO was red and nobody noticed, the target is too tight.

### Assured

Everything in Standard, plus:

1. Map each contractual or regulatory service commitment to an SLO with a documented margin (for example SLA 99.5%, SLO 99.9%).
2. Keep monthly SLO reports and every error budget policy decision for at least 12 months (starting point; follow your record-retention rules). Auditors use them as evidence for ISO/IEC 27001:2022 controls 8.16 (monitoring activities) and 5.30 (ICT readiness for business continuity), and for SOC 2 CC7.
3. Store SLO definitions in version control. Changes to targets go through review like any other change (see [change management](change-management.md)).
4. Separate who sets the target from who reports against it: the service owner proposes, a reliability or risk function approves.
5. For EU financial entities, link SLOs for critical functions to the ICT risk framework required by the EU Digital Operational Resilience Act (Regulation (EU) 2022/2554). This regulation is unrelated to the DORA software delivery metrics research.

## Cloud, on-premises and air-gapped

- The whole SLO stack runs on-premises: Prometheus, Alertmanager, Grafana and Loki, with rules generated by Sloth or Pyrra. No hosted service is needed.
- In air-gapped networks, run synthetic probes (for example Prometheus blackbox_exporter) from a separate host inside the network, so a single host failure does not hide an outage.
- When users reach the service over links you do not control (branch offices, mobile networks), measure at the edge you own and record the limitation next to the SLO.
- Pages must reach people who are outside the isolated network. See [on-call](on-call.md) for paging options.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Ten SLOs per service, none acted on | Cut to 2 or 3 tied to user journeys. Move the rest to dashboards. |
| SLO measured from server CPU or host uptime | Measure requests at the edge. Users feel failed requests, not CPU. |
| Target copied from a vendor's marketing page | Set it from your own last 4 weeks of data and what users tolerate. |
| Error budget policy written by engineering alone | Product owner co-signs it, or nobody will honour it when the budget runs out. |
| Paging on every threshold breach | Page on burn rate. Send cause-based alerts to dashboards or tickets. |
| SLO never changes | Review quarterly against complaints and incidents. |

## Templates

- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml): record SLOs, owners and tier.
- [Production readiness review](../../templates/docs/production-readiness-review.md): SLOs are a launch requirement for Tier 1 and Tier 2.
- [Runbook](../../templates/docs/runbook.md): one section per SLO alert.

## Sources

- Google, *Site Reliability Engineering*, chapter "Service Level Objectives": https://sre.google/sre-book/service-level-objectives/
- Google, *The Site Reliability Workbook*, "Implementing SLOs": https://sre.google/workbook/implementing-slos/
- Google, *The Site Reliability Workbook*, "Alerting on SLOs": https://sre.google/workbook/alerting-on-slos/
- Google, *The Site Reliability Workbook*, "Example Error Budget Policy": https://sre.google/workbook/error-budget-policy/
- OpenSLO specification: https://openslo.com/
- Sloth: https://github.com/slok/sloth and Pyrra: https://github.com/pyrra-dev/pyrra
