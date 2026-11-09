# Regulated overlay

Apply this overlay on top of your size profile when a regulator can fine you, stop you trading or ask for evidence of how you build and run software. It raises the target to Assured: every control produces evidence automatically, no one person can write, approve and deploy the same change, and incident reporting deadlines are tested before you need them. Done well, this makes delivery faster, because evidence comes from the pipeline instead of from engineers' time.

## How overlays work

1. Pick your size profile first: [solo](solo.md), [startup](startup.md), [scale-up](scale-up.md) or [enterprise](enterprise.md). Its week 1 to year 1 tables still apply.
2. Add the rows below at each horizon. Where both tables name the same page, do the overlay version.
3. Your target becomes Assured in every area. The assessment does this when your answers file says `overlays = ["regulated"]`.
4. Scope by regulation and service tier. Systems in the regulator's scope need all of it. A marketing site may not. Record each exception, its reason and its owner in a [decision record](../playbook/architecture/decision-records.md).

You can apply both overlays. A state-owned bank or a public health service applies regulated and [public sector](public-sector.md) together.

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
| EU Cyber Resilience Act, Regulation (EU) 2024/2847 | Manufacturers report actively exploited vulnerabilities and severe incidents from 11 September 2026: early warning within 24 hours, notification within 72 hours. Most other obligations apply from 11 December 2027. |
| EU AI Act, Regulation (EU) 2024/1689 | Prohibited practices apply from 2 February 2025. Dates for high-risk systems have been revised; check EUR-Lex for the current ones. |
| ISO/IEC 27001:2022 Annex A, controls 8.25 to 8.33 | Secure development life cycle, secure coding, security testing, separation of environments, change management |
| SOC 2 Trust Services Criteria, CC8.1 and CC7 | Change management, system operations and incident response |
| Data protection law, such as EU GDPR, Kenya Data Protection Act 2019, Rwanda Law No 058/2021, Nigeria Data Protection Act 2023, Brazil LGPD, India DPDP Act 2023 | Privacy by design, impact assessments, breach notification |

## What it adds by area

| Area | Assured adds |
|---|---|
| Strategy | Technical risks in the enterprise risk register, reviewed every 90 days |
| Operating model | Separation of duties enforced in tooling; regular reporting to the board or audit committee |
| Ways of working | Every change traceable to an approved requirement or risk item |
| Delivery | Change evidence (request, reviewer, CI result, deployer) retrievable within one hour for 12 months or longer |
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

## Year 1

| Add this | Read | Template |
|---|---|---|
| Collect control evidence from pipelines into tamper-evident storage | [Control mapping](../playbook/compliance/control-mapping.md) | |
| Run a reporting drill: a simulated incident reported to an internal "regulator" inside the real deadline | [Regulated industries](../playbook/compliance/regulated-industries.md), [Incident management](../playbook/reliability/incident-management.md) | [incident-update.md](../templates/docs/incident-update.md) |
| Run and record a disaster recovery test for every critical service | [Backup and recovery](../playbook/reliability/backup-and-recovery.md) | |
| Postmortems that trace contributing factors across detection, response and recovery | [Root cause analysis](../playbook/reliability/root-cause-analysis.md) | [postmortem.md](../templates/docs/postmortem.md) |
| Adopt an AI management framework for AI used in decisions about customers | [AI governance](../playbook/ai/ai-governance.md) | |
| A post-quantum migration plan for the systems in the inventory | [Post-quantum readiness](../playbook/security/post-quantum-readiness.md) | |
| Exit plans for critical ICT suppliers, tested on paper | [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) | |
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
- Regulation (EU) 2024/1689, AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- NIST Secure Software Development Framework: https://csrc.nist.gov/projects/ssdf
- OpenSSF Scorecard: https://scorecard.dev
