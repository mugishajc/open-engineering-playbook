# Scale-up profile

Take every area to Standard within a year, starting with ownership, review speed and incident learning, because those are what break first when one team becomes five. A scale-up's risk is that what the founding team carried in its heads stops reaching new teams. Write it down, make the default path the easy path, and measure whether it works.

## Who this is for

- About 20 to 200 engineers in several teams, often hiring fast.
- An engineering leadership group: a CTO or VP, engineering managers, perhaps a first principal engineer, platform engineer or security lead.
- More than one codebase or service, and customers who now send security questionnaires and ask about uptime.
- If you sell to government or to regulated customers, apply the [public sector](public-sector.md) or [regulated](regulated.md) overlay to the products in scope.

## Target level by area

| Area | Target | Notes |
|---|---|---|
| Strategy | Standard | Add a transition charter before any migration that spans teams |
| Operating model | Standard | Name team types and owners before you add teams |
| Ways of working | Standard | Let teams choose Scrum or Kanban; require throughput data either way |
| Delivery | Standard | Code review within one working day is the first number to track |
| Quality | Standard | Flaky tests are the main cause of slow CI at this size |
| Reliability | Standard | SLOs for every user-facing service, postmortems for every major incident |
| Security | Standard | Go to Assured on supply chain if customers ask for SBOMs |
| Data | Standard | Owners and data contracts once teams publish data to each other |
| AI | Standard | Assess and test every AI feature; keep a register of tools in use |
| Architecture | Standard | RFCs for cross-team changes, a debt register per team |
| Platform | Standard | A golden path before a platform team |
| People | Standard | Structured hiring and a career framework before the next hiring wave |
| Measurement | Standard | All five DORA metrics from tooling, used for team learning only |
| Compliance | Standard | A control map once the first SOC 2 or ISO/IEC 27001 request arrives |

## Week 1

| Do this | Read | Template |
|---|---|---|
| Run the assessment with each team lead; commit one answers file per team or one for the whole group | [Maturity model](../playbook/measurement/maturity-model.md) | [assessment](../assessment/README.md) |
| Name one owning team for every repository and production service | [Roles](../playbook/operating-model/roles.md) | [CODEOWNERS](../templates/github/CODEOWNERS), [service-catalog-entry.yaml](../templates/docs/service-catalog-entry.yaml) |
| Write who decides what: production changes, architecture, vendors, hiring | [Decision rights](../playbook/operating-model/decision-rights.md) | [raci.csv](../templates/strategy/raci.csv) |
| Apply branch protection and the CI template to every active repository with `tools/adopt.sh` | [Source control](../playbook/delivery/source-control.md), [Continuous integration](../playbook/delivery/continuous-integration.md) | [default-branch.json](../templates/github/rulesets/default-branch.json), [ci.yml](../templates/github/workflows/ci.yml) |
| Classify every data store and check who can reach the restricted ones | [Data governance](../playbook/data/data-governance.md) | [data-classification.md](../templates/docs/data-classification.md) |

## Month 1

| Do this | Read | Template |
|---|---|---|
| Publish the code assistant policy and the AI use register; assess every AI feature in flight | [Code assistants](../playbook/people/code-assistants.md), [AI governance](../playbook/ai/ai-governance.md) | [code-assistant-policy.md](../templates/docs/code-assistant-policy.md), [ai-use-case-assessment.md](../templates/docs/ai-use-case-assessment.md) |
| Measure time to first review per team; agree one working day | [Code review](../playbook/delivery/code-review.md) | [PULL_REQUEST_TEMPLATE.md](../templates/github/PULL_REQUEST_TEMPLATE.md) |
| Write down each team's type and how it works with the others | [Team topology](../playbook/operating-model/team-topology.md) | |
| One incident process for all teams; blameless postmortems within 5 working days that look for contributing factors | [Incident management](../playbook/reliability/incident-management.md), [Postmortems](../playbook/reliability/postmortems.md), [Root cause analysis](../playbook/reliability/root-cause-analysis.md) | [incident-update.md](../templates/docs/incident-update.md), [postmortem.md](../templates/docs/postmortem.md) |
| Set on-call rules: nobody on call more than one week in four, a runbook per paging alert | [On-call](../playbook/reliability/on-call.md), [Sustainable pace](../playbook/people/sustainable-pace.md) | [runbook.md](../templates/docs/runbook.md) |
| A working agreement per team | [Agile and Scrum](../playbook/ways-of-working/agile-and-scrum.md) | [team-working-agreement.md](../templates/docs/team-working-agreement.md) |
| Quarantine or fix flaky tests within 5 working days | [Quality engineering](../playbook/quality/quality-engineering.md) | |

## Quarter 1

