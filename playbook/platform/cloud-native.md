# Cloud native

"We moved to Kubernetes and now we spend more time on the cluster than on the product." Package software as containers, build it to the Twelve-Factor principles, and pick the simplest runtime that meets your needs: a PaaS or serverless platform when you can, Kubernetes when you need its control or must run the same way on-premises and air-gapped, and plain VMs when the software demands them. Add a service mesh, multiple clusters or multiple regions only when a measured need justifies the operating cost.

## Outcomes

Starting points. Tune them to your organisation.

- 100% of new services are built as signed container images (or functions) from the [golden path](golden-paths.md).
- Every service passes the Kubernetes Pod Security Standards "restricted" profile, or has a recorded exception.
- Cluster upgrades stay within the supported Kubernetes versions at all times (the project supports roughly the three most recent minor releases).
- A node or zone failure causes no user-visible outage for services with an SLO of 99.9% or higher.
- The platform team spends less than 30% of its time on unplanned cluster work, measured quarterly.

## Choose the runtime

| Runtime | Choose it when | Watch out for |
|---|---|---|
| PaaS (managed app platform) | Small team, standard web or API workloads, public cloud allowed | Platform limits, vendor lock-in, cost at scale |
| Serverless functions and containers | Spiky or event-driven load, short tasks | Cold starts, execution time limits, harder local testing |
| Managed Kubernetes | Several teams and services, need for portability or fine control | Cluster upgrades, add-on sprawl, skills |
| Self-managed Kubernetes | On-premises, sovereign or air-gapped hosting | You run the control plane, upgrades and certificates |
| Virtual machines | Software that cannot be containerised, licensing tied to hosts, single large stateful systems | Patching, configuration drift; manage with infrastructure as code |

Record the choice per workload in an [ADR](../architecture/decision-records.md). For an organisation with fewer than about 3 teams, Kubernetes is rarely the cheapest answer unless you must run on-premises. Kubernetes skills are scarce: plan how you will build them before you commit (see [skills gap](../people/skills-gap.md)).

## Twelve-Factor in practice

The Twelve-Factor App sets out how to build services that deploy cleanly anywhere. The factors that cause the most trouble when ignored:

- **Config in the environment.** No environment-specific values in the image. The same image runs in test and production.
- **Backing services as attached resources.** Databases and queues are addressed by configuration, so they can be swapped.
- **Stateless processes.** Session and file state live in backing services, so any instance can be killed or added.
- **Disposability.** Start in seconds, shut down gracefully on SIGTERM, finish or hand back in-flight work.
- **Logs as event streams.** Write to standard output. The platform collects them (see [observability](../architecture/observability.md)).
- **Dev and prod parity.** Keep environments close (see [environments](../delivery/environments.md)).

## Kubernetes baseline

Every workload on Kubernetes starts from the [service baseline template](../../templates/platform/k8s-service-baseline.yaml):

- Runs as non-root with a read-only root filesystem, all Linux capabilities dropped, no privilege escalation, and the runtime default seccomp profile.
- Resource requests and limits set from measurement, not guesses. Review after 2 weeks in production.
- Readiness, liveness and startup probes that reflect real health.
- At least 2 replicas spread across nodes or zones, a PodDisruptionBudget and a HorizontalPodAutoscaler.
- NetworkPolicy that denies all traffic by default and allows only what the service needs.
- Deployed by GitOps (see [GitOps and deployment](../delivery/gitops-and-deployment.md) and the [Argo CD application template](../../templates/platform/argocd-application.yaml)). Nobody runs `kubectl apply` against production by hand.
- Cluster configuration managed as code (see [infrastructure as code](../delivery/infrastructure-as-code.md)).

## Service mesh, multi-cluster and multi-region

- **Service mesh** (for example Istio or Linkerd) gives mutual TLS between services, traffic shifting and uniform telemetry. Adopt it when you need mutual TLS everywhere or fine traffic control across many services, and can staff it. Do not add it for observability alone: OpenTelemetry covers that.
- **Multi-cluster** separates failure domains, environments, tenants or compliance scopes. Manage clusters as cattle with infrastructure as code and GitOps, so a cluster can be rebuilt from git.
- **Multi-region** active-active is expensive and hard for stateful systems. Start with one region and tested restore into another. Go active-active only for services whose SLO or regulator requires it.

## Practice

### Foundation

- Containerise with a minimal base image from a trusted source. Build to Twelve-Factor.
- Use a PaaS or a managed container service unless you must run on-premises.
- One environment per stage, deployed from CI.

### Standard

- Kubernetes (managed where allowed) as the default runtime for services, with the baseline template enforced by admission policy (for example Kyverno or OPA Gatekeeper).
- Pod Security Standards "restricted" enforced per namespace. Exceptions recorded.
- GitOps for all deployments. Clusters rebuilt from code at least twice a year as a test.
- Kubernetes minor version upgrades at least every 6 months.
- CNCF projects as building blocks where they fit: for example Prometheus, OpenTelemetry, Argo CD or Flux, cert-manager, Harbor. Treat each as a dependency with an owner.

### Assured

- Admission control verifies image signatures and provenance before any pod starts (see [supply chain](../security/supply-chain.md)).
- Cluster configuration is benchmarked against a published hardening guide (for example the CIS Kubernetes Benchmark) every quarter, with results kept.
- Audit logging is on for the Kubernetes API server, shipped off-cluster and retained per your records policy.
- Production and non-production run on separate clusters, with separate administrator groups.

## Cloud, on-premises and air-gapped

- On public cloud, use the provider's managed Kubernetes and keep workloads portable through standard APIs.
- On-premises, choose a supported distribution, for example k3s for small or edge sites, RKE2 or Red Hat OpenShift for larger estates. Budget for the people who will run upgrades, storage, networking and certificates.
- Air-gapped, every image, chart, operator and add-on comes from the internal registry. Configure the container runtime to pull only from internal mirrors. Test a full cluster install and upgrade with egress blocked. See [cloud, on-premises and air-gapped](cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Kubernetes for one small team with three services | PaaS or managed containers until the need is real. |
| Images that differ per environment | One image, configuration from the environment. |
| Pods running as root with writable filesystems | Baseline template plus admission policy. |
| Service mesh installed "for the future" | Adopt when a measured need exists and someone owns it. |
| Hand-edited clusters nobody can rebuild | Infrastructure as code and GitOps. Rebuild drills. |
| Falling several Kubernetes versions behind | Scheduled upgrades every 6 months at least. |

## Templates

- [Kubernetes service baseline](../../templates/platform/k8s-service-baseline.yaml)
- [Argo CD application](../../templates/platform/argocd-application.yaml)
- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml)

## Sources

- The Twelve-Factor App: https://12factor.net/
- Kubernetes documentation: https://kubernetes.io/docs/
- Kubernetes version skew and support policy: https://kubernetes.io/releases/
- Kubernetes Pod Security Standards: https://kubernetes.io/docs/concepts/security/pod-security-standards/
- CNCF projects: https://www.cncf.io/projects/
- CIS Kubernetes Benchmark: https://www.cisecurity.org/benchmark/kubernetes
