# Data security and privacy

Classify data, collect only what you need, encrypt it, control and log who reads it, and delete it on schedule. Most organisations cannot say where their personal data lives, who can read it, or when it is deleted, and that is what regulators, customers and attackers all find first. Privacy built into the design (GDPR Article 25) costs far less than retrofitting it after a breach or a complaint.

## Outcomes

Starting points. Tune them to your data and the laws that apply.

- 100% of data stores have an owner, a classification and a retention period in the data inventory.
- 100% of restricted and confidential data is encrypted at rest and in transit, with keys managed separately from the data.
- Every new processing of personal data that is likely to be high risk has a data protection impact assessment (DPIA) before launch.
- Zero copies of unmasked production personal data exist in development or test environments.
- Data subject requests (access, deletion) are completed within the legal deadline in 100% of cases; under GDPR this is one month, extendable in some cases.
- Automated deletion jobs run for every store with a retention period, and their results are monitored.

## Classification

Use four classes. The [data classification template](../../templates/docs/data-classification.md) has the full definitions and handling rules.

| Class | Examples | Minimum controls |
|---|---|---|
| Public | Published documentation, marketing pages | Integrity: only authorised people can change it |
| Internal | Internal wiki, non-sensitive metrics | SSO, MFA |
| Confidential | Customer records, contracts, source code, most personal data | Encryption at rest and in transit, role-based access, access logged |
| Restricted | Special category personal data (health, biometrics), payment card data, national ID numbers, credentials | Confidential controls, plus field-level encryption or tokenisation, just-in-time access, every read logged, access reviewed every quarter, strict data residency |

Government classified information follows its national scheme and stays out of this one.

## Practice

### Legal floor: applies at every level

Levels never lower a legal duty. If the GDPR or a similar law applies to you, these are required from day one, whatever level you have chosen. The playbook does not give legal advice; confirm with your data protection officer or counsel.

| Duty | GDPR | What engineering provides |
|---|---|---|
| Records of processing | Art. 30 | The data inventory below, with purpose, categories of data and people, recipients, transfers, retention and security measures. The small-firm exemption in Art. 30(5) is narrow: assume you need the record unless counsel confirms otherwise. |
| DPIA before likely high-risk processing | Art. 35 | Design input and the risks of the system, before launch, not after. |
| Processor contracts | Art. 28 | A list of every supplier that processes personal data for you, each with a signed data processing agreement. |
| Breach notification and breach register | Art. 33, 34 | A path to notify within 72 hours, and a register of every personal data breach, reported or not (Art. 33(5)). |
| Transfer mechanism for data leaving the EEA | Chapter V (Arts. 44 to 49) | The country of every copy and every remote access, and the mechanism for each transfer. |
| Lawful basis, and an Art. 9 condition for special category data | Art. 6, 9 | The purpose of each field, recorded in the inventory. |

### Foundation

