# Cognitive load

Cognitive load is the amount of mental effort a team needs to do its work. When a team owns too many services, talks to too many other teams, or works with unclear boundaries, its cognitive load rises until throughput drops and defects climb. Team Topologies brought the term into engineering management. This page makes it measurable and actionable, so you can use it to decide when to split a team, create a platform capability, or stop adding responsibilities.

## Outcomes

Starting targets. Tune them after two quarters of data.

| Signal | Starting target |
|---|---|
| Cognitive load survey score (1-5 scale) | Median at or below 3 for every stream-aligned team |
| Teams reporting "too hard to make a change" (score 4 or 5) | Under 15% of teams |
| Services per stream-aligned team | No more than 2 to 3 in production, plus their supporting jobs and pipelines |
| Cross-team dependencies per sprint or iteration | Trending down quarter over quarter |
| Change fail rate for overloaded teams (score 4+) | Tracked separately and compared to baseline |

## Practice

### Foundation

Understand the three types of cognitive load and measure them with a short survey.

**Three types.**

| Type | What it is | Example | What to do about it |
|---|---|---|---|
| Intrinsic | The difficulty of the domain itself | Tax calculation rules, payment processing, medical terminology | Accept it. Hire for domain knowledge. Write clear documentation. |
| Extraneous | Friction from bad tools, unclear ownership, and unnecessary cross-team coordination | Deploying requires 5 manual steps, nobody knows who owns the shared library, the CI pipeline breaks weekly | Remove it. This is the type you can and should reduce. |
| Germane | The effort of learning new skills and building new mental models | Learning a new language, understanding a new architecture pattern, onboarding to a new team | Protect it. This is how people grow. |

The goal is to reduce extraneous load so teams have capacity for intrinsic and germane load.

**Measure it.** Run a short survey every quarter, alongside the developer experience survey (see [developer experience](../measurement/developer-experience.md)). Use these questions from the Team Topologies assessment:

1. "How hard is it to make a change to the primary service your team owns?" (1 = easy, 5 = very hard)
2. "How many other teams do you need to coordinate with to ship a typical change?" (count)
3. "How much of your week is spent on work outside your team's core mission?" (percentage)
4. "Do you feel your team owns too many things to do any of them well?" (agree/disagree)

A team-level median score of 4 or 5 on question 1 is a signal to act.

**Make it visible.** Plot cognitive load scores by team on a simple chart. Share it with engineering leadership. A team with a high score and a rising change fail rate is overloaded, not underperforming.

### Standard

Use cognitive load as a decision input for team design.

**When to split a team.** If a team's cognitive load score stays at 4 or above for two consecutive quarters, and their change fail rate or lead time is worse than the organisation median, the team has too much to own. Options:

- Move one service to another team that has capacity.
- Create a new team and transfer ownership of a bounded set of services.
- Move a cross-cutting concern to a platform team (see [team topology](team-topology.md)).

Do not split a team just because it is large. Split it because the cognitive load exceeds what the team can handle.

**When to create a platform capability.** If three or more stream-aligned teams spend significant time on the same infrastructure concern (CI pipelines, observability setup, secret management, database provisioning), that concern is a candidate for a platform team or a self-service capability. The platform team absorbs the extraneous load so stream-aligned teams can focus on their domain.

**When to stop adding services.** Before assigning a new service to a team, check their cognitive load score. If it is already at 3 or above, either move something off their plate first or assign the new service elsewhere. Adding a service to an overloaded team makes the overload worse and the new service unreliable.

**Signals of overload.** These often appear together:

- Rising change fail rate (more deployments that are unplanned fixes).
- Slowing lead time for changes (longer from commit to production).
- Increasing incident rate for the team's services.
- Rising developer dissatisfaction in the DX survey.
- Context switching: the team works on 4 or more unrelated things in the same sprint.
- Knowledge silos: only one person can deploy or debug a service.

**Relationship to team topology.** Platform teams exist to reduce cognitive load on stream-aligned teams. Enabling teams exist to help stream-aligned teams learn new skills (germane load) without becoming a permanent dependency. Complicated-subsystem teams own domains where the intrinsic load is so high that a specialist team is more effective. Every team topology decision is a cognitive load decision.

### Assured

Cognitive load is a formal input to portfolio and capacity planning.

- **Quarterly review.** Engineering leadership reviews cognitive load scores alongside delivery metrics and DX survey results. Teams with high load and declining metrics get investment (headcount, platform capability, or scope reduction) before they get new work.
- **Capacity model.** When planning a new initiative, estimate the cognitive load it will add to each affected team. If a team is already at capacity, the initiative either waits, goes to a different team, or comes with a plan to offload something else.
- **Organisational health metric.** Track the share of teams with a cognitive load score of 4 or above. Set a target (for example, under 10%) and report it to the executive team. A rising share means the organisation is growing faster than its ability to absorb complexity.
- **Platform investment case.** Use cognitive load data to justify platform investment. "Five stream-aligned teams each spend 15% of their time on CI pipeline maintenance" is a stronger case than "we should build a platform" without data.

## Cloud, on-premises and air-gapped

Cognitive load is a people and organisation measure, not an infrastructure measure. The survey and the practices work the same way regardless of where the systems run. Teams in air-gapped environments may have higher extraneous load from manual processes (deployments, patching, certificate rotation) that would be automated in cloud environments. Measure it, and use the data to justify automation investment.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Adding a fifth service to a team of 4 because they are "the best team" | Check their cognitive load score first. Being good does not mean having infinite capacity. |
| Splitting a team by technology layer (frontend team, backend team) | Split by domain. Layer splits increase coordination load. See [team topology](team-topology.md). |
| Using cognitive load as an excuse to avoid hard work | Intrinsic load is real and necessary. Reduce extraneous load, not the domain. |
| Measuring cognitive load once and never again | Quarterly, same questions. Load changes as services grow and teams change. |
| Platform team that adds complexity instead of removing it | A platform team that requires 20 configuration files to deploy a service has moved load, not removed it. Measure whether stream-aligned teams actually spend less time after the platform launches. |
| Ignoring the data because "everyone is busy" | High cognitive load predicts attrition, rising defects and slowing delivery. The data is an early warning, not a complaint. |

## Templates

- [Team cognitive load survey](../../templates/docs/team-cognitive-load-survey.md) (if available)
- [Team API template](../../templates/docs/team-api.md) (if available)

## Sources

- Skelton, Pais. Team Topologies: Organizing Business and Technology Teams for Fast Flow. IT Revolution, 2019: https://teamtopologies.com
- Team Topologies cognitive load assessment: https://teamtopologies.com/key-concepts
- Sweller. Cognitive Load Theory. Springer, 2011
- Forsgren, Humble, Kim. Accelerate: The Science of Lean Software and DevOps. IT Revolution, 2018
