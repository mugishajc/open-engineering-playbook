# Metrics

Measure a small set of system-level metrics: the five DORA software delivery metrics, SLO attainment for reliability, and developer experience across several SPACE dimensions. Collect them automatically from the tools you already run, compare each team with its own past rather than with other teams, and use them to choose what to improve next. Never use them to rate individuals: the moment a metric becomes a target for people, it stops telling you the truth.

## Outcomes

Starting points. Tune them to your organisation.

- The five DORA metrics are collected automatically for at least 80% of production services, refreshed at least weekly.
- Every user-facing service reports SLO attainment over a rolling 28-day window.
- A developer experience survey runs every 6 months with a response rate of at least 40%.
- Each quarter, each team picks at most 1 or 2 metrics to improve and reviews them at the end of the quarter.
- No metric in this page appears in an individual's performance review.

## Software delivery: the five DORA metrics

| Metric | Definition | Measures |
|---|---|---|
| Deployment frequency | How often the team deploys to production | Throughput |
| Change lead time | Time from a change being committed to it running in production | Throughput |
| Failed deployment recovery time | Time to recover when a deployment fails and needs immediate action (formerly called mean time to restore) | Throughput |
| Change fail rate | Share of deployments that cause a failure in production needing immediate action (rollback, fix forward, hotfix) | Instability |
| Rework rate | Share of deployments that are unplanned and happen because of an incident in production | Instability |

Throughput and stability move together in DORA's research: teams do not have to trade one for the other. The 2025 DORA report replaced the old low, medium, high and elite tiers with team archetypes, so do not set targets by copying a tier threshold. Set them against your own baseline, for example "halve change lead time in 2 quarters".

## Reliability

- **SLO attainment.** Share of SLOs met over the window, per service and overall. Define SLOs as described in [service levels](../reliability/service-levels.md).
- **Error budget consumed.** Per service, per window. Drives the decision to slow releases or invest in reliability.
- **Incidents by severity** and **time to detect**. Useful for trend, not for comparison between teams.

## Developer experience: SPACE

The SPACE framework (Forsgren, Storey, Maddila, Zimmermann, Houck and Butler, 2021) says productivity has five dimensions and that no single metric captures it. Use at least three dimensions, and mix survey data with system data.

| Dimension | Example measures |
|---|---|
| Satisfaction and well-being | Survey: satisfaction with tools and work, sustainable pace, likelihood to stay |
| Performance | Outcomes: SLO attainment, change fail rate, customer-reported defects |
| Activity | Counts used only as context: deployments, reviews completed. Never alone. |
| Communication and collaboration | Review turnaround time, time waiting on other teams, quality of docs (survey) |
| Efficiency and flow | Change lead time, CI duration, time in review, interruptions per week (survey) |

Keep the survey short: 10 to 15 questions, the same each time, with one free-text question. Publish the results and what you will do about them within 30 days.

## How to collect

| Metric | GitHub | GitLab | On-premises or air-gapped |
|---|---|---|---|
| Deployment frequency | Deployments API or Actions environment deployments | Built-in DORA metrics from environment deployments (check which tier includes them) | Deployment events from the CD tool (Argo CD, Flux, Jenkins) sent to a metrics store |
| Change lead time | Commit timestamp to deployment timestamp, joined on commit SHA | Built-in DORA metrics | Same join, from git server and CD tool events |
| Change fail rate | Deployments linked to incidents, rollbacks or hotfix labels | Incidents linked to deployments | Incident tool records linked to deployment IDs |
| Failed deployment recovery time | Time from failed deployment to the next successful deployment or rollback | Built-in metric based on incidents | Same calculation from CD and incident events |
| Rework rate | Deployments tagged as unplanned and incident-driven (label or commit trailer) | Same, with labels | Same |
| SLO attainment | From the observability stack | Same | Prometheus recording rules and Grafana |
| Developer experience | Survey tool | Survey tool | Self-hosted survey tool |

The open source Four Keys project shows one way to compute delivery metrics from event data. Whatever you use, store raw events, not only aggregates, so you can fix definitions later.

## Rolling up across many teams

With dozens or hundreds of teams, the roll-up is where most reports go wrong.

- **Report medians and the spread** (for example the 25th and 75th percentile) per value stream or division. One very slow or very fast team moves a mean and hides everything else.
- **Never average percentages across teams of very different size.** Compute the rate from the pooled events instead: total failed deployments divided by total deployments.
- **Group by value stream or product**, not by reporting line, so the numbers match how work flows to users.
- **Show coverage.** State what share of services report each metric. A median over 30% of services is a sample, not the organisation.
- **Trend before level.** Leaders act on the direction over 4 quarters; a single quarter's level invites comparison between teams.

## What not to measure

