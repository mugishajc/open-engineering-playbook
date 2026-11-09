# Enterprise profile

Treat adoption as a transition, not a mandate: baseline a few representative teams, fix what blocks them through a platform and clear decision rights, then widen in waves. With 200 or more engineers the practices are rarely unknown. They are unevenly applied, and the gap between the best and the weakest team is where outages, audit findings and slow delivery come from. The target is Standard everywhere, with evidence you can show a board.

## Who this is for

- 200 or more engineers, many teams, shared platforms, and usually a mix of new and legacy systems.
- A CTO, CIO, chief architect, head of platform or principal engineer who must change how many teams work without stopping delivery.
- Most enterprises also fall under an overlay for some products. Apply [regulated](regulated.md) or [public sector](public-sector.md) to those products, not to the whole estate at once.

## Target level by area

| Area | Target | Notes |
|---|---|---|
| Strategy | Standard | Horizon scan every quarter; a charter for each transition |
| Operating model | Standard | Team types and decision rights published; separation of duties where regulated |
| Ways of working | Standard | Common forecasting from throughput; teams choose their own method |
| Delivery | Standard | Staged rollout for configuration and content, not only code |
| Quality | Standard | Accessibility testing for every user-facing service |
| Reliability | Standard | SLOs for tier 1 services first, then the rest |
| Security | Standard | Assured for supply chain and cryptography on long-lived systems |
| Data | Standard | One classification scheme across the group |
| AI | Standard | Assured if you run AI features in regulated decisions |
| Architecture | Standard | A debt register and modernisation plan for each major legacy system |
| Platform | Standard | Platform run as a product with its own users and SLOs |
| People | Standard | One career framework; structured hiring in every team |
| Measurement | Standard | Metrics for learning; assessment results tracked in git |
| Compliance | Standard | Assured for any product under a regulator |

## Week 1

| Do this | Read | Template |
|---|---|---|
| Name an executive sponsor and one transition owner with time to do it | [Transition playbook](../playbook/strategy/transition-playbook.md) | [transition-charter.md](../templates/strategy/transition-charter.md) |
| Baseline 3 to 5 representative teams with the assessment, including one legacy team | [Maturity model](../playbook/measurement/maturity-model.md) | [assessment](../assessment/README.md) |
| Map the people affected: who decides, who must be told, who can block | [Stakeholders and communication](../playbook/strategy/stakeholders-and-communication.md) | [stakeholder-map.md](../templates/strategy/stakeholder-map.md) |
| Write down current decision rights for production changes, architecture and vendors | [Decision rights](../playbook/operating-model/decision-rights.md) | [raci.csv](../templates/strategy/raci.csv) |

## Month 1

| Do this | Read | Template |
|---|---|---|
| Write the transition charter and business case: scope, exit criteria, rollback, cost | [Transition playbook](../playbook/strategy/transition-playbook.md), [Business case](../playbook/strategy/business-case.md) | [transition-charter.md](../templates/strategy/transition-charter.md), [business-case.md](../templates/strategy/business-case.md), [risk-register.csv](../templates/strategy/risk-register.csv) |
| Publish the group code assistant policy, start the AI use register and assess AI features in flight | [Code assistants](../playbook/people/code-assistants.md), [AI governance](../playbook/ai/ai-governance.md) | [code-assistant-policy.md](../templates/docs/code-assistant-policy.md), [ai-use-case-assessment.md](../templates/docs/ai-use-case-assessment.md) |
| Publish one data classification scheme and map existing schemes to it | [Data governance](../playbook/data/data-governance.md) | [data-classification.md](../templates/docs/data-classification.md) |
| Start the governance forum with a public decision log and a 10 working day answer limit; agree what goes to the board | [Engineering governance](../playbook/operating-model/engineering-governance.md), [IT governance](../playbook/operating-model/it-governance.md) | [adr.md](../templates/docs/adr.md) |
| Run the first horizon scan and add the results to the technical strategy | [Horizon scan](../playbook/strategy/horizon-scan.md), [Technical strategy](../playbook/strategy/technical-strategy.md) | [strategy-one-pager.md](../templates/strategy/strategy-one-pager.md) |

## Quarter 1

