# Transition playbook

Change how the organisation builds software in five gated phases: Assess, Decide, Pilot, Scale, Sustain. Fund one phase at a time, and at every gate choose one of three outcomes: continue, change scope, or stop. Most failed transitions skip the pilot or never decide when to switch the old way off.

Use this playbook for any change that alters how many teams work, for example:

| Transition | What changes |
|---|---|
| Monolith to services (or services back to a modular monolith) | deployment units, data ownership, team boundaries |
| On-premises to cloud, or cloud back to on-premises | hosting, cost model, operations skills, contracts |
| Sovereignty-driven repatriation | jurisdiction of data and operators, supplier set, support model |
| Manual releases to continuous delivery | release process, test automation, change approval |
| Adopting an internal developer platform | team interfaces, golden paths, platform team funding |
| New source control or CI system | tooling, permissions, evidence trail, training |

## Outcomes

Starting points. Tune them to your organisation.

- Every gate has a written decision (continue, change scope, stop) within 5 working days of the phase ending.
- The pilot meets its exit criteria within 125% of its planned time box, or the gate decides to stop or rescope.
- Old and new run in parallel for no longer than the planned limit (default 6 months per system).
- The old path is switched off on a date set at the Decide gate. Slips longer than one quarter go back to the sponsor.
- Delivery metrics for migrated teams do not get worse for more than one quarter: change lead time, deployment frequency, change fail rate and failed deployment recovery time. See [metrics](../measurement/metrics.md).
- Every role the transition changes or removes has a written plan, agreed with HR and, where they exist, employee representatives, before the Pilot gate.
- No team is in more than one major change at a time.

## Phase overview

Typical durations are planning assumptions, not promises. Public sector and Regulated overlays usually add time at Decide and Scale (see below).

| Phase | Question | Solo | Startup | Scale-up | Enterprise | Lead |
|---|---|---|---|---|---|---|
| Assess | Where are we, and is the change worth it? | 1 to 3 days | 1 to 2 weeks | 3 to 6 weeks | 6 to 12 weeks | staff or principal engineer |
| Decide | Which option, at what cost, with what exit? | 1 day | 1 week | 2 to 4 weeks | 4 to 8 weeks | CTO or head of engineering |
| Pilot | Does it work for one real team? | 1 to 2 weeks | 3 to 6 weeks | 6 to 12 weeks | 8 to 16 weeks | pilot tech lead |
| Scale | Can every team move without hurting delivery? | n/a | 1 to 3 months | 3 to 12 months | 6 to 24 months | programme lead with platform team |
| Sustain | Is the new way the normal way? | ongoing | ongoing | ongoing | ongoing | owning team or platform team |

## The phases

### 1. Assess

- **Purpose:** describe the current state with evidence and decide whether the change is worth studying further.
- **Inputs:** the [technical strategy](technical-strategy.md), delivery metrics, incident history, cost reports, contracts and their end dates, a [maturity model](../measurement/maturity-model.md) self-assessment.
- **Activities:** map systems, teams and dependencies. Measure a baseline for 4 to 8 weeks of data. Interview at least one person from each affected team. List constraints: data residency, contracts, skills, budget year. Draft two to four options, always including "do nothing" and "improve what we have".
- **Outputs:** baseline report, dependency map, option list, first draft of the [risk register](../../templates/strategy/risk-register.csv).
- **Exit criteria:** baseline covers at least 80% of in-scope systems. Each option has a rough cost range. The sponsor agrees in writing to fund the Decide phase.
- **Gate:** stop if the baseline shows the problem is smaller than assumed, or if "improve what we have" meets the goal at less than half the cost.

### 2. Decide

