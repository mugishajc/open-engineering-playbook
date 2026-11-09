# Solo profile

Adopt Foundation in every area, in the order below, and skip everything that only pays off with a second team. One engineer has no reviewer, no on-call rota and no budget for process, so the aim is a setup that protects you and your clients while you sleep. Most of week 1 is one command and an afternoon of settings.

## Who this is for

- One engineer: a freelancer, a consultant, an indie product builder, or the only developer inside a non-software business.
- You ship to production yourself and nobody reviews your changes.
- If a client is a bank, insurer, health provider or government body, also read the [regulated](regulated.md) or [public sector](public-sector.md) overlay. Apply it to that client's work only.

## Target level by area

Foundation everywhere. The right column says when one area is worth taking to Standard early.

| Area | Target | Go to Standard early when |
|---|---|---|
| Strategy | Foundation | A client or investor asks for a roadmap |
| Operating model | Foundation | You bring in a second engineer or a subcontractor |
| Ways of working | Foundation | You work in a client's team with their cadence |
| Delivery | Foundation | You ship a library or API that others depend on |
| Quality | Foundation | A bug would cost a client money or data |
| Reliability | Foundation | You sign a contract with an uptime commitment |
| Security | Foundation | You hold payment, health or identity data |
| Data | Foundation | You process personal data for a client (you are their processor) |
| AI | Foundation | You ship a feature that calls a language model |
| Architecture | Foundation | The system outgrows one repository |
| Platform | Foundation | You run more than three production services |
| People | Foundation | You hire, even part time |
| Measurement | Foundation | You want to show clients your delivery record |
| Compliance | Foundation | A client sends you a security questionnaire |

## Week 1

Run `tools/adopt.sh --target <your-repo> --platform github --solo` (or `--platform gitlab`) first, for example `tools/adopt.sh --target . --platform github --solo` from inside your repository. It copies most of the files below and never overwrites yours. `--solo` copies the solo ruleset: the team ruleset needs a second person to approve, and GitHub does not let you approve your own pull request. Use the solo ruleset until a second engineer joins.

| Do this | Read | Template |
|---|---|---|
| Turn on multi-factor authentication for source control, cloud, registrar and email | [Access control](../playbook/security/access-control.md) | |
| Protect the default branch: no direct pushes, CI must pass before merge, no approval needed. GitHub does not read the ruleset file: import it with the command adopt.sh prints, then check that a direct push to main is rejected. On a private repository, rulesets need GitHub Pro or higher; on a free plan use classic branch protection instead | [Source control](../playbook/delivery/source-control.md) | [default-branch-solo.json](../templates/github/rulesets/default-branch-solo.json) |
| Run build, lint and tests in CI on every pull or merge request | [Continuous integration](../playbook/delivery/continuous-integration.md) | [ci.yml](../templates/github/workflows/ci.yml), [.gitlab-ci.yml](../templates/gitlab/.gitlab-ci.yml) |
| Move every secret into a secrets manager and turn on secret scanning | [Secrets](../playbook/security/secrets.md) | [.pre-commit-config.yaml](../templates/repo/.pre-commit-config.yaml) |
| Turn on automated dependency update pull requests, with one bot only | [Dependencies](../playbook/security/dependencies.md) | [dependabot.yml](../templates/github/dependabot.yml) or [renovate.json](../templates/repo/renovate.json) |
| List every data store and give each a class: public, internal, confidential or restricted | [Data governance](../playbook/data/data-governance.md) | [data-classification.md](../templates/docs/data-classification.md) |

Done when: a direct push to main is rejected, CI runs on every change, and the secret scanner reports no live secret in the repository or its history.

## Month 1

| Do this | Read | Template |
|---|---|---|
| Automate backups to a separate account or site, then restore one into a scratch environment | [Backup and recovery](../playbook/reliability/backup-and-recovery.md) | |
| Write a one-page incident plan: how you notice, who you tell, where updates go | [Incident management](../playbook/reliability/incident-management.md) | [incident-update.md](../templates/docs/incident-update.md) |
| Write your code assistant policy: which tools, and which client data never goes into them | [Code assistants](../playbook/people/code-assistants.md), [AI governance](../playbook/ai/ai-governance.md) | [code-assistant-policy.md](../templates/docs/code-assistant-policy.md) |
| List every AI tool you use and every AI feature you ship, with the data each one sees | [AI governance](../playbook/ai/ai-governance.md) | [ai-use-case-assessment.md](../templates/docs/ai-use-case-assessment.md) |
| Encrypt confidential and restricted data at rest and in transit | [Data security and privacy](../playbook/data/data-security-and-privacy.md) | |
| Add a failing test to every bug fix; keep the merge-gating suite under 10 minutes | [Test-driven development](../playbook/quality/test-driven-development.md), [Testing](../playbook/delivery/testing.md) | |
| Send structured logs and an external uptime check to one place you look at daily | [Observability](../playbook/architecture/observability.md) | |

