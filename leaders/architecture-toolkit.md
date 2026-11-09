# Architecture toolkit

A senior architect's job is to make the important trade-offs visible early, when they are still cheap to change, and then get out of the way. Keep a small kit you use every week: a shared list of quality attributes, testable scenarios, a short review checklist, a trade-off matrix, C4 diagrams, fitness functions and reference architectures. Say no rarely, in writing, and always with a path forward. The practice behind this page is in [architecture practice](../playbook/architecture/architecture-practice.md).

## When to use this

| Situation | Tool on this page | Time |
|---|---|---|
| A new system or major change is being designed | Quality attributes, then scenarios | 60 to 90 minutes |
| A team asks for an architecture review | Review checklist | 90 minutes, answer within 5 working days |
| Two or three designs compete | Trade-off matrix | 60 minutes |
| Nobody agrees what the system looks like | C4 context and container diagrams | 2 hours |
| A standard keeps being broken | Fitness function | half a day to write the first one |
| Several teams build the same kind of system | Reference architecture | 2 to 4 weeks, owned by one team |
| A proposal adds risk without enough benefit | When to say no | one decision record |

## Quality attributes (ISO/IEC 25010:2023)

Use the product quality model in ISO/IEC 25010:2023 as a shared vocabulary, so a team cannot forget a whole category. Pick the top five for each system and rank them. A system that ranks everything first has no architecture, only hopes.

| Characteristic | Question to ask | Example measure |
|---|---|---|
| Functional suitability | Does it do what users need, correctly? | defects found in acceptance per release |
| Performance efficiency | How fast, with how many resources, at what load? | p95 latency at peak load |
| Compatibility | Can it run beside and exchange data with other systems? | integrations working after each upgrade |
| Interaction capability (usability in the 2011 edition) | Can the intended users, including disabled users, do their task? | task completion rate, WCAG 2.2 AA conformance |
| Reliability | Does it keep working and recover? | SLO attainment, recovery time |
| Security | Does it protect data and resist attack? | critical findings open past target, time to revoke access |
| Maintainability | Can the team change it safely? | change lead time, change fail rate |
| Flexibility (portability in the 2011 edition) | Can it move, scale or adapt to new environments? | time to deploy in a new region or on-premises |
| Safety | Can it cause harm to people or property, and does it fail safe? | hazards with tested mitigations |

## Quality attribute scenarios

A quality attribute is only useful when it is testable. Write it as a scenario in the form used in SEI work on software architecture.

| Part | Performance example | Modifiability example | Security example |
|---|---|---|---|
| Source | 5,000 concurrent customers | a product team | an outside attacker |
| Stimulus | submit orders | adds a new payment method | replays a stolen session token |
| Environment | end-of-month peak | normal development | production, normal operation |
| Artefact | order service | payments module | customer API |
| Response | orders are accepted and confirmed | change made, tested and deployed | request rejected and alert raised |
| Response measure | p95 under 500 ms, error rate under 0.1% | within 5 working days, no change outside the module | rejected within one request, alert within 5 minutes |

The numbers are illustrative. Each scenario should become either a test, a fitness function or a monitored SLO. A scenario that cannot be checked is a wish.

## Lightweight architecture review

Review only designs that meet a trigger in [engineering governance](../playbook/operating-model/engineering-governance.md): hard to reverse, three or more teams affected, off the [tech radar](../playbook/architecture/tech-radar.md), regulated data or high-risk AI. Everything else uses a [decision record](../playbook/architecture/decision-records.md). Large proposals go through an [RFC](../playbook/architecture/rfcs.md) first.

**Agenda (90 minutes).**

| Minutes | Item |
|---|---|
| 10 | The team presents the problem, the top five quality attributes and the context diagram. Reviewers have read the document beforehand. |
| 30 | Walk the top three scenarios through the design. Note sensitivity points, trade-off points and risks. |
| 30 | Go through the checklist. Skip items that do not apply, and say why. |
| 15 | Agree the outcome: approve, approve with conditions, or rework. |
| 5 | Record the outcome and conditions in the decision record. |

**Checklist questions (full version in the template).**

1. Are the top quality attributes written as measurable scenarios?
2. Is the decision reversible? If not, what would it cost to reverse in two years?
3. What happens when each dependency is slow or down?
4. Where does personal or regulated data flow, and where is it stored?
5. How is it deployed, rolled back and observed?
6. What does it cost to run at today's load and at 10 times today's load?
7. Does it follow a reference architecture? If not, why not?
8. Who owns it in production, and do they have the skills?
9. What is the exit plan for each supplier or product it depends on?
10. Which fitness functions will check that the design stays true?

## Trade-off matrices

Use a trade-off matrix when two or three options compete and the team keeps arguing past each other.

