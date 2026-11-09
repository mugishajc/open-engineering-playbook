# Technology budget and cost

Build the technology budget from parts a finance team can check: the run baseline, persistent funded teams, and investment bets released one phase at a time. Agree with finance how development cost is capitalised before you change how teams plan or record time, because a planning change can become an audit finding. Then show each business unit what its services cost, per unit it recognises, so cost conversations are about demand and value rather than a single large number.

## Outcomes

Starting points. Tune them to your organisation.

- At least 90% of technology spend is allocated to a named service or business unit. The unallocated "shared" line is under 10%.
- A written capitalisation policy for software development exists, agreed with finance and reviewed by the external auditor, and is checked before any change to planning or time recording.
- Run, funded teams and investment bets are reported against budget each quarter. Any variance above 5% has a written reason.
- Unit cost (for example cost per customer, per transaction or per case) is reported for the five services with the largest spend, with a 4-quarter trend.

## How the budget is built

| Part | What it covers | How to set it | Owner |
|---|---|---|---|
| Run baseline | licences, hosting, support contracts, hardware refresh, the share of team time spent keeping services running | last year's actual, adjusted for contract changes, volume and end-of-life work | CTO or CIO with finance |
| Funded teams | persistent product and platform teams at loaded cost | number of teams x loaded team cost; changed at the annual cycle or by [decision rights](../operating-model/decision-rights.md#money-people-and-contracts) row 22 | heads of engineering |
| Investment bets | transitions, new products, large upgrades | one [business case](business-case.md) each; money released per phase, as in the [transition playbook](transition-playbook.md#funding-per-phase) | the sponsor of each bet |
| Contingency | overruns on bets, unplanned regulatory work | held centrally, released at a gate | CTO and CFO |

```
loaded team cost per year = people x loaded annual cost per person
                          + tools and licences per person x people
                          + the team's share of platform and shared service cost
```

Map the three parts to the run, grow and transform mix in [portfolio and capacity](portfolio-and-capacity.md). Funded teams usually split across all three; label their work so the split can be reported.

## Capital and operating cost

Ask finance for the rules that apply to you. The usual pattern:

| Spend | Usual treatment |
|---|---|
| Servers, network, data centre fit-out, perpetual licences | capital, depreciated over the asset's useful life |
| Cloud consumption, SaaS subscriptions, support contracts | operating |
| Configuration and customisation of SaaS | often operating under IFRS (see the IFRS Interpretations Committee agenda decision of April 2021); check with finance |
| Building software you own | capital when the accounting criteria below are met, operating otherwise |

Moving from on-premises to cloud moves cost from capital to operating, and the reverse for repatriation. Show both views in the business case, because the budget holder and the profit line see different numbers.

## Capitalising development cost

Many organisations capitalise part of the cost of building software. Engineering produces the evidence, so engineering has to know the rules.

- **IFRS (IAS 38).** Research cost is an expense. Development cost is capitalised only when all six criteria are met, including technical feasibility, the intention and ability to complete and use the software, probable future economic benefits, and the ability to measure the cost reliably.
- **US GAAP, internal-use software (ASC 350-40).** ASU 2025-06 removes the old project-stage model. Capitalisation starts when management has authorised and committed funding and it is probable the software will be completed and used as intended. It applies to annual periods beginning after 15 December 2027, and early adoption is allowed. Software sold to customers follows a different subtopic (ASC 985-20).

What engineering does:

1. Label every work item by product and as capitalisable or not, using definitions finance has written and agreed.
2. Record team time per product from rosters or a light weekly allocation. Hours per task are rarely needed.
3. Change the planning method and the evidence on the same date. Do not leave a quarter without records, for example when you stop estimating in story points (see [agile in the AI era](../ways-of-working/agile-in-the-ai-era.md#agree-it-with-finance-before-you-stop-estimating)).
4. Get the external auditor's view before the change, not after.

Capitalised cost reaches the profit and loss account later, as amortisation over the software's useful life. A rising capitalised share makes this year's profit look better and raises future cost. Report both, so nobody is surprised in year three.

## Cost transparency

- **Allocate everything.** People, licences, hosting and suppliers are allocated to services, and services to business units, using a published taxonomy. The TBM Council taxonomy is a common starting point.
- **Showback first.** Each business unit sees what its services cost and why. Move to chargeback only when units can change how much they consume; charging for what they cannot control only starts arguments.
- **Unit cost.** Divide service cost by a unit the business recognises: per customer, per order, per claim, per citizen transaction. Report the trend.
- **Shared services.** Platform and shared services publish their service levels and cost per unit, so consumers see what they pay for. See [developer platform](../platform/developer-platform.md).

## Explaining cost to a CFO

| The CFO asks | Answer with |
|---|---|
| Why does technology cost more every year? | The run trend split into volume, price (contract increases), new services and debt. Show what was retired. |
| What do we get for it? | Unit cost and its trend, and the outcomes of the investment bets against their business cases |
| What happens if we cut 10%? | Two or three options with the services, risks and dates each one affects. Never a flat cut across teams. |
| How much of this is fixed? | Funded teams and contracts are fixed in the year; consumption and contractors are variable. Give the split. |

## Practice

### Foundation

Solo and Startup. One spreadsheet: people, tools, hosting, by month, against plan. Tag cloud resources by service. Ask your accountant once a year whether any development cost should be capitalised, and label work items if the answer is yes.

### Standard

Scale-up and Enterprise. The four-part budget above. A written capitalisation policy agreed with finance. Showback to business units every quarter. Unit cost for the largest services. Monthly cost review in the [operating rhythm](../../leaders/operating-rhythm.md).

### Assured

Regulated and Public sector. Everything in Standard, plus capital and operating cost shown separately in every business case, approval records for the budget and its changes, and the allocation method documented for audit. Public bodies follow their budget rules, which often separate capital and resource budgets and limit moving money between them or between years. See [public sector](../compliance/public-sector.md).

## Cloud, on-premises and air-gapped

Cloud cost is mostly operating and varies with use: link the budget to [FinOps](../platform/finops.md) and treat commitment discounts (reserved capacity, savings plans) as contracts that need finance approval. On-premises and air-gapped estates are mostly capital, with hardware refresh every few years, floor space, power and staff. Plan the refresh in the run baseline, not as a surprise bet.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| One technology cost number for the whole business | Allocate to services and business units; report unit cost. |
| Changing planning or time recording without finance | Agree capitalisation evidence first, with the auditor's view. |
| Chargeback for costs units cannot control | Showback first; chargeback only for consumption units can change. |
| Flat percentage cuts across all teams | Options with named services and risks. |
| Capitalised share rising quietly | Report capitalised and expensed cost, and future amortisation, together. |

## Templates

- [Business case](../../templates/strategy/business-case.md)
- [Application portfolio](../../templates/leaders/application-portfolio.csv)
- [Capability map](../../templates/leaders/capability-map.csv)

## Sources

- IFRS Foundation, IAS 38 Intangible Assets: https://www.ifrs.org/issued-standards/list-of-standards/ias-38-intangible-assets/
- IFRS Interpretations Committee, agenda decision "Configuration or Customisation Costs in a Cloud Computing Arrangement (IAS 38)", April 2021, as presented to the IASB: https://www.ifrs.org/content/dam/ifrs/meetings/2021/april/iasb/ap12a-maintenance-and-consistent-application.pdf
- FASB, ASU 2025-06, Intangibles, Goodwill and Other, Internal-Use Software (Subtopic 350-40), September 2025: https://www.fasb.org
- TBM Council, TBM Taxonomy: https://www.tbmcouncil.org/learn-tbm/tbm-taxonomy/
- FinOps Foundation, FinOps Framework: https://www.finops.org/framework/
