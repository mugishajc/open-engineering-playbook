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
| Restricted | Special category personal data (health, biometrics), payment card data, national ID numbers, credentials, classified material | Confidential controls, plus field-level encryption or tokenisation, just-in-time access, every read logged and reviewed, strict data residency |

## Practice

### Foundation

1. **Data inventory.** List every database, bucket, file share, analytics tool and SaaS that holds personal or confidential data, with owner, class, location and retention. A spreadsheet is fine to start.
2. **Encrypt** at rest (storage and database encryption) and in transit (TLS everywhere, including internal traffic).
3. **Collect less.** For each personal data field, write why you need it. Drop the fields nobody can justify.
4. **Keep personal data out of logs.** Mask or drop emails, phone numbers, tokens and national IDs in application logs and error trackers.
5. **No production personal data in test.** Use synthetic data or masked copies.
6. **Breach readiness.** Know who decides whether a breach is reportable and how to reach them in 1 hour (see [incident management](../reliability/incident-management.md)).

### Standard

1. **Privacy by design.** Every design review for a feature that touches personal data answers: what data, why, who can see it, how long, where it is stored, and how a person can see or delete their data. GDPR Article 25 requires data protection by design and by default.
2. **DPIA** before high-risk processing: large-scale special category data, systematic monitoring, profiling with significant effects, new technologies such as AI on personal data (GDPR Article 35). Keep it short and specific, and update it when the processing changes.
3. **Key management.** Keys in a KMS or HSM, separate from the data, rotated on schedule, with access logged (see [secrets](../security/secrets.md)).
4. **Access control and logging.** Access to confidential data by role; restricted data by just-in-time approval; every read of restricted data logged (see [access control](../security/access-control.md)).
5. **Retention and deletion.** Each store has a retention period from the inventory. Automated jobs delete or anonymise expired data, and alerts fire when they fail. Backups expire on their own schedule (see [backup and recovery](../reliability/backup-and-recovery.md)).
6. **Data subject requests.** A documented, tested process to find and export or delete one person's data across all stores, including SaaS tools and analytics.
7. **Pseudonymisation** for analytics and machine learning: replace direct identifiers with tokens; keep the mapping in a separate, restricted store.
8. **Data leakage controls.** Block public buckets by policy; scan for personal data in places it should not be; restrict bulk exports.

### Assured

Everything in Standard, plus:

1. **Records of processing** as required by GDPR Article 30 or local law, kept current from the data inventory.
2. **Data residency and transfers.** Record the country of every copy, including backups and supplier subprocessors. Transfers outside permitted jurisdictions need a legal basis (see [third-party and SaaS risk](../security/third-party-and-saas-risk.md)).
3. **Field-level encryption or tokenisation** for restricted fields, so database administrators and backups do not see clear values.
4. **Independent review** of DPIAs for high-risk processing by the data protection officer.
5. **Evidence.** Inventory, DPIAs, deletion job results and access logs kept for the audit period. This supports ISO/IEC 27001:2022 controls 5.12 (classification), 5.34 (privacy and protection of PII), 8.10 (information deletion), 8.11 (data masking), 8.12 (data leakage prevention) and 8.33 (test information). ISO/IEC 27701 extends 27001 for privacy management.

## Laws to check

The playbook does not give legal advice. These are examples of data protection laws that set duties on engineering: EU GDPR, UK GDPR, Kenya Data Protection Act 2019, Rwanda Law No 058/2021 on personal data protection, Nigeria Data Protection Act 2023, Brazil LGPD, India DPDP Act 2023, and California CCPA/CPRA. Breach notification deadlines, data subject rights and transfer rules differ. List the laws that apply to you and the duty each places on your systems.

## Cloud, on-premises and air-gapped

- **Cloud:** use the provider's region controls and organisation policies to keep data in permitted regions, and customer-managed keys for restricted data.
- **On-premises and air-gapped:** encryption at rest is still needed; disks leave buildings for repair and disposal. Record media destruction.
- **Sovereignty:** some public bodies and regulated firms must keep data and keys under national jurisdiction. Hold keys in your own HSM even when data sits with a cloud provider.
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

## Sources

- Regulation (EU) 2016/679 (GDPR), Articles 25, 28, 30, 33, 35: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
- ISO/IEC 27701, privacy information management: https://www.iso.org/standard/27701
- OWASP Cheat Sheet Series, Logging: https://cheatsheetseries.owasp.org/cheatsheets/Logging_Cheat_Sheet.html
