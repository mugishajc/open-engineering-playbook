# Regulated overlay

Apply this overlay on top of your size profile when a regulator can fine you, stop you trading or ask for evidence of how you build and run software. It raises the target to Assured: every control produces evidence automatically, no one person can write, approve and deploy the same change, and incident reporting deadlines are tested before you need them. Done well, this makes delivery faster, because evidence comes from the pipeline instead of from engineers' time.

## How overlays work

1. Pick your size profile first: [SME](sme.md), [solo](solo.md), [startup](startup.md), [scale-up](scale-up.md) or [enterprise](enterprise.md). Its week 1 to year 1 tables still apply.
2. Add the rows below at each horizon. Where both tables name the same page, do the overlay version.
3. Your target becomes Assured in every area. The assessment does this when your answers file says `overlays = ["regulated"]`.
4. Scope by regulation and service tier. Systems in the regulator's scope need all of it. A marketing site may not. Record each exception, its reason and its owner in a [decision record](../playbook/architecture/decision-records.md).

You can apply both overlays. A state-owned bank or a public health service applies regulated and [public sector](public-sector.md) together.

Levels never lower a legal duty. The reporting deadlines, registers, records of processing, impact assessments and contract terms that a law sets apply from the day the law applies to you, whatever level you are working towards. See the [legal floor](../playbook/data/data-security-and-privacy.md#legal-floor-applies-at-every-level) for data protection.

## With the SME profile

A clinic, pharmacy, insurance broker or other small regulated business that does not build software does not need most of this page. Assured applies to the controls your regulator inspects, not to engineering practices you do not run. Add only these rows to the [SME profile](sme.md):

| When | Add this |
|---|---|
| Week 1 | List the rules that apply to you, the regulator for each, and every reporting deadline, for example a data breach report within 72 hours |
| Month 1 | Name who reports an incident to the regulator, including out of hours, and put the deadlines in the printed first-hour plan |
| Quarter 1 | Check that every supplier holding regulated data (for example patient records) has a contract with breach notice within 24 hours of the supplier becoming aware, data location and exit terms |
| Year 1 | Restore your most important system from backup, compare the time with your recovery target, and keep the written result as evidence |

Ask your sector body or regulator whether it publishes guidance for small firms, and follow that first.

## Who this is for

- Banks, payment firms, insurers, investment firms.
- Health providers and health software makers.
- Telecom operators, energy, water, transport and other critical infrastructure.
- Their software suppliers, who usually inherit the same controls through contracts.

## Rules you are likely to meet

Examples, not legal advice. Check the current text with your compliance team.

| Rule | What it means for engineering |
|---|---|
| EU Digital Operational Resilience Act, Regulation (EU) 2022/2554, applies from 17 January 2025. It is unrelated to the DORA delivery metrics. | ICT risk management, incident reporting, resilience testing and oversight of ICT third parties for financial entities |
| EU NIS2 Directive (EU) 2022/2555, national laws due by 17 October 2024 | Risk management and incident reporting for essential and important entities |
| EU Cyber Resilience Act, Regulation (EU) 2024/2847 | Since 11 September 2026, manufacturers report actively exploited vulnerabilities and severe incidents: early warning within 24 hours of becoming aware, notification within 72 hours, and a final report 14 days after a fix is available (vulnerabilities) or 1 month after the notification (incidents). This covers products placed on the market before 11 December 2027 too. Most other obligations apply from 11 December 2027. See [vulnerability management](../playbook/security/vulnerability-management.md). |
| EU AI Act, Regulation (EU) 2024/1689 | Prohibited practices apply from 2 February 2025. After Regulation (EU) 2026/1744, high-risk obligations apply from 2 December 2027 (Annex III) and 2 August 2028 (Annex I products), and new prohibitions on non-consensual intimate imagery and child sexual abuse material from 2 December 2026. See [AI governance](../playbook/ai/ai-governance.md). |
| ISO/IEC 27001:2022 Annex A, controls 8.25 to 8.33 | Secure development life cycle, secure coding, security testing, separation of environments, change management |
| SOC 2 Trust Services Criteria, CC8.1 and CC7 | Change management, system operations and incident response |
| Data protection law, such as EU GDPR, Kenya Data Protection Act 2019, Rwanda Law No 058/2021, Nigeria Data Protection Act 2023, Brazil LGPD, India DPDP Act 2023 | Records of processing, privacy by design, impact assessments, breach notification and a breach register, and a transfer mechanism for data leaving the country. See [data security and privacy](../playbook/data/data-security-and-privacy.md). |
| India CERT-In Directions of 28 April 2022 (IT Act section 70B(6)) | Service providers, intermediaries, data centres and body corporates report listed cyber incidents to CERT-In within 6 hours of noticing them, and keep ICT system logs for a rolling 180 days within India |
| EU NIS2 Implementing Regulation (EU) 2024/2690 | For cloud, data centre, managed service and managed security providers, DNS and similar digital providers: detailed technical measures and significant incident criteria that apply directly |

## What it adds by area

| Area | Assured adds |
|---|---|
| Strategy | Technical risks in the enterprise risk register, reviewed every 90 days |
| Operating model | Separation of duties enforced in tooling; regular reporting to the board or audit committee |
| Product | No experiments on prices, credit or entitlements without compliance sign-off; customer communications reviewed before launch; a fair value assessment per product where rules require it |
| Project management | A written project management method tailored from a recognised standard; independent assurance at major gates; gate records kept. EU financial entities keep an ICT project management policy |
| Ways of working | Every change traceable to an approved requirement or risk item |
| Delivery | Change evidence (request, reviewer, CI result, deployer) for any single change retrievable within 1 hour, and a sample of 25 changes within 1 working day, for 12 months or longer |
| Quality | Test results kept as release evidence |
| Reliability | Yearly disaster recovery test against written recovery time and recovery point objectives |
| Security | SBOM and signed releases verified before deploy; cryptographic inventory and post-quantum plan |
| Data | Retention and deletion enforced by automation, with deletion logs |
| AI | AI risk managed under ISO/IEC 42001 or the NIST AI RMF, with records an auditor can review |
| Architecture | Decision records name the approver and are retained |
| Platform | Builds work from internal mirrors; no direct internet dependency in the release path |
| People | Secure coding and data protection training recorded yearly |
| Measurement | Metrics and assessment results retained for auditors |
| Compliance | Evidence collected automatically into tamper-evident storage; reporting deadlines tested |

## Week 1

| Add this | Read | Template |
|---|---|---|
| List the rules that apply, the regulator for each, and every reporting deadline with its clock start | [Regulated industries](../playbook/compliance/regulated-industries.md) | |
| Name the owner for each rule and for incident reporting out of hours | [Roles](../playbook/operating-model/roles.md) | [raci.csv](../templates/strategy/raci.csv) |
| Classify data, marking which systems hold regulated data | [Data governance](../playbook/data/data-governance.md) | [data-classification.md](../templates/docs/data-classification.md) |

## Month 1

| Add this | Read | Template |
|---|---|---|
| Enforce separation of duties: required reviewers who are not the author, and deployment by pipeline only | [Decision rights](../playbook/operating-model/decision-rights.md), [Access control](../playbook/security/access-control.md) | [default-branch.json](../templates/github/rulesets/default-branch.json), [CODEOWNERS](../templates/github/CODEOWNERS) |
| Link every deployment to its change request, reviewer and CI run | [Change management](../playbook/reliability/change-management.md), [Release management](../playbook/delivery/release-management.md) | [release-checklist.md](../templates/docs/release-checklist.md) |
| Code assistant policy with data limits for regulated data, and an AI use register | [Code assistants](../playbook/people/code-assistants.md), [AI governance](../playbook/ai/ai-governance.md) | [code-assistant-policy.md](../templates/docs/code-assistant-policy.md), [ai-use-case-assessment.md](../templates/docs/ai-use-case-assessment.md) |
| Review every ICT supplier that supports a critical function | [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) | [vendor-risk-questionnaire.md](../templates/docs/vendor-risk-questionnaire.md) |
| Write the incident reporting runbook with the regulator deadlines in it | [Incident management](../playbook/reliability/incident-management.md) | [runbook.md](../templates/docs/runbook.md), [incident-update.md](../templates/docs/incident-update.md) |

## Quarter 1

| Add this | Read | Template |
|---|---|---|
| Build the control map from your rules to the playbook practices and their evidence | [Control mapping](../playbook/compliance/control-mapping.md) | |
| Generate an SBOM and sign every release; verify before deploy | [Supply chain](../playbook/security/supply-chain.md) | [sbom-and-sign.yml](../templates/security/workflows/sbom-and-sign.yml), [gitlab-supply-chain.yml](../templates/security/gitlab-supply-chain.yml), [scorecard.yml](../templates/security/workflows/scorecard.yml) |
| Threat model every system in scope; test AI features against the OWASP Top 10 for LLM Applications | [Secure development](../playbook/security/secure-development.md), [AI application security](../playbook/ai/ai-application-security.md) | [threat-model.md](../templates/docs/threat-model.md) |
| Set recovery time and recovery point objectives per service tier | [Backup and recovery](../playbook/reliability/backup-and-recovery.md), [Production readiness](../playbook/reliability/production-readiness.md) | [production-readiness-review.md](../templates/docs/production-readiness-review.md) |
| Make every release rollback-safe, and record time to rollback | [Rollbacks](../playbook/reliability/rollbacks.md) | |
| Start a cryptographic inventory, beginning with data that must stay secret for 10 years or more | [Post-quantum readiness](../playbook/security/post-quantum-readiness.md) | [crypto-inventory.csv](../templates/docs/crypto-inventory.csv) |
| Report to the board or audit committee on a short set of agreed measures | [IT governance](../playbook/operating-model/it-governance.md) | |
| Agree with compliance which product experiments and price tests may be shown to customers, and keep each brief as a record | [Product metrics and experiments](../playbook/product/product-metrics-and-experiments.md#assured), [Pricing and packaging](../playbook/product/pricing-and-packaging.md#assured) | [experiment-brief.md](../templates/product/experiment-brief.md) |

## Year 1

| Add this | Read | Template |
|---|---|---|
| Collect control evidence from pipelines into tamper-evident storage | [Control mapping](../playbook/compliance/control-mapping.md) | |
| Run a reporting drill: a simulated incident reported to an internal "regulator" inside the real deadline | [Regulated industries](../playbook/compliance/regulated-industries.md), [Incident management](../playbook/reliability/incident-management.md) | [incident-update.md](../templates/docs/incident-update.md) |
| Run and record a disaster recovery test for every critical service | [Backup and recovery](../playbook/reliability/backup-and-recovery.md) | |
| Postmortems that trace contributing factors across detection, response and recovery | [Root cause analysis](../playbook/reliability/root-cause-analysis.md) | [postmortem.md](../templates/docs/postmortem.md) |
| Adopt an AI management framework for AI used in decisions about customers | [AI governance](../playbook/ai/ai-governance.md) | |
| A post-quantum migration plan for the systems in the inventory | [Post-quantum readiness](../playbook/security/post-quantum-readiness.md) | |
| Exit plans for critical ICT suppliers, reviewed every year and tested with a real, timed data export and import (paper walk-throughs count only for less critical suppliers) | [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) | |
| A written project management method with independent assurance at major gates; EU financial entities map it to their ICT project management policy | [Risks, RAID logs and stage gates](../playbook/project-management/risks-raid-and-stage-gates.md#assured), [A modern PMO](../playbook/project-management/modern-pmo.md) | [stage-gate-checklist.md](../templates/project/stage-gate-checklist.md) |
| Internal mirrors for packages and images in the release path | [Cloud, on-premises and air-gapped](../playbook/platform/cloud-on-prem-air-gapped.md) | |
| Four committed assessments; every in-scope system at Assured or with recorded exceptions | [Maturity model](../playbook/measurement/maturity-model.md) | [assessment](../assessment/README.md) |

## Do not add

| Avoid | Why |
|---|---|
| A change advisory board meeting for every change | Pre-approved standard changes with automatic evidence satisfy change management controls with less delay. See [change management](../playbook/reliability/change-management.md). |
| Screenshots and spreadsheets as evidence | They cannot be verified and they cost engineering time every audit. |
| Freezing dependency updates for stability | It keeps known vulnerabilities in production. |
| Long release trains to reduce risk | Large batches make each release riskier and harder to roll back. |
| Separate "compliance copies" of pipelines | Two pipelines drift. Put the controls in the one pipeline everyone uses. |

## Sources

- Regulation (EU) 2022/2554, Digital Operational Resilience Act: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Directive (EU) 2022/2555, NIS2: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Regulation (EU) 2024/2847, Cyber Resilience Act: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- Regulation (EU) 2024/1689, AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj, as amended by Regulation (EU) 2026/1744: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- Commission Implementing Regulation (EU) 2024/2690 (NIS2 technical measures): https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj
- CERT-In, Directions under section 70B(6) of the IT Act, 28 April 2022: https://www.cert-in.org.in/PDF/CERT-In_Directions_70B_28.04.2022.pdf
- NIST Secure Software Development Framework: https://csrc.nist.gov/projects/ssdf
- OpenSSF Scorecard: https://scorecard.dev