| Do this | Read | Template |
|---|---|---|
| Pilot a golden path with 2 or 3 teams; measure time to first production deploy | [Golden paths](../playbook/platform/golden-paths.md) | [k8s-service-baseline.yaml](../templates/platform/k8s-service-baseline.yaml), [argocd-application.yaml](../templates/platform/argocd-application.yaml) |
| Set the investment mix (run, grow, transform) and a capacity split per team, tied to the budget cycle | [Portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md) | |
| Publish team types and interaction modes; fix the top three dependency bottlenecks | [Team topology](../playbook/operating-model/team-topology.md) | |
| Collect the five DORA metrics from tooling for the pilot teams | [Metrics](../playbook/measurement/metrics.md) | |
| SLOs for tier 1 services, one incident process across the group, and a rollback under 15 minutes for each tier 1 service | [Service levels](../playbook/reliability/service-levels.md), [Incident management](../playbook/reliability/incident-management.md), [Rollbacks](../playbook/reliability/rollbacks.md) | [incident-update.md](../templates/docs/incident-update.md), [postmortem.md](../templates/docs/postmortem.md) |
| Vulnerability fix time limits and an SBOM for every release of tier 1 services | [Vulnerability management](../playbook/security/vulnerability-management.md), [Supply chain](../playbook/security/supply-chain.md) | [sbom-and-sign.yml](../templates/security/workflows/sbom-and-sign.yml) |
| Review critical suppliers and SaaS tools that hold restricted data | [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) | [vendor-risk-questionnaire.md](../templates/docs/vendor-risk-questionnaire.md) |
| Start a cryptographic inventory for systems holding data that must stay secret 10 years or more | [Post-quantum readiness](../playbook/security/post-quantum-readiness.md) | [crypto-inventory.csv](../templates/docs/crypto-inventory.csv) |

## Year 1

| Do this | Read | Template |
|---|---|---|
| Run the platform as a product: users, roadmap, SLOs, adoption numbers | [Developer platform](../playbook/platform/developer-platform.md) | [service-catalog-entry.yaml](../templates/docs/service-catalog-entry.yaml) |
| Widen the golden path and assessment to every team, in waves of 5 to 10 teams | [Transition playbook](../playbook/strategy/transition-playbook.md) | [assessment](../assessment/README.md) |
| A modernisation plan for the largest legacy systems, using the strangler fig pattern | [Legacy modernisation](../playbook/architecture/legacy-modernisation.md), [Technical debt](../playbook/architecture/technical-debt.md) | [tech-debt-register.csv](../templates/docs/tech-debt-register.csv) |
| Architects working as enablers: review triggers, fitness functions in CI, C4 diagrams for tier 1 systems | [Architecture practice](../playbook/architecture/architecture-practice.md) | |
| Postmortems that look for contributing factors and fix classes of failure | [Root cause analysis](../playbook/reliability/root-cause-analysis.md) | [postmortem.md](../templates/docs/postmortem.md) |
| An internal academy, pairing and platform rotations for the skills you cannot hire fast enough | [Skills gap](../playbook/people/skills-gap.md) | |
| A group tech radar refreshed every six months | [Tech radar](../playbook/architecture/tech-radar.md) | [tech-radar.csv](../templates/architecture/tech-radar.csv) |
| A zero trust roadmap with dates per pillar | [Zero trust](../playbook/security/zero-trust.md) | |
| A post-quantum migration plan for the systems in the inventory | [Post-quantum readiness](../playbook/security/post-quantum-readiness.md) | [crypto-inventory.csv](../templates/docs/crypto-inventory.csv) |
| One career framework and structured hiring across the group | [Career framework](../playbook/people/career-framework.md), [Hiring](../playbook/people/hiring.md) | [career-ladder.csv](../templates/people/career-ladder.csv), [interview-scorecard.md](../templates/people/interview-scorecard.md) |
| Cost per team and per service, plus a first carbon estimate for the largest workloads | [FinOps](../playbook/platform/finops.md), [Green software](../playbook/platform/green-software.md) | |
| A control map shared with audit, so evidence comes from pipelines | [Control mapping](../playbook/compliance/control-mapping.md) | |

## Skip at this size

| Skip | Why | Revisit when |
|---|---|---|
| A big-bang reorganisation | It stops delivery for months and loses people who know the systems. Change team boundaries in waves. | Never as a single event |
| One mandated tool for every team on day one | Teams with good reasons resist and you lose trust. Make the golden path the easiest choice instead. | The path is proven with pilot teams |
| A dashboard that ranks teams on DORA metrics | Teams game targets; the data stops being useful. | Never |
| Rewriting a legacy system from scratch | Rewrites run long and the old system keeps changing underneath. Replace it piece by piece. | Only when the old system cannot be run at all |
| A central team that does the work for other teams | It becomes a queue. Platform and enabling teams build and teach; stream-aligned teams own their services. | Never as the default |
| Assured in every area for every system | Evidence costs time. Scope Assured by regulation and service tier. | A regulator or certification scope requires it |

## Check your progress

```bash
python3 assessment/assess.py --questions assessment/questions.toml --init --profile enterprise > teams/payments.toml
python3 assessment/assess.py --questions assessment/questions.toml --answers teams/payments.toml --format json --output reports/payments.json
```

Keep one answers file per team in a shared repository. See [assessment/README.md](../assessment/README.md) for the quarterly review.
