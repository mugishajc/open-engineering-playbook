# IT governance

Boards and audit committees are accountable for technology risk, but the reports they receive are often long, late and unrelated to how software is actually built. At the same time, ITIL-style processes copied without thought can add a week to every change. Connect the two: the board sets direction, risk appetite and investment through a recognised governance model, and engineering shows that it is working through a small set of measures drawn from its own systems. Keep process controls automated so governance does not slow delivery.

## Outcomes

Starting points. Tune them to your organisation.

- The board or audit committee receives a technology report at least once a quarter, no longer than two pages, with 8 to 12 measures and their trends.
- At least 80% of those measures come straight from systems of record (CI, incident, ticketing, finance), not manual collection.
- Technology risk appetite is written down and approved by the board, with numeric thresholds for at least availability, security and supplier concentration.
- At least 90% of production changes follow a standard, pipeline-approved route (see [change management](../reliability/change-management.md)).
- Every governance control engineering owns maps to a practice in [control mapping](../compliance/control-mapping.md).

## How the layers fit

| Layer | Who | Question | Playbook pages |
|---|---|---|---|
| Governance of IT | board, audit committee, ministers or accounting officer | Are we doing the right things, within our risk appetite? | this page |
| Management of IT | CTO, CIO, CISO, heads of engineering | Are we doing things the right way, and getting value? | [technical strategy](../strategy/technical-strategy.md), [portfolio and capacity](../strategy/portfolio-and-capacity.md), [decision rights](decision-rights.md) |
| Engineering governance | staff and principal engineers, architecture group | Are the standards right, and are they followed? | [engineering governance](engineering-governance.md), [architecture practice](../architecture/architecture-practice.md) |
| Delivery and operations | teams | Is each change safe, tested and traceable? | [delivery](../delivery/continuous-integration.md), [reliability](../reliability/incident-management.md), [security](../security/secure-development.md) |

## Frameworks and how to use them

| Framework | What it is | Use it for | Do not |
|---|---|---|---|
| ISO/IEC 38500 | international standard for the governance of IT by the governing body; its model is Evaluate, Direct and Monitor | defining what the board does and does not do about IT | treat it as a process manual; it is deliberately short |
| COBIT 2019 (ISACA) | governance and management framework with objectives in five domains: EDM (Evaluate, Direct and Monitor), APO (Align, Plan and Organise), BAI (Build, Acquire and Implement), DSS (Deliver, Service and Support), MEA (Monitor, Evaluate and Assess) | mapping governance objectives to owners and evidence; internal audit planning | implement every objective at the same depth; COBIT expects you to tailor using its design factors |
| ITIL 4 (PeopleCert, formerly Axelos) | service management guidance built around a service value system: guiding principles, governance, the service value chain, practices and continual improvement | service desk, incident, problem, request and change enablement practices for live services | run a manual change board for every change; ITIL 4 itself calls the practice "change enablement" and expects standard changes to be pre-authorised |

Pick one framework as the language for the board and auditors (often COBIT in regulated firms). Map it once to the engineering practices in this playbook. Do not run parallel process sets for each framework.

## Keeping ITIL-style processes from slowing delivery

| ITIL-style process | Fast, compliant version |
|---|---|
| Change enablement | standard changes pre-authorised when the pipeline checks pass; normal changes reviewed in the pull request by the right people; a change board only for major changes |
| Incident management | the same process for engineering and the service desk; on-call engineers own incidents for their services; see [incident management](../reliability/incident-management.md) |
| Problem management | [postmortems](../reliability/postmortems.md) with tracked actions, linked to the problem record |
| Release management | [release management](../delivery/release-management.md) with automated notes and evidence |
| Configuration management | configuration and infrastructure in code; the service catalogue generated from repositories, not typed in |
| Service level management | SLOs agreed with users and reported automatically, see [service levels](../reliability/service-levels.md) |

## Policies and risk appetite