1. **Data inventory.** List every database, bucket, file share, analytics tool and SaaS that holds personal or confidential data, with owner, class, location and retention. A spreadsheet is fine to start.
2. **Encrypt** at rest (storage and database encryption) and in transit (TLS everywhere, including internal traffic).
3. **Collect less.** For each personal data field, write why you need it. Drop the fields nobody can justify.
4. **Keep personal data out of logs.** Mask or drop emails, phone numbers, tokens and national IDs in application logs and error trackers.
5. **No production personal data in test.** Use synthetic data or masked copies.
6. **Breach readiness.** Know who decides whether a breach is reportable and how to reach them in 1 hour (see [incident management](../reliability/incident-management.md)). Under GDPR Article 33 the controller notifies the supervisory authority within 72 hours of becoming aware of a reportable personal data breach; other laws set their own clocks. A processor tells the controller without undue delay, so supplier contracts set a notice period well inside your own: 24 hours from the supplier becoming aware (starting point, see [third-party and SaaS risk](../security/third-party-and-saas-risk.md)).
7. **Breach register.** Record every personal data breach, reported or not, with the facts, the effects, the remedial action and the reason for the reporting decision (GDPR Art. 33(5)). Supervisors and auditors ask for this log.
8. **Records of processing.** Keep the record required by GDPR Article 30 or your local law, generated from the data inventory so the two never drift apart.
9. **DPIA** before processing that is likely to be high risk (GDPR Article 35). Article 35(3) names three cases that always need one: systematic and extensive profiling with legal or similarly significant effects, large-scale special category or criminal offence data, and large-scale systematic monitoring of public areas. Your supervisory authority publishes a longer list. New technologies such as AI on personal data often qualify. Keep it short and specific, and update it when the processing changes.
10. **Transfers.** For every supplier, subprocessor or copy outside your jurisdiction, record the transfer mechanism. Under the GDPR that is an adequacy decision (for the US, check the recipient is certified under the EU-US Data Privacy Framework), standard contractual clauses (Implementing Decision (EU) 2021/914) with a transfer impact assessment, or binding corporate rules. Remote access by supplier staff from another country is a transfer. Review the list when a supplier adds a subprocessor. Other laws have their own rules; see [Laws to check](#laws-to-check).

### Standard

1. **Privacy by design.** Every design review for a feature that touches personal data answers: what data, why, who can see it, how long, where it is stored, and how a person can see or delete their data. GDPR Article 25 requires data protection by design and by default.
2. **DPIA quality.** Every DPIA names the risks, the design changes it caused, and the residual risk owner. Revisit each one at least yearly and whenever the processing changes.
3. **Key management.** Keys in a KMS or HSM, separate from the data, rotated on schedule, with access logged (see [secrets](../security/secrets.md)).
4. **Access control and logging.** Access to confidential data by role; restricted data by just-in-time approval; every read of restricted data logged (see [access control](../security/access-control.md)).
5. **Retention and deletion.** Each store has a retention period from the inventory. Automated jobs delete or anonymise expired data, and alerts fire when they fail. Backups expire on their own schedule (see [backup and recovery](../reliability/backup-and-recovery.md)).
6. **Data subject requests.** A documented, tested process to find and export or delete one person's data across all stores, including SaaS tools and analytics.
7. **Pseudonymisation** for analytics and machine learning: replace direct identifiers with tokens; keep the mapping in a separate, restricted store.
8. **Data leakage controls.** Block public buckets by policy; scan for personal data in places it should not be; restrict bulk exports.

### Assured

Everything in Standard, plus:

1. **Records of processing checked against reality.** Each quarter, compare the record of processing with what the systems actually hold (scans of stores, supplier lists), and fix the gaps.
2. **Data residency evidence.** The country of every copy, including backups and supplier subprocessors, is enforced by policy (region controls, organisation policies) and the policy results are kept as evidence. Transfer impact assessments are reviewed when a destination's law changes (see [third-party and SaaS risk](../security/third-party-and-saas-risk.md)).
3. **Field-level encryption or tokenisation** for restricted fields, so database administrators and backups do not see clear values.
4. **Independent review** of DPIAs for high-risk processing by the data protection officer.
5. **Evidence.** Inventory, DPIAs, deletion job results and access logs kept for the audit period. This supports ISO/IEC 27001:2022 controls 5.12 (classification), 5.34 (privacy and protection of PII), 8.10 (information deletion), 8.11 (data masking), 8.12 (data leakage prevention) and 8.33 (test information). ISO/IEC 27701:2025 is a certifiable privacy information management system standard that can be used on its own or with ISO/IEC 27001.

## Laws to check

The playbook does not give legal advice. These are examples of data protection laws that set duties on engineering. Breach notification deadlines, data subject rights and transfer rules differ. List the laws that apply to you and the duty each places on your systems. Each of the laws below has its own rule for data leaving the country, so the transfer record in Foundation item 10 applies under all of them.

| Law | Transfer rule to check |
|---|---|
| EU GDPR | Chapter V: adequacy decision, standard contractual clauses with a transfer impact assessment, or binding corporate rules |
| UK GDPR | Its own Chapter V: UK adequacy regulations, the International Data Transfer Agreement or the UK Addendum to the EU clauses |
| Kenya Data Protection Act 2019 | Sections 48 to 50: conditions and safeguards for transfer out of Kenya; some processing must stay in Kenya |
| Rwanda Law No 058/2021 | Articles 48 to 50: conditions for transfer, a written contract, and storage outside Rwanda only when your registration with the supervisory authority allows it |
| Nigeria Data Protection Act 2023 | Sections 41 to 43: adequate protection in the destination, or one of the listed other bases |
| Brazil LGPD | Article 33, with the ANPD standard contractual clauses (Resolution CD/ANPD 19/2024) |
| India DPDP Act 2023 | Section 16: transfers allowed unless the government restricts the destination; sector rules can be stricter |
| California CCPA/CPRA | No transfer rule; contracts with service providers and contractors are required |

## Cloud, on-premises and air-gapped

- **Cloud:** use the provider's region controls and organisation policies to keep data in permitted regions, and customer-managed keys for restricted data.
- **On-premises and air-gapped:** encryption at rest is still needed; disks leave buildings for repair and disposal. Record media destruction.
- **Sovereignty:** some public bodies and regulated firms must keep data and keys under national jurisdiction. Customer-managed keys in the provider's KMS protect against some insider and deletion risks, not against compelled access while the provider's service processes the data. Where sovereignty requires more, use an external key manager that you operate, and record which services cannot work with it.
- **AI services:** sending personal data to a hosted model is a transfer to a supplier. Apply the same classification, contract and DPIA rules (see [AI application security](../ai/ai-application-security.md)).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Production database copied to staging "for realistic testing" | Masked or synthetic data only. |
| Retention periods written in a policy, never enforced | Automated deletion jobs with monitoring. |
| Personal data in logs kept for years | Mask in the logging library; short retention for raw logs. |
| DPIA written after launch to satisfy an auditor | DPIA at design time; it should change the design. |
| Nobody can find all of one person's data | Data inventory and a tested subject request process. |

## Templates

- [Data classification](../../templates/docs/data-classification.md)
- [Threat model](../../templates/docs/threat-model.md)
- [Vendor risk questionnaire](../../templates/docs/vendor-risk-questionnaire.md)
- [Records of processing](../../templates/security/records-of-processing.csv)
- [Personal data breach register](../../templates/security/personal-data-breach-register.csv)
- [Data protection impact assessment](../../templates/security/dpia.md)

## Sources

- Regulation (EU) 2016/679 (GDPR), Articles 6, 9, 25, 28, 30, 33, 35 and Chapter V: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Commission Implementing Decision (EU) 2021/914, standard contractual clauses for transfers: https://eur-lex.europa.eu/eli/dec_impl/2021/914/oj
- Commission Implementing Decision (EU) 2023/1795, adequacy of the EU-US Data Privacy Framework: https://eur-lex.europa.eu/eli/dec_impl/2023/1795/oj
- EDPB Recommendations 01/2020 on supplementary measures for transfers: https://www.edpb.europa.eu/our-work-tools/our-documents/recommendations/recommendations-012020-measures-supplement-transfer_en
- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
- ISO/IEC 27701:2025, privacy information management systems: https://www.iso.org/standard/27701
- OWASP Cheat Sheet Series, Logging: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
