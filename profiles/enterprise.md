# Enterprise profile

Treat adoption as a transition, not a mandate: baseline a few representative teams, fix what blocks them through a platform and clear decision rights, then widen in waves. With 200 or more engineers the practices are rarely unknown. They are unevenly applied, and the gap between the best and the weakest team is where outages, audit findings and slow delivery come from. The target is Standard everywhere, with evidence you can show a board. Follow the phases of the [transition playbook](../playbook/strategy/transition-playbook.md): quarter 1 is Assess and Decide, pilots start in quarter 2, and the wider changes arrive wave by wave.

## Who this is for

- 200 to about 1,000 engineers, many teams, shared platforms, and usually a mix of new and legacy systems. Larger groups with several business units also read [large groups](#large-groups).
- A CTO, CIO, chief architect, head of platform or principal engineer who must change how many teams work without stopping delivery.
- Most enterprises also fall under an overlay for some products. Apply [regulated](regulated.md) or [public sector](public-sector.md) to those products, not to the whole estate at once.

## Target level by area

| Area | Target | Notes |
|---|---|---|
| Strategy | Standard | Horizon scan every 6 months, feeding the quarterly strategy review; a charter for each transition |
| Operating model | Standard | Team types and decision rights published; separation of duties where regulated |
| Product | Standard | A product strategy per product area under one company strategy; teams get problems, not features |
| Project management | Standard | A small PMO with governance scaled by class; most projects are Small |
| Ways of working | Standard | Common forecasting from throughput; teams choose their own method |
| Delivery | Standard | Staged rollout for configuration and content, not only code |
| Quality | Standard | Accessibility testing for every user-facing service |
| Reliability | Standard | SLOs for Tier 1 services first, then the rest |
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
| Check three risks for every Tier 1 service before the transition starts: date of the last restore test, privileged accounts without phishing-resistant MFA, and critical vulnerabilities past their fix deadline. Fix the worst gap now. | [Board and executive reporting](../leaders/board-and-executive-reporting.md), [Backup and recovery](../playbook/reliability/backup-and-recovery.md), [Access control](../playbook/security/access-control.md) | [risk-register.csv](../templates/strategy/risk-register.csv) |

## Month 1

| Do this | Read | Template |
|---|---|---|
| Write the transition charter and business case: scope, exit criteria, rollback, cost | [Transition playbook](../playbook/strategy/transition-playbook.md), [Business case](../playbook/strategy/business-case.md) | [transition-charter.md](../templates/strategy/transition-charter.md), [business-case.md](../templates/strategy/business-case.md), [risk-register.csv](../templates/strategy/risk-register.csv) |
| Publish the group code assistant policy, start the AI use register and assess AI features in flight | [Code assistants](../playbook/people/code-assistants.md), [AI governance](../playbook/ai/ai-governance.md) | [code-assistant-policy.md](../templates/docs/code-assistant-policy.md), [ai-use-case-assessment.md](../templates/docs/ai-use-case-assessment.md) |
| Publish one data classification scheme and map existing schemes to it | [Data governance](../playbook/data/data-governance.md) | [data-classification.md](../templates/docs/data-classification.md) |
| Start the governance forum with a public decision log: 5 working days to answer a complete request in each division's review group, 10 for the group-level forum. Agree what goes to the board | [Engineering governance](../playbook/operating-model/engineering-governance.md), [IT governance](../playbook/operating-model/it-governance.md) | [adr.md](../templates/docs/adr.md) |
| Run the first horizon scan and add the results to the technical strategy | [Horizon scan](../playbook/strategy/horizon-scan.md), [Technical strategy](../playbook/strategy/technical-strategy.md) | [strategy-one-pager.md](../templates/strategy/strategy-one-pager.md) |

## Quarter 1: Assess and Decide

At this size Assess takes 6 to 12 weeks and Decide 4 to 8 weeks. Do not start pilots before the Decide gate.

| Do this | Read | Template |
|---|---|---|
| Agree the Tier 1 service list and test a restore for every Tier 1 service | [Backup and recovery](../playbook/reliability/backup-and-recovery.md) | |
| Give each Tier 1 service a written, timed rollback or fall-forward plan. Set a recovery target per service class: 15 minutes applies to services deployed through the pipeline, not to vendor packages or mainframe batch | [Rollbacks](../playbook/reliability/rollbacks.md) | |
| Choose 2 or 3 pilot teams, one with a legacy system, and the golden path they will pilot | [Golden paths](../playbook/platform/golden-paths.md), [Transition playbook](../playbook/strategy/transition-playbook.md) | [transition-charter.md](../templates/strategy/transition-charter.md) |
| Set the investment mix (run, grow, transform) and a capacity split per team, tied to the budget cycle | [Portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md) | |
| Publish team types and interaction modes; name the top three dependency bottlenecks | [Team topology](../playbook/operating-model/team-topology.md) | |
| Baseline the five DORA metrics for the pilot teams, by hand if the tooling is not ready | [Metrics](../playbook/measurement/metrics.md) | |
| Label every funded piece of work project or product, and name the persistent team that will run what each project builds | [Projects and products](../playbook/project-management/projects-and-products.md) | [project-charter.md](../templates/project/project-charter.md) |
| Vulnerability fix time limits for Tier 1 services | [Vulnerability management](../playbook/security/vulnerability-management.md) | |
| Review critical suppliers and SaaS tools that hold restricted data | [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) | [vendor-risk-questionnaire.md](../templates/docs/vendor-risk-questionnaire.md) |
| Start a cryptographic inventory for systems holding data that must stay secret 10 years or more | [Post-quantum readiness](../playbook/security/post-quantum-readiness.md) | [crypto-inventory.csv](../templates/docs/crypto-inventory.csv) |

## Year 1

| Do this | Read | Template |
|---|---|---|
| Pilot the golden path with the chosen teams (8 to 16 weeks); measure time to first production deploy | [Golden paths](../playbook/platform/golden-paths.md) | [k8s-service-baseline.yaml](../templates/platform/k8s-service-baseline.yaml), [argocd-application.yaml](../templates/platform/argocd-application.yaml) |
| In each wave: SLOs for Tier 1 services, one incident process, and an SBOM for every Tier 1 release | [Service levels](../playbook/reliability/service-levels.md), [Incident management](../playbook/reliability/incident-management.md), [Supply chain](../playbook/security/supply-chain.md) | [incident-update.md](../templates/docs/incident-update.md), [postmortem.md](../templates/docs/postmortem.md), [sbom-and-sign.yml](../templates/security/workflows/sbom-and-sign.yml) |
| Run the platform as a product: users, roadmap, SLOs, adoption numbers | [Developer platform](../playbook/platform/developer-platform.md) | [service-catalog-entry.yaml](../templates/docs/service-catalog-entry.yaml) |
| Widen the golden path and assessment to every team in waves of 2 to 5 teams. Once the first two waves have closed, run waves in parallel in different divisions | [Transition playbook](../playbook/strategy/transition-playbook.md) | [assessment](../assessment/README.md) |
| A modernisation plan for the largest legacy systems, using the strangler fig pattern | [Legacy modernisation](../playbook/architecture/legacy-modernisation.md), [Technical debt](../playbook/architecture/technical-debt.md) | [tech-debt-register.csv](../templates/docs/tech-debt-register.csv) |
| Architects working as enablers: review triggers, fitness functions in CI, C4 diagrams for Tier 1 systems | [Architecture practice](../playbook/architecture/architecture-practice.md) | |
| Postmortems that look for contributing factors and fix classes of failure | [Root cause analysis](../playbook/reliability/root-cause-analysis.md) | [postmortem.md](../templates/docs/postmortem.md) |
| An internal academy, pairing and platform rotations for the skills you cannot hire fast enough | [Skills gap](../playbook/people/skills-gap.md) | |
| A group tech radar refreshed every six months | [Tech radar](../playbook/architecture/tech-radar.md) | [tech-radar.csv](../templates/architecture/tech-radar.csv) |
| A zero trust roadmap with dates per pillar | [Zero trust](../playbook/security/zero-trust.md) | |
| A post-quantum migration plan for the systems in the inventory | [Post-quantum readiness](../playbook/security/post-quantum-readiness.md) | [crypto-inventory.csv](../templates/docs/crypto-inventory.csv) |
| One career framework and structured hiring across the group | [Career framework](../playbook/people/career-framework.md), [Hiring](../playbook/people/hiring.md) | [career-ladder.csv](../templates/people/career-ladder.csv), [interview-scorecard.md](../templates/people/interview-scorecard.md) |
| Cost per team and per service, plus a first carbon estimate for the largest workloads | [FinOps](../playbook/platform/finops.md), [Green software](../playbook/platform/green-software.md) | |
| A control map shared with audit, so evidence comes from pipelines | [Control mapping](../playbook/compliance/control-mapping.md) | |
| Status reports built from team systems, colours set by rule, steering groups that decide, and stage gates funded one stage at a time | [Status reporting](../playbook/project-management/status-reporting.md), [A modern PMO](../playbook/project-management/modern-pmo.md) | [status-report.md](../templates/project/status-report.md), [stage-gate-checklist.md](../templates/project/stage-gate-checklist.md) |
| A test strategy per product, with performance, security and accessibility testing on a schedule and quality engineers who coach | [Test strategy](../playbook/quality/test-strategy.md), [For QA and test leaders](../leaders/for-qa-and-test-leaders.md) | [test-strategy.md](../templates/quality/test-strategy.md) |

## Skip at this size

| Skip | Why | Revisit when |
|---|---|---|
| A big-bang reorganisation | It stops delivery for months and loses people who know the systems. Change team boundaries in waves. | Never as a single event |
| One mandated tool for every team on day one | Teams with good reasons resist and you lose trust. Make the golden path the easiest choice instead. | The path is proven with pilot teams |
| A dashboard that ranks teams on DORA metrics | Teams game targets; the data stops being useful. | Never |
| Rewriting a legacy system from scratch | Rewrites run long and the old system keeps changing underneath. Replace it piece by piece. | Only when the old system cannot be run at all |
| A central team that does the work for other teams | It becomes a queue. Platform and enabling teams build and teach; stream-aligned teams own their services. | Never as the default |
| Assured in every area for every system | Evidence costs time. Scope Assured by regulation and service tier. | A regulator or certification scope requires it |

## Large groups

Groups with 1,000 or more engineers, or several business units with their own technology leaders, add five steps to the plan above.

| Do this | Why | Read |
|---|---|---|
| Write the group and division split: what the group decides (identity, security baseline, data classification, shared platforms), what each division decides | Without it, every standard becomes a negotiation | [Decision rights: group and division](../playbook/operating-model/decision-rights.md#group-and-division), [IT governance](../playbook/operating-model/it-governance.md) |
| Convert the existing PMO, architecture board and change advisory board, do not abolish them: give each a written purpose, an answer limit and the evidence it now reads from pipelines | They hold real knowledge and authority; removing them stalls the transition | [Engineering governance: if you already have a PMO, an EA board or a change board](../playbook/operating-model/engineering-governance.md#if-you-already-have-a-pmo-an-ea-board-or-a-change-board), [Change management](../playbook/reliability/change-management.md) |
| If a scaling framework is in place, keep its planning cadence and drop the ceremonies the pilot shows add no value. Change one thing per wave | Replacing a framework at once is a big-bang reorganisation | [Agile and Scrum](../playbook/ways-of-working/agile-and-scrum.md) |
| Bring outsourcing partners onto the same practices through the contract: review, CI, security checks, access rules and the assessment apply to their teams too. Change time-and-materials terms to outcome measures at renewal | A large share of delivery may sit with partners the playbook cannot reach otherwise | [Suppliers and contracts](../playbook/strategy/suppliers-and-contracts.md), [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) |
| Consult employee representatives or works councils before the Pilot gate wherever law or agreements require it | Roles change; late consultation can stop a programme | [Transition playbook: people and roles](../playbook/strategy/transition-playbook.md#people-and-roles) |

## Check your progress

```bash
python3 assessment/assess.py --questions assessment/questions.toml --init --profile enterprise > teams/payments.toml
python3 assessment/assess.py --questions assessment/questions.toml --answers teams/payments.toml --format json --output reports/payments.json
```

Keep one answers file per team in a shared repository. See [assessment/README.md](../assessment/README.md) for the quarterly review.
