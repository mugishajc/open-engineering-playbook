# Zero trust

Stop treating the internal network as safe: authenticate and authorise every request based on who is asking, from what device, for which resource, and check again on every session. The problem most organisations have is a flat network behind a VPN, where one phished laptop or one compromised server can reach everything. Zero trust is not a product you buy; it is a set of changes to identity, devices, networks, workloads and data that you make in order, starting with identity.

## Outcomes

Starting points. Tune them to your estate.

- 100% of internal applications require SSO and MFA, whether or not the user is on the corporate network or VPN.
- Production systems accept connections only from authenticated workloads (mutual TLS or signed tokens), not from any host on a subnet.
- At least 90% of user access to internal tools goes through an identity-aware proxy or the application's own SSO, not through a network-level VPN.
- Access to sensitive data requires a managed, compliant device in 100% of cases.
- You can show, for any production resource, which identities can reach it and why, within 1 working day.
- Each pillar's maturity stage is assessed once a year against the CISA Zero Trust Maturity Model.

## The model in brief

NIST SP 800-207 (2020) describes zero trust architecture: no implicit trust from network location, access granted per session by a policy decision point, and continuous checks of identity and device state. The CISA Zero Trust Maturity Model v2.0 (2023) breaks the work into five pillars and four stages (Traditional, Initial, Advanced, Optimal), with three cross-cutting capabilities: visibility and analytics, automation and orchestration, and governance.

| Pillar | First move | Where in this playbook |
|---|---|---|
| Identity | SSO and phishing-resistant MFA for every tool | [Access control](access-control.md) |
| Devices | Inventory and management of every device that touches company data | This page |
| Networks | Segment by service; encrypt all internal traffic | This page; [cloud native](../platform/cloud-native.md) |
| Applications and workloads | Workload identity; authorise every call | [Secrets](secrets.md); [API standards](../architecture/api-standards.md) |
| Data | Classify; encrypt; log access to sensitive data | [Data security and privacy](../data/data-security-and-privacy.md) |

## Practice

### Foundation

1. **Identity first.** SSO and MFA on every application, including the ones "only reachable from the office". This single step removes most of the value of a stolen password.
2. **Device inventory.** Know every laptop and phone that reaches company data. Turn on disk encryption, screen lock and automatic updates through device management.
3. **No shared admin credentials** and no flat admin network. Admin access is per person and logged.
4. **TLS everywhere,** including internal traffic between services.
5. **Remove direct exposure.** No database, admin panel or remote desktop port open to the internet.

### Standard

1. **Identity-aware access instead of VPN** for internal web tools: a proxy checks the user's identity, group and device before each session. Keep VPN for the few protocols that need it, and segment what it reaches.
2. **Device posture in access decisions.** Production and sensitive data require a managed device that is encrypted, patched within 14 days (starting point) and running endpoint protection.
3. **Micro-segmentation.** Default-deny network policies between services; allow only declared flows. On Kubernetes, a default-deny NetworkPolicy per namespace (see the [service baseline](../../templates/platform/k8s-service-baseline.yaml)).
4. **Workload identity.** Services authenticate to each other with mutual TLS certificates issued automatically or with short-lived signed tokens, and each call is authorised against a policy. A service mesh is one way to get mutual TLS; it is not required.
5. **Least-privilege data access** with logging of every read of restricted data.
6. **Central logs** of authentication and authorisation decisions, kept for at least 12 months (starting point), with alerts on impossible travel, new devices and unusual data volumes. Retention, write-once storage and clock synchronisation for security logs follow [observability](../architecture/observability.md).
7. **Endpoint and email.** Endpoint detection and response on every managed device, with coverage reported monthly (target 100% of devices that reach production or restricted data). Block macros from internet files and script execution from user download folders. Filter inbound email for spoofing (SPF, DKIM and DMARC at `p=reject` on your own domains) and for malicious attachments and links.

### Assured

Everything in Standard, plus:

1. **Formal maturity assessment** against the CISA model per pillar, with a funded plan to reach the target stage. Public sector bodies often have a mandated target.
2. **Continuous evaluation.** Sessions are re-checked when risk changes (device falls out of compliance, user changes role), not only at sign-in.
3. **Policy as code** for access rules, reviewed and versioned like application code.
4. **Evidence.** Access policies, decision logs and assessment results kept for the audit period. This supports ISO/IEC 27001:2022 controls 5.15 (access control), 8.5 (secure authentication), 8.16 (monitoring activities), 8.20 (networks security) and 8.22 (segregation of networks).

## Cloud, on-premises and air-gapped

- **Air-gapped is not zero trust.** An isolated network still needs identity, segmentation and logging inside it. Insiders, removable media and one compromised host inside the gap can reach everything on a flat network.
- **On-premises:** Keycloak for identity, an identity-aware reverse proxy in front of internal tools, network policies or firewalls between segments, and an internal certificate authority for mutual TLS.
- **Hybrid:** use one identity provider and one policy model across cloud and on-premises, so access decisions do not depend on where the resource runs.
- **Operational technology and legacy systems** that cannot authenticate users: put them behind a gateway that does, and segment them tightly.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "We bought a zero trust product" | Zero trust is a set of changes across five pillars. Map the product to the pillar it helps. |
| VPN gives full network access after login | Identity-aware access per application; segment what the VPN reaches. |
| Internal APIs with no authentication "because they are internal" | Workload identity and authorisation on every call. |
| Big-bang programme with no early results | Start with identity and MFA; show progress per pillar every quarter. |
| Device checks only at enrolment | Check posture at each session. |

## Templates

- [Kubernetes service baseline with default-deny network policy](../../templates/platform/k8s-service-baseline.yaml)
- [Threat model](../../templates/docs/threat-model.md)

## Sources

- NIST SP 800-207, *Zero Trust Architecture* (2020): https://csrc.nist.gov/pubs/sp/800/207/final
- CISA, *Zero Trust Maturity Model* version 2.0 (2023): https://www.cisa.gov/zero-trust-maturity-model
- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
