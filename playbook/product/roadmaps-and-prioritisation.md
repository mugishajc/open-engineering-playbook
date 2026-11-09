# Roadmaps and prioritisation

The problem: the roadmap is a dated list of features promised to sales, customers and the board. Everything is "priority one", dates slip, and whoever says no is called the blocker. Publish the roadmap as a forecast of problems and outcomes in Now, Next and Later, and rank work with an explicit method tied to the [product strategy](product-strategy.md). Treat saying no, in writing and with reasons, as a core product skill.

## Outcomes

Starting targets. Tune them after two quarters.

| Signal | Starting target |
|---|---|
| Roadmap items stated as a problem or outcome with a metric | At least 80% (the same target as [product partnership](../ways-of-working/product-partnership.md)) |
| Dates shared outside the team given as a range with a confidence level | 100% |
| Items forecast at 85% confidence that land by the forecast date | About 85% (much higher means the ranges are too wide) |
| Requests declined or deferred with a written reason sent to the requester | 100% of requests from named stakeholders |
| Items in Now that trace to a strategy outcome or to mandatory work | 100% |
| Commitments to customers made without the product lead's agreement | Zero |
| Share of the feature capacity held by customer commitments | Measured each quarter; a starting ceiling of 25% |
| Customer commitments delivered by the contracted date | 100% (make few, keep all) |

## The roadmap shape

