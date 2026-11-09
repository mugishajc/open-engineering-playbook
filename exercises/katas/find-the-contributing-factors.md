# Kata: find the contributing factors

Read the timeline of a real-feeling incident and find every condition that made it possible, made it worse or made it last longer. The draft postmortem blames one engineer and one bad rule. Your job is to find what that version misses, group the factors by detection, response and recovery, and write action items that fix a class of failure rather than one line of configuration.

| | |
|---|---|
| Who | One person, a pair, or a postmortem facilitator in training |
| Time | 40 minutes: 25 to analyse, 15 to compare with the answers |
| Practice it teaches | [Root cause analysis](../../playbook/reliability/root-cause-analysis.md), [postmortems](../../playbook/reliability/postmortems.md), [postmortem template](../../templates/docs/postmortem.md) |

## The organisation

A 40-person SaaS company sells scheduling software to clinics. Clinic staff use a web app and a mobile app; the mobile app carries about 70% of daytime traffic. An API gateway applies rate limits from a YAML file in a separate configuration repository. A sync job copies that file to the gateways in all three regions every 30 minutes, or on demand when an administrator triggers it. All organisations, people and numbers here are fictional.

## The timeline (UTC, a Tuesday)

| Time | Event |
|---|---|
| 13:41 | Chen opens a change to the rate-limit file: lower the limit from 600 to 60 requests per minute for one partner whose integration has been flooding the API. The partner's client is identified by its user agent, `okhttp`. |
| 13:58 | Chen merges the change. The configuration repository has no branch protection; code repositories require one review, this one does not. Chen's leave starts at 14:30. |
| 14:00 | The scheduled sync pushes the new file to all three regions at the same time. |
| 14:03 | The mobile app also uses the `okhttp` library and sends the same user agent. Mobile requests start receiving HTTP 429 (too many requests). The app shows "Could not load your schedule". |
| 14:03 | The availability SLO counts only 5xx responses as bad. No alert fires. The API dashboard stays green. |
| 14:21 | First support ticket. The agent sees "too many requests" in the screenshot, assumes the clinic's phone is misbehaving, and suggests reinstalling the app. |
| 14:52 | 40 similar tickets. The support lead posts in the `#engineering` chat channel. Support has no way to page on-call. |
| 15:10 | Ravi, the on-call engineer, finishes a meeting and sees the message. He checks the API servers: CPU at 20%, error rate normal, web traffic normal. |
| 15:34 | Ravi declares a SEV2 and acts as incident commander while he keeps investigating. |
| 15:55 | Ravi searches gateway logs and finds a large rise in 429 responses for `okhttp` clients since 14:03. He finds Chen's merge and messages Chen. No reply. |
| 15:58 | Ravi reverts the commit. The next scheduled sync is at 16:30. Triggering it by hand needs one of two administrators. |
| 16:05 | First status page update: "Some users may experience issues with the mobile app." |
| 16:09 | Ravi reaches Fatima, an administrator, by phone. |
| 16:12 | Fatima triggers the sync. |
| 16:14 | 429 rates return to normal in all regions. Incident resolved at 16:30 after monitoring. |

**Draft postmortem, written by Ravi's manager:** "Root cause: an engineer pushed an untested rate-limit rule. Action: remind engineers to test configuration changes."

## Your tasks

1. Work out how long it took to detect, to declare and to mitigate, measured from 14:03.
2. List the contributing factors. Aim for 6 to 10. Group them under trigger, detection, response and recovery.
3. For Chen's action, write what Chen knew and why the change looked reasonable at the time.
4. Rewrite the draft "root cause" sentence and action.
5. Propose 3 to 5 action items. At least half must fix a class of failure ("all configuration pushes"), not only this rule.
6. Where did the team get lucky?

<details>
<summary>Answer 1: the numbers</summary>

| Measure | From 14:03 to | Duration |
|---|---|---|
| First signal to the company (ticket) | 14:21 | 18 minutes |
| Engineering aware | 15:10 | 1 hour 7 minutes |
| Incident declared | 15:34 | 1 hour 31 minutes |
| Cause identified | 15:55 | 1 hour 52 minutes |
| Mitigated | 16:14 | 2 hours 11 minutes |

