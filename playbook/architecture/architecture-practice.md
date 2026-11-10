# Architecture practice

Architects in many organisations are either absent, so each team reinvents the same structures, or act as gatekeepers whose sign-off every team waits for. Run architecture as an enabling function: make quality attributes and trade-offs explicit, encode the important ones as automated fitness functions, draw systems with one shared notation, and review only the decisions that are expensive to reverse. Measure the architecture group by how fast good decisions get made, not by how many it approves.

## Outcomes

Starting points. Tune them to your organisation.

- Every critical system has its top five quality attributes written as measurable scenarios, reviewed at least once a year.
- At least 60% of architecture standards are enforced by automated fitness functions in CI rather than by review.
- Architecture reviews answer within 5 working days, and fewer than 20% of significant decisions need one.
- Every critical system has current C4 context and container diagrams, updated within 30 days of a structural change.
- Planned architecture work (runway) is visible in the portfolio and takes an agreed share of capacity (see [portfolio and capacity](../strategy/portfolio-and-capacity.md)).

## The architect's role

| Enabling (do this) | Gatekeeping (avoid this) |
|---|---|
| writes reference architectures and golden paths teams can copy | approves every design by meeting |
| pairs with teams early, when changes are cheap | reviews after the design is built |
| makes trade-offs explicit and records them in [decision records](decision-records.md) | issues rulings without stated reasons |
| turns standards into automated checks | relies on people remembering standards |
| owns cross-team concerns: integration, data flows, quality attributes at system level | owns team-internal design choices |
| keeps writing code and reading production data | works only from slides |

In a Startup the CTO or a senior engineer holds this role part time. In a Scale-up, staff and principal engineers hold it inside the [team topology](../operating-model/team-topology.md). Enterprises may add an enterprise architecture function. Keep it small and give it the same response-time targets as everyone else.

## Quality attributes and trade-offs

Every architecture trades one quality for another: latency for consistency, flexibility for simplicity, cost for availability. Write the important qualities as scenarios so they can be tested. The six-part form from SEI work on software architecture is the most useful:

| Part | Example (availability) |
|---|---|
| Source | a cloud zone |
| Stimulus | fails completely |
| Environment | during peak trading hours |
| Artefact | the payments API |
| Response | traffic moves to the remaining zones |
| Response measure | fewer than 0.1% of requests fail and service recovers within 2 minutes |

For decisions with several competing qualities, use a lightweight version of the Architecture Tradeoff Analysis Method (ATAM), developed at the Software Engineering Institute:

1. List the business drivers and the top quality attribute scenarios, ranked by importance and difficulty.
2. Walk through each high-ranked scenario against the proposed design.
3. Record **sensitivity points** (a design choice that strongly affects one quality), **trade-off points** (a choice that affects two or more qualities in opposite directions) and **risks**.
4. Write the result into the decision record.

A full ATAM takes several days with many stakeholders. For most decisions a 2 to 3 hour session with the team, a staff engineer and the main consumers is enough. Keep the full method for critical or regulated systems.

## Fitness functions

A fitness function is an automated check that an architecture characteristic still holds, as described in "Building Evolutionary Architectures" (Ford, Parsons, Kua and Sadalage, 2nd edition, 2022). Examples:

| Characteristic | Fitness function | Where it runs |
|---|---|---|
| Layering | no import from the domain layer to the web layer (for example with ArchUnit or a dependency linter) | CI on every change |
| Coupling | no service calls more than N others synchronously on a request path | CI, from service catalogue and traces |
| Performance | p95 latency of key endpoints under 300 ms in a load test | nightly pipeline |
| Security | no container runs as root; no public storage buckets | CI and policy as code |
| Data residency | no resource created outside approved regions | infrastructure plan check, see [infrastructure as code](../delivery/infrastructure-as-code.md) |
| Operability | every service has SLOs, dashboards and a runbook | [production readiness](../reliability/production-readiness.md) checks |
| AI quality | evaluation score above threshold on the gating eval set | CI on every prompt, model or retrieval change (see [quality engineering](../quality/quality-engineering.md#in-the-ai-era)) |
| AI latency | model call p95 under budget (for example 2 seconds per turn) | load test or synthetic probe |
| AI cost | cost per request below cap (for example $0.05 per API call) | nightly cost report from the AI gateway |
| AI retrieval | retrieval recall above floor on the reference set | CI on every index or chunking change |

Start with three fitness functions for the qualities that hurt most when they break. Each one replaces part of a manual review.

## Diagrams: the C4 model

Use Simon Brown's C4 model so every diagram uses the same levels:

1. **Context:** the system, its users and the systems it talks to.
2. **Containers:** deployable units (applications, databases, queues) and how they communicate.
3. **Components:** the main parts inside one container.
4. **Code:** usually generated or skipped.

Keep diagrams as code (for example Structurizr DSL, Mermaid or PlantUML) in the same repository, reviewed in pull requests. Context and container diagrams are required for critical systems. Components and code are optional.

## Lightweight reviews with clear triggers

Review a design only when it meets a trigger in [engineering governance](../operating-model/engineering-governance.md): hard to reverse, three or more teams affected, off the [tech radar](tech-radar.md), regulated data or high-risk AI. Everything else uses the advice process and a decision record. Large proposals go through an [RFC](rfcs.md).

### The architecture forum

At Standard and above, one forum handles triggered reviews, cross-team decision records and radar changes. Starting points:

- Meets weekly for 45 minutes. Members: 3 to 6 staff or principal engineers from different teams, plus security when the agenda needs it. Membership rotates every 12 months.
- Gives a first written response within 5 working days of a request, and a decision within 10 working days. The same targets apply in [decision records](decision-records.md).
- Advises; it does not own team designs. The owning team decides unless the change crosses a trigger, and then the named decision-maker from [decision rights](../operating-model/decision-rights.md) decides.
- Publishes its decisions as decision records, and reviews its own response times each quarter.

## When to change the architecture

Architecture should change when evidence says the current structure no longer serves, not when a new pattern becomes fashionable. Open a review when any of these triggers fires (starting points):

| Trigger | Signal to watch |
|---|---|
| A fitness function keeps failing | The same fitness function has failed, or been waived, for two quarters in a row |
| Team cognitive load | A team owns more services than it can operate, or more than about 20% of its pull requests need another team's approval (see [team topology](../operating-model/team-topology.md)) |
| Unit cost rising | Cost per transaction, per customer or per request rises for two quarters while volume grows (see [FinOps](../platform/finops.md)) |
| Scaling headroom | Forecast peak in the next 12 months is within 2 times of the highest load the system has been shown to carry (see [scaling](scaling.md)) |
| New AI workloads | A feature adds model calls with latency, cost or data-handling needs the current design was not built for: seconds rather than milliseconds, per-token cost, GPU capacity, prompts that carry personal data (see [AI architecture patterns](../ai/ai-architecture-patterns.md)) |
| Regulatory change | A new law or rule changes where data may live, how decisions must be explained, or how fast incidents must be reported |
| Repeated incidents | Postmortems name the same structural cause three times in 12 months |

The rule when a trigger fires: change incrementally, behind a decision record. Write the ADR that states the trigger, the options and the measure that will show the change worked. Then move one slice at a time, using the strangler fig or branch by abstraction from [legacy modernisation](legacy-modernisation.md), with a fitness function that guards the new structure. A big-bang redesign needs an [RFC](rfcs.md) that explains why incremental change cannot work.

## Reference architectures

A reference architecture is a worked, deployable example of how to build a common kind of system: a web service, an event consumer, a batch job, a retrieval-augmented AI application. Each one includes C4 diagrams, quality attribute scenarios it meets, the fitness functions that check it, and a template in the [developer platform](../platform/developer-platform.md) or [golden paths](../platform/golden-paths.md). Retire a reference architecture when fewer than two teams use it.

## Architecture runway

Architecture runway is the existing technical foundation that lets upcoming features be built without major redesign. The term comes from the Scaled Agile Framework. Whatever framework you use, keep runway work visible:

- list the runway items each upcoming product goal depends on, at least two quarters ahead;
- fund runway from the platform or technical debt share of capacity, not from spare time;
- stop runway items that no planned goal needs within four quarters.

## Practice

### Foundation

Solo and Startup. Write the top three quality attributes for your product. Draw a C4 context and container diagram. Record big decisions as decision records. Add one fitness function, such as a dependency rule in CI.

### Standard

Scale-up and Enterprise. Staff and principal engineers hold architecture responsibility with a written scope. Quality attribute scenarios for every critical system. Fitness functions for the main standards. Reference architectures for the three or four most common system types. Diagrams as code. Reviews by trigger only, with a 5-day response target.

### Assured

Regulated and Public sector. Everything in Standard, plus full ATAM-style evaluation for critical systems before major change, architecture documentation kept as records, traceability from quality attributes to controls in [control mapping](../compliance/control-mapping.md), and independent review for systems supporting critical or important functions.

## Cloud, on-premises and air-gapped

Write the hosting environment into the context diagram and the quality attribute scenarios: "no outbound internet" is a constraint every container must meet. Reference architectures need on-premises and air-gapped variants that use self-hosted equivalents. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Ivory tower architecture | Architects write code, pair with teams and own outcomes. |
| Architecture by approval meeting | Triggers, advice process, decision records, fitness functions. |
| "Highly available, scalable and secure" as requirements | Quality attribute scenarios with response measures. |
| Diagrams that disagree with production | Diagrams as code, updated with structural changes. |
| Reference architectures nobody uses | Ship them as working templates; retire unused ones. |

## Templates

- [Decision record](../../templates/docs/adr.md)
- [RFC](../../templates/docs/rfc.md)
- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml)
- [Tech radar](../../templates/architecture/tech-radar.csv)

## Sources

- Rick Kazman, Mark Klein and Paul Clements, "ATAM: Method for Architecture Evaluation", CMU/SEI-2000-TR-004, Software Engineering Institute, 2000: https://www.sei.cmu.edu
- Len Bass, Paul Clements and Rick Kazman, "Software Architecture in Practice", Addison-Wesley.
- Neal Ford, Rebecca Parsons, Patrick Kua and Pramod Sadalage, "Building Evolutionary Architectures", 2nd edition, O'Reilly Media, 2022: https://www.oreilly.com/library/view/building-evolutionary-architectures/9781492097532/
- Simon Brown, The C4 model for visualising software architecture: https://c4model.com
- Scaled Agile Framework, Architectural Runway: https://scaledagileframework.com/architectural-runway/
