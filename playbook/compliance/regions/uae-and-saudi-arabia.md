# UAE and Saudi Arabia: what changes when you apply this playbook

This guide is for engineering leaders, security teams and compliance staff who build or run software in the United Arab Emirates (UAE) or the Kingdom of Saudi Arabia (KSA), or process data of their residents. The playbook's legal defaults are written around EU law. Three differences matter most in the Gulf. First, both countries enforce data localisation and sector-specific residency rules that go beyond GDPR transfer mechanisms, and Saudi Arabia requires cybersecurity monitoring centres to operate from inside the Kingdom. Second, you face several parallel regulators and free-zone regimes rather than one data protection authority: in the UAE, the federal Personal Data Protection Law (PDPL), the DIFC Data Protection Law and the ADGM Data Protection Regulations each apply in their own territory; in KSA, the Saudi Data and Artificial Intelligence Authority (SDAIA), the National Cybersecurity Authority (NCA), the Saudi Central Bank (SAMA) and the Communications, Space and Technology Commission (CST) each issue binding rules. Third, Arabic is the binding language for Saudi NCA controls and most Gulf legislation, and public-facing services must support right-to-left (RTL) interfaces.

> Not legal advice. Facts checked against primary sources on 9 Nov 2026. Laws change; confirm with counsel.

## At a glance

