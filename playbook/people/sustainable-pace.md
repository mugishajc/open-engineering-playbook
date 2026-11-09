# Sustainable pace

The problem: "We ship by heroics." Deadlines are met with late nights, the same few people get paged every week, and good engineers burn out or leave. Plan work so the team can keep the same pace indefinitely: limit work in progress, cap on-call load, treat overtime as a signal that planning failed, and give time back when a crunch happens. Tired engineers make more mistakes, and those mistakes reach production.

## Outcomes

Starting targets. Tune them to your context and local law.

| Signal | Starting target |
|---|---|
| Weeks in which anyone on the team works more than 48 hours | Rare, and each one discussed at the retrospective |
| On-call load | Incidents: on average no more than 2 per 12-hour period on call. Out-of-hours pages: under 2 per week per rotation. Same measures as [on-call](../reliability/on-call.md) |
| Annual leave taken | Everyone takes their full entitlement each year |
| Engineers with at least 2 blocks of 2 hours focus time per day | Most of the team, most days |
| Engineers on a team's on-call rotation | At least 6 for a 24 by 7 primary rotation (each person primary at most 1 week in 6). If the same people also cover backup, at least 8 at one site or 6 per site across two sites; otherwise the backup comes from a shared escalation rotation, as in [on-call](../reliability/on-call.md) |
| Team health survey score on workload | Measured every quarter, trending stable or up |

## Why it matters

- The Agile Manifesto principles say sponsors, developers and users "should be able to maintain a constant pace indefinitely".
- The World Health Organization includes burn-out in ICD-11 as an occupational phenomenon resulting from chronic workplace stress that has not been successfully managed.
- A joint WHO and International Labour Organization study (2021) linked working 55 or more hours a week with a higher risk of death from stroke and heart disease.
- In the EU, the Working Time Directive (2003/88/EC) limits average weekly working time, including overtime, to 48 hours. Many countries have similar rules, and some (for example France and Portugal) have right-to-disconnect rules. Check your local law.

## Practice

### Foundation

- **Plan to 80%.** Do not plan more than about 80% of the team's capacity. The rest absorbs interruptions, support and learning. See [planning and forecasting](../ways-of-working/planning-and-forecasting.md).
- **Limit work in progress.** Fewer things in progress finish sooner and cause less context switching.
- **No regular overtime.** Extra hours are an exception that the team discusses at the next retrospective, with a plan to prevent the cause.
- **Time back after a crunch.** If people work extra hours or out-of-hours on an incident, they take equivalent time off within 2 weeks, without having to ask twice.
- **Leave is taken.** Managers check that everyone books holidays and that nobody is contacted while on leave except for a pre-agreed emergency.
- **Founders and solo engineers** set working hours for themselves too. Automate alerts so only real emergencies wake you.

### Standard

- **On-call limits.** Use rotations of at least 6 people for 24 by 7 primary cover (8 at one site if the same people also cover backup), pay or time off for on-call according to local law and policy, and the load targets above: no more than 2 incidents per 12 hours on call and under 2 out-of-hours pages per week. Every page that did not need a human is a defect to fix. See [on-call](../reliability/on-call.md).
- **Interrupt rotation.** One person per week handles support questions and unplanned requests, so the rest of the team has focus time.
- **Meeting budget.** Protect at least two 2-hour focus blocks a day. Keep one meeting-free day per week if the team wants one.
- **Crunch rules.** If the business genuinely needs a crunch (a legal deadline, a launch):
  1. Leadership states the reason and the end date in writing.
  2. It lasts at most 2 weeks.
  3. Scope is cut before hours are added.
  4. Time is given back afterwards.
  5. There is at most one per team per half-year. A second one means planning is broken.
- **Measure workload.** Run a short team health check every quarter (workload, focus time, on-call, clarity of goals). Act on the bottom score.
- **Asynchronous by default** across time zones: decisions in writing, no expectation of replies outside the reader's working hours, recorded meetings when someone cannot attend.
- **Heroes are a risk.** If one person is always the one who fixes things, spread the knowledge (pairing, runbooks, rotation). See [knowledge sharing](knowledge-sharing.md).

### Assured

- **Working time records** where law requires them, including on-call and incident hours.
- **Fatigue rules for critical operations.** For changes to critical infrastructure, require a rested approver: no one approves or executes a high-risk production change after more than 12 hours on duty, except in a declared incident with a second person checking.
- **Occupational health** support and an escalation route for workload concerns that bypasses the line manager.

## Cloud, on-premises and air-gapped

Air-gapped and secure environments often need people on site, which removes the option of a quick fix from home. Plan on-site cover as a rotation with the same limits, and make sure runbooks let the on-site person act without calling an expert at night. Work on customer sites in other time zones counts as working time.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Crunch" every release | Plan to 80%. Cut scope before adding hours. |
| The same two people on call every other week | Rotations of 6 or more. Grow skills through shadowing. |
| Praise for late-night heroics | Praise the fix that stopped the page. Discuss the overtime in the retrospective. |
| Unused annual leave rolling over | Managers check bookings each quarter. |
| Chat messages at midnight with an expectation of reply | Asynchronous norms in the working agreement. |
| Burnout discovered at the exit interview | Quarterly health checks and regular one-to-ones. |

## Templates

- [Team working agreement (hours, response times, on-call)](../../templates/docs/team-working-agreement.md)
- [Runbook](../../templates/docs/runbook.md)

## Sources

- Principles behind the Agile Manifesto: https://agilemanifesto.org/principles.html
- World Health Organization, burn-out an occupational phenomenon (ICD-11): https://www.who.int/news/item/28-05-2019-burn-out-an-occupational-phenomenon-international-classification-of-diseases
- World Health Organization, long working hours and stroke and heart disease (2021): https://www.who.int/news/item/17-05-2021-long-working-hours-increasing-deaths-from-heart-disease-and-stroke-who-ilo
- Directive 2003/88/EC concerning certain aspects of the organisation of working time: https://eur-lex.europa.eu/eli/dir/2003/88/oj
- Kent Beck, *Extreme Programming Explained*, second edition (Addison-Wesley, 2004), sustainable pace.
- Google SRE book, being on-call: https://sre.google/sre-book/being-on-call/
