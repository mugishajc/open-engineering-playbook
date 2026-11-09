# Software supply chain

Know exactly what goes into every artifact you ship, prove where and how it was built, and refuse to deploy anything you cannot verify. Attackers now compromise build systems, maintainers and packages rather than the final product, and customers and regulators now ask for proof. A software bill of materials (SBOM), signed build provenance and signature checks at deployment answer both, and they cost a few CI steps.

## Outcomes

Starting points. Tune them to your risk.

- 100% of release artifacts (container images, packages, binaries) have an SBOM in CycloneDX or SPDX, stored with the artifact.
- 100% of release artifacts are signed, and production admission rejects unsigned or unverified artifacts.
- Release builds reach SLSA Build Level 2 at Standard and Level 3 at Assured.
- Third-party CI actions and base images are pinned by commit SHA or digest in 100% of pipelines.
- When a new critical vulnerability is published, you can list every affected service from SBOM data within 4 hours.
- Repositories you publish score at least 7 out of 10 on OpenSSF Scorecard.

## Two lessons from real incidents

- **Log4Shell (CVE-2021-44228, December 2021).** Many organisations spent days finding out where they ran Log4j, often as a transitive dependency. Teams with SBOMs and a searchable inventory answered in hours. Know what you run.
- **The xz-utils backdoor (CVE-2024-3094, 2024).** Malicious code was found in the upstream release tarballs of xz from version 5.6.0, inserted through the build process after a long effort to gain maintainer trust. Lessons: one overloaded maintainer is a supply chain risk; release tarballs can differ from the source repository; reproducible builds and building from the tagged source make that difference visible.

## Key terms

| Term | What it is | Standard |
|---|---|---|
| SBOM | A machine-readable list of components and versions in an artifact | CycloneDX (ECMA-424); SPDX (ISO/IEC 5962:2021) |
| Provenance | A signed statement of how, where and from what an artifact was built | SLSA provenance, in-toto attestations |
| Signature | Cryptographic proof that a trusted identity published the artifact and that it has not changed | Sigstore (cosign, Fulcio, Rekor) |
| VEX | A statement of whether a known vulnerability actually affects your product | OpenVEX; CSAF 2.0 VEX profile; CycloneDX VEX |

## SLSA build levels

SLSA version 1.1 defines the Build track; version 1.2 (2025) adds a Source track for source control integrity.

| Level | Requirement | How to reach it |
|---|---|---|
| Build L0 | No guarantees | Where most teams start |
| Build L1 | Provenance exists, showing how the artifact was built | Generate provenance in CI |
| Build L2 | Builds run on a hosted build platform that generates and signs the provenance | GitHub artifact attestations, GitLab or self-hosted CI with signed provenance |
| Build L3 | Hardened build platform: builds are isolated from each other and signing secrets are out of reach of build steps | Reusable, isolated provenance generators (for example the SLSA GitHub generator), hardened self-hosted builders |

## Practice

### Foundation

1. **Lockfiles and pinning** for every dependency (see [dependencies](dependencies.md)).
2. **Generate an SBOM** for every release in CI and store it with the release. Pick CycloneDX or SPDX and use it everywhere.
3. **Sign release artifacts** with Sigstore keyless signing from CI. No keys to manage: CI proves its identity with an OIDC token and the signature is recorded in a public transparency log.
4. **Pin third-party CI actions by commit SHA**, not by tag. Tags can move.
5. **Run OpenSSF Scorecard** on repositories you publish, and fix the cheapest checks first.

The [SBOM and signing workflow](../../templates/security/workflows/sbom-and-sign.yml) and the [Scorecard workflow](../../templates/security/workflows/scorecard.yml) do steps 2, 3 and 5 on GitHub Actions.

### Standard

