# User acceptance testing sign-off: [service or release]

<!--
How to use: agree sections 1 to 4 before UAT starts. Fill in sections 5 to 8 during and after UAT.
The accountable business owner signs section 9. A signature means the signer accepts the open
defects and risks listed here; it is a decision, not a formality. Keep this record with the release.
Guidance: playbook/quality/exploratory-and-acceptance-testing.md
-->

| Field | Value |
|---|---|
| Service or system | [name] |
| Release or version | [version, artifact digest] |
| Business owner (accountable, signs) | [name, role] |
| Service owner | [name, role] |
| UAT coordinator | [name] |
| UAT environment | [name, link to parity list] |
| UAT dates | [YYYY-MM-DD to YYYY-MM-DD] |
| Reason for a formal UAT | [system replacement / packaged software / supplier delivery / regulated release / other] |

## 1. Scope

Business processes in scope, each tested end to end:

| # | Business process | Roles involved | Critical (Yes/No) |
|---|---|---|---|
| P1 | [register a new business, from application to certificate] | [applicant, case officer, supervisor] | Yes |
| P2 | | | |

Out of scope, and why: [ ]

## 2. Participants

Real users from each role. Not the project team.

| Name | Role in daily work | Process(es) | Assistive technology used (if any) | Time released from day job |
|---|---|---|---|---|
| | | | | |

## 3. Severity definitions

| Severity | Meaning |
|---|---|
| 1 | A business process cannot be completed, money or data is wrong, or a legal duty is broken. No workaround. |
| 2 | A process can be completed only with a costly or error-prone workaround |
| 3 | A process works with a reasonable workaround, or a minor error |
| 4 | Cosmetic |

## 4. Entry criteria (all must be met before UAT starts)

- [ ] Automated tests green on the release artifact
- [ ] No open severity 1 defects
- [ ] Environment stable, with integrations connected (sandbox mode where needed): [list]
- [ ] Realistic data loaded: [synthetic / masked copy with approval record link]; migrated records included for replacements
- [ ] Participants trained and their time booked
- [ ] Exploratory testing of the high-risk areas completed by the team

Entry criteria confirmed by [name] on [YYYY-MM-DD].

## 5. Results by process

| # | Process | Completed end to end by users (Yes/No) | Participants | Defects raised (IDs) | Notes |
|---|---|---|---|---|---|
| P1 | | | | | |
| P2 | | | | | |

## 6. Open defects and change requests at sign-off

| ID | Summary | Severity | Process | Workaround | Fix by (date or release) | Owner |
|---|---|---|---|---|---|---|
| | | | | | | |

Change requests raised during UAT (new or different behaviour, not failures against the agreed criteria). They do not block exit; the business owner decides which must come before go-live.

| ID | Summary | Raised by | Needed before go-live (Yes/No) | Decided by |
|---|---|---|---|---|
| | | | | |

## 7. Data migration checks (replacements only)

| Check | Old system | New system | Match (Yes/No) | Notes |
|---|---|---|---|---|
| Record count: [entity] | | | | |
| Control total: [for example open balances] | | | | |
| Sample of [number] records compared field by field | | | | |
| Rehearsals completed and timed | [number, durations] | | | |

## 8. Exit criteria

- [ ] Every critical process completed end to end by users
- [ ] No open severity 1 defects
- [ ] Each open severity 2 defect has a workaround and a written risk acceptance below
- [ ] Results and defects recorded in sections 5 and 6

## 9. Decision

Decision: [Accepted / Accepted with conditions / Rejected]

Conditions (if any), each with an owner and date: [ ]

Risks accepted (open severity 2 defects and anything not tested):

| Risk | Why acceptable | Until |
|---|---|---|
| | | |

| Role | Name | Signature | Date |
|---|---|---|---|
| Business owner (accountable) | | | |
| Service owner | | | |
| [Assured: independent reviewer] | | | |

## 10. After go-live

At 30 days, record severity 1 and 2 defects found in production that participants would have met in their normal work: [count, IDs]. Use this to improve the next UAT.
