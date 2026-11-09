# Business case for engineering investment

Justify engineering work in the units finance and boards already use: money per year, payback period and risk. Count four kinds of benefit (toil removed, incident cost avoided, risk reduced and delay avoided), keep cash apart from released capacity, and compute payback on cash only. Show a conservative case, with lower benefits and higher costs, that still pays back, using formulas a finance partner can check in ten minutes.

## Outcomes

Starting points. Tune them to your organisation.

- Every investment above an agreed threshold (for example 3 engineer-months) has a one to two page business case before work starts.
- Every number in the case has a source: a system report, a time study, an invoice, or a stated assumption.
- The case shows a low, expected and high scenario. The low scenario is the one you commit to.
- Payback is computed on cash benefits only. Released capacity is shown separately, with what it will be used for.
- Benefits are checked 6 and 12 months after delivery. At least 70% of cases deliver their low scenario or better. Each benefit has a business owner, a baseline measured before go-live and its dis-benefits recorded; see [benefits after go-live](../project-management/projects-and-products.md#benefits-after-go-live).

## The four benefit types

All figures below are **illustrative**. They describe a fictional organisation. Use your own data. Money is shown in generic currency units (CU).

### 1. Toil removed

Toil is manual, repetitive work that scales with the size of the service and adds no lasting value. The Google SRE book defines it in detail.

```
annual toil cost = hours per week x loaded hourly cost x working weeks per year
benefit          = annual toil cost x share the investment removes
```

Illustrative: 6 engineers each spend 5 hours a week on manual releases. That is 30 hours. At 60 CU per hour over 46 working weeks, toil costs 30 x 60 x 46 = 82,800 CU a year. Release automation removes 80%, so the benefit is 66,240 CU a year.

Measure toil with a two-week time study or ticket labels. Do not guess.

Removed toil is **capacity, not cash**. It becomes cash only if headcount, contractor or overtime spend falls. Otherwise show it as hours released and say what they will be used for.

### 2. Incident cost avoided

```
lost margin per hour = revenue lost per hour (not deferred) x contribution margin
cost per incident    = duration in hours x (lost margin per hour + responders x hourly cost) + penalties
annual cost          = incidents per year x cost per incident
```

Most revenue during an outage is deferred, not lost: customers come back and buy later. Count only the revenue that does not come back, and only its contribution margin. Ask finance for both figures.

Illustrative: 12 incidents a year, each lasting 3 hours. Lost margin is 800 CU per hour. Four responders at 60 CU per hour add 240 CU per hour. Cost per incident is 3 x 1,040 = 3,120 CU. Annual cost is 37,440 CU. Better observability and rollback cut average recovery to 1 hour, so the new annual cost is 12 x 1,040 = 12,480 CU. The benefit is 24,960 CU a year: 19,200 CU of margin (cash) and 5,760 CU of responder time (capacity).

Take incident counts and durations from your [incident records](../reliability/incident-management.md). Include contractual service credits and regulatory penalties only where a contract or law states them.

### 3. Risk reduced

```
annual loss expectancy (ALE) = probability per year x impact
benefit                      = ALE before - ALE after
```

Illustrative: the chance of losing a day of customer data is estimated at 5% a year, with an impact of 1,000,000 CU. ALE is 50,000 CU. Tested, automated restores cut the probability to 1%. New ALE is 10,000 CU. The benefit is 40,000 CU a year.

Probabilities are estimates. Show who made them and how, for example the risk committee's register. See [backup and recovery](../reliability/backup-and-recovery.md).

### 4. Delay avoided (cost of delay)

Cost of delay is the value lost for each week a change is not in users' hands. Donald Reinertsen describes it in "The Principles of Product Development Flow" (2009).

```
cost of delay = value per week of the change x weeks of delay removed x changes per year
```

Illustrative: four major features a year are each worth 10,000 CU a week once live. The current release process adds three weeks to each. Removing that delay is worth 4 x 3 x 10,000 = 120,000 CU a year.

Ask product and finance to agree the value per week, as margin rather than revenue. If they will not, leave this benefit out rather than invent it.

### Option value

Some investments create choices for later. Value them as expected savings.

```
option value = probability you will need the option x cost saved if you do - extra cost now
```

Illustrative: using open standards for container images and telemetry costs 20,000 CU more now. If there is a 30% chance of changing hosting provider in three years, and open standards save 200,000 CU on that move, the expected value is 0.3 x 200,000 - 20,000 = 40,000 CU.

## Putting it together

Illustrative totals for the fictional organisation. Cash and capacity are kept apart.

| Line | Type | Expected (CU per year) |
|---|---|---|
| Incident margin avoided | cash | 19,200 |
| Risk reduced | cash (expected value, not certain in any one year) | 40,000 |
| Delay avoided | cash | 120,000 |
| **Cash benefit** | | **179,200** |
| Annual running cost of the new tooling | cash | -30,000 |
| **Net annual cash benefit** | | **149,200** |
| Toil removed | capacity, not cash | 66,240 (about 1,100 hours) |
| Incident responder time | capacity, not cash | 5,760 |
| **Capacity released** | | **72,000**, used for the reliability backlog |

One-time investment: 150,000 CU (two engineers for six months plus tooling).

```
payback period (years) = one-time investment / net annual cash benefit
                       = 150,000 / 149,200 = about 1 year
three-year net cash    = 3 x 149,200 - 150,000 = 297,600 CU (undiscounted)
```

**Low scenario.** Halve every benefit and raise the one-time cost by 50%, because cost overrun is the most common way IT investments fail. Cash benefit 89,600 CU, net 59,600 CU a year, one-time cost 225,000 CU, payback in about 3.8 years. If finance accepts 3 years, this case does not pass as written: cut scope or phase it, and run the numbers again. If the low scenario pays back within the period your finance team accepts, commit to it.

For large programmes, do not trust a single estimate. Check the cost and duration against the outcomes of similar past projects, inside or outside your organisation (reference class forecasting). Flyvbjerg and Budzier found that IT project cost overruns have a fat tail: a small share overrun by very large amounts.

Use your organisation's discount rate if finance asks for net present value. Keep the undiscounted figures alongside so engineers can follow the numbers. Show capital and operating costs separately where finance capitalises development cost (see [technology budget and cost](technology-budget-and-cost.md)).

## Practice

### Foundation

Solo and Startup. One page: problem, the two largest benefits with their formulas, cost, payback. Use the [business case template](../../templates/strategy/business-case.md). Delay and toil are usually enough; show toil as capacity unless spend falls.

### Standard

Scale-up and Enterprise. All four benefit types where they apply, three scenarios, a finance partner reviews the numbers before the decision meeting. Link the case to the [technical strategy](technical-strategy.md) action it supports. Review the realised benefit at 6 and 12 months against [metrics](../measurement/metrics.md).

### Assured

Regulated and Public sector. Everything in Standard, plus:

- Link risk figures to the official risk register and name the risk owner.
- Show regulatory drivers separately from discretionary benefits. A mandatory change needs a cost case, not a benefit case.
- Public sector: follow the national appraisal method. In the UK that is HM Treasury's Green Book. Match spending to budget years and show capital and operating costs separately.
- Keep the approved version, the approver and the date as a record.

## Cloud, on-premises and air-gapped

Cloud costs are mostly operating spending and scale with use. On-premises and air-gapped costs are mostly capital spending with depreciation, plus floor space, power, hardware refresh and staff. Compare them over the same 3 to 5 year period with the [build, buy or adopt](build-buy-adopt.md) total cost of ownership method. Air-gapped sites add the cost of moving updates across the gap: count the hours per month.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Engineers will be happier" as the only benefit | Measure the toil, delay or incident cost behind the complaint. |
| Counting saved hours as cash | Show them as capacity released, with what the hours will be used for. Count them as cash only if headcount or spend falls. |
| Counting revenue during an outage as lost | Count only revenue that does not come back, times contribution margin. |
| A low scenario that cuts benefits but keeps costs fixed | Raise the one-time cost too. Check large programmes against similar past projects. |
| One optimistic number | Show low, expected and high. Commit to low. |
| Invented probabilities | Use the risk register or a named estimator. Show the range. |
| Never checking afterwards | Review realised benefits at 6 and 12 months. |

## Templates

- [Business case](../../templates/strategy/business-case.md)
- [Risk register](../../templates/strategy/risk-register.csv)

## Sources

- Bent Flyvbjerg and Alexander Budzier, "Why Your IT Project May Be Riskier Than You Think", Harvard Business Review, September 2011: https://papers.ssrn.com/abstract=2229735
- Google, "Site Reliability Engineering", chapter "Eliminating Toil": https://sre.google/sre-book/eliminating-toil/
- Donald G. Reinertsen, "The Principles of Product Development Flow", Celeritas Publishing, 2009.
- HM Treasury, "The Green Book": https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
