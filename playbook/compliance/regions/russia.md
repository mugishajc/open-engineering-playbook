# Russia: what changes when you apply this playbook

This page is for engineering, security and compliance leads who build or run software for users in Russia, sell products into the Russian market, or operate infrastructure on Russian soil. Three things differ most from the playbook's EU-centered defaults. First, personal data of Russian citizens must be stored in databases physically located in Russia (Federal Law 152-FZ, Art. 18(5)), cross-border transfers need Roskomnadzor approval, and penalties for data leaks now include turnover-based fines and criminal liability. Second, critical information infrastructure (CII) operators face a ban on foreign software on significant CII objects, must report incidents to the national coordination center (GosSOPKA) within 3 or 24 hours, and must move to domestically produced software and hardware by set deadlines. Third, US, EU and UK sanctions restrict the supply of IT services, enterprise software and security tools to Russian entities, and the engineering environment relies on domestic cloud providers, domestic app stores and GOST cryptography certified by the FSB.

> Not legal advice. Facts checked against primary sources on 9 Nov 2026. Laws change; confirm with counsel.

## At a glance

| Topic | What applies | Regulator or owner | Source |
|---|---|---|---|
| Personal data | Federal Law 152-FZ (27 Jul 2006, with amendments through 2026) | Roskomnadzor | [pd.rkn.gov.ru](https://pd.rkn.gov.ru/) |
| Data localization | 152-FZ Art. 18(5), as amended by 23-FZ (28 Feb 2025, in force 1 Jul 2025) | Roskomnadzor | pravo.gov.ru |
| Data leak penalties | 420-FZ (30 Nov 2024, in force 30 May 2025): KoAP Art. 13.11 parts 12 to 18; 421-FZ (30 Nov 2024, in force 11 Dec 2024): Criminal Code Art. 272.1 | Courts, Roskomnadzor | [rg.ru](https://rg.ru/2024/12/06/personalnye-dannye-dok.html) |
| Cross-border transfers | 152-FZ Art. 12; 265-FZ (26 Jul 2026) removed Convention 108 as a separate adequacy basis | Roskomnadzor | [rg.ru](https://rg.ru/documents/2026/08/03/fz265-dok.html) |
| Critical information infrastructure | 187-FZ (26 Jul 2017, in force 1 Jan 2018), amended by 58-FZ (7 Apr 2025, in force 1 Sep 2025) | FSTEC, FSB | [fstec.ru](https://fstec.ru/) |
| CII incident reporting | FSB Order No. 547 (25 Dec 2025, in force 30 Jan 2026) | FSB, GosSOPKA national coordination center | [safe-surf.ru](https://safe-surf.ru/) |
| State system incidents | FSB Order No. 297 (6 Aug 2026, in force 1 Sep 2026) | FSB | FSB |
| Foreign software ban on CII | Decree No. 166 (30 Mar 2022, amended by No. 887 and No. 214); Government Resolution 1912 (14 Nov 2023) | Government, sector regulators | Government decrees |
| Security tools | Decree No. 250 (1 May 2022, amended by No. 500): from 1 Jan 2025, covered bodies may not use information security tools from unfriendly countries | Government | Government Order 430-r |
| Domestic software in state procurement | Government Resolution 1236 (16 Nov 2015, in force 1 Jan 2016); register at reestr.digital.gov.ru | Ministry of Digital Development | [reestr.digital.gov.ru](https://reestr.digital.gov.ru/) |
| Cryptography | GOST R 34.12-2015 (Kuznyechik, Magma), GOST R 34.10-2012 (signatures), GOST R 34.11-2012 (Streebog); FSB certifies tools | FSB | FSB |
| AI | National AI Strategy (Decree 490, 10 Oct 2019, amended by Decree 124); experimental legal regimes under 258-FZ; no general AI statute | Government, Ministry of Digital Development | Government |
| Accessibility | GOST R 52872-2019 (in force 1 Apr 2020, based on WCAG 2.1) | Voluntary standard | GOST |
| Sanctions and export controls | US EO 14071 and OFAC determination of 12 Jun 2024; EU Regulation 833/2014 Art. 5n; UK SI 2019/855 reg. 54C | US OFAC, BIS; EU Council; UK OFSI | [OFAC](https://ofac.treasury.gov/), [EUR-Lex](https://eur-lex.europa.eu/eli/reg/2014/833/oj), [UK](https://www.legislation.gov.uk/uksi/2019/855/regulation/54C) |

## Laws and regulators

**Data protection.** Federal Law No. 152-FZ (27 Jul 2006) on personal data is the general statute. Operators must notify Roskomnadzor before processing personal data (Art. 22). Consent is the primary lawful basis; written consent in a prescribed form is needed for biometrics, cross-border transfers and certain other processing. Recent amendments include 519-FZ (28 Dec 2024), 121-FZ (23 May 2025), 156-FZ (24 Jun 2025) and 265-FZ (26 Jul 2026). Government Resolution 1119 (2012) sets protection levels for personal data information systems. FSTEC Order 21 sets the security measures. In practice: keep the playbook's data inventory and processing records, add a Roskomnadzor notification column, and collect consent in the form 152-FZ prescribes.

**Data localization.** Art. 18(5), as amended by 23-FZ (28 Feb 2025, in force 1 Jul 2025), requires that when collecting personal data of Russian citizens, including over the internet, using databases located outside Russia is not allowed, with limited exceptions (Art. 6(1) items 2, 3, 4 and 8). In practice: host the primary personal data database on Russian soil.

**Cross-border transfers.** Art. 12 requires the operator to notify Roskomnadzor before starting cross-border transfers and to assess the recipient. Roskomnadzor decides within 10 working days. Countries on its adequacy list may receive data right after notice; others must wait for the decision. Roskomnadzor may ban or restrict transfers. 265-FZ (26 Jul 2026, Art. 1 in force on official publication, Art. 2 from 1 Sep 2027) removed Convention 108 membership as a standalone adequacy basis; the Roskomnadzor list now governs. In practice: apply before you transfer and plan for the 10-day wait.

**Data leak penalties.** 420-FZ (30 Nov 2024, in force 30 May 2025) added scaled fines to KoAP Art. 13.11 (parts 12 to 18), based on the number of affected people and the type of data. Repeat leaks carry a turnover fine up to 3% of revenue, with a minimum of 20 million and a maximum of 500 million roubles. 421-FZ (30 Nov 2024, in force 11 Dec 2024) added Criminal Code Art. 272.1 on illegal use or transfer of personal data. In practice: these penalties make breach response and preventive controls a board-level topic.

**Breach notification.** Art. 21(3.1) requires notifying Roskomnadzor within 24 hours of a personal data leak (the incident, suspected causes, harm, measures and a contact person) and within 72 hours (results of the internal investigation and the persons responsible). Operators must also interact continuously with GosSOPKA (Art. 19(12)), under the procedure in FSB Order No. 77 (13 Feb 2023). In practice: build both the Roskomnadzor and GosSOPKA reporting paths into your [incident management](../../reliability/incident-management.md) runbook.

**Critical information infrastructure.** 187-FZ (26 Jul 2017, in force 1 Jan 2018) covers CII across 14 sectors. Subjects of CII categorize their objects under Government Resolution 127. FSTEC Order 239 sets the security requirements. 58-FZ (7 Apr 2025, in force 1 Sep 2025) removed individual entrepreneurs, added typical industry objects, and gave the Government powers over the transition to Russian software and hardware. FSTEC Order 254 (17 Jul 2025, from 1 Sep 2025) sets the registry format; Order 247 (11 Jul 2025) sets the categorization form. FSTEC Order 117 (11 Apr 2025) replaces Order 17 from 1 Mar 2026 for state information systems, including CII, and requires a threat model and MFA for privileged access. In practice: categorize each system, file with FSTEC, and prepare for the domestic software requirements.

**Foreign software restrictions.** Decree No. 166 (30 Mar 2022, amended by No. 887 of 22 Nov 2023 and No. 214 of 7 Apr 2025) banned buying foreign software for significant CII objects from 31 Mar 2022 and using it from 1 Jan 2025. Government Resolution 1912 (14 Nov 2023) sets a deadline of 1 Jan 2030 to move significant CII objects to trusted software-hardware complexes; untrusted ones bought after 1 Sep 2024 may not be used. Decree No. 250 (1 May 2022, amended by No. 500 of 13 Jun 2024) bans covered bodies from using information security tools from unfriendly countries from 1 Jan 2025 (country list in Government Order 430-r of 5 Mar 2022). Government Resolution 1236 (16 Nov 2015) bars foreign software from state procurement; the domestic software register is at reestr.digital.gov.ru. In practice: check each software component against the register and the restriction lists before procurement or deployment.

**Cryptography.** The FSB certifies cryptographic tools. National algorithms are GOST R 34.12-2015 (Kuznyechik and Magma block ciphers), GOST R 34.10-2012 (digital signatures) and GOST R 34.11-2012 (Streebog hash). For TLS 1.2, RFC 9189 defines Kuznyechik and Magma CTR_OMAC suites (0xC100, 0xC101). For TLS 1.3, RFC 9367 defines MGM suites (0xC103 to 0xC106). Neither RFC is IETF-endorsed as a standard. The Ministry of Digital Development publishes the Russian Trusted Root CA at gosuslugi.ru/crt; foreign browsers do not trust it by default. In practice: use FSB-certified GOST libraries, run dual-stack TLS (international algorithms plus GOST suites), and add the Russian Trusted Root CA to your internal trust store. Keep a [crypto inventory](../../../templates/docs/crypto-inventory.csv) with a GOST-approval column.

**AI.** No general AI statute exists. Decree 490 (10 Oct 2019, amended by Decree 124 of 15 Feb 2024) sets a national AI strategy to 2030. Experimental legal regimes under 258-FZ allow sandboxed AI deployment. In practice: follow the playbook's [AI governance](../../ai/ai-governance.md) register; add regulatory sandbox conditions if you operate under one.

**Accessibility.** GOST R 52872-2019 (in force 1 Apr 2020) covers web and app accessibility based on WCAG 2.1. It is a voluntary standard. In practice: test against GOST R 52872 alongside WCAG 2.2 AA.

**Internet presence.** 236-FZ (1 Jul 2021) requires foreign internet firms with more than 500,000 daily users in Russia to open a local branch and register with Roskomnadzor.

## Reporting clocks

| Event | Who must report | To whom | Deadline | Source |
|---|---|---|---|---|
| Personal data leak: initial notice | Personal data operator | Roskomnadzor | Within 24 hours | 152-FZ Art. 21(3.1) |
| Personal data leak: investigation results | Personal data operator | Roskomnadzor | Within 72 hours | 152-FZ Art. 21(3.1) |
| Computer incident at a significant CII object | CII subject | GosSOPKA national coordination center | Within 3 hours of detection | FSB Order No. 547 (30 Jan 2026) |
| Computer incident at other CII objects | CII subject | GosSOPKA national coordination center | Within 24 hours of detection | FSB Order No. 547 |
| Incident at a state information system | Operator | Coordination center, via personal account | Within 24 hours | FSB Order No. 297 (1 Sep 2026) |

## What changes in the playbook

| Playbook page | What to add or change in this region |
|---|---|
| [Data security and privacy](../../data/data-security-and-privacy.md) | Add 152-FZ to the laws-to-check table. Add the localization rule, the Roskomnadzor notification duty, and the cross-border transfer approval process. |
| [Incident management](../../reliability/incident-management.md) | Add Roskomnadzor 24-hour and 72-hour clocks, GosSOPKA 3-hour and 24-hour clocks, and the FSB Order 297 state-system clock to the Assured table. |
| [Control mapping](../control-mapping.md) | Add GOST R 57580.1-2017 for financial firms and the FSTEC Order 239 requirements for CII. Note that FSTEC and FSB frameworks, not ISO 27001, govern CII and state systems. |
| [Cloud, on-prem, air-gapped](../../platform/cloud-on-prem-air-gapped.md) | Add domestic cloud providers (Yandex Cloud, VK Cloud, Cloud.ru). US hyperscalers run no regions in Russia. Mirror container images and verify signatures locally; some foreign registries restrict access. Use RuStore for Android distribution. Yandex Maps and 2GIS replace Google Maps. ESIA (Gosuslugi) is the citizen identity provider; use self-hosted Keycloak or similar for staff. Self-hosted Forgejo or GitLab with cosign key-pair signing replaces GitHub and public Sigstore. |
| [Post-quantum readiness](../../security/post-quantum-readiness.md) | Note that Russia approves cryptographic algorithms nationally through the FSB; GOST algorithms have no NIST equivalent. |
| [Vulnerability management](../../security/vulnerability-management.md) | Add the FSTEC vulnerability database (BDU, bdu.fstec.ru) alongside CISA KEV. |
| [Supply chain](../../security/supply-chain.md) | Replace public Sigstore with cosign key-pair signing and a self-hosted transparency log. Mirror upstream sources behind an internal proxy and verify checksums. |
| [AI governance](../../ai/ai-governance.md) | Note the experimental legal regime option under 258-FZ. |
| [Third-party and SaaS risk](../../security/third-party-and-saas-risk.md) | Add sanctions and export-control screening. Screen each supplier and customer against the US SDN list, EU consolidated list and UK sanctions list before signing. US, EU and UK rules restrict IT services and software supply to Russian entities. |
| [Build, buy, adopt](../../strategy/build-buy-adopt.md) | For CII, foreign software is banned on significant objects from 1 Jan 2025. State procurement requires domestic-register software. Screen the domestic software register at reestr.digital.gov.ru. |
| [Suppliers and contracts](../../strategy/suppliers-and-contracts.md) | Add sanctions screening to vendor onboarding. Include a termination clause for sanctions changes. |
| [Public sector](../public-sector.md) | Add Russia data localization, FSTEC and FSB requirements, the domestic software register, and GOST accessibility. |
| [Secrets](../../security/secrets.md) | Store GOST keys with the same controls. Note that FSB certification applies to key management modules. |

## Public sector

Government systems are classified as state information systems under FSTEC Order 117 (replacing Order 17 from 1 Mar 2026). They follow FSTEC security requirements, which include a threat model, MFA for privileged access and regular audits. Software must be on the domestic software register (reestr.digital.gov.ru). Information security tools must not come from unfriendly countries (Decree 250). CII objects in government follow 187-FZ and the FSTEC and FSB requirements above. The Russian Trusted Root CA and GOST TLS are expected for government-facing services. Data classification follows Government Resolution 1119 (2012). State secrets follow a separate regime.

## Financial services

- **Bank of Russia.** Instruction 683-P sets information protection requirements for credit institutions, referencing GOST R 57580.1-2017. Instruction 787-P (in force 1 Oct 2022) covers operational resilience. FinCERT, the Bank of Russia's incident response center, receives incident reports.
- **GOST R 57580.** The standard covers information protection for financial organizations at two levels; compliance is assessed by licensed auditors.
- **Domestic software.** Banks that are CII subjects face the same foreign-software restrictions as other CII operators.
- **Cross-border.** Financial data transfers follow both 152-FZ Art. 12 and Bank of Russia sector rules.

## Deadlines to watch, 2026 to 2028

| Date | What happens |
|---|---|
| In force | 152-FZ localization (1 Jul 2025); data leak fines 420-FZ (30 May 2025); criminal liability 421-FZ (11 Dec 2024) |
| In force | Foreign software ban on significant CII (1 Jan 2025); security-tool ban for covered bodies (1 Jan 2025) |
| In force | FSB Order 547 incident reporting (30 Jan 2026); FSB Order 297 state-system reporting (1 Sep 2026) |
| In force | 58-FZ CII amendments (1 Sep 2025); FSTEC Orders 254 and 247 (1 Sep 2025) |
| 1 Sep 2027 | 265-FZ Art. 2 on cross-border transfer provisions takes effect |
| 1 Mar 2026 | FSTEC Order 117 replaces Order 17 for state information systems |
| 1 Jan 2030 | Government Resolution 1912 deadline: significant CII objects on trusted software-hardware complexes |
| Rolling | Roskomnadzor may update the adequacy list for cross-border transfers |

## Sources

- Roskomnadzor personal data portal: https://pd.rkn.gov.ru/
- Official publication of federal laws: https://pravo.gov.ru/
- Rossiyskaya Gazeta (official publication outlet): https://rg.ru/
- 265-FZ (26 Jul 2026): https://rg.ru/documents/2026/08/03/fz265-dok.html
- 421-FZ (30 Nov 2024): https://rg.ru/2024/12/06/personalnye-dannye-dok.html
- FSTEC: https://fstec.ru/
- FSTEC vulnerability database (BDU): https://bdu.fstec.ru/
- GosSOPKA and incident coordination: https://safe-surf.ru/
- Bank of Russia: https://cbr.ru/
- Domestic software register: https://reestr.digital.gov.ru/
- GOST R 34.12-2015, R 34.10-2012, R 34.11-2012: national standardization body
- RFC 9189, GOST cipher suites for TLS 1.2: https://www.rfc-editor.org/rfc/rfc9189
- RFC 9367, GOST cipher suites for TLS 1.3: https://www.rfc-editor.org/rfc/rfc9367
- Russian Trusted Root CA: https://gosuslugi.ru/crt
- OFAC determination of 12 Jun 2024 under EO 14071: https://ofac.treasury.gov/system/files/2024-06/determination_06122024_eo14071.pdf
- EU Council Regulation 833/2014: https://eur-lex.europa.eu/eli/reg/2014/833/oj
- EU Commission FAQ on software sanctions: https://finance.ec.europa.eu/system/files/2024-02/faqs-sanctions-russia-software_en%2C.pdf
- UK Russia sanctions, regulation 54C: https://www.legislation.gov.uk/uksi/2019/855/regulation/54C
- DOJ National Security Division, Data Security Program: https://www.justice.gov/nsd/data-security
