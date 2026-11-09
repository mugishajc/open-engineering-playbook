# Running a tabletop exercise

A tabletop exercise is a rehearsal of a bad day, run around a table or a video call, with nothing touched in production. A facilitator reads out a scenario, then adds timed events called injects, and the players decide what to do with the information they have at that moment. Run one every quarter: the first real ransomware attack, region outage or regulator deadline is a poor time to discover that nobody knows who decides.

## What you need

| Item | Detail |
|---|---|
| Time | 90 minutes for most scenarios: 10 to brief, 60 to play, 20 to debrief. Leadership scenarios can run in 60. |
| People | 4 to 10 players, plus a facilitator, a scribe and, ideally, one observer |
| Room | A room or call with no laptops open on production. One shared screen for the scenario. |
| Materials | The scenario page, printed injects (one per card), the [incident update template](../../templates/docs/incident-update.md), your real escalation list and your real runbooks |
| Output | A decision log, a scored rubric and 3 to 7 follow-up actions with owners and dates |

Use your real documents. The exercise tests your runbooks, contact lists and decision rights, not a fictional set. If a document does not exist, that is the first finding.

A tabletop tests decisions; it does not test the system. To check that a failover, rollback or degraded mode works, run a game day that injects a real fault (see [resilience testing](../../playbook/reliability/resilience-testing.md)). A good pattern is a tabletop one quarter and a game day on the same scenario the next.

## Roles

| Role | Does | Does not |
|---|---|---|
| Facilitator | Reads the scenario and injects, keeps time, asks "what do you do now?", plays every outside party (journalist, regulator, vendor, angry customer) | Play, hint at the answer, or let one voice dominate |
| Players | Act in their real roles. Decide with what they know. Say out loud who does what. | Pretend to have information that has not been given |
| Incident commander | One player, named before T+0. Runs the response as they would for real. | Debug or draft messages themselves during a SEV1 |
| Scribe | Records every decision, owner and time in the decision log. Records open questions. | Judge or filter what is important |
| Observer | Watches how the group works: who decided, what was missed, where people waited. Speaks only in the debrief. | Join the play |

In a team of five, the facilitator can also be the observer, and one player can scribe. Rotate the incident commander role between exercises so more people practise it (see [incident management](../../playbook/reliability/incident-management.md)).

## Timing

| Phase | Minutes | What happens |
|---|---|---|
| Brief | 10 | Rules, roles, the starting situation. Confirm who is incident commander. |
| T+0 to T+60 (or later) | 50 to 70 | Injects arrive at the times in the scenario. The clock in the room is the scenario clock. |
| Hot wash | 5 | Each player says one thing that worked and one thing that worried them. No discussion. |
| Debrief | 15 to 20 | The format below |

The facilitator may compress time ("it is now 03:40, nothing new has happened") or skip an inject that the group has already handled. Do not extend the exercise because the group is struggling. A missed decision is a finding, not a failure.

## Injects

An inject is a new piece of information that changes the situation: a call from a journalist, a second system failing, a vendor that stops replying, a regulator's clock that started an hour ago. Each scenario lists its injects at T+0, T+15, T+30, T+60 and sometimes later.

- **Deliver them as cards or messages,** not as a discussion. Read the inject, hand it to the person who would receive it in real life, and start the clock.
- **Play the outside parties with a straight face.** The journalist wants a quote now. The vendor's account manager is on holiday. The board member asks the same question twice.
- **Add pressure, not chaos.** One inject should force a trade-off the group has not yet faced. Two at once is fine late in the exercise. Five at once teaches nothing.
- **Optional injects** in each scenario let you tune difficulty. Use them with experienced groups.

## Rules for players

1. **No blame.** We are testing the system, the runbooks and the decision rights, not people. Nothing said in the room goes into a performance review.
2. **Decide with what you know.** Real incidents never give complete information. "We need more data" is allowed only with a named person, a time limit and a decision for what to do meanwhile.
3. **Say it out loud.** "I page the database team" counts. Thinking it does not.
4. **Use real names and real tools.** If the runbook says to call someone who left last year, say so.
5. **No fighting the scenario.** "That could never happen to us" is the most useful sentence in the room. Write it down and test it afterwards.
6. **Phones away,** except for the person playing the communications lead, who may draft messages.

## The debrief

Run it immediately, while memory is fresh. Keep it blameless. The [postmortem](../../playbook/reliability/postmortems.md) principles apply: ask "what made that seem reasonable at the time?", not "who got it wrong?".

1. **Score the rubric together** (5 minutes). Each scenario has 5 to 6 criteria scored 0, 1 or 2. Agree a score; if you cannot agree, take the lower one and write down why.
2. **Walk the decision log** (5 minutes). For each decision: how long did it take, who made it, did the right person make it?
3. **Three questions** (5 to 10 minutes):
   - What did we assume that was not true?
   - Where did we wait, and for whom?
   - What would have happened at 03:00 on a holiday, with half these people unreachable?
4. **Compare with "what good looks like"** in the scenario. Gaps become actions.

## Turning findings into actions

- **3 to 7 actions, no more.** Each has one owner, a due date and a link to the finding. Put them in the normal backlog with a `tabletop` label.
- **Prefer actions that fix a class of problem.** "Add Amina's mobile number to the escalation list" fixes one gap. "Check the escalation list every quarter against the HR leavers list" fixes the class. See [root cause analysis](../../playbook/reliability/root-cause-analysis.md).
- **Test the fix.** The next exercise reuses the inject that exposed the gap.
- **Track completion** the same way as postmortem actions. Overdue actions go to the engineering lead's staff meeting.
- **Keep the record.** Decision log, rubric, actions and attendance. At Assured level these are evidence for ISO/IEC 27001:2022 controls 5.24 to 5.30 and for the testing duties in regulations such as the EU Digital Operational Resilience Act.

## Scoring scale

Every rubric uses the same scale.

| Score | Meaning |
|---|---|
| 0 | Not done, or done too late to matter |
| 1 | Done, but late, incomplete or by the wrong person |
| 2 | Done on time, by the right role, and written down |

A total below half the maximum is normal for a first run. Track the score across exercises; the trend matters more than the number.

## Choosing a scenario

| Scenario | Best for | Minutes |
|---|---|---|
| [Ransomware at 2 a.m.](ransomware-at-2am.md) | Engineering, security and executives together | 90 |
| [Cloud region outage](cloud-region-outage.md) | Platform, SRE and product owners | 90 |
| [The chatbot leaks data](chatbot-leaks-data.md) | AI product teams, security, privacy and support | 90 |
| [Actively exploited vulnerability: the CRA clock](actively-exploited-vulnerability-cra-clock.md) | Product security, engineering and legal at software makers selling in the EU | 90 |
| [Bad deploy at peak](bad-deploy-at-peak.md) | Delivery teams and on-call engineers | 75 |
| [Key engineer resigns](key-engineer-resigns.md) | Engineering managers and team leads | 60 |
| [Supplier breach](supplier-breach.md) | Security, procurement, legal and IT | 90 |
| [The quantum question from the board](quantum-question-from-the-board.md) | CTO, CISO and executive team | 60 |

For leaders, read [crisis leadership](../../leaders/crisis-leadership.md) before the ransomware, supplier and region outage scenarios, and [decision making](../../leaders/decision-making.md) before the quantum scenario.
