# Launch and adoption

The problem: a feature is merged, announced and counted as done. Support is surprised, users never find it, and nobody checks whether it is used. Treat launch as a product decision separate from deployment. Size it to its risk, roll it out in stages against success and stop criteria written in advance, get support and documentation ready, and measure adoption until the feature proves its value or is removed. A feature is done when users get value from it, not when the code reaches production.

## Outcomes

Starting targets. Tune them after a quarter.

| Signal | Starting target |
|---|---|
| Launches with success and stop criteria written before rollout starts | 100% of launches in launch tiers 1 and 2 |
| New behaviour released behind a flag with staged rollout | 100% of user-facing changes at Standard and above |
| Support and documentation ready before the first external user sees the change | 100% of launches in launch tiers 1 and 2 |
| Launches reviewed against their adoption and outcome metric | 100% within 6 weeks of full rollout |
| Features retired after failing their adoption criteria | More than zero per year |
| Deprecations announced with notice and a migration path | 100%, with the notice period stated in the [versioning policy](../delivery/versioning-and-changelogs.md) |

## Launch tiers

Not every change needs a launch plan. Size the effort to the change. Launch tiers are not the service tiers (Tier 1, Tier 2, Tier 3) in [production readiness](../reliability/production-readiness.md): a small change to a Tier 1 service can be a launch tier 3.

| Launch tier | Typical change | What it needs |
|---|---|---|
| Launch tier 1 | a new product, a new paid plan, a change to a core flow most users touch, anything with legal, pricing or data protection impact | full [launch checklist](../../templates/product/launch-checklist.md), staged rollout over at least 2 weeks, named launch owner, sign-off from support, legal or compliance as relevant, announcement plan |
| Launch tier 2 | a visible new feature or a change to an existing flow | short checklist, staged rollout, help content and support briefing, release note |
| Launch tier 3 | small improvements and fixes | release note or changelog entry; no plan |

Decide the tier when the work enters Now on the roadmap, not the week before release.

## Practice

### Foundation

- **Deploy is not release.** Merge behind a [feature flag](../delivery/feature-flags.md), turn it on for your own team first, then for a few friendly users, then for everyone.
- **Write the success and stop criteria first.** One adoption measure, one outcome measure, one guardrail, and the date you will check. "If fewer than 20% of active shops use it after 4 weeks, we simplify or remove it" is a stop criterion.
- **Tell the people who will be asked about it.** Whoever answers support needs a short note: what changed, who it affects, known limits, how to turn it off for a user.
- **Write the release note** in the user's terms: what they can now do, not what you built. See [versioning and changelogs](../delivery/versioning-and-changelogs.md).
- **Check after 2 to 6 weeks** and write one line: worked, did not work, unclear. The same rule is in [product partnership](../ways-of-working/product-partnership.md).

### Standard

