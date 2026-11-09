# Decision rights

Push each decision to the lowest level that has the information and will live with the result, and write down who decides the common ones. Every decision has exactly one accountable person and a time limit. Escalate only when a decision crosses team boundaries, cannot be undone cheaply, or breaks an agreed standard.

## Outcomes

Starting points. Tune them to your organisation.

- The RACI below (or your version of it) is published and every row has exactly one "A".
- At least 80% of decisions are made inside the team that owns the system.
- Escalated decisions are resolved within 5 working days at each level.
- Every decision that is hard to reverse has a [decision record](../architecture/decision-records.md).
- Nobody has to ask "who decides this?" more than once for the same type of decision. Track repeated questions and add rows.

## Classify the decision first

| Question | If yes | If no |
|---|---|---|
| Is it easy and cheap to reverse (within a day, without data loss)? | decide fast inside the team, record briefly | slow down, write a decision record, consult |
| Does it affect only one team's systems? | team decides | the owners of affected systems are consulted |
| Does it follow an Adopt entry on the [tech radar](../architecture/tech-radar.md) or an existing standard? | no review needed | architecture review or a waiver (see [engineering governance](engineering-governance.md)) |
| Does it change risk, cost or legal exposure beyond the team's budget or mandate? | escalate to the accountable role below | team decides |

## RACI for common engineering decisions

R = responsible (does the work), A = accountable (decides, one per row), C = consulted before, I = informed after.

Columns: Team = owning engineering team; TL = tech lead; SP = staff or principal engineer; EM = engineering manager; HoE = head of engineering; CISO = chief information security officer; Plat = platform team; PM = product manager; P&L = procurement and legal.

| # | Decision | Team | TL | SP | EM | HoE | CTO | CISO | Plat | PM | P&L |
|---|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Library or framework within an Adopt standard | R | A | I | | | | | | | |
| 2 | New language, database or framework (not on radar) | R | R | A | C | I | | C | C | | |
| 3 | Service design inside one team's boundary | R | A | C | | | | | | I | |
| 4 | API change that breaks other teams | R | R | A | I | | | | C | C | |
| 5 | Merge a pull request | R | A | | | | | | | | |
| 6 | Release to production (normal change) | R | A | | I | | | | | I | |
| 7 | Emergency change during an incident | R | A | | I | I | | C | | I | |
| 8 | Roll back a release | R | A | | I | | | | | I | |
| 9 | Set or change an SLO | R | R | C | C | | | | C | A | |
| 10 | Accept a security risk (waiver) | R | R | C | C | I | | A | | C | |
| 11 | Severity and disclosure of a vulnerability | R | C | | | I | | A | | I | C |
| 12 | Adopt a new third-party product or supplier, within the delegated limit | R | C | C | C | A | I | C | C | C | R |
| 13 | Open source an internal project | R | R | C | C | A | | C | | | C |
| 14 | Add a golden path or platform capability | C | C | C | | I | | C | A | | |
| 15 | Change an engineering standard | C | C | R | | A | I | C | C | | |
| 16 | Team boundaries and ownership of services | C | C | C | R | A | I | | C | C | |
| 17 | Select a candidate for an approved role | C | C | | A | I | | | | C | |
| 18 | Start a transition programme | | | R | C | C | A | C | C | C | C |
| 19 | Technical strategy | C | C | R | C | R | A | C | C | C | |
| 20 | Data residency or hosting jurisdiction | C | C | C | | C | A | C | C | | R |

Adapt the columns to your organisation. In a startup, TL, SP, EM, HoE and CTO may be two people. Keep the rows.

### Money, people and contracts

These decisions cause the most conflict in large organisations and need finance, HR and procurement at the table. Match the thresholds to your delegated authority policy.

| # | Decision | Accountable | Responsible | Consulted | Informed |
|---|---|---|---|---|---|
| 21 | Approve new headcount | HoE within the approved budget; CTO above it | EM | Finance, HR | Team |
| 22 | Move budget between teams within a quarter | CTO | HoE | Finance | Affected EMs |
| 23 | Sign or exit a supplier contract above the delegated limit | Per the delegated authority policy | Procurement | HoE, CISO, legal, finance | CTO |
| 24 | Approve a reorganisation affecting more than one team | CTO | HoE | HR, finance, affected EMs, employee representatives where required | All affected staff |
| 25 | Remove or materially change roles | CTO with HR | HR | Legal, employee representatives where required | Affected staff first, then others |

