# Technical due diligence

Before you buy a company, invest in one, outsource a service or sign a multi-year contract with a major vendor, find out what the technology will cost you after the signature. Run a time-boxed review of eleven areas over 2 to 4 weeks, separate red flags (which change the price, the structure or the decision) from yellow flags (which add cost to the plan), and report every finding with a severity and a remediation cost range. The output is a short report the deal team can act on, not a description of the target's architecture.

## When to use this

| Context | Main question | Depth | Typical length |
|---|---|---|---|
| Acquisition | What will it cost to own, integrate and secure this, and who must we keep? | all eleven areas, hands-on, plus a compromise assessment | 3 to 4 weeks |
| Investment (minority or growth) | Can this technology and team scale to the plan in the investment case? | all eleven areas, lighter on integration | 2 to 3 weeks |
| Outsourcing a service or development | Can this supplier run our service safely, and can we leave? | delivery, security, data, people, compliance, exit | 2 to 3 weeks |
| Major vendor or platform selection | Will this product still meet our needs in 5 years, and what is the exit cost? | architecture, security, data, licences, cost, roadmap | 2 weeks, after [build, buy or adopt](../playbook/strategy/build-buy-adopt.md) scoring |

Use the [third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) process for routine supplier onboarding. This page is for decisions large enough to need a dedicated team.

## Scope it first

Agree these in writing with the sponsor before any work starts:

1. **The thesis.** What must be true for the deal to make sense? For example, "the platform can serve three more countries without a rewrite" or "the supplier can run our service on-premises".
2. **The questions.** Turn the thesis into 5 to 10 questions the review must answer.
3. **Access.** Data room, read-only repository access, interviews, and whether you may run the build. Code access often needs a clean team or an independent reviewer; take legal advice on competition and confidentiality rules.
4. **Team.** A lead, plus specialists in security, infrastructure and licences as needed. Two to four people is typical.
5. **Output and deadline.** Report format, severity scale and the date the deal team needs it.

## The eleven areas

| Area | What to examine | Ask for | Example red flag |
|---|---|---|---|
| 1. Architecture | structure, coupling, single points of failure, fit with your plans | C4 context and container diagrams, decision records, scaling history | the thesis needs a rewrite of the core system |
| 2. Code health | test coverage on critical paths, age of dependencies, build reproducibility, hotspots | read-only access, CI history, dependency report | the product cannot be built from source by anyone outside one person |
| 3. Delivery | how often and how safely they release | deployment frequency, change lead time, change fail rate, failed deployment recovery time ([metrics](../playbook/measurement/metrics.md)) | releases only a few times a year, each with a long outage |
| 4. Security | vulnerability handling, access control, incidents, and whether an attacker is already inside | penetration test reports, vulnerability backlog, incident log, [secure development](../playbook/security/secure-development.md) evidence; for acquisitions, a compromise assessment by an independent team (a threat hunt on identity, endpoint and cloud logs) before signing or as a condition of closing, and a search of the target's repositories for leaked credentials and secrets | an undisclosed breach; signs of a current or past undetected intrusion; critical vulnerabilities known to be exploited left open for months |
| 5. Data and privacy | what personal data is held, on what legal basis, where | data inventory, records of processing, impact assessments, data processing agreements | personal data used without a lawful basis, or transferred where the law does not allow |
| 6. Licences and open source obligations | copyleft obligations, licence compatibility, third-party commercial licences | SBOM (CycloneDX or SPDX), licence scan, list of commercial licences and whether they transfer | copyleft code in a distributed product with no compliance process; a key licence that ends on change of control |
| 7. Infrastructure and cost | hosting, run cost trend, unit cost, resilience, backups | cloud and data centre bills for 12 months, architecture of environments, last restore test | run cost grows faster than revenue with no plan; backups never restored |
| 8. People and key-person risk | who knows what, retention risk, skills | org chart, tenure, a skills matrix, contractor share | one person is the only one who can deploy or fix the core system |
| 9. Compliance | certifications, regulatory duties, audit findings | ISO/IEC 27001 or SOC 2 reports, regulator letters, open audit findings | a lapsed licence or certification the business depends on |
| 10. Roadmap | whether the plan is credible and funded | product and technical roadmap, capacity split, debt register | the roadmap needs more people than exist, with no hiring plan |
| 11. AI and models | model and data provenance, rights to training data, dependence on external model providers, inference cost, EU AI Act exposure | AI use-case register and risk tiers ([AI governance](../playbook/ai/ai-governance.md)), licences for models and training data, provider contracts and exit options, inference cost as a share of revenue | the product depends on training data the target has no right to use, or on one model provider with no exit and a cost that grows faster than revenue |

## Red flags and yellow flags

| Type | Meaning | What happens next |
|---|---|---|
| Red flag | Could change the price, the deal structure or the decision itself | Report to the deal lead within 24 hours. Do not wait for the final report. |
| Yellow flag | Real cost or risk that can be fixed after signing | Price it and put it in the integration or onboarding plan. |
| Observation | Worth knowing; no material cost | List it in an appendix. |

