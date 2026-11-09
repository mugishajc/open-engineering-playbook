# Operating rhythm

Run technology leadership on a fixed calendar of short forums, each with named inputs and a written output, and protect the rest of the week for deep work. A rhythm turns metrics, risks and decisions into routine instead of surprises. Without one, the leader's week fills with whatever is loudest, and the board hears about problems from someone else.

This page is for the CTO, CIO, head of engineering, principal engineer and chief architect. Each role attends a different subset of the forums; the table says who.

## When to use this

- You start a new leadership role and want a calendar by the end of week two.
- Your week is all meetings and none of them changes a decision.
- Metrics exist but nobody looks at them until something breaks.
- The board, the audit committee or a ministry asks how technology is governed, and the honest answer is "ad hoc".

## The rhythm at a glance

All durations and frequencies are starting points. Tune them after one quarter.

| Cadence | Forum | Purpose | Attendees | Inputs | Outputs | Duration |
|---|---|---|---|---|---|---|
| Daily | Risk and incident glance | Know what is on fire and what is blocked | Leader alone, or with the on-call lead | Incident channel, overnight alerts, escalations | Unblocking actions, one line per open SEV1 or SEV2 | 15 minutes |
| Weekly | Engineering metrics review | Spot trends before they become incidents | Head of engineering (chair), engineering managers, SRE or platform lead, FinOps owner | DORA metrics, SLO attainment, incidents, cloud and run cost | Up to 3 actions with owners and dates | 45 minutes |
| Weekly | Leadership team meeting | Decide cross-team issues | CTO or CIO (chair), direct reports | Decision requests sent 24 hours before | Decisions logged, owners named | 60 minutes |
| Weekly | One-to-ones | Coach, unblock, hear bad news early | Leader and each direct report | Report's agenda first | Agreed follow-ups | 30 minutes each |
| Monthly | Architecture review | Review significant decisions and drift from the strategy | Chief architect (chair), principal engineers, affected tech leads, security | Decision records and RFCs in "proposed" state, fitness function results | Decisions accepted, rejected or sent back; radar changes | 90 minutes |
| Monthly | Technology risk review | Keep the risk register current | CTO or CIO (chair), CISO, head of engineering, risk or compliance | Risk register, vulnerability ageing, supplier changes, audit findings | Risks rescored, treatments assigned, items for board escalation | 60 minutes |
| Monthly | Cost and capacity review | Match spend and people to priorities | CTO or CIO, finance partner, FinOps owner, heads of engineering | Spend against budget, unit cost trend, hiring plan | Budget variances explained, reallocations proposed | 60 minutes |
| Quarterly | Strategy and portfolio review | Check the strategy still holds; stop, start or reshape work | CTO or CIO (chair), product leadership, chief architect, finance | Strategy one-pager, portfolio status, OKR results, capacity mix | Updated strategy, stop decisions, next-quarter priorities | Half day |
| Quarterly | Quarterly engineering review | Show the whole organisation where it stands | Head of engineering (chair), all managers and principal engineers | Self-assessment results, metrics trend, incidents, people data | Published review and 3 to 5 improvement goals | 2 hours |
| Quarterly | Talent and succession review | Keep key roles covered and promotions fair | CTO or CIO (chair), HR partner, direct reports | Successors for leaders and critical roles, key-person risks, open critical roles, promotion proposals | Succession gaps with owners, promotion calibration, retention actions | 2 hours |
| Quarterly | Strategic supplier review | Hold strategic suppliers to service levels and plan renewals | Supplier owner (chair), procurement, service owners, the supplier for part of the session | Service level history, incidents, roadmap, licence use, renewal and exit status | Actions for the supplier and for you, renewal decision dates (see [suppliers and contracts](../playbook/strategy/suppliers-and-contracts.md)) | 60 minutes per supplier |
| Quarterly | Board or executive committee report | Give governors what they need to govern | CTO or CIO, CEO or accounting officer | One-page scorecard, top risks, key programmes | Decisions or guidance from the board | 20 to 45 minutes on the board agenda |
| Twice a year | Crisis exercise | Practise the executive response | Executive team, communications, legal, CISO; the board joins at least one exercise a year | A realistic scenario | Gaps and owners; see [crisis leadership](crisis-leadership.md) | 2 to 3 hours |
| Annual | Planning and budget | Set the investment mix and the year's bets | CTO or CIO, CFO, product leadership, heads of engineering | Strategy, run cost, demand, horizon scan | Budget, headcount plan, annual objectives | 4 to 8 weeks elapsed |

