# Rwanda: what changes when you apply this playbook

This guide is for engineering leaders, security teams and compliance staff who build or run software in Rwanda or process data of Rwandan residents. The playbook's legal defaults are written around EU law. Three differences matter most in Rwanda. First, Rwanda's data protection law (Law No 058/2021) requires registration with the National Cyber Security Authority (NCSA) and storage of personal data in Rwanda unless the NCSA authorises a transfer, a stricter default than the GDPR transfer regime. Second, financial services follow National Bank of Rwanda (BNR) regulations on cyber security, cloud outsourcing and payment services that have no EU equivalent. Third, infrastructure realities (intermittent connectivity, limited local cloud regions, mobile money as the main payment rail, and a multilingual population using Kinyarwanda, English and French) change how every playbook practice is applied in practice.

> Not legal advice. Facts checked against primary sources on 10 Nov 2026. Laws change; confirm with counsel.

## At a glance

| Topic | What applies | Regulator or owner | Source |
|---|---|---|---|
| Data protection | Law No 058/2021 of 13/10/2021 relating to the protection of personal data and privacy | NCSA (supervisory authority under Art. 46) | [Official Gazette](https://www.ncsa.gov.rw) |
| Cyber security authority | Law No 26/2017 of 31/05/2017 establishing the NCSA | NCSA | [NCSA](https://www.ncsa.gov.rw) |
| Cyber crime | Law No 60/2018 of 22/08/2018 on prevention and punishment of cyber crimes | Rwanda Investigation Bureau (RIB), prosecution service | [Official Gazette](https://www.minijust.gov.rw) |
| Financial services | BNR Regulation No 03/2021 on cyber security, Regulation on cloud and outsourcing, Regulation on payment service providers and e-money issuers | National Bank of Rwanda (BNR) | [BNR](https://www.bnr.rw) |
| Telecoms | Law No 24/2016 governing ICT; RURA regulations on telecoms operators | Rwanda Utilities Regulatory Authority (RURA) | [RURA](https://www.rura.rw) |
| Public sector digital services | National digital transformation policy; the government portal for public services | Ministry of ICT and Innovation (MINICT); Rwanda Information Society Authority (RISA) | [MINICT](https://www.minict.gov.rw) |
| AI | National AI policy (2023) | MINICT | [MINICT](https://www.minict.gov.rw) |
| Accessibility | No standalone accessibility statute; disability rights under Law No 01/2007 | National Council of Persons with Disabilities (NCPD) | [NCPD](https://www.ncpd.gov.rw) |
| Data localisation | Personal data must be stored in Rwanda unless the NCSA authorises otherwise (Art. 37, Law 058/2021) | NCSA | [NCSA](https://www.ncsa.gov.rw) |

## Laws and regulators

**Data protection.** Law No 058/2021 of 13/10/2021 is Rwanda's data protection law. It applies to any person or organisation that processes personal data of people in Rwanda, regardless of where the processing happens (Art. 3). In practice:

- Controllers and processors must register with the NCSA before processing personal data (Art. 32).
- A data protection officer (DPO) is required for public bodies and for private organisations that process personal data on a large scale or process sensitive data (Art. 34). The DPO must be resident in Rwanda.
- Data protection impact assessments are required before processing that is likely to result in high risk to data subjects (Art. 35).
- Consent must be specific, informed and freely given (Art. 9). Processing of sensitive personal data requires explicit consent or one of the listed exceptions (Art. 14).
- Data subjects have rights of access, rectification, erasure, restriction, portability and objection (Arts. 18 to 27).
- Personal data must be stored in Rwanda unless the NCSA has authorised the transfer (Art. 37). The NCSA may authorise a transfer if the receiving country provides adequate protection, or if appropriate safeguards are in place.
- Breach notification: the controller must notify the NCSA within 48 hours of becoming aware of a personal data breach (Art. 38). The data subject must be notified without undue delay if the breach is likely to result in high risk.

**Cyber security authority.** Law No 26/2017 established the NCSA as the body responsible for cyber security policy and operations in Rwanda. The NCSA also serves as the supervisory authority for data protection under Law 058/2021.

**Cyber crime.** Law No 60/2018 criminalises unauthorised access, interference with data or systems, and related offences. It covers fraud, forgery and identity theft carried out through electronic means.

**Financial services.** The BNR regulates banks, microfinance institutions, insurers, payment service providers and e-money issuers. BNR Regulation No 03/2021 on cyber security requires regulated entities to maintain a cyber security framework, conduct regular risk assessments, report cyber incidents to the BNR promptly, and appoint a chief information security officer or equivalent. Outsourcing and cloud regulations require prior BNR notification or approval before outsourcing critical functions or storing data outside Rwanda. Payment service provider regulations set requirements for mobile money operators, including transaction limits, agent management and consumer protection.

**Telecoms.** RURA regulates telecoms operators and internet service providers under Law No 24/2016 governing ICT. RURA sets conditions on data retention, lawful interception capability and network security.

**Public sector.** Rwanda runs a digital-first government programme. The government portal serves as the single window for public services (civil registration, permits, payments). RISA manages government IT infrastructure and the national data centre. The national digital transformation policy sets the direction for e-government, digital identity and data sharing across ministries.

**AI.** Rwanda published a national AI policy in 2023 to guide the responsible use of AI across government and industry. It is a policy framework, not binding legislation.

**Accessibility.** There is no standalone digital accessibility statute equivalent to the EU's Web Accessibility Directive. Law No 01/2007 on protection of disabled persons in general includes rights to access services. In practice, teams building government services should follow WCAG 2.1 AA as a minimum, and support Kinyarwanda alongside English and French.

**Data localisation and transfers.** Art. 37 of Law 058/2021 requires personal data to be stored in Rwanda unless the NCSA authorises a transfer. This is stricter than the GDPR default. Engineering teams must plan for local hosting or obtain NCSA authorisation early. Rwanda has one commercial data centre operated by Africa Data Centres in Kigali; hyperscaler cloud regions are not present in Rwanda, though some providers offer nodes in neighbouring countries (South Africa, Kenya). Teams that cannot host locally should apply to the NCSA with documented safeguards.

## Reporting clocks

| Event | Who must report | To whom | Deadline | Source |
|---|---|---|---|---|
| Personal data breach | Controller | NCSA | Within 48 hours of becoming aware | Art. 38, Law 058/2021 |
| Personal data breach (high risk to subject) | Controller | Affected data subjects | Without undue delay | Art. 38, Law 058/2021 |
| Cyber incident at a financial institution | Regulated entity | BNR | Promptly (within 24 hours in practice) | BNR Regulation 03/2021 |
| Cyber crime | Any person | Rwanda Investigation Bureau | As soon as practicable | Law 60/2018 |
| Telecoms network incident | Telecoms operator | RURA | As required by licence conditions | RURA regulations |

## What changes in the playbook

| Playbook page | What to add or change in this region |
|---|---|
| [Data security and privacy](../../data/data-security-and-privacy.md) | Add the 48-hour breach notification clock. Replace GDPR transfer tools with NCSA authorisation for cross-border transfers. Add NCSA registration as a prerequisite. Require a DPO resident in Rwanda. |
| [Incident management](../../reliability/incident-management.md) | Add the Rwanda rows from the reporting clocks table. Note the 48-hour NCSA clock and 24-hour BNR clock. |
| [Vulnerability management](../../security/vulnerability-management.md) | Note that Rwanda has no standalone product security law like the EU CRA. Follow NCSA guidance and BNR requirements for financial systems. |
| [Control mapping](../control-mapping.md) | Add a Rwanda column: map NCSA registration, DPO, DPIA and breach notification duties to playbook practices. Map BNR cyber security regulation to the financial services controls. |
| [Regulated industries](../regulated-industries.md) | Add BNR cyber security, outsourcing and cloud regulations. Note that BNR approval is needed before outsourcing critical functions or storing data abroad. |
| [Public sector](../public-sector.md) | Add the government portal integration requirements, RISA infrastructure standards and the national digital transformation policy. |
| [IT governance](../../operating-model/it-governance.md) | Government projects follow MINICT and RISA standards. Procurement follows Rwanda Public Procurement Authority (RPPA) rules. |
| [AI governance](../../ai/ai-governance.md) | Reference the national AI policy (2023). No binding AI regulation yet. |
| [Accessibility testing](../../quality/accessibility-testing.md) | Target WCAG 2.1 AA minimum. Support Kinyarwanda, English and French. Design for mobile-first and low-bandwidth users. |
| [Post-quantum readiness](../../security/post-quantum-readiness.md) | No country-specific timeline. Follow NCSA guidance as it develops. |

## Public sector

- **Government portal.** The government portal is the main channel for public services. Teams building services that integrate with it must follow the portal's API standards and identity framework (national ID integration).
- **National data centre.** RISA operates the national data centre in Kigali. Government systems are expected to be hosted there or in approved facilities.
- **Digital identity.** Rwanda's national ID system (Nida) is the foundation for identity verification across government and regulated services.
- **Procurement.** Public IT procurement follows the Rwanda Public Procurement Authority (RPPA) law and regulations. Open tendering is the default method.
- **Language.** Government services must support Kinyarwanda. English and French are also official languages. All three should be supported in user interfaces.

## Financial services

- **Cyber security framework.** BNR Regulation 03/2021 requires every regulated institution to have a board-approved cyber security strategy, a CISO or equivalent role, regular penetration tests, and an incident response plan. Boards must receive quarterly cyber risk reports.
- **Outsourcing and cloud.** Regulated entities must notify or obtain BNR approval before outsourcing critical functions. Cloud hosting outside Rwanda requires documented risk assessment and NCSA authorisation for personal data. The BNR expects a full exit strategy for every outsourced function.
- **Mobile money.** Rwanda has high mobile money adoption (MTN MoMo, Airtel Money). Payment service providers must comply with BNR regulations on consumer protection, transaction limits, agent management and anti-money-laundering rules. Engineering teams integrating mobile money must handle USSD timeouts (sessions typically last 120 to 180 seconds), offline reconciliation and partial connectivity.
- **Payment systems.** RSwitch operates the national payment switch. Integration with RSwitch is required for interbank and mobile money interoperability.
- **Anti-money laundering.** Law No 027/2008 on prevention of money laundering and financing of terrorism applies to financial institutions and designated non-financial businesses. Suspicious transaction reports go to the Financial Intelligence Centre (FIC). Engineering teams must build automated screening and reporting into payment flows.

## Infrastructure realities

Engineering teams deploying in Rwanda face conditions that change how playbook practices work in practice:

- **Connectivity.** Internet penetration is growing but many end users rely on mobile data with variable speeds. Build for low bandwidth: compress assets, lazy-load images, support USSD and SMS fallback channels for critical flows.
- **Power.** Power outages occur, especially outside Kigali. Data centres and server rooms need uninterruptible power supplies and generator backup. Application design should handle ungraceful shutdowns and recover state on restart.
- **Cloud.** No hyperscaler has a region in Rwanda. The nearest regions are in South Africa (AWS, Azure, GCP) and Kenya (GCP). Use the national data centre or approved local facilities for data that must stay in Rwanda. For workloads that can be hosted abroad with NCSA authorisation, choose the nearest region and measure latency.
- **Mobile first.** Most users access services on smartphones with small screens. Progressive web apps (PWAs) and responsive design are the baseline. USSD remains important for users on feature phones.
- **Talent.** The local pool of specialist security, SRE and cloud engineers is small. Invest in training, pair less experienced engineers with seniors, and document runbooks so knowledge stays in the organisation.

## Deadlines to watch, 2026 to 2028

| Date | What happens | Source |
|---|---|---|
| Ongoing | NCSA may issue implementing regulations or guidelines under Law 058/2021, including on cross-border transfers and registration procedures | [NCSA](https://www.ncsa.gov.rw) |
| Ongoing | BNR may update cyber security and outsourcing regulations for banks and payment providers | [BNR](https://www.bnr.rw) |
| 2027 | Malabo Convention (AU Convention on Cyber Security and Personal Data Protection) may drive harmonisation, depending on AU member state ratification | [AU](https://au.int/en/treaties/african-union-convention-cyber-security-and-personal-data-protection) |

## Sources

- Law No 058/2021 of 13/10/2021 relating to the protection of personal data and privacy: https://www.ncsa.gov.rw
- Law No 26/2017 of 31/05/2017 establishing the NCSA: https://www.ncsa.gov.rw
- Law No 60/2018 of 22/08/2018 on prevention and punishment of cyber crimes: https://www.minijust.gov.rw
- BNR Regulation No 03/2021 on cyber security for regulated institutions: https://www.bnr.rw
- BNR regulations on payment service providers and e-money issuers: https://www.bnr.rw
- RURA, telecoms regulations: https://www.rura.rw
- MINICT, national digital transformation policy: https://www.minict.gov.rw
- MINICT, national AI policy: https://www.minict.gov.rw
- Rwanda Information Society Authority (RISA): https://www.risa.rw
- Rwanda Public Procurement Authority (RPPA): https://www.rppa.gov.rw
- AU Convention on Cyber Security and Personal Data Protection (Malabo Convention): https://au.int/en/treaties/african-union-convention-cyber-security-and-personal-data-protection
