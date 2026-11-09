# Projects and products

The problem: organisations run long-lived software as projects that end at launch, so the service loses its team the day it goes live. Others run a contracted, deadline-bound change across ten teams and three suppliers with no plan at all. Fund a persistent product team for anything that will change for more than a year. Wrap a project around it when there is a fixed end, a contract, a legal date, or a change that many teams and business units must make together. The project manages the edges (money, contracts, dependencies, cutover, the people outside engineering). The teams own how the software is built and shipped.

## Outcomes

Starting points. Tune them to your organisation.

- Every funded piece of work is labelled project or product in the portfolio, and every project names the persistent team that will run what it builds before its first gate.
- No service is left without a funded owning team when its project closes. Target: zero.
- At least 80% of the measures in project status reports come straight from team systems (work tracker, CI, test results, finance), not from manual collection.
- Project routines add no more than 1 hour per engineer per week on top of the team's own routines.
- Every project closes within 6 weeks of handover with a closure report and lessons learned, and has benefits reviews booked at 6 and 12 months.
- Every benefit in the business case has a named business owner and a baseline measured before go-live.
- Delivery metrics of the teams inside a project are no worse than their baseline for more than one quarter. See [metrics](../measurement/metrics.md).

## Project or product: decide first

A project is temporary: it has a start, an end and a defined result. A product (or service) is persistent: it is changed for as long as people use it. A programme is also temporary, but larger: a group of related projects and business change run together to reach outcomes and benefits that no single project delivers. A portfolio is the whole set of work an organisation funds, and it never ends. Most technology work in a modern organisation is product work, but projects and programmes are still the right tool for some jobs.

| | Project | Programme | Product | Portfolio |
|---|---|---|---|---|
| Exists to | deliver a defined result | change the organisation and realise benefits | serve users for as long as they need it | choose and balance what gets funded |
| Ends when | the result is accepted and handed over | the benefits are embedded in normal business | the product is retired | never; reviewed every quarter |
| Accountable person | sponsor, with a project manager | senior responsible owner, with a programme manager | product manager, with the owning team | portfolio owner, usually an executive |
| Judged by | result within agreed tolerances | benefits realised | outcomes for users and the business | value from the whole set of work |

Call something a programme only when it needs coordinated business change and benefits management across several projects. Ten unrelated projects under one name are a portfolio slice, and a programme structure on top of them adds meetings and nothing else.

| Signal | Run it as | Why |
|---|---|---|
| The thing will be changed for more than a year after launch | A product, with a persistent funded team | Project funding ends at launch and leaves the service without owners |
| The work is mostly finding out what to build | A product, in discovery | A plan written before discovery fixes the wrong things. See [product discovery](../product/product-discovery.md). |
| The work has a fixed end and a defined result: a migration, a cutover, a decommission, a regulatory change | A project, delivered by existing product teams where possible | Someone has to own the end date, the dependencies and the switch-off |
| Many teams, suppliers or business units must change together by a date | A project or programme on top of the product teams | The cross-team plan, contracts and business readiness need one owner |
| A contract, a law or a tender fixes scope, date or price | A project, with the rules in [planning fixed scope and budget](planning-fixed-scope-and-budget.md) | The constraint is real and has to be managed openly |
| The change alters how teams work, not what they build | A transition, using the [transition playbook](../strategy/transition-playbook.md) | Phases, pilots and switch-off dates are the main risk |

Fund the persistent teams through [portfolio and capacity](../strategy/portfolio-and-capacity.md). Fund a project as a time-boxed claim on those teams' capacity, plus the extra money it needs (suppliers, hardware, licences, business change, parallel running).

## Who owns what

In an organisation that ships continuously, the project does not run the teams' day-to-day work. It runs what no single team can.

| Owned by the teams | Owned by the project |
|---|---|
| The order of the backlog inside the agreed outcome, with the product manager | The charter: outcome, constraints, tolerances, stop conditions |
| Splitting work, forecasting from their own throughput | The plan across teams, suppliers and business units, built from the teams' forecasts |
| Design, code, tests, pipeline, deployment and release mechanics | Contracts and supplier performance, with the [supplier owner](../strategy/suppliers-and-contracts.md) |
| Definition of done and quality bar | Dependencies outside the teams, in the risks, assumptions, issues and dependencies ([RAID](risks-raid-and-stage-gates.md)) log |
| Incident response for their services | Business readiness: training, process change, communications, support model |
| Their own retrospectives | Cutover, data migration rehearsals and the go/no-go decision |
| | Status to the steering group, stage gates, closure and lessons learned |

