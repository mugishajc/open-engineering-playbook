# Technical strategy

Write the technical strategy as one page: a diagnosis, a guiding policy and three to seven coherent actions. Review it every quarter and link every action to a decision record, a tech radar entry or a business case. A strategy that names the problem and the trade-offs gets acted on. A list of goals and tools does not.

## Outcomes

Starting points. Tune them to your organisation.

- The strategy fits on one page (about 600 words). Any engineering lead can state its diagnosis in two sentences.
- Every action has a named owner, a date and a measure. At least 80% of actions show measurable progress at each quarterly review.
- At least 70% of significant decision records from the last quarter cite the strategy, or explain why they depart from it.
- Every "Hold" entry on the tech radar cites the strategy or a decision record.
- When asked "what are we not doing?", five randomly chosen leads give the same answer.

## What a strategy contains

The playbook uses the kernel from Richard Rumelt's "Good Strategy Bad Strategy" (2011) without changes.

| Part | Question it answers | Engineering example |
|---|---|---|
| Diagnosis | What is going on? What is the hardest part? | "Releases take three weeks because 14 services share one database schema and one release train. Most incidents start with a schema change." |
| Guiding policy | What approach will we take? What will we stop doing? | "Each service owns its data. No new tables go into the shared schema." |
| Coherent actions | Which steps, in which order, support each other? | "Q1: freeze the shared schema. Q2: move the two most-changed services to their own databases. Q3: split the release train." |

A good diagnosis is specific enough that someone could disagree with it. A guiding policy rules options out. Coherent actions reinforce one another. A list of unrelated projects is a backlog, not a strategy.

### Horizons

Place each action on one horizon. Review each horizon at a different depth.

| Horizon | Time span (starting point) | Detail required | Commitment |
|---|---|---|---|
| Now | current quarter | owner, dates, measure, budget | committed and funded |
| Next | the following 1 to 3 quarters | owner and expected outcome | planned, funding requested |
| Later | 1 to 3 years | direction only | options kept open on purpose |

Move an item from Later to Next only with a decision record. Remove Later items that have not moved in four quarters, or write one sentence on why they stay.

### How the strategy reaches daily work

- **Decision records** ([decision records](../architecture/decision-records.md)): each significant decision cites the action it serves. A decision that goes against the strategy says so and proposes a change to the strategy.
- **RFCs** ([RFCs](../architecture/rfcs.md)): large proposals open by quoting the diagnosis they address.
- **Tech radar** ([tech radar](../architecture/tech-radar.md)): the guiding policy shows up as Adopt and Hold entries. If the policy is "one relational database engine", the radar shows one engine in Adopt and the others in Hold.
- **Metrics** ([metrics](../measurement/metrics.md)): each action names the measure it should move, such as change lead time or failed deployment recovery time.
- **Business case** ([business case](business-case.md)): actions that need money get a business case. The strategy explains why. The business case explains how much and when it pays back.
- **Transitions** ([transition playbook](transition-playbook.md)): when an action changes how the whole organisation builds software, run it as a phased transition.
- **Portfolio** ([portfolio and capacity](portfolio-and-capacity.md)): actions get capacity and a place on the roadmap through the quarterly portfolio review.

## Practice

### Foundation

Default for Solo and Startup.

1. Write the one-pager in one sitting with the [strategy one-pager template](../../templates/strategy/strategy-one-pager.md). Budget 2 to 4 hours.
2. Diagnosis: list the three things that slow you down or hurt customers most. Pick the one that, once fixed, makes the others easier.
3. Guiding policy: two or three sentences. Include at least one thing you will stop doing.
4. Coherent actions: five at most, all on the Now or Next horizon.
5. Keep the file in the repository, for example `docs/strategy.md`, so it has history. Review it every quarter in 30 minutes.

### Standard

Default for Scale-up and Enterprise.

