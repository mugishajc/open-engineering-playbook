# Planning and forecasting

The problem: "Our estimates are always wrong, and every date we give becomes a promise we break." Estimating each task in hours or story points takes time and still misses, because most delay comes from waiting, interruptions and discovered work, not from slow typing. Forecast from what the team has actually finished (throughput), give dates as ranges with a stated confidence, and re-forecast every week. Spend the time saved on splitting work small and removing waits.

Code assistants shorten typing, not waiting, so throughput-based forecasting matters more as they spread. [Agile in the AI era](agile-in-the-ai-era.md) covers how planning changes when the bottleneck moves to framing, review and verification.

## Outcomes

Starting targets. Tune them after a quarter of data.

| Signal | Starting target |
|---|---|
| Forecasts given as a range with a confidence level | 100% of dates shared outside the team |
| Forecast re-run | Weekly, and whenever scope changes |
| Delivery inside the 85% forecast range | About 85% of the time (if it is much higher, your ranges are too wide) |
| Work items that finish within the team's service level expectation | At least 85% |
| Time spent in estimation meetings per engineer | Under 1 hour per 2 weeks |
| Capacity reserved for reliability, debt and unplanned work | Agreed and visible, at least 20% |

## Why points and velocity fail as forecasts

- Story points are a team-local unit. They drift over time and inflate when velocity becomes a target. They cannot be compared across teams.
- Estimates measure effort; delivery time is dominated by waiting (for review, for another team, for a decision) and by work nobody knew about at the start.
- The Scrum Guide does not require story points or velocity. They are an optional technique, not part of Scrum.
- Throughput (items finished per week) already includes waiting, interruptions and discovered work, because it is measured on real outcomes.

## Practice

### Foundation

- **Right-size, do not estimate.** Split each work item until the team agrees it can be done in a few days (for example under 5 working days). Then count items instead of adding up points. A team's question becomes "is this small enough?", which takes seconds.
- **Track two numbers** from your board: throughput (items finished per week) and cycle time (start to done for each item).
- **Use Little's Law to see the cost of WIP.** On average, cycle time equals work in progress divided by throughput. Starting more work without finishing more makes everything slower.
- **Ranges, not dates.** Say "between 3 and 6 weeks, 85% likely", not "in 4 weeks".
- **Now, Next, Later** roadmap instead of a dated Gantt chart for anything more than one quarter out.

### Standard

- **Monte Carlo forecast.** Answer "when will these N items be done?" by replaying your own history thousands of times:

```python
import random

def forecast_weeks(weekly_throughput, items_left, runs=10_000):
    """weekly_throughput: items finished in each of the last 8 to 12 weeks."""
    results = []
    for _ in range(runs):
        done, weeks = 0, 0
        while done < items_left:
            done += random.choice(weekly_throughput)
            weeks += 1
            if weeks > 520:  # stop if history has too many zero weeks
                break
        results.append(weeks)
    results.sort()
    return {p: results[int(runs * p / 100) - 1] for p in (50, 85, 95)}

print(forecast_weeks([4, 6, 3, 5, 0, 7, 4, 5, 6, 3], items_left=40))
```

  Read the result as "50% likely within X weeks, 85% within Y, 95% within Z". Share the 85th percentile by default. Add a buffer for scope growth: if past projects grew by a third after they started, multiply items left by about 1.3, and say so.
- **Service level expectation.** From your cycle time history, publish "85% of items finish within N days". Look at any item older than N days at the daily sync.
- **Weekly re-forecast.** Run the forecast every week and share changes early. A forecast that moves is information, not failure.
- **Quarterly planning on outcomes.** Agree 2 to 4 outcomes per team per quarter (for example "cut failed sign-ups by half"), not a list of features. Link them to the [technical strategy](../strategy/technical-strategy.md).
- **Capacity split.** Agree with product a visible split in the four categories from [portfolio and capacity](../strategy/portfolio-and-capacity.md), for example 60% features, 20% reliability (including unplanned and support work), 15% technical debt, 5% platform. Label work items by category and measure the real split monthly. If unplanned work alone takes more than its share two months running, forecast with the lower feature capacity rather than hoping it falls.
- **Dependencies.** For work that needs another team, agree a date for their part first and forecast your part from that date. Reduce dependencies through [team topology](../operating-model/team-topology.md) rather than through planning meetings.

### Assured

- Contracts and public-sector programmes often need fixed dates. Share forecasts with confidence levels and record each re-forecast and its reason, so the change history is auditable.
- Report against outcomes and forecast ranges in programme governance, not against percent-complete of a task list.
- Where procurement rules require a fixed scope, split it into small releases with acceptance at each one.

## When estimates still help

| Situation | Use |
|---|---|
| Deciding whether something is worth doing at all | A rough size (days, weeks, months) for a cost and value conversation |
| Comparing options | Relative size, quickly, in one meeting |
| A first project with no history | Expert ranges, replaced by throughput data after 4 to 6 weeks |
| Fixed-price bid | Ranges plus explicit assumptions and risk contingency |

## Cloud, on-premises and air-gapped

Forecasting works the same everywhere. Teams in air-gapped networks should include import and approval wait times for new dependencies in their cycle time, since these waits are real and often long.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Two-hour estimation meetings every sprint | Right-size items. Count them. |
| Velocity as a team target | Points inflate. Track throughput and cycle time, not as targets. |
| A single-date forecast | Range with a confidence level. |
| Forecast once, never updated | Weekly re-forecast. |
| Planning 100% of capacity on features | Reserve capacity for maintenance and unplanned work. |
| Padding every estimate quietly | Show the range openly and explain the risk. |

## Templates

- [Team working agreement (planning cadence, WIP limits)](../../templates/docs/team-working-agreement.md)
- [Business case](../../templates/strategy/business-case.md)

## Sources

- John D. C. Little, "A Proof for the Queuing Formula: L = λW", Operations Research 9(3), 1961.
- The Kanban Guide (service level expectation, flow metrics): https://kanbanguides.org/
- The Scrum Guide (2020): https://scrumguides.org/scrum-guide.html
- Daniel S. Vacanti, *Actionable Agile Metrics for Predictability* (2015).
- DORA metrics: https://dora.dev/guides/dora-metrics-four-keys/