Common red flags: unclear ownership of the code or key intellectual property; an undisclosed security incident; signs of a current or past undetected intrusion; personal data processed without a lawful basis; a single person holding all production access; licence terms that end on change of control; a product that cannot run where you need it (for example in-country or on-premises).

Common yellow flags: old but supported dependencies; missing automated tests outside critical paths; manual releases; no SBOM; thin documentation; high but explained cloud cost.

## How to run it in 2 to 4 weeks

| Week | Work |
|---|---|
| Week 0 (before start) | Scope agreed, request list sent, access arranged |
| Week 1 | Read the data room. Interview the CTO, a lead engineer, the security lead and the operations lead. Get repository access. |
| Week 2 | Hands-on: build from source, run a dependency and licence scan, read CI and incident history, walk the production architecture. Raise red flags as found. |
| Week 3 | Follow-up interviews on gaps. Price each finding. Draft the report. |
| Week 4 (if needed) | With the deal lead's approval, check factual points with the target. Do not share severity ratings or cost ranges. Final report to the deal team. |

For a vendor selection, compress weeks 1 to 3 into two weeks and focus on the areas in the table above.

## What to ask for

- Architecture diagrams, decision records and the last two years of major incidents with postmortems.
- Read-only access to the main repositories and CI history for the last 6 to 12 months.
- An SBOM for each shipped product, and the result of a licence scan (for example with ScanCode or FOSSology).
- The last two penetration test reports and the current vulnerability backlog by severity and age.
- Data inventory, records of processing and data protection impact assessments.
- Hosting bills for 12 months and the result of the last restore test.
- Certification and audit reports, with open findings.
- An org chart with tenure, and who holds production access.
- Contracts for critical suppliers and commercial licences, with change of control and exit terms.

If the target cannot produce an item, record that as a finding. Absence of evidence is evidence.

## After signing: the first 100 days

For acquisitions, most of the technology cost lands after close. Turn the findings into a 100-day plan owned by a named integration lead:

- **Day 1:** access and security controls on the acquired estate: privileged accounts reset or brought under your identity provider, logging into your monitoring, and an agreed incident contact.
- **Carve-outs:** a list of transitional service agreements, each with an exit date and an owner.
- **Identity integration:** a plan and date for moving users and admins onto your identity provider.
- **Key people:** retention status reviewed at day 30 and day 90.
- **Contracts:** licence true-ups and the list of contracts to novate or renegotiate on change of control.
- **Platforms:** a decision per capability (keep, migrate, retire) using the [application portfolio (TIME)](../templates/leaders/application-portfolio.csv) model.

## Reporting findings

Lead with a one-page summary: the answer to each scoping question, the red flags, the total remediation cost range and your confidence. Then one row per finding.

| Severity | Definition (starting point) |
|---|---|
| Critical | Breaks the thesis or creates legal, regulatory or security exposure now. Fix before signing or change the deal. |
| High | Needs fixing within 6 months of signing and costs enough to affect the valuation or contract. |
| Medium | Needs fixing within 12 months; fits inside a normal budget. |
| Low | Improvement; no deadline. |

Each finding states: area, severity, evidence, impact, recommended remediation, cost range (people-weeks and money, low and high estimate), time to fix, and the confidence of the estimate (high, medium, low). Give ranges, never single figures. State what you could not see and how it limits the conclusions.

## Common mistakes

| Mistake | Fix |
|---|---|
| Reviewing the architecture the target describes, not the one that runs | Look at the bills, the CI history and the production configuration. |
| A long report with no prices | Every finding gets a severity and a cost range. |
| Red flags held for the final report | Raise them within 24 hours. |
| Ignoring licences until after signing | Run a licence scan in week 2. |
| Treating key people as a footnote | Name the key-person risks and plan retention with the deal team. |
| No exit view for outsourcing or vendor deals | Price the exit before the contract, not at renewal. |
| Scope that grows every day | Hold to the written questions; record new ones for after the deal. |

## Templates

- [Technical due diligence checklist](../templates/leaders/technical-due-diligence-checklist.md)
- [Vendor risk questionnaire](../templates/docs/vendor-risk-questionnaire.md)
- [Risk register](../templates/strategy/risk-register.csv)
- [Application portfolio (TIME)](../templates/leaders/application-portfolio.csv)

## Sources

- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
- SPDX License List: https://spdx.org/licenses/
- CycloneDX (ECMA-424): https://cyclonedx.org
- OpenSSF Scorecard: https://scorecard.dev
- CISA Known Exploited Vulnerabilities catalog: https://www.cisa.gov/known-exploited-vulnerabilities-catalog
- UK NCSC Board Toolkit: https://www.ncsc.gov.uk/collection/board-toolkit
- ICO, Marriott International Inc penalty notice, 30 October 2020 (a 2014 intrusion at Starwood, found in 2018 after the acquisition): https://ico.org.uk/media2/migrated/2618524/marriott-international-inc-mpn-20201030.pdf
