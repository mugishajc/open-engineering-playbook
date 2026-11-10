# Glossary

Acronyms and terms used across the playbook, in plain words. Each line links to the page that uses the term most. When two words mean the same thing, the second points to the one the playbook uses.

Jump to: [A](#a) · [B](#b) · [C](#c) · [D](#d) · [E](#e) · [F](#f) · [G](#g) · [H](#h) · [I](#i) · [J](#j) · [K](#k) · [L](#l) · [M](#m) · [N](#n) · [O](#o) · [P](#p) · [R](#r) · [S](#s) · [T](#t) · [U](#u) · [V](#v) · [W](#w) · [Z](#z)

## A

| Term | Meaning | Read more |
|---|---|---|
| AARRR | Dave McClure's five product funnel measures: acquisition, activation, retention, referral and revenue. | [Product metrics and experiments](playbook/product/product-metrics-and-experiments.md#choosing-what-to-measure) |
| A/B test | A controlled experiment that randomly shows users the current version or a change and compares what they do. | [Product metrics and experiments](playbook/product/product-metrics-and-experiments.md#experiment-design) |
| ADR (architecture decision record) | A short file in the repository that records one significant technical decision: the context, the options, the choice and its consequences. The playbook also says "decision record". | [Decision records](playbook/architecture/decision-records.md) |
| Agentic | A system or workflow where an AI model plans and executes multi-step tasks with tool access and limited human oversight at defined checkpoints, rather than answering a single prompt. | [AI engineering practices](playbook/ai/ai-engineering-practices.md) |
| AI Act | The EU's Regulation (EU) 2024/1689 on artificial intelligence, amended by Regulation (EU) 2026/1744. Duties depend on the risk of the AI system. | [AI governance](playbook/ai/ai-governance.md) |
| API (application programming interface) | The defined way one program asks another for data or actions. | [API standards](playbook/architecture/api-standards.md) |
| Assured | The highest of the playbook's three levels: Standard plus the evidence, separation of duties and audit trail that regulators ask for. | [Maturity model](playbook/measurement/maturity-model.md) |
| ASVS (Application Security Verification Standard) | OWASP's list of security requirements at three levels, used to decide what to test for each service. | [Security testing](playbook/quality/security-testing.md) |

## B

| Term | Meaning | Read more |
|---|---|---|
| B2B (business to business) | A product sold to organisations, where the buyer, the daily users and the administrator are often different people. | [Product discovery](playbook/product/product-discovery.md#b2b-and-enterprise-discovery) |
| Blameless postmortem | A written review after an incident that asks how the system let the failure happen, not who to blame. | [Postmortems](playbook/reliability/postmortems.md) |
| Brooks's law | Fred Brooks's observation (1975) that adding people to a late software project makes it later. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#when-the-project-is-late) |
| Burn rate | How fast a service is using up its error budget. A burn rate of 1 uses the whole budget in exactly the SLO period. | [Service levels](playbook/reliability/service-levels.md) |
| Burn-up chart | A chart of work accepted over time with the total scope drawn as a second line, so progress and scope growth show together. | [Status reporting](playbook/project-management/status-reporting.md#measure-from-systems-not-opinion) |
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
| Cone of uncertainty | The wide range of likely outcomes around an early estimate, which narrows only as decisions remove uncertainty. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#why-single-number-estimates-fail) |
| Contingency | Money and time held for the risks in the RAID log and the uncertainty in an estimate, released against a named item. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#contingency-and-management-reserve) |
| Contract test | A test that checks two services agree on the requests and responses between them, so each side can change without a full end-to-end run. | [Test automation](playbook/quality/test-automation.md) |
| Controlled experiment | See A/B test. |  |
| Coordinated omission | A load test error in which the tool sends less load when the system slows down, so the slowest responses are never measured. | [Performance testing](playbook/quality/performance-testing.md) |
| CRA (Cyber Resilience Act) | The EU's Regulation (EU) 2024/2847 on security of products with digital elements, including a duty to report actively exploited vulnerabilities. | [Regulated industries](playbook/compliance/regulated-industries.md) |
| CUPED | Controlled experiments using pre-experiment data: adjusting each user's result for the same metric measured before the test, so fewer users are needed. | [Product metrics and experiments](playbook/product/product-metrics-and-experiments.md#sample-size) |
| Cutover | The hours or days in which the old system stops and the new one starts, run from a timed and rehearsed runbook. | [Risks, RAID logs and stage gates](playbook/project-management/risks-raid-and-stage-gates.md#cutover-and-rollback) |
| CVE | A public identifier for one known vulnerability, for example CVE-2021-44228. | [Vulnerability management](playbook/security/vulnerability-management.md) |
| CVSS (Common Vulnerability Scoring System) | A score from 0 to 10 for how severe a vulnerability is. It does not say how likely it is to be exploited. | [Vulnerability management](playbook/security/vulnerability-management.md) |
| Cynefin | A framework that sorts situations into clear, complicated, complex and chaotic, each needing a different way to decide. | [Decision making](leaders/decision-making.md) |

## D

| Term | Meaning | Read more |
|---|---|---|
| DAST (dynamic application security testing) | Scanning a running application from the outside for vulnerabilities, for example with ZAP. | [Security testing](playbook/quality/security-testing.md) |
| Data contract | An agreement between the team that produces data and the teams that use it: schema, meaning, quality and notice of changes. | [Data quality](playbook/data/data-quality.md) |
| Deal desk | The group in a company that sells to organisations which approves non-standard deal terms, such as deep discounts or promised features. | [Roadmaps and prioritisation](playbook/product/roadmaps-and-prioritisation.md#b2b-and-enterprise-roadmaps) |
| Decision record | See ADR. | |
| Delivery confidence | A judgement (high, medium or low) of how likely a project is to deliver its outcome, reported next to its status colours. | [Status reporting](playbook/project-management/status-reporting.md#define-red-amber-and-green-by-rule) |
| Discovery, alpha, beta, live | The phases of a digital service in the GOV.UK Service Manual: understand the problem, try options with prototypes, run with real users, then run and improve. | [Projects and products](playbook/project-management/projects-and-products.md#choose-a-life-cycle-per-part-of-the-work) |
| DKIM, DMARC, SPF | Email settings published in your domain's DNS that let other mail servers check that mail claiming to come from you is genuine. | [For small and medium businesses](leaders/for-small-and-medium-businesses.md) |
| DNS | The internet's address book: it turns names such as example.org into network addresses. | |
| DORA (EU regulation) | The EU's Digital Operational Resilience Act, Regulation (EU) 2022/2554, for banks, insurers and other financial firms. Not the same as DORA metrics. | [Regulated industries](playbook/compliance/regulated-industries.md) |
| DORA metrics | Five software delivery measures from the DevOps Research and Assessment programme: deployment frequency, change lead time, change fail rate, failed deployment recovery time and rework rate. Not the same as EU DORA. | [Metrics](playbook/measurement/metrics.md) |
| DPI (digital public infrastructure) | Shared national platforms, such as digital identity, payments and data exchange, that many public and private services build on. | [For government](leaders/for-government.md) |
| DPIA (data protection impact assessment) | A written check of the risks to people before high-risk processing of personal data. Required by GDPR Article 35. | [Data security and privacy](playbook/data/data-security-and-privacy.md) |
| DPO | Data protection officer. | [Data security and privacy](playbook/data/data-security-and-privacy.md) |
| Dual-track | Discovery and delivery done by the same team in the same weeks, so evidence reaches the backlog continuously. | [Product discovery](playbook/product/product-discovery.md#standard) |

## E

| Term | Meaning | Read more |
|---|---|---|
| ECDH, RSA | Public-key cryptography in wide use today. A large enough quantum computer could break both, so they are being replaced. | [Post-quantum readiness](playbook/security/post-quantum-readiness.md) |
| Eval (evaluation set) | A fixed set of inputs and expected outputs used to measure whether an AI feature meets its quality bar. Run before and after every change. | [Building with AI](playbook/ai/building-with-ai.md) |
| Eval-driven development | Building AI features by writing the evaluation set and its pass threshold first, then iterating on prompts, models or retrieval until the set passes. | [Building with AI](playbook/ai/building-with-ai.md) |
| EPSS (Exploit Prediction Scoring System) | An estimate of the probability that a vulnerability will be exploited in the next 30 days. | [Vulnerability management](playbook/security/vulnerability-management.md) |
| Error budget | The amount of unreliability an SLO allows in a period. A 99.9% monthly target allows about 43 minutes of failure a month. | [Service levels](playbook/reliability/service-levels.md) |
| EVM (earned value management) | A method, standardised in SAE EIA-748, that compares the budgeted value of accepted work with its actual cost and its plan. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#earned-value-without-fiction) |
| Exploratory testing | Designing and running tests at the same time, in a time-boxed session guided by a charter that states the mission. | [Exploratory and acceptance testing](playbook/quality/exploratory-and-acceptance-testing.md#charters-and-sessions) |

## F

| Term | Meaning | Read more |
|---|---|---|
| Failure demand | Contact caused by failing to do something, or to do it right, for the user, such as a call to ask where an application is. | [Product discovery](playbook/product/product-discovery.md#assured) |
| Feature flag | A setting that turns a feature on or off without a new deployment. | [Feature flags](playbook/delivery/feature-flags.md) |
| FinOps | Managing cloud cost as a shared engineering and finance practice. | [FinOps](playbook/platform/finops.md) |
| FIPS 203, 204, 205 | The US NIST standards for post-quantum algorithms: ML-KEM, ML-DSA and SLH-DSA. | [Post-quantum readiness](playbook/security/post-quantum-readiness.md) |
| Flaky test | A test that passes and fails on the same code; the playbook quarantines it within 24 hours and fixes or deletes it within 14 days. | [Test automation](playbook/quality/test-automation.md) |
| Foundation | The first of the playbook's three levels: the minimum that pays for itself at once. | [Maturity model](playbook/measurement/maturity-model.md) |

## G

| Term | Meaning | Read more |
|---|---|---|
| GDPR | The EU General Data Protection Regulation, Regulation (EU) 2016/679. The UK has its own version, UK GDPR. | [Data security and privacy](playbook/data/data-security-and-privacy.md) |
| GitOps | Keeping the desired state of a system in Git and letting an agent apply it, so every change is a reviewed commit. | [GitOps and deployment](playbook/delivery/gitops-and-deployment.md) |
| Golden path | The supported, documented way to build and run a common kind of service, made the easiest choice. Some pages and companies say "paved road". | [Golden paths](playbook/platform/golden-paths.md) |
| Go/no-go | The decision, against criteria agreed weeks in advance, on whether a release or cutover goes ahead. | [Risks, RAID logs and stage gates](playbook/project-management/risks-raid-and-stage-gates.md#gono-go-before-go-live) |
| Guardrail metric | A metric that must not get worse while a team chases its main outcome, with a written margin for the largest harm it would accept. | [Product metrics and experiments](playbook/product/product-metrics-and-experiments.md#experiment-design) |

## H

| Term | Meaning | Read more |
|---|---|---|
| HEART | Google's framework for user experience metrics: happiness, engagement, adoption, retention and task success. | [Product metrics and experiments](playbook/product/product-metrics-and-experiments.md#choosing-what-to-measure) |
| HSM (hardware security module) | A tamper-resistant device that stores keys and performs cryptography without exposing the keys. | [Secrets](playbook/security/secrets.md) |
| Hypercare | A set period after go-live when the project team and supplier stay on call with daily checks, ending on written exit criteria. | [Risks, RAID logs and stage gates](playbook/project-management/risks-raid-and-stage-gates.md#cutover-and-rollback) |

## I

| Term | Meaning | Read more |
|---|---|---|
| IaC (infrastructure as code) | Defining servers, networks and cloud services in version-controlled files instead of clicking in consoles. | [Infrastructure as code](playbook/delivery/infrastructure-as-code.md) |
| IC (incident commander) | The one person who leads the response to an incident and makes the calls. | [Incident management](playbook/reliability/incident-management.md) |
| ICT | Information and communication technology. | |
| Intelligent client | A small expert team kept by the buyer, often a product manager, an architect and a test lead, to check a supplier's claims against evidence. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#fixed-price-contracts-and-systems-integrators) |
| ISO/IEC 27001 | The international standard for an information security management system. Annex A lists its controls. | [Control mapping](playbook/compliance/control-mapping.md) |
| ISO/IEC 42001 | The international standard for an AI management system. | [AI governance](playbook/ai/ai-governance.md) |
| ITIL | A widely used framework for IT service management. | [IT governance](playbook/operating-model/it-governance.md) |

## J

| Term | Meaning | Read more |
|---|---|---|
| Jobs to be done | Describing the progress people are trying to make in a situation, which they "hire" a product for, rather than the features they ask for. | [Product strategy](playbook/product/product-strategy.md#what-a-product-strategy-contains) |

## K

| Term | Meaning | Read more |
|---|---|---|
| Kano model | A survey method that sorts features into must-be, one-dimensional, attractive and indifferent by how they change satisfaction. | [Roadmaps and prioritisation](playbook/product/roadmaps-and-prioritisation.md#choosing-a-prioritisation-method) |
| Kata | A short exercise repeated to build a skill, for example reviewing a pull request. | [Exercises](exercises/README.md) |
| KEV (Known Exploited Vulnerabilities) | CISA's catalogue of vulnerabilities that attackers are known to be using. Fix these first. | [Vulnerability management](playbook/security/vulnerability-management.md) |
| KMS (key management service) | A service, often from a cloud provider, that creates, stores and controls the use of encryption keys. | [Secrets](playbook/security/secrets.md) |

## L

| Term | Meaning | Read more |
|---|---|---|
| Launch tier | The playbook's size class for a launch (1, 2 or 3), which sets the rollout and sign-off it needs; not the same as service Tier 1, 2 or 3. | [Launch and adoption](playbook/product/launch-and-adoption.md#launch-tiers) |
| LGTM | "Looks good to me": a quick approval in code review, often given without a careful read. | [Code review](playbook/delivery/code-review.md) |
| LLM (large language model) | The kind of AI model behind chat assistants and code assistants. | [Building with AI](playbook/ai/building-with-ai.md) |

## M

| Term | Meaning | Read more |
|---|---|---|
| Management reserve | Money held by the sponsor or the portfolio for work nobody foresaw, released only at a gate or an exception. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#contingency-and-management-reserve) |
| MCP (Model Context Protocol) | An open protocol for connecting AI assistants and agents to tools and data sources. | [AI architecture patterns](playbook/ai/ai-architecture-patterns.md) |
| MFA (multi-factor authentication) | Signing in with something more than a password, such as a code from a phone app or a security key. "Phishing-resistant" MFA (security keys, passkeys) cannot be tricked into working on a fake site. | [Access control](playbook/security/access-control.md) |
| Minimum detectable effect | The smallest change in a metric that an experiment is sized to detect, set at the change that would pay for building and owning the feature. | [Product metrics and experiments](playbook/product/product-metrics-and-experiments.md#experiment-design) |
| ML-KEM | The NIST post-quantum algorithm for agreeing a shared key (FIPS 203). | [Post-quantum readiness](playbook/security/post-quantum-readiness.md) |
| Monte Carlo forecast | A forecast made by replaying past throughput thousands of times at random, giving a date range with a stated confidence such as 85%. | [Planning and forecasting](playbook/ways-of-working/planning-and-forecasting.md) |
| MoSCoW | Sorting requirements into Must have, Should have, Could have and Won't have this time (from DSDM), so a fixed date or budget can flex on scope. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#fix-the-date-and-cost-manage-the-scope-moscow) |
| Mutation testing | Changing the code on purpose and checking that some test fails, to find tests that run code without really checking it. | [Test automation](playbook/quality/test-automation.md) |

## N

| Term | Meaning | Read more |
|---|---|---|
| NCSC | The UK's National Cyber Security Centre. | [For small and medium businesses](leaders/for-small-and-medium-businesses.md) |
| Net revenue retention | Revenue kept from existing customers over 12 months, counting expansion as well as losses, as a share of where it started. | [Product metrics and experiments](playbook/product/product-metrics-and-experiments.md#choosing-what-to-measure) |
| NIS2 | The EU's Directive (EU) 2022/2555 on cyber security for essential and important entities. | [Regulated industries](playbook/compliance/regulated-industries.md) |
| NIST | The US National Institute of Standards and Technology. It publishes the SSDF, the Cybersecurity Framework and the post-quantum standards. | |

## O

| Term | Meaning | Read more |
|---|---|---|
| OKR (objectives and key results) | A goal-setting method: a qualitative objective with a few measurable results. | [Strategy toolkit](leaders/strategy-toolkit.md) |
| On-call | Being the person who responds when a service pages outside or during working hours, on a rotation. | [On-call](playbook/reliability/on-call.md) |
| Opportunity solution tree | Teresa Torres's map that links a team's outcome to the opportunities found in research, the possible solutions and the tests of their assumptions. | [Product discovery](playbook/product/product-discovery.md#standard) |
| OWASP | The Open Worldwide Application Security Project. It publishes the Top 10 lists of web and LLM application risks. | [AI application security](playbook/ai/ai-application-security.md) |

## P

| Term | Meaning | Read more |
|---|---|---|
| p95, p99 | The 95th or 99th percentile: 95% or 99% of requests were faster than this. | [Service levels](playbook/reliability/service-levels.md) |
| PaaS, SaaS | Platform as a service (you deploy code, the provider runs the servers) and software as a service (you use a finished application online). | [Cloud native](playbook/platform/cloud-native.md) |
| Paved road | See golden path. | |
| Planning fallacy | The habit, described by Kahneman and Tversky, of forecasting from the plan in front of you and ignoring how similar work actually went. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#why-single-number-estimates-fail) |
| PMBOK Guide, PRINCE2 | Two widely used project management methods: the PMBOK Guide from the Project Management Institute and PRINCE2 from the UK. | [Projects and products](playbook/project-management/projects-and-products.md#choose-a-life-cycle-per-part-of-the-work) |
| PMO (project management office) | A team that keeps portfolio data, forecasting methods, the gate calendar and assurance for projects across an organisation. | [A modern PMO](playbook/project-management/modern-pmo.md) |
| Point of no return | The step in a cutover after which going back costs more than fixing forward. | [Risks, RAID logs and stage gates](playbook/project-management/risks-raid-and-stage-gates.md#cutover-and-rollback) |
| PQC (post-quantum cryptography) | Cryptography designed to stay secure against a large quantum computer. | [Post-quantum readiness](playbook/security/post-quantum-readiness.md) |
| Product operations | A small function that runs the shared machinery product teams depend on, such as data, research operations and launch calendars. | [For product leaders](leaders/for-product-leaders.md#product-operations) |
| Product trio | The product manager, designer and tech lead who run discovery together for one team. | [Product discovery](playbook/product/product-discovery.md) |
| Profile | The playbook's adoption path for one size of organisation: SME, solo, startup, scale-up or enterprise, plus public sector and regulated overlays. | [Profiles](profiles/README.md) |
| Programme | A temporary group of related projects and business change, run together to reach benefits no single project delivers. | [Projects and products](playbook/project-management/projects-and-products.md#project-or-product-decide-first) |
| Property-based testing | Tests that state a rule and check it against many generated inputs, for example with QuickCheck or Hypothesis. | [Test automation](playbook/quality/test-automation.md) |
| PRR (production readiness review) | A checklist review before a service takes real traffic. | [Production readiness](playbook/reliability/production-readiness.md) |

## R

| Term | Meaning | Read more |
|---|---|---|
| RACI | Responsible, accountable, consulted, informed: a table of who does what for each decision. | [Decision rights](playbook/operating-model/decision-rights.md) |
| RAG (retrieval-augmented generation) | Giving an AI model relevant documents at question time so it answers from them, not only from its training. | [AI architecture patterns](playbook/ai/ai-architecture-patterns.md) |
| RAID log | A project's working list of risks, assumptions, issues and dependencies, each with an owner, a next action and a date. | [Risks, RAID logs and stage gates](playbook/project-management/risks-raid-and-stage-gates.md#the-raid-log) |
| RCA (root cause analysis) | Finding why an incident happened. The playbook looks for several contributing factors, not one root cause. | [Root cause analysis](playbook/reliability/root-cause-analysis.md) |
| Reference class forecasting | Estimating from the actual results of similar past projects, then adjusting the plan's own estimate by how far those projects overran. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#estimate-with-ranges-and-reference-classes) |
| RFC (request for comments) | A written proposal for a significant change, shared for comment for a fixed period before a decision. | [RFCs](playbook/architecture/rfcs.md) |
| RICE | A scoring method from Intercom: reach times impact times confidence, divided by effort. | [Roadmaps and prioritisation](playbook/product/roadmaps-and-prioritisation.md#choosing-a-prioritisation-method) |
| RPO (recovery point objective) | The most data you can afford to lose, measured in time. An RPO of 1 hour means backups or replicas no more than 1 hour old. | [Backup and recovery](playbook/reliability/backup-and-recovery.md) |
| RTO (recovery time objective) | How long a service may be down before it must be back. | [Backup and recovery](playbook/reliability/backup-and-recovery.md) |
| Runbook | Step-by-step instructions for handling one alert or operational task. | [Runbook template](templates/docs/runbook.md) |

## S

| Term | Meaning | Read more |
|---|---|---|
| Sample ratio mismatch | A split of users between variants that did not come out as planned, which means assignment or logging is broken and the result cannot be trusted. | [Product metrics and experiments](playbook/product/product-metrics-and-experiments.md#reading-results-honestly) |
| SAST (static application security testing) | Scanning source code for security flaws without running it. | [Security testing](playbook/quality/security-testing.md) |
| SBOM (software bill of materials) | A list of every component and version inside a piece of software. | [Supply chain](playbook/security/supply-chain.md) |
| SCA (software composition analysis) | Scanning the open source components a product uses for known vulnerabilities and licences. | [Security testing](playbook/quality/security-testing.md) |
| Senior responsible owner (SRO) | The one person accountable for a programme meeting its objectives and realising its benefits. | [Projects and products](playbook/project-management/projects-and-products.md#project-or-product-decide-first) |
| SEV1, SEV2, SEV3 | Incident severity levels. SEV1 is the most serious. | [Incident management](playbook/reliability/incident-management.md) |
| SI (systems integrator) | A supplier that builds and joins systems for you, often under a fixed-price contract. | [Planning fixed scope and budget](playbook/project-management/planning-fixed-scope-and-budget.md#fixed-price-contracts-and-systems-integrators) |
| SLA (service level agreement) | A promise to a customer about reliability, usually with a penalty if missed. Set it looser than the internal SLO. | [Service levels](playbook/reliability/service-levels.md) |
| SLI (service level indicator) | A measure of what users experience, for example the share of requests that succeed in under 300 ms. | [Service levels](playbook/reliability/service-levels.md) |
| SLO (service level objective) | A target for an SLI over a period, for example 99.9% of requests succeed each month. | [Service levels](playbook/reliability/service-levels.md) |
| SLSA (Supply-chain Levels for Software Artifacts) | A framework of levels for proving how software was built and that nobody tampered with it. | [Supply chain](playbook/security/supply-chain.md) |
| SME | Small or medium business. In the playbook, one that uses software but does not build it. | [SME profile](profiles/sme.md) |
| Soak test | A load test held for hours at normal to peak load to find problems that build up over time, such as memory leaks. | [Performance testing](playbook/quality/performance-testing.md) |
| SOC 2 | An audit report on a service provider's controls, against the AICPA Trust Services Criteria. | [Control mapping](playbook/compliance/control-mapping.md) |
| SPACE | A framework for developer productivity: satisfaction and well-being, performance, activity, communication and collaboration, efficiency and flow. | [Metrics](playbook/measurement/metrics.md) |
| Sponsor | The one person accountable for a project's outcome and money, who chairs the steering group and decides at each gate. | [Status reporting](playbook/project-management/status-reporting.md#steering-groups-that-decide) |
| SRE (site reliability engineering) | Running services with software engineering methods: SLOs, error budgets, automation and blameless learning. | [Service levels](playbook/reliability/service-levels.md) |
| SSDF (Secure Software Development Framework) | NIST SP 800-218, a set of secure development practices. | [Secure development](playbook/security/secure-development.md) |
| SSO (single sign-on) | One company login for many services, so access can be removed in one place. | [Access control](playbook/security/access-control.md) |
| Stage gate | A decision point between stages of a project where the sponsor chooses to continue, continue with conditions, rescope, pause or stop. | [Risks, RAID logs and stage gates](playbook/project-management/risks-raid-and-stage-gates.md#stage-gates-that-can-stop-work) |
| Standard | The middle of the playbook's three levels: shared practice across several teams, measured. | [Maturity model](playbook/measurement/maturity-model.md) |
| Steering group | Three to six people, chaired by the sponsor, who make the decisions a project manager cannot. | [Status reporting](playbook/project-management/status-reporting.md#steering-groups-that-decide) |
| Strangler fig | Replacing a legacy system piece by piece, routing one function at a time to the new system. | [Legacy modernisation](playbook/architecture/legacy-modernisation.md) |
| STRIDE | A threat modelling checklist: spoofing, tampering, repudiation, information disclosure, denial of service, elevation of privilege. | [Secure development](playbook/security/secure-development.md) |
| Synthetic data | Test data generated by code, with no link to real people. | [Test data and environments](playbook/quality/test-data-and-environments.md) |

## T

| Term | Meaning | Read more |
|---|---|---|
| Tabletop exercise | A team talks through a realistic incident scenario, step by step, without touching real systems. | [Exercises](exercises/README.md) |
| TDD (test-driven development) | Writing a failing test first, then the code that makes it pass, then tidying up. | [Test-driven development](playbook/quality/test-driven-development.md) |
| Tech radar | A list of tools and techniques rated adopt, trial, assess or hold. | [Tech radar](playbook/architecture/tech-radar.md) |
| Test pyramid | Mike Cohn's guide to the mix of tests: many fast unit tests, fewer integration tests and a few end-to-end tests. | [Testing](playbook/delivery/testing.md#pyramid-or-trophy) |
| Tier 1, Tier 2, Tier 3 | Service classes by business impact. Tier 1 services are the ones the business cannot run without and get the strictest targets. | [Production readiness](playbook/reliability/production-readiness.md) |
| TIME model | Sorting each application into Tolerate, Invest, Migrate or Eliminate. | [Strategy toolkit](leaders/strategy-toolkit.md) |
| Toil | Manual, repetitive operational work that grows with the service and could be automated. | [Business case](playbook/strategy/business-case.md) |
| Tolerance | The limits of date, cost and scope within which a project manager may act without asking the steering group. | [Status reporting](playbook/project-management/status-reporting.md#define-red-amber-and-green-by-rule) |
| Two-way door | A decision you can reverse cheaply, so decide it fast. A one-way door is hard to reverse and needs more care. | [Decision making](leaders/decision-making.md) |

## U

| Term | Meaning | Read more |
|---|---|---|
| UAT (user acceptance testing) | A check by real users, with their own data and procedures, that a service does their job, ending in a signed decision. | [Exploratory and acceptance testing](playbook/quality/exploratory-and-acceptance-testing.md) |

## V

| Term | Meaning | Read more |
|---|---|---|
| Value metric | The unit a customer pays for, such as a seat, a location or a transaction. | [Pricing and packaging](playbook/product/pricing-and-packaging.md#the-five-decisions) |
| Vanity metric | A number that rises whatever happens to users, such as total registered users or page views. | [Product metrics and experiments](playbook/product/product-metrics-and-experiments.md#choosing-what-to-measure) |
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
