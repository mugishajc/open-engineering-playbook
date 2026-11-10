# United Kingdom: what changes when you apply this playbook

This guide is for engineering leaders, security teams and compliance staff who run software in the UK or sell into it, including public bodies, banks, insurers and telecoms operators. The playbook's legal defaults are written around EU law. Three differences matter most in the UK. First, UK GDPR, as amended by the Data (Use and Access) Act 2025, now differs from the EU GDPR on transfers, automated decisions, subject access timing and complaints, and the regulator became the Information Commission on 30 Sep 2026. Second, NIS2, the Cyber Resilience Act (CRA) and the AI Act do not apply in Great Britain: the NIS Regulations 2018, the product security regime and voluntary codes apply instead, and the Cyber Security and Resilience Bill is still in Parliament. Third, financial firms follow PRA and FCA operational resilience rules and the critical third parties regime, not EU DORA.

> Not legal advice. Facts checked against primary sources on 9 Nov 2026. Laws change; confirm with counsel.

## At a glance

| Topic | What applies | Regulator or owner | Source |
|---|---|---|---|
| Data protection | UK GDPR and Data Protection Act 2018, amended by the Data (Use and Access) Act 2025 | Information Commission (the ICO until 30 Sep 2026) | [DUAA 2025](https://www.legislation.gov.uk/ukpga/2025/18/contents) |
| Cookies and electronic marketing | Privacy and Electronic Communications Regulations 2003 (PECR) | Information Commission | [PECR](https://www.legislation.gov.uk/uksi/2003/2426/contents) |
| Essential services and digital services | NIS Regulations 2018 (SI 2018/506) | 12 sector competent authorities; Information Commission for digital service providers | [SI 2018/506](https://www.legislation.gov.uk/uksi/2018/506/contents) |
| Cyber baseline for essential services | NCSC Cyber Assessment Framework (CAF) v4.0, 4 Aug 2025 | NCSC | [CAF](https://www.ncsc.gov.uk/collection/cyber-assessment-framework/changelog) |
| Telecoms security | Telecommunications (Security) Act 2021, Security Measures Regulations 2022, code of practice | Ofcom | [Act](https://www.legislation.gov.uk/ukpga/2021/31/contents) |
| Consumer connectable products | PSTI Act 2022 and SI 2023/1007, in force 29 Apr 2024 | Office for Product Safety and Standards | [SI 2023/1007](https://www.legislation.gov.uk/uksi/2023/1007/contents/made) |
| Software vendors | Software Security Code of Practice, 7 May 2025 (voluntary) | NCSC and government | [Code](https://www.gov.uk/government/publications/software-security-code-of-practice/software-security-code-of-practice) |
| Financial services resilience | PRA SS1/21, FCA PS21/3, PRA SS2/21, critical third parties regime | PRA, FCA, Bank of England | [SS2/21](https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/outsourcing-and-third-party-risk-management-ss) |
| Public procurement | Procurement Act 2023, in force 24 Feb 2025 | Cabinet Office | [SI 2024/716](https://www.legislation.gov.uk/uksi/2024/716) |
| Public digital services | Service Standard (14 points), Technology Code of Practice (13 points), Digital Assurance Playbook | Government Digital Service (GDS) | [Service Standard](https://www.gov.uk/service-manual/service-standard) |
| AI | No AI statute; existing regulators apply existing law | AI Security Institute; sector regulators | [AISI](https://www.aisi.gov.uk/) |
| Accessibility | Public Sector Bodies Accessibility Regulations 2018; Equality Act 2010 | GDS monitors; EHRC and ECNI enforce | [SI 2018/952](https://www.legislation.gov.uk/uksi/2018/952/contents/made) |
| Cryptography exports | Export Control Order 2008; UK Strategic Export Control Lists, Category 5 Part 2 | Export Control Joint Unit | [Order](https://www.legislation.gov.uk/uksi/2008/3231/contents) |

## Laws and regulators

**Data protection.** The UK GDPR and the Data Protection Act 2018 apply. The Data (Use and Access) Act 2025 (c. 18, Royal Assent 19 Jun 2025) amended both in stages. Most data protection changes started on 5 Feb 2026 under SI 2026/82. In practice:

- Recognised legitimate interests (Schedule 4) are a new lawful basis for listed purposes, such as crime prevention and safeguarding, with no balancing test.
- Automated decision-making (section 80) is allowed with safeguards: tell the person, let them make representations, and offer human review. Stricter limits remain for special category data.
- Subject access (section 76, new Article 12A): the one-month clock starts at the latest of receipt, identity confirmation or fee. It pauses while you wait for clarification and can be extended by two months for complex or numerous requests.
- Cookies (section 112): some analytics and functional cookies no longer need consent. PECR enforcement now uses the Data Protection Act 2018 penalty regime (Schedule 13).
- Complaints (section 103): since 19 Jun 2026, controllers must make it possible to complain, for example with an electronic form. They acknowledge each complaint within 30 days and respond without undue delay.
- Regulator: the Information Commissioner's office was abolished on 30 Sep 2026 and its functions moved to the Information Commission (SI 2026/1015).

**Cyber security.** The NIS Regulations 2018 cover operators of essential services (energy, transport, health, water, digital infrastructure) and relevant digital service providers (online marketplaces, search engines, cloud). Most competent authorities assess operators against the NCSC CAF, now v4.0, which added secure software development and AI risk. The Cyber Security and Resilience (Network and Information Systems) Bill extends NIS to managed service providers, data centres and large load controllers. It lets regulators designate critical suppliers and adds a 24-hour initial notification. Parliament's bill record shows Lords third reading on 2 Nov 2026 and Commons consideration of Lords amendments still to come. It is not yet law.

**Critical infrastructure and telecoms.** Public telecoms providers follow the Telecommunications (Security) Act 2021, which inserted security duties into the Communications Act 2003. The Electronic Communications (Security Measures) Regulations 2022 (SI 2022/933) set the duties and the code of practice sets the measures and dates. Ofcom enforces and reports. A draft revised code was published in 2026; check whether it is final.

**Products.** The UK did not adopt the EU CRA. For consumer connectable products, PSTI requires no universal default passwords, a published way to report vulnerabilities, and a published minimum security update period. Manufacturers, importers and distributors share the duties. Software vendors can follow the voluntary Software Security Code of Practice: 14 principles in 4 themes. The UK government's position is that most of the CRA does not apply in Northern Ireland unless added under the Windsor Framework; the current status of that discussion is unverified. UK firms selling into the EU must still meet the CRA there.

**Financial services.** See [Financial services](#financial-services) below.

**Public sector.** See [Public sector](#public-sector) below.

**AI.** No AI-specific statute applies. Existing regulators apply data protection, equality, consumer and financial services law to AI. The AI Safety Institute was renamed the AI Security Institute on 14 Feb 2025. The machinery of government fact sheet of 22 Jul 2026 moves AI policy and the institute to the Cabinet Office. No government AI bill was before Parliament on 9 Nov 2026 (Parliament bill search). UK public bodies use the AI Playbook for the UK Government (Feb 2025) and the Algorithmic Transparency Recording Standard. UK firms that place AI on the EU market follow the EU AI Act there.

**Accessibility.** SI 2018/952 requires public sector websites and apps to meet WCAG 2.2 level AA, as GOV.UK guidance states, with exemptions. Each body publishes an accessibility statement. GDS monitors a sample each year. The Equality and Human Rights Commission and the Equality Commission for Northern Ireland enforce. Private firms have the reasonable adjustment duty under the Equality Act 2010; the UK has no equivalent of the European Accessibility Act.

**Cryptography.** Exports of encryption items are controlled under the Export Control Order 2008 and the UK Strategic Export Control Lists (entries 5A002 and 5D002). The Cryptography Note (Note 3) releases many mass-market items. The Open General Export Licence for cryptographic development covers collaboration on commercial products and excludes some destinations, including Russia and Belarus. Sanctions and end-use controls apply on top. Separately, under the Investigatory Powers Act 2016, section 253, the Secretary of State can give telecoms operators technical capability notices.

**Data localisation and transfers.** The UK has no general data localisation law. Transfers out of the UK follow the UK GDPR Chapter V as amended by section 85: UK adequacy regulations, the International Data Transfer Agreement, or the UK Addendum to the EU clauses. Transfers to certified US organisations use the UK Extension to the EU-US Data Privacy Framework (SI 2023/1028, from 12 Oct 2023). The EU renewed its UK adequacy decisions on 19 Dec 2025 until 27 Dec 2031, so EU to UK flows need no extra mechanism. Government data follows the Government Security Classifications Policy (OFFICIAL, SECRET, TOP SECRET) and departmental hosting rules.

## Reporting clocks

| Event | Who must report | To whom | Deadline | Source |
|---|---|---|---|---|
| Personal data breach | Controller | Information Commission; affected people if high risk | Without undue delay, within 72 hours where feasible | [UK GDPR Arts. 33, 34](https://www.legislation.gov.uk/eur/2016/679/contents) |
| Personal data breach at a processor | Processor | Controller | Without undue delay | UK GDPR Art. 33(2) |
| Personal data breach at a public electronic communications service | Service provider | Information Commission; subscriber if adversely affected | Within 72 hours where feasible (was 24 hours before 20 Aug 2025) | [PECR reg. 5A](https://www.legislation.gov.uk/uksi/2003/2426/regulation/5A) |
| NIS incident with significant impact on an essential service | Operator of essential services | Competent authority | Without undue delay, no later than 72 hours | [NIS reg. 11](https://www.legislation.gov.uk/uksi/2018/506/regulation/11) |
| Incident with substantial impact on a digital service | Relevant digital service provider | Information Commission | No later than 72 hours | [NIS reg. 12](https://www.legislation.gov.uk/uksi/2018/506/regulation/12) |
| Significant incident, once the Bill is law and commenced | NIS entities, managed service providers, data centres | Regulator, with NCSC told at the same time; then affected customers | Initial 24 hours, full report 72 hours (proposed) | [Bill factsheet](https://www.gov.uk/government/publications/cyber-security-and-resilience-network-and-information-systems-bill-factsheets/incident-reporting) |
| Security compromise with significant effect | Public electronic communications provider | Ofcom | As soon as reasonably practicable | [Communications Act 2003 s. 105K](https://www.legislation.gov.uk/ukpga/2003/21/section/105K) |
| Operational incident meeting a threshold, from 18 Mar 2027 | FCA and PRA firms (one report for dual-regulated firms) | FCA via Connect; PRA | Initial within 24 hours of meeting a threshold; final within 30 working days of resolution, 60 at most | [FCA PS26/2](https://www.fca.org.uk/publications/policy-statements/ps26-2-operational-incident-third-party-reporting), [PRA PS7/26](https://www.bankofengland.co.uk/prudential-regulation/publication/2026/march/operational-incident-and-third-party-reporting-policy-statement) |
| Major operational or security incident | Payment service providers | FCA | Within 4 hours of first detecting it | FCA PS26/2, section on when to report |
| Data subject complaint, since 19 Jun 2026 | Controller | The complainant | Acknowledge within 30 days | [DPA 2018 s. 164A](https://www.legislation.gov.uk/ukpga/2025/18/section/103) |

Before 18 Mar 2027, FCA firms notify under Principle 11 and [SUP 15.3](https://www.handbook.fca.org.uk/handbook/SUP/15/3.html). Ransomware reporting is not yet mandatory; see [Deadlines to watch](#deadlines-to-watch-2026-to-2028).

## What changes in the playbook

| Playbook page | What to add or change in this region |
|---|---|
| [Data security and privacy](../../data/data-security-and-privacy.md) | Read GDPR article numbers as UK GDPR. Add Article 12A timing for subject access, recognised legitimate interests, the section 164A complaints process, and the UK transfer tools above. |
| [Incident management](../../reliability/incident-management.md) | Add the UK rows from the reporting clocks table to the Assured checklist: NIS 72 hours, PECR 72 hours, Ofcom, and FCA and PRA from 18 Mar 2027. |
| [Vulnerability management](../../security/vulnerability-management.md) | For consumer products, publish the PSTI vulnerability contact and support period. Map secure development evidence to the Software Security Code of Practice. |
| [Control mapping](../control-mapping.md) | Add a UK column: CAF v4.0 outcomes for NIS and GovAssure, Cyber Essentials for supplier contracts, SS1/21 and SS2/21 for financial firms. |
| [Regulated industries](../regulated-industries.md) | Replace EU DORA with SS1/21, PS21/3, SS2/21, the critical third parties regime and PS26/2 for UK entities. Use CBEST for threat-led testing. |
| [Third-party and SaaS risk](../../security/third-party-and-saas-risk.md) | Record material third-party arrangements in the format of the 2027 FCA and PRA register; note which suppliers are designated critical third parties. |
| [Public sector](../public-sector.md) | Add Procurement Act 2023, PPN 014, GovAssure, the Digital Assurance Playbook and the Government Security Classifications Policy. |
| [IT governance](../../operating-model/it-governance.md) | UK digital and technology spend controls ended on 1 Apr 2026. Describe the pipeline, delegated authority limits and assurance instead. |
| [AI governance](../../ai/ai-governance.md) | No UK AI Act: map tiers to sector regulator expectations, UK GDPR Article 22A to 22D, PRA SS1/23 and the Algorithmic Transparency Recording Standard. |
| [Accessibility testing](../../quality/accessibility-testing.md) | Public sector: WCAG 2.2 AA and an accessibility statement are required, not only targeted. |
| [Post-quantum readiness](../../security/post-quantum-readiness.md) | Use the NCSC milestones (2028, 2031, 2035) as the UK plan dates. |

## Public sector

The Government Digital Service is now part of the Department for Digital, Culture, Media and Sport (GOV.UK organisation page, checked 9 Nov 2026). Departments moved several times since 2024, so confirm owners before you cite them.

- **Service Standard.** 14 points, from understanding users to operating a reliable service. Services are assessed through the service assessment process, which continues under the Digital Assurance Playbook.
- **Technology Code of Practice.** 13 points, including cloud first, open source, open standards and sustainability. GDS updated it on 29 Oct 2026 and removed references to spend controls.
- **Spend controls replaced.** From 1 Apr 2026 digital and technology spend controls are removed. Organisations keep a pipeline of initiatives above £5 million whole-life cost in Government Assurance Services and run their own functional assurance. GDS approval applies only above the organisation's Delegated Authority Limit, set by HM Treasury, or for novel, contentious or repercussive initiatives.
- **Procurement.** The Procurement Act 2023 applies to procurements started on or after 24 Feb 2025; earlier ones stay under the old regulations. PPN 014 asks for Cyber Essentials or Cyber Essentials Plus on higher-risk contracts, renewed every year, and warns against applying it to every contract.
- **Cyber assurance.** GovAssure assesses critical government systems against a government CAF profile, with independent review. The Government Cyber Security Strategy 2022 to 2030 sets the goal.
- **Money and AI.** Managing Public Money and the Green Book still apply. Central government departments publish algorithmic tools under the Algorithmic Transparency Recording Standard.
- **Testing.** Use NCSC CHECK companies for penetration tests of government systems where your department requires it.

## Financial services

- **Operational resilience.** PRA SS1/21 and FCA PS21/3 required firms to identify important business services, set impact tolerances, map and test, and remain within tolerance by 31 Mar 2025. The playbook's [for financial services](../../../leaders/for-financial-services.md) method matches.
- **Outsourcing.** PRA SS2/21 sets expectations for outsourcing and third-party risk, including a register. PS7/26 amends it from 18 Mar 2027, with clearer tests for material third-party arrangements and a notification when one starts or changes materially.
- **Critical third parties.** The regime started on 1 Jan 2025 (PRA PS16/24, FCA PS24/16). The first designations, by SI 2026/777 in force 13 Jul 2026, are Amazon Web Services EMEA SARL, Google Cloud EMEA Limited, Microsoft Ireland Operations Limited and Oracle Corporation UK Limited. Oversight covers only the services they give the financial sector. Firms remain accountable for their own use of those services.
- **Incident and third-party reporting.** From 18 Mar 2027, under FCA PS26/2 and PRA PS7/26, firms report operational incidents in three phases and submit a yearly register of material third-party arrangements.
- **Testing.** CBEST is the Bank of England's threat intelligence-led testing framework, used by the PRA and FCA. Testers and threat intelligence providers must be accredited.
- **Models.** PRA SS1/23 (model risk) applies to banks with internal model approval and covers AI models.
- **EU DORA.** It applies to your EU-authorised entities, not to UK entities. Groups with both run one evidence set against both regimes.

## Deadlines to watch, 2026 to 2028

| Date | What happens | Source |
|---|---|---|
| Late 2026 or 2027 | Cyber Security and Resilience Bill: Commons consideration of Lords amendments, then Royal Assent. Most duties start by later regulations; managed service providers register within 3 months of commencement. | [Bill record](https://bills.parliament.uk/bills/4035) |
| Rolling | HM Treasury may designate more critical third parties. | [SI 2026/777](https://www.legislation.gov.uk/uksi/2026/777/made) |
| 18 Mar 2027 | FCA, PRA and Bank of England incident and third-party reporting starts. | FCA PS26/2, PRA PS7/26 |
| 31 Mar 2027 and 31 Mar 2028 | Telecoms security code: remaining Tier 1 and Tier 2 measures due. Check the revised code. | [Draft revised code](https://www.gov.uk/government/publications/draft-revised-telecommunications-security-code-of-practice-2026/draft-revised-telecommunications-security-code-of-practice) |
| 11 Dec 2027 | EU CRA main obligations for UK firms selling products into the EU. | [Regulation (EU) 2024/2847](https://eur-lex.europa.eu/eli/reg/2024/2847/oj) |
| 2028 | NCSC milestone: post-quantum discovery and initial migration plan done. | [NCSC](https://www.ncsc.gov.uk/guidance/pqc-migration-timelines) |
| Not scheduled | Targeted ransomware payment ban for public bodies and CNI, announced 22 Jul 2025. No government bill on 9 Nov 2026. | [Home Office](https://www.gov.uk/government/consultations/ransomware-proposals-to-increase-incident-reporting-and-reduce-payments-to-criminals) |

## Sources

- Data (Use and Access) Act 2025: https://www.legislation.gov.uk/ukpga/2025/18/contents
- DSIT, Data (Use and Access) Act 2025: plans for commencement: https://www.gov.uk/guidance/data-use-and-access-act-2025-plans-for-commencement
- SI 2026/82, DUAA Commencement No. 6: https://www.legislation.gov.uk/uksi/2026/82/contents/made
- SI 2026/1015, DUAA Commencement No. 9: https://www.legislation.gov.uk/uksi/2026/1015/contents/made
- UK GDPR: https://www.legislation.gov.uk/eur/2016/679/contents
- Data Protection Act 2018: https://www.legislation.gov.uk/ukpga/2018/12/contents
- Privacy and Electronic Communications Regulations 2003: https://www.legislation.gov.uk/uksi/2003/2426/contents
- Data Protection (Adequacy) (United States of America) Regulations 2023: https://www.legislation.gov.uk/uksi/2023/1028/contents/made
- European Commission, renewal of UK adequacy decisions (IP/25/3059): https://ec.europa.eu/commission/presscorner/detail/en/ip_25_3059
- NIS Regulations 2018: https://www.legislation.gov.uk/uksi/2018/506/contents
- UK Parliament, Cyber Security and Resilience (Network and Information Systems) Bill: https://bills.parliament.uk/bills/4035
- GOV.UK, Cyber Security and Resilience Bill factsheets: https://www.gov.uk/government/publications/cyber-security-and-resilience-network-and-information-systems-bill-factsheets/summary-of-the-bill
- NCSC, Cyber Assessment Framework: https://www.ncsc.gov.uk/collection/cyber-assessment-framework
- Telecommunications (Security) Act 2021: https://www.legislation.gov.uk/ukpga/2021/31/contents
- Electronic Communications (Security Measures) Regulations 2022: https://www.legislation.gov.uk/uksi/2022/933/contents/made
- Communications Act 2003, section 105K: https://www.legislation.gov.uk/ukpga/2003/21/section/105K
- Product Security and Telecommunications Infrastructure Act 2022: https://www.legislation.gov.uk/ukpga/2022/46/contents
- SI 2023/1007, security requirements for relevant connectable products: https://www.legislation.gov.uk/uksi/2023/1007/contents/made
- Software Security Code of Practice: https://www.gov.uk/government/publications/software-security-code-of-practice/software-security-code-of-practice
- UK government explanatory memorandum on the EU Cyber Resilience Act and Northern Ireland: https://www.gov.uk/government/publications/em-on-council-decision-2025799-on-the-eu-cyber-resilience-act
- PRA SS1/21: https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/operational-resilience-impact-tolerances-for-important-business-services-ss
- FCA PS21/3: https://www.fca.org.uk/publications/policy-statements/ps21-3-building-operational-resilience
- PRA SS2/21: https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/outsourcing-and-third-party-risk-management-ss
- FCA PS26/2: https://www.fca.org.uk/publications/policy-statements/ps26-2-operational-incident-third-party-reporting
- PRA PS7/26: https://www.bankofengland.co.uk/prudential-regulation/publication/2026/march/operational-incident-and-third-party-reporting-policy-statement
- FCA Handbook, SUP 15.3: https://www.handbook.fca.org.uk/handbook/SUP/15/3.html
- Critical Third Parties (Designation) Regulations 2026: https://www.legislation.gov.uk/uksi/2026/777/made
- PRA PS16/24, critical third parties: https://www.bankofengland.co.uk/prudential-regulation/publication/2024/november/operational-resilience-critical-third-parties-to-the-uk-financial-sector-policy-statement
- Bank of England, CBEST implementation guide: https://www.bankofengland.co.uk/financial-stability/operational-resilience-of-the-financial-sector/cbest-threat-intelligence-led-assessments-implementation-guide
- PRA SS1/23: https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- Procurement Act 2023: https://www.legislation.gov.uk/ukpga/2023/54/contents
- SI 2024/716, Procurement Act commencement: https://www.legislation.gov.uk/uksi/2024/716
- PPN 014, Cyber Essentials scheme: https://www.gov.uk/government/publications/ppn-014-cyber-essentials-scheme/ppn-014-cyber-essentials-scheme-html
- Digital Assurance Playbook: https://www.gov.uk/government/publications/digital-assurance-playbook/digital-assurance-playbook
- Service Standard: https://www.gov.uk/service-manual/service-standard
- Technology Code of Practice: https://www.gov.uk/guidance/the-technology-code-of-practice
- Government Digital Service organisation page: https://www.gov.uk/government/organisations/government-digital-service
- Machinery of government changes fact sheet, 22 Jul 2026: https://www.gov.uk/government/news/machinery-of-government-changes-fact-sheet
- GovAssure: https://www.security.gov.uk/policy-and-guidance/govassure/
- Government Security Classifications Policy: https://www.gov.uk/government/publications/government-security-classifications
- Algorithmic Transparency Recording Standard hub: https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub
- AI Playbook for the UK Government: https://www.gov.uk/government/publications/ai-playbook-for-the-uk-government
- GOV.UK, AI Security Institute renaming, 14 Feb 2025: https://www.gov.uk/government/news/tackling-ai-security-risks-to-unleash-growth-and-deliver-plan-for-change
- Public Sector Bodies (Websites and Mobile Applications) (No. 2) Accessibility Regulations 2018: https://www.legislation.gov.uk/uksi/2018/952/contents/made
- GOV.UK, accessibility requirements for public sector websites and apps: https://www.gov.uk/guidance/accessibility-requirements-for-public-sector-websites-and-apps
- Export Control Order 2008: https://www.legislation.gov.uk/uksi/2008/3231/contents
- Open General Export Licence (cryptographic development): https://www.gov.uk/government/publications/open-general-export-licence-cryptographic-development
- Notice to exporters 2018/07, the Cryptography Note: https://www.gov.uk/government/publications/notice-to-exporters-201807-guidance-on-the-cryptography-note/notice-to-exporters-201807-guidance-on-the-cryptography-note
- Investigatory Powers Act 2016, section 253: https://www.legislation.gov.uk/ukpga/2016/25/section/253
- Home Office, ransomware consultation and response: https://www.gov.uk/government/consultations/ransomware-proposals-to-increase-incident-reporting-and-reduce-payments-to-criminals
- NCSC, timelines for migration to post-quantum cryptography: https://www.ncsc.gov.uk/guidance/pqc-migration-timelines