## Agendas

**Daily glance (15 minutes, often alone).**
1. Open SEV1 and SEV2 incidents: is there a named incident commander? Does anyone need executive cover?
2. Escalations waiting on you. Decide or delegate each one before noon.
3. Any regulatory clock running (see [incident management](../playbook/reliability/incident-management.md)).
4. One message to unblock someone.

**Weekly metrics review (45 minutes).**
1. DORA metrics for Tier 1 services: deployment frequency, change lead time, change fail rate, failed deployment recovery time, rework rate (10 minutes). See [metrics](../playbook/measurement/metrics.md).
2. SLOs: services that burned more than 25% of their monthly error budget this week (10 minutes). See [service levels](../playbook/reliability/service-levels.md).
3. Incidents since last week and overdue postmortem actions (10 minutes).
4. Cost: spend this week against forecast, any line more than 10% over (10 minutes). See [FinOps](../playbook/platform/finops.md).
5. Actions: no more than 3, each with an owner and a date (5 minutes).

Look at trends over 4 to 12 weeks, not single points. Never rank teams against each other on these numbers. If suppliers run most of your systems, replace item 1 with supplier service level attainment, failed or rolled-back changes and open supplier incidents.

**Leadership team meeting (60 minutes).**
1. Decisions requested in writing at least 24 hours before (35 minutes). No paper, no slot. Each paper names the owner, the options and the cost of waiting.
2. Decisions past their deadline in the decision log (5 minutes). Decide now, or set a new date and say why.
3. Risks or incidents that need cross-team action (10 minutes).
4. What each person will tell their teams (10 minutes).

**Monthly architecture review (90 minutes).**
1. Fitness function and standards drift report (15 minutes).
2. Proposed decision records and RFCs, 15 to 20 minutes each, at most 4 per session.
3. Tech radar moves (10 minutes). See [architecture practice](../playbook/architecture/architecture-practice.md).

