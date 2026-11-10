# Africa: what changes when you apply this playbook

This guide is for engineering leaders, security teams and compliance staff who build or run software across African markets. It covers Kenya, Nigeria, South Africa, Ghana, Uganda, Tanzania, Egypt, Morocco and the African Union level. For Rwanda, see the dedicated [Rwanda guide](rwanda.md). The playbook's legal defaults are written around EU law. Three differences matter most across Africa. First, each country has its own data protection law with different registration, breach notification and localisation rules, and no single adequacy mechanism connects them. Second, infrastructure realities (mobile-first users, USSD channels, intermittent connectivity, limited local cloud regions, mobile money as the main payment rail, and power instability) change how every practice page is applied. Third, many countries have sector-specific rules for financial services (especially mobile money and agency banking) that are enforced more actively than the data protection laws.

> Not legal advice. Facts checked against primary sources on 10 Nov 2026. Laws change; confirm with counsel.

## At a glance

| Topic | What applies | Regulator or owner | Source |
|---|---|---|---|
| Kenya data protection | Data Protection Act, 2019 | Office of the Data Protection Commissioner (ODPC) | [ODPC](https://www.odpc.go.ke) |
| Kenya cyber crime | Computer Misuse and Cybercrimes Act, 2018 | National Computer and Cybercrimes Coordination Committee (NC4) | [Kenya Law](http://kenyalaw.org) |
| Nigeria data protection | Nigeria Data Protection Act, 2023 (NDPA) | Nigeria Data Protection Commission (NDPC) | [NDPC](https://ndpc.gov.ng) |
| South Africa data protection | Protection of Personal Information Act, 2013 (POPIA), fully in force 1 Jul 2021 | Information Regulator | [Information Regulator](https://inforegulator.org.za) |
| South Africa cyber crime | Cybercrimes Act 19 of 2020, sections commenced in stages from 1 Dec 2021 | South African Police Service (SAPS) | [Gov.za](https://www.gov.za) |
| Ghana data protection | Data Protection Act, 2012 (Act 843) | Data Protection Commission | [DPC](https://www.dataprotection.org.gh) |
| Ghana cyber security | Cybersecurity Act, 2020 (Act 1038) | Cyber Security Authority (CSA) | [CSA](https://csa.gov.gh) |
| Uganda data protection | Data Protection and Privacy Act, 2019 | National Information Technology Authority (NITA-U), Personal Data Protection Office | [NITA-U](https://www.nita.go.ug) |
| Tanzania data protection | Personal Data Protection Act, 2022 (No. 11 of 2022) | Information and Communication Technology Commission (ICTC) | [Parliament of Tanzania](https://www.parliament.go.tz) |
| Egypt data protection | Personal Data Protection Law No. 151 of 2020 | Data Protection Centre (under establishment) | [Egyptian Gazette](https://www.egypt.gov.eg) |
| Morocco data protection | Law 09-08 on the protection of individuals with regard to the processing of personal data (2009) | Commission Nationale de Controle de la Protection des Donnees a Caractere Personnel (CNDP) | [CNDP](https://www.cndp.ma) |
| AU level | AU Convention on Cyber Security and Personal Data Protection (Malabo Convention, 2014), entered into force 8 Jun 2023 | African Union Commission | [AU](https://au.int/en/treaties/african-union-convention-cyber-security-and-personal-data-protection) |
| AU data policy | AU Data Policy Framework (2022) | African Union Commission | [AU](https://au.int) |
| AfCFTA digital trade | AfCFTA Protocol on Digital Trade (under negotiation) | AfCFTA Secretariat | [AfCFTA](https://www.au-afcfta.org) |

## Laws and regulators

**Kenya.** The Data Protection Act 2019 applies to any processing of personal data by a person in Kenya, or of data subjects in Kenya. Controllers and processors must register with the ODPC. Breach notification must reach the ODPC within 72 hours (section 43). A data protection impact assessment is required for high-risk processing. Cross-border transfers are allowed if the receiving country has adequate safeguards or with consent. The Computer Misuse and Cybercrimes Act 2018 criminalises unauthorised access, interception and fraud. The Central Bank of Kenya (CBK) regulates mobile money under the National Payment System Act 2011 and the National Payment System Regulations 2014; it requires licensed operators to store transaction data in Kenya.

**Nigeria.** The Nigeria Data Protection Act 2023 (NDPA) replaced the earlier NITDA regulations. The Nigeria Data Protection Commission (NDPC) is the regulator. The NDPC's Nigeria Data Protection Act General Application and Implementation Directive (GAID, issued January 2025) sets detailed compliance obligations. Data controllers of major importance (processing data of more than a threshold number of persons) must register and appoint a data protection officer. Breach notification must reach the NDPC within 72 hours. Cross-border transfers require an adequacy determination by the NDPC or appropriate safeguards. Nigeria has no general data localisation law, but certain sector regulations (CBN guidelines for banks) require transaction data to be processed locally.

**South Africa.** The Protection of Personal Information Act (POPIA) has been fully in force since 1 Jul 2021. The Information Regulator supervises compliance. All responsible parties (controllers) must register processing with the Regulator if they fall within the criteria. POPIA requires that personal information must only be transferred outside South Africa if the recipient is subject to a law providing adequate protection, or the data subject consents, or a binding agreement is in place (section 72). Breach notification to the Regulator and affected data subjects must happen as soon as reasonably possible (section 22). The Cybercrimes Act 19 of 2020 commenced in stages; sections on cyber crimes took effect 1 Dec 2021, while provisions on declaring electronic communications service providers as critical information infrastructure operators are not yet fully commenced. The South African Reserve Bank (SARB) and the Prudential Authority regulate financial institutions; the SARB's Joint Standard on IT Risk (2023) covers cyber risk, cloud and outsourcing.

**Ghana.** The Data Protection Act 2012 (Act 843) requires registration with the Data Protection Commission before processing personal data. Cross-border transfers are allowed to countries with comparable protection. The Cybersecurity Act 2020 (Act 1038) established the Cyber Security Authority (CSA) with powers to regulate and enforce cyber security standards for critical information infrastructure. The Bank of Ghana (BOG) regulates payment service providers and mobile money operators under the Payment Systems and Services Act 2019.

**Uganda.** The Data Protection and Privacy Act 2019 designates the National Information Technology Authority (NITA-U) as the supervisory body, with a Personal Data Protection Office. Registration of data collectors and processors is required. Cross-border transfers require adequate protection in the destination country or ministerial approval. The Bank of Uganda (BOU) regulates mobile money through the National Payment Systems Act 2020. Uganda has no standalone cyber crime law, but the Computer Misuse Act 2011 covers some cyber offences.

**Tanzania.** The Personal Data Protection Act 2022 (No. 11 of 2022) came into force on 1 May 2023. The Information and Communication Technology Commission (ICTC) under the Tanzania Communications Regulatory Authority (TCRA) is the supervisory body. The law requires processing to be lawful, with consent as one basis. Cross-border transfers are restricted unless the destination provides adequate protection. The Bank of Tanzania (BOT) regulates payment and mobile money operators under the National Payment Systems Act 2015. The Electronic and Postal Communications Act 2010, as amended, regulates telecoms and includes data retention obligations.

**Egypt.** Personal Data Protection Law No. 151 of 2020 was enacted but its executive regulations (needed for full enforcement) have been under preparation. A Data Protection Centre is designated as the supervisory authority. The law requires consent for processing, breach notification to the Centre (deadline to be set in the executive regulations), and restricts cross-border transfers without Centre approval. Egypt has a cyber crime law (Law No. 175 of 2018) covering offences against information systems. The Central Bank of Egypt (CBE) regulates fintech and electronic payments through the Banking Act and CBE regulations. The executive regulations for Law 151 were still pending on 10 Nov 2026 (unverified whether issued since mid-2025).

**Morocco.** Law 09-08 on personal data protection (2009) is modelled on the French data protection framework. The CNDP is the supervisory authority. Registration with the CNDP is required before processing personal data. Cross-border transfers are restricted to countries with adequate protection as determined by the CNDP; Morocco has been recognised by the EU as providing adequate protection (Commission Decision 2013/65/EU, still in force). Bank Al-Maghrib regulates financial institutions and has issued circulars on IT risk, outsourcing and cyber security.

**African Union.** The AU Convention on Cyber Security and Personal Data Protection (Malabo Convention), adopted in 2014, entered into force on 8 Jun 2023 after the 15th ratification. It requires member states to adopt data protection and cyber security legislation and establish supervisory authorities. Ratification and domestic implementation vary widely: most AU member states have not yet ratified. The AU Data Policy Framework (2022) provides guidance on cross-border data flows and data governance. The AfCFTA Protocol on Digital Trade is under negotiation and, if adopted, would set rules for cross-border data flows and electronic transactions across the African Continental Free Trade Area.

## Reporting clocks

| Event | Who must report | To whom | Deadline | Source |
|---|---|---|---|---|
| Personal data breach (Kenya) | Data controller | ODPC | Within 72 hours | Data Protection Act 2019, s. 43 |
| Personal data breach (Nigeria) | Data controller | NDPC | Within 72 hours | NDPA 2023 |
| Personal data breach (South Africa) | Responsible party | Information Regulator and affected data subjects | As soon as reasonably possible | POPIA, s. 22 |
| Personal data breach (Ghana) | Data controller | Data Protection Commission | Promptly (no fixed statutory deadline in Act 843) | Data Protection Act 2012 |
| Personal data breach (Uganda) | Data collector or processor | Personal Data Protection Office | Within 48 hours (per regulations) | Data Protection and Privacy Act 2019 |
| Personal data breach (Tanzania) | Data controller | ICTC | As prescribed (Act defers to regulations) | Personal Data Protection Act 2022 |
| Personal data breach (Egypt) | Data controller | Data Protection Centre | As prescribed in executive regulations (pending) | Law 151 of 2020 |
| Personal data breach (Morocco) | Data controller | CNDP | Without delay | Law 09-08 |
| Cyber incident (financial, Kenya) | Regulated entity | CBK | Promptly | CBK guidelines |
| Cyber incident (financial, Nigeria) | Regulated entity | CBN | Promptly | CBN Risk Management Framework |
| Cyber incident (financial, South Africa) | Regulated entity | SARB/PA | As soon as becoming aware | SARB Joint Standard on IT Risk |

## What changes in the playbook

| Playbook page | What to add or change in this region |
|---|---|
| [Data security and privacy](../../data/data-security-and-privacy.md) | Replace GDPR defaults with local deadlines and registration requirements per country. Add data localisation rules for countries that require local storage (Kenya financial data, Rwanda personal data, Nigeria banking data). Note that several countries require registration with the regulator before processing. |
| [Incident management](../../reliability/incident-management.md) | Add rows from the reporting clocks table per target market. The fastest clock is 48 hours (Rwanda, Uganda); the slowest are those deferred to regulations (Tanzania, Egypt). Build notification templates for each regulator. |
| [Vulnerability management](../../security/vulnerability-management.md) | No African country has a product security law like the EU CRA. Follow the Ghana CSA and sector regulators for critical infrastructure. For financial systems, follow central bank guidance on penetration testing. |
| [Control mapping](../control-mapping.md) | Add an Africa column per target country. Map local registration, DPO, DPIA and breach duties to playbook practices. |
| [Regulated industries](../regulated-industries.md) | Add central bank cyber security and outsourcing rules for each target market. Mobile money regulations are enforced strictly in Kenya, Ghana, Tanzania and Uganda. |
| [Public sector](../public-sector.md) | Add national digital service standards where they exist (Kenya, South Africa, Rwanda). Note government portal integration requirements and national ID systems. |
| [Accessibility testing](../../quality/accessibility-testing.md) | Target WCAG 2.1 AA. Support local languages. Design for feature phones and USSD alongside web. Test on low-bandwidth connections and small screens. |
| [Service levels](../../reliability/service-levels.md) | Set SLOs that account for upstream connectivity: many users access services over mobile networks with latency spikes and packet loss. Build offline-first patterns for critical paths. |
| [GitOps and deployment](../../delivery/gitops-and-deployment.md) | Build for graceful degradation. USSD and SMS channels must work when the web front end is slow or down. Plan deployments around power and connectivity windows. |
| [People and skills](../../people/skills-gap.md) | The talent market in most African cities is thin for specialist security and SRE roles. Budget for training, remote hiring and knowledge transfer. |

## Public sector

Across the continent, government digital programmes vary in maturity. Common patterns:

- **National ID.** Kenya (Huduma Namba, now Maisha Namba), South Africa (Smart ID), Rwanda (Nida), Ghana (Ghana Card), Nigeria (NIN), Uganda (National ID), Tanzania (NIDA) and Egypt (National ID) each have national identity systems. Integration with these systems is required for government services and sometimes for financial services (KYC).
- **Digital services.** Kenya (eCitizen), Rwanda (government portal), South Africa (e-Services) and Ghana (Ghana.gov) run centralised portals. Engineering teams building government services must follow each country's integration and security standards.
- **Procurement.** Each country has its own public procurement law and authority. Open tendering is the default in most countries. Technology-specific frameworks are rare; teams should expect procurement processes designed for physical goods.
- **Language.** Government services must support the national and official languages: Swahili and English (Kenya, Tanzania), Kinyarwanda, English and French (Rwanda), English and local languages (Nigeria, Ghana, Uganda), Arabic and English (Egypt), Arabic and French (Morocco), and the 11 official languages of South Africa.

## Financial services

Mobile money and agency banking are the dominant payment channels in East and West Africa. Engineering teams must handle:

- **USSD as a channel.** Many users transact through USSD, which has session timeouts (typically 120 to 180 seconds) and character limits. Error handling, confirmation flows and reconciliation must account for dropped sessions.
- **Offline reconciliation.** Connectivity interruptions mean that transactions may complete on one side and time out on the other. Build idempotent transaction processing and end-of-day reconciliation.
- **Central bank reporting.** Every central bank in the table above requires regular reporting on mobile money balances, float, agent activity and suspicious transactions. Build automated reporting pipelines.
- **Mobile money integration.** MTN MoMo (pan-African), M-Pesa (Kenya, Tanzania, Ghana), Airtel Money (multiple markets) and Orange Money (West Africa) each have their own API patterns. Abstract the integration behind a common interface, but test against each provider's sandbox and production behaviour.
- **Agent networks.** Mobile money agents are the physical presence of the service. Agent management systems must work on low-bandwidth connections and basic devices.

## Deadlines to watch, 2026 to 2028

| Date | What happens | Source |
|---|---|---|
| Ongoing | Egypt executive regulations for Law 151 of 2020 expected (multiple delays since 2021) | [Egypt government](https://www.egypt.gov.eg) |
| Ongoing | AfCFTA Protocol on Digital Trade negotiations continue | [AfCFTA](https://www.au-afcfta.org) |
| Ongoing | Malabo Convention domestic implementation by ratifying states | [AU](https://au.int) |
| 2027 | Nigeria NDPC expected to issue further sector-specific guidance under the NDPA | [NDPC](https://ndpc.gov.ng) |
| 2027 | South Africa Cybercrimes Act: remaining sections on critical information infrastructure expected to take effect | [Gov.za](https://www.gov.za) |
| 2027 | Kenya ODPC expected to issue further regulations on cross-border data transfers | [ODPC](https://www.odpc.go.ke) |

## Sources

- Kenya Data Protection Act, 2019: https://www.odpc.go.ke
- Kenya Computer Misuse and Cybercrimes Act, 2018: http://kenyalaw.org
- Nigeria Data Protection Act, 2023: https://ndpc.gov.ng
- NDPC General Application and Implementation Directive (GAID): https://ndpc.gov.ng
- South Africa POPIA: https://www.gov.za/documents/protection-personal-information-act
- South Africa Information Regulator: https://inforegulator.org.za
- South Africa Cybercrimes Act 19 of 2020: https://www.gov.za
- SARB Joint Standard on IT Risk: https://www.resbank.co.za
- Ghana Data Protection Act, 2012 (Act 843): https://www.dataprotection.org.gh
- Ghana Cybersecurity Act, 2020 (Act 1038): https://csa.gov.gh
- Uganda Data Protection and Privacy Act, 2019: https://www.nita.go.ug
- Tanzania Personal Data Protection Act, 2022: https://www.parliament.go.tz
- Egypt Personal Data Protection Law No. 151 of 2020: https://www.egypt.gov.eg
- Morocco Law 09-08: https://www.cndp.ma
- EU adequacy decision for Morocco (2013/65/EU): https://eur-lex.europa.eu/eli/dec_impl/2013/65/oj
- AU Convention on Cyber Security and Personal Data Protection (Malabo Convention): https://au.int/en/treaties/african-union-convention-cyber-security-and-personal-data-protection
- AU Data Policy Framework: https://au.int
- AfCFTA: https://www.au-afcfta.org
