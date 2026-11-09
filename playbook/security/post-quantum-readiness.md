# Post-quantum readiness

Start now by building an inventory of where you use public-key cryptography, make it possible to swap algorithms without rewriting systems, and move first the data that must stay secret for 10 years or more. A future quantum computer could break RSA and elliptic-curve cryptography, and attackers can record encrypted traffic today and decrypt it later ("harvest now, decrypt later"). Past cryptographic migrations took 10 to 20 years according to NIST, and NIST plans to deprecate these algorithms after 2030 and disallow them after 2035.

## Outcomes

Starting points. Tune them to your data and suppliers.

- A cryptographic inventory covers 100% of Tier 1 systems by the end of 2027, and all systems by the end of 2028.
- Every system that protects data needing confidentiality for 10+ years has a migration plan with a date.
- External TLS endpoints you control support hybrid post-quantum key exchange where your TLS library offers it, with progress reported quarterly.
- 100% of new procurement contracts for software and hardware ask for the supplier's post-quantum roadmap.
- New systems pass a crypto-agility check at design review: algorithms are configured, not hard-coded.

## What changes and what does not

| Cryptography | Quantum risk | Action |
|---|---|---|
| Key exchange (RSA, ECDH, DH) in TLS, SSH, VPNs | High: recorded traffic can be decrypted later | Move first, using hybrid key exchange (classical plus ML-KEM) |
| Digital signatures (RSA, ECDSA, EdDSA) for code signing, certificates, documents | High once a large quantum computer exists, but cannot be forged retroactively for past verification | Plan now; migrate long-lived roots of trust and firmware signing early |
| Symmetric encryption (AES) and hashes (SHA-2, SHA-3) | Low: NIST believes approved symmetric primitives with at least 128 bits of classical security meet its lowest post-quantum security category | Keep AES-128 or stronger; move away from 112-bit symmetric algorithms, which NIST disallows in 2030 |

NIST published the first post-quantum standards on 13 Aug 2024: FIPS 203 (ML-KEM, key encapsulation), FIPS 204 (ML-DSA, signatures) and FIPS 205 (SLH-DSA, hash-based signatures). In March 2025 NIST selected HQC as an additional key encapsulation algorithm.

## Timeline, 2026 to 2035

| When | Milestone | Source |
|---|---|---|
| Now (2026) | Build the inventory; add crypto-agility to design standards; ask suppliers for roadmaps; enable hybrid key exchange where available | NIST IR 8547; UK NCSC |
| By 2028 | Discovery complete and an initial migration plan in place, including supplier dependencies and long-lived hardware roots of trust | UK NCSC migration timelines |
| 2030 to 2031 | US federal high value assets and high impact systems move to post-quantum cryptography | Executive Order 14412 and OMB M-26-15, as referenced by NIST IR 8547 |
| After 2030 | NIST deprecates quantum-vulnerable public-key algorithms (RSA, ECDSA, EdDSA, DH, ECDH) | NIST IR 8547 |
| By 2031 | Highest-priority migrations done; plan refined to finish by 2035 | UK NCSC |
| After 2035 | NIST disallows quantum-vulnerable public-key algorithms; migration complete | NIST IR 8547; UK NCSC |

If you are not a US federal body, the federal dates still shape what your suppliers build. Check the current version of NIST IR 8547 (final, October 2026) and your national authority's guidance.

## Practice

### Foundation

1. **Inventory.** List where you use public-key cryptography: TLS endpoints, SSH, VPNs, code and artifact signing, certificates and certificate authorities, tokens (JWT signing), encrypted backups, hardware security modules, and third-party services that do it for you. Use the [crypto inventory template](../../templates/docs/crypto-inventory.csv). For each, record the algorithm, key size, owner, and how long the protected data must stay secret.
2. **Find the long-lived secrets.** Rank systems by confidentiality lifetime. Health records, state secrets, long-term contracts, identity data and anything kept 10+ years go first.
3. **Stay current.** Keep TLS libraries, operating systems and language runtimes updated. Most of the migration arrives through these updates.
4. **Ask suppliers** the questions below at renewal.

### Standard

