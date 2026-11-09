# Product metrics and experiments

The problem: success is reported as features shipped or sign-ups, experiments stop the day the dashboard turns green, and nobody knows whether last quarter's work helped users. Give each product one primary outcome metric with a few guardrails, and define every metric in writing. Run controlled experiments with the sample size, duration and decision rule fixed before the first user sees a variant. Where an honest experiment is not possible, say so and state the confidence of the evidence you use instead.

Engineering metrics, such as DORA metrics, service level objectives (SLOs) and SPACE, live in [metrics](../measurement/metrics.md). This page covers what users do and whether your changes helped them. The same rules apply to both: definitions are versioned, teams compare themselves with their own baseline, and no metric is used to rate individuals.

## Outcomes

Starting targets. Tune them after two quarters.

| Signal | Starting target |
|---|---|
| Products with one written primary outcome metric and 1 to 3 guardrails | 100% |
| Metric definitions written, versioned and owned | 100% of metrics shown to leaders |
| Experiments with hypothesis, primary metric, guardrails, sample size and decision rule written before launch | 100% |
| Experiments checked for sample ratio mismatch before reading results | 100% |
| Experiments with a minimum detectable effect and a power calculation in the brief | 100% |
| Guardrails with a written margin of acceptable harm | 100% of experiment guardrails |
| Experiments stopped early on a significant result without a pre-planned sequential method | Zero |
| Shipped features reviewed against their metric | 100% within 1 quarter of release (see [product partnership](../ways-of-working/product-partnership.md)) |

## Choosing what to measure

| Level | What it is | Example (illustrative) |
|---|---|---|
| Primary outcome | the one number that shows users get value and the product is working; changes over weeks | shops still active in week 8 after sign-up |
| Input metrics | 2 to 4 behaviours the team can move that drive the outcome | setup completed within a day; sales recorded per active shop per week |
| Guardrails | numbers that must not get worse while you chase the outcome | support contacts per 1,000 users; page load time at the 95th percentile; refunds; complaints; unsubscribes |
| Health | service reliability and cost | SLO attainment, cost per transaction; see [service levels](../reliability/service-levels.md) |

Two published frameworks help you find candidates. Use them as checklists, not as a set of numbers to collect.

| Framework | Parts | Best for |
|---|---|---|
| HEART (Rodden, Hutchinson and Fu, CHI 2010) | Happiness, Engagement, Adoption, Retention, Task success; chosen through goals, then signals, then metrics | user experience of a product or feature |
| AARRR (Dave McClure, 2007) | Acquisition, Activation, Retention, Referral, Revenue | a commercial product's funnel |

For a business product sold to organisations, measure at the account level as well as the user level. A licence bought is not use. Track active seats as a share of seats bought, the share of accounts where the key workflow runs every week, and revenue kept from existing customers over 12 months (net revenue retention, which includes expansion and losses). A few large accounts can hide many small ones that are leaving, so report retention by account size.

For a public service, the funnel stages do not fit: there is no acquisition and no revenue, and users cannot leave. Measure completion rate (share of started transactions finished), digital take-up (share completed online), user satisfaction, cost per transaction, and time to outcome (for example days from application to decision). Point 10 of the UK Government Service Standard asks services to define what success looks like and publish performance data.

Avoid metrics that rise whatever happens to users: total registered users, page views, features shipped, time on site for a task people want to finish quickly. Eric Ries (2011) calls these vanity metrics. Retention and task success are harder to inflate.

## Experiment design

A controlled experiment (an A/B test) randomly assigns users to the current version or a change and compares outcomes. It is the strongest evidence of cause you can get in production. Ron Kohavi, Diane Tang and Ya Xu's *Trustworthy Online Controlled Experiments* (2020) is the reference for this section. They report that most ideas tested in large online experiments fail to improve the metric they targeted, which is why the test matters.

Write the [experiment brief](../../templates/product/experiment-brief.md) before you build the variant. It fixes:

