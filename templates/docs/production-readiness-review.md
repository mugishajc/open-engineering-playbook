# Production readiness review: <service name>

<!--
How to use: the owning team fills in every row and links evidence. A claim without evidence
counts as "No". The reviewer marks each gap as a Blocker (must close before launch) or a
Follow-up (owner and date, closes within 30 days). Tier 3 services answer only the rows marked T3.
Tiers and process: playbook/reliability/production-readiness.md
-->

| Field | Value |
|---|---|
| Service | |
| Tier | Tier 1 / Tier 2 / Tier 3 |
| Owning team | |
| Planned launch date | |
| Reviewer (outside the owning team for Tier 1) | |
| Review requested | YYYY-MM-DD |
| Decision | Approved / Approved with follow-ups / Not approved |
| Decision date | YYYY-MM-DD |

Answer: **Yes**, **No** or **N/A** (with reason). Required: T1 = Tier 1, T2 = Tier 2, T3 = Tier 3.

## 1. Ownership

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 1.1 | Owning team and service catalogue entry exist | T1 T2 T3 | | | |
| 1.2 | On-call rotation (or business-hours support) defined and staffed | T1 T2 T3 | | | |
| 1.3 | Escalation path and incident process known to the team | T1 T2 | | | |

## 2. Service levels and alerting

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 2.1 | 2 or 3 SLOs defined for the main user journey | T1 T2 | | | |
| 2.1a | One availability check (external probe or SLI) | T3 | | | |
| 2.2 | Multi-window burn-rate alerts route to the on-call rotation | T1 T2 | | | |
| 2.3 | Error budget policy agreed with the product owner | T1 T2 | | | |
| 2.4 | External synthetic check in place | T1 | | | |
| 2.5 | Paging path tested end to end; heartbeat alert to an external dead man's switch; alert when telemetry stops arriving | T1 T2 | | | |

## 3. Observability

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 3.1 | Metrics, structured logs and traces for the main journey | T1 T2 | | | |
| 3.2 | Dashboard shows SLOs, traffic, errors, latency and saturation | T1 T2 | | | |
| 3.3 | Logs exclude secrets and mask personal data | T1 T2 T3 | | | |

## 4. Capacity and performance

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 4.1 | Load tested at 2 times expected peak | T1 T2 | | | |
| 4.4 | Capacity carries peak with one zone or failure domain lost, without counting on autoscaling | T1 | | | |
| 4.2 | Known limits and bottlenecks written down | T1 T2 | | | |
| 4.3 | Scaling is automatic, or a scaling procedure exists (on-premises: hardware lead time known) | T1 T2 | | | |

## 5. Resilience

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 5.1 | Timeouts with deadline propagation; retries at one layer only, with backoff, jitter and a retry budget | T1 T2 | | | |
| 5.2 | Behaviour with each critical dependency down is known and tested | T1 | | | |
| 5.3 | No single point of failure, or the risk is accepted in writing | T1 | | | |
| 5.4 | Behaviour above capacity tested: load shedding by priority, graceful degradation, no retry storm | T1 | | | |
| 5.5 | Each dependency classed hard or soft; soft dependencies fail open with a degraded response; readiness does not check shared dependencies | T1 T2 | | | |
| 5.6 | Cloud quotas and provider rate limits listed, with headroom for peak and for failover | T1 T2 | | | |
| 5.7 | Certificates renewed automatically, with expiry alerts at 21 days; domains and tokens with expiry dates listed | T1 T2 T3 | | | |

## 6. Change and rollback

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 6.1 | Deployed only by the pipeline from version control | T1 T2 T3 | | | |
| 6.2 | Rollback tested and takes under 15 minutes, using the fast path under canary delivery (abort or rollback window, not only a Git revert) | T1 T2 | | | |
| 6.5 | Manifests leave `spec.replicas` out when an autoscaler owns it | T1 T2 | | | |
| 6.3 | Risky features behind flags with a kill switch | T1 T2 | | | |
| 6.4 | Schema changes are backward compatible (expand and contract) | T1 T2 | | | |

## 7. Data

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 7.1 | Data classified; retention period set | T1 T2 T3 | | | |
| 7.2 | Backups meet the tier's RPO; immutable copy exists | T1 T2 | | | |
| 7.3 | Restore from backup tested at production size; measured time within the restore RTO (date of test) | T1 T2 | | | |
| 7.4 | DPIA done where personal data processing is high risk | T1 T2 | | | |

## 8. Security

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 8.1 | Threat model for new data flows and integrations | T1 T2 | | | |
| 8.2 | Secrets in a secret manager; none in git; CI uses OIDC | T1 T2 T3 | | | |
| 8.3 | Dependencies and images scanned; no open P0 or P1 findings | T1 T2 T3 | | | |
| 8.4 | Access through SSO; production access just in time | T1 T2 | | | |
| 8.5 | Artifacts signed with SBOM; admission verifies signatures | T1 | | | |
| 8.6 | Penetration test done (Tier 1 before first release) | T1 | | | |
| 8.7 | AI features: threat model section 6 complete, evaluation threshold met, agent tools least privilege with human approval for irreversible actions, kill switch tested | T1 T2 | | | |

## 9. Operations

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 9.1 | Runbook with a section for every paging alert | T1 T2 | | | |
| 9.2 | On-call engineers trained on the service | T1 T2 | | | |
| 9.3 | Status page component exists | T1 | | | |

## 10. Compliance and cost

| # | Question | Req. | Answer | Evidence | Gap type |
|---|---|---|---|---|---|
| 10.1 | Legal and regulatory requirements listed (accessibility, residency, sector rules) | T1 T2 | | | |
| 10.2 | Supplier reviews done for new third parties | T1 T2 | | | |
| 10.3 | Monthly cost estimate and budget alert | T1 T2 T3 | | | |

## Gaps

| # | Gap | Blocker or Follow-up | Owner | Due | Status |
|---|---|---|---|---|---|
| | | | | | |

## Risk acceptance (only if launching with an open blocker)

| Risk | Accepted by (name, role) | Expiry (90 days max) | Risk register ID |
|---|---|---|---|
| | | | |

## Sign-off

| Role | Name | Date |
|---|---|---|
| Service owner | | |
| Reviewer | | |
