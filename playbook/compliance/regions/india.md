# India

This page is for engineering, security and compliance leads who build or run software for Indian customers, for Indian government bodies, or for firms regulated by Indian authorities. Three things differ most from the playbook's EU-centered defaults. First, India has no single data protection authority yet; sector regulators (RBI, SEBI, IRDAI, TRAI) each set their own cyber security and data rules, and you must track obligations per sector. Second, the Digital Personal Data Protection Act 2023 (DPDPA) is being brought into force in phases, so some duties apply now and others start in 2027. Third, CERT-In's 6-hour incident reporting window is one of the shortest in the world and applies to every organisation operating in India.

> Not legal advice. Facts checked against primary sources on 10 Nov 2026. Laws change; confirm with counsel.

## At a glance

| Topic | What applies | Regulator or owner | Source |
|---|---|---|---|
| Data protection | Digital Personal Data Protection Act 2023 (DPDPA); DPDP Rules 2025, notified 13 Nov 2025 | MeitY; Data Protection Board (not yet constituted) | [DPDPA Gazette](https://www.meity.gov.in/data-protection-framework) |
| Cyber incident reporting | CERT-In Directions of 28 Apr 2022; 6-hour reporting for 20 categories of incidents | CERT-In (under MeitY) | [CERT-In Directions](https://www.cert-in.org.in/) |
| IT law (general) | Information Technology Act 2000, amended 2008; IT Rules under various sections | MeitY | [IT Act](https://www.meity.gov.in/content/information-technology-act) |
| Payment data localisation | RBI circular of 6 Apr 2018; payment system data must be stored only in India | RBI | [RBI Payment Data](https://www.rbi.org.in/) |
| Financial services cyber security | RBI IT Outsourcing Directions 2023; RBI Master Direction on IT Governance | RBI | [RBI Directions](https://www.rbi.org.in/) |
| Capital markets | SEBI Cybersecurity and Cyber Resilience Framework (CSCRF), Aug 2024 | SEBI | [SEBI Circulars](https://www.sebi.gov.in/sebiweb/home/HomeAction.do?doListing=yes&sid=2&ssid=9) |
| Insurance | IRDAI Information and Cyber Security Guidelines, Apr 2023 | IRDAI | [IRDAI Guidelines](https://www.irdai.gov.in/) |
| Telecom | Telecommunication Cyber Security Rules 2024, amended Oct 2025 | DoT; TRAI for tariffs and consumer issues | [DoT](https://dot.gov.in/) |
| AI governance | No dedicated AI law; NITI Aayog Responsible AI principles (2021); MeitY advisory on labelling (Mar 2024, withdrawn) | MeitY; NITI Aayog | [NITI Aayog AI](https://niti.gov.in/) |
| E-commerce | Consumer Protection (E-Commerce) Rules 2020, amended Sep 2026 | Department of Consumer Affairs | [Consumer Affairs](https://consumeraffairs.nic.in/) |
| Health data | Ayushman Bharat Digital Mission (ABDM); NHA Health Data Management Policy | National Health Authority (NHA) | [ABDM](https://abdm.gov.in/) |
| Accessibility | Rights of Persons with Disabilities Act 2016; Guidelines for Indian Government Websites (GIGW) | Department of Empowerment of Persons with Disabilities; NIC | [GIGW](https://guidelines.india.gov.in/) |

## Laws and regulators

### Regulatory bodies

**MeitY (Ministry of Electronics and Information Technology).** MeitY administers the IT Act 2000 and the DPDPA 2023. It issues rules, notifications and advisories on cyber security, data protection and intermediary obligations. CERT-In operates under MeitY.

**CERT-In (Indian Computer Emergency Response Team).** The national incident response agency. It issues directions under Section 70B of the IT Act. Its April 2022 directions set the 6-hour incident reporting clock and the 180-day log retention mandate.

**RBI (Reserve Bank of India).** Regulates banks, non-banking financial companies (NBFCs), payment system operators and fintech firms. RBI sets data localisation rules for payment data, IT governance frameworks and outsourcing norms for regulated entities.

**SEBI (Securities and Exchange Board of India).** Regulates stock exchanges, brokers, mutual funds, portfolio managers and other capital market participants. SEBI's CSCRF (August 2024) is the current cyber security framework for regulated entities.

**TRAI (Telecom Regulatory Authority of India).** Advises on telecom tariffs, quality of service and consumer protection. The Department of Telecommunications (DoT) issues binding telecom cybersecurity rules; TRAI issues recommendations.

**IRDAI (Insurance Regulatory and Development Authority of India).** Regulates insurers and intermediaries. Its 2023 Information and Cyber Security Guidelines set board-level governance, audit and incident reporting duties for the insurance sector.

### Key legislation

**Information Technology Act 2000 (amended 2008).** India's base cyber law. It covers electronic contracts, digital signatures, cyber offences and intermediary liability. Section 43A requires bodies corporate that handle sensitive personal data to maintain reasonable security practices. Section 69 gives the government powers to intercept, monitor or decrypt information. Section 70B establishes CERT-In.

**Digital Personal Data Protection Act 2023 (DPDPA).** India's first general data protection law. It received Presidential assent on 11 August 2023. The DPDP Rules 2025 were notified on 13 November 2025 (Gazette notification G.S.R. 846(E)), and the Act is being brought into force in stages. Key concepts:

- **Data Fiduciary** (the controller) and **Data Principal** (the individual).
- **Significant Data Fiduciaries (SDFs)** face extra duties: appoint a Data Protection Officer and an independent data auditor, conduct periodic data protection impact assessments. Telecom operators are classified as SDFs under the DPDP Rules 2025.
- **Consent** must be free, specific, informed and unambiguous. Consent managers (registered with the Data Protection Board) will manage consent on behalf of Data Principals, starting November 2026.
- **Cross-border transfers** follow a blacklist model: transfers are allowed to all countries except those the Central Government restricts by notification. No restricted list has been published yet. Sector-specific rules (such as RBI's payment data localisation) still apply on top.
- **Penalties** of up to INR 250 crore (approximately USD 30 million) per violation.
- **Children's data** requires verifiable parental consent. Processing children's data for behavioural monitoring or targeted advertising is prohibited.

**Digital India Act (proposed).** MeitY announced the Digital India Act in 2023 as a replacement for the IT Act 2000. Stakeholder consultations took place in mid-2023. No public draft has been released. The timeline is uncertain; the Act was not tabled before the 2024 general elections and its current status is unconfirmed.

## Data localisation

India has sector-specific data localisation rules rather than a single general requirement.

**Payment data (RBI).** The RBI's circular of 6 April 2018 requires payment system operators to store the complete end-to-end transaction data relating to payment systems operated in India only within India. Processing may happen abroad, but data must be brought back and stored in India within 24 hours. The RBI enforced this rule against American Express and Diners Club in 2021, barring them from onboarding new customers until they complied.

**DPDPA cross-border transfers.** Section 16 of the DPDPA allows transfers to any country except those the Central Government restricts. No restricted country list has been notified yet. Once the list is published, transfers to those countries will require the Central Government's prior approval or will be prohibited outright.

**SEBI-regulated data.** SEBI's CSCRF requires regulated entities to store data within India. Cloud service providers used by SEBI-regulated entities must keep data in Indian data centres.

**Insurance data.** IRDAI's 2023 guidelines require that critical data of policyholders and operational data remain within India.

**Telecom data.** The Telecommunication Cyber Security Rules 2024 require telecom entities to store traffic data and other specified data within India.

**Practical step.** Maintain a data residency register. For each data category, record whether Indian law requires local storage. The playbook's [data security and privacy](../../data/data-security-and-privacy.md) page has a transfer table; add an India column.

## Incident reporting

### CERT-In 6-hour mandate

The CERT-In Directions of 28 April 2022 (effective 27 June 2022) require every service provider, intermediary, data centre, body corporate and government organisation to report cyber security incidents to CERT-In within 6 hours of noticing the incident or being informed about it.

**Reportable incidents** include (from Annexure I of the directions, 20 categories):

- Targeted scanning or probing of critical networks or systems
- Compromise of critical systems or information
- Unauthorised access to IT systems or data
- Defacement of websites or intrusion into websites
- Malicious code attacks (such as spreading of virus, worm, trojan, bots, spyware, ransomware or cryptominers)
- Attacks on servers, such as database, mail or DNS, and network devices such as routers
- Identity theft, spoofing and phishing attacks
- Denial of service and distributed denial of service attacks
- Attacks on critical infrastructure, SCADA and operational technology systems, and wireless networks
- Attacks on e-governance, e-commerce and digital payment applications and systems
- Data breaches and data leaks
- Attacks on Internet of Things devices and associated systems, networks and software
- Attacks or incidents affecting digital payment systems
- Attacks through malicious mobile apps
- Fake mobile apps
- Unauthorised access to social media accounts
- Attacks or suspicious activities affecting cloud computing systems, servers, software and applications
- Attacks or malicious or suspicious activities affecting systems relating to big data, blockchain, virtual assets, robotics, 3D and 4D printing and additive manufacturing
- Attacks or malicious or suspicious activities affecting systems relating to AI and ML

**Other obligations under the 2022 directions:**

- Maintain logs of all ICT systems for a rolling period of 180 days, stored within Indian jurisdiction.
- Synchronise system clocks to the NTP server of the National Informatics Centre (NIC) or the National Physical Laboratory (NPL), or to an NTP server traceable to them.
- Designate a point of contact to interface with CERT-In. Provide the contact's name, designation, phone number and email to CERT-In.
- VPN service providers, cloud service providers and virtual private server providers must maintain records of subscribers and their activity for 5 years or longer as directed. Records include validated customer names, dates, IPs allotted, email addresses, IP addresses used at the time of registration, purpose of use and contact numbers.

### Sector-specific reporting

| Event | Who reports | To whom | Deadline | Source |
|---|---|---|---|---|
| Any of the 20 categories of cyber incidents | Service providers, intermediaries, data centres, body corporates, government organisations | CERT-In | 6 hours from noticing or being informed | [CERT-In Directions 2022](https://www.cert-in.org.in/) |
| Personal data breach | Data Fiduciaries | Data Protection Board (once constituted) and each affected Data Principal | Without unreasonable delay (DPDPA Section 8(6)); timelines to be set by rules | [DPDPA 2023](https://www.meity.gov.in/data-protection-framework) |
| Cyber security incident (banking) | RBI-regulated entities | RBI and CERT-In | Immediately, and not later than 6 hours (aligned with CERT-In); detailed report within specific RBI timelines | [RBI Circulars](https://www.rbi.org.in/) |
| Cyber security incident (capital markets) | SEBI-regulated entities | SEBI and CERT-In | 6 hours to CERT-In; within timelines set by SEBI CSCRF | [SEBI CSCRF](https://www.sebi.gov.in/) |
| Cyber security incident (insurance) | Insurers and intermediaries | IRDAI and CERT-In | Promptly (per IRDAI June 2023 circular); 6 hours to CERT-In | [IRDAI Guidelines 2023](https://www.irdai.gov.in/) |
| Telecom cyber security incident | Telecom entities | DoT and CERT-In | 6 hours to CERT-In; DoT timelines per Telecom Cyber Security Rules 2024 | [DoT](https://dot.gov.in/) |

**Practical step.** Build the 6-hour clock into your incident runbook. The playbook's [incident management](../../reliability/incident-management.md) page has a regulatory clock checklist; add the CERT-In row. Pre-draft a CERT-In report template (incident.cert-in.org.in is the reporting portal). The 6-hour window leaves almost no room for triage before reporting, so automate detection-to-notification where possible.

## Financial services

### RBI

**IT Outsourcing Directions 2023.** The RBI's Outsourcing of Information Technology Services Directions, issued 10 April 2023 and effective 1 October 2023, apply to scheduled commercial banks, small finance banks, payments banks, NBFCs, credit information companies and All India Financial Institutions. Key requirements:

- Board-approved IT outsourcing policy covering roles of the board, senior management and IT functions.
- Risk management framework for outsourcing, covering risk identification, measurement, mitigation and reporting.
- Service providers must maintain and test business continuity and disaster recovery plans.
- Contracts must include right-to-audit clauses, data security obligations and exit management.
- Transition deadlines: agreements due for renewal before 1 October 2023 had to comply by 9 April 2024. Agreements due for renewal on or after that date must comply by renewal or by 9 April 2026, whichever is earlier.
- Foreign bank branches follow a "comply or explain" approach.

**IT Governance and Controls.** The RBI's Master Direction on Information Technology Governance, Risk, Controls, Assurance and Audit (issued in phases) requires regulated entities to maintain IT governance at the board level, conduct IT risk assessments and perform internal and external IT audits.

**Payment data localisation.** See [Data localisation](#data-localisation) above. This is strictly enforced.

**UPI and payment systems.** The Unified Payments Interface (UPI) is operated by the National Payments Corporation of India (NPCI). Payment system operators require RBI authorisation under the Payment and Settlement Systems Act 2007. Third-party application providers (TPAPs) on UPI must comply with NPCI's technical and security specifications, including two-factor authentication and transaction limits.

### SEBI

**Cybersecurity and Cyber Resilience Framework (CSCRF).** SEBI issued the CSCRF on 20 August 2024 (circular SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113). It supersedes prior SEBI cybersecurity circulars issued between 2015 and 2023. Key duties:

- Classify assets and data; maintain an asset inventory.
- Conduct vulnerability assessments and penetration testing at least twice per financial year.
- Implement a Security Operations Centre (SOC), either in-house or through a managed SOC provider.
- Report incidents to SEBI and CERT-In.
- Keep audit trails and logs.
- The compliance deadline was extended several times: from January 2025 to June 2025, then to 31 August 2025 for most regulated entities. Market Infrastructure Institutions (MIIs) had earlier deadlines.

**Practical step.** Map the CSCRF controls to the playbook's [control mapping](../control-mapping.md). Many controls align with NIST CSF 2.0 and ISO 27001.

### IRDAI

**Information and Cyber Security Guidelines 2023.** Issued 24 April 2023, superseding the 2017 guidelines. Apply to insurers and intermediaries (insurance and micro-insurance agents are exempt). Key requirements:

- Board-approved information and cyber security policy.
- Designate a Chief Information Security Officer (CISO).
- Annual independent assurance audit.
- Incident reporting to IRDAI (promptly, per the June 2023 circular) and to CERT-In (6 hours).
- Compliance deadline: April 2024 for most entities.
- Amendments issued 6 April 2026 retained the core structure.

## AI governance

India has taken a principle-based, sector-neutral approach to AI regulation. There is no dedicated AI law.

**NITI Aayog Responsible AI.** NITI Aayog published a two-part framework in 2021:

- Part 1 (February 2021) set out seven principles for responsible AI, drawn from the Indian Constitution: safety and reliability, equality, inclusivity and non-discrimination, privacy and security, transparency, accountability, and protection and reinforcement of positive human values.
- Part 2 (August 2021) proposed mechanisms to put the principles into practice, divided among government, the private sector and research institutions. It recommended a risk-based approach to regulation and continuous assessment throughout an AI system's lifecycle.

These principles are advisory. They do not have the force of law.

**MeitY advisory on AI labelling (March 2024).** MeitY issued an advisory requiring platforms to label AI-generated content and obtain government approval before deploying under-tested or unreliable AI models. The advisory was criticised by industry and parts of it were withdrawn within weeks. The current status of remaining obligations under the advisory is unclear.

**Digital India Act.** If the proposed Digital India Act is enacted, it is expected to include provisions on high-risk AI systems, algorithmic accountability and regulatory sandboxes. No draft text is available.

**Sector-specific AI rules.** No sector regulator has issued binding AI-specific rules yet. RBI's IT governance framework covers model risk for traditional models but does not specifically address generative or agentic AI. SEBI has referenced AI in its consultation papers. Firms should govern AI use under their own policies.

**Practical step.** Use the playbook's [AI governance](../../ai/ai-governance.md) register. Record the NITI Aayog principles as the applicable Indian framework. Monitor MeitY and the Digital India Act process for binding rules.

## Government and public sector

### India Stack

India Stack is a set of open APIs and digital public infrastructure:

- **Aadhaar** - a 12-digit biometric identity number issued by the Unique Identification Authority of India (UIDAI). Using Aadhaar for authentication or eKYC requires UIDAI approval and compliance with the Aadhaar Act 2016 and its regulations. Data collected through Aadhaar authentication must not be stored beyond the transaction (Section 29 of the Aadhaar Act).
- **UPI** - real-time payment system operated by NPCI. See [Financial services](#financial-services).
- **DigiLocker** - a platform for issuing and verifying digital documents. Government agencies and registered issuers can push documents; citizens access them with Aadhaar-linked accounts.
- **ONDC (Open Network for Digital Commerce)** - an open protocol for e-commerce, decoupling buyer and seller platforms. ONDC participation requires compliance with its network policies, including data-sharing rules between buyer and seller network participants.

### GovTech requirements

Software sold to the Indian government typically goes through the Government e-Marketplace (GeM). The Ministry of Electronics and IT has issued guidelines on:

- **MeghRaj / GI Cloud** - the government's cloud initiative. Government applications should prefer empanelled cloud service providers listed by MeitY.
- **Cyber security** - government websites and applications must follow the Guidelines for Indian Government Websites (GIGW) and the security practices published by NIC and CERT-In.
- **Accessibility** - the Rights of Persons with Disabilities Act 2016 (Section 46) requires the government to ensure that all public documents and websites are accessible. The GIGW incorporates WCAG 2.0 Level AA.

### Central vs state jurisdiction

IT and telecom fall under the Union List (Entry 31, List I of the Seventh Schedule to the Constitution). Data protection under the DPDPA is also a central subject. However, state governments administer their own IT departments, run state data centres and issue state-level IT policies. Some states (such as Karnataka, Telangana and Maharashtra) have their own IT and startup policies that may impose additional requirements for government contracts.

## Sector-specific rules

### Telecom

The Telecommunication Cyber Security Rules 2024 (amended October 2025) apply to telecom service providers and are issued under the Telecommunications Act 2023. Key duties:

- Report cyber incidents to DoT and CERT-In.
- Store traffic data within India.
- Implement identity verification and KYC for subscribers.
- Cooperate with government directions on interception and monitoring.

TRAI issues recommendations on tariffs, quality of service and consumer data privacy. TRAI recommendations are advisory until accepted by DoT.

### Healthcare (ABDM)

The Ayushman Bharat Digital Mission (ABDM) builds India's national digital health ecosystem. Key components:

- **ABHA (Ayushman Bharat Health Account)** - a 14-digit health ID for citizens.
- **Health Information Exchange and Consent Manager (HIE-CM)** - manages consent for sharing health records between Health Information Providers (HIPs) and Health Information Users (HIUs).
- **Technical standards** - ABDM uses HL7 FHIR R4. The FHIR Implementation Guide published by the National Resource Centre for EHR Standards (NRCeS) defines minimum conformance requirements.
- **Certification** - software connecting to ABDM must be certified by NHA-empanelled agencies. Developers must register on the NHA Sandbox before testing.
- **Health Data Management Policy** - the NHA's policy (last publicly available draft: April 2022, Version 2) sets consent, access control and audit logging requirements for health data.

ABDM consent is separate from DPDPA consent. Both must be obtained where applicable.

### E-commerce

The Consumer Protection (E-Commerce) Rules 2020, most recently amended in September 2026, apply to e-commerce entities. Key requirements:

- Appoint a grievance officer, a chief compliance officer and a nodal contact person for law enforcement.
- Display the country of origin and importer details for imported goods.
- Do not manipulate search results or promote sponsored listings without disclosure.
- Marketplace entities must not exercise ownership or control over the inventory of sellers.
- Cancellation and return policies must be clearly stated.

## Compliance calendar

| Date | What happens |
|---|---|
| Already in force | CERT-In 6-hour incident reporting (since 27 Jun 2022); CERT-In 180-day log retention; RBI payment data localisation (since Oct 2018); IRDAI Cyber Security Guidelines 2023 (since Apr 2024); IT Act 2000 and amendments |
| Already in force | DPDPA Sections 1, 2, 18-26, 35 and 38-44 (since 13 Nov 2025); DPDP Rules 2025 (first-phase provisions) |
| 13 Nov 2026 | DPDPA consent manager registration and obligations (Rule 4); Sections 6(9) and 27(1)(d) |
| 9 Apr 2026 | RBI IT Outsourcing Directions - final transition deadline for agreements due for renewal on or after 1 Oct 2023 |
| 13 May 2027 | DPDPA remaining provisions, including cross-border transfer rules and full enforcement (Section 44(2)); exact date to be confirmed against gazette notification |
| Pending | Digital India Act (no public draft); Data Protection Board constitution; DPDPA restricted country list for cross-border transfers |
| Ongoing | SEBI CSCRF compliance (deadline passed Aug 2025 for most entities; check SEBI for current enforcement status) |

## What changes in the playbook

| Playbook page | What to add or change for India |
|---|---|
| [Control mapping](../control-mapping.md) | Add columns for CERT-In Directions 2022 and SEBI CSCRF. Map IRDAI Guidelines 2023 and RBI IT Governance controls. |
| [Incident management](../../reliability/incident-management.md) | Add the 6-hour CERT-In clock to the regulatory clock checklist. Pre-draft CERT-In report templates. Automate detection-to-notification. |
| [Data security and privacy](../../data/data-security-and-privacy.md) | Add the DPDPA to the privacy law table. Add India's data residency rules per sector. Note the blacklist model for cross-border transfers. Name a Data Protection Officer for SDF-class operations. |
| [Regulated industries](../regulated-industries.md) | Add RBI IT Outsourcing Directions 2023, SEBI CSCRF 2024 and IRDAI Guidelines 2023. |
| [Secure development](../../security/secure-development.md) | Map CERT-In log retention (180 days) and clock synchronisation requirements to the logging standard. |
| [AI governance](../../ai/ai-governance.md) | Add NITI Aayog Responsible AI principles (advisory). Monitor the Digital India Act for binding AI provisions. |
| [Backup and recovery](../../reliability/backup-and-recovery.md) | Confirm that 180-day log retention within Indian jurisdiction is met. |
| [Access control](../../security/access-control.md) | Aadhaar-based authentication requires UIDAI approval and compliance with the Aadhaar Act; do not store biometric data beyond the transaction. |
| [Accessibility testing](../../quality/accessibility-testing.md) | Government projects must meet GIGW (WCAG 2.0 AA). The playbook's WCAG 2.2 AA target exceeds this. |
| [Third-party and SaaS risk](../../security/third-party-and-saas-risk.md) | Apply RBI IT Outsourcing Directions to vendor assessments for financial services. Require right-to-audit clauses. |

## Sources

- CERT-In, Directions under Section 70B(6) of the IT Act, 28 April 2022: https://www.cert-in.org.in/
- Digital Personal Data Protection Act 2023: https://www.meity.gov.in/data-protection-framework
- DPDP Rules 2025, Gazette notification G.S.R. 846(E), 13 November 2025: https://www.meity.gov.in/
- Information Technology Act 2000: https://www.meity.gov.in/content/information-technology-act
- RBI, Storage of Payment System Data, 6 April 2018: https://www.rbi.org.in/
- RBI, Outsourcing of Information Technology Services Directions, 10 April 2023: https://www.rbi.org.in/
- SEBI, Cybersecurity and Cyber Resilience Framework, circular SEBI/HO/ITD-1/ITD_CSC_EXT/P/CIR/2024/113, 20 August 2024: https://www.sebi.gov.in/
- IRDAI, Information and Cyber Security Guidelines, 24 April 2023: https://www.irdai.gov.in/
- NITI Aayog, Responsible AI Part 1 (February 2021) and Part 2 (August 2021): https://niti.gov.in/
- Telecommunication Cyber Security Rules 2024, amended October 2025: https://dot.gov.in/
- Consumer Protection (E-Commerce) Rules 2020, amended September 2026: https://consumeraffairs.nic.in/
- NHA, Ayushman Bharat Digital Mission: https://abdm.gov.in/
- NHA, Health Data Management Policy (Draft Version 2, April 2022): https://abdm.gov.in/
- UIDAI, Aadhaar Act 2016: https://uidai.gov.in/
- NPCI, UPI guidelines: https://www.npci.org.in/
- Guidelines for Indian Government Websites (GIGW): https://guidelines.india.gov.in/
- AZB & Partners, DPDPA phased rollout and compliance milestones: https://www.azbpartners.com/bank/indias-digital-personal-data-protection-act-phased-rollout-and-key-compliance-milestones/
- Mondaq, CERT-In 6 hours to report cyber incidents: https://mondaq.co.uk/india/it-and-internet/1270332/6-hours-to-report-cyber-incidents-to-cert-in
- KSK Law, RBI IT outsourcing regulations: https://ksandk.com/banking/rbi-empowers-businesses-with-new-regulations-on-outsourcing-it-services/
- Mondaq, IRDAI Information and Cyber Security Guidelines: https://www.mondaq.com/india/security/1338148/an-overview-of-the-irdai-information-and-cyber-security-guidelines-2023
