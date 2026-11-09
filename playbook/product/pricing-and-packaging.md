# Pricing and packaging

The problem: prices are set once at launch by copying a competitor, plans fill up with every feature anyone asked for, and nobody knows which customers the business loses money on. Treat pricing and packaging as product decisions owned jointly by the product lead, finance and sales. Charge for a unit that grows with the value customers get, test willingness to pay before you build, and change prices rarely, with notice, as a launch tier 1. In public services, where fees are set by law or policy, the same discipline applies to fees, exemptions and the cost to serve.

## Outcomes

Starting targets. Tune them after two quarters.

| Signal | Starting target |
|---|---|
| Every paid plan has a written target customer, value metric, owner and gross margin | 100% |
| New paid products or plans with willingness-to-pay evidence before build | 100%, from at least 10 conversations with target buyers |
| Price changes for existing customers announced with notice | 100%, at least one full billing period ahead, or longer where the contract or law requires |
| Business deals with discounts inside the approved bands, or approved by the named owner | 100% |
| Gross margin, discount depth and plan mix reviewed | Every quarter |
| Customers paying less than their cost to serve, known and listed | Yes, reviewed every quarter |

## The five decisions

| Decision | Question | Starting point |
|---|---|---|
| Value metric | What unit do customers pay for: user, seat, location, transaction, usage or a flat fee? | A unit the customer understands, can predict and that grows with the value they get. Per-seat pricing discourages wide use inside an account. Pure usage pricing matches value but makes bills hard to budget; offer a committed amount with usage above it. |
| Packaging | Which features go in which plan? | Three plans at most to start, separated by the needs of different segments, not by how hard a feature was to build. A feature only one segment needs is an add-on. Keep security basics (single sign-on, audit logs) affordable or included where your customers handle personal data. |
| Free offer | Free plan, free trial, or neither? | A free plan when users can get value alone and some of them bring paying customers. A time-limited trial when value needs setup. Neither when every user carries real cost to serve or support. |
| Price level | How much? | From the value to the customer and the price of their alternative (often a spreadsheet, a person or doing nothing), checked against cost to serve. Cost plus a margin is the floor, not the price. |
| Discounts and changes | Who can discount, how far, and how do prices change? | Written discount bands with named approvers. Price rises with notice, a reason customers can understand, and a stated policy on existing customers. |

Write the decisions on one page and link it from the [product strategy on a page](../../templates/product/product-strategy-on-a-page.md). Ramanujam and Tacke (2016) argue for designing the product around the price: settle what customers will pay for, and in which bundles, before the feature set is fixed.

## Finding out what people will pay

| Method | Use it for | Limits |
|---|---|---|
| Willingness-to-pay conversations | early, before build: which problems are worth paying for, which features matter most, which unit makes sense | People say a price more easily than they pay it; treat answers as a range |
| Van Westendorp price sensitivity meter | a first range for a new product, from four survey questions on too cheap, cheap, expensive and too expensive (van Westendorp, 1976) | Stated, not real, behaviour; needs respondents who understand the product |
| Conjoint analysis | trade-offs between features, plans and price in a survey of choices (Green and Srinivasan, 1978) | Needs a careful survey design and enough respondents in each segment; buy the expertise if you do not have it |
| Sales data in business products | win rate, deal size and discount depth by price point and segment | Salespeople's discounting changes the result; record list price and final price |
| Live price tests | new customers only, by market or time period, with a written plan | Legal and trust limits; see Assured. Existing customers comparing notes find a random split quickly |

Read price tests over a full billing cycle, not one week, and include guardrails: refunds, downgrades, cancellations, support contacts and complaints. The rules in [product metrics and experiments](product-metrics-and-experiments.md) apply.

## Practice

### Foundation

- **One page of pricing decisions** covering the five decisions above, owned by the founder or product lead.
- **Know your cost to serve** per customer or per plan: hosting, third-party fees, payment fees, support time. A plan you lose money on is a decision, not an accident.
- **Publish prices** where your buyers expect them. If you sell by quote, publish a starting price or a range so buyers can qualify themselves.
- **Few plans, few changes.** Change the price structure at most once or twice a year. Each change costs support, sales and billing work.
- **Ask about money in discovery.** End some interviews with "what do you pay for this today, in money or time?" See [product discovery](product-discovery.md).

### Standard