See [team topology](team-topology.md#running-a-reorganisation) for how to run a reorganisation.

Notes on specific rows:

- **Row 5 and 6.** In Assured setups the merge approver must be a different person from the author, enforced by branch protection. See [code review](../delivery/code-review.md) and [release management](../delivery/release-management.md).
- **Rows 7 and 8.** During a declared incident the incident commander holds the "A", whatever their usual role, and can act first and record afterwards. A retrospective review is due within 2 working days. Outside an incident, the on-call engineer may roll back their own service without asking, because rollback is the default response (see [rollbacks](../reliability/rollbacks.md)). See [change management](../reliability/change-management.md).
- **Row 9.** In Assured setups the service owner proposes the SLO and a reliability or risk function approves it, so the column holding "A" changes. See [service levels](../reliability/service-levels.md).
- **Row 10.** Every accepted risk has an expiry date of no more than 12 months.
- **Row 20.** Public sector and Regulated users add the data protection officer as consulted.

## Escalation path

1. **Team level.** The owning team decides within the time box of the work, default 5 working days.
2. **Cross-team.** If two teams disagree, their tech leads meet with a staff or principal engineer within 3 working days. The staff or principal engineer decides if they cannot agree.
3. **Organisation.** If the decision is still blocked, or changes strategy, cost or risk beyond the mandate, the head of engineering decides within 5 working days. Security risks go to the CISO.
4. **Executive.** Only decisions in rows 18 to 25, or those over an agreed money threshold, go to the CTO or executive committee.

Rules for every escalation:

- The person escalating writes one page: the options, a recommendation, the cost of waiting.
- The decider answers in writing, even if the answer is "go back and decide yourselves".
- Once decided, everyone carries out the decision. Disagreement goes into the decision record, not into delay.

When speed and a control conflict, use the default rules in [speed and control](../../leaders/decision-making.md#speed-and-control). The decisions leaders keep for themselves are in [what you never delegate](../../leaders/decision-making.md#what-you-never-delegate).

## Group and division

In a group with several business units, write down which decisions the group keeps and which each division makes. Without this, every division builds its own identity, security and supplier set, and the group pays for all of them.

| Group decides | Division decides |
|---|---|
| Risk appetite, security and data standards | Its own strategy, inside group policy |
| Shared platforms: identity, network, logging, the delivery pipeline | Team design and product roadmaps |
| Strategic suppliers and contracts above the group threshold | Suppliers below the threshold, from the approved list |
| Architecture principles and Hold entries on the tech radar | Adopting anything in Adopt; trials within its own budget |
| Funding of shared services and how their cost is allocated | Its investment mix within its budget |

A division departs from a group standard only with a time-limited waiver recorded by the group architecture forum. Shared services publish their service levels and their cost per unit, so divisions can see what they pay for. See [engineering governance](engineering-governance.md) and [technology budget and cost](../strategy/technology-budget-and-cost.md).

## Practice

### Foundation

Solo and Startup. Write a ten-line list of who decides what. Use decision records for anything hard to reverse. Founders or the CTO handle all escalations, within 2 working days.

### Standard

Scale-up and Enterprise. Publish the RACI. Use the escalation path with time limits. Track the number and age of escalations each month. More than a handful a month for the same row means that row needs a clearer standard.

### Assured

Regulated and Public sector. Everything in Standard, plus:

- Enforce separation of duties for rows 5, 6, 10 and 12 in tooling.
- Keep decision records and escalation outcomes as records for the period your policy sets.
- Match money and risk thresholds to the organisation's delegated authority policy.
- Internal audit samples decisions once a year to check the accountable person decided.

## Cloud, on-premises and air-gapped

Rows 12 and 20 matter more off the public cloud. Hosting jurisdiction, hardware buying and import of new tools into an air-gapped network usually need extra approval. Add a row for "import a new tool into the classified network" with the security officer as accountable.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Two "A"s on a row | Pick one. The other becomes "C". |
| Everything escalates to the CTO | Add thresholds. Delegate rows 1 to 17 and row 21 within budget. |
| Decisions made in meetings with no record | One decision record or one message in a known channel. |
| Consulted means veto | Consulted people give input by a deadline. The accountable person decides. |

## Templates

- [RACI](../../templates/strategy/raci.csv)
- [Decision record](../../templates/docs/adr.md)
- [RFC](../../templates/docs/rfc.md)

## Sources

- Michael Nygard, "Documenting Architecture Decisions", 2011: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- Matthew Skelton and Manuel Pais, "Team Topologies", IT Revolution, 2019: https://teamtopologies.com