The product manager decides what is worth building and why, and judges whether it worked. The project manager makes sure the agreed change lands within the agreed constraints, and says early and plainly when it will not. On small projects one person can hold both roles; on large ones, keep them separate so value and delivery are argued in the open. See [product partnership](../ways-of-working/product-partnership.md) and [decision rights](../operating-model/decision-rights.md).

## Continuous delivery changes what go-live means

With [continuous delivery](../delivery/gitops-and-deployment.md), deploying and releasing are separate. Code reaches production weeks before users see it, behind [feature flags](../delivery/feature-flags.md), and the release is a decision to switch it on for a group of users. A project in such an organisation should:

- Deploy to production from the first weeks, dark, so the go-live date tests a decision, not a deployment.
- Release in steps: an internal group, a pilot group of real users, then everyone. Each step has its own go/no-go criteria.
- Keep the project-style cutover only for what cannot be switched gradually: one-way data migrations, a switch of an external interface, contract dates, staff moving to a new process, and switching the old system off.
- Rehearse each cutover end to end, with timings, at least twice. The last rehearsal before go-live must meet the go/no-go criteria. See [database changes](../delivery/database-changes.md) and [running old and new in parallel](../strategy/transition-playbook.md#running-old-and-new-in-parallel).
- Use release management for the mechanics. See [release management](../delivery/release-management.md).

A project that cannot deploy until the end carries all of its integration risk into the last month. Moving that risk earlier is the main reason to join project management with continuous delivery.

## Choose a life cycle per part of the work

Use phases that produce evidence, and choose a predictive or adaptive approach for each part of the work rather than one for the whole project. The PMBOK Guide (7th edition, 2021) treats the development approach as a choice that can differ between deliverables in one project, and the 8th edition (2025) keeps predictive, adaptive and hybrid approaches with tailoring. PRINCE2 (7th edition) has tailoring as one of its seven principles. If the contract is predictive and the software work is adaptive, see [agile delivery inside a fixed contract](planning-fixed-scope-and-budget.md#agile-delivery-inside-a-fixed-contract).

| Part of the work | Usual approach | Why |
|---|---|---|
| Software the organisation will own | Adaptive: small releases, forecasts from throughput | Requirements are learned by using the software |
| Hardware, data centre, network circuits | Predictive: fixed lead times, a dated plan | Orders and deliveries are fixed once placed |
| Contracts and procurement | Predictive, set by procurement rules | Dates and steps are set by law or policy |
| Data migration | Adaptive build, predictive cutover | Mapping rules are found by rehearsal; the cutover weekend is a fixed plan |
| Business change and training | Predictive near go-live, adaptive before | Training needs a stable product; content can grow with each release |

For digital services, the phases in the UK GOV.UK Service Manual are a well-tested shape. Discovery: understand the problem. Alpha: try options and test the riskiest assumptions. Beta: build and run with real users, first private, then public. Live: run and improve. Then retirement. Put a gate at the end of each phase. See [risks, RAID logs and stage gates](risks-raid-and-stage-gates.md#stage-gates-that-can-stop-work).

## Closing a project

1. Hand the service to its owning team with a run budget agreed with finance. See [technology budget and cost](../strategy/technology-budget-and-cost.md).
2. Move every open RAID item to the owning team, the enterprise [risk register](../../templates/strategy/risk-register.csv) or a closed state with a reason. Nothing stays with a project that no longer exists.
3. Switch off the old system on the date in the charter, and end its contracts.
4. Run a lessons learned session within 4 weeks of go-live, with the [lessons learned template](../../templates/project/lessons-learned.md). Record the estimate at each gate and the actual result, so the next estimate has a reference class.
5. End hypercare on its written exit criteria and record the start and end of the supplier's warranty. See [cutover and rollback](risks-raid-and-stage-gates.md#cutover-and-rollback).
6. Pass the benefits to their owners, as below.

## Benefits after go-live

Most benefits arrive after the project has closed, so the project cannot be the one to deliver them. Plan for that from the charter.

- **Name a benefit owner in the business for each benefit,** such as the head of the operations team whose processing time should fall. Not the project manager, who will be gone.
- **Measure the baseline before go-live.** A benefit with no baseline cannot be shown later. Write the measure, the source system and the date it was taken.
- **Write a profile for each benefit:** when it should start, how fast it should grow, and what has to change in the business for it to happen (a process removed, a role changed, an old contract ended). Most benefits need business change that no software delivers by itself.
- **Track leading measures** during and soon after go-live, such as the share of cases handled in the new system, so you see early whether benefits are on course.
- **Record dis-benefits** honestly: a slower process for some users, a new run cost, a period of lower productivity while people learn.
- **Review at 6 and 12 months** against the [business case](../strategy/business-case.md). The sponsor or the senior responsible owner chairs the review. The portfolio owner sees the result.
- **Act on a shortfall.** If a benefit is below 80% of its target at the 12 month review, the benefit owner brings a recovery plan or the business case is restated. Either way, the result goes into the outcome register so the next business case starts from real numbers.

Benefits that cannot be measured are opinions. Leave them in the case as unquantified, and do not count them in the return.

## Practice

### Foundation

Solo, Startup and SME. Most work is product work and needs no project manager. For anything with an external date (a contract, a customer launch, a legal deadline), write a one-page [project charter](../../templates/project/project-charter.md): the outcome, what is fixed and why, the stop conditions and who decides. Check dates and dependencies for 15 minutes once a week.

### Standard

Scale-up and Enterprise. Persistent product teams funded through the portfolio. A project manager for work that crosses teams, suppliers or business units, with a charter, a [RAID log](../../templates/project/raid-log.csv), stage gates, a steering group and a [status report](../../templates/project/status-report.md) every 2 weeks built from team data. Project routines sit on top of team routines and do not replace them.

### Assured

Regulated and Public sector. Everything in Standard, plus a written method tailored from a recognised one: PRINCE2, the PMBOK Guide, ISO 21502, or a national standard such as the UK Government Functional Standard GovS 002 for project delivery. Add independent assurance at the major gates, service assessments for citizen-facing services, and gate records kept for audit. Financial entities in the EU also need a written ICT project management policy under the EU DORA regulation's technical standards. See [risks, RAID logs and stage gates](risks-raid-and-stage-gates.md#practice).

## Cloud, on-premises and air-gapped

The project mechanics are the same everywhere. On-premises and air-gapped work adds procurement, hardware delivery and software import steps with long, fixed lead times. Treat each one as a dated dependency in the RAID log from the first week, because they are often on the critical path and cannot be shortened by adding people.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A project team builds a service and is disbanded at launch | Name the owning team and its run budget before the first gate. |
| The project manager assigns tasks to engineers | Teams plan their own work; the project plans across teams from their forecasts. |
| One big deployment at the end | Deploy dark from the first weeks; release in steps. |
| Status rebuilt by hand from meetings | Pull status from team systems; meet only to decide. |
| One method imposed on hardware, contracts and software alike | Choose predictive or adaptive per part of the work. |
| Project closed with open risks and no owner | Transfer every open item before closure. |
| Benefits owned by the project manager | A business owner per benefit, with a baseline measured before go-live. |
| A programme that is a list of unrelated projects | Run them through the portfolio; use a programme only for coordinated change and benefits. |

## Templates

- [Project charter](../../templates/project/project-charter.md)
- [RAID log](../../templates/project/raid-log.csv)
- [Status report](../../templates/project/status-report.md)
- [Stage gate checklist](../../templates/project/stage-gate-checklist.md)
- [Lessons learned](../../templates/project/lessons-learned.md)
- [Transition charter](../../templates/strategy/transition-charter.md)

## Sources

- Project Management Institute, A Guide to the Project Management Body of Knowledge (PMBOK Guide), 7th edition, 2021, and 8th edition, 2025: https://www.pmi.org/standards/pmbok
- AXELOS (PeopleCert), Managing Successful Programmes (MSP), 5th edition, 2020.
- AXELOS (PeopleCert), Managing Successful Projects with PRINCE2, 7th edition, 2023.
- ISO 21502:2020, Project, programme and portfolio management: Guidance on project management. International Organization for Standardization.
- UK Government, Service Manual, agile delivery and the phases of a service: https://www.gov.uk/service-manual/agile-delivery
- UK Government Functional Standard GovS 002, Project delivery: https://www.gov.uk/government/publications/project-delivery-functional-standard
- Mik Kersten, "Project to Product", IT Revolution, 2018.
- DORA, continuous delivery capability: https://dora.dev/capabilities/continuous-delivery/
