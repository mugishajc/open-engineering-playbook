# Product discovery

The problem: teams build what was asked for and find out months later that users did not need it, could not use it, or the business could not afford to run it. Make discovery a weekly habit of the product trio (product manager, designer and tech lead): talk to users every week, map the opportunities behind your outcome, and test the riskiest assumption before you build. Discovery and delivery run side by side in the same team, so evidence reaches the backlog every week, not once in a research report.

## Outcomes

Starting targets. Tune them after a quarter.

| Signal | Starting target |
|---|---|
| Product trio talks with at least one real user | Every week |
| Engineers who took part in research or support | Every engineer, at least once a quarter (see [product partnership](../ways-of-working/product-partnership.md)) |
| Roadmap items with linked evidence (interview notes, usage data, test results) | At least 80% |
| Assumption tests run per team | At least 2 a month |
| Ideas dropped or reshaped in discovery before delivery started | More than zero each quarter (if zero, you are confirming, not testing) |
| Time from booking to holding a user conversation | Under 1 week, from a standing recruitment process |

## Four risks to test before you build

Marty Cagan's *Inspired* names four risks. Discovery exists to reduce them before the team commits delivery capacity.

| Risk | Question | Typical test | Who leads |
|---|---|---|---|
| Value | Will people choose to use it, or buy it? | story-based interviews, a fake door, a concierge test, a pilot with real data | product manager |
| Usability | Can people work out how to use it? | usability test with about 5 users from each distinct user group on a prototype, repeated after each change (Nielsen, 2000) | designer |
| Feasibility | Can we build and run it with the time, skills and technology we have? | a spike, a working prototype, a load test, an eval set for AI features | tech lead |
| Viability | Does it work for the rest of the organisation: legal, finance, support, sales, compliance? | a review with the people who carry the cost or the risk | product manager |

In regulated and public-sector settings, viability carries the most weight and is the risk most often tested last. Test it first. Where people must use the service, "will they choose it?" becomes "will they succeed first time, without help, and does that deliver the policy outcome?". People who cannot switch provider still drop out, phone, make mistakes or give up, and those are the value signals to test against.

## Discovery without a research budget

Most teams have no researcher, no recruitment agency and no incentive budget. Discovery still works at that cost, if you use the contact you already have.

| Source you already have | How to use it | Watch out for |
|---|---|---|
| Support tickets, chats and call notes | Read 20 a week as a trio. Tag each to an opportunity. Count repeats. | It only shows people who bothered to contact you |
| Sales calls, demos and lost deals | Sit in on 2 calls a month; ask sales for the last 5 lost deals and call the buyers | Sales reports the reason the buyer gave, not always the real one |
| Front-line and operations staff | Shadow the people who answer the phone or process cases for half a day a quarter | Staff describe users' problems through their own workload; check with users |
| Product data you already log | Find the step where most people stop, then ask 5 of them what happened | Data shows where, never why |
| Your own users, recruited in the product | A one-line invitation after a key task; 20-minute calls on video or phone | Volunteers are more engaged than average; also recruit people who stopped |
| Quick tests in person | Five short sessions in a place users already are: a branch, a counter, a trade event | Ask permission from whoever runs the place; follow the consent rules below |

Rules that keep it cheap and honest:

- **Time is the budget.** Thirty minutes of conversation and thirty minutes of synthesis a week per trio is the minimum. Put it in the calendar like any other meeting.
- **Paper and screenshots are prototypes.** A sketch or a screenshot with a changed label answers most usability questions.
- **Say thank you in a way you can afford.** A thank-you note, early access or a small voucher. Do not promise features in return for time.
- **Do not substitute colleagues for users.** Staff can try a prototype for obvious bugs, but they know the jargon and the workarounds. They are not evidence of value or usability.

## B2B and enterprise discovery

In business-to-business (B2B) products sold to organisations, the person who buys, the people who use it every day and the administrator who sets it up are different people with different problems. Interview all three. A product that wins the buyer and fails the daily user puts the renewal at risk.

