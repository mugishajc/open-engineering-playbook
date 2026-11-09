# Startup profile

Adopt Foundation in every area in the first quarter, then take delivery, security and data to Standard as soon as a customer contract or a second team needs it. A startup's main risks are losing data, leaking secrets and shipping so slowly that it runs out of money. These steps cover all three and cost a few days of setup, not a process team.

## Who this is for

- One product team, up to about 20 engineers, usually one codebase or a handful of services.
- A CTO or tech lead who still writes code and makes most technical decisions.
- If you sell to government or to banks, insurers, health or telecoms, also apply the [public sector](public-sector.md) or [regulated](regulated.md) overlay. Many startups apply it to one product line only.

## Target level by area

| Area | Target | Go to Standard early when |
|---|---|---|
| Strategy | Foundation | You raise a round or plan a platform migration |
| Operating model | Foundation | You split into a second team |
| Ways of working | Foundation | Forecasts are missed two cycles in a row |
| Delivery | Foundation | More than 5 engineers merge to the same repository daily |
| Quality | Foundation | Customers find more bugs than your tests do |
| Reliability | Foundation | A contract names an uptime figure or a support window |
| Security | Foundation | You hold payment, health or identity data, or a customer sends a security questionnaire |
| Data | Foundation | You process personal data of more than a few thousand people |
| AI | Foundation | An AI feature reaches customers |
| Architecture | Foundation | A second team works in the same codebase |
| Platform | Foundation | New services take more than a day to set up |
| People | Foundation | You hire more than 3 engineers in a quarter |
| Measurement | Foundation | Investors or the board ask about delivery speed |
| Compliance | Foundation | A customer asks for SOC 2 or ISO/IEC 27001 |

## Week 1

Run `tools/adopt.sh --target <repo> --platform github --with-security` on your main repository. Review the copied files in one pull request.

| Do this | Read | Template |
|---|---|---|
| Require multi-factor authentication everywhere; remove leavers' access | [Access control](../playbook/security/access-control.md) | |
| Protect the default branch and require a passing CI run and one approval. Import the ruleset (adopt.sh prints the `gh api` command); a file in the repository does nothing | [Source control](../playbook/delivery/source-control.md) | [default-branch.json](../templates/github/rulesets/default-branch.json) |
| Run build, lint and tests in CI on every pull or merge request | [Continuous integration](../playbook/delivery/continuous-integration.md) | [ci.yml](../templates/github/workflows/ci.yml), [.gitlab-ci.yml](../templates/gitlab/.gitlab-ci.yml) |
| Add a pull request template and CODEOWNERS with real names | [Code review](../playbook/delivery/code-review.md) | [PULL_REQUEST_TEMPLATE.md](../templates/github/PULL_REQUEST_TEMPLATE.md), [CODEOWNERS](../templates/github/CODEOWNERS) |
| Move secrets out of code; turn on secret scanning and one dependency update bot | [Secrets](../playbook/security/secrets.md), [Dependencies](../playbook/security/dependencies.md) | [dependabot.yml](../templates/github/dependabot.yml) or [renovate.json](../templates/repo/renovate.json) |
| Classify every data store: public, internal, confidential or restricted | [Data governance](../playbook/data/data-governance.md) | [data-classification.md](../templates/docs/data-classification.md) |

## Month 1

| Do this | Read | Template |
|---|---|---|
| Publish a code assistant policy: approved tools, data that never goes in, how generated code is reviewed | [Code assistants](../playbook/people/code-assistants.md) | [code-assistant-policy.md](../templates/docs/code-assistant-policy.md) |
| Start an AI use register and assess every AI feature before customers see it | [AI governance](../playbook/ai/ai-governance.md), [Building with AI](../playbook/ai/building-with-ai.md) | [ai-use-case-assessment.md](../templates/docs/ai-use-case-assessment.md) |
| Automate backups off-site and test a restore | [Backup and recovery](../playbook/reliability/backup-and-recovery.md) | |
| Write the incident process and use the update template in the next incident | [Incident management](../playbook/reliability/incident-management.md) | [incident-update.md](../templates/docs/incident-update.md) |
| Write a team working agreement and put all work on one board with a work-in-progress limit | [Agile and Scrum](../playbook/ways-of-working/agile-and-scrum.md) | [team-working-agreement.md](../templates/docs/team-working-agreement.md) |
| Write the onboarding checklist; the next hire merges a change in week one | [Onboarding](../playbook/people/onboarding.md) | [onboarding-checklist.md](../templates/docs/onboarding-checklist.md) |
| Record significant decisions as decision records | [Decision records](../playbook/architecture/decision-records.md) | [adr.md](../templates/docs/adr.md) |
| Encrypt confidential and restricted data; limit access to named roles | [Data security and privacy](../playbook/data/data-security-and-privacy.md) | |

## Quarter 1