- **Purpose:** choose one option, fund it, and agree in advance how it will be stopped if needed.
- **Inputs:** Assess outputs, [build, buy or adopt](build-buy-adopt.md) scoring, a [business case](business-case.md).
- **Activities:** score the options. Write a decision record. Write the [transition charter](../../templates/strategy/transition-charter.md): scope, sponsor, budget per phase, success measures, stop conditions, switch-off date for the old path. Agree the pilot team. Start any procurement and regulator conversations now.
- **Outputs:** signed charter, decision record, business case, pilot plan, [stakeholder map](../../templates/strategy/stakeholder-map.md).
- **Exit criteria:** sponsor and finance approve Pilot funding. The change impact table (see [people and roles](#people-and-roles)) is complete and consultation has started where required. Success measures have baseline values and targets. Stop conditions are written as numbers, for example "stop if pilot change lead time is more than 20% worse after 8 weeks".
- **Gate:** stop if no option beats "improve what we have" on the business case, or if exit costs are unknown for the chosen supplier.

### 3. Pilot

- **Purpose:** prove the new way with one real team on real work, and find the hidden costs.
- **Inputs:** charter, pilot plan, a working minimum version of the new tooling.
- **Activities:** move one service or product. Run old and new in parallel (see below). Hold a 30-minute retrospective every two weeks. Record every manual step, workaround and missing feature. Write the first migration guide and [golden path](../platform/golden-paths.md).
- **Outputs:** pilot report with before and after metrics, migration guide, updated cost estimate, list of blockers for Scale.
- **Exit criteria:** pilot team ships to production on the new path at least 10 times (or for 4 weeks, whichever is longer). Delivery metrics are no worse than baseline. The pilot team would choose to stay on the new path. Updated Scale cost is within 25% of the Decide estimate.
- **Gate:** continue, run a second pilot with a different team type, or stop. Stopping here is cheap. Treat it as a good result, not a failure.

### 4. Scale

- **Purpose:** move the remaining teams in waves without hurting delivery.
- **Inputs:** pilot report, migration guide, platform team capacity, wave plan.
- **Activities:** group teams into waves of 2 to 5 teams. Each wave gets a fixed window (default 6 weeks), embedded support from the platform or pilot team, and office hours. Track progress weekly. Freeze new features on the old path once 50% of teams have moved. Decommission old components as each wave completes.
- **Outputs:** migrated teams, decommission log, updated runbooks, training records, final cost report.
- **Exit criteria:** at least 90% of in-scope workloads run on the new path. The old path has a published switch-off date within the next quarter. No migrated team has worse delivery metrics than baseline for more than one quarter.
- **Gate (after each wave):** continue, pause to fix shared blockers, or stop and keep a stable hybrid. A planned hybrid is acceptable. An unplanned one is not.

### 5. Sustain

- **Purpose:** make the new way the default and remove the old one.
- **Inputs:** Scale outputs, ongoing metrics, support tickets.
- **Activities:** switch off and archive the old path. Move ownership from the programme to a permanent team. Add the new standards to [engineering governance](../operating-model/engineering-governance.md) and the [tech radar](../architecture/tech-radar.md). Update [onboarding](../people/onboarding.md).
- **Outputs:** closed charter, final decision record, lessons learned, budget moved to run costs.
- **Exit criteria:** old path off and its contracts ended. New starters reach their first production change through the new path only. Run costs are within 15% of the business case.
- **Gate:** close the programme. Review the outcome against the business case 12 months later.

## Choosing the pilot team

Pick a team that meets at least five of these seven criteria:

1. Volunteers, and its manager supports the change.
2. Owns a service that is real and in production, but not the most critical one.
3. Has stable membership for the next 3 months.
4. Has a measured baseline for the metrics the charter names.
5. Has typical dependencies, so the lessons apply to others.
6. Is not your strongest team only. A pilot that works only for experts proves little. If you run two pilots, make the second team an average one.
7. Has a low regulatory impact if things go wrong, or a tested rollback.

## Running old and new in parallel

- **Route, do not rewrite.** Put a routing layer in front of the old system and move capabilities one at a time (the strangler fig approach). Keep the old path working until each capability is switched.
- **One source of truth for data.** During parallel running, one side owns writes. Sync in one direction only, and test reconciliation daily.
- **Compare outputs.** For high-risk systems, run the new path in shadow mode and compare results before switching traffic. Set a match threshold, for example 99.9% of records identical.
- **Use flags for the switch.** Move traffic in steps with [feature flags](../delivery/feature-flags.md) (1%, 10%, 50%, 100%) with a tested rollback at each step.
- **Cap the overlap.** Parallel running doubles operating cost and on-call load. Set a limit in the charter (default 6 months per system) and report the extra cost monthly.

## People and roles

Most transitions fail on people, not tools. Plan the people side with the same care as the technology.

**Change impact table.** In Assess, list every role the change touches. Complete the table before the Decide gate and update it at every gate.

| Role | What changes | When | Support offered | New role or path |
|---|---|---|---|---|
| Release manager | Releases move to the pipeline | Scale, wave 2 | Training on pipeline controls | Platform team, release controls owner |
| Change board secretariat | Most changes pre-authorised | Scale | Help to define standard changes | Change and risk analyst |
| Manual tester | More automated checks | Pilot onwards | Test automation training, pairing | Quality engineer |
| Scrum Master | Fewer ceremonies | Scale | Flow metrics coaching | Delivery lead or engineering manager |

These rows are examples; write your own.

**Rules.**

- No role is removed by the transition without a redeployment or consultation plan agreed with HR and, where they exist, employee representatives, before the Pilot gate. In the EU, Directive 2002/14/EC sets general duties to inform and consult employees; national law often adds more, and changes to systems that can monitor staff may need works council agreement.
- Budget training time per wave. A starting point: 2 days per person moving to the new way, plus pairing during the wave. Correct it after the pilot.
- Check change load before each wave: no team is in more than one major change at once (a reorganisation, a platform move and a new tool count as three).
- Size change support to the programme. For Scale-up, a part-time [technical evangelist](stakeholders-and-communication.md#the-technical-evangelist) per few teams can be enough. For Enterprise, fund a named change team (communications, training, HR partner and evangelists) for the whole of Scale.
- Watch attrition, the team survey and on-call load for affected teams at every gate.

## Funding per phase

Release money one phase at a time. The planning share is a starting point for the expected case and adds up to 100% of the phase budget. The range shows typical variation.

| Phase | Planning share | Typical range | What it pays for |
|---|---|---|---|
| Assess | 4% | 2% to 5% | engineer time for discovery, data collection |
| Decide | 2% | 1% to 3% | option analysis, legal and procurement review |
| Pilot | 15% | 10% to 20% | one team's time, minimum tooling, parallel running |
| Scale | 70% | 55% to 75% | platform team, migration support, double running costs, training, change support |
| Sustain | 9% | 5% to 10% in year one, then normal run budget | decommissioning, contract exit, documentation |
| **Total** | **100%** | | |

Hold contingency **on top of** the phase budget, released only by the sponsor at a gate. For Solo, Startup and Scale-up, 10% to 20% is a starting point. For Enterprise transitions, size it from the outcomes of similar past programmes (reference class forecasting), not a fixed percentage: IT cost overruns have a fat tail, and 10% to 20% is a floor, not a ceiling.

## Practice

### Foundation

Solo and Startup. Write a one-page charter. Assess and Decide can be one sitting. Pilot on one service for two weeks with a rollback ready, then move the rest. Set the switch-off date before you start.

### Standard

Scale-up and Enterprise. Run all five phases with written gate decisions. A steering group of sponsor, programme lead, a staff or principal engineer and a finance partner meets at each gate and monthly. Publish a weekly progress table. Use [decision rights](../operating-model/decision-rights.md) to settle disputes within 5 working days.

### Assured

Regulated and Public sector. Everything in Standard, plus independent review at the Decide and Scale gates, a risk assessment per phase, evidence kept for each gate, and the overlay steps below.

**Public sector overlay.**

- Start procurement in Assess, not Decide. Use existing framework agreements where they exist. Prefer open standards and open source to avoid lock-in. See [public sector](../compliance/public-sector.md).
- Match phase gates to the budget year. Money that is not committed by year end may be lost, so plan Pilot and early Scale within one budget year where you can.
- Plan for ministerial or board sign-off at Decide. Add the approval lead time to the plan.
- Run a service assessment against your national service standard before Scale for citizen-facing services.
- Check data residency and records retention for both old and new paths before Pilot.

**Regulated overlay.**

- Check notification duties in Assess. Financial entities under the EU Digital Operational Resilience Act (Regulation (EU) 2022/2554, unrelated to the DORA metrics research) must keep a register of ICT third-party arrangements and inform the competent authority about planned arrangements for critical or important functions.
- Treat a new hosting or platform supplier as outsourcing. Do due diligence, write an exit strategy, and test it before Scale.
- If the transition touches models used for decisions, such as credit scoring or fraud detection, run model validation before switching traffic.
- Keep separation of duties working on both paths throughout. See [regulated industries](../compliance/regulated-industries.md).

## 90-day starter plan

For a Scale-up or Enterprise starting from zero. Shrink each step for smaller profiles.

| Days | Focus | Done when |
|---|---|---|
| 1 to 10 | Sponsor, scope, team | sponsor named, programme lead named, Assess funded |
| 11 to 30 | Baseline and dependency map | at least 4 weeks of metrics (pulled from existing CI, incident and cost systems), dependency map covers 80% of scope |
| 31 to 40 | Options and business case | 2 to 4 options costed, including "improve what we have" |
| 41 to 50 | Decide gate | charter signed, decision record merged, pilot team agreed |
| 51 to 60 | Pilot setup | minimum tooling ready, rollback tested, parallel run configured |
| 61 to 90 | Pilot running | first production changes on the new path, two retrospectives held, midpoint review against exit criteria written |

The plan compresses Assess and Decide to their shortest, which works only when baseline data already exists in your tools. The Pilot gate falls after day 90: a pilot runs 6 to 16 weeks (see the phase table) and must ship at least 10 times or run 4 weeks, whichever is longer.

## Cloud, on-premises and air-gapped

Moves into or out of a hyperscaler change cost structure: capital spending becomes operating spending, or the reverse. Show both in the business case. For on-premises and air-gapped targets, add hardware lead time to Decide, and pilot the offline update process (packages, images, vulnerability data) before Scale. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Big-bang cutover | Move in waves with a rollback at every step. |
| No switch-off date | Set it at Decide. Report slips to the sponsor. |
| Pilot with the best team only | Run a second pilot with an average team. |
| Funding the whole programme up front | Release funds per phase at each gate. |
| Measuring activity (tickets closed) | Measure delivery metrics and cost against baseline. |
| Roles removed by surprise at the end | Change impact table at Assess; consultation before Pilot. |
| A team in three changes at once | Check change load before each wave. |
| Treating stop as failure | Write stop conditions in the charter and honour them. |

## Templates

- [Transition charter](../../templates/strategy/transition-charter.md)
- [Business case](../../templates/strategy/business-case.md)
- [Risk register](../../templates/strategy/risk-register.csv)
- [Stakeholder map](../../templates/strategy/stakeholder-map.md)
- [RACI](../../templates/strategy/raci.csv)

## Sources

- Bent Flyvbjerg and Alexander Budzier, "Why Your IT Project May Be Riskier Than You Think", Harvard Business Review, September 2011: https://papers.ssrn.com/abstract=2229735
- Directive 2002/14/EC on informing and consulting employees: https://eur-lex.europa.eu/eli/dir/2002/14/oj
- Martin Fowler, "Strangler Fig Application": https://martinfowler.com/bliki/StranglerFigApplication.html
- Regulation (EU) 2022/2554 (Digital Operational Resilience Act): https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
