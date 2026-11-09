# Vendor risk questionnaire

<!--
How to use: tier the supplier first (playbook/security/third-party-and-saas-risk.md).
Tier 3: do not send this. Tier 2: send sections A, B, C, D and H. Tier 1: send all sections
(section I only to suppliers of ICT services to EU financial entities).
Accept existing evidence instead of answers where it covers the question: an ISO/IEC 27001
certificate with its scope and statement of applicability, a SOC 2 Type II report, or a
completed CSA CAIQ. Mark which answers are backed by evidence.
When you accept a SOC 2 Type II report, check: the period ended within the last 12 months
(ask for a bridge letter for the gap); the service you buy is in scope; subservice
organisations are included or have their own reports; every exception and the management
response; and the complementary user entity controls, which become your controls. Record
who checked and when.
-->

| Field | Value |
|---|---|
| Supplier | |
| Product or service | |
| Internal owner | |
| Tier | Tier 1 / Tier 2 |
| Data shared (classes) | |
| Production access? | No / Yes: describe |
| Date sent / received | |
| Reviewer | |

Answer each question. Attach evidence where asked. "Not applicable" needs a reason.

## A. Company and certifications

| # | Question | Answer | Evidence |
|---|---|---|---|
| A1 | Which security certifications or audit reports do you hold (ISO/IEC 27001, SOC 2 Type II, sector schemes)? What is their scope and date? | | Certificate or report |
| A2 | Who is accountable for security, and how do we contact your security team? | | |
| A3 | Have you had a security incident affecting customer data in the last 3 years? What changed after it? | | |

## B. Data protection

| # | Question | Answer | Evidence |
|---|---|---|---|
| B1 | Which of our data will you store or process, and for what purpose? | | |
| B2 | In which countries will our data, backups and support access be located? | | |
| B3 | List your subprocessors. How do you notify us of changes, and how far in advance? | | Subprocessor list |
| B4 | Is our data encrypted in transit and at rest? Who manages the keys? Can we hold our own keys? | | |
| B5 | Will you use our data to train or improve models or products? Can we opt out? | | |
| B6 | How and how fast do you return and delete our data at the end of the contract? | | |
| B7 | Will you sign data processing terms meeting GDPR Article 28 or our local equivalent? | | |
| B8 | How is our data isolated from other customers' data? | | |
| B9 | For each country outside ours where our data is stored or accessed, which transfer mechanism do you rely on (adequacy, standard contractual clauses, binding corporate rules or a local equivalent)? | | |

## C. Access and identity

| # | Question | Answer | Evidence |
|---|---|---|---|
| C1 | Do you support SSO (SAML or OIDC) and SCIM provisioning for our users? Is it included in our plan? | | |
| C2 | Do your staff use phishing-resistant MFA to access production and customer data? | | |
| C3 | How is your staff's access to our data granted, limited, logged and reviewed? | | |
| C4 | Can we see an audit log of actions in our account, and export it? | | |
| C5 | How do you store, scope, rotate and revoke the tokens or keys you hold for access to our systems? Can we see and revoke them? | | |
| C6 | Are staff who access our data screened before hiring, and do they use managed devices? | | |

## D. Incidents and continuity

| # | Question | Answer | Evidence |
|---|---|---|---|
| D1 | How quickly will you notify us of a suspected security incident affecting our data or service? (We ask for 24 hours or less from when you become aware, and 4 hours or less if you support a function in scope of DORA or NIS2.) | | |
| D2 | What are your availability commitments and service credits? | | SLA |
| D3 | What are your backup, recovery point and recovery time objectives? When did you last test a restore? | | |
| D4 | Do you have a business continuity plan that is tested at least yearly? | | |
| D5 | Is at least one backup copy immutable or offline, and when did you last restore from it? | | |

## E. Secure development and vulnerabilities

