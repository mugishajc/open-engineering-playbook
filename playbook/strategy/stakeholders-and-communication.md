# Stakeholders and communication

Map who is affected by an engineering change, give each group the message it needs in its own terms, and keep a fixed cadence so nobody hears news first from a rumour. Treat resistance as information about a real cost or risk until proven otherwise. Name one person, the technical evangelist, to carry the message between engineers and everyone else.

## Outcomes

Starting points. Tune them to your organisation.

- Every strategy or transition has a [stakeholder map](../../templates/strategy/stakeholder-map.md) reviewed at least once a quarter.
- Each high-influence stakeholder has a named relationship owner and has had a direct conversation in the last 6 weeks.
- Scheduled updates go out on time at least 90% of the time.
- Questions from stakeholders get a first answer within 2 working days.
- A short pulse survey of affected engineers (for example three questions every 6 weeks) shows understanding of "why we are doing this" at 70% or higher.

## Stakeholder map

Place each person or group on two axes: influence over the outcome, and interest in it.

| | Low interest | High interest |
|---|---|---|
| **High influence** | Keep satisfied: short, outcome-focused updates; consult before decisions that affect them | Manage closely: involve in decisions, meet regularly, share bad news early |
| **Low influence** | Monitor: general channels, no special effort | Keep informed: regular updates, demos, a place to ask questions |

People move between boxes. A finance director becomes high-interest the week a budget is cut. Review the map at every gate of the [transition playbook](transition-playbook.md).

## Message by audience

| Audience | They care about | Lead with | Format | Avoid |
|---|---|---|---|---|
| Board or ministers | risk, cost, reputation, obligations | the decision needed, the risk of not acting, the cost and payback | one page, three numbers | tool names, jargon |
| Finance | cash, timing, budget fit | [business case](business-case.md), phased funding, payback, low scenario | spreadsheet plus one page | benefits that do not turn into money or reduced risk |
| Engineers | daily work, skills, autonomy, on-call load | the problem in their words, what changes for them and when, how they can influence it | RFC, demo, open Q and A | slogans, decisions presented as consultation |
| Engineering managers | team capacity, deadlines, hiring | timeline per team, support offered, what they can say no to | plan per wave, office hours | surprise dates |
| Security, risk and audit | control, evidence, separation of duties | which controls change and what evidence the new way produces | [control mapping](../compliance/control-mapping.md) | "trust us" |
| Regulators | resilience, consumer impact, outsourcing | what changes, how risk is managed, notification where required | formal letter or meeting, via compliance | informal channels, late notice |
| Citizens or customers | service availability, data safety | what they will notice, when, and where to get help | service status page, release notes | internal project names |
| Suppliers and partners | contract, timeline, integration changes | dates, technical changes, support contacts | written notice per contract terms | changes without notice periods |

## Cadence

| Audience | Frequency | Channel | Owner |
|---|---|---|---|
| Sponsor and steering group | monthly, plus every gate | meeting with written decisions | programme lead |
| Board or ministers | quarterly, or at major gates | paper through governance | CTO |
| All engineers | every 2 weeks | written update plus recorded demo | technical evangelist |
| Affected teams | weekly during their wave | team channel, office hours | platform team |
| Finance | monthly | spend against plan | programme lead with finance partner |
| Regulators | as required by law or agreement | formal | compliance function |
| Customers or citizens | before and after visible changes | status page, notices | product manager |

A written update uses the same four headings every time: what changed, what is next, what we need from you, risks. Keep it under 300 words.

## Handling resistance

Resistance usually points to a real cost. Ask what the person expects to lose before you argue.

| What you hear | Likely cause | Response |
|---|---|---|
| "We tried this before and it failed." | memory of a failed programme | Ask what failed. Show what is different, in writing. Invite them to review the plan. |
| "This will slow us down." | delivery pressure, unclear support | Show the support offered per team and the delivery metrics from the pilot. Move their wave if the deadline is real. |
| "The old system works fine." | sunk effort, expertise at risk | Name what they know as valuable. Give them a role in the migration. |
| "Security or audit will never accept it." | unknown control impact | Bring security and audit in at Assess. Show the evidence the new way produces. |
| Silence | fear of speaking up | Use anonymous questions and 1:1 conversations. Report back what you heard. |

When an objection identifies a real problem, change the plan and say so publicly. When it does not, explain the decision and the reason, record it, and move on. Use the escalation path in [decision rights](../operating-model/decision-rights.md) when disagreement blocks work for more than 5 working days.

## The technical evangelist

The technical evangelist (also called advocate or champion) is a respected engineer who explains the change to engineers and explains engineers' concerns to leadership. It is a part-time role, typically 20% to 50% of one person during a transition. One evangelist is not enough change capacity for an enterprise programme: there, evangelists work inside a named change team with communications, training and an HR partner (see [people and roles](transition-playbook.md#people-and-roles)).

They:

- write the fortnightly update and run demos;
- run office hours and collect questions, with answers published in one place;
- pair with early teams in each wave;
- report recurring complaints to the programme lead, with evidence;
- keep the [documentation](../people/documentation.md) and golden paths current.

They do not own the decision, enforce adoption or report on individuals. Their value depends on engineers trusting them.

## Practice

### Foundation

Solo and Startup. A short written note for each change that affects others: what, why, when, what to do. One channel, one place for questions. For a startup, the founder or CTO talks to every engineer directly.

### Standard

Scale-up and Enterprise. A stakeholder map per programme, the cadence table above, a named technical evangelist, and messages tailored by audience. Track questions and answers in a public log.

### Assured

Regulated and Public sector. Everything in Standard, plus a communications plan approved at the Decide gate, records of regulator and board communications kept per your records policy, and accessible formats for public notices (see [public sector](../compliance/public-sector.md)). Coordinate any external statement with legal and communications teams.

## Cloud, on-premises and air-gapped

Communication channels must reach every audience. Staff on classified or air-gapped networks may not see the corporate chat or wiki. Publish updates inside those networks too, and allow extra time for questions to cross the gap.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Announcing a finished decision as "consultation" | Say clearly which parts are decided and which are open. |
| Same message for every audience | Use the audience table. |
| Updates stop when news is bad | Keep the cadence. Bad news early costs less. |
| Evangelist as enforcer | Keep the role advisory. Enforcement belongs to governance. |

## Templates

- [Stakeholder map](../../templates/strategy/stakeholder-map.md)
- [RACI](../../templates/strategy/raci.csv)
- [Transition charter](../../templates/strategy/transition-charter.md)

## Sources

- UK Government Service Manual: https://www.gov.uk/service-manual
- US Digital Services Playbook: https://playbook.cio.gov/