1. List the top five quality attributes as rows, with weights that add up to 100.
2. List the options as columns. Make the current design or simplest option the baseline.
3. Score each option against the baseline from -2 (much worse) to +2 (much better).
4. Multiply by the weight and add up. Then look for sensitivity points (one choice that moves one quality a lot) and trade-off points (one choice that helps one quality and hurts another).

| Attribute (weight) | Baseline: synchronous API calls | Option B: events through a message broker | Option C: shared database |
|---|---|---|---|
| Reliability (30) | 0 | +2 | -1 |
| Maintainability (25) | 0 | +1 | -2 |
| Performance efficiency (20) | 0 | -1 | +1 |
| Security (15) | 0 | 0 | -1 |
| Operability skills (10) | 0 | -1 | +1 |
| **Weighted total** | **0** | **+55** | **-65** |

Fictional example. Treat totals within 20 points of each other as a tie (a starting point; the range runs from -200 to +200). Settle a tie on reversibility, then on what the team can run. The matrix supports judgement. It does not replace it.

## C4 diagrams

Draw systems with Simon Brown's C4 model: context, containers, components, code. Context and container diagrams are required for every critical system. Components are optional. Code-level diagrams are usually generated or skipped.

A good C4 diagram has a title, a key, a label on every arrow saying what flows and how (for example "sends orders, HTTPS/JSON"), the technology on every container, and a date. Keep diagrams as code in the repository and review them in pull requests.

## Fitness functions

A fitness function is an automated check that an architecture characteristic still holds, from "Building Evolutionary Architectures" (Ford, Parsons and Kua, 2017). Write one when a standard keeps being broken, or when a review keeps asking the same question.

- **One characteristic or several.** Some checks test one characteristic, such as layering. Others test several together, such as latency while a dependency is failing.
- **Triggered or continual.** A triggered check runs on an event, such as each build. A continual check runs all the time, such as a production monitor.

Start with three checks for the qualities that hurt most when they break. Examples are on the [architecture practice](../playbook/architecture/architecture-practice.md) page. Each fitness function replaces a manual review question. Remove the question from the checklist once the check is in CI.

## Reference architectures

A reference architecture is a working, deployable example of a common kind of system. Each one contains: context and container diagrams, the quality attribute scenarios it meets, the fitness functions that check it, a template on the [golden paths](../playbook/platform/golden-paths.md), a named owning team and a review date. For scaling choices, start from [scaling](../playbook/architecture/scaling.md). Retire a reference architecture when fewer than two teams use it.

## When to say no

Say no when a proposal is hard to reverse and the benefit is not shown, when it breaks a top quality attribute without a plan, when it adds a technology the organisation cannot run, or when it duplicates a platform that already works. Spend review effort on one-way doors (hard to reverse) and let teams decide two-way doors themselves. The test and the time limits for each kind are in [decision making](decision-making.md).

| Instead of | Say |
|---|---|
| "No." | "Not in this form. If the design meets these two scenarios, it is approved." |
| "Use the standard." | "The standard does X. Show the case it cannot handle and we will change the standard." |
| A verbal veto | A decision record with the reason, the conditions and a review date |

If you say no to more than about one review in five, the triggers or the reference architectures are wrong. Fix those first.

## Common mistakes

| Mistake | Fix |
|---|---|
| Every quality attribute ranked "high" | Force a ranking of the top five. |
| Scenarios with no numbers | Add a response measure, or drop the scenario. |
| Reviews after the build | Review at design time, with triggers everyone can read. |
| Diagrams with unlabelled boxes and arrows | Use C4 with a key and labelled arrows. |
| Standards enforced by memory | Turn the most-broken standard into a fitness function. |
| Reference architectures nobody uses | Ask teams why, fix or retire them. |
| Architects who no longer read code | Spend part of each week in code, incidents and production data. |

## Templates

- [Architecture review checklist](../templates/leaders/architecture-review-checklist.md)
- [Quality attributes checklist](../templates/leaders/quality-attributes-checklist.md)
- [Trade-off matrix](../templates/leaders/trade-off-matrix.md)
- [Decision record](../templates/docs/adr.md)
- [RFC](../templates/docs/rfc.md)
- [Tech radar](../templates/architecture/tech-radar.csv)

## Sources

- ISO/IEC 25010:2023, Systems and software engineering, Systems and software Quality Requirements and Evaluation (SQuaRE), Product quality model, ISO.
- Len Bass, Paul Clements and Rick Kazman, "Software Architecture in Practice", Addison-Wesley (quality attribute scenarios).
- Rick Kazman, Mark Klein and Paul Clements, "ATAM: Method for Architecture Evaluation", CMU/SEI-2000-TR-004, Software Engineering Institute, 2000: https://www.sei.cmu.edu
- Neal Ford, Rebecca Parsons and Patrick Kua, "Building Evolutionary Architectures", O'Reilly Media, 2017.
- Simon Brown, The C4 model: https://c4model.com
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/
