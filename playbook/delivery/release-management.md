# Release management

Deploy small changes often and release them to users gradually, so that each release is low risk and easy to undo. When something goes wrong, roll back first and investigate second. Use scheduled release trains only for software that customers install themselves, and publish a support policy that says how long each version gets fixes.

## Outcomes

Starting targets. Compare them with the DORA delivery metrics in [metrics](../measurement/metrics.md).

| Signal | Starting target (services you run) | Starting target (software customers install) |
|---|---|---|
| Deployment frequency | At least daily per service | One release train every 2 to 6 weeks, patches as needed |
| Change lead time (merge to production) | Under 1 day | Under one train interval |
| Change fail rate | Under 15% | Under 15% of releases need a patch |
| Failed deployment recovery time | Under 1 hour | Patch release within 5 working days, or within 72 hours for actively exploited vulnerabilities (P0 in [vulnerability management](../security/vulnerability-management.md)) |
| Rollback decision after a release alarm | Within 15 minutes | Workaround or advisory to customers within 1 working day |
| Release notes published with every release | 100% | 100% |

## Continuous delivery or scheduled releases

| Model | Fits | How it works |
|---|---|---|
| Continuous deployment | SaaS, internal services, websites | Every merge to `main` that passes CI deploys to production automatically, behind flags where needed |
| Continuous delivery | Services where a human picks the moment, regulated services | Every merge produces a deployable artifact; a person promotes it with one action |
| Release train | On-premises software, mobile apps, firmware, products with many integrators | A release leaves on a fixed schedule with whatever is ready; late work waits for the next train |
| Long Term Support line | Software with enterprise or public-sector customers who upgrade slowly | Selected releases get security and critical fixes for a published period |

Default: continuous delivery for anything you operate yourself. Pick release trains only when customers control when they upgrade.

## Practice

### Foundation

- **Automate the deploy.** One command or one button deploys a given artifact version to an environment. No hand-edited servers.
- **Version every artifact** and tag every release in Git. See [versioning and changelogs](versioning-and-changelogs.md).
- **Rollback first.** If a release causes a user-visible regression, roll back to the previous artifact, then debug. Fix forward only when rollback is impossible (for example after an irreversible data change) or the fix is smaller and faster than the rollback. Practise rollback at least once a quarter so it works when you need it.
- **Deploy and release are separate.** Deploying puts code on servers. Releasing turns behaviour on for users. Use [feature flags](feature-flags.md) to release gradually and turn off fast.
- **Release notes for every release.** Generate them from Conventional Commits with release-please and edit the result for humans.
- **Use a checklist** for anything not yet automated: [release checklist](../../templates/docs/release-checklist.md). Automate one checklist item per month until the list is short.

### Standard

- **Progressive delivery.**
  - **Canary.** Send a small share of traffic to the new version (for example 1%, then 10%, 50%, 100%), compare error rate and latency against the old version, and stop automatically if the new version is worse. Each step waits long enough to see real traffic (for example 10 minutes at low volume).
  - **Blue-green.** Run the new version next to the old one, switch traffic at the load balancer, keep the old version warm for fast switch-back. Costs double capacity during the switch.
  - **Rolling.** Replace instances in batches with health checks. Simple, but rollback is slower and both versions run at once.
  - Whatever the method, both versions run together for a while, so every change must be backward compatible. See [database changes](database-changes.md).
- **Automated release gates** based on [service levels](../reliability/service-levels.md): stop promotion when the error budget burn rate is high.
- **Release notes** in the changelog and, for user-facing products, in plain language for customers.
- **Freeze windows: minimise them.** A freeze builds up a batch of changes that then ship together, which raises risk. Prefer slowing down (smaller canary steps, more approvals) over stopping. If the business needs a freeze (for example a national tax deadline or peak trading), keep it short (a few days, and no more than 2 weeks), allow security and incident fixes through an exception process, and plan a gentle restart with small batches.
- **Deployment records.** Every production deployment is logged with version, time, who or what triggered it, and the change it contains. Link this to [change management](../reliability/change-management.md).

### Assured

- **Approved artifact only.** Production deploys only signed artifacts built by CI, verified at deploy time against provenance. See [supply chain](../security/supply-chain.md).
- **Separation of duties.** The person who wrote a change does not approve its production release. Automated deployment after a two-person reviewed merge can meet this; agree that with your auditor and record it.
- **Change records** link pull requests, approvals, test evidence and deploy logs. This gives evidence for ISO/IEC 27001:2022 Annex A 8.32 and SOC 2 CC8.1.
- **Pre-agreed rollback criteria** in each change record: which metric, which threshold, who decides.
- **Customer notice periods** where contracts or regulators require them, published in the support policy.

