# The playbook

Fourteen areas, about ninety pages. Each page follows the same layout: the decision up front, measurable outcomes, the practice at three levels (Foundation, Standard, Assured), what changes on-premises and air-gapped, common failures, templates and primary sources.

Start with [principles.md](principles.md). Then pick your [profile](../profiles/README.md), which tells you which pages to read first and at which level. If you arrived with a specific problem, [PROBLEMS.md](../PROBLEMS.md) takes you straight to the right page.

## 1. Strategy

How to decide where engineering is going and how to get there without stopping the business.

| Page | Read it when |
|---|---|
| [Technical strategy](strategy/technical-strategy.md) | You need a strategy people act on, not a slide deck |
| [Transition playbook](strategy/transition-playbook.md) | You are moving to a new way of building or running software |
| [Business case](strategy/business-case.md) | You need finance or a board to fund engineering work |
| [Build, buy or adopt](strategy/build-buy-adopt.md) | You are choosing a platform, product or open source project |
| [Stakeholders and communication](strategy/stakeholders-and-communication.md) | A change affects people outside engineering |
| [Horizon scan](strategy/horizon-scan.md) | You want to know what to prepare for between now and 2030 |
| [Portfolio and capacity](strategy/portfolio-and-capacity.md) | You plan budgets and capacity across many teams |

## 2. Operating model

| Page | Read it when |
|---|---|
| [Team topology](operating-model/team-topology.md) | You are designing or reorganising teams |
| [Decision rights](operating-model/decision-rights.md) | Nobody knows who can say yes |
| [Roles](operating-model/roles.md) | You want to know what each role owns and reads first |
| [Engineering governance](operating-model/engineering-governance.md) | You need standards without a bottleneck |
| [IT governance](operating-model/it-governance.md) | The board and auditors need to see that IT is under control |

## 3. Ways of working

| Page | Read it when |
|---|---|
| [Agile and Scrum](ways-of-working/agile-and-scrum.md) | The ceremonies run but nothing improves |
| [Planning and forecasting](ways-of-working/planning-and-forecasting.md) | Estimates are always wrong |
| [Product partnership](ways-of-working/product-partnership.md) | Product and engineering pull in different directions |

## 4. Delivery

| Page | Read it when |
|---|---|
| [Source control](delivery/source-control.md) | Setting up branching and repository rules |
| [Code review](delivery/code-review.md) | Reviews are slow, shallow or painful |
| [Testing](delivery/testing.md) | Tests are slow, flaky or missing |
| [Continuous integration](delivery/continuous-integration.md) | CI takes too long or breaks often |
| [Release management](delivery/release-management.md) | Releases are risky, manual or rare |
| [Versioning and changelogs](delivery/versioning-and-changelogs.md) | Users cannot tell what changed |
| [Feature flags](delivery/feature-flags.md) | You want to separate deploy from release |
| [Environments](delivery/environments.md) | Staging lies to you |
| [Database changes](delivery/database-changes.md) | Migrations cause downtime |
| [GitOps and deployment](delivery/gitops-and-deployment.md) | Deployments are manual or a change reached everyone at once |
| [Infrastructure as code](delivery/infrastructure-as-code.md) | Nobody could rebuild production from scratch |

## 5. Quality

| Page | Read it when |
|---|---|
| [Quality engineering](quality/quality-engineering.md) | QA is a phase at the end and a bottleneck |
| [Test-driven development](quality/test-driven-development.md) | You want design feedback from tests, not only coverage |

## 6. Reliability

| Page | Read it when |
|---|---|
| [Service levels](reliability/service-levels.md) | You cannot say how reliable is reliable enough |
| [Incident management](reliability/incident-management.md) | Incidents are chaotic |
| [Postmortems](reliability/postmortems.md) | The same incidents keep happening |
| [Root cause analysis](reliability/root-cause-analysis.md) | Your RCAs stop at one cause and nothing changes |
| [Rollbacks](reliability/rollbacks.md) | Undoing a bad change takes too long |
| [On-call](reliability/on-call.md) | People are tired of being paged |
| [Production readiness](reliability/production-readiness.md) | A new service is about to go live |
| [Backup and recovery](reliability/backup-and-recovery.md) | You have never tested a restore |
| [Change management](reliability/change-management.md) | A change board slows everything down |

