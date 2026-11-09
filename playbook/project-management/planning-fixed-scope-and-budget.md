# Planning fixed scope and budget

Some projects are fixed for good reasons: a contract price, a date set in law, a public tender, a budget that lapses at year end. Fixing them is not the lie. The lie is a single number presented as certain, and a plan that hides where the slack went. Estimate as a range from a reference class of similar past projects. Fix no more than two of scope, date and cost, and manage the third openly (usually scope). Hold contingency as a visible line with rules for releasing it, and re-forecast every week.

This page builds on [planning and forecasting](../ways-of-working/planning-and-forecasting.md), which covers throughput, Monte Carlo forecasts and ranges for team work. It adds what changes when a contract, a regulator or a funding body wants a fixed answer.

## Outcomes

Starting points. Tune them to your organisation.

- 100% of estimates shared outside the project are ranges with a confidence level (at least the 50% and 85% values) and name the reference class they came from.
- The approved budget shows three separate lines: the base estimate (50% confidence), contingency up to the agreed confidence level, and the management reserve held by the sponsor.
- Must-have scope is no more than 60% of estimated effort when the baseline is set.
- Every draw on contingency is logged with its reason and a reference to the risks, assumptions, issues and dependencies (RAID) log.
- Across the portfolio, about 85% of projects finish inside their 85% range. Check once a year. Much higher means the ranges are too wide; much lower means they are too narrow.
- Every re-baseline is approved by the steering group and the original baseline stays visible in every later report.

## When fixed is legitimate

| Where the constraint comes from | Example | What is really fixed | What you can still change |
|---|---|---|---|
| A law or a regulator | a reporting format required from a date | the date and the minimum compliant scope | everything beyond compliance, how it is built, temporary manual steps |
| Public procurement | a tender with specified requirements and a ceiling price | the contract as signed | the order of delivery, release slicing, scope through the contract's change mechanism |
| A fixed-price commercial contract | a client pays a set price for an agreed result | price and acceptance criteria | how the work is done; scope through change control |
| A budget year that lapses | money that must be committed by year end | the money available this year | how much scope it buys; each year ends at a usable state |
| An external event | an election, a season, a hardware end-of-support date | the date | scope |

You can fix at most two of scope, date and cost. When a contract fixes all three, quality and risk become the hidden variable: testing gets cut and defects ship. Before signing, say so in writing and propose which of the three can move. After signing, you cannot refuse a contract you are bound by. Write down what the fixed terms cost in risk, record it in the [RAID log](risks-raid-and-stage-gates.md) as a risk owned by the sponsor, and protect the go/no-go criteria, because they are the last place quality is defended.

Even inside a fixed contract, scope is rarely as fixed as it looks. A legal deadline fixes the minimum compliant scope, not every feature someone added to the specification. Separate the two early.

## Public procurement: put the flexibility in the tender

In public procurement you often cannot "manage scope openly" after award, because a large change to a signed contract may need a new procurement. In the EU, Article 72 of Directive 2014/24/EU allows a contract to be changed without a new procurement only in set cases. The main ones:

- the change was provided for in the tender documents in "clear, precise and unequivocal review clauses", which may include options, and does not alter the overall nature of the contract;
- the change is small: below the EU threshold and below 10% of the initial value for service and supply contracts (15% for works), counting all changes together;
- additional work that only the original contractor can do, or a change caused by circumstances a diligent buyer could not foresee, each capped at 50% of the original value and published in the Official Journal;
- the change is not substantial in the sense of the Article.

Other countries have their own rules; ask your procurement lawyer which apply. The practical lesson is the same everywhere: **the flexibility you will need has to be written into the tender.**

- Publish the requirements with MoSCoW priorities, and state that Should and Could haves may be removed without a price change.
- Add options for later releases, extra capacity and extended support, each priced in the bid, so they can be called off without a new procurement.
- Add an exchange clause: the buyer may swap a requirement not yet started for a new one of equal estimated size without a price change.
- Price a rate card for changes, and state the change budget the buyer may draw on.
- Track the cumulative value of changes against the legal limits in the change request log. The project manager and procurement both see it.

A requirement that turns out to be unnecessary is still in the contract until the contract is changed. Plan the procurement with the same care as the delivery.

## Why single-number estimates fail