No system detected the incident at all. Of the 2 hours 11 minutes, the gap between cause identified and mitigated (19 minutes) was mostly waiting for an administrator.

</details>

<details>
<summary>Answer 2: contributing factors</summary>

**Trigger**
- The rule matched clients by user agent, a value shared by the partner and the company's own mobile app.
- Configuration changes had no required review, unlike code ([code review](../../playbook/delivery/code-review.md)).
- No test or dry run showed which clients a rule would match before it shipped.

**Detection**
- The SLO counted only 5xx responses; 429 responses to legitimate users were invisible ([service levels](../../playbook/reliability/service-levels.md)).
- No alert on a sudden change in 429 rate.
- Support had no route to page on-call; the only path was a chat message.
- Support's first diagnosis blamed the customer's device, a reasonable guess with no signal to the contrary.

**Response**
- On-call was in a meeting and saw the message 18 minutes after it was posted.
- The dashboards Ravi checked first (CPU, 5xx, web traffic) could not show this failure.
- Ravi held incident commander and investigator at once, so nobody updated the status page until 16:05 ([incident management](../../playbook/reliability/incident-management.md)).
- No deployment or change log for configuration in the place Ravi looked first.

**Recovery**
- The configuration went to all three regions at once, with no canary ([GitOps and deployment](../../playbook/delivery/gitops-and-deployment.md)).
- Reverting the commit did not roll back production: the sync ran only on a schedule or by an administrator.
- Only two people could trigger the sync ([rollbacks](../../playbook/reliability/rollbacks.md)).
- The change author left for leave 32 minutes after merging, with no handover expectation for risky changes.

</details>

<details>
<summary>Answer 3: how it made sense at the time</summary>

Chen was solving a real problem: one partner was flooding the API, probably causing slowness for others. The partner's traffic was identifiable by user agent in the logs Chen looked at. Chen did not know the mobile app used the same HTTP library, and nothing in the repository, the rule syntax or the review process would have shown it. The configuration repository had been treated as low risk for years, so merging without review was normal practice, not a shortcut. Leaving for planned leave after a merge is normal; nothing marked this change as one to watch.

</details>

<details>
<summary>Answer 4: a better summary</summary>

"A rate-limit rule intended for one partner matched the company's own mobile app, because both send the same user agent. The change reached all regions at once, no alert counted the resulting 429 responses as failures, and rolling back needed an administrator. Mobile users could not load schedules for 2 hours 11 minutes."

The action "remind engineers to test configuration changes" relies on memory and fixes nothing. Replace it with the items below.

</details>

<details>
<summary>Answer 5: class-level action items</summary>

| Action | Class it fixes | Priority |
|---|---|---|
| Require review and a CI dry run (which clients does this rule match, from the last 24 hours of logs) for every change in the configuration repository | All configuration changes | P1, 2 weeks |
| Roll out every configuration push region by region with a 10-minute canary and automatic stop on error-rate change | All configuration and content pushes | P1, 2 weeks |
| Count 429 responses to authenticated first-party clients as bad events in the SLO; alert on a sudden change in 429 rate | All gateway-generated errors | P2, 6 weeks |
| Let the pipeline apply a reverted commit immediately, without an administrator | All configuration rollbacks | P1, 2 weeks |
| Give support a way to page on-call, with guidance on when to use it | All customer-reported incidents | P2, 6 weeks |
| Identify partner traffic by API key, not user agent | This rule (one-off fix) | P1, 2 weeks |

Five of the six fix a class. The incident is also a reminder of the July 2024 CrowdStrike lesson: configuration and content are changes and need staged rollout.

</details>

<details>
<summary>Answer 6: where they got lucky</summary>

- The web app was not affected, so clinics had a workaround.
- Ravi reached Fatima by phone within 11 minutes. With both administrators unreachable, recovery would have waited until the 16:30 sync.
- The incident happened on a Tuesday afternoon, not during a Monday morning rush when clinics load the week's appointments.

</details>

## Going further

Run the same exercise on your own last SEV2 postmortem. Count how many factors it lists under detection and recovery. If the answer is zero, the analysis stopped at the trigger. The [root cause analysis](../../playbook/reliability/root-cause-analysis.md#techniques) page lists techniques to go further, including fishbone diagrams and CAST.
