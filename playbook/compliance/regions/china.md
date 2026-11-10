# China: what changes when you apply this playbook

This page is for engineering, security and compliance leads who build or run software for users in China, sell products into the Chinese market, or operate infrastructure on Chinese soil. Three things differ most from the playbook's EU-centered defaults. First, China has its own data protection, cyber security and data security laws (the Personal Information Protection Law, the Cybersecurity Law and the Data Security Law), each with its own regulator, cross-border transfer rules and incident clocks, and the Cyberspace Administration of China (CAC) sits above all three. Second, cryptography follows national standards (SM2, SM3, SM4) and a separate approval process; NIST FIPS does not satisfy Chinese requirements, and critical information infrastructure (CII) operators must pass a yearly cryptography evaluation. Third, every system that matters must be classified under the Multi-Level Protection Scheme (MLPS 2.0) and tested, every app and website must be filed, and cross-border data transfers need a security assessment, standard contract or certification depending on volume.

> Not legal advice. Facts checked against primary sources on 9 Nov 2026. Laws change; confirm with counsel.

## At a glance

| Topic | What applies | Regulator or owner | Source |
|---|---|---|---|
| Personal information | Personal Information Protection Law (PIPL), in force 1 Nov 2021 | CAC, sector regulators | [CAC](https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm) |
| Cyber security | Cybersecurity Law, amended and in force 1 Jan 2026; CII Security Protection Regulations (State Council Order 745, 1 Sep 2021) | CAC, Ministry of Public Security, sector protection departments | [CAC](https://www.cac.gov.cn/2026-01/05/c_1769341969044337.htm) |
| Data security | Data Security Law (DSL), in force 1 Sep 2021; Network Data Security Management Regulations (State Council Order 790, 1 Jan 2025) | CAC, sector regulators | [CAC](https://www.cac.gov.cn/2024-09/30/c_1729384453671239.htm) |
| Security classification | MLPS 2.0 (GB/T 22239-2019), in force 1 Dec 2019 | Ministry of Public Security | GB/T 22239-2019 |
| Cross-border data | CAC Provisions on Promoting and Regulating Cross-border Data Flows, 22 Mar 2024; Certification Measures (Order 20, 1 Jan 2026) | CAC, SAMR | [CAC](https://www.cac.gov.cn/2024-03/22/c_1712776612187994.htm) |
| Incident reporting | National Cybersecurity Incident Reporting Measures, 1 Nov 2025 | CAC, sector authorities | [CAC](https://www.cac.gov.cn/2025-09/15/c_1759583021718167.htm) |
| Cryptography | Cryptography Law (1 Jan 2020); Commercial Cryptography Administration Regulations (State Council Order 760, 1 Jul 2023) | State Cryptography Administration, CAC | [MEE](https://www.mee.gov.cn/zcwj/gwywj/202305/t20230529_1031579.shtml) |
| AI | Generative AI Interim Measures (15 Aug 2023); AI content labelling measures and GB 45438-2025 (1 Sep 2025); algorithm recommendation provisions (1 Mar 2022); deep synthesis provisions (10 Jan 2023) | CAC | [CAC](https://www.cac.gov.cn/2024-04/02/c_1713729983803145.htm) |
| Accessibility | Barrier-free Environment Construction Law (1 Sep 2023); GB/T 37668-2019 | Ministry of Housing and Urban-Rural Development | GB/T 37668-2019 |
| Financial data | PBOC data security measures (PBOC Order [2025] No. 3, 30 Jun 2025); NFRA measures for banks and insurers (27 Dec 2024) | PBOC, NFRA | Sector rules |
| App and website filing | ICP filing (State Council Order 292); app filing (MIIT Order [2023] No. 105) | MIIT | MIIT |
| Sanctions and export controls | US EAR Entity List and advanced computing controls; US DOJ Data Security Program (28 CFR part 202); EU dual-use Regulation (EU) 2021/821; US Outbound Investment Security Program (31 CFR part 850) | US BIS, DOJ, OFAC; EU Commission | [DOJ NSD](https://www.justice.gov/nsd/data-security) |

## Laws and regulators

**Data protection.** The Personal Information Protection Law (PIPL, adopted 20 Aug 2021, in force 1 Nov 2021) is the general data protection statute. It requires a lawful basis, purpose limitation, data minimization, storage limitation and rights of access, correction, deletion and portability. Processors of more than 1 million people's personal information, and all CII operators, must store personal information inside China (Art. 40). Foreign processors must appoint a representative in China (Art. 53). Compliance audits are mandatory: the Personal Information Protection Compliance Audit Measures (CAC Order 18, 1 May 2025) require processors of more than 10 million people's data to audit at least every 2 years. Penalties reach 50 million yuan or 5% of the previous year's turnover, plus personal fines and a ban on holding responsible positions. In practice: keep the playbook's data inventory, add a PIPL lawful basis column, appoint a personal information protection officer (Art. 52), and run the PIPL impact assessment (Art. 55) before any cross-border transfer.

**Cross-border data transfers.** Three paths exist, with thresholds set by the CAC Provisions on Promoting and Regulating Cross-border Data Flows (22 Mar 2024). Security assessment (filed with the CAC): CII operators, important data, or transfer of 1 million or more people's non-sensitive personal information or 10,000 or more people's sensitive personal information, counted from 1 January of each year. Assessment results are valid for 3 years. Standard contract or certification: 100,000 to under 1 million non-sensitive, or under 10,000 sensitive. The Personal Information Cross-border Certification Measures (CAC and SAMR Order 20, 14 Oct 2025, in force 1 Jan 2026) set a 3-year certificate validity. Exempt: under 100,000 non-sensitive personal information, or transfer for contract performance, cross-border HR management and certain other purposes. Free trade zones may publish their own negative lists. Data is not important data unless the government has notified or published it as such. In practice: count transfer volumes quarterly and route to the right path.

**Cyber security.** The Cybersecurity Law (original 1 Jun 2017, amended 1 Jan 2026) sets network security duties for all network operators and extra duties for CII operators. The 2025 amendment raised penalties (including for large data leaks and loss of CII function), added an AI article and aligned penalties with PIPL. CII operators are identified by sector protection departments under the CII Security Protection Regulations (State Council Order 745, 1 Sep 2021) and must use only products and services that have passed a cybersecurity review (Cybersecurity Review Measures, 15 Feb 2022). Platform operators with more than 1 million users' personal information must apply for review before listing abroad.

**Security classification.** Every network and information system must be classified at one of five protection levels under MLPS 2.0 (GB/T 22239-2019, 1 Dec 2019). Level 2 and above must file with the local public security bureau. Level 3 and above must pass yearly testing by an accredited firm. CII operators are typically level 3 or above. Data classification follows GB/T 43697-2024 (1 Oct 2024). In practice: classify each system and dataset before launch, file with the bureau, and schedule testing.

**Incident reporting.** The National Cybersecurity Incident Reporting Measures (1 Nov 2025) set four grades (from general to especially major, based on GB/T 20986-2023). CII operators report to their sector protection department and to public security within 1 hour. Central and state organs report to their own cyberspace authority within 2 hours. Other network operators report to the provincial CAC within 4 hours. Personal information leaks are reported immediately (PIPL Art. 57). Suspected crimes are reported to public security promptly.

**Cryptography.** The Cryptography Law (1 Jan 2020) divides cryptography into core, ordinary and commercial. Commercial cryptography follows the Commercial Cryptography Administration Regulations (State Council Order 760, 1 Jul 2023). CII operators must pass a commercial cryptography application security evaluation before going live and at least yearly after (Art. 38). Products used must pass testing and certification (Art. 39). National standards are SM2 (GB/T 32918, elliptic curve), SM3 (GB/T 32905-2016, hash) and SM4 (GB/T 32907-2016, block cipher). For TLS, the national protocol is TLCP (GB/T 38636-2020, 1 Nov 2020), which uses dual certificates and SM4 with SM3. RFC 8998 defines TLS 1.3 cipher suites TLS_SM4_GCM_SM3 and TLS_SM4_CCM_SM3. Open-source implementations include Tongsuo and GmSSL. In practice: run dual-stack TLS (international algorithms plus TLCP or RFC 8998 suites), keep a [crypto inventory](../../../templates/docs/crypto-inventory.csv) with an SM-approval column, and schedule the yearly evaluation.

**AI.** The Generative AI Service Interim Measures (15 Aug 2023) require filing of generative AI services with the CAC; apps must show the filed model name and filing number. The AI Content Labelling Measures and mandatory standard GB 45438-2025 (1 Sep 2025) require explicit labels and implicit metadata labels on AI-generated content and ban removing them. The Algorithm Recommendation Provisions (1 Mar 2022) and Deep Synthesis Provisions (10 Jan 2023) add registration and transparency duties. In practice: file each model, label all generated content, and add these to the [AI governance](../../ai/ai-governance.md) register.

**Accessibility.** The Barrier-free Environment Construction Law (1 Sep 2023) encourages accessible websites and apps across sectors. The web accessibility standard is GB/T 37668-2019. In practice: test against GB/T 37668 alongside WCAG 2.2 AA, as the playbook recommends.

**Data localization.** PIPL Art. 40 requires CII operators and processors above the CAC volume threshold to store personal information inside China. The DSL Art. 36 and PIPL Art. 41 prohibit providing data to foreign judicial or law enforcement bodies without approval from the competent Chinese authority. The Export Control Law (1 Dec 2020) and Anti-Foreign Sanctions Law (10 Jun 2021) add further restrictions. In practice: host in a domestic cloud (Alibaba Cloud, Tencent Cloud or Huawei Cloud) or use a global provider's China region run by its local partner, and treat the cross-border network link as unreliable.

## Reporting clocks

| Event | Who must report | To whom | Deadline | Source |
|---|---|---|---|---|
| Cybersecurity incident at a CII operator | CII operators | Sector protection department and public security | Within 1 hour | [CAC](https://www.cac.gov.cn/2025-09/15/c_1759583021718167.htm) |
| Cybersecurity incident at a central or state organ | Central and state organs | Their cyberspace authority | Within 2 hours | Same |
| Cybersecurity incident at other network operators | Other network operators | Provincial CAC | Within 4 hours | Same |
| Personal information leak | Personal information processors | Authorities and affected individuals | Immediately (PIPL Art. 57) | [PIPL](https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm) |

## What changes in the playbook

| Playbook page | What to add or change in this region |
|---|---|
| [Data security and privacy](../../data/data-security-and-privacy.md) | Add PIPL to the laws-to-check table. Add PIPL lawful basis, impact assessment (Art. 55), processor representative (Art. 53), and the cross-border transfer paths and thresholds. |
| [Incident management](../../reliability/incident-management.md) | Add the 1-hour (CII), 2-hour (state organs) and 4-hour (other operators) clocks and the PIPL immediate-report duty to the Assured table. |
| [Control mapping](../control-mapping.md) | Add an MLPS 2.0 column mapping controls to GB/T 22239-2019. Note that MLPS, not ISO 27001, is the required framework. |
| [Cloud, on-prem, air-gapped](../../platform/cloud-on-prem-air-gapped.md) | Add domestic cloud providers. Note that ICP filing is required before serving content. Package mirrors (Nexus, Artifactory, Harbor) behind your own proxy are normal. Domestic Android app stores replace Google Play. Map SDKs use a national datum that differs from WGS-84; convert at the boundary. |
| [Post-quantum readiness](../../security/post-quantum-readiness.md) | Note that China approves algorithms nationally (SM series), not through NIST. |
| [Vulnerability management](../../security/vulnerability-management.md) | Add the China National Vulnerability Database (CNNVD) and CNVD alongside CISA KEV. |
| [Supply chain](../../security/supply-chain.md) | Note that public Sigstore is reachable but slow; use cosign key-pair signing and a self-hosted transparency log or private Rekor where needed. |
| [AI governance](../../ai/ai-governance.md) | Add the CAC generative-AI filing, the content labelling duty, and the algorithm and deep-synthesis provisions. |
| [Third-party and SaaS risk](../../security/third-party-and-saas-risk.md) | Add sanctions and export-control screening (US EAR Entity List, US DOJ Data Security Program, EU dual-use Regulation). Screen both suppliers and customers. |
| [Build, buy, adopt](../../strategy/build-buy-adopt.md) | For CII, products must pass cybersecurity review. The Government Procurement Law Art. 10 requires domestic goods for government buyers. |
| [Public sector](../public-sector.md) | Add China data residency, MLPS, the Government Procurement Law and the Revised Law on Guarding State Secrets (1 May 2024). Map reviews require an audit number for any map shown in China. |
| [Secrets](../../security/secrets.md) | Store SM keys with the same controls. Note that the State Cryptography Administration governs key management for commercial cryptography. |

## Public sector

Government systems follow MLPS 2.0 at level 3 or above, classified and filed with the public security bureau. The Government Procurement Law Art. 10 gives preference to domestic goods; local policy may further restrict foreign software. The Revised Law on Guarding State Secrets (in force 1 May 2024) sets handling rules for state secrets at three levels. Software that processes, transmits or stores classified information must use state-secret-grade cryptography, not commercial-grade.

- **ICP filing.** Every website serving content in China needs an ICP filing (State Council Order 292). Commercial sites need an ICP license. Filing is done through the provincial communications authority. Without it, domestic hosting providers will not serve your domain.
- **App filing.** MIIT Order [2023] No. 105 requires mobile apps to be filed. Existing apps had until end of March 2024. App stores may not distribute unfiled apps. Android apps in China are distributed through domestic stores (Huawei AppGallery, Xiaomi GetApps, Tencent MyApp and others), not Google Play.
- **Maps.** Map Management Regulations require a map review number for any map shown in China. Domestic map SDKs (such as those from Amap or Baidu Maps) use the national coordinate system GCJ-02, which differs from WGS-84. Convert coordinates at the boundary between your internal systems and the public-facing map.
- **Identity.** National network identity authentication measures (15 Jul 2025) introduce voluntary network credentials. Real-name registration duties already apply to many internet services under the Cybersecurity Law.
- **Network.** Treat the cross-border network link as variable in latency and throughput. Keep China sites autonomous: local container registries, package mirrors (Nexus, Artifactory, Harbor) and artifact stores behind your own proxy. Build and deploy from inside the region.

## Financial services

- **PBOC.** The People's Bank of China data security measures for business fields (PBOC Order [2025] No. 3, in force 30 Jun 2025) cover banking and payment data. They add sector-specific classification, access control and audit duties on top of the PIPL and DSL.
- **NFRA.** The National Financial Regulatory Administration data security measures for banks and insurers (27 Dec 2024) set classification, access control and audit requirements in 81 articles. Banks and insurers must follow both the NFRA measures and the general PIPL and DSL rules.
- **Cybersecurity review.** Financial institutions may be classified as CII operators, which triggers the cybersecurity review for procurement and the yearly commercial cryptography evaluation. Check with your sector protection department.
- **Cross-border.** Financial data transfers follow both the CAC cross-border rules and sector-specific PBOC or NFRA requirements. Count transfer volumes per quarter and route to the right path (security assessment, standard contract or certification).
- **Cryptography.** Financial systems on CII must pass the commercial cryptography application security evaluation. Use SM algorithms for data at rest and in transit within China, and keep international algorithms for cross-border connections where the counterpart does not support SM suites.

## Deadlines to watch, 2026 to 2028

| Date | What happens |
|---|---|
| In force | PIPL, DSL, Cybersecurity Law (amended), MLPS 2.0, Network Data Security Management Regulations, Cryptography Law, Commercial Cryptography Regulations |
| In force | Cross-border transfer provisions (22 Mar 2024), certification measures (1 Jan 2026), compliance audit measures (1 May 2025) |
| In force | AI content labelling measures and GB 45438-2025 (1 Sep 2025) |
| Rolling | CAC may update cross-border thresholds, important data catalogues and free trade zone negative lists |
| Rolling | MLPS testing cycle: level 3 and above tested yearly |
| 2027 onward | US connected vehicles software ban begins model year 2027 (BIS rule, 17 Mar 2025) |
| 2 Jan 2025 onward | US Outbound Investment Security Program covers semiconductors, quantum and AI investments involving China |

## Sources

- PIPL full text: https://www.cac.gov.cn/2021-08/20/c_1631050028355286.htm
- Cybersecurity Law (amended), official publication: https://www.cac.gov.cn/2026-01/05/c_1769341969044337.htm
- Network Data Security Management Regulations: https://www.cac.gov.cn/2024-09/30/c_1729384453671239.htm
- Provisions on Promoting and Regulating Cross-border Data Flows: https://www.cac.gov.cn/2024-03/22/c_1712776612187994.htm
- Personal Information Cross-border Certification Measures: https://www.cac.gov.cn/2025-10/17/c_1762449728518762.htm
- Personal Information Protection Compliance Audit Measures: https://www.cac.gov.cn/2025-02/14/c_1741232791991016.htm
- Cybersecurity Review Measures: https://www.cac.gov.cn/2022-02/17/c_1646738974343952.htm
- National Cybersecurity Incident Reporting Measures: https://www.cac.gov.cn/2025-09/15/c_1759583021718167.htm
- Generative AI Interim Measures (interpretation): https://www.cac.gov.cn/2024-04/02/c_1713729983803145.htm
- Commercial Cryptography Administration Regulations: https://www.mee.gov.cn/zcwj/gwywj/202305/t20230529_1031579.shtml
- RFC 8998, ShangMi cipher suites for TLS 1.3: https://www.rfc-editor.org/rfc/rfc8998
- DOJ National Security Division, Data Security Program: https://www.justice.gov/nsd/data-security
- US BIS, connected vehicles rule: https://www.bis.gov/press-release/commerce-finalizes-rule-secure-connected-vehicle-supply-chains-foreign-adversary-threats
- US Treasury, Outbound Investment Security Program FAQs: https://home.treasury.gov/system/files/206/Outbound-Investment-Security-Program-FAQs.pdf
- EU dual-use Regulation (EU) 2021/821: https://eur-lex.europa.eu/eli/reg/2021/821/oj
