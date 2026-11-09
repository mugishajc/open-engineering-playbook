# Cloud, on-premises and air-gapped

Run the same engineering practices wherever your software lives, and change only the tools underneath. Code review, signed builds, scanned dependencies, tested restores and SLOs mean the same thing on a hyperscaler, in your own data centre and on a network with no internet connection. Choose the hosting model per workload in a [decision record](../architecture/decision-records.md), prefer open standards so you can move, and keep a written, tested exit plan.

## Outcomes

Starting points. Tune them to your organisation.

- Every production workload has an ADR stating its hosting model and the conditions that would make you move it.
- The [golden path](golden-paths.md) templates build and deploy on every hosting model you support, tested at least once a quarter on each.
- Air-gapped sites meet the same fix-by times as every other site (see [vulnerability management](../security/vulnerability-management.md)): KEV-listed (P0) issues are fixed or mitigated with a pre-approved mitigation within 72 hours, and other critical (P1) issues are fixed within 7 days, through the transfer process below.
- Every critical vendor or platform has an exit plan reviewed at least once a year. At Assured, the plan is rehearsed every 2 years.
- Time on every air-gapped host stays within 100 milliseconds of the internal reference.

## Parity table

| Practice area | Public cloud | Private cloud or on-premises | Air-gapped |
|---|---|---|---|
| Source control | GitHub, GitLab.com, Bitbucket Cloud | GitHub Enterprise Server, GitLab self-managed, Bitbucket Data Center, Gitea or Forgejo | Same as on-premises, inside the enclave |
| CI | Hosted runners | Self-hosted runners on internal hosts | Self-hosted runners. Every action, component and tool vendored or mirrored. |
| Package dependencies | Public registries through a proxy | Nexus or Artifactory proxying public registries | Offline mirror of approved packages, refreshed through the transfer process |
| Container images | Cloud registry | Harbor, Nexus or Artifactory | Harbor or equivalent, loaded from transfer media. Only signed images admitted. |
| Signing and provenance | Sigstore keyless signing with public Fulcio and Rekor | Keyless with a private Sigstore deployment, or key-pair signing | Cosign key-pair signing with keys in an HSM. Private transparency log if you need one. |
| Vulnerability data | Scanner fetches feeds live | Same, through a proxy | Scanner databases downloaded outside, verified and transferred on a fixed schedule (daily to weekly) |
| Secrets | Cloud KMS and secrets manager | HashiCorp Vault or OpenBao, HSM for root keys | Same as on-premises. Root keys never leave the enclave. |
| Identity | Cloud identity provider with SSO | Keycloak, Active Directory or other corporate identity provider | Local identity provider inside the enclave. No federation to outside. |
| Deployment | Managed Kubernetes, PaaS, serverless | Kubernetes distribution, VMs, Argo CD or Flux | Same as on-premises, with all images and charts from internal sources |
| Observability | Managed or vendor service | Prometheus, Grafana, Loki, Tempo, OpenTelemetry Collector | Same as on-premises. Every component checked for call-home features. |
| Time | Provider time service | Internal NTP servers fed from trusted upstream sources | Internal stratum 1 source (GNSS receiver or atomic reference), distributed with NTP or PTP |
| Certificates | Public CA and cloud certificate service | Internal CA for internal names, public CA for public names | Internal CA only. CRLs and OCSP served inside the enclave. |
| Backups | Cloud snapshots plus copies in a second account or region | Backup system with an off-site or immutable copy | Immutable copies inside the enclave, with offline media for disaster recovery |
| Documentation | Hosted docs site | Internal docs site | Internal docs site. External references copied in with version and date. |
| Code assistants | Approved SaaS tools per [policy](../people/code-assistants.md) | Approved SaaS or self-hosted models | Self-hosted models only, or none |

## Air-gapped essentials

### Offline mirrors and internal registries

- Mirror only what is approved: packages and images from the Adopt and Trial rings of the [tech radar](../architecture/tech-radar.md) and their dependencies. A full public mirror is large and imports risk you have not reviewed.
- Keep the mirror's lock files and SBOMs, so you can answer "do we have the vulnerable version anywhere?" without internet access.
- Tools exist to package Kubernetes workloads for disconnected sites, for example Zarf and Hauler. Evaluate them against your transfer rules.

### Update media transfer

- Write down one transfer process and use it for everything: code, packages, images, vulnerability data, model weights, documentation.
- On the connected side, collect the items, generate a manifest with SHA-256 checksums and sign the manifest.
- Move the media through a one-way path (data diode or approved removable media). Scan it on a dedicated transfer station.
- On the isolated side, verify the signature and every checksum before import. Reject the whole batch on any mismatch.
- Log every transfer: who, when, what manifest, which approver. At Assured, two people take part: one prepares, one approves.

### Key-pair signing

- Without access to public Sigstore services, sign with cosign key pairs. Keep private keys in an HSM or in a KMS inside the enclave, never on a build agent's disk.
- Distribute public keys to admission controllers and verification tools through configuration management. Rotate keys at least once a year and on any suspected compromise.
- See [supply chain](../security/supply-chain.md) for what to sign and how to verify.

### Time synchronisation

