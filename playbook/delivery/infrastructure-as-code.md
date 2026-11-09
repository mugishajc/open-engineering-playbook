# Infrastructure as code

The problem: "Nobody knows how production was built, and rebuilding it would take weeks." Infrastructure created by hand in a console cannot be reviewed, repeated or audited. Define infrastructure in code, review every change through a pull request that shows the plan, keep state remote, locked and encrypted, and check policy automatically before apply. Choose the tool by your team and targets; the practices matter more than the tool.

## Outcomes

Starting targets. Tune them to your estate.

| Signal | Starting target |
|---|---|
| Production infrastructure managed by code | 100% of new resources; existing resources imported within 12 months |
| Infrastructure changes applied from a pipeline, not a laptop | 100% at Standard |
| Pull requests with the plan output attached for review | 100% |
| Drift detected between code and live infrastructure | Checked daily, resolved within 1 working day |
| Policy checks run before apply | 100% at Standard |
| Time to rebuild a non-production environment from code | Under 1 day, tested twice a year |

## Choosing a tool

| Tool | Model | Fits | Watch out for |
|---|---|---|---|
| Terraform | Declarative HCL, plan and apply, large provider catalogue | Multi-cloud and SaaS resources | Licence changed to the Business Source License in August 2023; check that your use is allowed |
| OpenTofu | Open source fork of Terraform under the Linux Foundation, compatible language | Same as Terraform, with an open source licence | Check provider and feature compatibility for your version |
| Pulumi | General-purpose languages (TypeScript, Python, Go, C#, Java) | Teams who want loops, types and tests in a familiar language | Discipline to keep code declarative and readable |
| Crossplane | Kubernetes controllers that manage cloud resources as custom resources | Platforms that already run Kubernetes and GitOps | Requires a reliable management cluster |
| Cloud-native tools (CloudFormation, AWS CDK, Azure Bicep, Google Cloud Infrastructure Manager) | Provider-specific | Single-cloud estates | Lock-in to one provider |
| Ansible and similar | Configuration management, procedural | Servers and network devices on-premises | Not a replacement for declarative provisioning |

Record the choice in a [decision record](../architecture/decision-records.md) and see [build, buy or adopt](../strategy/build-buy-adopt.md).

## Practice

### Foundation

- **Everything in code.** New infrastructure is created only through code in a repository. Console changes are for reading, not writing.
- **Remote state with locking.** Store state in a remote backend that supports locking and encryption at rest (an object store bucket with versioning, or a managed backend). Never commit state to Git.
- **State is a secret.** State can contain passwords, keys and connection strings. Restrict access to the people and pipelines that need it, and turn on versioning so you can recover a bad state.
- **Secrets out of code and state where possible.** Read secrets at run time from a secret manager (Vault, OpenBao or a cloud secret manager) instead of passing them through the IaC tool. Where a value must pass through, mark it sensitive and use your tool's features that avoid writing it to state, where available. See [secrets](../security/secrets.md).
- **Pin versions** of the tool, providers and modules, and commit the lock file.
- **Format and validate in CI** (`fmt`, `validate`, a linter such as TFLint).

### Standard

- **Plan in the pull request.** CI runs `plan` for each changed root module and posts the output to the pull request. Reviewers read the plan, especially every `destroy` and `replace`. Tools such as Atlantis or your CI platform can do this.
- **Apply from the pipeline after merge**, using the plan that was reviewed, with a short-lived identity (OIDC federation, no long-lived keys). See [continuous integration](continuous-integration.md).
- **Small root modules.** Split state by environment and by blast radius (network, data, compute, per service). A plan that touches hundreds of resources is hard to review and slow to lock.
- **Reusable modules** with versioned releases, inputs validated, and examples. Keep a small internal module registry. Teams consume modules through [golden paths](../platform/golden-paths.md).
- **Policy as code before apply.** Check plans against rules with Open Policy Agent (Conftest), or a scanner such as Checkov or Trivy: no public storage buckets, encryption on, required tags, approved regions only. For Kubernetes resources, enforce at admission with Kyverno or OPA Gatekeeper.
- **Drift detection.** Run `plan` on a schedule (daily) against each root module. Any diff raises an alert to the owning team. Either import the manual change into code or revert it.
- **Tag everything** with owner, service, environment and cost centre, enforced by policy. See [FinOps](../platform/finops.md).
- **Protect destructive changes.** Use lifecycle rules that prevent destroying data stores, and require a second approver for plans that destroy stateful resources.

### Assured

- **Separation of duties.** The author of an infrastructure change cannot approve it. The pipeline applies; people do not hold standing admin rights in production accounts.
- **Evidence.** Keep the pull request, the reviewed plan, policy results and apply log for each change. This supports ISO/IEC 27001:2022 Annex A 8.9 (configuration management) and 8.32 (change management), and SOC 2 CC8.1.
- **Policy exceptions** are recorded with an owner and an expiry date, in code, so auditors can see them.
- **Data residency.** Policy restricts regions and locations to those allowed by law and contract.

## Cloud, on-premises and air-gapped

- On-premises, IaC manages virtualisation platforms, Kubernetes, network devices, DNS and load balancers through their providers, and servers through configuration management.
- In air-gapped networks, run a provider and module mirror inside the network (the IaC tool's network mirror or a filesystem mirror), and pin versions with checksums. New providers enter through the reviewed import process.
- State backends must be inside the network: an S3-compatible object store (for example MinIO or Ceph), a database backend, or GitLab's managed Terraform state.
- Test disaster recovery by rebuilding an environment from code and backups in an isolated network at least once a year. See [backup and recovery](../reliability/backup-and-recovery.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Click-ops" in production, IaC only for new projects | Import existing resources. Remove write access from the console. |
| One giant state file for everything | Split by environment and blast radius. |
| State file in Git with secrets in it | Remote encrypted backend. Rotate exposed secrets. |
| Apply from a laptop with admin keys | Pipeline apply with short-lived identity. |
| Reviewing the code diff but not the plan | Plan posted to the pull request and read. |
| Modules copied and edited per team | Versioned shared modules with releases. |

## Templates

- [CI workflow](../../templates/github/workflows/ci.yml)
- [CODEOWNERS (infrastructure paths)](../../templates/github/CODEOWNERS)
- [Pre-commit hooks](../../templates/repo/.pre-commit-config.yaml)

## Sources

- OpenTofu documentation: https://opentofu.org/docs/
- Terraform documentation: https://developer.hashicorp.com/terraform/docs
- Pulumi documentation: https://www.pulumi.com/docs/
- Crossplane documentation: https://docs.crossplane.io/
- Open Policy Agent: https://www.openpolicyagent.org/docs/latest/
- Conftest: https://www.conftest.dev/
- Kyverno: https://kyverno.io/docs/
- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
