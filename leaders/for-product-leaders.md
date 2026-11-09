# For product leaders

A chief product officer or head of product is judged on outcomes that users and the business feel, not on the volume of features shipped. Give teams problems to solve instead of features to build, insist on evidence over opinion in every review, publish roadmaps as forecasts, and make stopping work as normal as starting it. When code is cheap to produce, your scarcest resources are focus, discovery and users' attention, so protect those before you add delivery capacity.

## When to use this

- You are new in a chief product officer, head of product or service owner role and need a plan.
- Teams ship steadily, yet the outcomes the board cares about do not move.
- The roadmap is a list of dated promises made by sales, the board or ministers.
- Product managers spend their week writing tickets and chasing status.
- Code assistants have raised output, and you suspect the product is growing without getting better.
- You run a public service or a regulated product where users cannot choose another provider.
- You sell to organisations and the roadmap is set deal by deal.
- You lead an internal platform or staff system whose users have no other option.

The practice behind this page is in the [product](../playbook/README.md#3-product) pages: [product strategy](../playbook/product/product-strategy.md), [product discovery](../playbook/product/product-discovery.md), [roadmaps and prioritisation](../playbook/product/roadmaps-and-prioritisation.md), [product metrics and experiments](../playbook/product/product-metrics-and-experiments.md), [pricing and packaging](../playbook/product/pricing-and-packaging.md) and [launch and adoption](../playbook/product/launch-and-adoption.md). How product and engineering share decisions is in [product partnership](../playbook/ways-of-working/product-partnership.md).

## Feature teams or product teams

Marty Cagan's *Empowered* (2020) separates teams that are given features to build from teams that are given problems to solve and are accountable for the result. The difference is in what the leader hands over.

| You hand a team | Feature team | Product team |
|---|---|---|
| The work | a list of features with dates | 1 to 3 outcomes per quarter, with the strategy and the evidence behind them |
| Who decides the solution | stakeholders or the leader | the product trio, within the strategy and an appetite |
| How success is judged | delivered on time | the outcome moved, or the team learned why not and stopped |
| What the product manager does | writes tickets, manages stakeholders | owns value and viability risk, runs discovery, says no with evidence |
| What engineers do | estimate and build | take part in discovery, own feasibility, propose solutions |

Moving from the first column to the second is the main job of a new product leader in most organisations. It takes trust in both directions: the leader gives problems, and the team shows evidence each week.

## A product leader's rhythm

Fit this into the wider [operating rhythm](operating-rhythm.md).

| Cadence | Forum | Time box | Questions |
|---|---|---|---|
| Weekly | Outcome review per product area | 30 minutes | What moved this week? What did we learn from users? What will we test next? |
| Every 2 weeks | Forecast check with engineering | 30 minutes | Have any 85% dates moved by more than two weeks? Who needs to hear it? |
| Monthly | Product review of 2 or 3 bets | 60 minutes | Evidence level, assumption tests run, stop conditions, carrying cost |
| Quarterly | Strategy and roadmap review with the CTO and design lead | half a day | Which outcomes moved? What do we stop? Does the roadmap fit the capacity split? |
| Quarterly | Pricing and commitments review with finance and sales (commercial products) | 90 minutes | Margin and discount depth by plan; share of capacity held by customer commitments; any commitment at risk? |
| Twice a year | Retirement review | 2 hours | Which features have low use and high carrying cost? What do we remove? |

## Questions to ask in a product review

Ask these instead of "is it on track?". A strong team answers with evidence and a link.

| # | Question | A good answer sounds like |
|---|---|---|
| 1 | Which outcome does this serve, and where is it now against the baseline? | a number, a trend and a data source |
| 2 | What is the strongest evidence that users need this? | observed behaviour or a test result, not "a big customer asked" |
| 3 | Which assumption is riskiest, and how did you test it? | a named test, its pass line and the result |
| 4 | What did you compare it with? | at least two alternatives, and why they lost |
| 5 | What would make you stop? | a measure, a threshold and a date |
| 6 | Who did you talk to this week? | names or roles of real users, including ones who struggle |
| 7 | What will it cost to own each year? | support, run cost, maintenance, in rough numbers |
| 8 | When will you know if it worked, and how? | a check date and a method, with its confidence stated |

Speak last. If the most senior person gives an opinion first, the review becomes a guess at what the leader wants.

## Evidence over opinion

- **Name the evidence level** on every roadmap item: opinion, user statements, observed in a test, measured in production. Fund large bets (a starting point: more than one team-quarter of work) only above opinion, and approve them in stages as in [approve, fund, stop or escalate](for-business-executives.md#approve-fund-stop-or-escalate).
- **Treat experiments honestly.** Sample size, duration, guardrails and the decision rule are written before launch; nobody stops a test the day it looks good. Check the rules in [product metrics and experiments](../playbook/product/product-metrics-and-experiments.md#reading-results-honestly).
- **Reward good stops.** A team that tests an idea cheaply and drops it saved the cost of a launch. Say so in public, or teams will hide weak results.
- **Separate decision quality from outcome quality.** A well-evidenced bet can still fail. Review the reasoning, not only the result; see [decision making](decision-making.md).

## Roadmaps, forecasts and saying no

- Publish Now, Next and Later, with Next as the following 1 to 3 quarters and dates only as forecast ranges. See [roadmaps and prioritisation](../playbook/product/roadmaps-and-prioritisation.md).
- Agree with the board, sales leaders or ministers that a roadmap is a forecast. Report a change as soon as an 85% date moves by more than two weeks.
- No one outside product commits roadmap items or dates to customers. Custom work is a commercial decision with a price and a carrying cost.
- Answer every named request with yes, later, not now or no, with the reason and what would change the answer. Keep the log and read it for patterns each quarter.
- Agree the capacity split with the CTO (a starting point of 60% features, 20% reliability, 15% debt, 5% platform) and defend the non-feature share. See [portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md).

## Splitting the work with the CTO and design lead

There must be a written split. Record it in [decision rights](../playbook/operating-model/decision-rights.md).

| Area | Product leader | CTO or head of engineering | Design lead |
|---|---|---|---|
| Which problems, and why now | decides | input | input |
| Product strategy and outcome targets | owns | agrees | agrees |
| Technical strategy, architecture, quality bar | input | owns | input |
| Capacity split | agrees | agrees | informed |
| Pricing and packaging | owns, with finance (margin) and sales | input on cost to serve | input on how plans are shown |
| Customer commitments in contracts | approves, with the sales leader | approves the forecast | informed |
| Discovery practice and research operations | owns with design | supports engineers' time | owns with product |
| What ships and when | together, against agreed criteria | together | together |
| Whether it worked | together, against the agreed metric | together | together |

## B2B and enterprise products

When you sell business to business (B2B), sales is the product's main source of revenue and of market evidence, and its strongest pressure on the roadmap. Work with it, in writing.

- **Agree the target segment with the sales leader.** The strategy names the customers you sell to and the ones you decline. Sales targets and compensation that reward deals outside the segment will defeat any roadmap.
- **One commitment review.** Every feature or date promised to a customer passes a short review by product, engineering and sales, as set out in [roadmaps and prioritisation](../playbook/product/roadmaps-and-prioritisation.md#b2b-and-enterprise-roadmaps). Track the share of feature capacity it consumes and keep every commitment you make.
- **Win and loss interviews every month.** The reasons buyers give to a salesperson are not always the real ones. Have product or research staff call them.
- **Separate buyer, user and administrator.** Each gets discovery time; renewals depend on the daily user.
- **Own pricing and packaging with finance.** Plans, discount bands and price changes are product decisions with a margin floor set by finance. See [pricing and packaging](../playbook/product/pricing-and-packaging.md).

## Product operations

Product operations is a small function that runs the shared machinery product teams depend on, so that product managers spend their time on users and decisions (Perri and Tilles, 2023). Start it when you have more than about five product teams, or earlier if product managers spend a day a week collecting data by hand.

| Owns | Does not own |
|---|---|
| Access to product data and the metric definitions behind dashboards, with the data team | Which outcomes teams pursue |
| The customer feedback pipeline: support, sales and research notes tagged and searchable | Deciding which requests are accepted |
| Research operations: recruiting, consent, incentives, the research repository | Running the interviews for the trio |
| The experiment log, launch checklist and decision log, kept current | Approving experiments or launches |
| The product rhythm: review calendars, roadmap publishing, pricing and commitment review papers | Writing strategy or roadmaps |

Judge it by the time product managers get back and by how fast a trio can answer a question with data, not by the number of processes it runs. If it becomes a gate that teams must pass, reduce it.

## Internal platforms and staff systems

A developer platform, a data platform, or a case-management, finance or HR system used by staff is a product whose users usually cannot leave. Like a public service, the missing market signal has to be replaced on purpose.

- **Name a product owner** for each internal product, with the same strategy page, outcomes and say-no rights as an external product. See [developer platform](../playbook/platform/developer-platform.md#platform-as-a-product).
- **Measure the work removed, not the adoption mandated.** Track time saved for the teams that use it, tickets avoided, time to complete the main task, and voluntary adoption where teams have a choice. Mandated adoption shows compliance, not value.
- **Discovery with captive users.** Shadow staff doing real work, read their workarounds (spreadsheets kept next to the system are the clearest signal) and survey satisfaction every 6 months.
- **Roadmap from the consuming teams' outcomes.** Each item names the teams and the outcome it serves. Requests from senior stakeholders go through the same evidence rules.
- **Charge with care.** Charging internal teams for a platform can show real demand, but it also pushes teams to build their own copies. Decide with finance; see [technology budget and cost](../playbook/strategy/technology-budget-and-cost.md).

## Product in regulated and public-sector settings

Where people cannot choose another provider, the usual market feedback is missing. Users who struggle do not leave; they phone, queue, ask for help or give up. Product leadership has to make up for that on purpose.

| Decision | Starting point | Read |
|---|---|---|
| Who owns the service | one named service owner per end-to-end service, judged on completion rate, time to outcome and user satisfaction | [For data and digital officers](for-data-and-digital-officers.md#chief-digital-officers) |
| Who the product must serve | everyone eligible, including assisted-channel users, assistive technology users and people on low-cost phones and slow networks | [Product strategy](../playbook/product/product-strategy.md#assured) |
| How success is measured | completion rate, digital take-up, user satisfaction, cost per transaction and time to outcome, with results for struggling groups reported separately | [Product metrics and experiments](../playbook/product/product-metrics-and-experiments.md) |
| What may be tested on real people | presentation and service design; never entitlements, prices or legal protections; ethics or legal review where outcomes could change | [Product metrics and experiments](../playbook/product/product-metrics-and-experiments.md#assured) |
| How phases are governed | discovery, alpha, beta, live, with an assessment before public beta and before live where a service standard applies | [Public sector](../playbook/compliance/public-sector.md) |
| How launches work | assisted channel kept until the digital route works for everyone; regulated communications reviewed with lead time | [Launch and adoption](../playbook/product/launch-and-adoption.md#assured) |
| How fixed scope is handled | MoSCoW inside small releases, Must kept to about 60% of effort, re-forecasts recorded | [Roadmaps and prioritisation](../playbook/product/roadmaps-and-prioritisation.md#assured) |

Policy intent is the vision. A product leader in government translates a law or ministerial decision into a measurable outcome for the people it is meant to reach, then defends that outcome when deadlines press on scope.

## Product management when code is cheap

Code assistants and agents lower the cost of building. They do not lower the cost of deciding what to build, checking it works for users, supporting it, or owning it for years. The public evidence on speed gains is mixed (see [agile in the AI era](../playbook/ways-of-working/agile-in-the-ai-era.md#what-the-evidence-says)), so plan on measured results, not assumed ones.

| What changes | What a product leader does |
|---|---|
| Building is no longer the slow part | Protect discovery time and review capacity before adding delivery capacity |
| Prototypes cost hours | Test value with working prototypes on real data; keep them out of production until rebuilt to standard |
| Product managers and designers can build working prototypes themselves | Encourage it for discovery; engineers still own what reaches production and its quality bar |
| Language models can imitate users | Never accept generated personas or synthetic interviews as evidence of need, price or usability |
| Every feature scores well on effort | Weigh carrying cost and users' attention alongside build effort when ranking |
| The product grows by default | Retirement review twice a year; count features removed as well as shipped |
| Launch, support and adoption do not scale with code | Cap concurrent launches per product area (a starting point: one launch tier 1 and two launch tier 2 launches in rollout at once) |
| AI features behave probabilistically | Require an eval set and a pass threshold, agreed with the product owner, before launch; see [building with AI](../playbook/ai/building-with-ai.md) |
| Output metrics rise quickly | Report outcomes, rework and change fail rate alongside throughput; see [metrics](../playbook/measurement/metrics.md) |

The product manager's job shifts further toward judgment: framing the problem precisely, writing acceptance examples and evals before generation starts, and deciding what not to build.

## Hiring and growing product managers

| Test for | How (starting point) |
|---|---|
| Problem framing | Give a vague stakeholder request; ask for the problem, the user, the evidence needed and the outcome measure |
| Evidence and experiment design | Show a dashboard from a stopped experiment; ask what they would conclude and what they would check first |
| Saying no | Role-play a senior stakeholder asking for a dated feature; listen for reasons, alternatives and what would change the answer |
| Working with engineers and designers | A joint exercise with an engineer and a designer from the team |
| Domain and regulation (Assured settings) | Ask how they would test an idea when users cannot choose another provider |

Use the [interview scorecard](../templates/people/interview-scorecard.md) and the methods in [hiring](../playbook/people/hiring.md). Do not judge product managers on features shipped or roadmap dates met. Judge them on outcomes moved, the quality of evidence behind their decisions, and good stops.

## First 90 days

Use [first 90 days](first-90-days.md) for the listening phase.

| Period | Focus | Exit criteria |
|---|---|---|
| Days 1 to 30 | listen: users, support, sales or service staff, every product trio; read the last year of launches and their results | a list of the 10 most-used flows with their completion rates; the current evidence level of the roadmap |
| Days 31 to 60 | agree the written split with the CTO and design lead; draft the product strategy on one page | split published; strategy draft reviewed by the executive team |
| Days 61 to 90 | move one or two teams from features to outcomes; start the weekly outcome review; publish the roadmap as Now, Next and Later | 2 teams working to outcomes; roadmap with forecast ranges; first retirement candidate named |

## Common mistakes

| Mistake | Fix |
|---|---|
| Product managers as ticket writers for stakeholders | Give teams outcomes; product managers own value and viability and say no with evidence. |
| Roadmap dates promised to the board as commitments | Forecast ranges with confidence; report changes early. |
| Opinion from the most senior person decides | Ask for the evidence level; speak last. |
| Experiments stopped as soon as they look good | Duration and decision rule fixed before launch. |
| Research outsourced to a separate team that returns reports | Weekly discovery by the trio, with research operations as support. |
| Success measured by features shipped or adoption totals | Outcome metrics, cohorts and guardrails. |
| Products only ever grow | Twice-yearly retirement review. |
| Public service optimised for the digitally confident | Measure and design for everyone who must be served, including the assisted channel. |
| More code from assistants read as more value | Report outcomes and instability metrics alongside throughput. |
| Sales promises features to close deals, product finds out later | One commitment review; capacity share tracked; every commitment kept. |
| Pricing left to finance or sales alone | Product owns packaging with finance and sales; quarterly review. |
| Product operations grows into an approval layer | It runs shared machinery; it does not decide or gate. |
| Internal platform success reported as mandated adoption | Measure time saved and voluntary adoption. |

## Templates

- [Product strategy on a page](../templates/product/product-strategy-on-a-page.md)
- [Product one-pager](../templates/product/product-one-pager.md)
- [Opportunity solution tree](../templates/product/opportunity-solution-tree.md)
- [Experiment brief](../templates/product/experiment-brief.md)
- [Launch checklist](../templates/product/launch-checklist.md)
- [OKR template](../templates/leaders/okr-template.md)
- [Pre-mortem](../templates/leaders/pre-mortem.md)

## Sources

- Marty Cagan with Chris Jones, *Empowered* (Wiley, 2020).
- Marty Cagan, *Inspired*, second edition (Wiley, 2017).
- Teresa Torres, *Continuous Discovery Habits* (Product Talk, 2021).
- Melissa Perri and Denise Tilles, *Product Operations: How Successful Companies Build Better Products at Scale* (Product Institute, 2023).
- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments* (Cambridge University Press, 2020).
- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
- GOV.UK Service Manual, agile delivery phases: https://www.gov.uk/service-manual/agile-delivery
