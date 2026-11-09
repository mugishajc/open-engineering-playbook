# Data classification and handling rules: [organisation]

<!-- Guidance: playbook/data/data-governance.md. Adapt the four levels to any national scheme you must follow. Not legal advice. -->

| Field | Value |
|---|---|
| Owner | [data protection officer, CISO or head of data] |
| Approved by | [name, date] |
| Next review | [YYYY-MM-DD, at most 12 months away] |

## 1. Levels

| Level | Definition | Examples |
|---|---|---|
| Public | approved for anyone to see | published reports, open data, marketing pages |
| Internal | for staff and contractors; low harm if disclosed | internal wiki, team metrics, non-sensitive tickets |
| Confidential | harm to people or the organisation if disclosed | customer records, most personal data, contracts, source code |
| Restricted | serious harm if disclosed or changed | special category personal data, credentials and keys, payment card data, national ID numbers |

Government classified information follows its national scheme and is out of scope of this template.

## 2. Handling rules

| Rule | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Who can access | anyone | staff and contractors | need to know, by role | named people, approved per request |
| Encryption in transit | recommended | required | required | required |
| Encryption at rest | optional | required on portable devices | required | required, keys in a managed key store |
| Access logging | no | optional | required | required and reviewed quarterly |
| Allowed hosting locations | any | [approved providers] | [approved regions] | [named data centres or regions only] |
| Copies in test or dev environments | allowed | allowed | masked or synthetic only | never |
| Use in external AI tools | allowed | approved tools only | only with data owner approval and a contract covering use, retention, training and location | never, unless the CISO and the data owner approve a specific service with a DPIA and contract terms on retention and training, recorded as an exception |
| Sharing with suppliers | allowed | under contract | under contract with data protection terms | only with approval from [role] |
| Retention | [...] | [...] | [per retention schedule] | [per retention schedule] |
| Disposal | none | standard delete | verified delete (NIST SP 800-88 Rev. 2 or national equivalent; for cloud storage, destroy the encryption key) | verified delete with record |

## 3. Labelling

- Data stores carry the level as a tag or catalogue field: [tag name, for example `data_class`].
- Documents show the level in the header or footer.
- When data of different levels is combined, the result takes the highest level.

## 4. Data store inventory

| Data store | Owner | Level | Personal data (yes, no) | Location | Retention | Allowed AI use |
|---|---|---|---|---|---|---|
| [EXAMPLE: customer database] | [name] | Confidential | yes | [region] | [7 years after account closure] | retrieval with approval; no training |
| [EXAMPLE: public website content] | [name] | Public | no | [any] | [until replaced] | any |
| [EXAMPLE: secrets store] | [name] | Restricted | no | [region] | [until rotated] | never |

## 5. Exceptions

Exceptions need the data owner's approval, a reason, a compensating control and an expiry date no more than 12 months away. Record them in the waiver register.