- **A pricing group** of the product lead, finance and sales meets each quarter. It reviews gross margin per plan, discount depth, win rate by price point, plan mix, upgrades and downgrades, and revenue kept from existing customers. The product lead owns packaging; finance owns the margin floor; the decision and its reasons are written down.
- **Discount bands.** Sales can give up to a set discount; deeper discounts need the named approver; non-standard terms (free months, custom features, unusual payment terms) go through the same commitment review as roadmap promises in [roadmaps and prioritisation](roadmaps-and-prioritisation.md#b2b-and-enterprise-roadmaps).
- **Price and packaging changes are launch tier 1.** Use the [launch checklist](../../templates/product/launch-checklist.md): billing system, invoices and tax handling tested; support and sales briefed; customer notice sent; help pages updated. See [launch and adoption](launch-and-adoption.md).
- **A written policy for existing customers.** Decide whether they keep the old price, move at renewal, or move after notice, and apply it to everyone in the same position.
- **Every feature has a plan.** When a feature enters Now on the roadmap, the one-pager says which plan it belongs to and why.

### Assured

- **Fair value in financial services.** In the UK, the Financial Conduct Authority's Consumer Duty requires that the price a customer pays is reasonable compared with the overall benefits. Keep a fair value assessment for each product, including for groups of customers who may get worse outcomes. Other regulators have similar rules; see [regulated industries](../compliance/regulated-industries.md).
- **Personalised prices must be disclosed.** In the EU, Directive (EU) 2019/2161 requires traders to tell consumers when a price was personalised on the basis of automated decision-making. Agree with legal before any price varies by user.
- **Clear total prices.** Show the full price, including mandatory fees, before the customer commits. Make cancelling a subscription as easy as starting it where the law requires, and check the rules in each market you sell to.
- **Public-service fees follow the law and the finance rules.** A fee, an exemption or a waiver for people on low incomes is set by legislation or by the finance rules of your government (in the UK, Managing Public Money). Product teams design how fees, exemptions and refunds work for users. They do not test fee levels on citizens. Measure the cost per transaction and publish it where the service standard asks.
- **Records.** Keep each pricing decision, its evidence and its approval, so an auditor or regulator can see why a price was set.

## When code is cheap to produce

- **AI features have a running cost per use.** Each model call costs money, and heavy users can cost far more than they pay on a flat plan. Before launch, estimate cost per active user at the 50th and 95th percentile of use. Set usage limits, a fair use policy or a usage-based add-on so the plan keeps a positive margin. Track gross margin per plan weekly for the first month. See [building with AI](../ai/building-with-ai.md).
- **Plans fill up faster.** Cheap features end up in a plan by default. Each one makes the plan harder to explain and to sell. A feature goes into a plan only when a target segment needs it.
- **Prototypes can test price.** A working prototype shown with a price, to buyers who could pay it, gives better evidence than a survey. Label it as a prototype and make no delivery promise.

## Cloud, on-premises and air-gapped

Hosted products can meter usage directly. Software installed on customer sites is usually sold as a subscription or as a perpetual licence with a yearly maintenance fee. Air-gapped sites cannot report usage, so use licence files with an expiry date, a yearly self-declaration by the customer administrator, and the right to audit in the contract. Price the extra support that offline upgrades need into the plan.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Price copied from a competitor at launch and never reviewed | Value, alternative and cost to serve on one page; quarterly review. |
| Ten plans and a matrix nobody can read | Three plans by segment need; add-ons for the rest. |
| Per-seat price that stops customers adding colleagues | A value metric that grows with value; consider site or usage pricing. |
| Discounts given freely to close the quarter | Discount bands with named approvers; record list and final price. |
| Price rise announced by invoice | Notice, a reason and a written policy for existing customers. |
| A/B testing prices on existing consumers | New customers only, by market or period, with legal agreement. |
| AI feature on a flat plan with no usage limit | Cost per user estimated before launch; limits or a usage add-on. |
| Security features only in the top plan | Keep basic security affordable for customers who handle personal data. |

## Templates

- [Product strategy on a page](../../templates/product/product-strategy-on-a-page.md)
- [Product one-pager](../../templates/product/product-one-pager.md)
- [Launch checklist](../../templates/product/launch-checklist.md)
- [Experiment brief](../../templates/product/experiment-brief.md)
- [Business case](../../templates/strategy/business-case.md)

## Sources

- Madhavan Ramanujam and Georg Tacke, *Monetizing Innovation: How Smart Companies Design the Product Around the Price* (Wiley, 2016).
- Peter H. van Westendorp, "NSS-Price Sensitivity Meter (PSM): a new approach to study consumer perception of prices", Proceedings of the ESOMAR Congress, 1976.
- Paul E. Green and V. Srinivasan, "Conjoint analysis in consumer research: issues and outlook", Journal of Consumer Research 5(2), 1978.
- Financial Conduct Authority, price and value outcome under the Consumer Duty: https://www.fca.org.uk/publications/good-and-poor-practice/price-value-outcome-good-poor-practice-update
- Directive (EU) 2019/2161 on better enforcement and modernisation of Union consumer protection rules: https://eur-lex.europa.eu/eli/dir/2019/2161/oj
- HM Treasury, Managing Public Money: https://www.gov.uk/government/publications/managing-public-money
- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020).
