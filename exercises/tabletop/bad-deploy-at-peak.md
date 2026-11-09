# Tabletop: bad deploy at peak

A release goes out twenty minutes before your biggest sale of the year, checkout starts failing, and the rollback does not work because the database changed underneath it. This scenario tests the roll back or roll forward decision under a time limit, why schema and code changes travel separately, what to do when you have already sold the same seat twice, and how an error budget policy holds up when product wants to ship again on Monday.

| | |
|---|---|
| Audience | Delivery team engineers, on-call engineers, tech leads, the product owner, the engineering manager. Customer support and a senior executive for the later injects. |
| Time | 75 minutes (10 brief, 45 play, 20 debrief) |
| Read first | [Rollbacks](../../playbook/reliability/rollbacks.md), [database changes](../../playbook/delivery/database-changes.md), [feature flags](../../playbook/delivery/feature-flags.md), [service levels](../../playbook/reliability/service-levels.md) |
| Facilitator notes | [Facilitator guide](facilitator-guide.md) |

## Setup

The organisation is an online ticketing company that sells concert and sports tickets in four countries. It has 45 engineers in six teams and deploys about 15 times a day. Today at 10:00 tickets go on sale for a stadium tour; 180,000 people are waiting in the virtual queue. The checkout service has an SLO of 99.9% of requests succeeding over 28 days.

At 09:41 a deployment went out. It contained a new seat-hold algorithm and a migration that renamed the column `hold_expires_at` to `hold_expiry`. The pull request had one approval and green CI. There is no rule against deploying on sale mornings. All organisations, people and numbers here are fictional.

## Injects

### T+0 (Friday 10:02): checkout fails

The fast-burn alert fires: 18% of checkout requests return errors and p95 latency is 4 seconds. The queue is letting 2,000 people a minute into checkout. Support chat is filling up. The deployment log shows the 09:41 release as the only change in the last 3 hours. Looking back, a small number of errors started at 09:42 during the rollout; traffic was low, so the alert stayed under its threshold.

**Decide:**
- Severity and incident commander. Who are the operations lead and the communications lead?
- Roll back, roll forward, or pause the queue? Apply the rule in [rollbacks](../../playbook/reliability/rollbacks.md#roll-back-or-roll-forward).
- Is there a faster lever than a deployment? (Hint: is the new seat-hold logic behind a flag?)

### T+15 (10:17): the rollback fails

The team redeploys the previous image. It crash-loops: the old code reads `hold_expires_at`, which no longer exists. The author of the change says: "I can fix it forward in 10 minutes, I know exactly what is wrong."

**Decide:**
- Do you allow the fix forward? Under what time limit? Who enforces it?
- Can you restore the column without a rollback of the data, for example by adding it back as a view or a duplicate column?
- Do you pause the queue while you decide? Who has the authority to pause a sale?

### T+30 (10:32): the shortcut and the double sale

The fix-forward pull request is ready. CI takes 25 minutes. A senior engineer proposes patching the running containers by hand to skip CI. Meanwhile the data team finds 340 seats sold to two different buyers. The concert promoter's operations director phones: "How many, and what are you telling the fans?"

**Decide:**
- Skip CI or not? If yes, what is the minimum check you still run, and who approves the break-glass?
- Who owns the double-sold seats: engineering, support or the promoter? What happens to the second buyer?
- What does the status page say now?

### T+60 (11:02): the error budget

Checkout is stable again at 10:51. The incident spent about three times the checkout service's whole 28-day error budget. The written error budget policy says: when the budget is exhausted, pause feature releases for that service; the pause ends when the postmortem's priority actions are done and the 7-day burn rate is below 1, or when the 28-day SLO is met again. On the rolling window, the SLO is not met again until about four weeks from now. The product owner wants to ship the new seat-hold algorithm, fixed, before Monday's on-sale for another tour.

**Decide:**
- Does the policy apply? Which exit can the team reach before Monday? Who decides, and by when?
- What would have to be true for Monday's release to go ahead?
- What is the next external update, and when?

### Optional injects

- **T+5:** An engineer finds a feature flag called `sh2_enabled`. Nobody is sure what it controls or whether turning it off is safe.
- **T+45:** A popular fan account posts that the company "sold fake tickets" and it starts trending.
- **T+10:** The checkout dashboards go blank. The metrics backend is overloaded by the spike in error logs. What do you decide from, and who checks that the monitoring itself is working?
- **T+75:** The CEO asks the engineering manager for the name of the person who approved the deployment.

## Discussion questions

1. Could your last ten releases be rolled back in under 15 minutes? Which could not, and why?
2. Do you ever ship a schema change and the code that needs it in the same release?
3. Is every risky feature behind a flag with a clear name and a known safe state?
4. When was your last rollback drill, and how long did it take?
5. Who has the authority to pause a sale, a campaign or a launch?

## What good looks like

- Decision to roll back or roll forward within 15 minutes of declaring the incident, without waiting for proof that the release caused it, with a 30-minute limit on fixing forward, enforced by the commander ([rollbacks](../../playbook/reliability/rollbacks.md)).
- New behaviour behind a [feature flag](../../playbook/delivery/feature-flags.md) with a clear name; turning it off is the first lever.
- Schema changes shipped separately using expand and contract, so the previous version always runs against the current schema ([database changes](../../playbook/delivery/database-changes.md)).
- Break-glass used only through a named group, with review afterwards, not as a habit ([code review: Assured](../../playbook/delivery/code-review.md#assured)).
- Impact on customers handled as part of the incident: double sales counted, owner named, promoter informed.
- The error budget policy applied as written, with product and engineering both signed up to it ([service levels](../../playbook/reliability/service-levels.md)).
- A blameless postmortem: the question is why a rename could ship with the code on a sale morning, and why the first errors at 09:42 did not page, not who approved it ([postmortems](../../playbook/reliability/postmortems.md)).

## Scoring rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Speed of decision | No roll back or forward decision by T+30 | Decided, no time limit | Decided by T+15 with a time limit and an owner |
| Use of levers | Only redeploys considered | Queue paused or flag found late | Flag, queue pause and schema workaround considered in order of speed |
| Change safety under pressure | CI skipped without approval | Skipped with approval but no check | Minimum checks defined; break-glass logged and reviewed |
| Customer impact | Double sales unnoticed | Noticed, no owner | Counted, owned, promoter and fans told |
| Error budget policy | Ignored | Debated, unresolved | Applied, or exception decided by the named owner with conditions |
| Blameless culture | Individual named as cause | Mixed | Conditions discussed; CEO question redirected to the system |

Maximum 12.

## Follow-up actions

- Add a CI check that blocks migrations which rename or drop columns in the same release as code changes ([database changes](../../playbook/delivery/database-changes.md)).
- Put new behaviour behind flags with descriptive names, an owner and a documented safe state.
- Run a timed rollback drill for checkout this month, including the database step.
- Agree a release window policy for major on-sales, and who can pause a sale.
- Use canary releases with automatic rollback on SLO burn ([GitOps and deployment](../../playbook/delivery/gitops-and-deployment.md)).
- Write the postmortem with the [template](../../templates/docs/postmortem.md) within 5 working days.
