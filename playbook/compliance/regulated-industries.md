# Regulated industries

Banks, insurers, health providers, telecoms operators and critical infrastructure operators can deliver software often and safely if controls are built into the pipeline instead of added as meetings. Enforce separation of duties with branch protection and signed releases, let the pipeline produce the change record, and keep a weekly change board only for the small set of changes that automation cannot judge. Regulators ask for control and evidence. They rarely require a specific meeting.

## Outcomes

Starting points. Tune them to your organisation.

- At least 90% of production changes are standard changes approved by the pipeline, with a complete evidence trail and no manual ticket.
- Every production change has an author and a different approver, enforced by tooling, with no exceptions outside documented emergency procedures.
- Emergency changes get retrospective review within 2 working days, 100% of the time.
- Evidence for any single change (who, what, why, tests, approval, deployment, outcome) can be produced within 1 hour; a sample of 25 changes within 1 working day.
- Every ICT supplier that supports a critical or important function has due diligence, a contract with audit and exit rights, and an exit plan reviewed every year and tested with a real, timed data export and import at least once a year.

## Separation of duties with automation

A weekly change advisory board (CAB) reviews changes after the risk is already set by their size and design. It slows delivery and its approvals often rest on little information. Replace it, for most changes, with controls that run on every change.

| Control objective | Automated control | Evidence |
|---|---|---|
| No single person can change production alone | protected branch; at least one approver who is not the author; CODEOWNERS for sensitive paths | pull request history |
| Only reviewed code is deployed | deploy only from the protected branch; build from a clean runner; signed artefacts; deploy checks the signature | CI logs, provenance, signature verification logs |
| Changes are tested | required status checks for tests, security scans and policy checks | CI results stored with the commit |
| Production access is limited | no standing write access; just-in-time access with approval and expiry | access logs, access reviews |
| Changes can be traced to a reason | pull request links to a ticket or decision record | pull request metadata |
| Failed changes are detected and reversed | progressive rollout, automated rollback on SLO breach | deployment and rollback logs |

See [code review](../delivery/code-review.md), [release management](../delivery/release-management.md), [supply chain](../security/supply-chain.md), [access control](../security/access-control.md) and [change management](../reliability/change-management.md).

## Change approval that does not slow delivery

Classify changes so that review effort matches risk.

| Class | Examples | Approval | Target lead time (starting point) |
|---|---|---|---|
| Standard | application change through the pipeline with all checks green | the pipeline, plus peer review | same day |
| Normal, higher risk | schema change on a core ledger, new external integration, change to authentication | peer review plus named service owner; optional asynchronous review by risk | 1 to 3 days |
| Major | new critical system, change of hosting provider, change to a model used in decisions | architecture review and risk sign-off; CAB if your policy requires | per plan |
| Emergency | fix during an incident | incident commander; retrospective review within 2 working days | immediate |

Measure change fail rate and failed deployment recovery time for each class. If standard changes fail no more often than normal ones, expand the standard class. See [metrics](../measurement/metrics.md).

## Evidence trails

- Keep pull requests, CI logs, deployment records and incident records in their systems of record, retained for the longest period any rule requires.
- Use the [control mapping](control-mapping.md) to show one piece of evidence against many requirements.
- Protect evidence from change: write-once storage or a signed log.
- Prove the population is complete: reconcile every production deployment to an approved pull request or emergency change record, and keep the ruleset bypass log (see [control mapping](control-mapping.md)).
- Give internal audit and the second line read-only access so they can test controls directly.

## Third-party and outsourcing risk

- Keep a register of ICT third-party arrangements, with the function each supports and whether it is critical or important. EU financial entities must keep such a register under the EU Digital Operational Resilience Act.
- Do due diligence before signing: security, resilience, sub-contractors, location of data and staff, financial health.
- Contracts include audit and access rights, incident notification times, service levels, data location, sub-contracting limits, termination rights and exit assistance.
- Write exit plans for critical suppliers and test them with a real, timed data export and import every year; paper walk-throughs count only for less critical suppliers. See [third-party and SaaS risk](../security/third-party-and-saas-risk.md) and [build, buy, adopt or partner](../strategy/build-buy-adopt.md).
- Watch concentration: several critical functions on one provider is a risk to record and manage.

## EU DORA: ICT risk for financial entities

The Digital Operational Resilience Act (Regulation (EU) 2022/2554) applies from 17 Jan 2025. It is unrelated to the DORA software delivery metrics. Its main areas and the playbook practices that support them:

| DORA area | Playbook practices |
|---|---|
| ICT risk management framework (Chapter II, with the RTS in Delegated Regulation (EU) 2024/1774) | [technical strategy](../strategy/technical-strategy.md), [engineering governance](../operating-model/engineering-governance.md), [secure development](../security/secure-development.md), [backup and recovery](../reliability/backup-and-recovery.md) |
| ICT-related incident management and reporting (Chapter III, with Delegated Regulation (EU) 2025/301 for report content and timing) | [incident management](../reliability/incident-management.md), [postmortems](../reliability/postmortems.md) |
| Digital operational resilience testing (Chapter IV) | [testing](../delivery/testing.md), [production readiness](../reliability/production-readiness.md), restore tests |
| ICT third-party risk (Chapter V) | [third-party and SaaS risk](../security/third-party-and-saas-risk.md), [build, buy, adopt or partner](../strategy/build-buy-adopt.md) |