## Quarter 1

| Do this | Read | Template |
|---|---|---|
| Write a one-page technical strategy: the main problem and three to seven actions for the next 12 months | [Technical strategy](../playbook/strategy/technical-strategy.md) | [strategy-one-pager.md](../templates/strategy/strategy-one-pager.md) |
| Record significant decisions as decision records in the repository | [Decision records](../playbook/architecture/decision-records.md) | [adr.md](../templates/docs/adr.md) |
| Version releases and generate the changelog from commits | [Versioning and changelogs](../playbook/delivery/versioning-and-changelogs.md) | [release-please.yml](../templates/github/workflows/release-please.yml), [CHANGELOG.md](../templates/repo/CHANGELOG.md) |
| Put production infrastructure in code and stop console changes | [Infrastructure as code](../playbook/delivery/infrastructure-as-code.md) | |
| Make the README good enough that someone new runs the project in under one hour | [Documentation](../playbook/people/documentation.md), [Golden paths](../playbook/platform/golden-paths.md) | [onboarding-checklist.md](../templates/docs/onboarding-checklist.md) |
| List the laws and contract terms that apply to you, and add a licence check to CI | [Control mapping](../playbook/compliance/control-mapping.md) | |
| Run the assessment and commit the answers file | [Maturity model](../playbook/measurement/maturity-model.md) | [assessment](../assessment/README.md) |

## Year 1

| Do this | Read | Template |
|---|---|---|
| Reach Foundation in all 14 areas, shown by four committed assessments | [Maturity model](../playbook/measurement/maturity-model.md) | [assessment](../assessment/README.md) |
| Threat model your main product once, and again after any major change | [Secure development](../playbook/security/secure-development.md) | [threat-model.md](../templates/docs/threat-model.md) |
| Publish a security contact and a vulnerability disclosure policy | [Vulnerability management](../playbook/security/vulnerability-management.md) | [SECURITY.md](../templates/repo/SECURITY.md), [vulnerability-disclosure-policy.md](../templates/docs/vulnerability-disclosure-policy.md) |
| Test a full restore every 90 days (four times this year) | [Backup and recovery](../playbook/reliability/backup-and-recovery.md) | |
| Practise rolling back each production service; keep the time under 15 minutes | [Rollbacks](../playbook/reliability/rollbacks.md) | |
| Log every deployment and its lead time, by hand if needed | [Metrics](../playbook/measurement/metrics.md) | |
| Review cloud spend monthly and remove anything without a purpose | [FinOps](../playbook/platform/finops.md) | |
| Read the horizon scan once and note what affects your clients | [Horizon scan](../playbook/strategy/horizon-scan.md) | |

## Skip at this size

| Skip | Why | Revisit when |
|---|---|---|
| Code review time limits | There is no second reviewer. Use CI, a self-review checklist and a day's pause on risky changes. | A second engineer joins |
| On-call rota, SLO error budget policy | One person cannot rotate. Keep an uptime check and a written response promise instead. | A contract names an uptime figure |
| RFCs, governance forum, tech radar | Decision records cover one person's decisions. | A second team exists |
| Kubernetes, service mesh, multi-region | A managed platform, PaaS or a single VM is cheaper to run alone. See [cloud native](../playbook/platform/cloud-native.md). | You run more services than you can patch by hand |
| Developer platform, service catalog | One README is your platform. | You run more than three services |
| Tooling for all five DORA metrics | A deployment log in a spreadsheet is enough. | Clients ask for delivery evidence |
| Career framework, structured hiring | Nobody to level or hire. | You hire |

## Check your progress

```bash
python3 assessment/assess.py --questions assessment/questions.toml --init --profile solo > my-answers.toml
python3 assessment/assess.py --questions assessment/questions.toml --answers my-answers.toml
```

The report lists your next five actions. For a solo engineer most of them are in week 1 and month 1 above.
