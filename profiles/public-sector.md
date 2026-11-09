# Public sector overlay

Apply this overlay on top of your size profile when you are a government body or build services for one. It raises the target to Assured: every practice must leave evidence, duties must be separated, and records must outlive the people who made them. It also adds five concerns a private company can often defer: procurement rules, accessibility, data residency, public records and open standards.

Leaders: read [for government](../leaders/for-government.md) first. It covers shared national platforms, low-bandwidth and offline use, local languages and funding across budget years.

## How overlays work

1. Pick your size profile first: [SME](sme.md), [solo](solo.md), [startup](startup.md), [scale-up](scale-up.md) or [enterprise](enterprise.md). Its week 1 to year 1 tables still apply.
2. Add the rows below at each horizon. Where both tables name the same page, do the overlay version.
3. Your target becomes Assured in every area. The assessment does this when your answers file says `overlays = ["public-sector"]`.
4. Scope Assured by service. A citizen-facing service that handles personal data needs all of it. An internal prototype may not. Record each exception, its reason and its owner in a [decision record](../playbook/architecture/decision-records.md), so an auditor can see it was a choice.

Levels never lower a legal duty. Data protection, accessibility, records and incident reporting laws apply from the day they apply to you, whatever level you are working towards (see the [legal floor](../playbook/data/data-security-and-privacy.md#legal-floor-applies-at-every-level)).

A school, small municipality or other public body that does not build software pairs it with the SME profile and applies it only to records, data protection, accessibility of its website and supplier contracts. A small digital unit inside a ministry usually pairs this overlay with the startup or scale-up profile. A large department or national agency pairs it with enterprise. A supplier to government applies it to the contracts in scope.

## Who this is for

- Ministries, agencies, regulators, local and regional government, state-owned enterprises, public health and education bodies.
- Suppliers and contractors who build or run software for them.

## What it adds by area

| Area | Assured adds |
|---|---|
| Strategy | Horizon scan covering procurement cycles, regulation and sovereignty; risk register reviewed every 90 days |
| Operating model | Separation of duties enforced in tooling; engineering reports fit the department's IT governance and spend controls |
| Product | Services move through discovery, alpha, beta and live with an assessment at each step; outcomes measured separately for assisted-channel users; no experiments on who receives an entitlement |
| Project management | Independent assurance at the major gates; gate decisions and re-baselines kept as records; tenders written with the flexibility the project will need |
| Ways of working | Every change traceable to an approved requirement |
| Delivery | Change evidence (request, reviewer, CI result, deployer) for any single change retrievable within 1 hour, and a sample of 25 changes within 1 working day, for 12 months or your records period |
| Quality | WCAG 2.2 level AA testing before every major release; test evidence kept |
| Reliability | Yearly disaster recovery test against written objectives |
| Security | SBOM and signed releases; cryptographic inventory and post-quantum plan |
| Data | Retention and deletion enforced by automation; data residency recorded per store |
| AI | AI risk managed under a documented framework; human oversight for decisions about people |
| Architecture | Decision records name the approver and follow the records policy |
| Platform | Builds work from internal mirrors where networks are restricted or air-gapped |
| People | Secure coding and data protection training recorded yearly |
| Measurement | Metrics and assessments retained and available to auditors |
| Compliance | Control evidence collected automatically; reporting deadlines tested |

## Week 1

| Add this | Read | Template |
|---|---|---|
| List your obligations: procurement rules, accessibility law, data protection law, records law, data residency, security classification | [Public sector](../playbook/compliance/public-sector.md), [Control mapping](../playbook/compliance/control-mapping.md) | |
| Classify every data store with the four classes the playbook uses. Government classified information stays in your national classification scheme, with its own vetting and accreditation rules, not in these classes | [Data governance](../playbook/data/data-governance.md) | [data-classification.md](../templates/docs/data-classification.md) |
| Record where each data store physically sits, and check it against residency rules. Record the transfer mechanism for every supplier or copy outside the country, including remote support access | [Data security and privacy](../playbook/data/data-security-and-privacy.md) | |
| List the shared national platforms you must or could use (identity, payments, data exchange) | [For government](../leaders/for-government.md) | |
| Keep a record of processing and run a DPIA before any high-risk processing of citizens' data | [Data security and privacy](../playbook/data/data-security-and-privacy.md) | |

## Month 1

| Add this | Read | Template |
|---|---|---|
| Code assistant policy that names approved tools and bans citizen data in tools that are not approved for it | [Code assistants](../playbook/people/code-assistants.md) | [code-assistant-policy.md](../templates/docs/code-assistant-policy.md) |
| AI use register; assess any AI that affects decisions about people before it goes live | [AI governance](../playbook/ai/ai-governance.md) | [ai-use-case-assessment.md](../templates/docs/ai-use-case-assessment.md) |
| Accessibility testing against WCAG 2.2 level AA in the release checklist | [Public sector](../playbook/compliance/public-sector.md) | [release-checklist.md](../templates/docs/release-checklist.md) |
| Retention periods for decision records, change evidence, incident records and logs, agreed with the records officer | [Documentation](../playbook/people/documentation.md), [Decision records](../playbook/architecture/decision-records.md) | [adr.md](../templates/docs/adr.md) |
| Supplier review that covers data location, exit terms and source code escrow or access | [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) | [vendor-risk-questionnaire.md](../templates/docs/vendor-risk-questionnaire.md) |

## Quarter 1

| Add this | Read | Template |
|---|---|---|
| Separation of duties in source control and deployment: the author cannot approve or deploy alone | [Decision rights](../playbook/operating-model/decision-rights.md), [Access control](../playbook/security/access-control.md) | [default-branch.json](../templates/github/rulesets/default-branch.json) |
| Change evidence linked automatically from pipeline to request | [Change management](../playbook/reliability/change-management.md), [Release management](../playbook/delivery/release-management.md) | |
| A control map from your national framework (and ISO/IEC 27001 if used) to the playbook practices | [Control mapping](../playbook/compliance/control-mapping.md) | |
| Fit engineering governance into the department's spend controls and assurance gates, so a gate reviews evidence instead of asking for new documents | [IT governance](../playbook/operating-model/it-governance.md) | |
| Open standards and open source by default: publish code unless there is a recorded reason not to | [Build, buy or adopt](../playbook/strategy/build-buy-adopt.md), [Public sector](../playbook/compliance/public-sector.md) | |
| Set a page weight budget and test key journeys on a slow mobile network and a low-cost phone | [For government](../leaders/for-government.md) | |
| Internal mirrors for packages and images on restricted networks | [Cloud, on-premises and air-gapped](../playbook/platform/cloud-on-prem-air-gapped.md) | |
| Cryptographic inventory, starting with data that must stay secret for 10 years or more | [Post-quantum readiness](../playbook/security/post-quantum-readiness.md) | [crypto-inventory.csv](../templates/docs/crypto-inventory.csv) |
| Write MoSCoW priorities, priced options, an exchange clause and a change budget into every new tender | [Planning fixed scope and budget](../playbook/project-management/planning-fixed-scope-and-budget.md#public-procurement-put-the-flexibility-in-the-tender) | |
| Gate each service at the end of discovery, alpha and beta, with criteria written before the phase and independent assurance at alpha and go/no-go | [Risks, RAID logs and stage gates](../playbook/project-management/risks-raid-and-stage-gates.md#a-gate-map-for-digital-projects) | [stage-gate-checklist.md](../templates/project/stage-gate-checklist.md) |

## Year 1

| Add this | Read | Template |
|---|---|---|
| Post-quantum migration plan with dates, aligned with national guidance where it exists | [Post-quantum readiness](../playbook/security/post-quantum-readiness.md) | [crypto-inventory.csv](../templates/docs/crypto-inventory.csv) |
| A documented AI risk framework, such as the NIST AI RMF or ISO/IEC 42001, for every AI feature that affects the public | [AI governance](../playbook/ai/ai-governance.md), [AI application security](../playbook/ai/ai-application-security.md) | |
| A disaster recovery test against written recovery objectives, with the results filed | [Backup and recovery](../playbook/reliability/backup-and-recovery.md) | |
| Signed releases with an SBOM for every citizen-facing service | [Supply chain](../playbook/security/supply-chain.md) | [sbom-and-sign.yml](../templates/security/workflows/sbom-and-sign.yml), [gitlab-supply-chain.yml](../templates/security/gitlab-supply-chain.yml) |
| An exit plan for every critical supplier, reviewed every year and tested with a real, timed data export and import (paper walk-throughs count only for less critical suppliers) | [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) | |
| Launch in the languages most users speak, and budget translation as a running cost | [For government](../leaders/for-government.md) | |
| Four committed assessments; every in-scope service at Assured or with recorded exceptions | [Maturity model](../playbook/measurement/maturity-model.md) | [assessment](../assessment/README.md) |

## Do not add

| Avoid | Why |
|---|---|
| A change board that approves every change | Pre-approved standard changes with automatic evidence give auditors more than meeting minutes. See [change management](../playbook/reliability/change-management.md). |
| Screenshots as evidence | They cannot be verified. Keep pipeline logs and signed records. |
| Freezing dependency updates for stability | Old dependencies are where known exploited vulnerabilities live. |
| Buying before checking what other government bodies already run | Shared platforms and published code often exist. Check first, then build, buy or adopt. |
| Assured on internal prototypes | Record the exception and move on. |

## Sources

- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
- UK Technology Code of Practice: https://www.gov.uk/guidance/the-technology-code-of-practice
- US Digital Services Playbook: https://playbook.cio.gov
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/
- Web Accessibility Directive, Directive (EU) 2016/2102, for public sector websites and mobile apps: https://eur-lex.europa.eu/eli/dir/2016/2102/oj
- European Accessibility Act, Directive (EU) 2019/882, for private-sector products and services, applies from 28 June 2025: https://eur-lex.europa.eu/eli/dir/2019/882/oj
