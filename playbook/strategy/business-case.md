# Business case for engineering investment

Justify engineering work in the units finance and boards already use: money per year, payback period and risk. Count four kinds of benefit (toil removed, incident cost avoided, risk reduced and delay avoided), then show a conservative case that still pays back. Keep each formula simple enough that a finance partner can check it in ten minutes.

## Outcomes

Starting points. Tune them to your organisation.

- Every investment above an agreed threshold (for example 3 engineer-months) has a one to two page business case before work starts.
- Every number in the case has a source: a system report, a time study, an invoice, or a stated assumption.
- The case shows a low, expected and high scenario. The low scenario is the one you commit to.
- Benefits are checked 6 and 12 months after delivery. At least 70% of cases deliver their low scenario or better.

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

### 2. Incident cost avoided

```
cost per incident = duration in hours x (revenue lost per hour + responders x hourly cost) + penalties
annual cost       = incidents per year x cost per incident
```

Illustrative: 12 incidents a year, each lasting 3 hours. Revenue lost is 2,000 CU per hour. Four responders at 60 CU per hour add 240 CU per hour. Cost per incident is 3 x 2,240 = 6,720 CU. Annual cost is 80,640 CU. Better observability and rollback cut average recovery to 1 hour, so the new annual cost is 12 x 2,240 = 26,880 CU. The benefit is 53,760 CU a year.

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

Ask product and finance to agree the value per week. If they will not, leave this benefit out rather than invent it.

### Option value

Some investments create choices for later. Value them as expected savings.

```
option value = probability you will need the option x cost saved if you do - extra cost now
```

Illustrative: using open standards for container images and telemetry costs 20,000 CU more now. If there is a 30% chance of changing hosting provider in three years, and open standards save 200,000 CU on that move, the expected value is 0.3 x 200,000 - 20,000 = 40,000 CU.

## Putting it together

Illustrative totals for the fictional organisation.

| Line | Expected (CU per year) |
|---|---|
| Toil removed | 66,240 |
| Incident cost avoided | 53,760 |
| Risk reduced | 40,000 |
| Delay avoided | 120,000 |
| **Total annual benefit** | **280,000** |
| Annual running cost of the new tooling | 30,000 |
| **Net annual benefit** | **250,000** |

One-time investment: 150,000 CU (two engineers for six months plus tooling).

```
payback period (years) = one-time investment / net annual benefit
                       = 150,000 / 250,000 = 0.6 years (about 7 months)
three-year net value   = 3 x 250,000 - 150,000 = 600,000 CU (undiscounted)
```

**Low scenario.** Halve every benefit: 140,000 CU benefit, 110,000 CU net, payback in about 1.4 years. If the low scenario still pays back within the period your finance team accepts, commit to it. If it does not, cut scope.

Use your organisation's discount rate if finance asks for net present value. Keep the undiscounted figures alongside so engineers can follow the numbers.

## Practice

### Foundation

Solo and Startup. One page: problem, the two largest benefits with their formulas, cost, payback. Use the [business case template](../../templates/strategy/business-case.md). Toil and delay are usually enough.

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
| Counting saved hours as cash | Say what the hours will be used for. Finance only counts cash if headcount or spend falls. |
| One optimistic number | Show low, expected and high. Commit to low. |
| Invented probabilities | Use the risk register or a named estimator. Show the range. |
| Never checking afterwards | Review realised benefits at 6 and 12 months. |

## Templates

- [Business case](../../templates/strategy/business-case.md)
- [Risk register](../../templates/strategy/risk-register.csv)

## Sources

- Google, "Site Reliability Engineering", chapter "Eliminating Toil": https://sre.google/sre-book/eliminating-toil/
- Donald G. Reinertsen, "The Principles of Product Development Flow", Celeritas Publishing, 2009.
- HM Treasury, "The Green Book": https://www.gov.uk/government/publications/the-green-book-appraisal-and-evaluation-in-central-government
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