1. **Crypto-agility as a design rule.** Algorithms and key sizes are configuration, not code. Cryptography goes through a small number of approved libraries. Protocols negotiate algorithms. Certificates and keys can be rotated without downtime (see [secrets](secrets.md)).
2. **Hybrid key exchange first.** Enable hybrid key exchange (a classical algorithm such as X25519 combined with ML-KEM) on TLS endpoints where your TLS library and clients support it. Hybrids protect against harvest-now-decrypt-later while hedging against weaknesses in new algorithms. NIST notes that hybrids add complexity and are expected to be temporary.
3. **CBOM.** Record cryptographic assets in machine-readable form. CycloneDX supports a cryptography bill of materials (CBOM) alongside the SBOM (see [supply chain](supply-chain.md)).
4. **Test interoperability** in a non-production environment: larger keys and signatures can break middleboxes, packet sizes and hardware with fixed buffers.
5. **Prioritised plan.** Order the migration by data lifetime, exposure (internet-facing first) and dependency on suppliers.

### Assured

Everything in Standard, plus:

1. **Board-level programme.** Name an executive owner, fund the plan, and report progress against the 2028, 2031 and 2035 milestones each year.
2. **Long-lived roots of trust.** Firmware signing keys, device identity certificates and hardware with lifetimes past 2035 need post-quantum or hybrid signatures planned now; you cannot update a device whose root of trust you cannot replace.
3. **Validated modules.** Regulated and public bodies use cryptographic modules validated for the new algorithms as they become available.
4. **Evidence.** Inventory, plan and supplier responses kept and reviewed yearly. This supports ISO/IEC 27001:2022 control 8.24 (use of cryptography).

## Questions to ask suppliers

1. Which of your products use RSA, ECDSA, EdDSA, DH or ECDH, and for what?
2. When will each product support ML-KEM, ML-DSA or SLH-DSA, and in which protocols?
3. Do you support hybrid key exchange today? Is it on by default?
4. Can algorithms be changed by configuration, or does it need a new version or new hardware?
5. Do your hardware products have roots of trust that can be updated to post-quantum signatures?
6. Can you provide a CBOM or a list of cryptographic dependencies?

The [vendor risk questionnaire](../../templates/docs/vendor-risk-questionnaire.md) includes these.

## Cloud, on-premises and air-gapped

- **Cloud and CDN providers** often enable hybrid key exchange at their edge first. Check what your provider supports between users and the edge, and between the edge and your origin.
- **On-premises and air-gapped** systems migrate only when you update libraries, HSM firmware and appliances. Plan transfer and test windows for these updates now.
- **Air-gapped data still leaks.** Data that leaves an isolated network encrypted (backups, transfers) is exposed to harvest-now-decrypt-later; inventory those flows first.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Waiting for a quantum computer to appear | Recorded traffic is already at risk. Start with inventory and long-lived data. |
| Rewriting cryptography by hand with new algorithms | Use maintained libraries and protocols; configure, do not implement. |
| Inventory done once in a spreadsheet | Generate CBOM data from builds and scans; review yearly. |
| Buying hardware in 2027 that cannot be updated | Ask the supplier questions in every procurement. |
| Replacing AES-256 "for quantum safety" | Symmetric crypto with 128+ bits is fine. Focus on public-key algorithms. |

## Templates

- [Crypto inventory](../../templates/docs/crypto-inventory.csv)
- [Vendor risk questionnaire](../../templates/docs/vendor-risk-questionnaire.md)

## Sources

- NIST IR 8547, *Transition to Post-Quantum Cryptography Standards* (final, October 2026): https://nvlpubs.nist.gov/nistpubs/ir/2026/NIST.IR.8547.pdf
- NIST FIPS 203: https://csrc.nist.gov/pubs/fips/203/final, FIPS 204: https://csrc.nist.gov/pubs/fips/204/final, FIPS 205: https://csrc.nist.gov/pubs/fips/205/final
- NIST, selection of HQC (March 2025): https://www.nist.gov/news-events/news/2025/03/nist-selects-hqc-fifth-algorithm-post-quantum-encryption
- UK NCSC, *Timelines for migration to post-quantum cryptography*: https://www.ncsc.gov.uk/guidance/pqc-migration-timelines
- CISA, *Quantum-Readiness: Migration to Post-Quantum Cryptography*: https://www.cisa.gov/resources-tools/resources/quantum-readiness-migration-post-quantum-cryptography
- CycloneDX, Cryptography Bill of Materials: https://cyclonedx.org/capabilities/cbom/
