# Developer platform

Build an internal developer platform only when several teams are solving the same infrastructure problems separately, and then run it as a product with users, a roadmap and service levels. A platform team exists to cut the work that stream-aligned teams repeat: provisioning, pipelines, observability, secrets, compliance evidence. If you have one or two teams, use managed services and a good template instead of building a platform.

## Outcomes

Starting points. Tune them to your organisation.

- Common requests (new service, new database, new environment, DNS record, certificate, secret) are self-service and complete in under 1 hour without a ticket.
- Platform services meet their own published SLOs, for example 99.5% availability for CI during working hours. The deploy and rollback path is held to the highest tier of any service it deploys, 24/7, because it is how teams roll back at night.
- Developer satisfaction with the platform, surveyed every 6 months, is stable or rising. Response rate is at least 40%.
- Time spent by stream-aligned teams on infrastructure work falls quarter on quarter, measured by survey or by work item tagging.

## When to build one, and when not to

| Situation | Do this |
|---|---|
| Solo or one team, under about 20 engineers | Do not build a platform. Use managed services, one [golden path](golden-paths.md) template and good docs. A part-time owner is enough. |
| 2 teams with some duplicated work | Name one engineer as platform owner part-time. Share templates and pipeline components. Still no platform team. |
| 3 or more teams repeating the same infrastructure work, or 40+ engineers | Start a platform team of 3 to 5 people with a product owner. Build the thinnest viable platform first. |
| Enterprise, regulated or public sector with shared controls | A platform group with several teams (for example developer experience, runtime, data, security tooling), each run as a product. |
| Must run on-premises or air-gapped | The platform carries the extra work of mirrors, registries and update transfer. Plan for it from day one. |

Signals that you need one: every team writes its own pipeline, teams wait days for infrastructure tickets, each audit means collecting evidence by hand from every team, and on-call tooling differs across teams.

## Platform as a product

- **Users.** The platform's customers are the engineers in stream-aligned teams. Interview 5 teams before building anything, then at least 2 teams every quarter. Judge the platform by the work it removes for those teams, not by adoption you mandated; see [internal platforms and staff systems](../../leaders/for-product-leaders.md#internal-platforms-and-staff-systems).
- **Product owner.** Someone owns the roadmap and says no. Without this the platform becomes a queue of tickets.
- **Thinnest viable platform.** Team Topologies uses this phrase: start with the smallest set of services, docs and APIs that removes real work. It may be a wiki page and three templates.
- **Interfaces.** Expose capabilities as self-service: a portal, a command-line tool, an API or a GitOps repository. Ticket queues are a last resort.
- **Interaction modes.** Use Team Topologies modes on purpose: collaboration with a team while a new capability is being shaped, X-as-a-Service once it is stable, facilitating to help teams adopt it.
- **Service levels.** Publish SLOs for platform services and report on them like any other service (see [service levels](../reliability/service-levels.md)).
- **Deprecation.** Announce removals of platform features with at least 3 months' notice and a migration guide.
- **Skills.** The platform team holds deep specialist skills so product teams do not each need them, and runs rotations and labs to spread the rest (see [skills gap](../people/skills-gap.md)).

## Capabilities, in rough build order

| Order | Capability | Typical tools |
|---|---|---|
| 1 | Source control, CI, artefact registry | GitHub, GitLab, Gitea or Forgejo; Harbor, Nexus or Artifactory |
| 2 | Service templates and catalogue | Template repositories, Copier, Backstage |
| 3 | Deployment to environments | Argo CD or Flux for GitOps, or the CI system's deploy jobs |
| 4 | Secrets and identity | HashiCorp Vault or OpenBao, cloud KMS, Keycloak or the corporate identity provider |
| 5 | Observability | OpenTelemetry Collector, Prometheus, Grafana, Loki, Tempo, or a managed service |
| 6 | Self-service data stores and queues | Operators on Kubernetes, or managed cloud databases behind a request form |
| 7 | AI gateway | Model routing, quotas, cost allocation, logging, prompt and response redaction, fallback between providers. Built or bought; one per organisation. See [AI architecture patterns](../ai/ai-architecture-patterns.md). |
| 8 | Compliance evidence collection | Pipeline attestations, policy-as-code reports, catalogue metadata |

