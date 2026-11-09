# Tabletop: cloud region outage

Your cloud provider's region fails on a weekday morning, the provider gives no time for recovery, and the failover plan you wrote 18 months ago meets reality. This scenario tests the decision to fail over or wait, what a standby region needs that nobody listed, how to keep customers and a regulator informed, and how to come back without losing or duplicating money.

| | |
|---|---|
| Audience | Platform and SRE engineers, service owners, the incident commander rotation, product owners, customer support lead, CTO. A compliance officer for the T+60 inject. |
| Time | 90 minutes (10 brief, 60 play, 20 debrief) |
| Read first | [Cloud, on-premises and air-gapped](../../playbook/platform/cloud-on-prem-air-gapped.md), [backup and recovery](../../playbook/reliability/backup-and-recovery.md), [service levels](../../playbook/reliability/service-levels.md), [incident management](../../playbook/reliability/incident-management.md) |
| Facilitator notes | [Facilitator guide](facilitator-guide.md) |

## Setup

The organisation is a B2B invoicing and payments platform used by 8,000 small businesses. It is regulated as a payment institution, so the EU Digital Operational Resilience Act (Regulation (EU) 2022/2554) applies. About 60 engineers. Everything runs in one cloud region across three availability zones. A warm standby exists in a second region: a database replica with asynchronous replication, and Kubernetes clusters scaled to zero. A failover was rehearsed once, in staging, 18 months ago.

Customer contracts promise 99.9% monthly availability. The payments API SLO is 99.95% over 28 days, and 11 minutes of its budget is already spent this window. The status page is hosted by the same provider, in the same region. All organisations, people and numbers here are fictional.

## Injects

### T+0 (Tuesday 10:12): errors everywhere

The fast-burn SLO alert fires for the payments API: 68% of requests fail. Then the same alert fires for invoicing and sign-in. The Kubernetes API in the primary region times out. The provider's status page says: "We are investigating increased error rates for some services in the region."

**Decide:**
- Severity and incident commander. Who are the operations lead and the communications lead?
- Is this your change or the provider's? How do you tell in 10 minutes? (Check the deployment log: the last deployment was 22 hours ago.)
- What is the first external message, and where do you post it?

### T+15 (10:27): no time for recovery

The provider confirms the failure affects multiple availability zones and gives no estimate. Your own status page returns errors. Support has 140 open chats and rising.

**Decide:**
- Fail over now, or wait for the provider? What evidence would change your mind, and by what time do you decide?
- Who has the authority to trigger a regional failover? Is it written down?
- Where do you publish status now?

### T+30 (10:42): the standby is not ready

The team starts the failover. Problems arrive one at a time:
- The CI/CD pipeline and the container registry run only in the primary region. New images cannot be pulled in the standby region.
- The standby database replica was 4 minutes 20 seconds behind at the time of failure. Payments submitted in that window may be lost, or may have been sent to the bank but not recorded.
- The standby region's account quota allows 40% of the compute you need.

**Decide:**
- Which services come up first with 40% capacity? Which can stay down?
- How do you find and reconcile the payments from the lost 4 minutes 20 seconds? Do you block retries to avoid paying a supplier twice?
- Do you open a quota increase request, run degraded, or both?

### T+60 (11:12): customers and the regulator

The chief executive of your largest customer (12% of revenue) phones your CEO: 48 supplier payments due today are stuck, and late fees start at 17:00. Your compliance officer asks whether this is a major ICT-related incident under EU DORA, which has its own classification criteria and reporting deadlines. Finance asks how much the SLA credits will cost.

**Decide:**
- What do you tell the largest customer, and who says it? Do you offer a manual workaround for urgent payments?
- Who decides on the DORA classification, and with what information? When does that clock start?
- Is the SLA credit question for now or for later?

### T+90 (11:42): the region comes back

The provider reports partial recovery. Half your traffic now runs in the standby region and writes to the promoted replica. The old primary database is reachable again and accepting connections.

**Decide:**
- Fail back now, stay in the standby region, or freeze? What stops two databases accepting writes at the same time?
- What has to be true before you fail back? Who signs it off?

