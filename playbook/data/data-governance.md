# Data governance

Most organisations cannot answer three questions quickly: what data do we hold, who owns it, and are we allowed to use it for this purpose, including training or prompting an AI model? Give every important data set a named owner, a classification and a retention rule, record them in a catalogue, and agree changes between producers and consumers with data contracts. Keep the process light enough that teams use it while they build, not after an incident.

## Outcomes

Starting points. Tune them to your organisation.

- At least 90% of production data stores appear in the catalogue with an owner, a classification and a retention period.
- Every use of personal data has a documented lawful basis (GDPR Article 6 or your local equivalent), plus an Article 9 condition for special category data. Every use of other confidential or restricted data has a documented business purpose.
- Every new system that processes personal data has a privacy review before production. High-risk processing has a data protection impact assessment (DPIA).
- Breaking changes to a shared data set are announced through its data contract at least 30 days before release (or the period the contract sets).
- Retention rules are enforced automatically for at least 80% of personal data stores.

## Core elements

| Element | What it is | Owner |
|---|---|---|
| Data owner | the person accountable for a data set: who may use it, for what, for how long | business or product lead for that domain |
| Data steward | the person who maintains definitions, quality rules and catalogue entries | engineer or analyst in the owning team |
| Catalogue | a searchable list of data sets with owner, classification, location, lineage and retention | platform or data team |
| Classification | a label that sets handling rules (see below) | data owner |
| Data contract | an agreement between a producer and its consumers on schema, meaning, quality and change process | producing team |
| Retention schedule | how long each class of data is kept and how it is deleted | data owner with legal and records |

DAMA-DMBOK is the reference body of knowledge for data management. Use it to check you have not missed an area. Do not try to implement all of it at once.

## Classification

Four levels work for most organisations. Use the [data classification template](../../templates/docs/data-classification.md) to write your handling rules.

| Level | Examples | Typical handling (starting point) |
|---|---|---|
| Public | published reports, marketing pages, open data | integrity checks; no access limits |
| Internal | internal wikis, non-sensitive metrics | staff access only; no public sharing |
| Confidential | customer records, contracts, source code, most personal data | need-to-know access, encryption at rest and in transit, logged access, no use in external AI tools without approval |
| Restricted | special category personal data, credentials, payment card data, national ID numbers | named access with approval, strong encryption with managed keys, approved locations only, no copies outside production |

Government classified information follows its national classification scheme, with its own vetting and accreditation rules. Keep it out of this scheme and do not mix it with ordinary restricted data.

## Privacy by design

- Build data protection into the design, not after it. GDPR Article 25 requires data protection by design and by default, and similar duties exist in other laws.
- Collect only the data the purpose needs. Set the shortest retention that meets the purpose and the law.
- Run a DPIA before processing that is likely to be high risk (GDPR Article 35). This and the other legal duties in the [legal floor](data-security-and-privacy.md#legal-floor-applies-at-every-level) apply at every level.
- Laws to check include the EU GDPR, UK GDPR, Kenya Data Protection Act 2019, Rwanda Law No 058/2021, Nigeria Data Protection Act 2023, Brazil LGPD, India DPDP Act 2023 and California CCPA/CPRA. This is not legal advice.
- Technical controls (encryption, masking, deletion) are covered in [data security and privacy](data-security-and-privacy.md).

## Data and AI

- Record in the catalogue whether each data set may be used for training, fine-tuning, retrieval or prompting, and with which providers.
- Confidential data goes to an external AI service only when the data owner approves and the contract covers data use, retention, training and location. Restricted data never goes to one, unless the CISO and the data owner approve a specific service, with a DPIA and contract terms on retention and training, recorded as an exception. The [data classification template](../../templates/docs/data-classification.md) uses the same rule.
- Keep lineage from source data to model and to output so you can answer "which data trained this?" See [AI governance](../ai/ai-governance.md) and [data quality](data-quality.md).

## Organising data ownership

Start with ownership by the team that produces the data. A central data team runs the catalogue and shared tooling. Data mesh, as described by Zhamak Dehghani, pushes ownership further into domain teams with data products and federated governance. Treat it as an option for large organisations with many domains and strong platform support, not a default. See [team topology](../operating-model/team-topology.md).

## Practice

### Foundation

Solo and Startup. Keep a one-page list of data stores with owner, classification and retention. Mark which ones hold personal data. Write a short privacy notice that matches what you actually do. Delete what you do not need. If a data protection law applies to you, the list also serves as your record of processing, and the [legal floor](data-security-and-privacy.md#legal-floor-applies-at-every-level) applies now, not at a later level.

### Standard

Scale-up and Enterprise. A catalogue fed automatically from schemas and infrastructure code. Named owners and stewards. Data contracts for shared data sets, checked in CI. Retention enforced by scheduled jobs. Privacy review in the [production readiness](../reliability/production-readiness.md) checklist.

### Assured

Regulated and Public sector. Everything in Standard, plus a data protection officer consulted on new processing, DPIAs reviewed independently, access reviews every quarter for restricted data, a records retention schedule agreed with the records office, and evidence for the controls in [control mapping](../compliance/control-mapping.md).

## Cloud, on-premises and air-gapped

Record the physical and legal location of every copy, including backups, logs and caches, and the supplier staff who can access them. Access by supplier staff from another country is a transfer and needs a transfer mechanism (see [data security and privacy](data-security-and-privacy.md), Foundation item 10). In air-gapped networks, the catalogue runs inside the network; only approved metadata leaves it. Check that cloud data services used for analytics or AI keep data in approved regions.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A governance committee that approves every query | Owners set rules once; access follows the classification. |
| A catalogue filled in by hand once | Generate entries from schemas and infrastructure code. |
| Everything marked confidential | Use the definitions. Over-classifying hides what really matters. |
| Personal data copied into test environments | Masked or synthetic test data only. |
| Data mesh as a reorganisation slogan | Fix ownership and contracts first; adopt mesh only if scale requires it. |

## Templates

- [Data classification](../../templates/docs/data-classification.md)
- [Records of processing](../../templates/security/records-of-processing.csv)
- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml)
- [Risk register](../../templates/strategy/risk-register.csv)

## Sources

- DAMA International, DAMA-DMBOK: https://www.dama.org
- EU GDPR, Regulation (EU) 2016/679 (Articles 6, 9, 25 and 35): https://eur-lex.europa.eu/eli/reg/2016/679/oj
- ISO/IEC 27001:2022, Annex A 5.12 (classification) and 5.34 (privacy and protection of PII): https://www.iso.org/standard/27001
- Zhamak Dehghani, "Data Mesh", O'Reilly Media, 2022.