## Sector notes

| Sector | What to add |
|---|---|
| Banks and insurers | model risk management for models used in credit, pricing, fraud and capital: independent validation before use and after material change (US SR 11-7; UK PRA SS1/23); EU DORA; payment card rules (PCI DSS) for card data. See [for financial services](../../leaders/for-financial-services.md) |
| Health | HIPAA in the US, with breach notice to affected individuals without unreasonable delay and within 60 days of discovery (45 CFR 164.404); EU Medical Device Regulation (EU) 2017/745 where software is a medical device (Annex VIII, Rule 11); European Health Data Space Regulation (EU) 2025/327 for electronic health record systems; in England, the NHS clinical safety standards DCB0129 (manufacturers) and DCB0160 (deploying organisations) |
| Telecoms | lawful interception and data retention duties; national telecom security rules, such as the UK Telecommunications (Security) Act 2021 and its code of practice; NIS2 where transposed |
| Critical infrastructure (energy, water, transport) | operational technology separation from IT; NIS2 where transposed; safety cases for control system changes; long-lived systems with slow patch windows |

## Model risk

When a change touches a model that drives decisions about customers or capital, add three steps to the normal change: independent validation of the model before production, monitoring of its performance and inputs in production, and a record of who approved it. Use the same approach for AI systems. US banks follow SR 11-7. UK banks with internal model approval follow PRA SS1/23, which covers AI models and expects a model inventory, risk tiering and an accountable senior manager. In the EU, AI that scores the creditworthiness of individuals is high-risk under the AI Act. See [AI governance](../ai/ai-governance.md).

## Practice

### Foundation

Smaller regulated firms and fintechs. The reporting duties, registers and contract terms that your regulator sets apply at this level too; levels never lower a legal duty. Protected branches with an independent approver, signed releases, CI evidence kept for the retention period, a supplier register, and an incident process that meets reporting deadlines.

### Standard

Mid-sized and large firms. Everything in Foundation, plus the change classes above, automated evidence collection, quarterly control testing on samples, and tested exit plans for critical suppliers.

### Assured

Systemically important institutions and critical infrastructure. Everything in Standard, plus independent challenge from the second line on every major change, advanced resilience testing where required, and regular regulator engagement planned into the [transition playbook](../strategy/transition-playbook.md).

## Cloud, on-premises and air-gapped

Using cloud for a critical or important function is usually treated as outsourcing. Notify or consult your regulator as your rules require, and keep a credible exit plan. On-premises and air-gapped systems in critical infrastructure still need the same automated controls: self-hosted source control, CI and signing, with evidence kept on site. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Weekly CAB for every change | Automate standard changes. Keep the CAB for major ones. |
| Approvals by people who did not read the change | Approval by a reviewer in the pull request, with the diff. |
| Evidence assembled by hand before audits | Collect it from systems of record continuously. |
| Exit plans that exist only on paper | Run a real, timed export and import for critical suppliers every year. |

## Templates

- [Risk register](../../templates/strategy/risk-register.csv)
- [RACI](../../templates/strategy/raci.csv)
- [Production readiness review](../../templates/docs/production-readiness-review.md)
- [Vendor risk questionnaire](../../templates/docs/vendor-risk-questionnaire.md)

## Sources

- Regulation (EU) 2022/2554 (Digital Operational Resilience Act): https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- NIS2 Directive (EU) 2022/2555: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Board of Governors of the Federal Reserve System, SR 11-7, Guidance on Model Risk Management: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm
- PCI Security Standards Council: https://www.pcisecuritystandards.org
- US HHS, HIPAA: https://www.hhs.gov/hipaa and 45 CFR 164.404: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D/section-164.404
- PRA, SS1/23 Model risk management principles for banks: https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- Commission Delegated Regulation (EU) 2024/1774: https://eur-lex.europa.eu/eli/reg_del/2024/1774/oj
- Regulation (EU) 2017/745 (Medical Device Regulation): https://eur-lex.europa.eu/eli/reg/2017/745/oj
- Regulation (EU) 2025/327 (European Health Data Space): https://eur-lex.europa.eu/eli/reg/2025/327/oj
- NHS England, DCB0129 clinical risk management (DCB0160 is linked from the same page): https://digital.nhs.uk/data-and-information/information-standards/governance/latest-activity/standards-and-collections/dcb0129-clinical-risk-management-its-application-in-the-manufacture-of-health-it-systems
- UK Telecommunications (Security) Act 2021: https://www.legislation.gov.uk/ukpga/2021/31/contents
- AICPA Trust Services Criteria (SOC 2): https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