1. **SLSA Build Level 2** for all release artifacts: provenance generated and signed by the build platform, not by a script the developer controls.
2. **Verify at deployment.** An admission controller (for example Sigstore policy-controller or Kyverno on Kubernetes) rejects images that are not signed by your CI identity. Verification in CI alone is not enough; the deploy target must check.
3. **SBOM inventory.** Send every SBOM to a central store that can answer "which services contain package X at version Y?". This turns a new critical vulnerability into a query.
4. **VEX for customers and auditors.** When a scanner reports a vulnerability that does not affect your product (code not reachable, feature not compiled in), publish a VEX statement instead of arguing in email.
5. **Base images** come from a small set of approved, regularly rebuilt images, pinned by digest (see [golden paths](../platform/golden-paths.md)).
6. **OSPS Baseline** for open-source projects you maintain: meet Level 1 now and plan for Level 2. The OpenSSF released the baseline on 25 Feb 2025 with three maturity levels.
7. **Source protection.** Branch rulesets, signed commits or verified pushes, and required review (see [source control](../delivery/source-control.md)).

### Assured

Everything in Standard, plus:

1. **SLSA Build Level 3** for Tier 1 artifacts: isolated builds, signing material unreachable from build steps.
2. **Reproducible builds** for critical components where feasible, so a second builder can confirm the artifact matches the source.
3. **Build from source for critical dependencies**, from the tagged repository commit, not from release tarballs. The xz-utils backdoor was in the tarballs.
4. **Supplier SBOMs.** Require SBOMs and vulnerability disclosure policies from software suppliers in contracts (see [third-party and SaaS risk](third-party-and-saas-risk.md)).
5. **EU Cyber Resilience Act.** Manufacturers must identify and document components, including by drawing up an SBOM in a commonly used, machine-readable format covering at least the top-level dependencies (Annex I, Part II). Most obligations apply from 11 Dec 2027.
6. **Evidence.** Keep SBOMs, provenance and signature verification logs for every release for the support period of the product. This supports SSDF practices PS.2 and PS.3 and ISO/IEC 27001:2022 control 8.30 for outsourced code.

## Cloud, on-premises and air-gapped

- **Keyless signing needs the internet.** Sigstore keyless signing uses the public Fulcio certificate authority and Rekor transparency log. In air-gapped networks, use cosign with a key pair held in an HSM, a KMS or Vault, skip the public transparency log, and verify with the public key. The [GitLab supply chain template](../../templates/security/gitlab-supply-chain.yml) does this.
- **Self-hosted Sigstore.** Larger organisations can run their own Fulcio, Rekor and timestamp services inside the network. It is significant work; start with key pairs.
- **Transfers.** Sign artifacts and SBOMs on the connected side, verify on the isolated side before import, and log both. A mirrored registry (Harbor, Nexus, Artifactory) holds the verified copies.
- **Vulnerability data** for SBOM matching must be imported regularly (at least weekly), with the import date recorded.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| SBOM generated once for a compliance request | Generate on every release, automatically, stored with the artifact. |
| Signatures created but never checked | Verify at admission. Unverified artifacts do not run. |
| Actions pinned to `@v4` or `@main` | Pin to full commit SHA, with the version in a comment; let an update bot bump it. |
| Signing key stored as a CI variable that every job can read | Keyless signing, or a KMS or HSM key that only the release job can use. |
| Scanner noise answered by email | Publish VEX statements. |

## Templates

- [SBOM and signing workflow for GitHub Actions](../../templates/security/workflows/sbom-and-sign.yml)
- [OpenSSF Scorecard workflow](../../templates/security/workflows/scorecard.yml)
- [GitLab supply chain include for self-managed and air-gapped](../../templates/security/gitlab-supply-chain.yml)
- [Renovate configuration](../../templates/repo/renovate.json)

## Sources

- SLSA specification: https://slsa.dev/spec/
- CycloneDX: https://cyclonedx.org/ and SPDX: https://spdx.dev/
- OpenVEX specification: https://github.com/openvex/spec
- OASIS CSAF 2.0: https://docs.oasis-open.org/csaf/csaf/v2.0/csaf-v2.0.html
- Sigstore documentation: https://docs.sigstore.dev/
- OpenSSF Scorecard: https://scorecard.dev and OSPS Baseline: https://baseline.openssf.org
- Reproducible Builds project: https://reproducible-builds.org/
- NVD, CVE-2024-3094 (xz-utils): https://nvd.nist.gov/vuln/detail/CVE-2024-3094
- NVD, CVE-2021-44228 (Log4Shell): https://nvd.nist.gov/vuln/detail/CVE-2021-44228
- Regulation (EU) 2024/2847 (Cyber Resilience Act), Annex I: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