- **Win and loss interviews.** Call buyers within a month of a won or lost deal, with someone other than the salesperson asking the questions.
- **Design partners.** Pick 3 to 5 customers who agree to try early versions on real work and talk every 2 weeks. Write down what they get and what they do not: early access and influence, not a promise to build what they ask.
- **Customer advisory boards** hear direction, not requirements. The biggest customers are not a sample of the market; weigh what they say against the target segment in the [product strategy](product-strategy.md).
- **Requests are leads.** "Customer X needs feature Y" is a solution. Ask what the customer was trying to do, how they do it today and what it costs them. Then look for the same problem in other accounts.
- **Contract and data limits.** Access to a customer's users or data for research often needs the customer's written agreement. Ask through the account owner and record what was agreed.

## Practice

### Foundation

- **Talk to users every week.** Teresa Torres's *Continuous Discovery Habits* (2021) sets the habit: at least weekly contact with customers by the team building the product, in pursuit of an outcome. Thirty minutes a week is enough to start. In a startup, the founders and engineers also answer support.
- **Ask about the past, not the future.** Ask "tell me about the last time you..." and follow the story. People cannot predict what they will do, and they are polite about your ideas. Do not pitch the solution in an interview.
- **Automate recruiting.** A short question inside the product or on the support page ("would you talk to us for 20 minutes?") keeps a list of willing users. Without it, weekly contact dies within a month.
- **Write one line after each conversation** in a shared place: who, the story, what surprised you. Tag it to the opportunity it relates to.
- **Test the riskiest assumption first,** with the cheapest test that could prove it wrong. A sketch shown to five users often settles a question a two-week build would not.

### Standard

- **Opportunity solution tree.** Torres's tree has four levels: the outcome the team owns, the opportunities (unmet needs, pain points, desires) discovered in research, the solutions that might address them, and the assumption tests for each solution. Keep it in the [opportunity solution tree](../../templates/product/opportunity-solution-tree.md) template and update it weekly. Compare at least three solutions for the chosen opportunity before picking one.
- **Dual-track work.** Discovery and delivery happen in the same team at the same time. The trio spends part of each week on discovery; the rest of the team delivers the solutions with the most evidence. Do not hand discovery to a separate research team that returns a report.
- **Name the evidence level.** For each roadmap item record the strongest evidence behind it: opinion, user statements, observed behaviour in a test, or measured behaviour in production. Treat "a customer asked for it" as a lead to investigate, not as evidence of value.
- **Jobs to be done interviews** for new markets or large bets: find recent buyers or switchers and reconstruct the situation that made them look for a new solution (Christensen and colleagues, 2016).
- **Test with prototypes of the right fidelity.** Clickable mock-ups for usability. Live-data prototypes when the value depends on the user's real data. Experiments in production for questions only real behaviour can answer; see [product metrics and experiments](product-metrics-and-experiments.md).
- **Use research operations at scale.** With more than about five teams, a small shared function runs recruiting, consent, incentives and the research repository so that each trio spends its time on conversations.

### Assured

