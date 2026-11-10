# Developer experience

Developer experience (DX) is a continuous program, not a one-off survey. It measures how easy it is for engineers to do their work, identifies the friction that slows them down, and tracks whether improvements land. A team with good DX ships faster, makes fewer errors and keeps its people. A team with bad DX loses engineers to companies that fix the friction.

## Outcomes

Starting targets. Tune them after two quarters of data.

| Signal | Starting target |
|---|---|
| DX survey response rate | At least 70% each quarter |
| Time from survey to published results and planned actions | Under 3 weeks |
| Actions completed from the previous quarter's survey | At least 2 per team |
| Environment setup time for a new engineer (clone to first passing test) | Under 2 hours |
| Local build time (incremental, after one file change) | Under 30 seconds |
| CI pipeline time (push to green) | Median under 10 minutes |
| Time to first merged pull request for a new hire | Under 2 weeks |
| Developer satisfaction score (quarterly, same scale) | Trending up or stable above 7 out of 10 |

## Practice

### Foundation

Run a quarterly developer experience survey with fixed questions. Use the same questions every quarter so you can trend the results. Keep it short: 15 to 20 questions, under 10 minutes to complete.

**What to ask.** Cover these dimensions:

| Dimension | Example question |
|---|---|
| Satisfaction | "I would recommend my team's development setup to a friend joining the company" (agree/disagree scale) |
| Flow and focus | "How often in the past week were you able to work for 2 hours without interruption?" |
| Cognitive load | "How hard is it to make a change to the service you work on most?" (Team Topologies question, 1-5 scale) |
| Tool friction | "Which tool or process caused you the most friction this week?" (open text) |
| Build and test | "How long does your local build take after a one-file change?" |
| Onboarding | "How many days did it take you to make your first meaningful contribution?" |

**Own the results.** Assign a DX owner: a person or a small team who publishes the results within 3 weeks, picks the top 2 to 3 friction points, and tracks fixes to completion. Without an owner, surveys become data that nobody acts on.

**Connect to delivery metrics.** Pair the survey with DORA delivery metrics (deployment frequency, lead time for changes, change fail rate, failed deployment recovery time, rework rate). Subjective experience and objective delivery tell different stories. A team can ship fast and hate their tools. Both matter.

### Standard

Adopt a structured DX framework. Two are widely used:

- **SPACE** (Satisfaction, Performance, Activity, Communication and collaboration, Efficiency and flow). Published by Microsoft Research, GitHub and the University of Victoria in 2021. SPACE gives five dimensions and warns against using any single metric.
- **DX Core 4.** Published by getdx.com in December 2024. DX Core 4 combines DORA delivery metrics with developer experience signals into a single framework. It was designed to work alongside AI adoption, where raw activity metrics (commits, lines changed, pull requests opened) become unreliable because tools generate a large share of the output.

**Activity metrics in the AI era.** When code assistants and agents generate a large share of commits, lines changed and pull requests opened, activity counts stop measuring developer productivity and start measuring tool throughput. Weight satisfaction, flow state and the ability to focus over raw activity counts. Track rework rate (the share of deployments that are unplanned fixes) as the quality signal that generation volume alone hides.

**Measure the environment, not just the opinion.** Instrument what you can:

| Metric | How to collect | Target |
|---|---|---|
| Environment setup time | Script the setup and time it on a clean machine | Under 2 hours |
| Incremental build time | CI telemetry or local timer | Under 30 seconds |
| Test suite time (full, local) | CI telemetry | Under 5 minutes |
| CI pipeline time (push to green) | CI telemetry | Median under 10 minutes |
| Deploy time (merge to production) | Deployment telemetry | Under 1 hour (Standard) |
| Time to first merged PR (new hire) | Git log | Under 2 weeks |
| Onboarding time (self-assessed "productive") | Survey | Under 1 month |

**Act on the results.** Each quarter, publish: the survey results (anonymised), the top 3 friction points, the actions taken since last quarter, and the next actions. Share it with the whole engineering organisation. A survey that disappears into a spreadsheet is worse than no survey, because it teaches engineers that feedback changes nothing.

### Assured

Run a formal DX program with budget, headcount and executive sponsorship.

- **DX team or platform DX function.** A team whose job is to fix the friction that the survey and instrumentation surface. This can be the developer platform team, or a dedicated DX team that works across platform, tooling and process.
- **Quarterly business review.** Present DX trends to engineering leadership alongside delivery metrics. Show the link: when DX improved, did throughput or retention follow? When it dropped, did attrition or change fail rate rise?
- **Retention correlation.** Track whether engineers who report low DX scores leave at a higher rate. This makes the business case for investment.
- **Benchmarking.** Compare your scores to industry benchmarks (DX Core 4 and similar frameworks publish benchmark data). Use benchmarks to set targets, not to rank teams against each other.
- **Continuous instrumentation.** Automate the collection of environment, build, test and deploy times. Alert when a metric degrades beyond a threshold (for example, CI time crosses 15 minutes). Treat DX regressions like production regressions.

## Cloud, on-premises and air-gapped

The survey works everywhere. Instrumentation varies: cloud teams get CI telemetry from hosted runners, on-premises teams instrument their own runners, and air-gapped teams may need to export timing data manually. The setup-time target may be longer in air-gapped environments where downloads are restricted. Adjust the target, not the practice.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Survey once a year | Quarterly, same questions, same scale. Annual surveys are too slow to show whether fixes worked. |
| Survey without action | Publish results and actions within 3 weeks. Cancel the survey if nobody acts on it. |
| Using activity metrics to rank engineers | Activity metrics measure tool throughput, not people. Use them at team level to spot bottlenecks, never to rate individuals. |
| DX is the platform team's problem only | DX spans tooling, process, documentation, team design and management. The platform team owns some of it. The DX owner coordinates all of it. |
| Measuring everything, fixing nothing | Pick the top 2 to 3 friction points per quarter. Fix them. Measure again. |
| Treating satisfaction as vanity | Developer satisfaction predicts retention. Retention predicts delivery capacity. The link is well documented. |

## Templates

- [Developer experience survey template](../../templates/docs/developer-experience-survey.md) (if available)
- [Quarterly DX report template](../../templates/docs/quarterly-dx-report.md) (if available)

## Sources

- Forsgren, Storey, Maddila, Zimmermann, Houck, Butler. The SPACE of Developer Productivity. ACM Queue, 2021: https://queue.acm.org/detail.cfm?id=3454124
- DX Core 4, getdx.com (December 2024): https://getdx.com/research/measuring-developer-productivity-with-the-dx-core-4
- Noda, Storey, Forsgren, Greiler. DevEx: What Actually Drives Productivity. ACM Queue, 2023: https://queue.acm.org/detail.cfm?id=3595878
- Team Topologies cognitive load assessment: https://teamtopologies.com/key-concepts
- DORA metrics: https://dora.dev/guides/dora-metrics-four-keys/
