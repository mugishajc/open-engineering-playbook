# Decision game: the red project before go-live

A new pensions system goes live in six weeks. The systems integrator's report has been green for nine months, and the board chair has announced the date in public. Then your own test lead tells you that two of three migration rehearsals failed to reconcile. You are the sponsor. Choose what you do, then see what happens.

| | |
|---|---|
| Who | Sponsors, programme directors, heads of project management offices (PMOs), chief information officers (CIOs) and procurement leads. Play alone, or as a group with the business owner, the test lead and someone from procurement in the room. |
| Time | 30 minutes alone; 45 minutes as a group |
| Practice it teaches | [Status reporting](../../playbook/project-management/status-reporting.md), [risks, RAID logs and stage gates](../../playbook/project-management/risks-raid-and-stage-gates.md), [planning fixed scope and budget](../../playbook/project-management/planning-fixed-scope-and-budget.md), [for programme and portfolio leaders](../../leaders/for-programme-and-portfolio-leaders.md) |

## The situation

A public pensions fund pays 180,000 pensioners on the 25th of every month from an administration system built 20 years ago. It is replacing the system under a fixed-price contract with a systems integrator (SI). All organisations, people and numbers here are fictional; amounts are in currency units (CU).

- Contract: 14 million CU fixed price, awarded through a public tender. A milestone payment of 3 million CU is due on go-live acceptance. The contract has delay damages capped at 0.5 million CU, and a right for the fund to commission independent testing.
- Go-live is planned for the weekend after a monthly payment run, so the first payment run on the new system comes about 4 weeks after go-live.
- The old system's support contract ends 8 weeks after the planned go-live. The vendor will extend it in blocks of 3 months, at 0.6 million CU per block, if asked at least 4 weeks ahead.
- The SI's status has been green for 9 months. Its latest report says "92% of test cases executed".
- Your test lead's figures: 61% of end-to-end tests passed on the last run. 4 severity 1 and 38 severity 2 defects are open. About 30 new defects arrive each week and about 25 are fixed.
- Three migration rehearsals have run. The first two failed to reconcile. The third matched every member record, but calculated payment amounts differed from the old system for 1,100 members (about 0.6%).
- The performance test for the payment run has not been done.
- Half of the fund's staff have been trained.
- Contingency: 0.4 million CU left of the original 1.5 million CU. The sponsor also holds a management reserve of 1.0 million CU, released only by the sponsor at a steering group meeting.
- The risks, assumptions, issues and dependencies (RAID) log has 140 items; 60 have overdue actions.

## Round 1: what do you do this week?

**A. Hold the date and push.** The status is green and the date is public. Ask the SI for a recovery plan, weekend working and a daily defect call. Moving the date means public embarrassment and paying for the support extension.

**B. Add people.** Ask the SI to bring 15 more engineers onto the project for the last six weeks. Argue later about who pays.

**C. Announce a delay now.** Tell the board the date moves by 6 months, to be safe.

**D. Get the truth in 10 working days.** Commission an independent readiness review against written go/no-go criteria, using the contract's right to independent testing. Reset the status rules so colours follow the forecast against tolerance. Call an extra steering meeting for day 10 to decide on options. Ask the old vendor for a price and a deadline for a support extension, as an option, not a decision. Tell the board chair that a decision on the date comes on day 10, with evidence.

Choose before you open the consequences.

<details>
<summary>Consequences of A: hold the date and push</summary>

The SI works weekends. Defects close faster for two weeks, then rushed fixes cause new ones, and the inflow rises. The fourth migration rehearsal, four weeks before go-live, fails to reconcile again. The go/no-go meeting treats the public date as the deciding criterion and approves go-live. There is no performance test result, and nobody has tested the payment file with the bank.

On the first payment day, the bank rejects the payment file. The SI fixes it overnight and the run is repeated, so most pensions arrive a day late. About 1,100 pensioners receive the wrong amount: some too much, some too little. The phone lines are overwhelmed, staff correct payments by hand, and the ombudsman and the regulator open cases. The fund paid the 3 million CU milestone on go-live, so its main lever on the SI is gone. With the old system's support ending in 8 weeks and data now changed in the new system, there is no practical fall-back. The cost of correction, complaints and lost trust is far larger than a support extension would have been.

