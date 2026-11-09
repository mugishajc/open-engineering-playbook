# Career framework

The problem: "Promotions feel arbitrary, and our best senior engineers leave or become reluctant managers." Without written levels, people are promoted for visibility or tenure, pay drifts apart for the same work, and the only way up is management. Publish a career framework with levels defined by scope of impact, two parallel tracks (individual contributor and manager) up to senior levels, and promotion decisions based on written evidence reviewed by a calibrated panel.

## Outcomes

Starting targets. Review them once a year.

| Signal | Starting target |
|---|---|
| Engineers who can name their level and what the next one needs | 100% |
| Promotion decisions with a written evidence packet | 100% |
| Promotion decisions reviewed in a cross-team calibration | 100% at Scale-up and above |
| Engineers with a written growth conversation in the last 6 months | 100% |
| Pay band published for each level | Yes, at least internally |
| Senior individual contributors (staff and above) who chose that path over management | Tracked; a healthy ladder has some |

## Principles

- **Levels describe scope, not tasks.** A level says how far your impact reaches (a task, a feature, a team, several teams, the organisation) and how much ambiguity you handle without help.
- **Behaviours are observable.** Every expectation can be shown with evidence: a design document, a review, an incident led, a person mentored.
- **Two tracks, equal standing.** Management is a change of job, not a promotion. Staff and principal engineers sit at the same levels and pay bands as engineering managers and directors.
- **Expectations are cumulative.** Each level includes the ones below it.
- **Impact over activity.** Lines of code, tickets closed and hours worked are not evidence. See [metrics](../measurement/metrics.md).

## Levels

A starting ladder. Rename the titles to fit your organisation. The full version with expectations per area is in [`career-ladder.csv`](../../templates/people/career-ladder.csv).

| Level | Individual contributor | Manager | Scope of impact |
|---|---|---|---|
| L1 | Engineer I | | Well-defined tasks with guidance |
| L2 | Engineer II | | Features within a team, with light guidance |
| L3 | Senior Engineer | | Large features and parts of a system; guides others on the team |
| L4 | Staff Engineer | Engineering Manager | A team's technical direction, or a cross-team problem |
| L5 | Senior Staff Engineer | Senior Engineering Manager | Several teams or a product area |
| L6 | Principal Engineer | Director of Engineering | An organisation or a technical domain across it |
| L7 | Distinguished Engineer | VP of Engineering | The whole company, and its standing outside |

Small organisations need fewer levels. A startup can start with L1 to L4 and add more when it has people working at that scope.

## Practice

### Foundation

- **Write the ladder down** and share it with everyone, including candidates. Start from the template and cut what does not fit.
- **Growth conversations** every 6 months, separate from pay: where you are against the ladder, one or two areas to grow, the next piece of work that would show it.
- **Level at hire** using the same ladder and a structured interview. See [hiring](hiring.md).
- **Solo and very small teams:** a short written list of what "senior" means for you still helps with hiring and pay.

### Standard

- **Promotion by evidence packet.** The engineer and manager write a packet of 2 to 4 pages: scope of work, outcomes, examples against each area of the next level, peer input. The packet shows the person already works at the next level for at least 6 months.
- **Calibration.** A panel of managers and senior engineers from other teams reviews packets together, twice a year, to keep the bar consistent. The direct manager presents but does not decide alone.
- **Pay bands per level**, reviewed against the market once a year. Publish them internally. Many jurisdictions now require pay transparency; for example the EU Pay Transparency Directive (EU) 2023/970 had a transposition deadline of 7 June 2026 for member states. Check your local law.
- **Staff-plus roles have a shape.** Name the common archetypes (tech lead for a team area, architect for a domain, solver for hard problems, right hand to a senior leader) so people can see different ways to work at that level.
- **Manager track starts with a trial.** Offer a 6 to 12 month trial in the manager role, with a clear, no-penalty route back to the individual contributor track.
- **Skills shift.** Update expectations as tools change. With code assistants doing more routine typing, weight judgement, review quality, system design, testing and clear writing more heavily at every level. See [code assistants](code-assistants.md).
- **Junior growth.** Keep hiring and growing early-career engineers. Pair them on real work, and make sure they still learn to read, debug and reason about code, not only to prompt tools.

### Assured

- **Fair process records.** Keep promotion and calibration records, with reasons, for the period your employment law and policies require. Check outcomes by gender and other protected characteristics where the law allows, and act on gaps.
- **Separation of roles.** Nobody decides alone on their own team's promotions or pay.
- **Public sector:** map levels to the civil service grades and pay scales you must use, and publish the mapping. Some governments publish digital, data and technology capability frameworks you can align to.

## Cloud, on-premises and air-gapped

No change. Teams in secure or air-gapped environments may need extra ways to show impact (for example internal write-ups instead of public talks or open source), so do not require external visibility for promotion.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Promotion for tenure or for being loud in meetings | Evidence packets and calibration. |
| Only way to senior pay is management | Parallel tracks with equal bands. |
| Ladder with 40 checkboxes per level | Short expectations by area, judged as a whole. |
| Managers promoted for being the best coder | Trial period with a route back. |
| Same title, very different pay | Published bands, yearly review. |
| Activity metrics (commits, tickets) in promotion cases | Outcomes and scope, with examples. |

## Templates

- [Career ladder (CSV)](../../templates/people/career-ladder.csv)
- [Interview scorecard](../../templates/people/interview-scorecard.md)
- [Team working agreement](../../templates/docs/team-working-agreement.md)

## Sources

- Directive (EU) 2023/970 on pay transparency: https://eur-lex.europa.eu/eli/dir/2023/970/oj
- Will Larson, *Staff Engineer: Leadership beyond the management track* (2021).
- Camille Fournier, *The Manager's Path* (O'Reilly, 2017).