## Release trains for shipped software

- Fixed cadence (for example every 4 weeks). The date does not move; scope does.
- Cut `release/x.y` from `main` on train day. Only bug fixes cherry-picked from `main` go onto it. See [source control](source-control.md#when-a-release-branch-is-justified).
- Release candidates (`x.y.0-rc.1`) go to internal and pilot customers for 1 to 2 weeks.
- Test install, upgrade from each supported version, and rollback or downgrade on each supported platform.
- Ship signed packages, checksums, SBOM and release notes together.

## Long Term Support policy

For software customers install, publish a support policy before the first customer asks. A starting policy:

| Item | Starting policy |
|---|---|
| LTS cadence | One LTS release every 12 months |
| LTS support period | 24 months of security and critical fixes |
| Non-LTS releases | Supported until the next release, plus 1 month |
| Supported LTS lines at once | At most 2 |
| End-of-life notice | At least 6 months, in release notes and by direct notice to customers |
| Upgrade path | Direct upgrade from the previous LTS to the current LTS is tested and documented |
| Security fixes | Back-ported to every supported line |

Every extra supported line multiplies test and back-port effort. Keep the count low and say so in contracts.

## In the AI era

An AI feature can change behaviour without a code change. Prompts, model versions, retrieval indexes, tool definitions and safety filters are all release artifacts.

- **Version each one.** Prompts and tool definitions live in the repository. The model is referenced by an exact version, never an alias that the provider can move. A retrieval index has a build identifier that names its source data snapshot and embedding model.
- **Release them through the pipeline.** A change to any of them passes the evaluation gate in CI (see [continuous integration](continuous-integration.md#in-the-ai-era)), gets a changelog entry and a deployment record, like code.
- **Canary them.** Send a small share of traffic to the new prompt, model or index and compare evaluation scores, user feedback signals, refusal rate, latency and cost per request against the current version before going further.
- **Keep the previous version ready.** Rolling back means switching to the previous prompt version, model version or index build within the same 15-minute limit as code (see [rollbacks](../reliability/rollbacks.md)). Keep the previous index built and loadable; rebuilding an index during an incident can take hours.
- **Plan for provider retirement.** Hosted models are retired on the provider's schedule. Track retirement dates, and test the replacement version against your evaluation set before you are forced to switch.

See [AI engineering practices](../ai/ai-engineering-practices.md) and [AI architecture patterns](../ai/ai-architecture-patterns.md).

## Cloud, on-premises and air-gapped

- Customers on air-gapped networks need offline bundles: packages, container images, checksums, signatures, SBOM and release notes in one archive, plus the public key or certificate to verify them.
- Publish a verification procedure that works without internet access (cosign with a key pair, or GPG).
- Internal deployments in air-gapped networks use GitOps tools (Argo CD or Flux) that pull from an internal Git server and registry.
- Under the EU Cyber Resilience Act, manufacturers of products with digital elements must report actively exploited vulnerabilities from 11 September 2026 (early warning within 24 hours, notification within 72 hours). Your release process must be able to ship a security fix fast. See [vulnerability management](../security/vulnerability-management.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Monthly "big bang" release of a service you run | Deploy daily behind flags. |
| Debugging in production for an hour before rolling back | Rollback first. Pre-agree rollback criteria. |
| Rollback never tested | Quarterly rollback drill. |
| Six-week holiday freeze | Short freeze with an exception path, or slow down instead of stopping. |
| Release notes copied from commit messages nobody can read | Conventional Commits plus a human edit. |
| Five LTS lines, each patched by hand | Publish a policy with at most 2 lines. |

## Templates

- [Release checklist](../../templates/docs/release-checklist.md)
- [release-please workflow](../../templates/github/workflows/release-please.yml) and [config](../../templates/github/release-please-config.json)
- [CHANGELOG.md](../../templates/repo/CHANGELOG.md)
- [Production readiness review](../../templates/docs/production-readiness-review.md)

## Sources

- DORA metrics: https://dora.dev/guides/dora-metrics-four-keys/
- Google SRE book, release engineering: https://sre.google/sre-book/release-engineering/
- Google SRE workbook, canarying releases: https://sre.google/workbook/canarying-releases/
- Martin Fowler, blue-green deployment: https://martinfowler.com/bliki/BlueGreenDeployment.html
- release-please: https://github.com/googleapis/release-please
- EU Cyber Resilience Act: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