The date was never a go/no-go criterion. See [go/no-go before go-live](../../playbook/project-management/risks-raid-and-stage-gates.md#gono-go-before-go-live).

</details>

<details>
<summary>Consequences of B: add people</summary>

The new engineers need access, test environments and an explanation of 20 years of pension rules. The engineers who know the rules spend their time teaching. The shared test environment, already the bottleneck, now has more people waiting for it. Defect inflow rises. Under the fixed-price contract, the SI raises a change request for the extra people, arguing the delay came from late business decisions. The remaining contingency of 0.4 million CU cannot cover it. Six weeks later the project is in a worse position and in a contract dispute.

"Adding manpower to a late software project makes it later" (Brooks, 1975). See [when the project is late](../../playbook/project-management/planning-fixed-scope-and-budget.md#when-the-project-is-late).

</details>

<details>
<summary>Consequences of C: announce a 6-month delay now</summary>

Better than A, because it stops the slide towards a bad go-live. But 6 months is a guess. The board asks why 6, and nobody can answer. The new date has no more evidence behind it than the old one, so the board does not believe it either. You will pay for two support extensions, may lose the SI's best people to other contracts, and still do not know what is actually broken. It might take 3 months; it might take 9.

A new date needs a forecast range with evidence. See [estimate with ranges and reference classes](../../playbook/project-management/planning-fixed-scope-and-budget.md#estimate-with-ranges-and-reference-classes).

</details>

<details>
<summary>Consequences of D: get the truth in 10 working days</summary>

The review costs 0.1 million CU from contingency, leaving 0.3 million CU. The SI objects to an outside team in its test environment until you point to the contract clause. The board chair is unhappy to wait 10 days, but agrees. The review finds:

- The core pension calculation is correct for every member category except two: members with protected rights from an old scheme merger, and members part-way through a transfer out. Together they are the 1,100 members whose payments differed. The other 178,900 members reconciled with no payment differences in rehearsal 3.
- "92% executed" hid the 61% pass rate. Most failing tests are in the two categories and in the payment file sent to the bank.
- Three of the 4 severity 1 defects are in the payment file, which affects every member. The SI forecasts the fix in 2 to 3 weeks, and the bank can test the file in week 5.
- A first performance test, run during the review, completes the monthly payment run in 5 hours against a 6-hour window. The margin is thin but inside the window.
- The forecast for fixing the two categories and running two clean rehearsals, from the defect fix rate and a reference class of the SI's past projects: 8 weeks at 50% confidence, 14 weeks at 85%, counted from day 10. With the review taking 2 of the 6 weeks, that is 4 weeks and 10 weeks after the planned go-live date.

Go to round 2.

</details>

## Round 2: with the review's findings

The steering group meets on day 10, 4 weeks before the planned go-live, which is the latest point to agree go/no-go criteria. The support extension must be requested by week 10 to avoid a gap. Three options are on the table.

**E. Go live on the date for everyone.** Staff calculate the 1,100 payments by hand outside the system each month until the fix arrives. The SI receives its milestone payment on go-live.

**F. Release in phases.** On the planned date, move the 178,900 members whose categories reconciled with no payment differences. Keep the two failing categories on the old system, extend its support by one 3-month block (0.6 million CU), and reconcile both systems daily. Move the remaining members when two rehearsals in a row reconcile. Split the milestone payment by phase, agreed as a contract change that procurement confirms is allowed. The go/no-go criteria for phase 1 still apply in full, including a payment file the bank has accepted.

**G. Move the whole go-live by 14 weeks:** the 85% readiness date plus 4 weeks for the final go/no-go, cutover rehearsal and a clean start after a payment run. One block of support (0.6 million CU) covers the old system to 7 weeks after the new date, enough for one payment run on the new system. A second block (another 0.6 million CU) keeps a fall-back through three payment runs. One cutover, when everything reconciles.

<details>
<summary>Consequences of E, F and G</summary>

**E** looks cheap and is not. Hand calculation of the most complex pensions by staff who were trained on the new system, not the old rules, produces errors every month. The workaround has no tested procedure and no audit trail. Paying the milestone on full go-live removes your main lever on the SI to finish the fix. Manual workarounds have a habit of becoming permanent. Choose this only when the affected group is tiny and the workaround is tested and audited; here it is neither.

**F** delivers the new system to almost every pensioner on the public date, and tests it in production with a limited blast radius. It works only if the split is clean in the data: each member is paid by exactly one system, and one system owns writes for each member. It also depends on the payment file fix landing in time; if the bank has not accepted the file by the go/no-go meeting, phase 1 does not go and F becomes G. It costs the support extension, daily reconciliation and a second cutover, and it adds complexity that must be capped; see [running old and new in parallel](../../playbook/strategy/transition-playbook.md#running-old-and-new-in-parallel). The 0.6 million CU is more than the 0.3 million CU of contingency left, so the sponsor releases 0.3 million CU of management reserve at the steering group: the kind of unforeseen cost the reserve exists for. The board gets the truth: the date holds for most people, and the rest follows within a forecast range.

**G** is also defensible. One cutover is simpler than two, and there is no parallel running. It costs up to 1.2 million CU of support, which uses the remaining contingency and up to 0.9 million CU of the 1.0 million CU reserve, leaving almost nothing for the next surprise. It moves the public date, but the new date has evidence behind it, not a guess. Under the fixed-price contract, the SI bears its own cost of fixing defects; the support extension is yours, unless the delay is the SI's fault and you claim delay damages, which are capped at 0.5 million CU and will be disputed. If the data cannot be split cleanly by member, G is the better choice.

</details>

## What the playbook recommends, and why

**D, then F if the data splits cleanly and the bank accepts the payment file, otherwise G. Never E.** The first job of a sponsor who suspects the status is wrong is to get evidence fast, not to decide on the old evidence. Set status by rules that compare the forecast with tolerance, so "92% executed" cannot pass for green. See [status reporting](../../playbook/project-management/status-reporting.md#define-red-amber-and-green-by-rule).

Go/no-go criteria are agreed weeks ahead and the date is not one of them. A fixed date can be honoured honestly by changing scope or phasing the release, which the [MoSCoW rules](../../playbook/project-management/planning-fixed-scope-and-budget.md#fix-the-date-and-cost-manage-the-scope-moscow) allow, but not by cutting the checks that protect people's pensions. A fixed price moves the SI's cost risk, not your delivery risk; tie payment to accepted, working increments. Contingency covers the risks you named; management reserve covers what nobody foresaw, and the sponsor releases it openly, on the record. Record the decision, the options considered and the reason in the steering group's decision log.

## Debrief questions

1. How would you have known earlier? Which measure in your own status reports would have shown this programme was red months before the test lead spoke up?
2. Do your go/no-go criteria exist in writing before the meeting? Has a go/no-go meeting in your organisation ever said no?
3. In your largest supplier contract, what triggers a payment: a document, a date or accepted working software?
4. When did someone in your organisation last report red early, and what happened to them?
5. If your largest contract had to be split into phases tomorrow, would the contract and your procurement rules allow it?
