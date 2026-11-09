# Team topology

Organise most engineers into stream-aligned teams that own a product or service end to end, and add platform, enabling and complicated-subsystem teams only when they reduce load on those stream-aligned teams. Define how teams interact, not only who is on them. This follows the model in "Team Topologies" by Matthew Skelton and Manuel Pais (2019).

## Outcomes

Starting points. Tune them to your organisation.

- At least 70% of engineers sit in stream-aligned teams.
- Each team can take a typical change from idea to production without waiting on another team for more than 1 working day.
- Every team has a published team API (what it owns, how to reach it, how to request work) reviewed every 6 months.
- Every collaboration between two teams has an end date, by default no more than 6 months.
- Team members rate their cognitive load as manageable in a short survey every quarter (for example, 70% or more agree).

## Team types

| Type | Purpose | Owns | Typical size | Signs it is needed |
|---|---|---|---|---|
| Stream-aligned | delivers a flow of change for one product, service, user group or business area | the service, its code, its on-call, its outcomes | 5 to 9 people | always; this is the default team |
| Platform | provides internal services that stream-aligned teams consume on their own | the [developer platform](../platform/developer-platform.md), [golden paths](../platform/golden-paths.md), shared infrastructure | 5 to 9 per platform team | three or more teams rebuild the same infrastructure |
| Enabling | helps other teams learn a skill, then leaves | coaching material, short engagements | 2 to 5 people | a skill gap (for example testing, observability, security) slows many teams |
| Complicated-subsystem | owns a part that needs rare specialist knowledge | the subsystem and its interface | 3 to 8 people | a component needs deep expertise, such as a risk engine, video codec or cryptography library |

Team sizes are starting points. A team that grows past 9 people usually needs splitting along a stream.

## Interaction modes

| Mode | When to use | Time limit (starting point) | Signal it should change |
|---|---|---|---|
| Collaboration | two teams discover something new together | 3 to 6 months | the interface is clear enough to write down |
| X-as-a-Service | one team consumes another's service with little contact | ongoing | consumers need frequent help, so the interface is wrong |
| Facilitating | an enabling team coaches another team | 4 to 12 weeks | the team can do the work alone |

Write the current mode between each pair of teams in their team APIs. Unplanned collaboration that never ends is the most common source of hidden dependencies.

## Conway's law and boundaries

Systems tend to copy the communication structure of the organisation that builds them (Melvin Conway, 1968). Use this on purpose:

- Draw the service boundaries you want, then shape teams to match.
- Give each service exactly one owning team. Shared ownership means no ownership.
- When a change regularly needs three or more teams, the boundary is wrong. Move the code or the people.
- Check boundaries with data: count pull requests that touch code owned by more than one team. See [source control](../delivery/source-control.md) for CODEOWNERS.

## Cognitive load

A team can own only as much as it can understand well enough to run it at 3 a.m. Signs of overload: rising change fail rate, long onboarding, frequent "nobody knows how this works". Reduce load by moving infrastructure to a platform, splitting a domain, or retiring services. Do not reduce it by adding more people to one team.

## Practice

### Foundation

Solo and Startup. One stream-aligned team owns everything. Write down who owns which service, even if it is the same five people. Buy or adopt managed services rather than building a platform. Split into two stream-aligned teams when the team passes about 9 people, along a product or user boundary.

### Standard

Scale-up and Enterprise.

1. Stream-aligned teams own services end to end, including on-call. See [on-call](../reliability/on-call.md).
2. Start a platform team when three or more stream-aligned teams spend noticeable time on the same infrastructure work. Run the platform as a product with users, a roadmap and satisfaction measures.
3. Use enabling teams for time-boxed adoption: a new testing practice, a security baseline, observability. Each engagement has goals and an end date.
4. Create complicated-subsystem teams only for real specialist domains. Review each one yearly.
5. Publish team APIs in a service catalogue. See the [service catalogue entry template](../../templates/docs/service-catalog-entry.yaml).
6. Review the topology twice a year against delivery [metrics](../measurement/metrics.md) and cross-team dependency counts.

### Assured

Regulated and Public sector. Everything in Standard, plus:

- Record ownership of each system that supports a critical or important function, with a named accountable manager.
- Keep separation of duties inside the team topology: the person who writes a change is not the only person who can approve it. Do this with automation, not a separate team. See [regulated industries](../compliance/regulated-industries.md).
- When a supplier staffs part of a team, write the team API into the contract: ownership, on-call, knowledge transfer and exit.
- Keep the ownership record current. Audit it at least once a year.

## Cloud, on-premises and air-gapped

On-premises and air-gapped environments often need a platform team earlier, because hosting, mirrors, registries and identity cannot be bought as managed services. Plan for it at a smaller size, for example from two or three stream-aligned teams. Where only cleared staff can work on a classified network, form a stream-aligned or platform team inside the network and keep its interface with outside teams as X-as-a-Service. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Component teams (front end team, database team) for a single product | Reorganise around streams of change. Keep specialists as enabling or complicated-subsystem teams. |
| Platform team as a ticket queue | Offer self-service with golden paths. Measure time to first deploy for new services. |
| Permanent "collaboration" | Set an end date. Write the interface. |
| Separate operations team carries all on-call | Teams that build a service also run it, with platform support. |
| Reorganising without moving ownership of code | Update CODEOWNERS and the service catalogue on the same day. |

## Templates

- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml)
- [CODEOWNERS (GitHub)](../../templates/github/CODEOWNERS)
- [RACI](../../templates/strategy/raci.csv)

## Sources

- Matthew Skelton and Manuel Pais, "Team Topologies", IT Revolution, 2019: https://teamtopologies.com
- Melvin E. Conway, "How Do Committees Invent?", Datamation, 1968: https://www.melconway.com/Home/Committees_Paper.html