Use the horizons already set in [portfolio and capacity](../strategy/portfolio-and-capacity.md#roadmaps-as-forecasts).

| Horizon | Meaning | What an item looks like | Dates |
|---|---|---|---|
| Now | committed, this quarter | an outcome with the solution being built, for example "cut failed applications from 18% to 10%: new address lookup" | forecast range from throughput at 50% and 85% |
| Next | planned, the following 1 to 3 quarters | a problem with evidence and a target outcome, solution open | quarter, labelled as a forecast |
| Later | direction only | a problem or opportunity the strategy points to | none |

Rules that keep it honest:

- **Forecast, do not promise.** Dates come from measured throughput with a Monte Carlo forecast, as in [planning and forecasting](../ways-of-working/planning-and-forecasting.md). Say "85% likely by 30 June", never "due 30 June".
- **Correct for the planning fallacy.** Kahneman and Tversky (1979) showed that people forecast from the plan in front of them and ignore how similar work went before. Before giving a range for a large item, ask how long the last three similar items took and start from that reference class (Flyvbjerg and Gardner, 2023).
- **Fit the capacity split.** Now holds only what fits the feature share of the agreed split (a starting point of 60% features, 20% reliability, 15% debt, 5% platform). Reliability, debt and platform work are on the same roadmap, not hidden.
- **Re-forecast weekly, review the roadmap quarterly.** Tell stakeholders as soon as an 85% date moves by more than two weeks.
- **One roadmap, several views.** Internal views show all three horizons. External views for customers show Now and Next only, without dates beyond the current quarter, and carry a line saying the roadmap can change.
- **Show what changed.** Each new version lists what was added, moved or dropped since the last one, and why. A roadmap that silently loses items teaches readers to ignore it.
- **Later is not a store room.** An item that has sat in Later for 4 quarters is either re-justified with new evidence or removed, and the requester is told.

## Choosing a prioritisation method

No scoring method replaces the strategy. Use one to make the reasoning visible and comparable, then let the product lead decide.

| Method | Use it for | How it works | Watch out for |
|---|---|---|---|
| Strategy fit first | every item | does it serve a strategy outcome, mandatory work or the capacity split? If not, it does not enter the ranking | skipping this step and scoring everything |
| RICE (Intercom) | ranking many small or medium items | (Reach x Impact x Confidence) / Effort. Impact on a fixed scale (3, 2, 1, 0.5, 0.25), confidence as 100%, 80% or 50% | confidence inflated to 100% without evidence; reach counted in different units |
| Cost of delay and weighted shortest job first | time-critical work: regulatory dates, contract ends, market windows | value lost per week of delay divided by duration; see the [strategy toolkit](../../leaders/strategy-toolkit.md#cost-of-delay-prioritisation) | large items sink forever; split them |
| Kano model | deciding the mix of features for a release or a new product | classifies features as must-be (expected, absence causes complaints), one-dimensional (more is better), attractive (unexpected delight) or indifferent, from a paired survey question (Kano and colleagues, 1984) | attractive features become must-be over time; repeat the survey |
| MoSCoW (DSDM) | a fixed date or fixed budget release | Must, Should, Could, Won't this time. DSDM guidance keeps Must items to no more than about 60% of the effort so the rest is contingency | everything labelled Must; no contingency left |
| Opportunity solution tree | choosing what to discover next | compare opportunities under the team's outcome before choosing solutions; see [product discovery](product-discovery.md) | treating the tree as a backlog |

Record the method and the inputs with each ranking, so a later reader can see why an item won or lost.

## Saying no

A product team that says yes to everything has no strategy. Make no a normal, respectful answer.

- **Answer every named request** within 10 working days with one of: yes, now; yes, later (with the horizon); not now (with what would change the answer); no (with the reason). Keep a public log of decisions.
- **Give the reason in the requester's terms:** which outcome the request does not serve, what would be displaced, and the evidence. "This would push the address lookup, which cuts failed applications, back by about six weeks" is a reason. "Not a priority" is not.
- **Say what would change the decision.** "If five more customers of this size report the same problem, we will look again" turns a no into a test.
- **Customer commitments need the product lead.** Sales or account teams do not promise roadmap items or dates on their own. Commitments go through the review in [B2B and enterprise roadmaps](#b2b-and-enterprise-roadmaps).
- **Escalate disagreements once, in writing,** to the person who owns the strategy. The decision and its reason go in the log.

## B2B and enterprise roadmaps

In business-to-business (B2B) products sold to organisations, deals and renewals put real pressure on the roadmap, and some commitments are worth making. The aim is not to refuse every commitment. It is to make few, make them on purpose and keep all of them.

- **One review for every commitment.** Any promise of a feature or date to a customer, in a contract, order form, proposal, email or slide, goes through a short review by the product lead, the engineering lead and the sales leader. Many companies run it inside the deal desk that already approves non-standard terms. It answers: does it fit the strategy and the target segment, would we build it for other customers anyway, how many other accounts need it (with evidence), what does it displace, and what is the 85% forecast?
- **Commit to the problem, not the specification.** Contract wording describes the outcome the customer needs and a forecast window, not a screen design. Leave the team room to solve it for every customer.
- **Count accounts, not pipeline.** A deal rarely depends on one feature, and summing the value of every deal that mentions a request inflates it. Weight requests by the number of accounts in the target segment that have the problem, and by lost deals where the buyer named it as the reason in a win or loss interview.
- **Custom work has a price.** Work for one customer that no other customer needs is a commercial decision with its own fee, its own maintenance charge and an end date, approved in writing. Prefer building it as a configurable part of the product, or say no.
- **Commitments are a protected line.** Show agreed commitments on the roadmap next to mandatory work, with the contract date. Measure the share of feature capacity they hold. Above about a quarter, sales is setting the roadmap; take that to the head of product and the sales leader together.
- **Ask finance before promising future features.** Under IFRS 15 and its US equivalent ASC 606, a promise of future functionality in a contract can be a separate performance obligation that delays when part of the contract revenue is recognised. Finance and legal review roadmap language in contracts.
- **Renewal risk is evidence, not a trump card.** A large customer threatening to leave is a real cost. Put the cost and the request through the same review, with the account's revenue stated, rather than letting it skip the queue.

## Practice

### Foundation

- One ranked list of problems, in Now, Next and Later, visible to everyone in the company.
- Forecast ranges from items finished per week. No single dates.
- Answer every customer request with yes, later, not now or no, and why. Keep the list.
- In a business product, the founder or product lead approves every customer commitment, in writing.

### Standard

- Outcome roadmaps per team, rolled up per product area. Strategy fit, then RICE or cost of delay, with inputs recorded.
- Roadmap reviewed quarterly with product, engineering and design leads; forecasts re-run weekly and rolled up every 2 weeks, as in [portfolio and capacity](../strategy/portfolio-and-capacity.md#portfolio-review-cadence).
- A decision log of declined and deferred requests, reviewed each quarter for patterns. Repeated requests become discovery questions.
- Each Now item has stop conditions: a measure, a threshold and a date. See [how to stop work](../strategy/portfolio-and-capacity.md#how-to-stop-work).

### Assured

- **Mandatory work on a separate, protected line.** Regulatory changes, audit findings and end-of-life risks are shown with their legal or contractual date and are not traded against features.
- **Fixed scope, split small.** Where procurement or legislation fixes the scope, use MoSCoW inside each release, keep Must to about 60% of effort, and accept the service in small releases, as in [planning and forecasting](../ways-of-working/planning-and-forecasting.md#assured).
- **Re-forecasts are recorded** with the reason, so programme boards and auditors see the history of each date.
- **Public commitments are made from the 85% forecast** and only after the dependencies (other departments, suppliers, legislation) have dates of their own.
- **Equity check before deprioritising.** In a public service, deferring work for a small group (assistive technology users, a minority language) can breach an accessibility or equality duty. Check with the service owner before it drops out of Now.

## When code is cheap to produce

- **Effort shrinks in every formula.** RICE and weighted shortest job first divide by effort. When an assistant cuts effort, almost everything scores well. Weight the carrying cost (support, security, complexity) alongside the build effort, or the roadmap fills with small features nobody needed.
- **Prioritise learning, not building.** The bottleneck moves to discovery, review and adoption. A good Now column holds fewer, better-evidenced items, not more.
- **Say no faster.** A request that once died because it would take a quarter can now be built in a week. The strategy has to decline it instead.

See [agile in the AI era](../ways-of-working/agile-in-the-ai-era.md) for how planning changes when the bottleneck moves.

## Cloud, on-premises and air-gapped

For products installed on customer sites or in air-gapped networks, the roadmap also shows the supported versions and the upgrade windows customers have agreed, because a feature is not in users' hands until they upgrade. Include import and approval time for new dependencies in forecasts.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A Gantt chart of features for the next 18 months | Now, Next and Later; dates only as forecast ranges in Now. |
| Everything is priority one | Strategy fit first, then one ranking method with recorded inputs. |
| Scores used to avoid making a decision | The product lead decides; the score shows the reasoning. |
| Sales promises a feature to close a deal | Commitment review by product, engineering and sales; problem and window in the contract, not a specification. |
| Requests ranked by the total pipeline that mentions them | Count accounts in the target segment and evidence from win and loss interviews. |
| Custom features built free to win one account | Separate price, maintenance charge and end date, or build it as configuration. |
| Requests disappear into a backlog nobody reads | Answer within 10 working days; keep a decision log. |
| Debt and reliability work kept off the roadmap | Show the capacity split on the roadmap. |
| A roadmap that never changes | Quarterly review; each change recorded with the evidence that caused it. |

## Templates

- [Product strategy on a page](../../templates/product/product-strategy-on-a-page.md)
- [Product one-pager](../../templates/product/product-one-pager.md)
- [Opportunity solution tree](../../templates/product/opportunity-solution-tree.md)
- [Business case](../../templates/strategy/business-case.md)

## Sources

- Intercom, "RICE: simple prioritization for product managers": https://www.intercom.com/blog/rice-simple-prioritization-for-product-managers/
- Noriaki Kano, Nobuhiko Seraku, Fumio Takahashi, Shin-ichi Tsuji, "Attractive quality and must-be quality", Journal of the Japanese Society for Quality Control (Hinshitsu) 14(2), 1984: https://doi.org/10.20684/quality.14.2_147
- IFRS Foundation, IFRS 15 Revenue from Contracts with Customers: https://www.ifrs.org/issued-standards/list-of-standards/ifrs-15-revenue-from-contracts-with-customers/
- Agile Business Consortium, DSDM Agile Project Framework, MoSCoW prioritisation: https://www.agilebusiness.org
- Donald G. Reinertsen, *The Principles of Product Development Flow* (Celeritas Publishing, 2009).
- Daniel Kahneman and Amos Tversky, "Intuitive prediction: biases and corrective procedures", TIMS Studies in Management Science 12, 1979.
- Bent Flyvbjerg and Dan Gardner, *How Big Things Get Done* (Currency, 2023).
- Teresa Torres, *Continuous Discovery Habits* (Product Talk, 2021).