- Keep a short set of technology policies (security, acceptable use, data, AI, supplier, change, resilience), each approved by a named executive, each reviewed at least every 2 years.
- Express risk appetite as thresholds the board can check, for example: "No more than 4 hours of unplanned downtime per quarter for tier 1 services", "Actively exploited vulnerabilities on internet-facing systems fixed within 72 hours, other critical ones within 7 days", "No single supplier supports more than two critical functions without an approved exit plan". These are illustrative; set your own.
- Link each threshold to a measure in the board report and to the risk register.

## Board report: a small set of measures

Use 8 to 12 measures. Show the trend for the last 4 quarters and the risk appetite threshold.

| Area | Measure |
|---|---|
| Delivery | deployment frequency and change lead time for tier 1 services |
| Stability | change fail rate and failed deployment recovery time |
| Availability | SLO attainment for tier 1 services |
| Security | open critical and high vulnerabilities past their fix deadline |
| Incidents | major incidents and their customer impact; reports made to regulators |
| Resilience | date of last successful restore test and failover test for tier 1 services |
| Suppliers | critical suppliers without a tested exit plan |
| Investment | run, grow and transform mix, and the run cost trend |
| People | key-person risks and open senior roles |
| Debt and end of life | systems on unsupported software, with planned dates |
| AI | AI systems in production by risk tier, and those overdue for review |

Write two or three sentences on what changed and what decision, if any, the board is asked to take.

## Public sector IT governance

- **Spend controls.** Many governments require approval from a central digital authority for technology spending above a threshold. UK central government, for example, runs digital and technology spend controls; check which body runs them in your jurisdiction and what the threshold is. Engage early, during Assess in the [transition playbook](../strategy/transition-playbook.md).
- **Assurance gates.** Large programmes pass independent review at fixed points, and citizen-facing services pass service assessments against the national service standard. Plan for them as gates with lead times.
- **Accountability.** An accounting officer or senior responsible owner is personally accountable for value for money. Give them the same short report as a board.
- **Transparency.** Publish spend, performance and decisions where policy requires. See [public sector](../compliance/public-sector.md).

## Practice

### Foundation

Solo and Startup. A founder or CTO reports to the board or investors each quarter on five measures: deployment frequency, major incidents, open critical vulnerabilities, last restore test, run cost. Write three policies: security, acceptable use (including AI), data.

### Standard

Scale-up and Enterprise. Approved risk appetite with thresholds, the board report above, a short policy set, and ITIL-style practices implemented as automated controls. Internal audit uses a single framework mapping.

### Assured

Regulated and Public sector. Everything in Standard, plus a governance framework (COBIT or equivalent) mapped to controls and evidence, audit committee oversight of technology risk, management body accountability where law requires it (for example the EU Digital Operational Resilience Act for financial entities and NIS2 for essential and important entities), and records of board decisions kept for the required period.

## Cloud, on-premises and air-gapped

Governance stays the same in every environment. Reporting does not: measures from air-gapped networks may need manual, approved export. Automate collection inside the network, and export a signed summary on a fixed schedule. Show cloud concentration risk as a supplier measure.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A 40-page board pack | Two pages, 8 to 12 measures, trends and thresholds. |
| ITIL adopted as a set of approval meetings | Pre-authorised standard changes and automated evidence. |
| Separate process sets for each framework | One mapping, one set of controls. |
| Risk appetite with no numbers | Thresholds the board can check each quarter. |
| Governance that sees only projects, not running services | Report on live services: availability, debt, end of life. |

## Templates

- [Risk register](../../templates/strategy/risk-register.csv)
- [RACI](../../templates/strategy/raci.csv)
- [Strategy one-pager](../../templates/strategy/strategy-one-pager.md)

## Sources

- ISO/IEC 38500, Information technology: Governance of IT for the organization, ISO and IEC: https://www.iso.org
- ISACA, COBIT: https://www.isaca.org/resources/cobit
- PeopleCert, ITIL 4: https://www.peoplecert.org
- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