## 7. Security

| Page | Read it when |
|---|---|
| [Secure development](security/secure-development.md) | You need a secure development lifecycle |
| [Supply chain](security/supply-chain.md) | You need to prove where your software came from |
| [Secrets](security/secrets.md) | Credentials live in code or chat |
| [Dependencies](security/dependencies.md) | Updates pile up |
| [Vulnerability management](security/vulnerability-management.md) | You have more findings than time |
| [Access control](security/access-control.md) | Too many people can reach production |
| [Zero trust](security/zero-trust.md) | The network perimeter is your main control |
| [Post-quantum readiness](security/post-quantum-readiness.md) | You need a plan before RSA and elliptic curves are deprecated |
| [Third-party and SaaS risk](security/third-party-and-saas-risk.md) | A supplier's breach could become yours |

## 8. Data

| Page | Read it when |
|---|---|
| [Data governance](data/data-governance.md) | Nobody owns the data and reports disagree |
| [Data quality](data/data-quality.md) | Upstream changes break pipelines silently |
| [Data security and privacy](data/data-security-and-privacy.md) | You cannot say where personal data lives |

## 9. AI

| Page | Read it when |
|---|---|
| [AI governance](ai/ai-governance.md) | You need rules for AI use that satisfy regulators and still let teams build |
| [Building with AI](ai/building-with-ai.md) | Pilots do not reach production |
| [AI application security](ai/ai-application-security.md) | You ship features built on language models or agents |

## 10. Architecture

| Page | Read it when |
|---|---|
| [Decision records](architecture/decision-records.md) | Nobody remembers why |
| [Architecture practice](architecture/architecture-practice.md) | You need architects who enable teams instead of blocking them |
| [RFCs](architecture/rfcs.md) | A change is big enough to need wider input |
| [Tech radar](architecture/tech-radar.md) | Teams keep picking different tools for the same job |
| [API standards](architecture/api-standards.md) | Every API looks different |
| [Observability](architecture/observability.md) | You find out about problems from users |
| [Scaling](architecture/scaling.md) | The system struggles under load |
| [Legacy modernisation](architecture/legacy-modernisation.md) | A critical old system cannot be changed safely |
| [Technical debt](architecture/technical-debt.md) | Debt slows every change |

## 11. Platform

| Page | Read it when |
|---|---|
| [Golden paths](platform/golden-paths.md) | Starting a new service takes weeks |
| [Developer platform](platform/developer-platform.md) | You are thinking about a platform team |
| [Cloud native](platform/cloud-native.md) | You are choosing between containers, Kubernetes, PaaS and serverless |
| [Cloud, on-premises and air-gapped](platform/cloud-on-prem-air-gapped.md) | You run in more than one kind of environment |
| [FinOps](platform/finops.md) | The cloud bill grows faster than usage |
| [Green software](platform/green-software.md) | You need to measure and cut the carbon cost of your systems |

## 12. People

| Page | Read it when |
|---|---|
| [Onboarding](people/onboarding.md) | New engineers take months to ship |
| [Documentation](people/documentation.md) | Docs are missing or out of date |
| [Code assistants](people/code-assistants.md) | You need a policy for code assistants |
| [Knowledge sharing](people/knowledge-sharing.md) | Knowledge sits with a few people |
| [Hiring](people/hiring.md) | Interviews do not predict who will do well |
| [Career framework](people/career-framework.md) | Good engineers leave because they cannot see how to grow |
| [Sustainable pace](people/sustainable-pace.md) | The team is tired |
| [Skills gap](people/skills-gap.md) | You lack people with Kubernetes, cloud, security or AI skills |

## 13. Measurement

| Page | Read it when |
|---|---|
| [Metrics](measurement/metrics.md) | You want to know if things are getting better |
| [Maturity model](measurement/maturity-model.md) | You want to see where you stand across all areas |

## 14. Compliance

| Page | Read it when |
|---|---|
| [Control mapping](compliance/control-mapping.md) | An auditor asks for evidence |
| [Public sector](compliance/public-sector.md) | You work for or sell to government |
| [Regulated industries](compliance/regulated-industries.md) | You are a bank, insurer, health or telecom provider |