1. **Hypothesis.** "Because we saw X in research, we believe change Y will move metric Z for users W."
2. **Primary metric**, called the overall evaluation criterion in the book. One metric that decides the result. It must be sensitive enough to move within the test and related to long-term value.
3. **Guardrails.** Metrics that stop the test or block the launch if they get worse, whatever the primary metric does. Include at least one trust guardrail (errors, latency) and one user guardrail (complaints, support contacts, opt-outs). Give each guardrail a margin: the largest harm you would accept, for example "support contacts per 1,000 users rise by no more than 5%". "No significant change" in a guardrail is not proof of no harm, because a small test cannot see harm. A guardrail passes only when its confidence interval rules out harm bigger than the margin.
4. **Randomisation unit.** Usually the user or the account, kept stable across sessions. Use the same unit for analysis. In business products, randomise by organisation so colleagues do not see different versions. Then the sample size is the number of organisations, not users: 40 organisations of 500 users each is a test of 40, not 20,000. Analyse per organisation, or use a method that allows for clustering such as the delta method described by Kohavi, Tang and Xu.
5. **Minimum detectable effect and sample size.** The minimum detectable effect is the smallest change worth acting on: the change that would pay for building, launching and owning the feature. State it in absolute terms (10% to 11% is 1 percentage point) and relative terms (a 10% relative lift). Then calculate the users per variant needed to see it, as below.
6. **Duration.** At least one full week, and in whole weeks, so weekday and weekend behaviour both appear. Two weeks is a common minimum, and longer if the sample size needs it.
7. **Decision rule.** What you will do for each result: ship, iterate, or stop. Written before launch. Ship only when the result is both statistically clear (the confidence interval excludes zero in the right direction) and large enough to matter (the effect is worth its carrying cost). A significant 0.1% lift may not pay for the code that produces it.

### Sample size

A rule of thumb from the book for about 80% power at a 5% two-sided significance level: users per variant is about 16 times the metric's variance, divided by the square of the smallest change you want to detect. For a conversion rate p, the variance is p(1 - p).

```python
import math

def sample_size_per_variant(baseline_rate, min_detectable_change):
    """About 80% power, 5% two-sided significance. Rule of thumb from
    Kohavi, Tang and Xu (2020): n = 16 * variance / change squared."""
    variance = baseline_rate * (1 - baseline_rate)
    return math.ceil(round(16 * variance / min_detectable_change ** 2, 6))

def sample_ratio_p_value(control_users, treatment_users):
    """Chi-squared test that a planned 50/50 split really came out 50/50."""
    expected = (control_users + treatment_users) / 2
    chi2 = ((control_users - expected) ** 2 + (treatment_users - expected) ** 2) / expected
    return math.erfc(math.sqrt(chi2 / 2))

print(sample_size_per_variant(0.10, 0.01))    # 14400 users per variant
print(sample_size_per_variant(0.10, 0.005))   # 57600: half the change, four times the users
print(sample_ratio_p_value(50_000, 51_000))   # about 0.0017: investigate before reading results
```

A worked example: a sign-up step converts 10% of visitors. To detect a change of 1 percentage point (10% to 11%) you need about 14,400 users in each variant. If 5,000 eligible users arrive each week, two variants need about 6 weeks. If that is too long, test a bolder change, pick a more sensitive metric, or accept that this question cannot be answered by an experiment at your traffic.

What the numbers mean and where the rule of thumb breaks:

- **Power is the chance of seeing a real effect.** At 80% power, a change that truly moves the metric by exactly the minimum detectable effect still shows as "no significant difference" in 1 test in 5. Smaller real effects are missed more often.
- **Underpowered tests exaggerate their wins.** When a test is too small, the only results that cross the significance line are the ones where chance pushed the estimate up. The reported lift is then larger than the real one, and sometimes has the wrong sign (Gelman and Carlin, 2014, call these magnitude and sign errors). Expect a win from a small test to shrink when you roll it out.
- **Means and revenue need their own variance.** The p(1 - p) formula is for rates. For averages such as orders per user or revenue per user, use the standard deviation measured over the last few weeks. Revenue is usually heavy-tailed: a few large buyers make the variance so big that the test needs many times more users. Cap extreme values at a percentile you fix in the brief, or test a rate such as "share of users who bought".
- **More than two variants need more users.** Each extra variant needs its own full sample, and comparing several variants with the control at 5% each raises the chance of a false winner. Divide the significance level by the number of comparisons (the Bonferroni correction) or test fewer variants.
- **Reduce variance before you add weeks.** Adjusting each user's result for the same metric measured before the experiment (controlled experiments using pre-experiment data, or CUPED, from Deng, Xu, Kohavi and Walker, 2013) can cut the users needed for metrics that are stable per user. Most experimentation platforms offer it. Decide to use it in the brief, not after seeing the result.

### Reading results honestly

