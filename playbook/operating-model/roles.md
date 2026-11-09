# Roles

Give every engineering responsibility a named role, and give each person a short reading list so they start with the parts of the playbook that matter to their job. In small organisations one person holds several roles. That is fine as long as the combinations do not break separation of duties where it is required.

## Outcomes

Starting points. Tune them to your organisation.

- Every role below that exists in your organisation is filled by a named person, or explicitly held by another role.
- New people in each role finish their playbook reading list within their first 2 weeks.
- In Assured setups, no person holds two roles that must be separated (for example author and sole approver of the same production change).
- Role descriptions are reviewed once a year and after any reorganisation.

## Roles and where to start

| Role | Owns | Read first in the playbook |
|---|---|---|
| Solo engineer | everything: code, releases, security, support | [profile: Solo](../../profiles/solo.md), [source control](../delivery/source-control.md), [continuous integration](../delivery/continuous-integration.md), [backup and recovery](../reliability/backup-and-recovery.md) |
| Tech lead | technical direction of one team, design quality, review standards | [code review](../delivery/code-review.md), [decision records](../architecture/decision-records.md), [production readiness](../reliability/production-readiness.md), [decision rights](decision-rights.md) |
| Staff or principal engineer | technical direction across teams, strategy drafts, hard problems | [technical strategy](../strategy/technical-strategy.md), [transition playbook](../strategy/transition-playbook.md), [RFCs](../architecture/rfcs.md), [engineering governance](engineering-governance.md) |
| Engineering manager | people, team health, delivery, hiring | [team topology](team-topology.md), [onboarding](../people/onboarding.md), [metrics](../measurement/metrics.md), [on-call](../reliability/on-call.md) |
| Head of engineering | engineering organisation, standards, budget across teams | [decision rights](decision-rights.md), [engineering governance](engineering-governance.md), [maturity model](../measurement/maturity-model.md), [business case](../strategy/business-case.md) |
| CTO | technology strategy, investment, risk at board level | [technical strategy](../strategy/technical-strategy.md), [horizon scan](../strategy/horizon-scan.md), [business case](../strategy/business-case.md), [stakeholders and communication](../strategy/stakeholders-and-communication.md) |
| CISO | security risk, policy, incident response, regulator contact on security | [secure development](../security/secure-development.md), [supply chain](../security/supply-chain.md), [vulnerability management](../security/vulnerability-management.md), [control mapping](../compliance/control-mapping.md) |
| Platform team | internal platform, golden paths, shared infrastructure | [developer platform](../platform/developer-platform.md), [golden paths](../platform/golden-paths.md), [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md), [observability](../architecture/observability.md) |
| Product manager | outcomes, priorities, service levels with users | [service levels](../reliability/service-levels.md), [feature flags](../delivery/feature-flags.md), [business case](../strategy/business-case.md), [AI governance](../ai/ai-governance.md) |
| Technical evangelist | explaining changes, collecting feedback, documentation | [stakeholders and communication](../strategy/stakeholders-and-communication.md), [documentation](../people/documentation.md), [knowledge sharing](../people/knowledge-sharing.md) |
| Procurement and legal | contracts, licences, supplier risk, data protection terms | [build, buy, adopt or partner](../strategy/build-buy-adopt.md), [public sector](../compliance/public-sector.md), [regulated industries](../compliance/regulated-industries.md), [data governance](../data/data-governance.md) |
| Auditor (internal or external) | independent assurance that controls work | [control mapping](../compliance/control-mapping.md), [change management](../reliability/change-management.md), [access control](../security/access-control.md), [postmortems](../reliability/postmortems.md) |

## What each role must not do alone

These are separation-of-duties limits for the Assured level. At Foundation, write down where one person holds both sides and add a compensating check, such as an automated test gate or a monthly review.

| Activity | Must be separate from |
|---|---|
| Writing a production change | approving the same change |
| Granting privileged access | using that access |
| Requesting a security waiver | approving the same waiver |
| Running the backup process | verifying restores for audit |
| Choosing a supplier | approving payment to that supplier |
| Building a model or AI system | validating it for production use |

## Practice

### Foundation

Solo and Startup. One or two people hold most roles. List the roles, the holder of each, and the backup person. The founder or CTO holds CISO duties until there are about 20 engineers or a customer contract requires a named security lead. Use automation to cover separation of duties: protected branches, required checks and signed releases.

### Standard

Scale-up and Enterprise. Write a one-page description for each role: owns, decides, consulted on, reads first. Link them from the [RACI](../../templates/strategy/raci.csv). Staff and principal engineers have a written scope (a domain or a set of teams). Engineering managers and tech leads are different people in teams larger than about 6. Fund at least one platform team once three or more teams share infrastructure.

### Assured

Regulated and Public sector. Everything in Standard, plus:

- Enforce the separation table above in tooling and check it quarterly with access reviews. See [access control](../security/access-control.md).
- Name the accountable owner for every critical system, and the management body member accountable for ICT risk where a law such as the EU Digital Operational Resilience Act requires it.
- Keep a record of role assignments and changes for your retention period.
- Make sure auditors can read evidence directly (read-only access to repositories, CI logs and ticket history) instead of asking engineers for screenshots.

## Cloud, on-premises and air-gapped

On-premises and air-gapped environments need named people for roles that a cloud provider would otherwise fill: hardware lifecycle, network, data centre access, and media transfer across the air gap. On classified networks, roles may also need security clearance. Plan cover for each cleared role, because a single cleared person is a single point of failure.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Staff engineer as a title without scope | Write the domain they own and the decisions they make. |
| CISO who learns about releases from incidents | Add the CISO as consulted on the rows in [decision rights](decision-rights.md) that change risk. |
| Auditors depend on engineers for screenshots | Give read-only access to systems of record. |
| One person holds every privileged role | Split roles or add automated compensating controls and reviews. |

## Templates

- [RACI](../../templates/strategy/raci.csv)
- [Onboarding checklist](../../templates/docs/onboarding-checklist.md)

## Sources

- ISO/IEC 27001:2022, Annex A 5.2 (roles and responsibilities) and 5.3 (segregation of duties): https://www.iso.org/standard/27001
- Matthew Skelton and Manuel Pais, "Team Topologies", IT Revolution, 2019: https://teamtopologies.com
