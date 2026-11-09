# On-call

Run on-call rotations large enough that nobody carries the pager more than one week in six, page only for symptoms that users feel, and pay people for the time. On-call that wakes the same three people every night burns them out and then loses them. Sustainable on-call is a staffing and alerting decision, not a test of character.

## Outcomes

Starting points. Tune them to your services and local labour law.

- Each 24/7 rotation has at least 6 people, so each person is on call no more than 1 week in 6.
- On average, no more than 2 incidents per 12-hour shift. Above that, the team stops feature work to cut alert load.
- At least 90% of pages are actionable (the responder had to do something). Non-actionable pages are fixed or removed within 2 weeks.
- Pages are acknowledged within 5 minutes in 95% of cases.
- Every on-call engineer has a written handover at the start of each shift.
- On-call is compensated with pay or time off, and the policy is written down.

## Practice

### Foundation

1. **Business hours first.** If the product does not need 24/7 response, do not run a 24/7 rotation. Say so in your customer terms and on the status page.
2. **One primary, one backup.** The backup is paged if the primary does not acknowledge within 10 minutes.
3. **Every page links to a runbook** (see the [runbook template](../../templates/docs/runbook.md)). A page with no runbook is a bug.
4. **Page on symptoms.** Page when users are affected or about to be: SLO burn rate, failed health checks from outside, queues that stop draining. Send causes (high CPU, a disk at 80%) to dashboards or tickets. See [service levels](service-levels.md).
5. **Time off after a bad night.** Someone paged overnight starts late or takes the morning off. No permission needed.

### Standard

1. **Rotation size.** Google's SRE book caps on-call at 25% of an engineer's time. With a primary and secondary on every shift, that needs at least 8 people at one site, or 6 per site across two sites. This playbook's starting point for a primary-only 24/7 rotation is 6 people. Below that, merge rotations across teams, move to business hours, or buy cover.
2. **Shift length.** One week, handed over on a weekday morning, not Monday or Friday. Follow-the-sun teams use 8 to 12-hour shifts.
3. **Alert hygiene.** Review every page weekly in a 30-minute meeting. For each: was it actionable, was it urgent, is the runbook right? Delete or demote alerts that fail.
4. **Handover.** Written, at every shift change, in the rotation's channel:
   - Open incidents and their state.
   - Alerts that fired and were not fixed.
   - Risky changes or migrations planned during the next shift.
   - Anything odd that the next person should watch.
5. **Onboarding.** New members shadow one full rotation, then lead one with an experienced engineer as reverse shadow, before going solo.
6. **Compensation principles.**
   - Pay a fixed amount for each on-call period, plus pay or time off in lieu for hours worked when paged. Write the rates down.
   - Time responding counts as working time. In the EU, standby time with tight response constraints can count as working time in full (Court of Justice of the EU, case C-518/15, *Matzak*, 2018). Check the law where each person works.
   - Respect minimum rest. The EU Working Time Directive (2003/88/EC) requires 11 consecutive hours of daily rest; a night of pages breaks it.
   - On-call is part of the role description, agreed at hiring, not added later without consent.
7. **Escalation path.** Primary, then secondary, then the engineering manager, then the incident commander rotation. Each step has a timeout of 10 to 15 minutes.
8. **Follow-the-sun for larger organisations.** When you have engineers in 2 or 3 regions at least 6 hours apart, each region covers its own daytime. Nobody is paged at night. It needs disciplined written handover and shared runbooks, and it fails if one region holds all the knowledge.

### Assured

Everything in Standard, plus:

1. **Records.** Keep page logs, acknowledgement times and escalations for the retention period your auditors need. They support SOC 2 CC7.4 and ISO/IEC 27001:2022 controls 5.24 to 5.26.
2. **Privileged access on call.** On-call engineers get production access through just-in-time elevation, logged and time-limited (see [access control](../security/access-control.md)). No standing admin rights because "they might need it at 3am".
3. **Separation of duties.** Emergency changes made on call are reviewed by a second person within 2 working days (see [change management](change-management.md)).
4. **Fatigue limits.** Written rule: after 2 or more hours of night-time response, the engineer hands over and rests. The manager enforces it.

## Cloud, on-premises and air-gapped

- **Pages must leave the building.** Alerts generated inside an isolated network have to reach people outside it. Options: an SMS gateway or GSM modem attached to the alerting server; a one-way relay that exports only alert names and severities; a phone tree for the most restricted sites. Agree with the security owner what alert content may leave the network.
- **Remote access.** If on-call engineers cannot reach the isolated network from home, response means travelling to site. Set your response targets and staffing to match, and say so in the service's commitments.
- **Hosted paging tools** depend on the internet and the vendor. Test what happens when the vendor is down, and keep a fallback such as a phone bridge.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Three people cover 24/7 | Merge rotations, move to business hours, or hire. Do not ask for heroics. |
| Paging on CPU, memory and disk thresholds | Page on user symptoms. Move resource alerts to tickets. |
| On-call is unpaid "because it is quiet" | Pay for availability, whether or not pages come. |
| The lead engineer is always the escalation point | Spread knowledge with runbooks and shadowing. Rotate the escalation role. |
| Alerts nobody understands are muted, not fixed | Weekly page review; every alert has an owner and a runbook. |
| Handover by memory | Written handover note in the rotation channel at every shift change. |

## Templates

- [Runbook](../../templates/docs/runbook.md)
- [Incident update](../../templates/docs/incident-update.md)

## Sources

- Google, *Site Reliability Engineering*, "Being On-Call": https://sre.google/sre-book/being-on-call/
- Google, *The Site Reliability Workbook*, "On-Call": https://sre.google/workbook/on-call/
- Directive 2003/88/EC (EU Working Time Directive): https://eur-lex.europa.eu/eli/dir/2003/88/oj
- Court of Justice of the EU, case C-518/15, *Ville de Nivelles v Rudy Matzak*: https://curia.europa.eu/juris/liste.jsf?num=C-518/15
