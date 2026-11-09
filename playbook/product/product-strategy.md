# Product strategy

The problem: the roadmap is a list of requests from whoever asked loudest, and nobody can say which few results the product exists to change this year. Write the product strategy on one page: who it serves, which problem it solves, why your approach can win, what you will not do, and 2 to 4 outcomes that show it is working. When code is cheap to produce, focus is the scarce resource, so a strategy that says no is worth more than a list of ambitions.

## Outcomes

Starting targets. Tune them after two quarterly reviews.

| Signal | Starting target |
|---|---|
| Product strategy fits on one page and has been reviewed this quarter | Yes, for every product with its own team |
| Team objectives that trace to a strategy outcome | At least 80% |
| Strategy states at least one thing the product will not do | Yes, and the list is used to decline requests |
| Strategy outcomes with a baseline, a target and a data source | 100% |
| Product leads who can state the target user and the main problem in two sentences | Every product lead, checked at the quarterly review |
| Features retired or simplified each year | More than zero (a product that only grows is not being managed) |

## What a product strategy contains

The [technical strategy](../strategy/technical-strategy.md) uses Rumelt's kernel: diagnosis, guiding policy, coherent actions. A product strategy uses the same kernel, applied to users and markets.

| Part | Question it answers | Weak version | Strong version (illustrative) |
|---|---|---|---|
| Vision | What will be different for users in 3 to 5 years? | "The leading platform for small business" | "A shop owner with no accountant closes the month in under an hour" |
| Target users | Who exactly, and who not? | "SMEs" | "Shops with 1 to 10 staff that sell in person and by phone; not chains with their own finance team" |
| Problem or job | What progress are they trying to make? | "They need better tools" | "Know by Friday whether they can pay suppliers next week" |
| Insight | What do we know that others have not acted on? | none, or a technology | "Most owners already record sales on their phone; the gap is turning that record into a cash view" |
| Guiding choices | How will we win, and what will we refuse? | a list of features | "Mobile first, works offline, no setup over 10 minutes. We will not build payroll." |
| Business model | Who pays, for what, and what does it cost to serve one more user? | "Freemium", or blank | "Shops pay a monthly fee per location; the free plan covers one till; cost to serve stays under 15% of the fee". See [pricing and packaging](pricing-and-packaging.md). In public services: the funding source and cost per transaction |
| Outcomes | Which 2 to 4 numbers show it is working? | features shipped, users registered | "Weekly active shops retained at week 8 rises from 35% to 50%" |
| Bets | Which few problems will teams take on next? | the full backlog | 3 to 5 opportunities, each owned by a team, see [roadmaps and prioritisation](roadmaps-and-prioritisation.md) |

The "problem or job" row uses jobs to be done (Christensen and colleagues, 2016): people "hire" a product to make progress in a particular situation. Describing the job, not the feature, keeps the strategy stable while solutions change.

Marty Cagan's *Empowered* (2020) frames product strategy as four activities: focus (choose few problems), insights (from data, users, technology and the industry), action (give teams problems to solve, not features to build) and management (follow up on progress). Use that as the test of whether your one page is used, not only written.

## Practice

### Foundation

- **One page, written by the founder or product lead** with the [product strategy on a page](../../templates/product/product-strategy-on-a-page.md). If it takes more than a page, the choices have not been made.
- **Name who it is not for.** Most early products fail by serving everyone a little. The "not for" line is what lets you say no to a paying customer whose request pulls the product sideways.
- **Pick one primary outcome** that shows users get value (for example retained active users at week 8, or tasks completed per week) and 1 to 3 guardrails (support contacts, refunds, complaints). See [product metrics and experiments](product-metrics-and-experiments.md).
- **Ground it in evidence from users.** Each claim in the "problem" and "insight" rows links to interview notes, support data or usage data. See [product discovery](product-discovery.md).
- **Review it every quarter** in 60 minutes: what did we learn, which outcome moved, what do we stop?

### Standard