- **Staged rollout with health checks:** internal users, then 1%, 10%, 50% and 100%, with stable bucketing and a pause at each step to read guardrails, as [feature flags](../delivery/feature-flags.md#standard) describes.
- **Launch readiness review for launch tier 1.** A 30-minute meeting a week before external rollout, using the [launch checklist](../../templates/product/launch-checklist.md): product, engineering, design, support, documentation, sales or account management, and legal or compliance where relevant. The launch owner records go or no-go. Reuse the [production readiness review](../reliability/production-readiness.md) for the service side rather than duplicating it.
- **Measure adoption in four steps:**

| Step | Question | Example measure |
|---|---|---|
| Reach | Did eligible users see it? | share of eligible active users exposed |
| Activation | Did they try it and get to first value? | share who completed the key action once; time to first value |
| Repeat use | Did they come back to it? | share still using it in week 4 after first use |
| Outcome | Did the product outcome move? | change in the primary outcome metric, against a holdout or baseline |

- **Look at cohorts, not totals.** Plot use by the week users first saw the feature. A rising total can hide every cohort dropping off.
- **Guardrails during rollout:** error rate, latency, support contacts per 1,000 users and complaints. A guardrail breach pauses the rollout; the kill switch turns it off in under 5 minutes.
- **Retire what failed.** A feature that misses its stop criterion is simplified, given one more test with a new hypothesis, or removed: delete the flag, the code and the help content in one change.
- **Deprecate with notice.** Announce, give a migration path and a date, measure who still uses the old behaviour, and contact them directly before switching off.
- **Business customers need warning.** In products sold to organisations, roll out by organisation, not by user, so colleagues see the same screens. Tell customer administrators about visible changes before their users see them: a starting point is 2 weeks for visible changes to existing flows, or the notice in the contract if longer. Removals follow the deprecation notice periods in the [versioning policy](../delivery/versioning-and-changelogs.md). Offer an opt-in preview, and let administrators delay a change to a core flow for one release where you can support it.
- **Pricing and packaging launches are launch tier 1.** Billing, invoices, tax handling and the customer notice are tested before the change; see [pricing and packaging](pricing-and-packaging.md).

### Assured

- **Customer communications approved where rules require.** In financial services, insurance, health and telecoms, launch messages, in-product text and pricing may count as regulated communications. Build compliance review into the launch tier 1 checklist with a lead time, not as a last-day gate. See [regulated industries](../compliance/regulated-industries.md).
- **Do not release legal duties to a subset.** Consent screens, retention changes, accessibility fixes and changes to rights are not staged by flag unless the law allows the old and new behaviour to co-exist, as [feature flags](../delivery/feature-flags.md#assured) sets out.
- **Public services keep the assisted channel.** People cannot choose another provider, so a digital launch does not remove the counter, phone or paper route until the digital service works for everyone who needs it. Measure digital take-up and completion rate for each group, and keep the assisted route funded. See [public sector](../compliance/public-sector.md).
- **Accessibility before launch, not after.** Every public launch in launch tiers 1 and 2 meets the Web Content Accessibility Guidelines (WCAG) 2.2 at level AA, tested with assistive technology, before the first public user sees it.
- **Service assessment.** Where a service standard applies, the move from private beta to public beta and from beta to live needs an assessment. Plan it into the launch date.
- **Internal launches are change management.** For staff systems (case management, finance, clinical), plan training, a support rota for the first weeks, a parallel run where errors carry legal or safety risk, and a fallback procedure. See [stakeholders and communication](../strategy/stakeholders-and-communication.md).

## When code is cheap to produce

- **Launch capacity becomes the limit.** Support, documentation, training and users' attention do not scale with code output. Cap the number of launches in tiers 1 and 2 a product area runs at once, the way a team caps work in progress. A starting point: one launch tier 1 and two launch tier 2 launches in rollout at a time.
- **More features dilute each other.** Every new option makes others harder to find. Count launches retired as well as launches shipped.
- **AI features launch on evals.** An AI feature does not reach general release until its eval threshold, cost budget and fallback are in place, as [building with AI](../ai/building-with-ai.md#from-pilot-to-production) sets out. Watch task success and escalation to a person as the adoption guardrails.

## Cloud, on-premises and air-gapped

Hosted products control rollout directly. For software customers install, a release is not adoption: customers upgrade on their own schedule, so measure adoption as the share of customers on the version, plus opt-in usage reports. Give customer administrators the flags and documented defaults to stage the rollout themselves. Air-gapped sites need release notes, training material and migration steps inside the transfer package, because they cannot reach your help site.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Merged" counted as "done" | Done means adopted against criteria written before rollout. |
| Big-bang launch on a fixed marketing date | Staged rollout; announce once guardrails hold at 50% or more. |
| Support learns about the feature from a customer | Support briefing in the checklist for launch tiers 1 and 2. |
| Totals reported, cohorts ignored | Plot adoption by first-exposure week. |
| Features that failed are kept "in case" | Stop criteria; remove the flag, code and help content together. |
| Paper or counter route closed on launch day | Keep the assisted channel until the digital route works for everyone. |
| Compliance review on the day before launch | Lead time for review in the checklist. |
| Enterprise users find a changed screen before their administrator heard about it | Administrator notice before release; roll out by organisation. |

## Templates

- [Launch checklist](../../templates/product/launch-checklist.md)
- [Product one-pager](../../templates/product/product-one-pager.md)
- [Release checklist](../../templates/docs/release-checklist.md)
- [Production readiness review](../../templates/docs/production-readiness-review.md)

## Sources

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020), on staged rollouts and guardrail metrics.
- Kerry Rodden, Hilary Hutchinson, Xin Fu, "Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications", Proceedings of CHI 2010, ACM (adoption and retention measures).
- GOV.UK Service Manual, agile delivery phases (beta and live): https://www.gov.uk/service-manual/agile-delivery
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/
