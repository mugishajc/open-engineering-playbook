# Environments

Keep as few long-lived environments as you can (usually development, staging and production), make them differ only in size and data, and deploy the same artifact to each one. Use short-lived preview environments per pull request for review and testing, and keep production personal data in production. Every difference between staging and production is a place where a bug can hide.

## Outcomes

Starting targets. Tune them to your platform.

| Signal | Starting target |
|---|---|
| Environments created from infrastructure as code | 100% |
| Artifacts rebuilt per environment | Zero; one artifact is promoted |
| Configuration differences between staging and production outside a reviewed list | Zero |
| Preview environment ready after a pull request opens | Under 15 minutes |
| Preview environments older than their time to live | Zero; default time to live 72 hours after last push |
| Copies of production personal data outside production without an approved record | Zero |

## Practice

### Foundation

- **Three environments at most to start:** local development, one shared pre-production (staging), production. Each extra long-lived environment costs maintenance and drifts.
- **Build once, deploy many.** CI builds one artifact per commit. Staging and production run the same image digest or package checksum. Configuration comes from the environment, not from the build.
- **Configuration in the environment.** Use environment variables or a configuration service. Secrets come from a secret manager, never from the repository. See [secrets](../security/secrets.md).
- **Local development in containers** or a dev container definition, so a new engineer can run the service on day one. See [onboarding](../people/onboarding.md).
- **No production data in development or staging.** See the data rules below.
- **Separate accounts or projects** for production and non-production, so a mistake in staging cannot touch production.

### Standard

- **Infrastructure as code** for every environment (Terraform or OpenTofu, Pulumi, Helm, Kustomize or similar), reviewed like application code. Drift detection runs daily and alerts the owner.
- **Parity list.** Write down every intended difference between staging and production (size, replica count, external integrations in sandbox mode, data). Anything not on the list is a defect.
- **Same major versions** of the database, cache, queue, runtime and operating system in every environment.
- **Ephemeral preview environments.**
  - Created automatically for each pull request that changes deployable code.
  - Seeded with synthetic data.
  - Linked from the pull request so reviewers, designers and product owners can try the change.
  - Destroyed when the pull request merges or closes, or after 72 hours without a push.
  - Cost tagged by team. Set a monthly budget per team and alert at 80%.
- **Promotion is automated.** A change moves from staging to production by promoting the same artifact, not by redeploying from source. See [release management](release-management.md).
- **Staging is not a test bed for every team at once.** Run integration tests in CI with containers; use staging for final checks against real integrations.

### Assured

- **Separation of environments** is a documented control: separate accounts, networks, credentials and access groups for development, test and production. Engineers do not have standing write access to production. See [access control](../security/access-control.md). This maps to ISO/IEC 27001:2022 Annex A 8.31.
- **Change evidence** for every production deploy (see [change management](../reliability/change-management.md)).
- **Test information control** for any data derived from production, mapped to ISO/IEC 27001:2022 Annex A 8.33.
- **Data residency.** Where law or contract requires data to stay in a country or region, every environment that holds real data runs in that location, including backups and logs.

## Production data rules

| Rule | Detail |
|---|---|
| Default | Production personal data stays in production. |
| Synthetic first | Generate test data from code or factories. Version it with the tests. |
| Masked copies | Only through an approved, automated masking pipeline. Direct identifiers removed or irreversibly transformed; indirect identifiers checked. |
| Approval | Data owner and data protection officer (or delegate) approve each copy, with purpose and deletion date. |
| Access | Same or stricter access controls as production. Logged. |
| Deletion | Copies deleted on the recorded date, at most 30 days after creation as a starting point. |
| Debugging production issues | Debug in production with audited, time-limited access, rather than copying data out. |

Data protection laws apply to test copies that still identify people. Examples include EU GDPR, UK GDPR, Kenya Data Protection Act 2019, Rwanda Law No 058/2021 on personal data protection, Nigeria Data Protection Act 2023, Brazil LGPD, India DPDP Act 2023 and California CCPA/CPRA. This is not legal advice.

## Cloud, on-premises and air-gapped

- On-premises, use separate clusters or at least separate namespaces with network policies and separate credentials per environment. Prefer separate clusters for production.
- Preview environments on-premises need spare capacity. Use a shared cluster with quotas per namespace, and a short time to live.
- In air-gapped networks, staging must use the same internal mirrors and registry as production, so a missing dependency shows up in staging first.
- For software customers install, keep a test lab that matches each supported customer platform. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Six long-lived environments (dev, test, QA, UAT, pre-prod, prod) | Collapse to staging plus previews. |
| Rebuilding the image for production | Promote the tested digest. |
| Staging on a different database version | Same major versions everywhere. Parity list. |
| Nightly copy of production into staging | Synthetic data or approved masking with deletion dates. |
| Preview environments nobody deletes | Time to live and automatic clean-up. |
| Shared admin credentials across environments | Separate credentials and accounts per environment. |

## Templates

- [Production readiness review](../../templates/docs/production-readiness-review.md)
- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml)
- [Release checklist](../../templates/docs/release-checklist.md)

## Sources

- The Twelve-Factor App, dev/prod parity: https://12factor.net/dev-prod-parity
- The Twelve-Factor App, config: https://12factor.net/config
- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
- Development Containers specification: https://containers.dev/
- OpenTofu documentation: https://opentofu.org/docs/
