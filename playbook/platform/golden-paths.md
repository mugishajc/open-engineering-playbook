# Golden paths

Give teams a supported, ready-made way to build and run the common kinds of software: a service template, a pipeline, a deployment target and the observability and security controls already wired in. Make it the easiest route, not the only one. Teams that follow the path get speed and support for free, and teams that leave it can, as long as they own the extra work and write down why.

## Outcomes

Starting points. Tune them to your organisation.

- A team goes from "we need a new service" to a running, monitored service in a non-production environment in under 1 working day.
- At least 80% of new services in the last 12 months started from a golden path template.
- At least 70% of services are on a template version less than 6 months old.
- Developer satisfaction with the golden path, measured by survey every 6 months, scores at least 4 out of 5 on average, with the trend reported.
- Every service that is off the path has an [ADR](../architecture/decision-records.md) saying why.

## What a golden path contains

A golden path is opinionated, documented and maintained. For a typical backend service it includes:

| Part | Contents |
|---|---|
| Repository skeleton | Language and framework from the Adopt ring of the [tech radar](../architecture/tech-radar.md), linter and formatter config, `.editorconfig`, pre-commit hooks |
| Build and CI | Pipeline with tests, dependency and secret scanning, SBOM and signing (see [supply chain](../security/supply-chain.md)) |
| Container and deploy | Hardened base image from the internal registry, deployment manifests, environment configuration |
| Observability | OpenTelemetry, structured logs, health endpoints, dashboard and default alerts (see [observability](../architecture/observability.md)) |
| Operations | Runbook stub, SLO stub, on-call routing, catalogue entry |
| Governance | `CODEOWNERS`, branch rules, `docs/decisions/` with the ADR template, `SECURITY.md` |
| Documentation | README following the [documentation](../people/documentation.md) standard, a "how this template works" page |

Build separate paths only for kinds of software you create often: backend service, web front end, data pipeline, scheduled job, library. Three good paths beat ten neglected ones.

## Paved roads, not cages

- The path is the default, not a mandate. Teams may leave it when they have a real reason.
- Leaving the path means the team owns what the path would have given them: patching, scanning, pipeline upkeep, on-call tooling.
- Security and compliance controls are the exception. Those are required whatever route a team takes. The path is the cheapest way to meet them.
- When several teams leave the path for the same reason, the path is wrong. Fix it.

## Practice

### Foundation

- One template repository per kind of software you build. Mark it as a template on your git host, or use a scaffolding tool such as Cookiecutter or Copier.
- The template passes CI on its own, deploys to a test environment and has a README explaining every file.
- One person owns each template and updates it at least once a quarter.

### Standard

- A platform team owns the golden paths as products (see [developer platform](developer-platform.md)), with a roadmap and a support channel.
- New services are created through self-service: a portal form (for example Backstage Software Templates) or a command-line tool. Creation also registers the service in the catalogue with a [catalogue entry](../../templates/docs/service-catalog-entry.yaml).
- Templates can be updated after creation. Use a scaffolding tool that can apply template changes to existing repositories (Copier supports this), or ship shared parts as versioned libraries and reusable CI components that dependency bots can update.
- Report adoption every quarter: share of new services from templates, template version spread, time to first deploy.
- Survey developers every 6 months with 5 to 10 fixed questions so the trend is comparable.

### Assured

- The golden path is the documented, audited route to production. Controls built into it (scanning, signing, approvals, separation of environments) are listed with the evidence each one produces, mapped in [control mapping](../compliance/control-mapping.md).
- Services off the path go through a fuller [production readiness review](../reliability/production-readiness.md) and an exception record with an owner and an expiry date.
- Template changes that affect controls go through [change management](../reliability/change-management.md) and are versioned, so an auditor can see which controls a service had on a given date.

## Measuring adoption and satisfaction

| Measure | How to collect | Watch for |
|---|---|---|
| New services from a template | Catalogue entries with a template annotation, or repository creation logs | Below 80%: find out why teams avoid it |
| Template version spread | Version file written into each repository at creation | Long tail of old versions means updates are too hard |
| Time to first deploy | Timestamp of repository creation to first successful deploy | Rising time means the path is getting heavier |
| Developer satisfaction | Survey, 1 to 5 scale, plus one free-text question | Comments matter more than the score |
| Support load | Questions per week in the platform channel, grouped by topic | Repeated questions point at missing docs or a missing feature |

Never use adoption numbers to rank teams. Low adoption is feedback for the platform, not a failing of the team.

## Cloud, on-premises and air-gapped

- Templates must build entirely from internal mirrors in air-gapped networks: base images from the internal registry, packages from internal proxies, CI actions or components vendored. Test this by building the template on a network with no internet access.
- Keep one template per kind of software, with the hosting target as a parameter, rather than separate cloud and on-premises templates that drift apart.
- See [cloud, on-premises and air-gapped](cloud-on-prem-air-gapped.md) for the tooling options behind each part.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Path is mandatory and slow, so teams route around it in secret | Make it optional and faster than the alternative. Measure time to first deploy. |
| Template is copied once and never updated | Use update-capable scaffolding or shared libraries. Track version spread. |
| Ten paths, all half-finished | Fewer paths, each owned, documented and tested. |
| Path built without talking to the teams who use it | Interview 3 to 5 teams before building. Run a pilot with one team. |
| Security controls bolted on outside the path | Put the controls in the path, so following it is how teams comply. |

## Templates

- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml)
- [ADR template](../../templates/docs/adr.md), for teams leaving the path
- [Production readiness review](../../templates/docs/production-readiness-review.md)

## Sources

- Backstage Software Templates: https://backstage.io/docs/features/software-templates/
- CNCF Platforms White Paper: https://tag-app-delivery.cncf.io/whitepapers/platforms/
- Copier documentation (template updates): https://copier.readthedocs.io/
- Matthew Skelton and Manuel Pais, Team Topologies (2019): https://teamtopologies.com/