## Practice

### Foundation

- No platform team. One person owns the template, the CI configuration and the runbook for shared infrastructure.
- Prefer managed services. Every self-hosted component is a system you must patch and support.
- Write down what is shared and who to ask in the README of one repository.

### Standard

- A platform team with a product owner, a public roadmap and a support channel answered within 1 working day.
- A software catalogue holds every service with owner, lifecycle, dependencies, APIs, runbook and dashboards. Use the [catalogue entry template](../../templates/docs/service-catalog-entry.yaml). Aim for 100% of production services registered.
- Self-service creation for the common requests in the outcomes list.
- Platform changes that affect other teams go through an [RFC](../architecture/rfcs.md).
- Quarterly platform review: adoption, SLOs, survey results, top support topics, next quarter's plan.
- **Break-glass deploy path.** A documented way to deploy the previous signed artifact that does not depend on CI, for example a pull request to the GitOps repository applied by the in-cluster agent, or a written manual procedure with logged access. Test it in the quarterly rollback drill (see [rollbacks](../reliability/rollbacks.md)).

### Assured

- The platform is where controls live: separation of environments, approvals, signing, scanning, logging. Each control produces evidence automatically, listed in [control mapping](../compliance/control-mapping.md). This supports ISO/IEC 27001:2022 Annex A 8.31 (separation of development, test and production environments) and 8.32 (change management).
- Platform administrators are a small, named group with just-in-time access and logged sessions (see [access control](../security/access-control.md)).
- The platform has its own disaster recovery plan and tested restores (see [backup and recovery](../reliability/backup-and-recovery.md)).
- Vendors and open source projects in the platform have a written exit plan (see [cloud, on-premises and air-gapped](cloud-on-prem-air-gapped.md)).

## Measuring the platform

| Dimension | Measure |
|---|---|
| Adoption | Share of services using each capability. Share of requests completed through self-service rather than tickets. |
| Speed | Time to first deploy of a new service. Lead time for a self-service request. |
| Reliability | Platform SLO attainment. Incidents caused by platform changes. |
| Satisfaction | Survey every 6 months, same questions each time, with free text. |
| Effect on delivery | The [DORA metrics](../measurement/metrics.md) of teams on the platform, compared with their own earlier baseline, not with other teams |

## Cloud, on-premises and air-gapped

The platform is where hosting differences are absorbed, so product teams see the same interface everywhere. On-premises, the platform team runs components that a cloud provider would otherwise manage, and needs staff and budget for it. Air-gapped platforms add package mirrors, internal registries, offline vulnerability data, update media transfer and internal time and certificate services. The full comparison is in [cloud, on-premises and air-gapped](cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Building a platform for 15 engineers | Managed services plus one template. Revisit at 3+ teams. |
| Platform team as a ticket queue | Self-service first. Track tickets as a signal of missing self-service. |
| Platform designed without users | User interviews, a pilot team, and satisfaction measured every 6 months. |
| Mandating the platform before it is good | Make it optional and better. Adoption is the test of whether it is good. |
| Portal built before the capabilities behind it | Capabilities first. A portal on top of manual steps is a slower ticket form. |
| Platform team owns everything, including product teams' services | The platform runs the platform. Teams own and operate their services. |
| Deploy pipeline held only to working hours | Hold the rollback path to the highest tier it deploys, 24/7, with a break-glass path. |

## Templates

- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml)
- [RFC template](../../templates/docs/rfc.md)

## Sources

- CNCF Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/
- CNCF Platform Engineering Maturity Model: https://tag-app-delivery.cncf.io/whitepapers/platform-eng-maturity-model/
- Matthew Skelton and Manuel Pais, Team Topologies (2019): https://teamtopologies.com/
- Backstage software catalogue: https://backstage.io/docs/features/software-catalog/
- DORA research: https://dora.dev/research/