| Do this | Read | Template |
|---|---|---|
| SLOs and error budgets for every user-facing service | [Service levels](../playbook/reliability/service-levels.md) | |
| Vulnerability fix time limits by severity, with known exploited ones first | [Vulnerability management](../playbook/security/vulnerability-management.md) | |
| A golden path that creates a service with CI, observability and security checks | [Golden paths](../playbook/platform/golden-paths.md) | [k8s-service-baseline.yaml](../templates/platform/k8s-service-baseline.yaml) |
| Infrastructure as code with plans reviewed in pull requests | [Infrastructure as code](../playbook/delivery/infrastructure-as-code.md) | |
| Staged rollout for code, configuration and content; every service can roll back within 15 minutes | [GitOps and deployment](../playbook/delivery/gitops-and-deployment.md), [Rollbacks](../playbook/reliability/rollbacks.md) | [argocd-application.yaml](../templates/platform/argocd-application.yaml) |
| Written triggers for architecture review, an RFC process for changes that cross team lines, and a first tech radar | [Architecture practice](../playbook/architecture/architecture-practice.md), [RFCs](../playbook/architecture/rfcs.md), [Tech radar](../playbook/architecture/tech-radar.md) | [rfc.md](../templates/docs/rfc.md), [tech-radar.csv](../templates/architecture/tech-radar.csv) |
| Structured interviews and a career framework | [Hiring](../playbook/people/hiring.md), [Career framework](../playbook/people/career-framework.md) | [interview-scorecard.md](../templates/people/interview-scorecard.md), [career-ladder.csv](../templates/people/career-ladder.csv) |
| Set a quarterly capacity split for features, reliability, debt and platform | [Portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md) | |
| Collect the five DORA metrics from tooling; review monthly per team | [Metrics](../playbook/measurement/metrics.md) | |

## Year 1

| Do this | Read | Template |
|---|---|---|
| An engineering governance forum with a public decision log and a 10 working day answer limit | [Engineering governance](../playbook/operating-model/engineering-governance.md) | |
| A transition charter and business case for each cross-team migration | [Transition playbook](../playbook/strategy/transition-playbook.md), [Business case](../playbook/strategy/business-case.md) | [transition-charter.md](../templates/strategy/transition-charter.md), [business-case.md](../templates/strategy/business-case.md) |
| Owners and data contracts for shared datasets; quality checks on critical pipelines | [Data governance](../playbook/data/data-governance.md), [Data quality](../playbook/data/data-quality.md) | |
| Test AI features against the OWASP Top 10 for LLM Applications; automated evaluations before every model or prompt change | [AI application security](../playbook/ai/ai-application-security.md), [Building with AI](../playbook/ai/building-with-ai.md) | |
| Identity-aware access to internal services instead of network trust | [Zero trust](../playbook/security/zero-trust.md) | |
| A control map and a supplier review process, before the first audit | [Control mapping](../playbook/compliance/control-mapping.md), [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) | [vendor-risk-questionnaire.md](../templates/docs/vendor-risk-questionnaire.md) |
| A skills matrix per team, with pairing or rotation until each critical system has two capable people | [Skills gap](../playbook/people/skills-gap.md) | |
| Monthly cost per team, with an owner for every cost line | [FinOps](../playbook/platform/finops.md) | |
| A technical debt register per team and a plan for the largest legacy system | [Technical debt](../playbook/architecture/technical-debt.md), [Legacy modernisation](../playbook/architecture/legacy-modernisation.md) | [tech-debt-register.csv](../templates/docs/tech-debt-register.csv) |
| Four quarterly assessments; every team at Standard in at least 10 of 14 areas | [Maturity model](../playbook/measurement/maturity-model.md) | [assessment](../assessment/README.md) |

## Skip at this size

| Skip | Why | Revisit when |
|---|---|---|
| Assured evidence in every area | Collecting audit evidence costs time. Do it only for the controls a customer or certification asks for. | You pursue a certification or a regulated customer |
| Building an internal developer portal | A portal without a used golden path is a list of links. Build the path first. | The golden path is used by most new services |
| A central architecture board that approves every change | It becomes the bottleneck. RFCs with a fixed comment period scale better. | Never as an approval gate |
| Multi-region active-active, service mesh | Expensive to run; adopt only when an SLO needs it. See [scaling](../playbook/architecture/scaling.md) and [cloud native](../playbook/platform/cloud-native.md). | An SLO or customer contract requires it |
| Data mesh | An option for many domain teams with mature data skills, not a default. | Several domains publish data products to each other |
| Ranking teams on DORA metrics | It turns metrics into targets and teams game them. | Never |

## Check your progress

```bash
python3 assessment/assess.py --questions assessment/questions.toml --init --profile scale-up > team-a.toml
python3 assessment/assess.py --questions assessment/questions.toml --answers team-a.toml --format json
```

The JSON output is easy to combine across teams into one table for the leadership review.
