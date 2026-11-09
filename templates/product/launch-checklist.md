# Launch checklist: [feature or product]

<!--
How to use: required for launch tier 1, a shorter version (sections 1, 2, 4 and 6) for launch tier 2.
Launch tier 3 needs only a release note. Start it when the work enters Now on the roadmap.
Hold the readiness review about one week before external rollout. The launch owner records go or no-go.
Guidance: playbook/product/launch-and-adoption.md. Service-side readiness: templates/docs/production-readiness-review.md
-->

| Field | Value |
|---|---|
| Launch owner | [name] |
| Launch tier | [1 / 2] |
| Product one-pager | [link] |
| Feature flag | [name] |
| Readiness review date | [YYYY-MM-DD] |
| Decision | [go / no-go / go with conditions: list] |

## 1. Success and stop criteria (written before rollout)

| Measure | Target | Check date |
|---|---|---|
| Adoption (activation) | [for example 30% of eligible active users complete the key action once] | [date] |
| Repeat use | [for example 50% of those use it again in week 4] | [date] |
| Outcome | [change in the primary outcome metric] | [date] |
| Guardrails | [error rate, latency, support contacts per 1,000 users, complaints] | throughout rollout |
| Stop criterion | [for example below 20% adoption after 4 weeks: simplify or remove] | [date] |

## 2. Rollout plan

| Stage | Audience | Earliest date | Guardrails to read before the next stage | Owner |
|---|---|---|---|---|
| 1 | internal users | [...] | [...] | [...] |
| 2 | 1% (or a named pilot group) | [...] | [...] | [...] |
| 3 | 10% | [...] | [...] | [...] |
| 4 | 50% | [...] | [...] | [...] |
| 5 | 100% | [...] | [...] | [...] |

- [ ] Kill switch tested: turns the feature off in under 5 minutes without a deploy
- [ ] Service-side production readiness review complete, if the change adds or changes a service: [link]

## 3. People and process readiness

- [ ] Support briefed: what changed, who it affects, known limits, how to turn it off for a user
- [ ] Help content and in-product text written and reviewed in every supported language
- [ ] Sales or account managers briefed; no commitments beyond what ships
- [ ] Business customers: administrators told before their users see the change, with the notice period in the contract met: [date sent]
- [ ] Customer commitments this launch fulfils listed, and each account owner told: [accounts]
- [ ] Training and a support rota for the first weeks (internal staff systems)
- [ ] Teams that depend on this change told, with dates

- [ ] Pricing or plan changes: billing, invoices, tax handling and plan limits tested end to end; existing-customer policy applied: [link]

## 4. Communication

- [ ] Release note in the user's terms: [link]
- [ ] Announcement plan (in product, email, customer administrators, status page): [...]
- [ ] Announcement sent only after guardrails hold at [50%] or more

## 5. Legal, compliance and accessibility (launch tier 1, and any launch that touches these)

- [ ] Data protection: impact assessment updated or not needed: [link or reason]
- [ ] Regulated communications (pricing, offers, terms) reviewed by compliance: [name, date]
- [ ] Accessibility: WCAG 2.2 level AA checked, including with assistive technology: [link]
- [ ] Legal duties (consent, retention, rights) not staged to a subset unless the law allows: [confirmed by]
- [ ] Public services: assisted channel stays open and staff know about the change
- [ ] Service assessment passed where a service standard applies: [date]

## 6. After launch

| Check | Date | Result | Decision (keep, change, remove) |
|---|---|---|---|
| Adoption and guardrails at 2 weeks | [...] | [...] | [...] |
| Outcome review at 6 weeks | [...] | [...] | [...] |
| Flag removed after 100% (within 30 days) | [...] | [...] | [...] |
