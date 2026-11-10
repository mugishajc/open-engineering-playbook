# United States: what changes when you apply this playbook

This page is for engineering, security and compliance leads who build or run software for US customers, for federal, state or local government, or for US-regulated firms. Three things differ most from the playbook's EU-centered defaults. First, there is no single federal privacy or cyber security law. Duties come from sector rules (HIPAA, GLBA, SEC, the banking agencies, NYDFS) and from state laws, so list obligations per sector and per state. Second, selling to government is gated by programs you must pass before the first contract: FedRAMP for cloud, DFARS and CMMC for defense, FIPS-validated cryptography and the federal post-quantum dates. Third, incident clocks differ in their trigger as well as their length. The SEC clock runs from a materiality determination, the banking clock from determining a notification incident, and state breach clocks are counted in days.

> Not legal advice. Facts checked against primary sources on 9 Nov 2026. Laws change; confirm with counsel.

## At a glance

| Topic | What applies | Regulator or owner | Source |
|---|---|---|---|
| Security framework | NIST Cybersecurity Framework (CSF) 2.0, published 26 Feb 2024; NIST SP 800-53 Rev. 5 for federal systems | NIST | [CSF 2.0](https://www.nist.gov/cyberframework) |
| Secure development | NIST SSDF (SP 800-218); the federal attestation form is optional since OMB M-26-05 (23 Jan 2026) | OMB, CISA | [M-26-05](https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf) |
| Federal cloud | FedRAMP Consolidated Rules for 2026, mandatory from 1 Jan 2027 | GSA FedRAMP | [fedramp.gov](https://www.fedramp.gov/2026/timeline/) |
| Defense contractors | DFARS 252.204-7012 and NIST SP 800-171; CMMC (32 CFR part 170) Phase 1 self-assessments; Phase 2 suspended on 13 Jul 2026 | Department of War CIO | [CMMC](https://dowcio.war.gov/CMMC/About) |
| Listed companies | Form 8-K Item 1.05 and Regulation S-K Item 106 | SEC | [Release 33-11216](https://www.sec.gov/rules-regulations/2023/07/s7-09-22) |
| Critical infrastructure | CIRCIA: reporting not required until CISA's final rule takes effect | CISA | [CISA CIRCIA](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia) |
| Health | HIPAA Privacy, Security and Breach Notification Rules (45 CFR parts 160 and 164) | HHS Office for Civil Rights | [HHS HIPAA](https://www.hhs.gov/hipaa) |
| Non-bank financial firms | GLBA Safeguards Rule (16 CFR part 314) | FTC | [FTC Safeguards Rule](https://www.ftc.gov/business-guidance/resources/ftc-safeguards-rule-what-your-business-needs-know) |
| Banks | 36-hour incident notification rule; model risk guidance SR 26-2 | OCC, Federal Reserve, FDIC | [SR 26-2](https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm) |
| New York financial firms | 23 NYCRR Part 500 | NYDFS | [Part 500](https://www.dfs.ny.gov/system/files/documents/2023/10/rf_fs_2amend23NYCRR500_text_20231101.pdf) |
| Consumer privacy | State laws, led by the California Consumer Privacy Act (CCPA) and its regulations | California Privacy Protection Agency, state attorneys general | [CPPA](https://cppa.ca.gov/regulations/ccpa_updates.html) |
| Bulk data leaving the US | DOJ Data Security Program (28 CFR part 202) | DOJ National Security Division | [DOJ NSD](https://www.justice.gov/nsd/data-security) |
| AI | No federal AI statute; state laws (Colorado, Texas, California); OMB M-25-21 for agencies | States; OMB | [Colorado SB 26-189](https://leg.colorado.gov/bills/sb26-189) |
| Accessibility | Section 508 (federal); ADA Title II rule (state and local government) | US Access Board; DOJ | [91 FR 20902](https://www.govinfo.gov/content/pkg/FR-2026-04-20/html/2026-07663.htm) |
| Cryptography | FIPS 140-3 modules; post-quantum dates in EO 14412 and OMB M-26-15; export rules in the EAR | NIST, OMB, Commerce BIS | [EO 14412](https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/) |

## Laws and regulators

**Data protection.** No general federal privacy law exists. Sector laws apply instead. The Health Insurance Portability and Accountability Act (HIPAA, 1996) works through 45 CFR parts 160 and 164. The Gramm-Leach-Bliley Act (GLBA, 1999) covers financial institutions. The Children's Online Privacy Protection Act works through 16 CFR part 312. The FTC also treats unreasonable data security as an unfair practice under Section 5 of the FTC Act (15 U.S.C. 45). Many states now have general consumer privacy laws; check each state where you have customers. California's CCPA, as amended by the California Privacy Rights Act (Civil Code 1798.100 and following), is the most demanding. CPPA regulations in force since 1 Jan 2026 add risk assessments, cybersecurity audits and rules for automated decision-making technology (ADMT). In practice: keep the playbook's data inventory and classification, add a per-state obligations list, and plan the CCPA audit evidence now.

**Breach notification.** Each state has its own law. California Civil Code 1798.82, as amended by SB 446 from 1 Jan 2026, requires notice to affected residents within 30 calendar days of discovery, with limited exceptions. When more than 500 residents are affected, a sample notice goes to the Attorney General within 15 days of notifying them. Build the playbook's [breach register](../../data/data-security-and-privacy.md) with one column per state clock.

**Cyber security.** NIST CSF 2.0 (26 Feb 2024) is voluntary but is the shared language of US regulators, insurers and boards; it added a Govern function. Federal systems follow the Federal Information Security Modernization Act of 2014 (44 U.S.C. 3551 and following), NIST SP 800-53 Rev. 5 and an authority to operate (ATO). SOC 2 remains the usual evidence for business-to-business software, as the [control mapping](../control-mapping.md) shows.

**Critical infrastructure.** The Cyber Incident Reporting for Critical Infrastructure Act of 2022 (CIRCIA) requires reports of covered cyber incidents within 72 hours and of ransom payments within 24 hours. The duty starts only when CISA's final rule takes effect. CISA's page says it continues to work on the final rule and that reports are not required until then. Write the 72-hour and 24-hour paths into your runbook now so the switch is a configuration change.

**Financial services.** See [Financial services](#financial-services) below.

**Public sector.** See [Public sector](#public-sector) below.

**AI.** There is no federal AI statute. Executive Order 14365 (11 Dec 2025) directs the Attorney General to set up a task force to challenge state AI laws. State laws apply until they are changed or struck down. Colorado SB 26-189 (signed 14 May 2026) repealed and re-enacted the 2024 Colorado AI Act (SB 24-205) as an ADMT law. From 1 Jan 2027 developers give deployers technical documentation. Deployers give consumers notice, an explanation within 30 days of an adverse decision, correction and human review. Both keep records for 3 years. Check the act for the start date of each deployer duty. Texas HB 149 (Texas Responsible Artificial Intelligence Governance Act) and California SB 53 (Transparency in Frontier Artificial Intelligence Act) apply from 1 Jan 2026. Federal agencies follow OMB M-25-21 (use) and M-25-22 (acquisition), both 3 Apr 2025. The NIST AI RMF is voluntary. Map these to the [AI use-case register](../../ai/ai-governance.md).

**Accessibility.** Section 508 of the Rehabilitation Act (29 U.S.C. 794d) covers federal technology; the Revised 508 Standards (36 CFR part 1194) incorporate WCAG 2.0 level AA. The DOJ's 2024 rule under ADA Title II (28 CFR part 35, subpart H) sets WCAG 2.1 level AA for state and local government web content and mobile apps. The interim final rule of 20 Apr 2026 (91 FR 20902) moved compliance to 26 Apr 2027 for public entities serving 50,000 people or more. Smaller ones and special districts have until 26 Apr 2028. Targeting WCAG 2.2 AA, as the playbook does, meets both.

**Cryptography.** Federal systems use cryptographic modules validated by the NIST Cryptographic Module Validation Program; new validations are under FIPS 140-3. Executive Order 14412 (22 Jun 2026) covers high value assets and high impact systems. Agencies move them to post-quantum key establishment by 31 Dec 2030 and to post-quantum signatures by 31 Dec 2031. It also directs the FAR Council to propose a rule requiring covered contractors to comply with NIST FIPS, including post-quantum standards, by 31 Dec 2030. OMB M-26-15 (24 Jun 2026) sets the phases to full migration by 2035 and restates, from Executive Order 14306, that agencies support TLS 1.3 by 2 Jan 2030. National security systems follow NSA CNSA 2.0. Exports of encryption items fall under the Export Administration Regulations (EAR), Category 5 Part 2, usually through License Exception ENC (15 CFR 740.17). On 13 May 2025 Commerce announced it would not enforce the January 2025 AI Diffusion rule and would replace it. The current status of controls on AI model weights is unverified here. Ask export counsel before you ship model weights abroad. Screen customers against the Entity List and embargoed destinations.

**Data localization and cross-border transfers.** No general localization law exists. The DOJ Data Security Program (28 CFR part 202) has applied since 8 Apr 2025, with due diligence, audit and reporting duties from 6 Oct 2025. It prohibits or restricts transactions that give countries of concern or covered persons access to bulk US sensitive personal data or government-related data. Vendor, employment and investment agreements can all be covered. Contracts add their own limits, for example DFARS 252.239-7010 for Department of War data in commercial cloud. For data arriving from the EU, see the EU-US Data Privacy Framework in [data security and privacy](../../data/data-security-and-privacy.md).

## Reporting clocks

| Event | Who must report | To whom | Deadline | Source |
|---|---|---|---|---|
| Material cybersecurity incident | SEC registrants | Investors, through Form 8-K Item 1.05 | 4 business days after determining materiality; the determination must be made without unreasonable delay; the Attorney General can authorize a delay | [SEC](https://www.sec.gov/rules-regulations/2023/07/s7-09-22) |
| Computer-security incident that is a notification incident | Banks | Primary federal regulator | As soon as possible, no later than 36 hours after determining it occurred | [12 CFR part 53](https://www.ecfr.gov/current/title-12/chapter-I/part-53) |
| Incident that disrupts services for 4 hours or more | Bank service providers | Each affected bank customer | As soon as possible | [12 CFR part 53](https://www.ecfr.gov/current/title-12/chapter-I/part-53) |
| Cybersecurity incident; extortion payment | NYDFS covered entities | NYDFS | 72 hours from determination; payment notice within 24 hours and written reasons within 30 days | [23 NYCRR 500.17](https://www.dfs.ny.gov/system/files/documents/2023/10/rf_fs_2amend23NYCRR500_text_20231101.pdf) |
| Unencrypted customer information of 500 or more consumers acquired | Financial institutions under FTC jurisdiction | FTC, through its online form | No later than 30 days after discovery | [FTC](https://www.ftc.gov/business-guidance/blog/2024/05/safeguards-rule-notification-requirement-now-effect) |
| Unauthorized access to sensitive customer information | Broker-dealers, investment advisers and other Regulation S-P institutions | Affected individuals | No later than 30 days after becoming aware | [SEC](https://www.sec.gov/newsroom/press-releases/2024-58) |
| Breach of unsecured protected health information | HIPAA covered entities (business associates tell the covered entity) | Individuals; HHS; media when more than 500 residents of a state | Individuals within 60 days of discovery; HHS at the same time when 500 or more, otherwise within 60 days of the year end | [45 CFR 164.404 to 164.410](https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D) |
| Cyber incident affecting covered defense information | Department of War contractors | Department of War, through DIBNet | 72 hours from discovery | [DFARS 252.204-7012](https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.) |
| Covered cyber incident; ransom payment | Covered critical infrastructure entities | CISA | 72 hours; 24 hours. Not required until the final rule takes effect | [CISA](https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia) |
| Breach of personal information of California residents | Businesses and agencies | Residents; Attorney General when over 500 | 30 calendar days; Attorney General within 15 days of notifying residents | [Civil Code 1798.82](https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.82) |

## What changes in the playbook

| Playbook page | What to add or change in this region |
|---|---|
| [Control mapping](../control-mapping.md) | Add columns for NIST CSF 2.0 and NIST SP 800-53 Rev. 5, and for NIST SP 800-171 if you hold controlled unclassified information. Map state and sector rules in the register, not only NIS2 transposition. |
| [Incident management](../../reliability/incident-management.md) | Add the US rows above to the regulatory clock checklist. Record the time of the SEC materiality determination as its own event. |
| [Data security and privacy](../../data/data-security-and-privacy.md) | Add the DOJ Data Security Program to the transfer table. Keep one breach clock per state. There is no general DPO duty; name a privacy lead and, under HIPAA, a privacy and a security official. |
| [Regulated industries](../regulated-industries.md) | Replace SR 11-7 with SR 26-2. Add GLBA, NYDFS Part 500 and the 36-hour banking rule. |
| [For financial services](../../../leaders/for-financial-services.md) | Use SR 26-2 for model risk; govern generative and agentic AI under your own policy, since SR 26-2 excludes them. |
| [Public sector](../public-sector.md) | Add FISMA ATO, FedRAMP and, for state and local bodies, the ADA Title II dates. |
| [Secure development](../../security/secure-development.md) | Keep the SSDF mapping: agencies may still ask for the attestation form or an SBOM case by case. |
| [Post-quantum readiness](../../security/post-quantum-readiness.md) | Plan for the FAR rule on FIPS and post-quantum compliance for contractors by 31 Dec 2030. |
| [Vulnerability management](../../security/vulnerability-management.md) | Federal agencies follow CISA Binding Operational Directive 22-01 deadlines for KEV entries; the playbook's 72 hours is stricter and fine to keep. |
| [AI governance](../../ai/ai-governance.md) | Add Colorado SB 26-189, Texas HB 149 and California SB 53 to the register's legal column. |
| [Accessibility testing](../../quality/accessibility-testing.md) | Note that Section 508 still points to WCAG 2.0 AA; test to WCAG 2.2 AA anyway. |

## Public sector

- **Federal.** Every federal information system needs an ATO under FISMA, based on NIST SP 800-53 Rev. 5 controls. Cloud services need FedRAMP certification. The Consolidated Rules for 2026 become mandatory for all providers on 1 Jan 2027. FedRAMP stops accepting new Rev5 certification applications on 11 Jun 2027. Offerings not fully following the rules lose certification on 1 Feb 2028. Produce the evidence from the pipeline, as the [control mapping](../control-mapping.md) describes.
- **Software buying.** OMB M-26-05 rescinded M-22-18 and M-23-16. Agencies may still require the CISA attestation form or an SBOM after a risk assessment, so keep both ready.
- **Defense.** DFARS 252.204-7012, NIST SP 800-171 and Phase 1 CMMC self-assessments with SPRS scores still apply. Phase 2 (third-party assessments, planned for 10 Nov 2026) was suspended on 13 Jul 2026 pending review. Do not stop preparing; the review outcome is not yet public.
- **State and local.** Meet the ADA Title II dates. Check your state's cloud and security programs and, for law enforcement data, the FBI CJIS Security Policy.
- **AI in agencies.** OMB M-25-21 requires minimum practices, including pre-deployment testing and impact assessments, for high-impact AI.

## Financial services

- **Model risk.** SR 26-2 (17 Apr 2026, Federal Reserve, OCC and FDIC) supersedes SR 11-7 and SR 21-8. It is most relevant to banks over $30 billion in assets and excludes generative and agentic AI, which your own governance must cover.
- **Incident reporting.** Banks notify their regulator within 36 hours; NYDFS licensees within 72 hours. Broker-dealers and advisers notify customers within 30 days under amended Regulation S-P (compliance from 3 Dec 2025 for larger entities and 3 Jun 2026 for smaller ones).
- **NYDFS Part 500.** Second amendment in force 1 Nov 2023. MFA for all access to information systems and a complete asset inventory apply from 1 Nov 2025. File the annual certification or acknowledgment by 15 April.
- **GLBA Safeguards Rule.** Non-bank lenders, fintechs and others under the FTC need a written program, a qualified individual, encryption, MFA and the 30-day FTC notice.
- **Self-assessment.** The FFIEC retired its Cybersecurity Assessment Tool on 31 Aug 2025 and pointed to NIST CSF 2.0 and CISA's Cybersecurity Performance Goals.

## Deadlines to watch, 2026 to 2028

| Date | What happens |
|---|---|
| Pending | CIRCIA final rule; HIPAA Security Rule final rule (proposed 6 Jan 2025, 90 FR 898); outcome of the CMMC review; FAR proposed rules on FIPS and post-quantum compliance and on vulnerability disclosure, directed by EO 14412 |
| 1 Jan 2027 | FedRAMP Consolidated Rules for 2026 mandatory; Colorado SB 26-189 developer duties begin |
| 26 Apr 2027 | ADA Title II compliance for public entities serving 50,000 people or more |
| 11 Jun 2027 | Last day for new FedRAMP Rev5 certification applications |
| 1 Feb 2028 | FedRAMP grace periods end |
| 1 Apr 2028 | CCPA risk assessment attestations and first cybersecurity audit certifications (businesses over $100 million revenue) due to the CPPA |
| 26 Apr 2028 | ADA Title II compliance for smaller public entities and special districts |
| 2 Jan 2030 onward | TLS 1.3 in federal systems; post-quantum key establishment (31 Dec 2030) and signatures (31 Dec 2031) for high value assets |

## Sources

- NIST, Cybersecurity Framework 2.0: https://www.nist.gov/cyberframework
- OMB M-26-05, Adopting a Risk-based Approach to Software and Hardware Security: https://www.whitehouse.gov/wp-content/uploads/2026/01/M-26-05-Adopting-a-Risk-based-Approach-to-Software-and-Hardware-Security.pdf
- OMB M-26-15, Execution of the Migration to Post-Quantum Cryptography: https://www.whitehouse.gov/wp-content/uploads/2026/06/M-26-15-Execution-of-the-Migration-to-Post-Quantum-Cryptography.pdf
- OMB memoranda, including M-25-21 and M-25-22: https://www.whitehouse.gov/omb/memoranda/
- Executive Order 14412: https://www.whitehouse.gov/presidential-actions/2026/06/securing-the-nation-against-advanced-cryptographic-attacks/
- FedRAMP Consolidated Rules for 2026, timeline: https://www.fedramp.gov/2026/timeline/
- Department of War CIO, CMMC: https://dowcio.war.gov/CMMC/About
- SEC, Cybersecurity Risk Management, Strategy, Governance, and Incident Disclosure: https://www.sec.gov/rules-regulations/2023/07/s7-09-22
- SEC, Regulation S-P amendments: https://www.sec.gov/newsroom/press-releases/2024-58
- CISA, CIRCIA: https://www.cisa.gov/topics/cyber-threats-and-advisories/information-sharing/cyber-incident-reporting-critical-infrastructure-act-2022-circia
- HHS, HIPAA Security Rule proposed rule (90 FR 898): https://www.federalregister.gov/documents/2025/01/06/2024-30983/hipaa-security-rule-to-strengthen-the-cybersecurity-of-electronic-protected-health-information
- 45 CFR part 164, subpart D: https://www.ecfr.gov/current/title-45/subtitle-A/subchapter-C/part-164/subpart-D
- FTC, Safeguards Rule notification requirement: https://www.ftc.gov/business-guidance/blog/2024/05/safeguards-rule-notification-requirement-now-effect
- 12 CFR part 53, computer-security incident notification: https://www.ecfr.gov/current/title-12/chapter-I/part-53
- Federal Reserve, SR 26-2: https://www.federalreserve.gov/supervisionreg/srletters/SR2602.htm
- NYDFS, second amendment to 23 NYCRR Part 500: https://www.dfs.ny.gov/system/files/documents/2023/10/rf_fs_2amend23NYCRR500_text_20231101.pdf
- FFIEC, Cybersecurity Assessment Tool sunset: https://www.ffiec.gov/news/press-releases/2024/an-09-29
- California Privacy Protection Agency, regulations: https://cppa.ca.gov/regulations/ccpa_updates.html
- California Civil Code 1798.82: https://leginfo.legislature.ca.gov/faces/codes_displaySection.xhtml?lawCode=CIV&sectionNum=1798.82
- DOJ National Security Division, Data Security Program: https://www.justice.gov/nsd/data-security
- Colorado SB 26-189: https://leg.colorado.gov/bills/sb26-189
- DOJ, ADA Title II compliance date extension (91 FR 20902): https://www.govinfo.gov/content/pkg/FR-2026-04-20/html/2026-07663.htm
- Section 508: https://www.section508.gov
- DFARS 252.204-7012: https://www.acquisition.gov/dfars/252.204-7012-safeguarding-covered-defense-information-and-cyber-incident-reporting.
- CISA, Binding Operational Directive 22-01: https://www.cisa.gov/news-events/directives/bod-22-01-reducing-significant-risk-known-exploited-vulnerabilities
- Executive Order 14365, Ensuring a National Policy Framework for Artificial Intelligence: https://www.govinfo.gov/app/details/DCPD-202501186/
- Texas HB 149, 89th Legislature: https://capitol.texas.gov/BillLookup/History.aspx?LegSess=89R&Bill=HB149
- California SB 53 (2025): https://leginfo.legislature.ca.gov/faces/billNavClient.xhtml?bill_id=202520260SB53
- Commerce BIS, rescission of the AI Diffusion rule (13 May 2025): https://www.bis.gov/press-release/department-commerce-announces-rescission-biden-era-artificial-intelligence-diffusion-rule-strengthens
- Export Administration Regulations, 15 CFR 740.17: https://www.ecfr.gov/current/title-15/subtitle-B/chapter-VII/subchapter-C/part-740/section-740.17
