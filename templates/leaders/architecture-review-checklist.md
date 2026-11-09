# Architecture review: <system or change name>

<!--
How to use: the proposing team fills in the header and the "Answer" and "Evidence" columns
before the review, and shares this file at least 2 working days ahead. Reviewers read it
before the session. Answer Yes, No or N/A (with reason). A claim without evidence counts as No.
Run the review in 90 minutes. Answer within 5 working days of the request (a starting point).
Guidance: leaders/architecture-toolkit.md and playbook/architecture/architecture-practice.md
-->

| Field | Value |
|---|---|
| System or change | |
| Proposing team and owner | |
| Review trigger | hard to reverse / 3+ teams affected / off the tech radar / regulated data / high-risk AI / other: |
| Linked RFC or decision record | |
| Reviewers | |
| Review requested | YYYY-MM-DD |
| Review held | YYYY-MM-DD |
| Outcome | Approved / Approved with conditions / Rework |

## 1. Problem and context

| # | Question | Answer | Evidence |
|---|---|---|---|
| 1.1 | The problem and the business outcome are stated in a few sentences | | |
| 1.2 | A C4 context diagram and container diagram are attached and current | | |
| 1.3 | The options considered, including "do nothing", are listed with reasons for rejection | | |
| 1.4 | The design follows a reference architecture, or says why not | | |

## 2. Quality attributes

| # | Question | Answer | Evidence |
|---|---|---|---|
| 2.1 | The top five quality attributes are ranked (see quality-attributes-checklist.md) | | |
| 2.2 | Each top attribute has at least one scenario with a response measure | | |
| 2.3 | The top three scenarios were walked through the design in the review | | |
| 2.4 | Sensitivity points and trade-off points are written down | | |

## 3. Reversibility and dependencies

| # | Question | Answer | Evidence |
|---|---|---|---|
| 3.1 | The cost of reversing the decision in two years is estimated | | |
| 3.2 | Behaviour is described for each dependency being slow or unavailable | | |
| 3.3 | Each external supplier or product has an exit plan and data export path | | |
| 3.4 | New technologies are on the tech radar, or a radar change is proposed | | |

## 4. Data, security and compliance

| # | Question | Answer | Evidence |
|---|---|---|---|
| 4.1 | Data flows are drawn, with classification of each data store | | |
| 4.2 | Personal or regulated data has a lawful basis, residency and retention rule | | |
| 4.3 | A threat model exists for new external interfaces | | |
| 4.4 | Authentication, authorisation and secrets handling follow the standard | | |
| 4.5 | AI components have a use-case assessment where required | | |

## 5. Operability and cost

| # | Question | Answer | Evidence |
|---|---|---|---|
| 5.1 | Deployment, rollback and feature flag strategy are described | | |
| 5.2 | SLOs, dashboards, alerts and runbooks are planned | | |
| 5.3 | Run cost is estimated at today's load and at 10 times today's load | | |
| 5.4 | The owning team in production is named and has the skills, or a plan to get them | | |
| 5.5 | The design works in each required environment (cloud, on-premises, air-gapped) | | |

## 6. Keeping it true

| # | Question | Answer | Evidence |
|---|---|---|---|
| 6.1 | Fitness functions are named for the top quality attributes | | |
| 6.2 | The decision record will be updated with the outcome and conditions | | |

## Outcome

| Item | Detail |
|---|---|
| Decision | Approved / Approved with conditions / Rework |
| Risks accepted, and by whom | |
| Conditions (each with owner and date) | |
| Review date for the decision | YYYY-MM-DD |
