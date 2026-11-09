# First 90 days

Spend the first 30 days listening and measuring, the next 30 diagnosing and securing a few early wins, and the last 30 publishing a one-page technical strategy that the organisation can act on. Change little in the first month except what is unsafe. Acting on a diagnosis you have not checked costs more credibility than moving a few weeks later.

This page is for a new CTO, CIO, head of engineering or chief architect, whether hired from outside or promoted. Michael Watkins's The First 90 Days (2003) argues that the right plan depends on the situation you inherit; the paths below adapt the plan to turnaround, scale-up and public-sector appointments.

## When to use this

- You start a technology leadership role in the next month, or started in the last one.
- You are an interim leader asked to stabilise and hand over.
- You are hiring a technology leader and want to agree what their first 90 days should produce.

## Before day 1

1. Agree with your manager, in writing, what success looks like at day 90 and day 365, and what you have authority to change.
2. Ask for: the last 4 quarters of board or executive reports, the risk register, the budget and run cost, the org chart, the last 5 postmortems, open audit findings, and any strategy documents.
3. Book listening sessions for the first 3 weeks before you arrive.

## Days 1 to 30: listen and measure

### Listening tour

Meet at least 30 people, or everyone if the function has fewer than 30. Include engineers at every level, not only managers. Ask the same questions of everyone so the answers can be compared. Take notes and promise confidentiality for individual answers.

| Group | Questions |
|---|---|
| Engineers and tech leads | What slows you down most in a normal week? What would you fix first if you were me? What is the system everyone is afraid to touch? When did you last ship something you were proud of? |
| Engineering managers | Which teams are healthy and which are struggling, and why? Where are we one resignation away from trouble? What decisions take too long? |
| Product and business leaders | What has technology promised and not delivered? What do customers complain about? What would you stop funding? |
| CISO, risk, audit, compliance | What are the top 3 technology risks? Which audit findings are open, and for how long? What would a regulator ask us tomorrow? |
| Finance | What does technology cost, and is the trend acceptable? Which spend is hardest to explain? |
| Customers or citizens (where possible) | What fails, and how often? What do you work around? |
| Key suppliers | What do we make hard for you? Where is our contract or integration fragile? |
| Your manager and peers | What must not go wrong this year? What did my predecessor get right? |

Close every session with: "What should I not change?"

### What to measure in the first 30 days

Run the [maturity self-assessment](../assessment/README.md) with 3 to 5 engineering leads, answering only what you can see evidence for. It gives you the level reached in each of the 14 practice areas and the gap to your profile's target. Alongside it, collect a baseline you can compare against at day 90 and day 365.

| Area | Baseline |
|---|---|
| Delivery | The five DORA metrics for the most important services (see [metrics](../playbook/measurement/metrics.md)), even if measured by hand |
| Reliability | SLOs that exist and their attainment; SEV1 and SEV2 count over 12 months; open postmortem actions |
| Security | Critical and high vulnerabilities past their fix deadline; date of last restore test; privileged accounts |
| Cost | Run cost by service or platform; spend trend over 12 months |
| People | Attrition over 12 months, open roles, key-person dependencies, on-call load per person |
| Portfolio | Number of active initiatives against number of teams; systems on unsupported software |

If most of your systems are bought or run by suppliers, as in many ministries and non-software firms, you will not have DORA metrics. Measure instead: supplier service level attainment, failed or rolled-back changes per month, contracts ending in the next 18 months, and critical systems that nobody on your own staff can explain.

Do not publish team-level comparisons. The baseline is for diagnosis, not judgement.

## Days 31 to 60: diagnose and secure early wins

Write a diagnosis: the 3 to 5 problems that matter most, each backed by evidence from the listening tour and the baseline. Test it with 5 people you trust, including at least one sceptic, before sharing it widely.

### Early wins versus things not to change too soon