- **Seek out the users you cannot see in the data.** Where people cannot choose another provider, the users who struggle most often leave no trace in analytics: they phone, visit a counter, ask a relative or give up. Recruit people who use assistive technology, people with low literacy or low digital confidence, people on low-cost phones and slow networks, and people who use the assisted channel. See [accessibility and inclusion](../../leaders/for-government.md#accessibility-and-inclusion).
- **Consent, data protection and safeguarding.** Research with members of the public needs informed consent, a lawful basis for any personal data recorded, a retention period, and extra care for children and vulnerable adults. Store recordings in the same controlled systems as other personal data. See [data security and privacy](../data/data-security-and-privacy.md).
- **Follow the phase model when one applies.** The GOV.UK Service Manual runs public services through discovery, alpha, beta and live. Discovery ends with a decision, which can be "do not build". Alpha compares several approaches with prototypes. Do not skip to beta because a supplier contract has started.
- **Fake doors and pricing tests need sign-off.** In regulated markets an offer shown to a customer can be a regulated promotion or a contractual commitment. Agree with compliance which discovery tests may be shown to real customers, and never test access to an entitlement on members of the public.
- **Use failure demand as evidence.** Failure demand is contact caused by a failure to do something, or to do it right, for the user (Seddon, 2003): "where is my application?", "I don't understand this letter", a resubmitted form. Sample calls, letters, complaints and appeals each month, sort them into value and failure demand, and treat each large failure category as an opportunity. Do not turn the failure-demand share into a target; Seddon warns it gets under-reported.
- **Recruit beyond the online sample.** Find people with low or no digital skills through the assisted channel, libraries, community organisations, advice services and charities. The GOV.UK Service Manual treats incentives for members of the public as normal and asks you to budget for disabled participants' extra costs, such as a helper or transport.
- **Keep the evidence trail.** Link research findings and test results to decision records, so a reviewer can see why a design was chosen.

## When code is cheap to produce

- **Prototypes become the discovery tool.** An assistant can produce a working prototype on real data in hours. That lets you test value with behaviour instead of opinions. It also tempts teams to ship the prototype. Label prototypes as throwaway, keep them out of production repositories, and rebuild what survives to the normal standard. See [AI engineering practices](../ai/ai-engineering-practices.md).
- **Building is no longer proof of commitment.** Stakeholders may see a demo and assume the feature is coming. Say before every demo what it is for and what decision it informs.
- **Discovery capacity becomes the constraint.** If delivery speeds up and discovery does not, the team ships more unvalidated work. Protect the trio's weekly discovery time before adding delivery capacity.
- **AI-assisted interview analysis.** Record interviews (with consent), transcribe them, then use a language model to pull quotes, group themes and flag contradictions across sessions. Always check the summary against the recording; models drop outlier opinions and soften negative feedback.
- **Synthetic users are not users.** A language model asked to play a customer returns the average of what it has read, politely. Use it to draft interview guides, rehearse a sales pitch or generate edge-case scenarios before a real session, never as evidence of a need, a price or usability.
- **Prototype generation from specs.** Use a code assistant to turn a one-page spec into a clickable prototype in hours instead of days. This shrinks the cost of testing an idea with real users but does not replace the test itself.
- **For AI features, the eval set is part of discovery.** Writing 50 real examples with expected answers forces the team to define "good" with users before building. See [building with AI](../ai/building-with-ai.md).

## Cloud, on-premises and air-gapped

Discovery is mostly conversations and tests, so the method does not change. Products installed on customer sites or in air-gapped networks give no telemetry: rely on structured customer calls, site visits, support tickets and upgrade surveys, as set out in [product partnership](../ways-of-working/product-partnership.md#cloud-on-premises-and-air-gapped). Research tools that store recordings must meet the same residency rules as the product's data.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A research phase that ends in a report, then delivery begins | Weekly discovery inside the team, alongside delivery. |
| "Would you use this?" questions | Ask about specific past behaviour. |
| Discovery used to confirm a decision already made | Compare at least three solutions; record ideas dropped. |
| Only the product manager meets users | Trio together; every engineer at least quarterly. |
| Analytics treated as the voice of all users | Recruit the users who leave no data: assisted, offline, excluded. |
| Prototype shipped to production because it worked in the demo | Throwaway label; rebuild to standard. |
| Stakeholder requests logged as validated needs | Record the evidence level for every item. |
| "No budget, so no research" | Use support, sales, operations staff and in-product recruiting; 30 minutes a week. |
| Only the buyer interviewed in a business product | Interview buyer, daily user and administrator. |
| Language-model personas reported as user research | Talk to real users; use generated personas only for preparation. |

## Templates

- [Opportunity solution tree](../../templates/product/opportunity-solution-tree.md)
- [Experiment brief](../../templates/product/experiment-brief.md)
- [Product one-pager](../../templates/product/product-one-pager.md)
- [Feature request form](../../templates/github/ISSUE_TEMPLATE/feature_request.yml)

## Sources

- Teresa Torres, *Continuous Discovery Habits* (Product Talk, 2021).
- Marty Cagan, *Inspired*, second edition (Wiley, 2017).
- Clayton M. Christensen, Taddy Hall, Karen Dillon, David S. Duncan, *Competing Against Luck* (HarperBusiness, 2016).
- Eric Ries, *The Lean Startup* (Crown Business, 2011).
- Jakob Nielsen, "Why You Only Need to Test with 5 Users" (Nielsen Norman Group, 2000): https://www.nngroup.com/articles/why-you-only-need-to-test-with-5-users/
- John Seddon, *Freedom from Command and Control* (Vanguard Education, 2003).
- GOV.UK Service Manual, finding participants for user research: https://www.gov.uk/service-manual/user-research/find-user-research-participants
- GOV.UK Service Manual, agile delivery phases: https://www.gov.uk/service-manual/agile-delivery
- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