- **The planning fallacy.** Kahneman and Tversky (1979) showed that people forecast from the details of the plan in front of them and give too little weight to how similar projects actually turned out. Kahneman and Lovallo (1993) later named these the inside view and the outside view. The fix is to start from the outside view.
- **The cone of uncertainty.** Boehm (1981) and later McConnell (2006) described how wide estimates are early. At the initial concept, the final result commonly falls anywhere from about a quarter to four times the estimate. McConnell stresses that the cone narrows only as decisions remove uncertainty. Time passing does not narrow it.
- **Fat tails.** Flyvbjerg and Budzier (2011) studied 1,471 IT projects and found an average cost overrun of 27%. But one project in six had a cost overrun of 200% on average, and a schedule overrun of almost 70%. An average hides the projects that hurt you. Size contingency from the tail, not the mean.

## Estimate with ranges and reference classes

Reference class forecasting, developed by Bent Flyvbjerg from Kahneman and Tversky's work, replaces a guess with the distribution of real outcomes.

1. **Name the reference class.** Pick past projects of the same kind: core system replacements, data migrations of similar volume, integrations with the same supplier. Use your own history first. Use published classes second, such as the HM Treasury guidance on optimism bias for public projects.
2. **Get the distribution.** For each past project, divide the actual cost and duration by the estimate made at the same stage. You now have a spread of ratios.
3. **Make the inside-view estimate.** Build it bottom-up from right-sized items, or from three-point estimates (low, likely, high) per work package. Combine them with a Monte Carlo simulation, as in [planning and forecasting](../ways-of-working/planning-and-forecasting.md#standard).
4. **Adjust with the outside view.** Multiply the inside-view estimate by the reference class ratios at 50% and at 80% or 85%. Apply the ratios to the same kind of number the history recorded. If past estimates were single "most likely" figures, multiply your most likely figure, not your own 85% value, or you count the same uncertainty twice.
5. **Write the assumptions down.** Each one goes into the RAID log with a date by which it will be tested.
6. **Narrow the range by learning, not by negotiating.** Discovery, an alpha, a technical spike or a migration rehearsal on a sample of real data removes uncertainty. Pressure on the number does not.

A worked example, with fictional figures:

| Step | Cost | Duration |
|---|---|---|
| Inside-view estimate | 2.0 million currency units (CU) | 10 months |
| Reference class: 12 past system replacements, ratio of actual to estimate at the same stage | median 1.2, 80th percentile 1.6 | median 1.3, 80th percentile 1.7 |
| Base estimate at 50% confidence | 2.4 million CU | 13 months |
| Value at 80% confidence | 3.2 million CU | 17 months |
| Ask the sponsor to approve | base 2.4 plus contingency 0.8, plus management reserve per policy | plan to 13, commit to 17 |

With no history, start with expert ranges and published classes, and replace them with your own data as soon as you have it. Keep a **project outcome register**: for every project above your threshold, the estimate at each gate and the actual result. After 10 to 20 closed projects it is your best estimating tool. The [lessons learned template](../../templates/project/lessons-learned.md) collects the entries.

## Contingency and management reserve

| Reserve | Covers | Sized from | Held by | Released |
|---|---|---|---|---|
| Contingency | identified risks in the RAID log and the uncertainty in the estimate | the gap between the 50% value and the agreed confidence level (often 80% or 85%) | the project manager within tolerance; the steering group above it | against a named RAID item, logged with the amount |
| Management reserve | the unknown: work inside the agreed scope that nobody foresaw, and events nobody listed | policy, informed by the tail of the reference class | the sponsor or the portfolio | by the sponsor, at a gate or an exception, with a re-baseline |

Neither reserve pays for new scope. When the sponsor adds scope, that is a change: estimate it, fund it with new money or by removing other scope, and approve it through change control. Reserves spent on new scope leave nothing for the risks they were sized for.

Rules:

- **Size exposure in money.** The money exposure of a risk is its probability as a percentage times its impact in money. A 1 to 5 likelihood and impact score is fine for sorting the RAID log, but it cannot be added up or compared with a budget (Cox, 2008). For the largest projects, use a Monte Carlo of the top risks instead of a simple sum.
- **Know whose risk the contingency covers.** Under a fixed-price contract, the supplier's own overrun is the supplier's cost. Your contingency covers your side: your staff, change requests you raise, delays you cause, extending the old system's support, parallel running and business change. Size it from that list, not from the contract value.
- **Hold contingency centrally.** Do not spread it across work packages. Work expands to fill the time available (C. Northcote Parkinson, The Economist, 1955), and contingency spread across tasks gets spent whether the risks happen or not.
- **Show it in every status report:** contingency remaining against the money exposure of the open risks. When the exposure exceeds what is left, the cost status is amber at least. See [status reporting](status-reporting.md#define-red-amber-and-green-by-rule).
- **Size it from evidence.** For Solo, Startup and Scale-up work, 10% to 20% is a starting point. For large or Enterprise projects, size it from the reference class; as the [transition playbook](../strategy/transition-playbook.md#funding-per-phase) says, 10% to 20% is a floor, not a ceiling.
- **Return what is not needed.** Release unused contingency at each gate to the portfolio, so other work can use it.

## Fix the date and cost, manage the scope: MoSCoW

MoSCoW, from the Dynamic Systems Development Method (DSDM), sorts requirements into Must have, Should have, Could have and Won't have this time. DSDM's rule for a fixed date and budget is to fix time, cost and quality and to vary the features.

- **Must have** means the release has no point without it: it is illegal, unsafe or unworkable without it. "Important" is not enough.
- **Must haves take no more than 60% of estimated effort** when the baseline is set. DSDM recommends this level so that Should and Could haves give the plan room.
- **Could haves are the first contingency.** DSDM suggests about 20% of effort. They are dropped first when the forecast slips, without a change request.
- **Won't have this time** is written down, so nobody believes it is coming.
- **Deliver Musts in the early releases,** not at the end. A project that saves its Must haves for the last month has no contingency left.
- **Put the priorities in the contract.** With a supplier, dropping a Could have without a change request works only if the contract says so. See [public procurement](#public-procurement-put-the-flexibility-in-the-tender).

Prioritisation methods for product work are in [roadmaps and prioritisation](../product/roadmaps-and-prioritisation.md).

## Fixed-price contracts and systems integrators

A systems integrator (SI) is a supplier that builds and joins systems for you. A fixed price moves some cost risk to the SI, and the SI prices that risk in. It does not move the delivery risk: if the system is late or wrong, your service is late or wrong. Commercial terms belong to the [suppliers and contracts](../strategy/suppliers-and-contracts.md) page; these are the delivery terms to add.

**Before you sign:**

- Pay for a short discovery or alpha first, on a separate contract, and fix the build price only after it. A fixed price on an unexplored problem is a guess with a penalty clause.
- Buy in lots or call-offs of one or a few releases each, so you can change course or supplier between them.
- Define acceptance as working software in a production-like environment passing agreed tests, including performance and security tests. Never pay milestones for documents alone.
- Agree a change budget and a rate card in the contract, so scope changes are priced the same day, not negotiated for weeks.
- Get access to the SI's repositories, pipeline, test results and defect data from day one, and use one definition of done for staff and supplier engineers.
- Name the key people, with a right to approve replacements.
- Make data migration responsibilities explicit: who maps, who cleanses, who reconciles, who signs off.
- Hold back part of each payment until the end of a warranty period after go-live.
- **Acceptance.** Write the acceptance tests, the acceptance period (for example 10 working days per release) and who signs. Remove clauses that make a release accepted by silence or by first use in production, or make the period long enough to test properly.
- **Warranty.** The warranty period starts at acceptance, covers defects found in production at no charge, and has fix times by severity. Release the held-back money when it ends with no open severity 1 or 2 warranty defects.
- **Exit.** The SI delivers an exit plan within the first months and updates it yearly: code, configuration, documentation, data in a documented format, and a priced period of help to hand over to you or another supplier. See [suppliers and contracts](../strategy/suppliers-and-contracts.md#terms-to-ask-for).
- **Delay damages.** If the contract has liquidated damages for late delivery, know the cap and what triggers them. They compensate for part of a delay; they do not deliver the system, and the SI has priced them in.

**During delivery:**

- Keep your own small expert team (often called the intelligent client): a product manager, an architect and a test lead who can check the SI's claims against the evidence.
- Test independently. The SI's tests show what the SI checked; yours show whether it works for you. See [exploratory and acceptance testing](../quality/exploratory-and-acceptance-testing.md).
- Integrate continuously with your other systems, not in a test phase at the end.
- **Run change requests by rule.** Every change request gets an impact assessment (cost, date, risk) from the SI within an agreed time, such as 5 working days, priced from the rate card. Classify each one: a clarification of the existing requirement (no charge), a change, or a defect. Nobody instructs work verbally; work started without an approved change request is a dispute later.
- Read the change request log weekly. Fast growth in change requests usually means the specification was unclear, and the cost will keep rising.
- Keep one joint RAID log and reconcile the SI's status with your own data before every steering meeting.
- **Watch the SI's margin.** A supplier losing money on a fixed price moves its best people to profitable work and contests every change. Ask for named-people continuity reports, and treat a falling margin as a delivery risk in your log, not only the SI's problem.

### Agile delivery inside a fixed contract

Many contracts are written for a predictive plan: a full specification, a design sign-off, then build, then test. You can still deliver in small, tested releases inside them.

- **Map the contract to the backlog.** Each contract requirement becomes one or more backlog items with its contract reference. A traceability report from the work tracker shows coverage at any time, which is what auditors and contract managers need.
- **Turn milestones into release acceptances.** Agree with the SI and procurement that each milestone is met by an accepted release with a defined set of requirements, rather than by a design document for the whole system.
- **Sign off designs per release.** Where the contract demands design documents, produce and sign them for the next release only, as a by-product of the work.
- **Use the exchange clause** for learning: swap requirements of equal size as users show what they need, and record each swap.
- **Keep the governance the contract requires,** such as the stage reports and the design authority, and feed it from the team's systems, not from a parallel plan.

If the contract has none of these mechanisms and the SI will not agree them as a non-substantial change, run the delivery to the contract and keep the adaptive practices inside the SI's build phase. Do not pretend to run agile delivery that the contract does not allow.

| Pricing model | Fits when | Watch for |
|---|---|---|
| Time and materials | the scope is unknown; short discovery work | effort is paid whether or not anything works |
| Capacity: a fixed price per team per month | long-running delivery with a stable team | needs outcome measures and service levels in the contract |
| Fixed price per release | scope for the next release is well understood | splitting releases so each one is usable |
| Fixed price for the whole project | rarely: small, well-understood work | change requests become the SI's margin |
| Target cost with shared overrun and underrun | large work with uncertain cost | needs open books and an agreed way to measure cost |

## When the project is late

Fred Brooks wrote in 1975 that "adding manpower to a late software project makes it later". New people need time to learn the system and take time from the people who know it. Recovery options, in the order to consider them:

1. **Re-forecast from current throughput,** not from the plan. Report the new range at once if the 85% date has moved more than two weeks.
2. **Cut or defer scope:** Could haves first, then Should haves, then question each Must have against the test above.
3. **Remove waiting:** shared test environments, slow decisions, approvals, dependencies on other teams. Most delay is waiting, not slow work.
4. **Move the date,** with the new date given as a range.
5. **Add people** only early, to work that can be separated cleanly, with their learning time counted in the forecast.
6. **Stop,** if the remaining cost is no longer worth the remaining value. Ignore money already spent.

Never cut testing silently to hold a date. If the sponsor chooses to accept more risk, record the decision and the risk with the sponsor's name on it.

**Re-baselining honestly.** Re-baseline only when the forecast breaks tolerance and the steering group approves a new plan. Keep the original baseline and every later one visible in the status report, with the reason for each change. A re-baseline that turns a report green without anyone deciding anything is a reporting failure.

## Earned value without fiction

Earned value management (EVM), defined for contracts by the standard SAE EIA-748, compares the value of work done with its cost and its plan. Some government contracts require an EVM system that meets the standard; follow the contract.

```
PV  planned value: budgeted cost of the work scheduled to date
EV  earned value: budgeted cost of the work actually accepted to date
AC  actual cost of the work done to date
BAC budget at completion

Cost performance index      CPI = EV / AC
Schedule performance index  SPI = EV / PV
Estimate at completion      EAC = AC + (BAC - EV) / CPI
```

Make it honest:

- **Earn value only for accepted increments:** working software that has passed its acceptance tests. Count nothing for "80% done". This is the 0/100 rule.
- **Use CPI for cost.** Treat a CPI below 1 as the trend to plan for, not a dip that will recover by itself. Show the EAC it implies next to the budget.
- **Use throughput forecasts for dates.** SPI is measured in money, so it drifts back towards 1.0 as the project nears the end whether or not it is late. Report schedule as a date range from [planning and forecasting](../ways-of-working/planning-and-forecasting.md).

## Practice

### Foundation

Solo, Startup and SME. Give every external date as a range with a confidence level. Sort the scope into MoSCoW and keep Must haves below 60% of the effort. Keep 10% to 20% contingency as a visible line, not hidden in each task. For a fixed-price bid, write the assumptions into the quote and price changes against them.

### Standard

Scale-up and Enterprise. A project outcome register used as the reference class for every new estimate. Monte Carlo forecasts for cost and date. Contingency and management reserve held separately with written release rules. Change budgets and rate cards in supplier contracts. Weekly re-forecast; re-baselines approved by the steering group.

### Assured

Regulated and Public sector. Everything in Standard, plus cost estimates with stated confidence levels and a documented risk analysis, as the US GAO Cost Estimating and Assessment Guide describes. Public business cases include optimism bias adjustments where the HM Treasury Green Book applies. Public tenders carry the flexibility the project will need (priorities, options, an exchange clause, a change budget), and the change request log tracks cumulative changes against the procurement rules. An independent cost estimate for the largest projects. EVM when the contract requires it. Every re-baseline recorded with the decision maker and reason, so the history is auditable. See [public sector](../compliance/public-sector.md).

## Cloud, on-premises and air-gapped

Cloud projects need a range for run cost as well as build cost, because consumption varies; link the estimate to [FinOps](../platform/finops.md). On-premises and air-gapped projects need hardware and import lead times in the estimate as fixed dependencies, and contingency for supply delays that more money cannot shorten.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| One number, no range | Give 50% and 85% values and name the reference class. |
| Contingency hidden in every task | Hold it centrally as a visible line with release rules. |
| Everything is a Must have | Must haves at most 60% of effort; test each one. |
| Fixed scope, date and cost, all at once | Fix at most two; record the risk if a contract fixes all three. |
| A fixed price before discovery | Pay for discovery or alpha first; fix price after. |
| Milestones paid for documents | Pay for accepted, working software. |
| Adding people to a late project | Cut scope and remove waiting first. |
| Re-baselining quietly to get back to green | Steering approves every re-baseline; old baselines stay visible. |
| Earned value from percent complete | Earn value only for accepted increments. |
| Management reserve spent on new scope | Fund new scope through change control; keep reserves for risk. |
| Counting on scope flexibility after a public contract is signed | Write priorities, options, an exchange clause and a change budget into the tender. |
| Releases accepted by silence or by first use | An acceptance period with named tests and a named signatory. |
| Risk exposure added up from 1 to 5 scores | Probability as a percentage times impact in money. |

## Templates

- [Project charter](../../templates/project/project-charter.md)
- [RAID log](../../templates/project/raid-log.csv)
- [Lessons learned and outcome register entry](../../templates/project/lessons-learned.md)
- [Business case](../../templates/strategy/business-case.md)

## Sources

- Daniel Kahneman and Amos Tversky, "Intuitive Prediction: Biases and Corrective Procedures", TIMS Studies in Management Science 12, 1979.
- Daniel Kahneman and Dan Lovallo, "Timid Choices and Bold Forecasts: A Cognitive Perspective on Risk Taking", Management Science 39(1), 1993.
- Louis Anthony Cox Jr., "What's Wrong with Risk Matrices?", Risk Analysis 28(2), 2008.
- Directive 2014/24/EU on public procurement, Article 72, modification of contracts during their term: https://eur-lex.europa.eu/eli/dir/2014/24/oj
- Barry W. Boehm, "Software Engineering Economics", Prentice Hall, 1981.
- Steve McConnell, "Software Estimation: Demystifying the Black Art", Microsoft Press, 2006.
- Bent Flyvbjerg and Alexander Budzier, "Why Your IT Project May Be Riskier Than You Think", Harvard Business Review, September 2011: https://papers.ssrn.com/abstract=2229735
- Bent Flyvbjerg, "From Nobel Prize to Project Management: Getting Risks Right", Project Management Journal 37(3), 2006.
- Bent Flyvbjerg and Dan Gardner, "How Big Things Get Done", Currency, 2023.
- HM Treasury, Green Book supplementary guidance: optimism bias: https://www.gov.uk/government/publications/green-book-supplementary-guidance-optimism-bias
- US Government Accountability Office, Cost Estimating and Assessment Guide, GAO-20-195G, 2020: https://www.gao.gov/products/gao-20-195g
- Agile Business Consortium, DSDM Agile Project Framework, MoSCoW prioritisation: https://www.agilebusiness.org/
- Frederick P. Brooks Jr., "The Mythical Man-Month", Addison-Wesley, 1975.
- C. Northcote Parkinson, "Parkinson's Law", The Economist, 19 November 1955.
- SAE International, EIA-748, Earned Value Management Systems.
