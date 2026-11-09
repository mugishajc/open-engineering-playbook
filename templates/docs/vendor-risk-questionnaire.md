# Vendor risk questionnaire

<!--
How to use: tier the supplier first (playbook/security/third-party-and-saas-risk.md).
Tier 3: do not send this. Tier 2: send sections A, B, C, D and H. Tier 1: send all sections.
Accept existing evidence instead of answers where it covers the question: an ISO/IEC 27001
certificate with its scope and statement of applicability, a SOC 2 Type II report, or a
completed CSA CAIQ. Mark which answers are backed by evidence.
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

## C. Access and identity

| # | Question | Answer | Evidence |
|---|---|---|---|
| C1 | Do you support SSO (SAML or OIDC) and SCIM provisioning for our users? Is it included in our plan? | | |
| C2 | Do your staff use phishing-resistant MFA to access production and customer data? | | |
| C3 | How is your staff's access to our data granted, limited, logged and reviewed? | | |
| C4 | Can we see an audit log of actions in our account, and export it? | | |

## D. Incidents and continuity

| # | Question | Answer | Evidence |
|---|---|---|---|
| D1 | How quickly will you notify us of a security incident affecting our data or service? (We ask for 72 hours or less.) | | |
| D2 | What are your availability commitments and service credits? | | SLA |
| D3 | What are your backup, recovery point and recovery time objectives? When did you last test a restore? | | |
| D4 | Do you have a business continuity plan that is tested at least yearly? | | |

## E. Secure development and vulnerabilities

| # | Question | Answer | Evidence |
|---|---|---|---|
| E1 | Do you follow a secure development framework (for example NIST SSDF)? How do you show it? | | |
| E2 | Do you publish a vulnerability disclosure policy and security.txt? | | Link |
| E3 | What are your fix times for critical and high vulnerabilities? | | |
| E4 | When did an independent party last test your product (penetration test)? Can we see a summary? | | Summary |
| E5 | Can you provide an SBOM (CycloneDX or SPDX) for software we run, and VEX statements for known vulnerabilities? | | |
| E6 | Are your releases signed, and how do we verify them? | | |
| E7 | If the EU Cyber Resilience Act applies to your product, how are you preparing to meet its reporting (from 11 Sep 2026) and other obligations (from 11 Dec 2027)? What is the support period? | | |

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

## Reviewer conclusion

| Field | Value |
|---|---|
| Risk rating | Low / Medium / High |
| Conditions before contract | |
| Contract clauses required | |
| Accepted risks (owner, expiry) | |
| Next review | YYYY-MM-DD |
| Approved by | |
