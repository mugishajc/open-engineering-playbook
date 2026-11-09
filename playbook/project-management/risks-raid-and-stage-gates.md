# Risks, RAID logs and stage gates

The problem: most RAID logs are written for the auditor and read by nobody, and most stage gates have never stopped anything. Keep one RAID (risks, assumptions, issues and dependencies) log per project and run the weekly meeting from it. Every item has an owner, a next action and a date, and the top items change what people do this week. At every gate, choose between continue, continue with conditions, rescope, pause and stop. Judge against criteria written before the stage began, and on remaining cost and remaining value only.

## Outcomes

Starting points. Tune them to your organisation.

- Every open RAID item has an owner, a next action and a due date. No item has a next action more than 5 working days overdue.
- Every assumption has a date by which it will be tested. Assumptions past that date are confirmed, or turned into risks or issues.
- Every external dependency has an owner on the providing side and a needed-by date that the provider has agreed.
- A risk or issue above the project manager's tolerance reaches the steering group within 5 working days, and the enterprise risk register when it is above appetite.
- Every gate has criteria published before the stage starts and a written decision within 5 working days of the stage ending.
- Across the portfolio, gates sometimes rescope or stop work. Each year, at least one gate does, or the annual review records why none should have.

## The RAID log

RAID stands for risks, assumptions, issues and dependencies. PRINCE2 keeps separate risk and issue registers; many teams add assumptions and dependencies and keep all four in one log. Some teams use the D for decisions; keep decisions in a separate decision log instead, so they are easy to find.

| Type | What it is | Fields that matter | Becomes |
|---|---|---|---|
| Risk | something that may happen and would affect the objectives | cause, event and effect; probability; impact in days and money; proximity (when it could happen); trigger; response (avoid, reduce, transfer, share, accept, or a prepared fallback); owner; next action | an issue when it happens |
| Assumption | something the plan treats as true without proof | how and by when it will be tested; owner; impact if false | a risk or issue if it proves false |
| Issue | something that has happened, or is certain | severity, owner, resolution action, due date, escalation level | closed, with what was done |
| Dependency | something the project needs from outside, or provides to others | provider, consumer, needed-by date, agreed by provider (yes or no), buffer | an issue when a date is missed |

Use the [RAID log template](../../templates/project/raid-log.csv). For risks that belong to the whole organisation, use the enterprise [risk register](../../templates/strategy/risk-register.csv); the RAID log is the project's working list.

## Make the log drive action