| Trap | What goes wrong | Rule (starting point) |
|---|---|---|
| Peeking | Checking the p-value every day and stopping when it dips below 0.05 raises the false-positive rate far above 5% | Fix the duration and read once at the end, or use a sequential method designed for repeated looks and set up before launch: a group sequential design with planned interim looks, or always-valid p-values (Johari and colleagues, 2017). Looking at guardrails daily is fine: stopping for harm is always allowed |
| Sample ratio mismatch | A planned 50/50 split comes out 50,000 to 51,000. Something in assignment or logging is broken, and the result cannot be trusted | Check the split before reading any metric. Investigate if the p-value is below 0.001 |
| Many metrics, one winner | With 20 metrics at a 5% threshold, about one will look significant by chance | One primary metric decides. Treat other movements as leads for the next test |
| Segment fishing | Slicing until some segment shows a win | Name segments in the brief; treat new ones as hypotheses |
| Novelty and primacy effects | Users click a new thing because it is new, or resist it because it is unfamiliar | Plot the effect by day and by how long each user has been exposed. Run until the daily effect is flat for a week. For changes whose effect can build or fade over months (ads, notifications, email frequency, recommendations), keep a small holdout group on the old version for a quarter or more; Hohnhold, O'Brien and Tang (2015) show how a short-term metric gain can hide a long-term loss |
| A surprising result | Very large wins are usually bugs | Re-run or check instrumentation before announcing |
| Platform never validated | The tool itself produces false results | Run A/A tests (two identical variants) when you adopt or change the platform; expect about 5% to show a "significant" difference |

Report every experiment, including the ones that failed, in a shared log with the brief, the result and the decision. A stopped idea is learning that cost less than a launch.

### When not to run an A/B test

An A/B test is the wrong tool in these cases. Say so in the brief, and use the strongest method available instead.

| Situation | Why a test is the wrong tool | Use instead |
|---|---|---|
| Too few units: a business product with a few dozen customers, a low-traffic flow | The sample size calculation needs more units than you will have in a quarter | Staged rollout with a holdout, customer interviews, usability tests |
| Users affect each other: marketplaces, messaging, shared workspaces, a shared stock of appointments or drivers | Treatment leaks into control, so the difference is biased | Randomise by market, region or time period (switchback), and accept fewer units |
| The outcome takes months: loan repayment, renewal, health outcomes | The test ends before the outcome appears | A leading indicator you have shown to predict the outcome, plus a long-term holdout |
| The change is required anyway: a legal duty, a security fix, an accessibility fix | The result cannot change the decision | Ship it and measure that nothing broke |
| The variants would treat people unfairly: prices, credit, benefits, legal protections | Unequal treatment can breach law or trust, see Assured below | Test presentation only, or pilot with consent |
| Customers will see and compare versions: enterprise accounts with administrators, contractual product descriptions | Customers notice, and the contract may describe the product | Opt-in previews and design partners |
| One-off or hard-to-reverse changes: a rebrand, a new pricing model, a migration | There is no stable "after" to compare, and no way back | Discovery before, staged rollout, before and after with a comparison |

Where a clean test is not possible, use the strongest of these:

- **Staged rollout with a holdout**: release behind a [feature flag](../delivery/feature-flags.md) to a group and keep a comparable group on the old version for a fixed period.
- **Before and after with a comparison**: compare the trend in the changed area with a similar unchanged one, not only with last month.
- **Qualitative evidence**: usability tests and interviews explain why, which numbers cannot. See [product discovery](product-discovery.md).

Record the method and its confidence in the decision. "Strong evidence, randomised test" and "weak evidence, before and after" are both honest. Presenting the second as the first is not.

## Practice

### Foundation

- One primary outcome metric and 1 to 3 guardrails, written down with their definitions and data source.
- Basic product analytics on the key user flow, with only the events you need.
- For each shipped feature, look at its metric after 2 to 6 weeks and write one line: worked, did not work, unclear.
- Run experiments only when traffic supports the sample size. Otherwise use staged rollouts and talk to users.

### Standard