| Do this | Read | Template |
|---|---|---|
| Write a one-page technical strategy and a one-page decision rights table | [Technical strategy](../playbook/strategy/technical-strategy.md), [Decision rights](../playbook/operating-model/decision-rights.md) | [strategy-one-pager.md](../templates/strategy/strategy-one-pager.md), [raci.csv](../templates/strategy/raci.csv) |
| Measure time to first review; aim for a median under 4 working hours and every review started within one working day | [Code review](../playbook/delivery/code-review.md) | |
| Automate versioning, changelog and release | [Release management](../playbook/delivery/release-management.md) | [release-please.yml](../templates/github/workflows/release-please.yml), [release-checklist.md](../templates/docs/release-checklist.md) |
| Hold a blameless postmortem within 5 working days of every major incident; list contributing factors, not one root cause | [Postmortems](../playbook/reliability/postmortems.md), [Root cause analysis](../playbook/reliability/root-cause-analysis.md) | [postmortem.md](../templates/docs/postmortem.md) |
| Threat model the product's riskiest flow (login, payments or data export) | [Secure development](../playbook/security/secure-development.md) | [threat-model.md](../templates/docs/threat-model.md) |
| Hire with a structured interview and a scored work sample | [Hiring](../playbook/people/hiring.md) | [interview-scorecard.md](../templates/people/interview-scorecard.md) |
| Track deployment frequency and change lead time; run the assessment and commit it | [Metrics](../playbook/measurement/metrics.md), [Maturity model](../playbook/measurement/maturity-model.md) | [assessment](../assessment/README.md) |

## Year 1

| Do this | Read | Template |
|---|---|---|
| Set SLOs for the two most used user-facing flows and review the error budget monthly | [Service levels](../playbook/reliability/service-levels.md) | |
| Start a 24 by 7 on-call rota once 6 people can share it; before that, cover business hours only and say so in customer terms. Write a runbook per paging alert | [On-call](../playbook/reliability/on-call.md) | [runbook.md](../templates/docs/runbook.md) |
| Roll out code and configuration in stages with automatic rollback; practise a rollback every quarter | [GitOps and deployment](../playbook/delivery/gitops-and-deployment.md), [Rollbacks](../playbook/reliability/rollbacks.md), [Feature flags](../playbook/delivery/feature-flags.md) | |
| Set fix time limits for vulnerabilities by severity | [Vulnerability management](../playbook/security/vulnerability-management.md) | [vulnerability-disclosure-policy.md](../templates/docs/vulnerability-disclosure-policy.md) |
| Review every SaaS tool that holds customer data | [Third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) | [vendor-risk-questionnaire.md](../templates/docs/vendor-risk-questionnaire.md) |
| Start a technical debt register and agree a share of time for it | [Technical debt](../playbook/architecture/technical-debt.md) | [tech-debt-register.csv](../templates/docs/tech-debt-register.csv) |
| Publish a career framework before you pass 15 engineers | [Career framework](../playbook/people/career-framework.md) | [career-ladder.csv](../templates/people/career-ladder.csv) |
| Set a quarterly capacity split for features, reliability, debt and platform, and check it against actual time | [Portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md) | |
| Keep a skills matrix so every critical system has at least two people who can run it | [Skills gap](../playbook/people/skills-gap.md) | |
| Forecast dates from throughput, as ranges | [Planning and forecasting](../playbook/ways-of-working/planning-and-forecasting.md) | |
| Four committed assessments, Foundation in all 14 areas | [Maturity model](../playbook/measurement/maturity-model.md) | [assessment](../assessment/README.md) |

## Skip at this size

| Skip | Why | Revisit when |
|---|---|---|
| A platform team and an internal developer portal | One team does not need a product for itself. A good template repository is enough. | Three or more teams repeat the same setup work |
| Governance forum, architecture review board | The CTO and a decision record are faster. | A second team disagrees with the first |
| RFCs for every change | Use decision records; keep RFCs for changes that affect customers or the whole company. | A change crosses team lines |
| Tech radar | A short "what we use" list in the README does the job. | Teams pick different tools for the same job |
| Kubernetes, service mesh, multi-region | Managed services cost less engineering time at this size. See [cloud native](../playbook/platform/cloud-native.md). | Your SLOs or customers require it |
| Change advisory board | CI, review and staged rollout are the control. | A regulator requires one; then read [change management](../playbook/reliability/change-management.md) |
| Tooling for all five DORA metrics | Two metrics by hand teach you more than a dashboard nobody reads. | Scale-up |
| Data mesh, data platform team | One owner per dataset is enough. | Several teams publish data to each other |

## Check your progress

```bash
python3 assessment/assess.py --questions assessment/questions.toml --init --profile startup > my-answers.toml
python3 assessment/assess.py --questions assessment/questions.toml --answers my-answers.toml
```

Commit the answers file. The diff between two quarters is your progress report to the board.
