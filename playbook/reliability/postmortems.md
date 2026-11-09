# Postmortems

Write a blameless postmortem for every serious incident within 5 working days, list the contributing factors, and track every action item to closure. Incidents are expensive lessons that the organisation has already paid for. Teams that skip the write-up, blame a person, or let action items rot pay for the same lesson again.

## Outcomes

Starting points. Tune them to your incident volume.

- 100% of SEV1 and SEV2 incidents have a published postmortem.
- The first draft is shared within 5 working days of resolution; the review meeting happens within 10 working days.
- At least 80% of high-priority action items close by their due date. The rate is reported monthly.
- Repeat incidents (same contributing factor within 6 months) fall quarter on quarter.
- Postmortems are readable by every engineer in the organisation, with redactions only for security or personal data.

## When a postmortem is required

- Every SEV1 and SEV2 incident (see [incident management](incident-management.md)).
- Any incident that spends more than 20% of a service's error budget (see [service levels](service-levels.md)).
- Any security incident and any personal data breach, reportable or not.
- Data loss, a failed restore, or a rollback that did not work.
- A near miss that someone thinks is worth learning from. Anyone may request one.

## Principles

1. **Blameless.** Ask "what made this action seem reasonable at the time?", not "who did this?". People act on the information, tools and pressure they had. Fix those. A blamed engineer stops reporting near misses, and the organisation goes blind.
2. **Contributing factors, not one root cause.** Incidents in complex systems have several causes that combined. A single "root cause" hides the others. List every factor that made the incident possible, worse or longer: the change, the missing test, the alert that did not fire, the runbook that was out of date, the deadline. [Root cause analysis](root-cause-analysis.md) describes the techniques.
3. **Timeline in UTC** from the first signal, not from the first page. The gap between them is often the most useful finding.
4. **Include what went well and where you got lucky.** Luck is a warning: next time it may not be there.
5. **Accountability is for the action items, not for the incident.** Each action has one owner and a date.

## Practice

### Foundation

1. Use the [postmortem template](../../templates/docs/postmortem.md). Store postmortems in the repository or wiki where engineers already work, in one folder, named `YYYY-MM-DD-short-title.md`.
2. The incident commander assigns an author before closing the incident. The author is usually someone who responded, not a manager.
3. Spend 30 to 60 minutes as a team reading the draft together. Agree the action items in the meeting.
4. Put every action item in the normal backlog with a `postmortem` label, an owner and a due date.

### Standard

1. **Action items are specific and testable.** "Improve monitoring" is not an action. "Add an alert when the payment queue age exceeds 5 minutes, routed to the payments rotation" is. Mix types: some to detect sooner, some to reduce impact, some to prevent recurrence.
2. **Priority rules** (starting points):

   | Priority | Meaning | Due within |
   |---|---|---|
   | P1 | Without it, the same incident is likely to recur soon | 2 weeks |
   | P2 | Reduces impact or detection time significantly | 6 weeks |
   | P3 | Useful improvement | Next quarter, or close it as "won't do" with a reason |

3. **Track completion.** Report monthly: action items opened, closed, overdue, and the share of P1 items closed on time. Overdue P1 items go to the engineering lead's staff meeting.
4. **A facilitator who was not involved** runs the review meeting for SEV1 incidents. They protect the blameless tone and ask the questions insiders skip.
5. **Share widely.** Send each postmortem to all engineering. Hold a monthly 30-minute session where one team presents an incident to the rest. Tag postmortems by contributing factor, using the shared tag list in [root cause analysis](root-cause-analysis.md) (for example `change-config`, `capacity`, `dependency`, `alerting-gap`), so you can see patterns across a year.
6. **Customer-facing summary** for SEV1 and SEV2 incidents that customers saw: what happened, impact, what you are changing. No internal names, no blame on suppliers.

### Assured

Everything in Standard, plus:

1. **Formal record.** Postmortems are controlled records with an approver, version history and retention period. This supports ISO/IEC 27001:2022 control 5.27 (learning from information security incidents) and SOC 2 CC7.4 and CC7.5.
2. **Link to the risk register.** Contributing factors that point to a systemic risk become risk entries with an owner.
3. **Regulatory final reports.** When a regulator needs a final report (for example under the EU Cyber Resilience Act or NIS2, see [incident management](incident-management.md)), the postmortem is its source. Keep the two consistent.
4. **Independent check of closure.** A risk or quality function samples closed action items each quarter and confirms the fix exists.
5. **Evidence of security incidents** follows chain-of-custody rules (ISO/IEC 27001:2022 control 5.28) before the postmortem is shared.

## Cloud, on-premises and air-gapped

- In air-gapped networks, write the postmortem inside the isolated network. Produce a sanitised copy for wider sharing, reviewed by the security owner before transfer.
- When a cloud provider or vendor caused the incident, request their incident report and attach it. Your contributing factors still include your own design choices, such as a single-region deployment.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Root cause: human error" | Ask what made the error possible and easy. That is the contributing factor to fix. |
| Postmortem written weeks later from memory | Scribe keeps a live log during the incident. Draft within 5 working days. |
| 20 action items, none done | Agree 3 to 7 items with owners. Close or drop the rest with a reason. |
| Postmortems hidden in a private folder | Default to readable by all engineers. Redact only what you must. |
| Review meeting turns into a trial | An uninvolved facilitator runs it and stops blame language. |
| Same incident every quarter | Tag contributing factors and review the tags quarterly. |

## Templates

- [Postmortem](../../templates/docs/postmortem.md)
- Related practice: [root cause analysis](root-cause-analysis.md) and [rollbacks](rollbacks.md)
- [Incident update](../../templates/docs/incident-update.md)

## Sources

- Google, *Site Reliability Engineering*, "Postmortem Culture: Learning from Failure": https://sre.google/sre-book/postmortem-culture/
- Google, *The Site Reliability Workbook*, "Postmortem Culture: Learning from Failure": https://sre.google/workbook/postmortem-culture/
- NIST SP 800-61 Rev. 3 (lessons learned as part of incident response): https://csrc.nist.gov/pubs/sp/800/61/r3/final
