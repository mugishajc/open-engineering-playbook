# Start from your problem

Most playbooks are organised by practice. People arrive with a problem. Find yours below and go straight to the pages that address it. Playbook pages give the practice at three levels, with measurable outcomes and templates. Leaders pages give decision makers agendas, checklists and decision rules.

If your problem is not here, [open an issue](https://github.com/mugishajc/open-engineering-playbook/issues/new). The list grows from what adopters report.

## Code assistants and AI

| Problem | Go to |
|---|---|
| Engineers use code assistants and nobody knows what code or data leaves the company | [Code assistants](playbook/people/code-assistants.md), [policy template](templates/docs/code-assistant-policy.md) |
| We ship faster since adopting code assistants, but production breaks more often | [Metrics: rework rate and change fail rate](playbook/measurement/metrics.md), [code review](playbook/delivery/code-review.md) |
| Our AI pilots never reach production | [Building with AI](playbook/ai/building-with-ai.md), [AI use case assessment](templates/docs/ai-use-case-assessment.md) |
| We do not know if the EU AI Act applies to us, or by when | [AI governance](playbook/ai/ai-governance.md) |
| Someone made our chatbot reveal internal data | [AI application security](playbook/ai/ai-application-security.md) |
| An agent can call tools and we cannot say what it is allowed to do | [AI application security](playbook/ai/ai-application-security.md), [access control](playbook/security/access-control.md) |
| Junior engineers are losing core skills | [Code assistants](playbook/people/code-assistants.md), [onboarding](playbook/people/onboarding.md), [career framework](playbook/people/career-framework.md) |
| The board asks for an AI strategy and all we have is a list of pilots | [Leading in the AI era](leaders/leading-in-the-ai-era.md), [AI governance](playbook/ai/ai-governance.md) |
| Coding agents open pull requests faster than anyone can review them | [AI engineering practices](playbook/ai/ai-engineering-practices.md), [code review](playbook/delivery/code-review.md) |
| A coding agent runs with an engineer's personal token and could merge its own changes | [AI engineering practices: coding agents in the repository](playbook/ai/ai-engineering-practices.md#coding-agents-in-the-repository), [source control](playbook/delivery/source-control.md) |
| Every team calls model providers directly and nobody can see the cost or where the data went | [AI architecture patterns: model gateway](playbook/ai/ai-architecture-patterns.md#model-gateway) |
| We are told to cut headcount because of AI, but cannot show any measured gain | [Leading in the AI era: measuring impact](leaders/leading-in-the-ai-era.md#measuring-impact-with-data-not-anecdotes) |

## Security

| Problem | Go to |
|---|---|
| We could not answer "are we affected?" when a big vulnerability was announced | [Supply chain: SBOMs](playbook/security/supply-chain.md), [dependencies](playbook/security/dependencies.md) |
| We have thousands of scanner findings and no idea which matter | [Vulnerability management](playbook/security/vulnerability-management.md) |
| Secrets end up in Git, chat and CI logs | [Secrets](playbook/security/secrets.md) |
| Too many people can reach production | [Access control](playbook/security/access-control.md), [zero trust](playbook/security/zero-trust.md) |
| Our VPN is the only thing between attackers and everything | [Zero trust](playbook/security/zero-trust.md) |
| A supplier breach became our breach | [Third-party and SaaS risk](playbook/security/third-party-and-saas-risk.md), [vendor questionnaire](templates/docs/vendor-risk-questionnaire.md) |
| We do not know which systems use RSA or elliptic-curve cryptography | [Post-quantum readiness](playbook/security/post-quantum-readiness.md), [crypto inventory](templates/docs/crypto-inventory.csv) |
| We sell software in the EU and the Cyber Resilience Act reporting clock already applies | [Vulnerability management](playbook/security/vulnerability-management.md), [incident management](playbook/reliability/incident-management.md) |
| A ransomware attack would take us down for weeks | [Backup and recovery](playbook/reliability/backup-and-recovery.md) |

## Data

| Problem | Go to |
|---|---|
| Nobody owns our data and every report gives a different number | [Data governance](playbook/data/data-governance.md), [data quality](playbook/data/data-quality.md) |
| We do not know where personal data lives | [Data security and privacy](playbook/data/data-security-and-privacy.md), [data classification](templates/docs/data-classification.md) |
| Upstream changes break our pipelines without warning | [Data quality: data contracts](playbook/data/data-quality.md) |
| We must keep citizen or customer data inside the country | [Public sector](playbook/compliance/public-sector.md), [cloud, on-premises and air-gapped](playbook/platform/cloud-on-prem-air-gapped.md) |

## Delivery and quality

| Problem | Go to |
|---|---|
| Pull requests wait days for review | [Code review](playbook/delivery/code-review.md) |
| Releases are rare, manual and scary | [Release management](playbook/delivery/release-management.md), [GitOps and deployment](playbook/delivery/gitops-and-deployment.md) |
| CI takes 40 minutes and fails at random | [Continuous integration](playbook/delivery/continuous-integration.md), [testing](playbook/delivery/testing.md) |
| QA is a phase at the end and a bottleneck | [Quality engineering](playbook/quality/quality-engineering.md) |
| We want TDD but the team does not believe in it | [Test-driven development](playbook/quality/test-driven-development.md) |
| A configuration change took down production everywhere at once | [GitOps and deployment: staged rollouts](playbook/delivery/gitops-and-deployment.md), [feature flags](playbook/delivery/feature-flags.md) |
| Database migrations mean downtime | [Database changes](playbook/delivery/database-changes.md) |
| Infrastructure is clicked together in a console and nobody can rebuild it | [Infrastructure as code](playbook/delivery/infrastructure-as-code.md) |
| Users cannot tell what changed between versions | [Versioning and changelogs](playbook/delivery/versioning-and-changelogs.md) |

## Architecture, scale and reliability

| Problem | Go to |
|---|---|
| The system falls over at peak load | [Scaling](playbook/architecture/scaling.md), [service levels](playbook/reliability/service-levels.md) |
| We split into microservices and now everything is slower and harder | [Scaling: modular monolith first](playbook/architecture/scaling.md), [cloud native](playbook/platform/cloud-native.md) |
| A legacy system runs the business and nobody dares touch it | [Legacy modernisation](playbook/architecture/legacy-modernisation.md) |
| Tech debt eats most of every sprint | [Technical debt](playbook/architecture/technical-debt.md), [tech debt register](templates/docs/tech-debt-register.csv) |
| We find out about outages from customers | [Observability](playbook/architecture/observability.md), [service levels](playbook/reliability/service-levels.md) |
| Incidents are chaotic and the same ones keep coming back | [Incident management](playbook/reliability/incident-management.md), [postmortems](playbook/reliability/postmortems.md) |
| Our root cause analyses blame one person or one bug, and nothing changes | [Root cause analysis](playbook/reliability/root-cause-analysis.md), [postmortems](playbook/reliability/postmortems.md) |
| A bad release stayed in production for hours because nobody knew how to roll back | [Rollbacks](playbook/reliability/rollbacks.md), [release management](playbook/delivery/release-management.md) |
| Nobody remembers why the system is built this way | [Decision records](playbook/architecture/decision-records.md) |
| Every team picks a different database, queue and framework | [Tech radar](playbook/architecture/tech-radar.md), [golden paths](playbook/platform/golden-paths.md) |
| We adopted Kubernetes and it costs more than it saves | [Cloud native: when not to](playbook/platform/cloud-native.md), [developer platform](playbook/platform/developer-platform.md) |
| We run Kubernetes but only two people understand it | [Skills gap](playbook/people/skills-gap.md), [golden paths](playbook/platform/golden-paths.md) |
| The cloud bill grows faster than revenue | [FinOps](playbook/platform/finops.md) |
| One cloud provider outage would stop us completely | [Cloud, on-premises and air-gapped](playbook/platform/cloud-on-prem-air-gapped.md), [backup and recovery](playbook/reliability/backup-and-recovery.md) |
| Our board asks about the carbon cost of our software | [Green software](playbook/platform/green-software.md) |

## People and ways of working

| Problem | Go to |
|---|---|
| We cannot hire senior engineers, and interviews do not predict who will do well | [Hiring](playbook/people/hiring.md), [interview scorecard](templates/people/interview-scorecard.md) |
| New engineers take months to ship their first change | [Onboarding](playbook/people/onboarding.md) |
| Good engineers leave because there is no path to grow | [Career framework](playbook/people/career-framework.md) |
| We cannot find people with cloud, Kubernetes, security or AI skills | [Skills gap](playbook/people/skills-gap.md), [hiring](playbook/people/hiring.md) |
| The team is burnt out from pages and deadlines | [Sustainable pace](playbook/people/sustainable-pace.md), [on-call](playbook/reliability/on-call.md) |
| We do Scrum ceremonies but nothing improves | [Agile and Scrum](playbook/ways-of-working/agile-and-scrum.md) |
| We do Scrum ceremonies but AI changed how fast we write code, and planning no longer fits | [Agile in the AI era](playbook/ways-of-working/agile-in-the-ai-era.md), [planning and forecasting](playbook/ways-of-working/planning-and-forecasting.md) |
| Story points doubled after we adopted code assistants, but users see no difference | [Agile in the AI era](playbook/ways-of-working/agile-in-the-ai-era.md), [metrics](playbook/measurement/metrics.md) |
| Estimates are always wrong and deadlines always slip | [Planning and forecasting](playbook/ways-of-working/planning-and-forecasting.md) |
| Product and engineering argue about priorities | [Product partnership](playbook/ways-of-working/product-partnership.md) |
| Knowledge sits in three people's heads | [Knowledge sharing](playbook/people/knowledge-sharing.md), [documentation](playbook/people/documentation.md) |

## Strategy, governance and compliance

| Problem | Go to |
|---|---|
| We have a strategy deck that nobody follows | [Technical strategy](playbook/strategy/technical-strategy.md), [one-pager template](templates/strategy/strategy-one-pager.md) |
| We need to move to the cloud, off the cloud, or to a new platform without stopping the business | [Transition playbook](playbook/strategy/transition-playbook.md), [transition charter](templates/strategy/transition-charter.md) |
| Finance will not fund engineering improvements | [Business case](playbook/strategy/business-case.md) |
| Nobody knows who can approve an architecture decision | [Decision rights](playbook/operating-model/decision-rights.md), [engineering governance](playbook/operating-model/engineering-governance.md) |
| The board cannot see whether IT is under control | [IT governance](playbook/operating-model/it-governance.md) |
| ITIL processes and continuous delivery are fighting each other | [IT governance](playbook/operating-model/it-governance.md), [change management](playbook/reliability/change-management.md) |
| Architects are a bottleneck, or nobody owns architecture at all | [Architecture practice](playbook/architecture/architecture-practice.md) |
| Every team says it is at capacity, yet the important work does not get done | [Portfolio and capacity](playbook/strategy/portfolio-and-capacity.md), [planning and forecasting](playbook/ways-of-working/planning-and-forecasting.md) |
| Audits take months of engineering time | [Control mapping](playbook/compliance/control-mapping.md), [change management](playbook/reliability/change-management.md) |
| A weekly change board slows every release | [Change management](playbook/reliability/change-management.md), [regulated industries](playbook/compliance/regulated-industries.md) |
| We are locked into a vendor we can no longer afford | [Build, buy or adopt](playbook/strategy/build-buy-adopt.md), [public sector](playbook/compliance/public-sector.md) |
| We do not know what to prepare for in the next five years | [Horizon scan](playbook/strategy/horizon-scan.md) |
| We want to know where we stand overall | [Maturity model](playbook/measurement/maturity-model.md), [self-assessment](assessment/README.md) |

## Leadership

| Problem | Go to |
|---|---|
| I just started as CTO, CIO or chief architect and do not know where to begin | [First 90 days](leaders/first-90-days.md) |
| The board does not understand our technology risk, or we do not understand theirs | [Board and executive reporting](leaders/board-and-executive-reporting.md) |
| My week is all meetings and no decisions | [Operating rhythm](leaders/operating-rhythm.md), [decision making](leaders/decision-making.md) |
| We are about to acquire, invest in or depend on a technology company | [Technical due diligence](leaders/technical-due-diligence.md) |
| We have too many applications doing the same job | [Strategy toolkit: application portfolio](leaders/strategy-toolkit.md) |
| Our data strategy is a slide, not a plan | [For data and digital officers](leaders/for-data-and-digital-officers.md) |
| Each ministry builds its own systems and none of them talk to each other | [For government](leaders/for-government.md) |
| The regulator asks how we stay within impact tolerances | [For financial services](leaders/for-financial-services.md) |
| We are an EU financial entity and must show evidence for the EU DORA regulation | [For financial services](leaders/for-financial-services.md), [control mapping](playbook/compliance/control-mapping.md) |
| A major outage or cyber attack is happening and the executives do not know their role | [Crisis leadership](leaders/crisis-leadership.md), [crisis decision log](templates/leaders/crisis-decision-log.md) |
| We are a small business with one IT person, or none, and do not know what matters most | [For small and medium businesses](leaders/for-small-and-medium-businesses.md), [SME profile](profiles/sme.md) |
| Our outside IT provider holds all the passwords and we have never read the contract | [For small and medium businesses: managing an outside IT provider](leaders/for-small-and-medium-businesses.md#managing-an-outside-it-provider) |
| As a CEO or CFO, I cannot tell whether our technology function is healthy | [For business executives](leaders/for-business-executives.md) |

## Practice

| Problem | Go to |
|---|---|
| We have never practised a major incident or cyber attack | [Tabletop exercises](exercises/README.md) |
| People read the playbook but nothing sticks | [True or false quizzes](exercises/README.md), [katas](exercises/README.md) |
| Leaders keep repeating the same expensive decisions | [Decision games](exercises/README.md) |
