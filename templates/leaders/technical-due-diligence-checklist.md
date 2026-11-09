# Technical due diligence: <target company, product or supplier>

<!--
How to use: agree the scope section with the sponsor before work starts. Send the request
list in week 0. Work through the eleven areas, mark each check Done, Not available or N/A, and
record findings in the findings table. Raise any red flag to the deal lead within 24 hours.
If the target cannot produce an item, record that as a finding.
Guidance: leaders/technical-due-diligence.md
-->

| Field | Value |
|---|---|
| Target | |
| Context | acquisition / investment / outsourcing / vendor selection |
| Sponsor | |
| Review lead | |
| Team | |
| Start date | YYYY-MM-DD |
| Report due | YYYY-MM-DD |
| Access granted | data room / read-only repositories / interviews / build from source |

## 1. Scope

| Item | Detail |
|---|---|
| Thesis: what must be true for the deal to make sense | |
| Question 1 | |
| Question 2 | |
| Question 3 | |
| Out of scope | |
| Confidentiality and clean-team rules (legal advice taken?) | |

## 2. Request list

| # | Item | Requested | Received | Notes |
|---|---|---|---|---|
| R1 | C4 context and container diagrams, decision records | | | |
| R2 | Major incidents and postmortems, last 24 months | | | |
| R3 | Read-only repository access and CI history, last 6 to 12 months | | | |
| R4 | SBOM per shipped product (CycloneDX or SPDX) and licence scan result | | | |
| R5 | Last two penetration test reports; vulnerability backlog by severity and age | | | |
| R6 | Data inventory, records of processing, impact assessments, processing agreements | | | |
| R7 | Hosting and licence bills, last 12 months; last restore test result | | | |
| R8 | Certifications and audit reports (for example ISO/IEC 27001, SOC 2), open findings | | | |
| R9 | Org chart with tenure and contractor share; list of production access holders | | | |
| R10 | Critical supplier and commercial licence contracts, with change of control and exit terms | | | |
| R11 | Product and technical roadmap, capacity split, technical debt register | | | |
| R12 | AI register with risk tiers; model and data provenance; contracts with model providers; inference cost per month | | | |

## 3. Checks by area

| Area | Check | Status | Notes |
|---|---|---|---|
| 1. Architecture | Production architecture matches the diagrams | | |
| 1. Architecture | Single points of failure identified | | |
| 1. Architecture | The thesis can be met without rewriting the core | | |
| 2. Code health | Product builds from source by someone outside the core team | | |
| 2. Code health | Critical paths have automated tests | | |
| 2. Code health | Dependencies are within supported versions | | |
| 3. Delivery | Deployment frequency, change lead time, change fail rate, recovery time measured | | |
| 3. Delivery | Rollback is tested | | |
| 4. Security | Known exploited vulnerabilities closed within target | | |
| 4. Security | Incident history disclosed and consistent with other evidence | | |
| 4. Security | Access is reviewed; no shared administrator accounts | | |
| 5. Data and privacy | Lawful basis recorded for each use of personal data | | |
| 5. Data and privacy | Data location and transfers comply with the applicable law | | |
| 6. Licences | No unmet copyleft obligations in distributed products | | |
| 6. Licences | Commercial licences transfer on change of control | | |
| 7. Infrastructure and cost | Run cost trend and unit cost understood | | |
| 7. Infrastructure and cost | Backups restored and tested in the last 12 months | | |
| 8. People | Key-person risks named; at least two people can deploy and fix each critical system | | |
| 8. People | Retention plan agreed with the deal team for key people | | |
| 9. Compliance | Certifications current; open audit findings have owners and dates | | |
| 9. Compliance | No open regulatory actions unknown to the deal team | | |
| 10. Roadmap | Roadmap is staffed and funded | | |
| 10. Roadmap | Technical debt register exists and is consistent with what you found | | |
| 11. AI and models | Rights to use the training and fine-tuning data are documented | | |
| 11. AI and models | Dependence on external model providers is known, with an exit option | | |
| 11. AI and models | Inference cost as a share of revenue is known and fits the margin in the deal model | | |
| 11. AI and models | AI systems are classified by risk tier, including under the EU AI Act where it applies | | |
| Exit (outsourcing and vendors) | Data and configuration can be exported in open formats; exit cost priced | | |

## 4. Findings

Severity: Critical (breaks the thesis or creates exposure now), High (fix within 6 months, affects price or contract), Medium (fix within 12 months), Low (improvement). Flag: Red (changes price, structure or decision), Yellow (cost to plan), Observation.

| ID | Area | Finding | Evidence | Severity | Flag | Remediation | Cost low | Cost high | Time to fix | Confidence |
|---|---|---|---|---|---|---|---|---|---|---|
| F1 | | | | | | | | | | high / medium / low |
| F2 | | | | | | | | | | |

## 5. Summary for the deal team

| Item | Detail |
|---|---|
| Answer to each scoping question | |
| Red flags | |
| Total remediation cost range (low to high) | |
| Key people to retain | |
| What we could not see, and how it limits the conclusions | |
| Overall confidence | high / medium / low |

## 6. After signing: first 100 days (acquisitions)

| Item | Owner | Due | Status |
|---|---|---|---|
| Day 1: access, security controls and incident contacts in place | | Day 1 | |
| Transitional service agreements listed with exit dates (carve-outs) | | Day 30 | |
| Identity and network integration plan agreed | | Day 30 | |
| Key-person retention status | | Day 30 and day 90 | |
| Licence true-ups and contract novations listed | | Day 60 | |
| Target platform decided per capability (tolerate, invest, migrate or eliminate) | | Day 100 | |