- **A strategy per product area, under one company strategy.** Each product lead's page names the company outcome it serves. Conflicts between pages are resolved by the head of product, in writing.
- **Teams get problems, not features.** Each team receives 1 to 3 outcomes per quarter from the strategy and decides how to reach them, the model described in [product partnership](../ways-of-working/product-partnership.md). Write them as objectives and key results if you use OKRs, following the rules in the [strategy toolkit](../../leaders/strategy-toolkit.md#okrs-done-properly).
- **Strategy and capacity agree.** The bets fit inside the feature share of the capacity split (a starting point of 60% features, 20% reliability, 15% debt, 5% platform from [portfolio and capacity](../strategy/portfolio-and-capacity.md)). A strategy that needs 120% of the feature share is a wish list.
- **Product and technical strategy are read together.** Every product bet that needs platform or architecture work names the matching action in the technical strategy. The CTO and head of product sign both.
- **Retire on purpose.** Twice a year, list features with low use and high carrying cost (support contacts, defects, security patches, code that slows other change), and remove or simplify at least one a year. This is the same retirement review as in [for product leaders](../../leaders/for-product-leaders.md#a-product-leaders-rhythm).
- **Business products have two customers.** Write the strategy for the organisation that buys and the people who use it every day. Name the segment you sell to (size, sector, region) and the one you do not, so sales and product decline the same deals.
- **Internal products need a strategy too.** A developer platform, a data platform or a staff case-management system has users who usually cannot choose another provider. Write the same page: who it serves, which problem, what it will not do, and outcomes such as time saved for the teams that use it or adoption where teams have a choice. See [developer platform](../platform/developer-platform.md#platform-as-a-product).

### Assured

- **Legal duties are part of the strategy, not a later check.** Accessibility, data protection, records and consumer protection duties appear as constraints in the guiding choices. See [regulated industries](../compliance/regulated-industries.md).
- **Public services serve everyone eligible.** A citizen cannot choose another provider for a tax return or a licence, and a regulated customer often cannot switch easily. The strategy cannot pick only the profitable or the digitally confident users. Write who must be served, including people who need an assisted channel, and measure the outcome for them separately. See [public sector](../compliance/public-sector.md).
- **Policy intent is the vision.** In government the "why" comes from legislation or a ministerial decision. The product strategy states the policy outcome (for example "eligible families receive the benefit within 10 working days") and works back to the service, following point 10 of the UK Government Service Standard: define what success looks like and publish performance data.
- **Approval and records.** The approved strategy, its version and the governance body that approved it are kept, so an auditor can see why a service was built the way it was.

## When code is cheap to produce

Code assistants and agents lower the cost of building a feature. They do not lower the cost of owning one: support, documentation, security patches, accessibility checks, data protection reviews and the attention it takes from users. Three consequences for strategy:

- **Focus matters more.** When anything can be built in a week, the question "should this exist?" is the only filter left. Write the "we will not" list first.
- **Carrying cost decides.** Before adding a feature, estimate its yearly cost to own. A feature that is cheap to build and costly to own is a bad bet.
- **Strategy is tested faster.** Working prototypes on real data can test a strategic bet in days instead of quarters. Use that speed to drop weak bets early, not to ship more of them. See [agile in the AI era](../ways-of-working/agile-in-the-ai-era.md) and, for AI features, [building with AI](../ai/building-with-ai.md).

## Cloud, on-premises and air-gapped

The strategy method does not change. Products installed on customer sites or in air-gapped networks have slower feedback and slower adoption, so write the strategy for longer horizons and include the upgrade path as a product choice: how many versions you support and how customers move between them. See [release management](../delivery/release-management.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A vision statement presented as the strategy | Add target users, the problem, the guiding choices and 2 to 4 measured outcomes. |
| Strategy is a list of features with dates | Replace features with problems and outcomes; put solutions on the roadmap. See [roadmaps and prioritisation](roadmaps-and-prioritisation.md). |
| "For everyone" | Name who it is not for. In public services, name who must be served, including assisted users. |
| The biggest customer sets the strategy | Weigh the request against the strategy in writing; a custom contract is a separate commercial decision. |
| Strategy written once, then forgotten | Quarterly 60-minute review against the outcomes. |
| Success measured as users registered or features shipped | Measure retained use and task success. See [product metrics and experiments](product-metrics-and-experiments.md). |
| Every feature kept forever | Yearly retirement review based on use and carrying cost. |

## Templates

- [Product strategy on a page](../../templates/product/product-strategy-on-a-page.md)
- [Product one-pager](../../templates/product/product-one-pager.md)
- [Strategy one-pager (technical strategy)](../../templates/strategy/strategy-one-pager.md)
- [OKR template](../../templates/leaders/okr-template.md)

## Sources

- Marty Cagan with Chris Jones, *Empowered* (Wiley, 2020).
- Marty Cagan, *Inspired*, second edition (Wiley, 2017).
- Clayton M. Christensen, Taddy Hall, Karen Dillon, David S. Duncan, *Competing Against Luck* (HarperBusiness, 2016).
- Richard Rumelt, *Good Strategy Bad Strategy* (Crown Business, 2011).
- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
