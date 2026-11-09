# Experiment brief: [short name]

<!--
How to use: complete sections 1 to 7 and get a review from someone outside the team before any user sees a variant.
Do not change sections 2 to 7 after launch. Fill in section 8 at the end and add the brief to the shared experiment log, whatever the result.
If section 1 shows an A/B test cannot answer the question, stop here and record the method you will use instead.
Guidance: playbook/product/product-metrics-and-experiments.md. Method: Kohavi, Tang and Xu, Trustworthy Online Controlled Experiments (2020).
-->

| Field | Value |
|---|---|
| Owner | [name, team] |
| Reviewer (outside the team) | [name, date reviewed] |
| Feature flag | [flag name, type: experiment] |
| Planned start and end | [YYYY-MM-DD to YYYY-MM-DD, whole weeks] |
| Compliance or ethics review needed? | [no / yes: reviewer and date] |

## 1. Why we are running this

- Evidence that led here: [research, data, links]
- Decision this experiment informs: [...]
- Could the result change the decision? [yes / no: if the change is required by law, security or accessibility, ship it and monitor instead]
- Is an A/B test the right method? Tick each that is true:
  - [ ] We will have enough units (users or organisations) for the sample size in section 5
  - [ ] Users in one variant do not affect users in the other (no shared marketplace, workspace or stock)
  - [ ] The primary metric moves within the test period, or a leading indicator is known to predict it
  - [ ] The variants do not change anyone's price, credit, benefit or legal protection

## 2. Hypothesis

Because we saw [evidence], we believe that [change] will [increase or decrease] [primary metric] for [users].

## 3. Metrics

| Role | Metric | Definition and source | Baseline | Decision line |
|---|---|---|---|---|
| Primary (decides the result) | [...] | [...] | [...] | [up or down, by at least the minimum detectable effect] |
| Guardrail: trust | [for example error rate, p95 latency] | [...] | [...] | margin: confidence interval must rule out a rise bigger than [x] |
| Guardrail: user | [for example support contacts, complaints, opt-outs] | [...] | [...] | margin: confidence interval must rule out a rise bigger than [x] |
| Secondary (leads only, not deciding) | [...] | [...] | [...] | [none: reported, not decided on] |

## 4. Design

| Item | Value |
|---|---|
| Randomisation unit | [user, account, organisation, session] |
| Analysis unit | [the same as the randomisation unit; if users within organisations, say how clustering is handled] |
| Split | [for example 50/50] |
| Number of variants including control | [2 is the default; each extra variant needs its own full sample] |
| Eligible population | [who can enter, who is excluded and why] |
| Segments to report (named now) | [for example new and returning users] |
| Variants | [control: current; treatment: description] |

## 5. Sample size and duration

| Item | Value |
|---|---|
| Baseline rate, or mean and standard deviation from the last 4 weeks | [...] |
| Minimum detectable effect (smallest change worth its build and carrying cost) | [absolute, for example 1 percentage point; and relative, for example 10%] |
| Power and significance level | [80% power, 5% two-sided; divide 5% by the number of treatment variants if more than one] |
| Units per variant | [n = 16 x variance / effect squared for one treatment at 5%; use a calculator for an adjusted significance level] |
| Variance reduction | [none / CUPED using the metric from the [N] weeks before the test] |
| Extreme values | [rule for capping, for example revenue capped at the 99.9th percentile; or not applicable] |
| Eligible units per week | [...] |
| Duration | [whole weeks, at least 1, usually 2 or more] |
| Analysis method | [fixed horizon, read once at the end / named sequential method with planned looks, set up before launch] |

If the duration is longer than the decision can wait, change the design (bolder change, more sensitive metric, variance reduction) or use another method. Do not run an underpowered test and read it as a result: a win from a small test overstates the real effect.

## 6. Decision rule

| Result | We will |
|---|---|
| Primary metric improves, confidence interval excludes zero, effect at least worth its carrying cost, guardrails pass their margins | [ship to 100%, keep a holdout of [x]% for [period] if the effect may fade, then remove the flag] |
| Primary metric improves but the effect is too small to matter | [for example do not ship; record] |
| No significant change | [for example stop; do not ship; record what we learned. Do not extend the test to "find" significance] |
| Primary metric worsens, or a guardrail fails its margin | [stop and roll back] |
| A guardrail breach during the test | [stop at once; stopping for harm needs no statistical test] |

## 7. Checks before reading results

- [ ] Sample ratio check passed (p-value of the split test above 0.001)
- [ ] Planned duration reached; no early stopping for a win unless a sequential method was planned
- [ ] Logging verified for both variants
- [ ] Effect plotted by day and by days since first exposure to look for novelty or primacy effects
- [ ] Results that look too good checked for bugs before anyone announces them

## 8. Result (after the end date)

| Item | Value |
|---|---|
| Units per variant | [...] |
| Primary metric: effect and 95% confidence interval | [...] |
| Guardrails: effect, interval and margin | [passed / failed: which] |
| Decision | [ship / iterate / stop] |
| What we learned | [...] |
| Link in the experiment log | [...] |
