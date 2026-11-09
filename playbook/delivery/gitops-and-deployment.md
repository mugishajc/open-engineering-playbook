# GitOps and deployment

The problem: "Deploys are manual, every environment is a little different, and a bad change reaches every server at once." Describe what should run in each environment in Git, let an agent inside the environment pull and apply it, and roll every change out in stages (canary or blue-green) with automatic checks that stop a bad rollout. Apply the same staged rollout to configuration and content, not only to code.

## Outcomes

Starting targets. Tune them to your platform.

| Signal | Starting target |
|---|---|
| Production changes applied through Git, not by hand | 100%, outside logged break-glass |
| Time from merge of an environment change to applied in that environment | Under 10 minutes |
| Drift between Git and a running environment | Detected within 15 minutes, resolved within 1 working day |
| Production rollouts that use staged delivery with automatic analysis | 100% of user-facing services at Standard |
| Configuration and content changes rolled out in stages | 100% for anything that can stop the service |
| Rollback time (decision to previous version serving traffic) | Under 5 minutes |

## GitOps in four principles

OpenGitOps (a CNCF working group) defines GitOps by four principles:

1. **Declarative.** The desired state of the system is expressed declaratively.
2. **Versioned and immutable.** Desired state is stored so that it keeps a complete version history.
3. **Pulled automatically.** Software agents pull the desired state from the source.
4. **Continuously reconciled.** Agents observe the actual state and try to apply the desired state.

Argo CD and Flux are the two common Kubernetes implementations. Both run inside the cluster and pull from Git, so CI never needs credentials to production.

## Deployment strategies

| Strategy | How | Cost | Use when |
|---|---|---|---|
| Recreate | Stop old, start new | Downtime | Batch jobs, dev environments only |
| Rolling | Replace instances in batches with health checks | Low | Default for stateless services with good health checks |
| Blue-green | Run new next to old, switch traffic, keep old warm | Double capacity during switch | Fast, all-at-once switch with instant switch-back |
| Canary | Send a small share of traffic to the new version, compare, then increase | Needs traffic splitting and metrics | User-facing services with enough traffic to compare |
| Progressive delivery | Canary or blue-green with automated metric analysis that promotes or aborts | Tooling (Argo Rollouts, Flagger) and good metrics | The Standard default for user-facing services |

Every strategy except recreate runs two versions at once, so every change must be backward compatible. See [database changes](database-changes.md).

## Practice

### Foundation

- **Deploys are code.** Every environment is described in Git (manifests, Helm values, Compose files or IaC). A person changes Git, not the server.
- **Build once, deploy many.** Environments reference an artifact by version or, better, by image digest. See [environments](environments.md).
- **Rolling deploys with health checks.** Readiness and liveness checks that test real dependencies, and a maximum unavailable count of 0 for services that must stay up.
- **Practise rollback.** Revert the Git change and let the deploy run, at least once a quarter. See [release management](release-management.md).
- **Solo and startup:** a single CI job that deploys from `main` is fine. Move to a pull-based agent when you have more than one cluster or environment to keep in sync.

### Standard

- **GitOps agent per cluster or environment** (Argo CD or Flux) with automatic sync and self-heal turned on for application workloads. Templates: [Argo CD Application](../../templates/platform/argocd-application.yaml), [Kubernetes service baseline](../../templates/platform/k8s-service-baseline.yaml).
- **Repository layout.** Keep application source and environment configuration in separate repositories, or separate directories with separate owners. Use one directory per environment (for example `envs/staging`, `envs/production`) on one branch. Avoid one branch per environment: branches drift and merges between them hide changes.
- **Promotion.** Promote by changing the image digest in the next environment's directory through a pull request, opened automatically after the previous environment passes its checks. The pull request is the record.
- **Progressive delivery.** Use Argo Rollouts or Flagger to run canary steps (for example 5%, 25%, 50%, 100%) with analysis against error rate and latency from your metrics system. Abort and roll back automatically when analysis fails.
- **Drift detection.** The agent alerts when live state differs from Git. Manual changes are reverted by self-heal or turned into a pull request within 1 working day.
- **Secrets.** Do not store plain secrets in Git. Use an external secrets operator that reads from Vault, OpenBao or a cloud secret manager, or encrypt with SOPS or Sealed Secrets. See [secrets](../security/secrets.md).
- **Sync windows** instead of freezes: block automatic production sync during agreed high-risk periods, with an override for incident fixes.

#### Staged rollout of configuration and content

In July 2024, a CrowdStrike Falcon content update crashed Windows hosts worldwide. The lesson for every team: configuration, rules, feature flags, machine learning models and content files can stop a system as surely as code. They need the same controls.

- Treat configuration and content as versioned artifacts with validation tests in CI.
- Roll them out in stages: internal hosts first, then a small share of customers, then everyone, with health checks and a pause between stages.
- Give customers who run your software control over when content updates apply, where the product allows it.
- Make every content update reversible, and test the rollback path.
- Make the code that loads content fail safe: reject malformed input and keep running on the last good version.

### Assured

- **Two-person rule on production changes.** Pull requests to production environment directories need approval from someone other than the author. See [code review](code-review.md#assured).
- **Verify before apply.** The cluster admits only signed images from your registry, checked by an admission policy (for example Kyverno or Sigstore policy-controller). See [supply chain](../security/supply-chain.md).
- **Deployment records.** The GitOps history plus the agent's sync log is your deployment record: who changed what, who approved, when it applied. Export it to your log store. This supports ISO/IEC 27001:2022 Annex A 8.32 and SOC 2 CC8.1.
- **No standing human write access** to production clusters. Break-glass access is time-limited and logged. See [access control](../security/access-control.md).

## Cloud, on-premises and air-gapped

- Pull-based GitOps suits on-premises and air-gapped networks well: the agent pulls from an internal Git server (GitLab self-managed, Gitea or Forgejo) and an internal registry (Harbor), and nothing outside needs a way in.
- Mirror Helm charts and images into the internal registry and reference them by digest.
- For edge or customer-site deployments with intermittent links, the agent keeps reconciling to the last state it pulled. Stage rollouts across sites in waves, like canaries.
- Outside Kubernetes, the same principles apply with configuration management tools (for example Ansible run from a pipeline, or a pull agent) and VM image pipelines.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| `kubectl apply` from a laptop | All changes through Git and the agent. |
| CI holds admin credentials to every cluster | Pull-based agent inside each cluster. |
| One branch per environment | One directory per environment, promotion by pull request. |
| Configuration pushed to every customer at once | Staged rollout with health checks and pause, as for code. |
| Drift alerts ignored | Self-heal on, or fix within 1 working day. |
| Canary with no automated analysis | Define metrics and thresholds; abort automatically. |

## Templates

- [Argo CD Application](../../templates/platform/argocd-application.yaml)
- [Kubernetes service baseline](../../templates/platform/k8s-service-baseline.yaml)
- [Release checklist](../../templates/docs/release-checklist.md)

## Sources

- OpenGitOps principles: https://opengitops.dev/
- Argo CD documentation: https://argo-cd.readthedocs.io/
- Flux documentation: https://fluxcd.io/flux/
- Argo Rollouts documentation: https://argoproj.github.io/argo-rollouts/
- Flagger documentation: https://docs.flagger.app/
- Kubernetes, deployments: https://kubernetes.io/docs/concepts/workloads/controllers/deployment/
- Google SRE workbook, canarying releases: https://sre.google/workbook/canarying-releases/
