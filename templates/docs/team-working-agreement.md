# Team working agreement

How our team works. Write it together, keep it to one or two pages, and review it every quarter at a retrospective. Replace every value in brackets with your own. The numbers are starting points from the Open Engineering Playbook; change them when the team agrees.

| Field | Value |
|---|---|
| Team | [name] |
| Members | [names and roles] |
| Last reviewed | [date] |
| Next review | [date, at most 3 months later] |

## 1. Hours and availability

- Core hours when everyone is reachable: [for example 10:00 to 15:00, time zone]
- Outside core hours, nobody is expected to reply to messages until their next working day.
- On-call is the only out-of-hours duty. Rotation: [link]. See [on-call](../../playbook/reliability/on-call.md).
- Time back: after out-of-hours work or a crunch, take equivalent time off within 2 weeks.

## 2. Communication

| Need | Channel | Expected response |
|---|---|---|
| Urgent production issue | [pager or incident channel] | Immediately, by on-call |
| Blocked, need help today | [team channel, mention the person] | Within 2 working hours |
| Question or review request | [team channel or pull request] | Within 1 working day |
| Decision that affects others | Written proposal, [RFC or decision record](../../playbook/architecture/decision-records.md) | Comments within 3 working days |

Decisions are written down where everyone can find them: [link].

## 3. How work flows

- Cadence: plan every [1 or 2] weeks, show working software every [2] weeks, retrospective every [2] weeks.
- Board: [link]. Work in progress limit for "in progress": [number, at most the number of people].
- Interrupt handler this week takes support questions and unplanned requests: [rotation link].
- Capacity split agreed with product: [60]% roadmap, [20]% maintenance and debt, [20]% unplanned.
- Forecasts are ranges with a confidence level, from throughput. See [planning and forecasting](../../playbook/ways-of-working/planning-and-forecasting.md).

## 4. Definition of done

A change is done when:

- [ ] It is merged to `main` through a reviewed pull request.
- [ ] Automated tests cover the new behaviour at the right level. Bug fixes include a test that failed before the fix.
- [ ] CI is green, including security checks.
- [ ] It is deployed to production, or behind a flag in production with a rollout plan.
- [ ] Logs, metrics and alerts cover the new behaviour.
- [ ] Docs, runbook and changelog are updated where users or operators will notice.
- [ ] Accessibility checked for user interface changes.
- [ ] The product owner has seen it working.

## 5. Code review

- Pull requests aim for under about 400 changed lines.
- First response within 1 working day; re-review within 4 working hours.
- Comments are labelled: `blocking:`, `question:`, `suggestion:`, `nit:`, `praise:`, `follow-up:`.
- The author owns every line, including code produced with tools or code assistants.
- See [code review](../../playbook/delivery/code-review.md).

## 6. Quality and production

- `main` is always releasable. If it breaks, the person who broke it fixes or reverts within 30 minutes.
- Flaky tests are quarantined within 24 hours and fixed or deleted within 14 days.
- When a release misbehaves, roll back first, investigate second.
- Every incident gets a blameless review. See [postmortems](../../playbook/reliability/postmortems.md).

## 7. Meetings and focus

- Recurring team meetings take at most [10]% of the week.
- Focus blocks: [for example 09:00 to 11:00 and 14:00 to 16:00] without meetings.
- Meeting-free day: [day, or none].
- Every meeting has an agenda in the invite and written notes after it.

## 8. Retrospective rules

- At most 2 actions per retrospective, each with an owner and a date.
- The next retrospective starts by checking those actions.

## 9. How we change this agreement

Anyone can propose a change at any time. Changes are agreed at a retrospective. If someone cannot follow the agreement, they say so early, and we adjust it rather than ignore it.
