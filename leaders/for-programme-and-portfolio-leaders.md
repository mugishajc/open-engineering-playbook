# For programme and portfolio leaders

Run large technology change so that the truth reaches the people who decide while there is still time to act on it. Estimate from what similar programmes actually cost, and fund one stage at a time with stop conditions written in advance. Set status by rules rather than by mood, and keep steering groups for decisions. When you take over a programme in trouble, get your own evidence in the first two weeks. Then put honest options in front of the sponsor: cut scope, move the date, phase the release, or stop.

## When to use this

This page is for programme directors, portfolio leads, heads of project management offices (PMOs), and the sponsors of large technology programmes in government, banks and other large organisations.

- You have been asked to rescue a programme that is late, over budget or reporting green while the teams say otherwise.
- A contract, a regulator or a minister has fixed a date or a price and you must deliver against it honestly.
- Your steering groups listen to reports and rarely decide anything.
- Your PMO collects templates and the teams work around it.
- You are about to sign a large contract with a systems integrator.

The practice lives in [project management](../playbook/project-management/projects-and-products.md): [planning fixed scope and budget](../playbook/project-management/planning-fixed-scope-and-budget.md), [risks, RAID logs and stage gates](../playbook/project-management/risks-raid-and-stage-gates.md), [status reporting](../playbook/project-management/status-reporting.md) and [a modern PMO](../playbook/project-management/modern-pmo.md). Portfolio funding is in [portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md). This page covers the decisions only programme and portfolio leaders can take.

## The first 30 days on a programme in trouble

| Days | Do | Output |
|---|---|---|
| 1 to 5 | Read the charter, the last six status reports, the risks, assumptions, issues and dependencies (RAID) log and the change request log. Read the contract for what it actually says about acceptance, change requests, delay damages, key people, termination and step-in. That is your real room to move. Then talk to the people who do the work: engineers, testers, the supplier's engineers, the people who will use the system. Ask them when they think it will be ready. | a list of gaps between what the reports say and what the people say |
| 6 to 10 | Get the raw data: throughput, accepted items, scope growth, defect inflow and outflow, test pass rates (not "executed"), migration reconciliation results, actual cost. Re-forecast from it, and check the result against a reference class of similar programmes. | an independent forecast range at 50% and 85% confidence |
| 11 to 15 | Freeze new scope. Sort what is left into Must, Should and Could. Fix the things that make everyone wait: test environments, slow decisions, unclear ownership. Meet the supplier's accountable lead to agree a joint recovery: a supplier pushed into a claims battle stops helping. | a Must have list with its effort; the top three blockers removed or owned |
| 16 to 20 | Write an options paper: cut scope, move the date, release in phases, stop. For each, the forecast range, the cost, the risks, what users get when, and whether the contract and procurement rules allow it. | options with a recommendation |
| 21 to 30 | Take it to the sponsor and steering group for a decision. Re-baseline openly, keep the old baseline visible, reset the status rules and the reporting rhythm. Tell the teams and the supplier what was decided and why. | a recorded decision, a new baseline, new status rules |

Do not add people in the first month unless the work can be separated cleanly. "Adding manpower to a late software project makes it later" (Brooks, 1975).

## Questions that find the real status

Ask these in the first week and at every gate. Ask for the evidence, not the answer.

1. How many Must have items are accepted by the business owner today, out of how many?
2. What share of end-to-end tests passed on the last run? Not executed: passed.
3. Are new defects arriving faster than they are being fixed? Show me the last 6 weeks.
4. How much scope has been added since the baseline? Show me the burn-up with the scope line.
5. Did the last migration rehearsal reconcile? To what threshold, and who checked it?
6. When did we last deploy to a production-like environment, and how long did it take?
7. What does our forecast say at 85% confidence, and what is it based on?
8. Which assumptions in the plan have not yet been tested?
9. What would the supplier's engineers say if I asked them the date privately?
10. Is the supplier making or losing money on this contract, and has it moved any named people off it?
11. Is the cutover rehearsed, timed, with a point of no return and a tested rollback?
12. If we were starting today, knowing what we know, would we start this programme?

