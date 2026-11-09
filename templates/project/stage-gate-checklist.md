# Stage gate checklist: [project name], gate [number and name]

<!--
How to use: the project manager fills sections 1 to 3 and sends them with the evidence at least
2 working days before the gate. The sponsor records the decision in section 4 at the gate and
the project manager tells the team within 2 working days. Criteria and stop conditions come from
the charter and must not be rewritten at the gate. Evidence means working software and measured
results; a plan is evidence only of intent.
Guidance: playbook/project-management/risks-raid-and-stage-gates.md
-->

| Field | Value |
|---|---|
| Gate | [0 Start / 1 End of discovery / 2 End of alpha / 3 Go/no-go / 4 Close] |
| Date | [YYYY-MM-DD] |
| Sponsor (decides) | [name] |
| Steering group present | [names] |
| Independent reviewer (Large projects) | [name, organisation or programme] |
| Charter version | [link and version] |

## 1. Exit criteria from the charter

| Criterion (as written in the charter) | Met? | Evidence (link) |
|---|---|---|
| [...] | [yes / partly / no] | [...] |

## 2. Questions for every gate

- [ ] Would we start this project today, knowing what we know now? Answer without counting money already spent.
- [ ] Is the outcome still wanted by the senior user, and is it still the right outcome?
- [ ] Forecast at 50% and 85% confidence for date and cost, compared with tolerance: [...]
- [ ] Has any written stop condition been met? [no / yes: which]
- [ ] Top 5 items in the risks, assumptions, issues and dependencies (RAID) log reviewed; each has an owner and an action due before the next gate.
- [ ] Conditions set at the last gate: all met by their dates? [yes / no: which]. A criterion passed with conditions at the last gate cannot pass with conditions again.
- [ ] Assumptions due for testing in this stage have been tested. Results: [...]
- [ ] Contingency used in this stage and the reason; unused contingency to return: [...]
- [ ] The team that will own the result is named and has agreed.
- [ ] Next stage exit criteria and stop conditions are written as numbers.

## 3. Questions for specific gates

**Gate 1, end of discovery**

- [ ] User needs found through research with real users, not only stakeholders.
- [ ] Options include "do nothing" and "improve what we have", each with a cost range.
- [ ] First estimate is a range with its reference class named.

**Gate 2, end of alpha**

- [ ] The riskiest assumptions were tested with prototypes, spikes or real data samples.
- [ ] The estimate range has narrowed, and the reason it narrowed is recorded.
- [ ] Must haves are no more than 60% of estimated effort.
- [ ] For a supplier contract: acceptance is defined as working software passing agreed tests, with an acceptance period and a named signatory; access to the supplier's repositories, pipeline and defect data is in the contract.
- [ ] For a supplier contract: change request process and rate card, warranty terms, money held back until warranty ends, and an exit plan are in the contract. For public contracts, the flexibility needed (priorities, options, exchange clause) is in the tender.
- [ ] Benefit owners named and benefit baselines planned, to be measured before go-live.

**Gate 3, go/no-go** (criteria agreed at least 4 weeks before; the date is not a criterion)

- [ ] All Must haves accepted by the business owner.
- [ ] No open severity 1 defects; severity 2 within the agreed limit, each with a tested workaround.
- [ ] Performance tested at expected peak plus the agreed margin.
- [ ] Security testing done; findings within appetite.
- [ ] Final migration rehearsal reconciled: 100% for money and legal records; [agreed rate] for others.
- [ ] Cutover runbook rehearsed at least twice with real data volumes; the last rehearsal fitted the outage window.
- [ ] Rollback or fall-back tested and timed; the point of no return and the checkpoint criteria are written.
- [ ] Hypercare staffed, with a length and written exit criteria.
- [ ] Benefit baselines measured and recorded.
- [ ] Any criterion with no current evidence is marked not met.
- [ ] Production readiness review passed; support staffed; users trained; communications ready.

**Gate 4, close**

- [ ] Service handed to its owning team with an agreed run budget.
- [ ] Every open RAID item transferred or closed with a reason.
- [ ] Old system switched off and its contracts ended, or a dated plan approved.
- [ ] Lessons learned session held; outcome register entry written.
- [ ] Hypercare ended on its exit criteria; warranty start and end dates recorded.
- [ ] Benefits reviews booked at 6 and 12 months, each benefit with a business owner.

## 4. Decision

| Decision | Tick one |
|---|---|
| Continue | [ ] |
| Continue with conditions (list below, each with owner and date) | [ ] |
| Rescope (new baseline approved, attached) | [ ] |
| Pause (date to decide again: [...]) | [ ] |
| Stop (release the team within 2 weeks; write the decision record) | [ ] |

- Reason: [...]
- Conditions: [...]
- Funding released for the next stage: [...]
- Contingency returned to the portfolio: [...]
- Signed by the sponsor: [name, date]
