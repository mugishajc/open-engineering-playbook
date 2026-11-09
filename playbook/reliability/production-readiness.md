# Production readiness

Before a service takes real traffic, check it against a short, tiered list: who owns it, how you will know it is broken, how you will roll it back, and how you will restore its data. Most launch-day incidents come from gaps that a one-hour review would have found. Scale the review to the service's tier so internal tools are not held to the bar of a payment system.

## Outcomes

Starting points. Tune them to your portfolio.

- Every service in production has a tier, an owning team and an entry in the service catalogue.
- 100% of new Tier 1 and Tier 2 services pass a production readiness review (PRR) before taking production traffic.
- A Tier 1 PRR takes no more than 5 working days from request to decision.
- Follow-up items from a PRR close within 30 days in at least 80% of cases.
- Tier 1 services are re-reviewed every 12 months or after a major change.

## Service tiers

Other reliability and security pages use these tiers. Pick the tier from the impact of an outage, not from how hard the service was to build.

| Tier | Meaning | Examples | Typical SLO | Review |
|---|---|---|---|---|
| Tier 1 | Outage stops revenue, harms users, breaks a legal duty, or affects safety | Payments, login, citizen-facing applications, core APIs | 99.9% or higher | Full PRR with an independent reviewer |
| Tier 2 | Outage degrades an important feature or an internal system many people depend on | Search, notifications, CI, internal identity tools | 99.5% to 99.9% | Full PRR, peer reviewer |
| Tier 3 | Outage is an inconvenience with a workaround | Internal dashboards, reporting jobs, prototypes | Best effort or 99% | Self-assessed short list |

## When to run a review

- Before a new service or a new public endpoint takes production traffic.
- Before a big change: a new region or site, a new data store, expected traffic above 3 times the current peak, or a new class of data (personal, payment, health, classified).
- When a service moves up a tier.
- Every 12 months for Tier 1.

## Practice

### Foundation

Self-assess against ten questions. Answer each in one or two lines in the service's README. A "no" is fine if it is written down and accepted by the owner.

1. Who owns the service, and how do you reach them at 3am (or is it business hours only)?
2. Which user journey matters most, and what SLO protects it?
3. How will you know it is broken before users tell you?
4. How do you deploy, and how do you roll back in under 15 minutes? (See [rollbacks](rollbacks.md).)
5. Where does data live, how is it backed up, and when was a restore last tested?
6. Which secrets does it use, and where are they stored? (Not in git. See [secrets](../security/secrets.md).)
7. Who can access production, and how is that access granted?
8. What happens when its most important dependency is down?
9. Are dependencies scanned for known vulnerabilities in CI?
10. Is there a runbook for each alert?

### Standard

Use the full [production readiness review template](../../templates/docs/production-readiness-review.md). It covers ten areas:

| Area | Must have before launch (Tier 1 and 2) |
|---|---|
| Ownership | Owning team, on-call rotation, escalation path, service catalogue entry |
| Service levels | 2 or 3 SLOs, burn-rate alerts, error budget policy (see [service levels](service-levels.md)) |
| Observability | Metrics, structured logs and traces for the main journey; dashboards (see [observability](../architecture/observability.md)) |
| Capacity | Load test at 2 times expected peak; known limits written down; autoscaling or a scaling procedure |
| Resilience | Timeouts, retries with backoff and limits on every network call; behaviour with each critical dependency down |
| Change | Automated deployment with a tested rollback under 15 minutes (see [rollbacks](rollbacks.md)); feature flags for risky features (see [release management](../delivery/release-management.md)) |
| Data | Backups meeting the tier's RPO and RTO, with a tested restore (see [backup and recovery](backup-and-recovery.md)) |
| Security | Threat model for new data flows; secrets in a secret manager; dependencies and images scanned; access through SSO and least privilege |
| Operations | Runbook for every paging alert; on-call trained; incident process known |
| Compliance and cost | Data classification and retention; privacy assessment where personal data is processed; cost estimate and budget alert |

How to run it:

1. The owning team fills in the template and links evidence (dashboards, test results, runbooks). Claims without evidence count as "no".
2. A reviewer from another team, or a reliability engineer, spends up to 2 hours reading and asks questions in writing.
3. Each gap is either a **blocker** (must close before launch) or a **follow-up** (has an owner and closes within 30 days).
4. The reviewer approves, approves with follow-ups, or rejects. The decision and date go in the service catalogue.

The review is there to help the team launch safely, not to stop launches. Reviewers suggest fixes and pair on the hard ones.

### Assured

Everything in Standard, plus:

1. **Independent sign-off** for Tier 1: the reviewer is outside the owning team's reporting line.
2. **Risk acceptance in writing.** A launch with an open blocker needs a named risk owner at the right level, an expiry date (90 days at most, as a starting point) and an entry in the risk register.
3. **Evidence kept** with the review: links resolve to stored copies, not live dashboards that change. This supports ISO/IEC 27001:2022 controls 8.25 to 8.29 (secure development), 8.32 (change management) and 5.30 (ICT readiness for business continuity).
4. **Regulatory checks.** Data protection impact assessment where required by GDPR Art. 35 or similar laws; accessibility conformance for public services (see [public sector](../compliance/public-sector.md)); outsourcing and third-party rules for regulated firms (see [third-party and SaaS risk](../security/third-party-and-saas-risk.md)).
5. **Annual re-review** of every Tier 1 service, recorded.

## Cloud, on-premises and air-gapped

- **Capacity is fixed on-premises.** Without elastic capacity, the PRR must show current headroom, procurement lead time for more hardware and a plan for the peak.
- **Air-gapped dependencies.** List every external dependency the service expects at runtime (licence servers, time sources, certificate revocation lists, package mirrors, model downloads) and show that each is mirrored or removed.
- **Managed cloud services** move some items to the provider. Record which ones, and check the provider's own SLA against your SLO.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A 200-item checklist applied to every service | Tier it. Tier 3 gets 10 questions. |
| Review happens the day before launch | Book it when the design is agreed; final check 1 week before launch. |
| "Yes, we have backups" with no restore ever tested | Ask for the date and result of the last restore test. |
| Review team becomes a gate that says no | Reviewers help fix gaps. Measure time-to-decision. |
| PRR passed once, never revisited | Re-review Tier 1 yearly and after big changes. |

## Templates

- [Production readiness review](../../templates/docs/production-readiness-review.md)
- [Runbook](../../templates/docs/runbook.md)
- [Threat model](../../templates/docs/threat-model.md)
- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml)
- [Release checklist](../../templates/docs/release-checklist.md)

## Sources

- Google, *Site Reliability Engineering*, "The Evolving SRE Engagement Model" (production readiness reviews): https://sre.google/sre-book/evolving-sre-engagement-model/
- Google, *Site Reliability Engineering*, Appendix "Launch Coordination Checklist": https://sre.google/sre-book/launch-checklist/
- Regulation (EU) 2016/679 (GDPR), Article 35: https://eur-lex.europa.eu/eli/reg/2016/679/oj