- Certificate validation, token expiry, log ordering and trace timing all depend on correct clocks. An isolated network drifts unless you give it a time source.
- Run at least 2 internal time servers with an independent reference each. Configure every host with chrony or an equivalent client and alert on offsets above 100 milliseconds.
- GNSS signals can be jammed or spoofed, and isolated sites are often the ones most exposed. Give each GNSS receiver a holdover oscillator (rubidium or OCXO) rated for your longest expected GNSS outage, and alert on loss of GNSS lock and on disagreement between the two time servers.

### Certificate revocation

- Serve CRLs and, if used, OCSP from inside the enclave. Clients that cannot fetch revocation data either fail closed (outage) or fail open (risk). Decide which, per system, and write it down.
- Set CRL validity longer than your longest expected gap between publications, with margin. Alert well before a CRL expires.
- Revocation of external certificates (vendor update signing, for example) arrives through the transfer process. Include it in the schedule.

### Licensing and call-home features

- Confirm before purchase that commercial software can be licensed offline. Some products fail closed when they cannot reach a licence server.
- Disable telemetry, update checks and remote feature flags in every component. Test by watching outbound connection attempts at the network boundary.

## Sovereignty and exit planning

- **Data residency.** Record where each data set is stored and processed, including backups, logs and support access. Data protection laws such as Rwanda Law No 058/2021, the Nigeria Data Protection Act 2023, India's DPDP Act 2023 and EU GDPR set conditions on transfers. This is not legal advice: confirm with counsel.
- **Key control.** For sensitive data, hold your own keys: customer-managed keys in the cloud KMS at minimum, keys in your own HSM where the threat model or law requires it.
- **Open standards.** Use portable building blocks: OCI images, Kubernetes APIs, OpenTelemetry, SQL databases, S3-compatible object storage APIs, OpenID Connect. Each proprietary service you adopt goes in the exit plan with its replacement.
- **Exit plan.** For each critical provider, write down: what you would move to, how data is exported and in what format, how long it would take, what it would cost and who decides. EU DORA (Regulation (EU) 2022/2554, the financial sector law, unrelated to the DORA metrics research) requires financial entities to have exit strategies for ICT services that support critical functions.
- **Rehearse.** Export a full data set and restore it on the alternative at least once. An exit plan that has never moved data is a guess.

## Hybrid

- Use one control plane for delivery: the same git server, the same GitOps tool and the same policies deploy to cloud and on-premises targets.
- Federate identity so engineers have one account, but keep production access separate per environment.
- Keep the build once, deploy many rule: the same signed artefact goes to every environment. Do not rebuild per site.
- Design for the link between sites failing. Each site must keep running and keep its own logs and metrics when the link is down.

## Practice

### Foundation

- Pick one hosting model and record it in an ADR. Use managed services where you can.
- Use open formats (containers, SQL, OpenTelemetry) even on a single cloud, so a later move stays possible.
- Keep a one-page list of every external service you depend on, with how to export your data from each.

### Standard

- Golden path templates build and deploy on every hosting model you support. CI tests the air-gapped build path with network egress blocked.
- Internal registries and package proxies for all builds, even on cloud. This gives one place to apply policy and protects builds from public registry outages.
- An exit plan for each critical vendor, reviewed yearly.
- Hybrid sites share one GitOps repository and one policy set.

### Assured

- A documented, two-person transfer process with signed manifests and a transfer log kept as an audit record.
- Exit plans rehearsed every 2 years, with results reported to the risk owner.
- Data residency recorded per data set and checked in each [production readiness review](../reliability/production-readiness.md).
- Public sector: follow national guidance on cloud use and sovereign hosting, and the open standards and exit expectations in codes such as the UK Technology Code of Practice. See [public sector](../compliance/public-sector.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A separate, weaker process for the air-gapped site | Same practice, different tools. Review, signing and testing still apply. |
| Mirroring all of a public registry "to be safe" | Mirror the approved set and its dependencies only. |
| Vulnerability scanners in the enclave with months-old databases | Scheduled transfer of scanner data, with an alert when it is older than 7 days. |
| Exit plan written once for the procurement file | Review yearly and rehearse a data export. |
| Rebuilding artefacts per site | Build once, sign once, transfer the signed artefact. |
| Unnoticed clock drift on isolated hosts | Internal time sources with offset alerts. |

## Templates

- [ADR template](../../templates/docs/adr.md), for the hosting decision
- [Risk register](../../templates/strategy/risk-register.csv), for exit and concentration risks
- [Runbook](../../templates/docs/runbook.md), for the transfer process

## Sources

- Sigstore cosign documentation: https://docs.sigstore.dev/
- RFC 5280, X.509 certificates and CRLs: https://www.rfc-editor.org/rfc/rfc5280
- RFC 6960, Online Certificate Status Protocol: https://www.rfc-editor.org/rfc/rfc6960
- RFC 5905, Network Time Protocol version 4: https://www.rfc-editor.org/rfc/rfc5905
- Open Container Initiative specifications: https://opencontainers.org/
- EU Digital Operational Resilience Act, Regulation (EU) 2022/2554: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- UK Technology Code of Practice: https://www.gov.uk/guidance/the-technology-code-of-practice