1. The CTO or head of engineering owns the strategy. Staff and principal engineers draft the diagnosis from evidence: incident data, delivery metrics, cost reports, developer survey results and the [maturity model](../measurement/maturity-model.md) score.
2. Circulate the draft as an RFC for two weeks. Record each objection and how it was resolved.
3. Each group writes a half-page local strategy that cites the organisation strategy. A local strategy that contradicts the top one goes through [escalation](../operating-model/decision-rights.md).
4. Score every action at each quarterly review: on track, at risk, or dropped. Rewrite the diagnosis once a year, or sooner after a major change such as an acquisition, a new regulation or a platform reaching end of life.
5. Publish the strategy to all engineers. A hidden strategy produces guesswork.
6. Keep one tracking table: action, owner, measure, current value, target, status.

### Assured

Default for Regulated and Public sector. Everything in Standard, plus:

1. Map each action to the risks it reduces in the [risk register](../../templates/strategy/risk-register.csv).
2. Record approval: who approved the strategy, when, and in which governance body. Keep superseded versions for the period your records policy sets.
3. Align horizons with budget cycles. In the public sector, the Next horizon matches the next budget submission. See [public sector](../compliance/public-sector.md).
4. Show which external obligations each action supports, for example the EU Digital Operational Resilience Act for financial entities, or a national cloud or open source policy. Link to [control mapping](../compliance/control-mapping.md).
5. Internal audit or the second line of defence checks the trace from strategy to actions to evidence once a year.

## Review cadence

| Activity | Frequency | Time box | Who |
|---|---|---|---|
| Action status check | monthly | 30 minutes | strategy owner and action owners |
| Strategy review | quarterly | 2 hours | engineering leadership, staff and principal engineers |
| Diagnosis rewrite | yearly, or after a major change | 2 to 4 weeks | CTO with staff and principal engineers |
| Radar alignment | twice a year | 1 day | [architecture review group](../operating-model/engineering-governance.md) |

## Cloud, on-premises and air-gapped

The kernel stays the same. The constraints change. Write hosting constraints into the diagnosis, not the actions: "we must run in two national data centres with no internet egress" is a fact that shapes the guiding policy. Lead times also differ. Hardware for on-premises and air-gapped sites can take several months to buy and install, so put it on the Next horizon at the latest. For air-gapped sites, list the tools you can actually import, verify and patch offline. An action that depends on a SaaS product will fail there. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | What it looks like | Fix |
|---|---|---|
| Tool shopping list | "Adopt Kubernetes, a service mesh and a new data platform." | Start from the diagnosis. Each tool must trace to a problem it solves. Tools belong on the radar, not in the strategy. |
| Goals without a diagnosis | "Be cloud native. Ship faster. Improve quality." | Write down what is stopping you today. If you cannot, collect evidence before setting goals. |
| Fluff | Long words, no trade-offs. | Each sentence must rule something in or out. Delete sentences any company could have written. |
| Everything is a priority | Fifteen actions, all marked high. | Cap at seven. Rank them. Name what you will not do. |
| Written once, filed away | No reviews. Nobody cites it. | Quarterly reviews. Decision records must cite it. |
| Strategy by slide deck | Lives in a presentation nobody can find. | Keep it in version control or the wiki, with history. |
| Borrowed diagnosis | "Do what the large tech companies do." | Their problems are not yours. Start from your own evidence. |
| Strategy without money | Actions with no budget or time. | Every Now action has funding. If not, move it to Next. |

## Templates

- [Strategy one-pager](../../templates/strategy/strategy-one-pager.md)
- [Risk register](../../templates/strategy/risk-register.csv)
- [Decision record](../../templates/docs/adr.md)
- [RFC](../../templates/docs/rfc.md)
- [Tech radar](../../templates/architecture/tech-radar.csv)

## Sources

- Richard Rumelt, "Good Strategy Bad Strategy: The Difference and Why It Matters", Crown Business, 2011.
- Thoughtworks Technology Radar: https://www.thoughtworks.com/radar
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
- Michael Nygard, "Documenting Architecture Decisions", 2011: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