- An experimentation platform (built or bought) with stable assignment, automatic sample ratio checks and guardrail alerts. Feature flags of the experiment type serve the variants; see [feature flags](../delivery/feature-flags.md).
- Every experiment has a written brief reviewed by someone outside the team before launch, and an entry in the shared log after.
- Metric definitions versioned, with a note on dashboards when a definition changes, as in [metrics](../measurement/metrics.md).
- Product and engineering leaders review outcomes, DORA metrics and reliability on one dashboard, as [product partnership](../ways-of-working/product-partnership.md) describes.
- A/A tests run when the platform is adopted or changed.
- Someone with statistics training (an analyst or data scientist) reviews the briefs for each team's first 10 experiments: power, randomisation unit and guardrail margins.
- A long-running holdout (for example 1% to 5% of users kept on last quarter's product) for areas where effects build or fade over months, read once a quarter.

### Assured

- **Do not randomise rights or entitlements.** In public services and regulated products, experiment on presentation (wording, layout, order of steps) and service design, never on who receives a benefit, a price, credit or a legal protection. Where a test could affect people's outcomes, get an ethics or legal review first.
- **Fair treatment of customers.** Price and offer tests in financial services, insurance, energy and telecoms can breach consumer protection rules. Agree the allowed scope with compliance and keep the briefs as records. See [regulated industries](../compliance/regulated-industries.md).
- **Analytics under data protection law.** Collect the minimum, check whether consent is needed for analytics cookies or device identifiers in your jurisdiction, pseudonymise identifiers, and set a retention period. See [data security and privacy](../data/data-security-and-privacy.md).
- **Published performance data** for public services, with definitions and method notes, following the service standard that applies.
- **Measure outcomes for groups who struggle.** Report completion rate and time to outcome separately for assisted-channel users and, where lawful, for groups protected by equality law, so an average does not hide a failure.

## When code is cheap to produce

- **More variants do not mean more learning.** Traffic, not build effort, limits how many experiments you can run. Ten variants split the same users ten ways and each needs the full sample. Test fewer, bolder ideas.
- **Measure the cost of what you ship.** Track carrying cost per feature (support contacts, defects, run cost) alongside adoption. Features with low use and rising cost are candidates for removal.
- **AI features need both evals and online metrics.** Offline evals decide whether a change is good enough to release; online metrics such as task success, escalation to a person and user feedback decide whether it helped. See [building with AI](../ai/building-with-ai.md#evals).

## Cloud, on-premises and air-gapped

Hosted analytics and experiment platforms send event data out of your network. Self-host them where data cannot leave, or compute product metrics from your own logs. Software installed on customer sites can only collect usage data the customer has agreed to, and air-gapped installs collect none: rely on support data, structured customer calls and opt-in usage reports exported by the customer's administrator.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Success reported as features shipped or sign-ups | One primary outcome metric with guardrails. |
| Experiment stopped the day it turned green | Fixed duration or a planned sequential method. |
| Results read without checking the split | Sample ratio check first, every time. |
| Twenty metrics, and the winner is whichever moved | One primary metric decides; others are leads. |
| "Inconclusive" read as "it worked" | Write the decision rule before launch, including what inconclusive means. |
| A guardrail with "no significant change" read as safe | A margin for each guardrail; the confidence interval must rule out harm larger than it. |
| A big win from a small test announced as the expected gain | Power the test for the minimum detectable effect; expect small-test wins to shrink at rollout. |
| Users randomised in a business product with 40 customers | Randomise by organisation, count organisations as the sample, or do not run an A/B test. |
| A/B testing who gets a benefit or a price | Test presentation and design only; ethics and legal review. |
| A dashboard with 60 numbers and no owner | Each metric has an owner, a definition and a decision it informs. |

## Templates

- [Experiment brief](../../templates/product/experiment-brief.md)
- [Product one-pager](../../templates/product/product-one-pager.md)
- [Product strategy on a page](../../templates/product/product-strategy-on-a-page.md)

## Sources

- Ron Kohavi, Diane Tang, Ya Xu, *Trustworthy Online Controlled Experiments: A Practical Guide to A/B Testing* (Cambridge University Press, 2020).
- Kerry Rodden, Hilary Hutchinson, Xin Fu, "Measuring the User Experience on a Large Scale: User-Centered Metrics for Web Applications", Proceedings of CHI 2010, ACM.
- Dave McClure, "Startup Metrics for Pirates: AARRR!" (presentation, 2007).
- Alex Deng, Ya Xu, Ron Kohavi, Toby Walker, "Improving the Sensitivity of Online Controlled Experiments by Utilizing Pre-Experiment Data", WSDM 2013, ACM: https://doi.org/10.1145/2433396.2433413
- Ramesh Johari, Pete Koomen, Leonid Pekelis, David Walsh, "Peeking at A/B Tests: Why It Matters, and What to Do About It", KDD 2017, ACM: https://doi.org/10.1145/3097983.3097992
- Henning Hohnhold, Deirdre O'Brien, Diane Tang, "Focusing on the Long-term: It's Good for Users and Business", KDD 2015, ACM.
- Andrew Gelman and John Carlin, "Beyond Power Calculations: Assessing Type S (Sign) and Type M (Magnitude) Errors", Perspectives on Psychological Science 9(6), 2014.
- Eric Ries, *The Lean Startup* (Crown Business, 2011).
- UK Government Service Standard, point 10: https://www.gov.uk/service-manual/service-standard