| Do not measure | Why |
|---|---|
| Lines of code | More code is usually more cost. Deleting code is often the best change. |
| Commit or pull request counts per person | Trivially gamed. Encourages splitting work artificially. |
| Story points or velocity across teams | Points are a team's private estimate. Comparing them across teams is meaningless and invites inflation. |
| Individual DORA metrics | They describe systems and teams. Assigning them to people punishes those who take the hard work. |
| Hours online or keyboard activity | Measures presence, not results, and damages trust. |
| Share of code written by assistants | Counts activity. See [code assistants](../people/code-assistants.md) for what to measure instead. |

Goodhart's law, as Marilyn Strathern phrased it in 1997: "When a measure becomes a target, it ceases to be a good measure." Use metrics to start conversations and choose experiments, not to reward or punish.

## In the AI era

Code assistants and agents change how fast code is written. Whether they change outcomes is an empirical question for each team. DORA's 2024 report found AI adoption associated with lower throughput and lower stability; the 2025 report found higher throughput and still more instability. A 2025 randomised trial by METR found experienced open source developers slower with AI tools, although they felt faster. Measure both sides (see [code assistants](../people/code-assistants.md) and [AI engineering practices](../ai/ai-engineering-practices.md)).

| Measure | How | What it tells you |
|---|---|---|
| Team baseline | Record the five DORA metrics for at least one quarter before wider adoption, or use the last two quarters of history | The only fair comparison is a team with its own past |
| Change fail rate and rework rate | As defined above, trended monthly | Whether faster output is reaching production broken |
| Review load | Median pull request size, time in review, review rounds per pull request, reviewer hours | Whether the bottleneck moved from writing code to reading it |
| Cost per change | Assistant and model spend per month divided by deployments to production | Whether spend scales with delivered changes or only with activity |
| Escaped defects | Defects found in production per 100 changes | Quality that tests and review missed |
| Developer survey | Two or three fixed questions each quarter: where the tools save time, where they cost time, confidence in generated code | Effects that system data cannot see, such as skill loss or review fatigue |

Decision rule (starting point): expand use when throughput improves and change fail rate, rework rate and escaped defects stay within 10% of the baseline for two consecutive quarters. If instability rises beyond that, hold expansion and fix review and test practice first.

Do not count lines of code generated, suggestion acceptance rate or "share of code written by AI". They measure activity and are easy to inflate. Do not compare teams with each other, and never attribute these metrics to individuals.

## Practice

### Foundation

- Track deployment frequency and change lead time from your git host and CI. Count failed deployments by hand in a spreadsheet if needed.
- One SLO for the most important user flow.
- Ask the team every quarter: what slowed you down most?

### Standard

- All five DORA metrics collected automatically, per service and team, on a shared dashboard.
- SLO attainment reported for every user-facing service.
- SPACE-based survey every 6 months.
- Quarterly review per team: pick 1 or 2 metrics to improve, choose an experiment, check the result.
- Metric definitions written down and versioned, so a change in definition is not mistaken for a change in performance.

### Assured

- Metrics used in reports to boards or regulators have documented definitions, data sources, owners and retention.
- Raw event data is retained and access-controlled, so figures can be reproduced for an auditor.
- Where employee representatives have rights over systems that can monitor performance or behaviour (for example works councils in Germany), agree metric definitions, aggregation level and retention with them before collection starts. Collect at team level and delete individual event data you do not need.
- Change fail rate and incident data feed [change management](../reliability/change-management.md): low-risk change types with good records can earn lighter approval.

## Cloud, on-premises and air-gapped

- Hosted DORA dashboards need the data to leave your network. On-premises and air-gapped, compute the metrics locally from git, CD and incident events, and store them in your own metrics stack.
- Delivery events carry author names. Pseudonymise or drop them at collection when the metric does not need them.
- Survey tools must meet data protection rules. Use a self-hosted tool where responses cannot leave the network.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Ranking teams by deployment frequency | Compare each team with its own baseline. |
| Dashboards nobody reads | Each metric has an owner and appears in a quarterly review that leads to a decision. |
| Measuring only speed | Always pair throughput with instability metrics and SLOs. |
| Changing the definition silently | Versioned definitions, with a note on the dashboard when they change. |
| Survey results with no follow-up | Publish results and actions within 30 days, or stop running the survey. |

## Templates

- [Postmortem template](../../templates/docs/postmortem.md), which feeds incident data

## Sources

- DORA metrics guide: https://dora.dev/guides/dora-metrics-four-keys/
- DORA research programme and reports: https://dora.dev/research/
- METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", July 2025: https://arxiv.org/abs/2507.09089
- Forsgren et al., "The SPACE of Developer Productivity", ACM Queue (2021): https://queue.acm.org/detail.cfm?id=3454124
- Google SRE book, "Service Level Objectives": https://sre.google/sre-book/service-level-objectives/
- GitLab DORA metrics documentation: https://docs.gitlab.com/user/analytics/dora_metrics/
- Marilyn Strathern, "Improving ratings: audit in the British University system", European Review 5(3), 1997
