# Project charter: [project name]

<!--
How to use: write this before the first gate and sign it at the gate that funds build (end of
alpha for digital work). Update it at every gate; keep earlier versions. One to three pages.
For a change to how teams work, use templates/strategy/transition-charter.md instead.
Square brackets mark your own data; never invent figures.
Guidance: playbook/project-management/projects-and-products.md and
playbook/project-management/planning-fixed-scope-and-budget.md
-->

| Field | Value |
|---|---|
| Sponsor (accountable, chairs the steering group) | [name, role] |
| Senior user (business owner receiving the change) | [name, role] |
| Senior supplier (engineering head, and systems integrator lead if any) | [names, roles] |
| Project manager | [name] |
| Product manager | [name, or "same as project manager" for small projects] |
| Technical lead | [name] |
| Team or teams doing the work | [persistent teams, suppliers] |
| Team that will own the result after close | [name; required before the first gate] |
| Governance class | [Small / Medium / Large] |
| Charter version and date | [v1.0, YYYY-MM-DD] |

## 1. Problem and outcome

- Problem, with evidence: [...]
- Outcome in one sentence: [what will be different, for whom, measured how]
- Strategy action or business case this serves: [link]

## 2. What is fixed, and why

Fix no more than two of scope, date and cost. If a contract or law fixes all three, record the risk to quality in the risks, assumptions, issues and dependencies (RAID) log with the sponsor as owner.

| Constraint | Fixed? | Source (law, contract, tender, budget year, event) | What can still change |
|---|---|---|---|
| Date | [yes / no] | [...] | [...] |
| Cost | [yes / no] | [...] | [...] |
| Scope | [yes / no] | [...] | [...] |

Procurement route and change limits (public contracts): [route; review clauses and options in the tender; exchange clause yes / no; change budget; the legal limit on changes without a new procurement, confirmed by procurement]

## 3. Scope

| Priority | Items | Share of estimated effort |
|---|---|---|
| Must have (illegal, unsafe or unworkable without it) | [...] | [no more than 60%] |
| Should have | [...] | [...] |
| Could have (first contingency) | [...] | [about 20%] |
| Won't have this time | [...] | n/a |

Out of scope: [...]

## 4. Estimate

| | 50% confidence | 85% confidence | Reference class used |
|---|---|---|---|
| Cost | [...] | [...] | [past projects of the same kind, or published class] |
| Duration or date | [...] | [...] | [...] |

Main assumptions (each one is in the RAID log with a test date): [...]

## 5. Budget

| Line | Amount | Held by | Released |
|---|---|---|---|
| Base estimate (50%) | [...] | project manager | per stage, at each gate |
| Contingency (to [80% / 85%] confidence) | [...] | project manager within tolerance; steering above | against a named RAID item, logged |
| Management reserve (unforeseen work inside scope; not for new scope) | [...] | sponsor | by the sponsor at a gate or exception, with a re-baseline |
| Capital and operating split | [...] | finance | n/a |

## 6. Tolerances

Within these limits the project manager acts without asking. A forecast outside them is red and goes to the steering group within 5 working days.

| Dimension | Tolerance |
|---|---|
| Date (85% forecast) | [for example: up to 4 weeks later than baseline] |
| Cost (estimate at completion) | [for example: up to 5% over base, within contingency] |
| Scope | [for example: Could haves may be dropped; no Must have may be dropped] |
| Quality | [for example: no severity 1 defects at release; go/no-go criteria unchanged] |
| Risk | [for example: no risk above the organisation's appetite without steering approval] |
| Benefits | [for example: forecast benefits no less than 80% of the business case] |
| Sustainability (if your organisation sets targets; PRINCE2 7th edition includes it) | [for example: run-time energy or carbon no higher than the system it replaces] |

## 7. Stages, gates and stop conditions

| Stage | Planned dates (range) | Budget | Exit criteria | Stop conditions (as numbers) |
|---|---|---|---|---|
| Discovery | [...] | [...] | [...] | [...] |
| Alpha | [...] | [...] | [...] | [...] |
| Beta or build | [...] | [...] | [...] | [...] |
| Go/no-go and release | [...] | [...] | [go/no-go criteria agreed 4 weeks ahead] | [...] |
| Close | [...] | [...] | [handover, RAID transferred, old system off] | n/a |

Example stop condition: "Stop if the alpha migration rehearsal does not reconcile 100% of account balances by [date]."

## 8. Dependencies, suppliers and contracts

| Dependency or contract | Provider owner | Needed by | Agreed by provider | Contract end or notice date |
|---|---|---|---|---|
| [...] | [...] | [...] | [yes / no] | [...] |

For each supplier contract, record where these are written (clause number): acceptance tests, acceptance period and signatory; change request process and rate card; warranty start, length and fix times; amount held back until warranty ends; exit plan and handover help; delay damages and their cap; named key people.

## 9. Business change

- Users and staff affected: [...]
- Training, process and communication plan owner: [...]
- Old system or process to be switched off, and date: [...]
- Cutover approach: [gradual release by user group / one cutover]; point of no return: [...]; rollback rehearsed by: [date]; hypercare length and exit criteria: [...]

## 10. Reporting and governance

- Status report: every 2 weeks, colours set by rule. [link to the status report]
- RAID log: [link]
- Steering group members and meeting rhythm: [...]
- Independent assurance (Large projects): [who, at which gates]

## 11. Benefits

| Benefit | Measure and source system | Baseline (value and date measured, before go-live) | Target and when | Business change it depends on | Review dates (6 and 12 months after release) | Benefit owner (in the business, not the project manager) |
|---|---|---|---|---|---|---|
| [...] | [...] | [...] | [...] | [...] | [...] | [...] |

Dis-benefits (costs or losses the change causes, such as a new run cost or a slower step for some users): [...]

## 12. Approvals

| Name | Role | Decision | Date |
|---|---|---|---|
| [...] | Sponsor | [...] | [...] |
| [...] | Senior user | [...] | [...] |
| [...] | Senior supplier | [...] | [...] |
| [...] | Finance partner | [...] | [...] |