### Optional injects

- **T+20:** An engineer proposes changing the DNS records by hand in the provider console. The DNS zone is managed by infrastructure as code, and the pipeline is down.
- **T+35:** Engineers cannot sign in to the standby region's console: the identity provider's tenant runs in the failed region. The secrets manager in the standby region has no replica of the database credentials.
- **T+45:** The on-call engineer who knows the failover runbook has been working since 06:00 and asks to hand over.
- **T+75:** A journalist from a trade publication asks whether the outage affected "all your customers' money".

## Discussion questions

1. For your most critical service, what is the RPO and RTO, and when did you last prove them in the other region?
2. List everything the standby region needs on the day: images, secrets, DNS, certificates, quota, pipeline, identity, runbooks. Which of these live only in the primary region?
3. Who can trigger a regional failover, and how long does it take to reach them?
4. What is your rule for failing back? Is it written down?
5. Which customer commitments (SLA, regulator, contracts) start a clock during an outage like this?

## What good looks like

- SEV1 within 15 minutes, communications lead posting from a status page that does not share the failed region ([incident management](../../playbook/reliability/incident-management.md)).
- A pre-agreed decision rule for failover, for example "fail over if the provider gives no recovery estimate within 20 minutes and the expected outage is longer than the time to fail over plus the cost of the replication gap", written in the runbook. The error budget decides release pace between incidents; it does not decide how long customers stay down ([service levels](../../playbook/reliability/service-levels.md)).
- Failover uses only actions that do not need the failed region: credentials provisioned in advance, DNS changed through a provider outside the region, break-glass accounts tested every quarter. This is called static stability.
- The standby holds its own copy of images, secrets and pipeline, tested on a schedule, not only once ([cloud, on-premises and air-gapped](../../playbook/platform/cloud-on-prem-air-gapped.md)).
- Reconciliation of in-flight payments using idempotency keys before retries are allowed ([rollbacks: when rollback is impossible](../../playbook/reliability/rollbacks.md#when-rollback-is-impossible)).
- Regulatory classification started early by the compliance lead, with facts from the incident commander ([incident management: Assured](../../playbook/reliability/incident-management.md#assured)).
- Failback treated as a planned change with a single writer at all times, not as a reflex.
- The provider's report attached to your postmortem, and your own design choices (single region, single registry) still listed as contributing factors ([postmortems](../../playbook/reliability/postmortems.md)).

## Scoring rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Declaration and roles | No commander by T+15 | Commander named, roles mixed | SEV1, commander, operations and communications leads by T+15 |
| Failover decision | Debated past T+45 without a decision | Decided, but no rule or owner | Decided by T+30 against a written rule, by the named owner |
| Standby readiness | Gaps discovered one by one with no plan | Gaps listed, partly worked around | Priority order for 40% capacity agreed; workarounds owned |
| Data integrity | Lost window ignored | Noticed, no reconciliation plan | Retries blocked, reconciliation owned, customers told |
| Customer and regulator communication | Silent or contradictory | Updates late or ad hoc | Status page outside the region, cadence kept, compliance engaged early |
| Failback | Failed back on first sign of recovery | Paused, but no criteria | Written failback criteria, single writer enforced, sign-off named |

Maximum 12.

## Follow-up actions

- Write the failover decision rule and the named owner into the runbook ([runbook template](../../templates/docs/runbook.md)).
- Replicate container images, secrets and pipeline capability to the standby region, and test a full failover in production hours at least once a year ([backup and recovery](../../playbook/reliability/backup-and-recovery.md)).
- Move the status page to a separate provider.
- Request and verify standby quota for 100% of Tier 1 capacity.
- List every control-plane dependency of the failover (identity, secrets, DNS, registry, pipeline) and remove the ones that live only in the primary region. See AWS Builders' Library, "Static stability using Availability Zones": https://aws.amazon.com/builders-library/static-stability-using-availability-zones/
- Add idempotency keys to every payment-initiating API, and a reconciliation job for replication gaps.
- Record the hosting decision and its exit and failover conditions in an [ADR](../../templates/docs/adr.md).