| # | Question | Answer | Evidence |
|---|---|---|---|
| E1 | Do you follow a secure development framework (for example NIST SSDF)? How do you show it? | | |
| E2 | Do you publish a vulnerability disclosure policy and security.txt? | | Link |
| E3 | What are your fix times for critical and high vulnerabilities? | | |
| E4 | When did an independent party last test your product (penetration test)? Can we see a summary? | | Summary |
| E5 | Can you provide an SBOM (CycloneDX or SPDX) for software we run, and VEX statements for known vulnerabilities? | | |
| E6 | Are your releases signed, and how do we verify them? | | |
| E7 | If the EU Cyber Resilience Act applies to your product, how do you meet its reporting duty (in force since 11 Sep 2026) and how are you preparing for the other obligations (from 11 Dec 2027)? What is the support period (at least 5 years unless expected use is shorter)? | | |

## F. Post-quantum cryptography (Tier 1, and suppliers of cryptographic products)

| # | Question | Answer | Evidence |
|---|---|---|---|
| F1 | Which of your products use RSA, ECDSA, EdDSA, DH or ECDH, and for what? | | |
| F2 | When will each support ML-KEM (FIPS 203), ML-DSA (FIPS 204) or SLH-DSA (FIPS 205), and in which protocols? | | Roadmap |
| F3 | Do you support hybrid post-quantum key exchange today? Is it on by default? | | |
| F4 | Can algorithms be changed by configuration, or does it need a new version or new hardware? | | |
| F5 | Can hardware roots of trust be updated to post-quantum signatures? | | |
| F6 | Can you provide a cryptography bill of materials (CBOM) or a list of cryptographic dependencies? | | |

## G. AI features (if the product uses AI on our data)

| # | Question | Answer | Evidence |
|---|---|---|---|
| G1 | Which AI models or providers process our data, and where? | | |
| G2 | Is our data retained by the model provider or used for training? | | |
| G3 | How do you defend against prompt injection and data leakage between customers? | | |
| G4 | What actions can AI agents take in our account, and which need human approval? | | |
| G5 | Are AI inputs, outputs and actions logged and available to us? | | |

## H. Exit

| # | Question | Answer | Evidence |
|---|---|---|---|
| H1 | In what format can we export all our data, and how long does it take? | | |
| H2 | What notice will you give before ending the service or a product we depend on? | | |

## I. Financial entities (DORA Article 30)

Only for ICT services to EU financial entities. Answer yes or no; your legal team checks the contract wording. Items I7 to I12 apply only to services supporting critical or important functions (Art. 30(3)).

| # | Will the contract include | Yes / No |
|---|---|---|
| I1 | A clear description of all functions and ICT services, and whether subcontracting is allowed and on what conditions (Art. 30(2)(a)) | |
| I2 | The regions or countries where services are provided and data is processed, and advance notice before changes (Art. 30(2)(b)) | |
| I3 | Availability, authenticity, integrity and confidentiality of data, and access, recovery and return of data at exit or insolvency (Art. 30(2)(c) and (d)) | |
| I4 | Assistance in ICT incidents at no extra cost or at a cost set in advance, and full cooperation with our competent authority (Art. 30(2)(f) and (g)) | |
| I5 | Termination rights and minimum notice periods (Art. 30(2)(h)) | |
| I6 | Participation in our ICT security awareness and digital operational resilience training (Art. 30(2)(i)) | |
| I7 | Full service level descriptions with precise quantitative and qualitative performance targets (Art. 30(3)(a)) | |
| I8 | Notice periods and reporting duties to us, including any development that could affect the service (Art. 30(3)(b)) | |
| I9 | Business contingency plans that you implement and test, and security measures that fit our regulatory framework (Art. 30(3)(c)) | |
| I10 | Participation and full cooperation in our threat-led penetration testing (Art. 30(3)(d)) | |
| I11 | Unrestricted rights of access, inspection and audit for us, an appointed third party and our competent authority (Art. 30(3)(e)) | |
| I12 | Exit strategies, including a mandatory, adequate transition period (Art. 30(3)(f)) | |

## Reviewer conclusion

| Field | Value |
|---|---|
| Risk rating | Low / Medium / High |
| Conditions before contract | |
| Contract clauses required | |
| Accepted risks (owner, expiry) | |
| Next review | YYYY-MM-DD |
| Approved by | |
