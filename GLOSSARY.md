# Glossary

Acronyms and terms used across the playbook, in plain words. Each line links to the page that uses the term most. When two words mean the same thing, the second points to the one the playbook uses.

Jump to: [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [V](#v) · [W](#w) · [Z](#z)

## A

| Term | Meaning | Read more |
|---|---|---|
| ADR (architecture decision record) | A short file in the repository that records one significant technical decision: the context, the options, the choice and its consequences. The playbook also says "decision record". | [Decision records](playbook/architecture/decision-records.md) |
| AI Act | The EU's Regulation (EU) 2024/1689 on artificial intelligence, amended by Regulation (EU) 2026/1744. Duties depend on the risk of the AI system. | [AI governance](playbook/ai/ai-governance.md) |
| API (application programming interface) | The defined way one program asks another for data or actions. | [API standards](playbook/architecture/api-standards.md) |
| Assured | The highest of the playbook's three levels: Standard plus the evidence, separation of duties and audit trail that regulators ask for. | [Maturity model](playbook/measurement/maturity-model.md) |

## B

| Term | Meaning | Read more |
|---|---|---|
| Blameless postmortem | A written review after an incident that asks how the system let the failure happen, not who to blame. | [Postmortems](playbook/reliability/postmortems.md) |
| Burn rate | How fast a service is using up its error budget. A burn rate of 1 uses the whole budget in exactly the SLO period. | [Service levels](playbook/reliability/service-levels.md) |
| Bus factor | How many people would have to leave before nobody can run or change a system. A bus factor of 1 is a single point of failure. | [Skills gap](playbook/people/skills-gap.md) |

## C

| Term | Meaning | Read more |
|---|---|---|
| C4 model | A way to draw software architecture at four zoom levels: context, containers, components and code. | [Architecture practice](playbook/architecture/architecture-practice.md) |
| CAB (change advisory board) | A meeting that approves production changes. The playbook replaces most CAB reviews with automated controls. | [Change management](playbook/reliability/change-management.md) |
| Canary release | Sending a new version to a small share of traffic first and widening it only if health checks pass. | [GitOps and deployment](playbook/delivery/gitops-and-deployment.md) |
| CAST (causal analysis based on system theory) | A method for analysing incidents that looks at the controls and feedback in the whole system, not one root cause. | [Root cause analysis](playbook/reliability/root-cause-analysis.md) |
| CBOM (cryptography bill of materials) | A list of the cryptographic algorithms, keys and libraries a system uses. | [Post-quantum readiness](playbook/security/post-quantum-readiness.md) |
| CC6, CC7, CC8 | Groups of SOC 2 criteria: CC6 covers access, CC7 system operations and monitoring, CC8 change management. | [Control mapping](playbook/compliance/control-mapping.md) |
| CD (continuous delivery or deployment) | Every change that passes the pipeline can be released (delivery) or is released automatically (deployment). | [GitOps and deployment](playbook/delivery/gitops-and-deployment.md) |
| CI (continuous integration) | Merging small changes to the main branch often, with an automatic build and test on every change. | [Continuous integration](playbook/delivery/continuous-integration.md) |
| CISA | The US Cybersecurity and Infrastructure Security Agency. It publishes the KEV catalogue. | [Vulnerability management](playbook/security/vulnerability-management.md) |
| CISO | Chief information security officer. | [For financial services](leaders/for-financial-services.md) |
| CODEOWNERS | A file that names who must review changes to each part of a repository. | [Code review](playbook/delivery/code-review.md) |
| CRA (Cyber Resilience Act) | The EU's Regulation (EU) 2024/2847 on security of products with digital elements, including a duty to report actively exploited vulnerabilities. | [Regulated industries](playbook/compliance/regulated-industries.md) |
| CVE | A public identifier for one known vulnerability, for example CVE-2021-44228. | [Vulnerability management](playbook/security/vulnerability-management.md) |
| CVSS (Common Vulnerability Scoring System) | A score from 0 to 10 for how severe a vulnerability is. It does not say how likely it is to be exploited. | [Vulnerability management](playbook/security/vulnerability-management.md) |
| Cynefin | A framework that sorts situations into clear, complicated, complex and chaotic, each needing a different way to decide. | [Decision making](leaders/decision-making.md) |

## D

| Term | Meaning | Read more |
|---|---|---|
| Data contract | An agreement between the team that produces data and the teams that use it: schema, meaning, quality and notice of changes. | [Data quality](playbook/data/data-quality.md) |
| Decision record | See ADR. | |
| DKIM, DMARC, SPF | Email settings published in your domain's DNS that let other mail servers check that mail claiming to come from you is genuine. | [For small and medium businesses](leaders/for-small-and-medium-businesses.md) |
| DNS | The internet's address book: it turns names such as example.org into network addresses. | |
| DORA metrics | Five software delivery measures from the DevOps Research and Assessment programme: deployment frequency, change lead time, change fail rate, failed deployment recovery time and rework rate. Not the same as EU DORA. | [Metrics](playbook/measurement/metrics.md) |
| DORA (EU regulation) | The EU's Digital Operational Resilience Act, Regulation (EU) 2022/2554, for banks, insurers and other financial firms. Not the same as DORA metrics. | [Regulated industries](playbook/compliance/regulated-industries.md) |
| DPI (digital public infrastructure) | Shared national platforms, such as digital identity, payments and data exchange, that many public and private services build on. | [For government](leaders/for-government.md) |
| DPIA (data protection impact assessment) | A written check of the risks to people before high-risk processing of personal data. Required by GDPR Article 35. | [Data security and privacy](playbook/data/data-security-and-privacy.md) |
| DPO | Data protection officer. | [Data security and privacy](playbook/data/data-security-and-privacy.md) |

## E

| Term | Meaning | Read more |
|---|---|---|
| ECDH, RSA | Public-key cryptography in wide use today. A large enough quantum computer could break both, so they are being replaced. | [Post-quantum readiness](playbook/security/post-quantum-readiness.md) |
| EPSS (Exploit Prediction Scoring System) | An estimate of the probability that a vulnerability will be exploited in the next 30 days. | [Vulnerability management](playbook/security/vulnerability-management.md) |
| Error budget | The amount of unreliability an SLO allows in a period. A 99.9% monthly target allows about 43 minutes of failure a month. | [Service levels](playbook/reliability/service-levels.md) |

## F

| Term | Meaning | Read more |
|---|---|---|
| Feature flag | A setting that turns a feature on or off without a new deployment. | [Feature flags](playbook/delivery/feature-flags.md) |
| FinOps | Managing cloud cost as a shared engineering and finance practice. | [FinOps](playbook/platform/finops.md) |
| FIPS 203, 204, 205 | The US NIST standards for post-quantum algorithms: ML-KEM, ML-DSA and SLH-DSA. | [Post-quantum readiness](playbook/security/post-quantum-readiness.md) |
| Foundation | The first of the playbook's three levels: the minimum that pays for itself at once. | [Maturity model](playbook/measurement/maturity-model.md) |

## G

| Term | Meaning | Read more |
|---|---|---|
| GDPR | The EU General Data Protection Regulation, Regulation (EU) 2016/679. The UK has its own version, UK GDPR. | [Data security and privacy](playbook/data/data-security-and-privacy.md) |
| GitOps | Keeping the desired state of a system in Git and letting an agent apply it, so every change is a reviewed commit. | [GitOps and deployment](playbook/delivery/gitops-and-deployment.md) |
| Golden path | The supported, documented way to build and run a common kind of service, made the easiest choice. Some pages and companies say "paved road". | [Golden paths](playbook/platform/golden-paths.md) |

## H

| Term | Meaning | Read more |
|---|---|---|
| HSM (hardware security module) | A tamper-resistant device that stores keys and performs cryptography without exposing the keys. | [Secrets](playbook/security/secrets.md) |

## I

| Term | Meaning | Read more |
|---|---|---|
| IaC (infrastructure as code) | Defining servers, networks and cloud services in version-controlled files instead of clicking in consoles. | [Infrastructure as code](playbook/delivery/infrastructure-as-code.md) |
| IC (incident commander) | The one person who leads the response to an incident and makes the calls. | [Incident management](playbook/reliability/incident-management.md) |
| ICT | Information and communication technology. | |
| ISO/IEC 27001 | The international standard for an information security management system. Annex A lists its controls. | [Control mapping](playbook/compliance/control-mapping.md) |
| ISO/IEC 42001 | The international standard for an AI management system. | [AI governance](playbook/ai/ai-governance.md) |
| ITIL | A widely used framework for IT service management. | [IT governance](playbook/operating-model/it-governance.md) |

## K

| Term | Meaning | Read more |
|---|---|---|
| Kata | A short exercise repeated to build a skill, for example reviewing a pull request. | [Exercises](exercises/README.md) |
| KEV (Known Exploited Vulnerabilities) | CISA's catalogue of vulnerabilities that attackers are known to be using. Fix these first. | [Vulnerability management](playbook/security/vulnerability-management.md) |
| KMS (key management service) | A service, often from a cloud provider, that creates, stores and controls the use of encryption keys. | [Secrets](playbook/security/secrets.md) |

## L

| Term | Meaning | Read more |
|---|---|---|
| LGTM | "Looks good to me": a quick approval in code review, often given without a careful read. | [Code review](playbook/delivery/code-review.md) |
| LLM (large language model) | The kind of AI model behind chat assistants and code assistants. | [Building with AI](playbook/ai/building-with-ai.md) |

## M

| Term | Meaning | Read more |
|---|---|---|
| MCP (Model Context Protocol) | An open protocol for connecting AI assistants and agents to tools and data sources. | [AI architecture patterns](playbook/ai/ai-architecture-patterns.md) |
| MFA (multi-factor authentication) | Signing in with something more than a password, such as a code from a phone app or a security key. "Phishing-resistant" MFA (security keys, passkeys) cannot be tricked into working on a fake site. | [Access control](playbook/security/access-control.md) |
| ML-KEM | The NIST post-quantum algorithm for agreeing a shared key (FIPS 203). | [Post-quantum readiness](playbook/security/post-quantum-readiness.md) |

## N

| Term | Meaning | Read more |
|---|---|---|
| NCSC | The UK's National Cyber Security Centre. | [For small and medium businesses](leaders/for-small-and-medium-businesses.md) |
| NIS2 | The EU's Directive (EU) 2022/2555 on cyber security for essential and important entities. | [Regulated industries](playbook/compliance/regulated-industries.md) |
| NIST | The US National Institute of Standards and Technology. It publishes the SSDF, the Cybersecurity Framework and the post-quantum standards. | |

## O

| Term | Meaning | Read more |
|---|---|---|
| OKR (objectives and key results) | A goal-setting method: a qualitative objective with a few measurable results. | [Strategy toolkit](leaders/strategy-toolkit.md) |
| On-call | Being the person who responds when a service pages outside or during working hours, on a rotation. | [On-call](playbook/reliability/on-call.md) |
| OWASP | The Open Worldwide Application Security Project. It publishes the Top 10 lists of web and LLM application risks. | [AI application security](playbook/ai/ai-application-security.md) |

## P

| Term | Meaning | Read more |
|---|---|---|
| p95, p99 | The 95th or 99th percentile: 95% or 99% of requests were faster than this. | [Service levels](playbook/reliability/service-levels.md) |
| PaaS, SaaS | Platform as a service (you deploy code, the provider runs the servers) and software as a service (you use a finished application online). | [Cloud native](playbook/platform/cloud-native.md) |
| Paved road | See golden path. | |
| PQC (post-quantum cryptography) | Cryptography designed to stay secure against a large quantum computer. | [Post-quantum readiness](playbook/security/post-quantum-readiness.md) |
| Profile | The playbook's adoption path for one size of organisation: SME, solo, startup, scale-up or enterprise, plus public sector and regulated overlays. | [Profiles](profiles/README.md) |
| PRR (production readiness review) | A checklist review before a service takes real traffic. | [Production readiness](playbook/reliability/production-readiness.md) |

## R

| Term | Meaning | Read more |
|---|---|---|
| RACI | Responsible, accountable, consulted, informed: a table of who does what for each decision. | [Decision rights](playbook/operating-model/decision-rights.md) |
| RAG (retrieval-augmented generation) | Giving an AI model relevant documents at question time so it answers from them, not only from its training. | [AI architecture patterns](playbook/ai/ai-architecture-patterns.md) |
| RCA (root cause analysis) | Finding why an incident happened. The playbook looks for several contributing factors, not one root cause. | [Root cause analysis](playbook/reliability/root-cause-analysis.md) |
| RFC (request for comments) | A written proposal for a significant change, shared for comment for a fixed period before a decision. | [RFCs](playbook/architecture/rfcs.md) |
| RPO (recovery point objective) | The most data you can afford to lose, measured in time. An RPO of 1 hour means backups or replicas no more than 1 hour old. | [Backup and recovery](playbook/reliability/backup-and-recovery.md) |
| RTO (recovery time objective) | How long a service may be down before it must be back. | [Backup and recovery](playbook/reliability/backup-and-recovery.md) |
| Runbook | Step-by-step instructions for handling one alert or operational task. | [Runbook template](templates/docs/runbook.md) |

## S

| Term | Meaning | Read more |
|---|---|---|
| SBOM (software bill of materials) | A list of every component and version inside a piece of software. | [Supply chain](playbook/security/supply-chain.md) |
| SEV1, SEV2, SEV3 | Incident severity levels. SEV1 is the most serious. | [Incident management](playbook/reliability/incident-management.md) |
| SLA (service level agreement) | A promise to a customer about reliability, usually with a penalty if missed. Set it looser than the internal SLO. | [Service levels](playbook/reliability/service-levels.md) |
| SLI (service level indicator) | A measure of what users experience, for example the share of requests that succeed in under 300 ms. | [Service levels](playbook/reliability/service-levels.md) |
| SLO (service level objective) | A target for an SLI over a period, for example 99.9% of requests succeed each month. | [Service levels](playbook/reliability/service-levels.md) |
| SLSA (Supply-chain Levels for Software Artifacts) | A framework of levels for proving how software was built and that nobody tampered with it. | [Supply chain](playbook/security/supply-chain.md) |
| SME | Small or medium business. In the playbook, one that uses software but does not build it. | [SME profile](profiles/sme.md) |
| SOC 2 | An audit report on a service provider's controls, against the AICPA Trust Services Criteria. | [Control mapping](playbook/compliance/control-mapping.md) |
| SPACE | A framework for developer productivity: satisfaction and well-being, performance, activity, communication and collaboration, efficiency and flow. | [Metrics](playbook/measurement/metrics.md) |
| SRE (site reliability engineering) | Running services with software engineering methods: SLOs, error budgets, automation and blameless learning. | [Service levels](playbook/reliability/service-levels.md) |
| SSDF (Secure Software Development Framework) | NIST SP 800-218, a set of secure development practices. | [Secure development](playbook/security/secure-development.md) |
| SSO (single sign-on) | One company login for many services, so access can be removed in one place. | [Access control](playbook/security/access-control.md) |
| Standard | The middle of the playbook's three levels: shared practice across several teams, measured. | [Maturity model](playbook/measurement/maturity-model.md) |
| STRIDE | A threat modelling checklist: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. | [Secure development](playbook/security/secure-development.md) |
| Strangler fig | Replacing a legacy system piece by piece, routing one function at a time to the new system. | [Legacy modernisation](playbook/architecture/legacy-modernisation.md) |

## T

| Term | Meaning | Read more |
|---|---|---|
| Tabletop exercise | A team talks through a realistic incident scenario, step by step, without touching real systems. | [Exercises](exercises/README.md) |
| TDD (test-driven development) | Writing a failing test first, then the code that makes it pass, then tidying up. | [Test-driven development](playbook/quality/test-driven-development.md) |
| Tech radar | A list of tools and techniques rated adopt, trial, assess or hold. | [Tech radar](playbook/architecture/tech-radar.md) |
| Tier 1, Tier 2, Tier 3 | Service classes by business impact. Tier 1 services are the ones the business cannot run without and get the strictest targets. | [Production readiness](playbook/reliability/production-readiness.md) |
| TIME model | Sorting each application into Tolerate, Invest, Migrate or Eliminate. | [Strategy toolkit](leaders/strategy-toolkit.md) |
| Toil | Manual, repetitive operational work that grows with the service and could be automated. | [Business case](playbook/strategy/business-case.md) |
| Two-way door | A decision you can reverse cheaply, so decide it fast. A one-way door is hard to reverse and needs more care. | [Decision making](leaders/decision-making.md) |

## V

| Term | Meaning | Read more |
|---|---|---|
| VEX (Vulnerability Exploitability eXchange) | A statement that says whether a known vulnerability in a component actually affects your product. | [Supply chain](playbook/security/supply-chain.md) |

## W

| Term | Meaning | Read more |
|---|---|---|
| Wardley map | A map of the parts of a service, placed by how visible they are to users and how mature (from new to commodity) each one is. | [Strategy toolkit](leaders/strategy-toolkit.md) |
| WCAG (Web Content Accessibility Guidelines) | The W3C standard for accessible websites and apps. Level AA of version 2.2 is the usual legal floor. | [Public sector](playbook/compliance/public-sector.md) |
| WIP (work in progress) | Work started but not finished. A WIP limit caps it so work finishes sooner. | [Agile and Scrum](playbook/ways-of-working/agile-and-scrum.md) |

## Z

| Term | Meaning | Read more |
|---|---|---|
| Zero trust | Deciding each access request from the user's and device's identity and state, never from network location alone. | [Zero trust](playbook/security/zero-trust.md) |