1. **One log per project,** in a shared tool everyone can edit, not inside a slide deck.
2. **Review it weekly for 30 minutes.** Sort by score and proximity. Each of the top 10 items leaves the meeting with an action due within 2 weeks.
3. **Write risks as cause, event and effect:** "Because the supplier's test environment is shared with two other clients, integration testing may slip, which would delay go-live by about 4 weeks." A risk written as one word ("testing") cannot be acted on.
4. **Give every top risk a trigger:** a measurable early warning, such as "fewer than 3 test environment days a week for 2 weeks running". When the trigger fires, start the response without waiting for the next meeting.
5. **Size top risks in days and money.** Exposure is probability as a percentage times impact. The 1 to 5 score sorts the log; it cannot be added up. The sum of the open money exposure is what contingency is held against. See [planning fixed scope and budget](planning-fixed-scope-and-budget.md#contingency-and-management-reserve).
6. **Test assumptions on purpose.** Each assumption has a date and a test: a spike, a call with the supplier, a sample of real data. An assumption nobody has tested by the start of build is a risk.
7. **Escalate by rule, not by mood.** Above the project manager's tolerance goes to the steering group. Above the organisation's risk appetite goes to the enterprise register and, if it qualifies, the [board report](../../leaders/board-and-executive-reporting.md).
8. **Clean it.** An item nobody has touched for 4 weeks is closed with a reason or rewritten. A log of 200 items with no actions is a sign that nobody uses it.
9. **Keep closed items** with their closing reason. They feed the lessons learned and the next project's pre-mortem.

Start every project above the small threshold with a [pre-mortem](../../templates/leaders/pre-mortem.md): imagine the project has failed and list why. The answers seed the first RAID log.

## Dependencies across teams and suppliers

- Draw the dependencies on one page: who needs what from whom, by when. Mark those with a date that cannot move (contracts, hardware deliveries, legal dates).
- Agree each dependency with the providing team's owner, not only with the project. A date the provider has not agreed is an assumption.
- Forecast your part from the provider's agreed date, as [planning and forecasting](../ways-of-working/planning-and-forecasting.md#standard) describes.
- Reduce dependencies rather than manage them. If the same two teams depend on each other every quarter, change the [team topology](../operating-model/team-topology.md) or the interface between them.

## Stage gates that can stop work

A stage gate is a decision point between stages of a project, where the sponsor decides whether to fund the next stage. PRINCE2 calls this managing by stages. A gate that only checks that documents exist adds delay and no control.

| Gate decision | Choose it when |
|---|---|
| Continue | exit criteria met; the forecast is inside tolerance |
| Continue with conditions | criteria mostly met; named gaps have owners and dates before the next gate |
| Rescope | the outcome is still worth it, but scope, date or cost must change; a re-baseline is approved |
| Pause | an external event (funding, a law, a supplier) must settle before more money is spent; set a date to decide again, and say what the team does meanwhile, because a paused team still costs money |
| Stop | the remaining value no longer justifies the remaining cost, or a written stop condition was met |

Rules:

1. **Criteria come first.** Write the exit criteria and stop conditions in the [charter](../../templates/project/project-charter.md) before the stage starts, as numbers where you can. For example: "stop if the migration rehearsal does not reconcile 100% of account balances by the end of alpha".
2. **Evidence, not documents.** The panel sees working software in a production-like environment, test results from the pipeline, reconciliation reports from migration rehearsals, the current forecast range and the top RAID items. A plan is evidence only of intent.
3. **One decision maker.** The sponsor decides, advised by the steering group. For large projects, include one independent reviewer who does not report to the sponsor.
4. **Ask "would we start this today, knowing what we know now?"** Ignore money already spent. See [how to stop work](../strategy/portfolio-and-capacity.md#how-to-stop-work).
5. **Fund only the next stage.** Finance releases money for a stage only against a recorded gate decision, so a missed gate stops spending instead of being skipped. Release contingency that the stage did not need.
6. **Write the decision down** with its reason and tell the team within 2 working days.
7. **Treat a stop as a good result** when the evidence supports it. Release the team to the next priority within 2 weeks.
8. **Do not let conditions become a habit.** Each condition on a "continue with conditions" has an owner and a date. A condition not met by its date sends the decision back to the sponsor. The same criterion passed with conditions at two gates in a row counts as not met.

Use the [stage gate checklist](../../templates/project/stage-gate-checklist.md).

### A gate map for digital projects

The gates follow the GOV.UK Service Manual phases. The [transition playbook](../strategy/transition-playbook.md#the-phases) uses the same idea for changes to how teams work.

| Gate | Before | Main question | Typical evidence |
|---|---|---|---|
| 0. Start | discovery | Is the problem worth studying? | problem statement, sponsor, discovery budget |
| 1. End of discovery | alpha | Is there a real user need and a viable way to meet it? | user research, options including "do nothing", first estimate range with its reference class |
| 2. End of alpha | beta or build | Have the riskiest assumptions been tested? Which option, at what range of cost? | prototypes tested with users, technical spikes, narrowed estimate, supplier award if any |
| 3. Go/no-go | release to all users | Is it ready to run and to support? | the go/no-go criteria below |
| 4. Close | handover | Is the owning team ready, and the old system off? | handover record, RAID transferred, benefits review booked |

### Go/no-go before go-live

Agree the criteria at least 4 weeks before the go/no-go meeting, and do not change them in the meeting. The date is not a criterion.

- All Must have scope accepted by the business owner. See the [UAT sign-off template](../../templates/quality/uat-sign-off.md).
- No open severity 1 defects; open severity 2 defects within an agreed limit, each with a workaround the support team has tested.
- Performance tested at the expected peak plus an agreed margin. See [performance testing](../quality/performance-testing.md).
- Security testing done and findings within appetite. See [security testing](../quality/security-testing.md).
- The final data migration rehearsal reconciled to the agreed threshold: 100% for money and legal records, and an agreed rate such as 99.9% of other records identical.
- Rollback or fall-back tested, with a decision time agreed for the cutover weekend.
- The [production readiness review](../reliability/production-readiness.md) passed, support staffed, users trained, communications ready.
- The cutover plan below rehearsed end to end, with the last rehearsal inside the outage window.

A criterion with no current evidence is not met. "The performance test has not been run" means no, not "probably fine". The business owner and your own test lead sign the readiness evidence; a supplier's report alone is not enough.

### Cutover and rollback

The cutover is the hours or days in which the old system stops and the new one starts. Plan it as a timed runbook, not a slide.

1. **Write the runbook** step by step: task, owner, planned start and duration, dependency, and how success is checked. Include the business steps (stop taking new work, final balances, the first business transactions to check) as well as the technical ones.
2. **Rehearse it at least twice** with real data volumes and the real people, and time every step. Plan the outage window from the rehearsed times plus a margin, not from the estimates.
3. **Mark checkpoints.** At each checkpoint a named decision maker chooses continue or roll back against written criteria, for example "data load reconciled to 100% of balances by 02:00".
4. **Find the point of no return:** the step after which going back costs more than fixing forward, such as payments sent to a bank or customers using the new system. Before it, rollback must be rehearsed and must fit in the time left in the window. After it, the plan is fix forward, with the fix team and the decision makers on call.
5. **Plan the reverse path for data.** If users can create records in the new system before a rollback, decide how those records reach the old system, or limit what users can do until the point of no return.
6. **Hold a go/no-go on the day,** at the start of the window, against the criteria above, with the runbook status and the latest rehearsal results.
7. **Run hypercare** after go-live: the project team and supplier stay on call with daily checks, for a set period such as 2 to 6 weeks or until the first full business cycle has run (a month end, a payroll, a billing run). Hypercare ends on written exit criteria, such as incident volume back to an agreed level and no open severity 1 or 2 defects.

Where the release can be done gradually with [feature flags](../delivery/feature-flags.md) or by moving groups of users, do that instead and keep the cutover only for the one-way steps. See [projects and products](projects-and-products.md#continuous-delivery-changes-what-go-live-means) and [release management](../delivery/release-management.md).

## Practice

### Foundation

Solo, Startup and SME. A short risk list in the backlog, top 5 reviewed weekly, each with an owner and next step. One written stop condition for any project with real money at stake. A go/no-go checklist before any launch that cannot be undone.

### Standard

Scale-up and Enterprise. A RAID log per project, reviewed weekly. A pre-mortem at the start. Gates with criteria written in the charter, evidence from working software, and one of the five decisions recorded each time. Go/no-go criteria agreed 4 weeks ahead. A cutover runbook rehearsed at least twice, with a point of no return and a timed rollback.

### Assured

Regulated and Public sector. Everything in Standard, plus independent assurance at the alpha and go/no-go gates and gate records kept for audit. For the largest projects, add a quantified risk analysis: a Monte Carlo of cost and date that includes the top risks. Link project risks to the enterprise register. Financial entities in the EU need an information and communication technology (ICT) project management policy that covers objectives, governance, planning, risk assessment, milestones, change management and testing. Projects that affect critical or important functions are reported to the management body. This is required by Article 15 of Commission Delegated Regulation (EU) 2024/1774, the EU DORA regulation's technical standard on ICT risk management. Public bodies follow their national assurance process and service assessments; see [public sector](../compliance/public-sector.md).

## Cloud, on-premises and air-gapped

The RAID log and gates work the same everywhere. On-premises and air-gapped projects carry more dated dependencies (hardware delivery, data centre space, software imports, security accreditation); give each one a needed-by date and a provider owner. Cloud projects should log quota limits, region availability and commitment discounts as dependencies or assumptions.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A RAID log nobody reads | Run the weekly meeting from it; every top item leaves with an action. |
| Risks written as one word | Cause, event, effect, with impact in days and money. |
| Assumptions that are never tested | A test and a date for each one. |
| Dependencies agreed only on your side | The providing owner agrees the date, or it is an assumption. |
| Gates that check documents | Gates see working software and measured results. |
| A gate that has never stopped anything | Write stop conditions before the stage; honour them. |
| The go-live date as the deciding criterion | Go/no-go criteria agreed 4 weeks ahead; the date is not one of them. |
| Conditions carried from gate to gate | A missed condition returns the decision to the sponsor. |
| A cutover with no rehearsed rollback | Rehearse twice, time it, mark the point of no return. |
| Risk exposure added up from 1 to 5 scores | Probability as a percentage times impact in money. |
| Money already spent used as a reason to continue | Decide on remaining cost and remaining value only. |

## Templates

- [RAID log](../../templates/project/raid-log.csv)
- [Stage gate checklist](../../templates/project/stage-gate-checklist.md)
- [Project charter](../../templates/project/project-charter.md)
- [Pre-mortem](../../templates/leaders/pre-mortem.md)
- [Risk register](../../templates/strategy/risk-register.csv)

## Sources

- AXELOS (PeopleCert), Managing Successful Projects with PRINCE2, 7th edition, 2023.
- Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK Guide), 8th edition, 2025, risk performance domain; the 7th edition (2021) covered the same ground as its uncertainty performance domain: https://www.pmi.org/standards/pmbok
- Louis Anthony Cox Jr., "What's Wrong with Risk Matrices?", Risk Analysis 28(2), 2008.
- UK Government, Service Manual, agile delivery and the phases of a service: https://www.gov.uk/service-manual/agile-delivery
- Gary Klein, "Performing a Project Premortem", Harvard Business Review, September 2007: https://hbr.org/2007/09/performing-a-project-premortem
- Commission Delegated Regulation (EU) 2024/1774, regulatory technical standards on the ICT risk management framework: https://eur-lex.europa.eu/eli/reg_del/2024/1774/oj
- ISO 31000:2018, Risk management: Guidelines. International Organization for Standardization.
