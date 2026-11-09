# Knowledge sharing

Make knowledge flow between people and teams on purpose: write decisions down, run small communities of practice, hold short internal talks, and let engineers contribute to other teams' code through inner source. Knowledge that lives only in a few heads is a delivery bottleneck and a continuity risk. The aim is that no critical system depends on one person, and that a good idea in one team reaches the others within weeks, not years.

## Outcomes

Starting points. Tune them to your organisation.

- Every critical system has at least 2 people who can operate and change it, recorded in the service catalogue.
- At least 80% of RFCs that affect several teams get written comments from those teams before the decision (the same target as [RFCs](../architecture/rfcs.md)).
- Every postmortem with lessons for other teams is shared and summarised in a session or note within 30 days.
- At least 1 internal talk or written deep explanation per month per 50 engineers.
- Inner source pull requests from outside the owning team get a first response within 2 working days.

## Practices

### Written culture

- Decisions go in [ADRs](../architecture/decision-records.md), proposals in [RFCs](../architecture/rfcs.md), incidents in [postmortems](../reliability/postmortems.md), and procedures in runbooks. Meetings are for discussion. Writing is the record.
- Teams publish a short weekly or fortnightly update in one shared place: what shipped, what they learned, what they need.
- Default to open: docs, RFCs and postmortems are readable by all of engineering unless there is a security or legal reason not to.

### Communities of practice (guilds)

- A guild is a voluntary group around a skill that cuts across teams: testing, frontend, security, data, accessibility.
- Each guild has 1 or 2 named organisers, meets for at most 1 hour every 2 to 4 weeks, and keeps notes.
- Guilds produce things: shared libraries, linter rulesets, radar proposals, how-to guides, review of RFCs in their area.
- Close a guild that has not met or produced anything for 3 months. It can restart when there is energy.
- In Team Topologies terms, an enabling team does similar work full-time for a period. A guild is the lighter, part-time version.

### Internal talks

- Short sessions of 20 to 30 minutes, recorded, with slides or notes stored on the docs site.
- Good topics: a postmortem, an ADR and its trade-offs, a tool a team adopted, a production system tour, a failed experiment.
- Rotate speakers. Help first-time speakers with a dry run.

### Inner source

- Inner source applies open source practices inside the organisation: any engineer may propose a change to another team's repository.
- Every repository open to contributions has a `CONTRIBUTING.md`, clear `CODEOWNERS` and labelled issues for outside contributors.
- Owning teams name trusted committers who review outside contributions and help contributors. The owning team keeps the final say and the on-call responsibility.
- Use inner source for shared libraries, platform components and internal tools. It is less useful for code with heavy on-call duty.

### Pairing and rotation

- Pair or mob on unfamiliar systems, and rotate who handles operational work so knowledge spreads.
- Short rotations (2 to 6 weeks) between teams, or into the platform team, spread context and build trust. To build a new skill, use the longer rotations (4 to 12 weeks) in [skills gap](skills-gap.md).

## Practice

### Foundation

- Write decisions and incidents down. One shared channel or page for team updates.
- Pair on anything only one person knows. Record a 15-minute walkthrough of each critical system.

### Standard

- Communities of practice for the 3 to 5 skills that matter most, each with organisers and notes.
- Monthly internal talk slot, recorded.
- Inner source for shared components, with `CONTRIBUTING.md`, trusted committers and response targets.
- The service catalogue records 2 or more people per critical system. Review gaps each quarter.

### Assured

- Key-person risk is recorded in the risk register for any critical system with fewer than 2 qualified people, with a plan and a date.
- Knowledge needed to operate regulated or critical systems is in controlled, reviewed runbooks, not only in people's heads or recordings.
- Succession plans exist for named roles in incident response and for privileged administration.

## Cloud, on-premises and air-gapped

- Teams on isolated networks easily drift away from the wider organisation. Share sanitised summaries of their ADRs, postmortems and talks outside the enclave, after review.
- Keep recordings and notes on the internal docs site of the network the knowledge belongs to.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Knowledge lives in chat threads | Move anything durable into docs, ADRs or runbooks within a week. |
| Guilds that meet but produce nothing | Each guild names one thing it will produce per quarter, or closes. |
| Inner source pull requests ignored for weeks | Response targets and named trusted committers. |
| Only senior people present | Rotate speakers. Support first-timers. |
| Attendance used as a performance measure | Count outputs (docs, libraries, fixes), not attendance. |

## Templates

- [ADR template](../../templates/docs/adr.md)
- [RFC template](../../templates/docs/rfc.md)
- [Postmortem template](../../templates/docs/postmortem.md)
- [Contributing guide](../../templates/repo/CONTRIBUTING.md)

## Sources

- InnerSource Commons, patterns and learning path: https://innersourcecommons.org/
- Matthew Skelton and Manuel Pais, Team Topologies (2019): https://teamtopologies.com/
- DORA capabilities, including learning culture: https://dora.dev/capabilities/