**Monthly technology risk review (60 minutes).**
1. New and changed risks since last month (20 minutes).
2. Risks outside appetite, with treatment status (20 minutes).
3. Audit findings and supplier changes (10 minutes).
4. What goes to the board this quarter, checked against the agreed escalation thresholds (10 minutes). See [what reaches the board, and how fast](board-and-executive-reporting.md#what-reaches-the-board-and-how-fast).

**Quarterly strategy and portfolio review (half day).**
1. Is the diagnosis in the [technical strategy](../playbook/strategy/technical-strategy.md) still true? What evidence changed?
2. Portfolio status and the run, grow and transform mix (see [portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md)).
3. Stop decisions: name at least one piece of work to stop or shrink. Check every initiative against its written stop conditions and ask "would we start this today?" Money already spent is not an input. See [investment decisions under uncertainty](decision-making.md#investment-decisions-under-uncertainty).
4. Next quarter's objectives and capacity allocation.

**Annual planning (4 to 8 weeks elapsed).** Start 3 to 4 months before the financial year. Week 1: refresh the [horizon scan](../playbook/strategy/horizon-scan.md) and the strategy diagnosis. Weeks 2 to 4: demand and capacity, run cost forecast, business cases for new bets. Weeks 5 to 6: negotiate the mix with finance and product. Final week: publish the plan with a forecast range, not a single date.

## The daily minimum

On a day with no time for anything else, do three things.

1. **Know the incident and risk state.** Every open SEV1 and SEV2, and any security event that may be reportable.
2. **Clear your own blockers.** Decisions waiting on you are the most expensive queue in the organisation. Target: no decision waits on you for more than 2 working days.
3. **Answer one escalation in person.** A short call beats a long thread.

## Protecting deep work

Leaders who never think in long blocks end up running the organisation on reflexes. Start with these rules and adjust after a month.

- **Meeting budget.** Recurring meetings take no more than 50% of your working hours. Audit your calendar every quarter and cut the bottom 20% by value.
- **Two blocks a week.** Book two half-day blocks with no meetings, for strategy, writing and reading code or designs. Treat them like a board meeting.
- **Write before you meet.** Every decision forum takes a written paper sent 24 hours ahead. Reading takes less time than a presentation and produces better questions.
- **Delegate forums.** A forum where you only listen should run without you. Read the written output instead.
- **One no-meeting day per fortnight** for principal engineers and chief architects, whose job depends on long thinking.
- **Batch messages.** Check chat and email at set times. The daily glance covers what cannot wait.

Andy Grove's High Output Management treats meetings as a tool with a cost, and one-to-ones as the main way to learn what is happening. Use that test: if a meeting does not change a decision or teach you something, cancel it.

## How the rhythm scales

| Organisation | What to keep | What to merge or drop |
|---|---|---|
| 10-person company | Daily glance, a 30-minute weekly review of metrics, incidents and cost, weekly one-to-ones, a quarterly half-day strategy session, an annual budget | Merge architecture and risk into one monthly hour. The board report is one page for the founders and investors. |
| Scale-up (20 to 200 engineers) | All forums in the table, with separate architecture and risk reviews | Quarterly engineering review can be a written document plus a 1-hour session |
| Enterprise (200+ engineers) | All forums, repeated at division level, with the division outputs feeding the group forums | Group forums read division summaries, not raw metrics. Stagger division reviews a week ahead of group reviews. |
| Regulated firm | All forums, plus minutes, decision logs and risk register history kept as audit evidence | Nothing. Map each forum to a governance body in your terms of reference. |
| Government department | All forums, aligned to the budget year, spending review and assurance gates; the senior responsible owner or accounting officer gets the board report | Annual planning starts earlier to meet budget submission dates. See [public sector](../playbook/compliance/public-sector.md) and [IT governance](../playbook/operating-model/it-governance.md). |

## Common mistakes

| Mistake | Fix |
|---|---|
| Forums with no written output | Every forum ends with decisions and actions recorded within 24 hours. If there is nothing to record twice in a row, cancel the forum. |
| Metrics reviews that become status theatre | Review trends and exceptions only. Ask "what will we do differently?" for each one. |
| The leader attends everything | Delegate forums where you only listen. Read the output. |
| Strategy reviewed once a year | Review it every quarter; change it when the evidence changes. |
| Board report written the night before | Generate it from the same data the weekly and monthly forums use. |
| Bad news held for the next scheduled forum | Use the escalation thresholds agreed with the board; the calendar is a minimum, not a gate. |
| Quarterly review that never stops anything | At least one stop or shrink decision each quarter, or a written reason why not. |
| Rhythm abandoned during a crisis | Cancel optional forums during a crisis, but keep one-to-ones and the risk review. Restart the full rhythm within 2 weeks. |

## Templates

- [Operating rhythm calendar](../templates/leaders/operating-rhythm-calendar.md)
- [Quarterly engineering review](../templates/leaders/quarterly-engineering-review.md)
- [Board engineering report](../templates/leaders/board-engineering-report.md)
- [Strategy one-pager](../templates/strategy/strategy-one-pager.md)
- [Risk register](../templates/strategy/risk-register.csv)

## Sources

- Andy Grove, "High Output Management", Random House, 1983.
- John Doerr, "Measure What Matters", Portfolio, 2018.
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
- Google SRE workbook, implementing SLOs: https://sre.google/workbook/implementing-slos/
- FinOps Foundation, FinOps Framework: https://www.finops.org/framework/
- UK NCSC, Board Toolkit: https://www.ncsc.gov.uk/collection/board-toolkit