## Fixed dates and prices without lying

Some dates and prices are fixed for good reasons: a law, a tender, a contract, a budget year. Accept the constraint and say plainly what it costs.

- Fix at most two of scope, date and cost. When all three are fixed, quality becomes the hidden variable; record that as a risk with the sponsor's name on it.
- Present every date and cost as a range with a confidence level and the reference class behind it.
- Hold contingency as a visible line released against named risks, and a management reserve held by the sponsor for the unforeseen. Neither pays for new scope; new scope is a funded change.
- In public procurement, the flexibility you will need (priorities, options, an exchange clause, a change budget) has to be in the tender, because a large change after award can need a new procurement. See [public procurement](../playbook/project-management/planning-fixed-scope-and-budget.md#public-procurement-put-the-flexibility-in-the-tender).
- Keep Must have scope to no more than 60% of effort, so the plan has room. See [planning fixed scope and budget](../playbook/project-management/planning-fixed-scope-and-budget.md#fix-the-date-and-cost-manage-the-scope-moscow).

## Sponsors and steering groups

A programme has one sponsor who is accountable for the outcome and the money, and who chairs a steering group of three to six people. The steering group decides; it does not receive briefings.

- Delegate tolerances so the group sees exceptions, not everything.
- Put decisions on the agenda, with options, a recommendation and a deadline.
- Keep a decision log. If three meetings in a row decide nothing, change the meeting.
- Thank the first person who reports red. People report what the sponsor rewards.
- Do not accept green for anything not yet tested. No current evidence means no green.
- Take commercial decisions in a client-only session when the systems integrator sits on the group.

Details in [status reporting](../playbook/project-management/status-reporting.md#steering-groups-that-decide).

## Systems integrators

A fixed price moves some cost risk to the systems integrator (SI). It never moves the delivery risk: a late system is your late service.

| Before signing | During delivery |
|---|---|
| Pay for discovery or alpha separately; fix the build price after it | Keep your own product manager, architect and test lead to check claims |
| Buy in lots of one or a few releases | Test independently, and integrate continuously, not at the end |
| Pay for accepted working software, not documents | Read the change request log every week |
| A change budget and a rate card in the contract | Reconcile the SI's status with your own data before every steering meeting |
| Access to the SI's repositories, pipeline and defect data from day one | One joint RAID log; one definition of done |
| Named key people; explicit migration duties; retention until warranty ends | Plan the exit and knowledge transfer from the start |
| An acceptance period with named tests; no acceptance by silence or first use | Every change request assessed and classified before work starts |

See [planning fixed scope and budget](../playbook/project-management/planning-fixed-scope-and-budget.md#fixed-price-contracts-and-systems-integrators) and [suppliers and contracts](../playbook/strategy/suppliers-and-contracts.md).

## Programmes alongside agile teams and continuous delivery

- Fund persistent product teams through the portfolio. Run the programme as a time-boxed claim on their capacity plus the extra money it needs.
- Let teams plan their own work and forecast from their throughput. Build the programme plan from their forecasts, not over them.
- Deploy to production early and dark; make go-live a release decision. Keep a formal cutover only for one-way steps such as data migration.
- Report from the teams' systems. The PMO reads the data; teams do not retype it.

See [projects and products](../playbook/project-management/projects-and-products.md).

## Go-live and benefits

- Go/no-go criteria are agreed at least 4 weeks ahead and the date is not one of them. The cutover is rehearsed at least twice, timed, with a point of no return and a tested rollback before it. See [cutover and rollback](../playbook/project-management/risks-raid-and-stage-gates.md#cutover-and-rollback).
- Benefits arrive after the programme team has gone. Name a business owner for each benefit, measure the baseline before go-live, and chair the 6 and 12 month reviews yourself. See [benefits after go-live](../playbook/project-management/projects-and-products.md#benefits-after-go-live).

## Stopping a programme

Stopping is a decision, not a failure. At every gate, decide on remaining cost and remaining value only, and honour the stop conditions written in the charter. When you stop: release the teams within two weeks, close or transfer the RAID items, record what was learned, and add the result to the outcome register so the next estimate is better. See [how to stop work](../playbook/strategy/portfolio-and-capacity.md#how-to-stop-work).

## Reporting to the board

Major programmes appear on the board scorecard as forecast cost to complete against the approved budget and the forecast date range at 85% confidence against the plan. Use the same numbers and colours as the programme report. Tell the CEO within 24 hours when a programme goes outside tolerance: forecast cost more than 10% over the approved budget, or the 85% date past the plan. These are the board page's starting thresholds; see [what reaches the board, and how fast](board-and-executive-reporting.md#what-reaches-the-board-and-how-fast). The board keeps the approval of each stage and the decision to continue, rescope or stop at a gate; see [what the board decides](board-and-executive-reporting.md#what-the-board-decides) and [investment decisions under uncertainty](decision-making.md#investment-decisions-under-uncertainty).

## Common mistakes

| Mistake | Fix |
|---|---|
| Trusting the status report on a programme you have just inherited | Get raw data and talk to the people doing the work in week one. |
| Promising a new date before you have evidence | Give a date for the forecast, not for the programme. |
| Adding people to recover a late programme | Cut scope and remove waiting first. |
| Single-number estimates for the business case | Ranges from a reference class, with confidence levels. |
| Steering groups that only listen | Decisions on the agenda; a decision log. |
| The go-live date treated as a go/no-go criterion | Criteria agreed 4 weeks ahead; the date is not one of them. |
| Accepting a systems integrator's green status | Reconcile with your own data and independent tests. |
| Re-baselining quietly | Steering approves every re-baseline; old baselines stay visible. |
| A PMO that collects templates | Run it as a service measured by time given back and forecast calibration. |
| Never stopping anything | Stop conditions in every charter; at least one rescope or stop a year, or a reason why not. |
| Signing a public contract with no room to change | Priorities, options, an exchange clause and a change budget in the tender. |
| Closing the programme at go-live and calling it a success | Benefit owners, baselines and reviews at 6 and 12 months. |

## Templates

- [Project charter](../templates/project/project-charter.md)
- [RAID log](../templates/project/raid-log.csv)
- [Status report](../templates/project/status-report.md)
- [Stage gate checklist](../templates/project/stage-gate-checklist.md)
- [Lessons learned](../templates/project/lessons-learned.md)
- [Pre-mortem](../templates/leaders/pre-mortem.md)
- [Board engineering report](../templates/leaders/board-engineering-report.md)
- Practise with the decision game [the red project before go-live](../exercises/decision-games/red-project-before-go-live.md).

## Sources

- Bent Flyvbjerg and Dan Gardner, "How Big Things Get Done", Currency, 2023.
- Bent Flyvbjerg and Alexander Budzier, "Why Your IT Project May Be Riskier Than You Think", Harvard Business Review, September 2011: https://papers.ssrn.com/abstract=2229735
- Daniel Kahneman and Amos Tversky, "Intuitive Prediction: Biases and Corrective Procedures", TIMS Studies in Management Science 12, 1979.
- Frederick P. Brooks Jr., "The Mythical Man-Month", Addison-Wesley, 1975.
- AXELOS (PeopleCert), Managing Successful Projects with PRINCE2, 7th edition, 2023.
- Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK Guide), 8th edition, 2025: https://www.pmi.org/standards/pmbok
- AXELOS (PeopleCert), Managing Successful Programmes (MSP), 5th edition, 2020.
- Directive 2014/24/EU on public procurement, Article 72, modification of contracts during their term: https://eur-lex.europa.eu/eli/dir/2014/24/oj
- UK Government Functional Standard GovS 002, Project delivery: https://www.gov.uk/government/publications/project-delivery-functional-standard
- US Government Accountability Office, Cost Estimating and Assessment Guide, GAO-20-195G, 2020: https://www.gao.gov/products/gao-20-195g