| Early wins (do now) | Leave alone for now (unless unsafe) |
|---|---|
| Fix the top annoyance from the listening tour that costs under 2 weeks | The org structure. Reorganise only after the strategy is written. |
| Close any critical security gap: an untested backup, an exposed admin interface, a shared root credential | Core technology choices such as language, cloud provider or main database |
| Make one decision that has been stuck for months | People's titles and levels |
| Start the weekly metrics review (see [operating rhythm](operating-rhythm.md)) | Processes that work, even if they are not how you did it before |
| Publish decision rights for the 10 most common decisions (see [decision rights](../playbook/operating-model/decision-rights.md)) | Supplier contracts, unless a renewal deadline forces it |
| Stop one initiative that everyone knows is dead | Your predecessor's commitments to the board, until you have discussed them |

An early win is visible, cheap, and supports the strategy you are about to write. A win that contradicts the later strategy costs credibility.

## Days 61 to 90: write the first technical strategy

Write a one-page strategy using [technical strategy](../playbook/strategy/technical-strategy.md): diagnosis, guiding policy and three to seven coherent actions, each with an owner, a date and a measure. Include what you will stop. Present it to your manager and peers, then to the whole function, and invite written challenge for 2 weeks before you finalise it.

By day 90 you should have:

- A published one-page strategy and the first quarter of actions.
- An operating rhythm running (weekly metrics, monthly risk and architecture reviews).
- A baseline you will report against, and targets for day 365.
- A first board or executive report in the format of [board and executive reporting](board-and-executive-reporting.md).
- A view of your leadership team: who stays in role, who needs support, which roles are missing.

## Paths by situation

| | Turnaround | Scale-up | Public-sector appointment |
|---|---|---|---|
| Typical signal | Frequent outages, missed commitments, a failed programme, a serious incident or audit finding | Fast hiring, systems and processes built for a smaller company, rising incidents | Legacy estate, supplier dependence, budget years, assurance gates, ministerial or public scrutiny |
| First 30 days | Shorten listening to 2 weeks. Stabilise first: incident process, backups, the riskiest change paths. | Full listening tour. Measure where growth is breaking things. | Full listening tour, including the senior responsible owner, the finance director, the central digital authority and key suppliers |
| What to do early | Stop work that cannot succeed. Freeze non-essential change to the most fragile systems. Be visible in incidents. | Decision rights, onboarding, golden paths, a hiring plan. Protect the teams that are working. | Map contracts and their end dates, spend controls and assurance gates. Learn the budget calendar. |
| What to avoid | Promising dates before the diagnosis is done | Reorganising in month 1; adding process that slows the teams that work | Announcing a big programme before you understand procurement lead times and the political calendar |
| Strategy horizon | 6 to 12 months, focused on stability | 12 to 24 months, focused on scale | Aligned to the spending review or budget cycle, typically 1 to 3 years |
| Read next | [Crisis leadership](crisis-leadership.md), [incident management](../playbook/reliability/incident-management.md) | [Team topology](../playbook/operating-model/team-topology.md), [golden paths](../playbook/platform/golden-paths.md) | [Public sector](../playbook/compliance/public-sector.md), [IT governance](../playbook/operating-model/it-governance.md) |

## Common mistakes

| Mistake | Fix |
|---|---|
| Arriving with the answer from your last job | Listen first. Write the diagnosis from evidence gathered here. |
| Only meeting managers | Meet engineers at every level, and on-call staff in particular |
| Reorganising in the first month | Strategy first, structure second |
| Criticising the previous leader's decisions in public | Ask what constraints they faced. Most decisions made sense at the time. |
| Too many early wins | Pick 2 or 3 and finish them |
| A 40-page strategy | One page. Detail goes in decision records and business cases. |
| No baseline, so progress cannot be shown | Measure in the first 30 days, even roughly |

## Templates

- [First 90 days plan](../templates/leaders/first-90-days-plan.md)
- [Strategy one-pager](../templates/strategy/strategy-one-pager.md)
- [Operating rhythm calendar](../templates/leaders/operating-rhythm-calendar.md)
- [Stakeholder map](../templates/strategy/stakeholder-map.md)

## Sources

- Michael Watkins, "The First 90 Days", Harvard Business School Press, 2003.
- Richard Rumelt, "Good Strategy Bad Strategy", Crown Business, 2011.
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
- UK NCSC, Board Toolkit: https://www.ncsc.gov.uk/collection/board-toolkit