| Topic | What applies | Regulator or owner | Source |
|---|---|---|---|
| Data protection (UAE federal) | Federal Decree-Law No. 45/2021 (PDPL) | UAE Data Office (absorbed into the Federal Authority for AI and Data, Jun 2026; unverified) | [u.ae](https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws) |
| Data protection (DIFC) | DIFC Law No. 5/2020 (Data Protection Law), as amended 2022 and 2025 | Commissioner of Data Protection, DIFC | [DIFC legal database](https://www.difc.com/business/laws-and-regulations/legal-database/difc-laws/data-protection-law-difc-law-no-5-2020) |
| Data protection (ADGM) | Data Protection Regulations 2021 | Office of Data Protection, ADGM | [ADGM](https://www.adgm.com) |
| Cybersecurity (UAE) | UAE IA Regulation v1.1 (TDRA, 2020) | Cyber Security Council | [government.ae](https://government.ae) |
| Cybersecurity (Dubai) | Dubai Information Security Regulation (ISR), Resolution No. 13/2012, Law No. 11/2014 | Dubai Electronic Security Centre (DESC) | [DESC](https://www.desc.gov.ae/regulations/standards-policies/) |
| Data protection (KSA) | Royal Decree M/19 (PDPL), amended by M/148; Implementing Regulation (Aug 2024) | SDAIA | [SDAIA portal](https://dgp.sdaia.gov.sa) |
| Cross-border transfers (KSA) | Regulation on Personal Data Transfer outside the Kingdom v2.0 (Aug 2024) | SDAIA | [SDAIA portal](https://dgp.sdaia.gov.sa) |
| Cybersecurity (KSA) | Essential Cybersecurity Controls (ECC-2:2024), Cloud Cybersecurity Controls (CCC-2:2024), Data Cybersecurity Controls (DCC), National Cryptographic Standards (NCS) | NCA | [NCA](https://nca.gov.sa/en/regulatory-documents/controls-list/) |
| Financial services (KSA) | SAMA Cyber Security Framework (CSF, Circular 381000091275, May 2017); BCM Framework (Feb 2017) | Saudi Central Bank (SAMA) | [SAMA Rulebook](https://rulebook.sama.gov.sa) |
| Financial services (UAE) | CBUAE Operational Risk Management Regulation, Circular 1/2026 (effective Sep 2026; unverified against the Rulebook) | Central Bank of the UAE (CBUAE) | [CBUAE](https://centralbank.ae) |
| Cloud (KSA) | Cloud Computing Services Provisioning Regulations, Decision 506/1445 (Oct 2023); Cloud First Policy (MCIT, draft 2019) | CST; MCIT | [CST](https://www.cst.gov.sa/en/regulations-and-licenses/regulations/cloud-computing-services-provisioning-regulations) |
| AI (KSA) | SDAIA AI Ethics Principles v2.0 (Sep 2023; unverified); Generative AI guidelines (Jan 2024; unverified) | SDAIA | [SDAIA](https://sdaia.gov.sa) |
| AI (UAE) | UAE Charter for the Development and Use of AI (Jun 2024, 12 principles, non-binding) | AI Office | [u.ae](https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/policies/Ai/The-UAE-Charter-for-the-Development-and-Use-of-Artificial-Intelligence) |
| Accessibility (KSA) | Law of the Rights of Persons with Disabilities, Resolution No. 110/1445H; DGA WCAG 2.1 AA policy (unverified) | Authority for the Care of Persons with Disabilities; DGA | [hrsd.gov.sa](https://hrsd.gov.sa) |
| Accessibility (UAE) | National Digital Accessibility Policy (Cabinet); federal entities cite W3C WCAG | TDRA | [u.ae](https://u.ae) |

## Laws and regulators

### UAE

**Data protection.** Federal Decree-Law No. 45/2021 (in force 2 Jan 2022) is the UAE's federal data protection law. It applies outside the DIFC and ADGM. Executive regulations had not been issued as far as could be confirmed as of the date of this guide, which leaves several operational details (processor obligations, transfer mechanisms, specific breach timelines) undefined. Art. 9 requires breach notification to the Data Office "immediately" or within a period the regulations will set (unverified against the law text). The DIFC and ADGM each have their own data protection frameworks and supervisory bodies.

**DIFC.** DIFC Law No. 5/2020 (in force 1 Jul 2020, consolidated Jul 2025) follows a GDPR-like model. Art. 41 requires controllers to notify the Commissioner of a breach "as soon as practicable in the circumstances". A processor must tell the controller without undue delay (Art. 41). Data subjects must be told of high-risk breaches (Art. 42). Cross-border transfers require adequacy findings or appropriate safeguards (Arts. 26, 27). Data Protection Regulations (consolidated v2, in force 1 Sep 2023) include Regulation 10 on personal data processed through autonomous and semi-autonomous systems.

**ADGM.** The Data Protection Regulations 2021 (enacted 11 Feb 2021, in effect 14 Aug 2021 for new entities, 14 Feb 2022 for existing ones) require breach notification to the Office of Data Protection without undue delay and, where feasible, within 72 hours.

**Cybersecurity.** The UAE IA Regulation v1.1 (TDRA, 2020) sets information assurance controls for federal entities. The Cyber Security Council oversees national cyber policy. In Dubai, the DESC enforces the ISR for government entities. Federal Decree-Law 34/2021 on combating rumours and cybercrimes covers unauthorised access and data interference. A UAE Cyber Security Council IA Standard v2 (2025) has been reported but is unverified.

**Financial services.** CBUAE Circular 1/2026 (Operational Risk Management Regulation, effective 14 Sep 2026; unverified against the CBUAE Rulebook) requires notification within 4 hours of a material event affecting critical operations, a summary report within 24 hours, and notification of high-risk incidents within 72 hours. It requires the master system of record to remain in the UAE. Material changes to critical operations require 30 days' notice and written CBUAE no-objection. Federal Decree-Law No. 6/2025 reorganises CBUAE supervisory powers (effective 16 Sep 2025 with one-year regularisation).

**AI.** The UAE Charter for the Development and Use of AI (Jun 2024) sets 12 non-binding principles. In Jun 2026, the Cabinet created the Federal Authority for AI and Data, absorbing the UAE Data Office, the TDRA digital government sector and the AI Office (unverified; the Cabinet page could not be read when checked).

### Saudi Arabia

**Data protection.** The Personal Data Protection Law (PDPL), Royal Decree M/19 (published 24 Sep 2021, secondary), amended by Royal Decree M/148, is enforced by SDAIA. The Implementing Regulation (Aug 2024) sets operational rules. Art. 24(1) of the Implementing Regulation requires the controller to notify SDAIA within 72 hours of becoming aware of a breach that could harm the data or the data subject. Data subjects must be notified without undue delay if the breach may harm them (Art. 24(5)). Penalties: up to SAR 5 million per violation (Art. 36), doubled for repeat violations; up to 2 years' prison and SAR 3 million for intentional disclosure of sensitive data (Art. 35). Draft amendments under consultation (6 Oct to 5 Nov 2026) would remove the harm threshold for SDAIA notification.

**Cross-border transfers.** The Regulation on Personal Data Transfer v2.0 (Aug 2024) permits transfers under standard contractual clauses (SCCs), binding common rules, or accreditation certificates (Art. 4). A risk assessment is needed for transfers using those safeguards, or for continuous or large-scale transfers of sensitive data (Art. 7). SDAIA has published template SCCs. Special economic zones and cities are treated like states for adequacy assessment.

**Cybersecurity.** The NCA issues binding controls for government entities, their companies and private entities that own, operate or host critical national infrastructure (CNI). ECC-2:2024 has 4 domains, 28 subdomains and 108 controls. Key requirements: an independent cybersecurity department separate from IT (ECC 1-2-1); all cybersecurity positions filled by full-time, qualified Saudi nationals (ECC 1-2-2); cryptography meeting the NCS (ECC 2-8-3); managed security operations centres located in the Kingdom (ECC 4-1-3-2); cloud controls binding on entities using or planning to use cloud (ECC subdomain 4-2). CCC-2:2024 applies to cloud service providers and to tenants in ECC scope, including Saudi-national staffing for CSP data centre cybersecurity roles (CCC 1-4-P-1-1). Incidents must be reported to the NCA (ECC 2-13-3-3); the deadline is "immediately" per secondary sources (unverified against NCA primary text). Data localisation rules formerly in the ECC and CCC have moved to the NDMO at SDAIA. The NCA also publishes the DCC, OTCC (industrial control systems), TCC and NCS.

**Cloud.** The CST Cloud Computing Services Provisioning Regulations (Decision 506/1445, Oct 2023) set licensing and data classification rules for cloud providers. The MCIT Cloud First Policy (draft, Feb 2019) directs civilian government entities to prefer SaaS over PaaS over IaaS and to avoid building new data centres, with exceptions.

**Financial services.** The SAMA Cyber Security Framework (May 2017) requires regulated entities to inform SAMA IT Risk Supervision immediately of medium or high classified security incidents (CSF 3.3.15). SAMA requires written no-objection before any media interaction about an incident. A formal incident report is due after operations resume. The BCM Framework (Feb 2017) mirrors the immediate reporting duty for incidents affecting customers (BCM 3.3.8). SAMA non-objection is required for material outsourcing by finance companies.

**AI.** SDAIA published AI Ethics Principles v2.0 (Sep 2023, unverified) and Generative AI guidelines for government and the public (Jan 2024, unverified). These are guidance, not binding legislation.

**Accessibility.** The Law of the Rights of Persons with Disabilities (Resolution No. 110/1445H) sets general accessibility rights. The Digital Government Authority (DGA) requires WCAG 2.1 AA for government services (unverified). Teams should target WCAG 2.2 AA, which covers both versions, and support Arabic RTL interfaces.

**Cryptography.** The NCA's National Cryptographic Standards (NCS) set minimum requirements. ECC 2-8-3 requires entities in scope to meet the NCS. Teams should confirm whether imported cryptographic products need a licence.

## Reporting clocks

| Event | Who must report | To whom | Deadline | Source |
|---|---|---|---|---|
| Personal data breach (KSA) | Controller | SDAIA | 72 hours from awareness (if breach could cause harm) | Art. 24(1), PDPL Implementing Regulation |
| Breach harming data subjects (KSA) | Controller | Affected data subjects | Without undue delay | Art. 24(5), PDPL Implementing Regulation |
| Cybersecurity incident (KSA, NCA scope) | Entity in scope | NCA | Immediately (unverified) | ECC 2-13-3-3; secondary sources |
| Security incident (KSA, SAMA) | Regulated entity | SAMA IT Risk Supervision | Immediately for medium or high incidents | CSF 3.3.15, SAMA Rulebook |
| Personal data breach (UAE federal) | Controller | UAE Data Office | Immediately, or per regulations (not yet issued) | Art. 9, Federal Decree-Law 45/2021 (unverified) |
| Personal data breach (DIFC) | Controller | DIFC Commissioner | As soon as practicable | Art. 41, DIFC Law 5/2020 |
| Personal data breach (ADGM) | Controller | ADGM Office of Data Protection | Without undue delay, within 72 hours where feasible | ADGM Data Protection Regulations 2021 |
| Material event, critical ops (UAE, CBUAE) | Regulated entity | CBUAE | 4 hours; summary report within 24 hours | Circular 1/2026 (unverified against Rulebook) |

## What changes in the playbook

| Playbook page | What to add or change in this region |
|---|---|
| [Data security and privacy](../../data/data-security-and-privacy.md) | Add KSA 72-hour and UAE "immediately" breach clocks. Add SDAIA transfer safeguards (SCCs, binding common rules, risk assessment). Add DIFC and ADGM regimes. Note that UAE federal executive regulations are pending. |
| [Incident management](../../reliability/incident-management.md) | Add the Gulf rows from the reporting clocks table. Note the SAMA "immediately" clock and media no-objection rule. |
| [Control mapping](../control-mapping.md) | Add NCA ECC-2:2024 and SAMA CSF columns. Map ECC controls (independent security department, Saudi-national staffing, NCS cryptography, in-Kingdom SOC) to playbook practices. |
| [Regulated industries](../regulated-industries.md) | Add SAMA CSF, BCM and outsourcing rules. Add CBUAE Circular 1/2026 requirements (4-hour clock, in-UAE system of record, no-objection for material changes). |
| [Public sector](../public-sector.md) | Add KSA government cloud-first policy (SaaS over PaaS over IaaS). Add UAE DESC ISR for Dubai government. Note that procurement uses national platforms (secondary). |
| [Cloud, on-prem, air-gapped](../../platform/cloud-on-prem-air-gapped.md) | Add KSA in-Kingdom SOC and monitoring requirements (ECC 4-1-3-2). Add CST cloud licensing. Note that data localisation rules sit with the NDMO (SDAIA). Add CBUAE in-UAE system-of-record rule. |
| [AI governance](../../ai/ai-governance.md) | Add UAE AI Charter (12 principles, non-binding). Add SDAIA AI Ethics Principles and Gen AI guidelines. Note DIFC Regulation 10 on AI and personal data. |
| [Accessibility testing](../../quality/accessibility-testing.md) | Target WCAG 2.2 AA. Add Arabic RTL interface requirement. Note KSA DGA and UAE TDRA accessibility policies. |
| [Post-quantum readiness](../../security/post-quantum-readiness.md) | Align with NCA NCS. Check import licence requirements for cryptographic products. |
| [For financial services](../../../leaders/for-financial-services.md) | Add SAMA CSF and CBUAE Circular 1/2026. Note the SAMA media no-objection rule. |
| [For government](../../../leaders/for-government.md) | Add Gulf procurement context (national platforms, not open-source-first by default). Add Arabic and RTL as required for public-facing services. |

## Public sector

**KSA.** Government entities fall under NCA controls (ECC, CCC). The Cloud First Policy directs agencies to adopt cloud (SaaS preferred) rather than build data centres. Procurement runs through the Etimad framework (secondary; unverified). The DGA sets digital government standards. Arabic is the primary interface language; the Arabic text of NCA controls is binding.

**UAE.** Federal entities follow the UAE IA Regulation (TDRA). Dubai government entities follow the DESC ISR. The UAE has a digital government strategy administered through the TDRA (now partly under the Federal Authority for AI and Data). Public services must meet the National Digital Accessibility Policy and support Arabic.

**Both.** The playbook's assumption of open-source-first procurement and publishing code openly does not hold by default. Government contracts may restrict code sharing. The working week differs from Western defaults: the UAE federal working week is Monday to Friday, with Friday afternoon off. KSA observes a Friday to Saturday weekend. Plan release and on-call schedules accordingly.

## Financial services

**KSA (SAMA).** The Cyber Security Framework applies to all SAMA-regulated entities (banks, insurers, finance companies, payment service providers). It requires a board-approved cyber strategy, an independent cyber function, regular penetration testing, and the immediate-reporting duties described above. SAMA non-objection is needed for material outsourcing. The PDPL (Art. 30) preserves SAMA's supervisory powers over financial sector personal data.

**UAE (CBUAE).** The Operational Risk Management Regulation (Circular 1/2026, effective Sep 2026; unverified) applies to CBUAE-licensed institutions. It requires a master system of record in the UAE, 4-hour notification for material events, and 30 days' notice plus written no-objection for material changes to critical operations. Teams must confirm requirements against the CBUAE Rulebook once the regulation takes effect.

## Deadlines to watch, 2026 to 2028

| Date | What happens | Source |
|---|---|---|
| 14 Sep 2026 | CBUAE Circular 1/2026 effective date (unverified) | Secondary sources |
| 16 Sep 2026 | End of CBUAE regularisation period under Decree-Law 6/2025 (secondary) | Secondary sources |
| Late 2026 | Saudi PDPL Implementing Regulation draft amendments (consultation closed 5 Nov 2026) may take effect | [SDAIA portal](https://dgp.sdaia.gov.sa) |
| Ongoing | UAE federal PDPL executive regulations expected; will set breach timelines and transfer rules | [u.ae](https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws) |
| Ongoing | NCA may update controls or issue new frameworks (NCNICC-1:2025 for non-CNI private entities reported Dec 2025; unverified) | [NCA](https://nca.gov.sa) |
| 2027 to 2028 | DIFC and ADGM may update regulations following the 2025 DIFC amendments | [DIFC](https://www.difc.com) |

## Sources

- UAE Federal Decree-Law No. 45/2021 on personal data protection: https://u.ae/en/about-the-uae/digital-uae/data/data-protection-laws
- UAE Charter for the Development and Use of AI (2024): https://u.ae/en/about-the-uae/strategies-initiatives-and-awards/policies/Ai/The-UAE-Charter-for-the-Development-and-Use-of-Artificial-Intelligence
- DIFC Data Protection Law No. 5/2020 (consolidated): https://www.difc.com/business/laws-and-regulations/legal-database/difc-laws/data-protection-law-difc-law-no-5-2020
- ADGM Data Protection Regulations 2021: https://www.adgm.com
- DESC regulations and standards: https://www.desc.gov.ae/regulations/standards-policies/
- CBUAE legislation: https://centralbank.ae/en/legislation
- Saudi PDPL, Implementing Regulation, Transfer Regulation and SCCs: https://dgp.sdaia.gov.sa
- NCA ECC-2:2024: https://cdn.nca.gov.sa/api/files/public/upload/86e09090-44e4-481f-bc28-355673607654_ECC--2024-EN.pdf
- NCA CCC-2:2024: https://cdn.nca.gov.sa/api/files/public/upload/6d5408a3-d8e6-4e96-963b-2c7198e5b7c2_CCC-2-2024-EN-.pdf
- NCA regulatory documents: https://nca.gov.sa/en/regulatory-documents/controls-list/
- SAMA Cyber Security Framework: https://rulebook.sama.gov.sa
- SAMA BCM Framework: https://sama.gov.sa/en-US/RulesInstructions/CyberSecurity/Business%20Continuity%20Management%20Framework.pdf
- CST Cloud Computing Services Provisioning Regulations: https://www.cst.gov.sa/en/regulations-and-licenses/regulations/cloud-computing-services-provisioning-regulations
- MCIT Cloud First Policy (draft): https://www.mcit.gov.sa/sites/default/files/ksa_cloud_first_policy_en.pdf
- KSA Law of the Rights of Persons with Disabilities: https://hrsd.gov.sa
- NCA incident reporting: https://nca.gov.sa/en/report-incident
