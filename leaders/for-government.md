# For government technology leaders

Build the shared parts once (identity, payments, data exchange, notifications, hosting) and let ministries build services on top of them, instead of letting every ministry buy its own. Buy outcomes on short contracts with exit terms, keep the knowledge to run critical systems inside the civil service, and fund live services every year as running costs, not as projects that end at launch. Design for the citizen with the slowest connection, the oldest phone and the least common language, because a service that excludes them fails the public it exists for.

## When to use this

This page is for ministers' technical advisers, permanent secretaries, government CIOs and CTOs, and heads of public digital programmes.

- You are setting or resetting a national or ministry digital strategy.
- Several ministries are about to buy the same thing (identity, payments, case management) separately.
- A large programme is late, over budget or locked into one supplier.
- Services launch and then decay because the team was disbanded.
- You need to show a minister, parliament or an audit office that technology spending is under control.

The engineering detail lives in [public sector](../playbook/compliance/public-sector.md), [IT governance](../playbook/operating-model/it-governance.md) and the [public sector profile](../profiles/public-sector.md). This page covers the decisions only senior officials can take.

## First month as a ministry CIO

Five facts to collect before you change anything. Each one feeds a section below. Use [first 90 days](first-90-days.md) for the listening tour.

| Collect | Why | Section |
|---|---|---|
| Every supplier contract with its end date, value and exit terms | contracts ending in the next 18 months are your first decisions | [Procurement for outcomes](#procurement-for-outcomes) |
| The list of systems the ministry cannot work without, and whether a civil servant can explain each one | shows where you depend on a supplier's memory | [In-house capability](#in-house-capability) |
| The date of the last restore test for each of those systems | a backup that has never been restored may not work when you need it | [Cyber resilience](#cyber-resilience-of-national-systems) |
| The budget calendar: submission dates, spend control thresholds, assurance gates | missing a submission date costs a year | [Funding](#funding-continuous-services-in-budget-years) |
| Shared platforms the central digital authority already runs | avoid buying what another ministry already pays for | [Digital public infrastructure](#digital-public-infrastructure) |

## Digital public infrastructure

Digital public infrastructure (DPI) is the set of shared digital systems that many public and private services build on: usually digital identity, payments and data exchange. Build or adopt each once, nationally, with open interfaces.

| Building block | What it gives every service | Example to study |
|---|---|---|
| Data exchange | ministries query each other's registers through a secure, logged layer instead of asking citizens for the same paper twice | Estonia's X-Road, an open source data exchange layer |
| Payments | interoperable, low-cost payments between people, businesses and government | India's UPI |
| Digital identity | one way for a person to prove who they are, with consent and an offline fallback | your national identity authority |
| Notifications | SMS, email and app messages through one service with templates and delivery records | a shared platform run by the central digital team |
| Hosting and platform | approved hosting, CI, registries, secrets and observability that services reuse | [developer platform](../playbook/platform/developer-platform.md) |

GovStack, an initiative backed by ITU, Germany, Estonia and the Digital Impact Alliance, publishes specifications for reusable building blocks. Use it as a checklist when you define your own.

Rules for shared platforms (starting points):

- Each platform has a product owner, a funded team, published service levels and a public roadmap.
- Ministries can adopt it in weeks, not months. Measure time from request to first use; target under 20 working days.
- Interfaces use open standards and are documented in the open, so a ministry can switch supplier without switching platform.
- Adoption is the default, not a mandate enforced by approval. A ministry that wants to build its own explains why in a [decision record](../playbook/architecture/decision-records.md).

## Procurement for outcomes

| Instead of | Do |
|---|---|
| a 300-page specification of features written before any user research | a problem statement, user needs and the outcome measures the supplier will be judged on |
| one contract for 5 to 10 years covering everything | lots of 1 to 2 years with options to extend, sized so smaller and local suppliers can bid |
| payment on delivery of documents | payment for working software in production, reviewed every 2 to 3 months |
| supplier-owned code | public ownership or an open licence for code written with public money |
| exit discussed at renewal | exit terms, data export formats, documentation and transition support in the original contract |

Run discovery with users before writing the tender. Keep a public servant with technical skills in every supplier-staffed team. See [build, buy or adopt](../playbook/strategy/build-buy-adopt.md).

## Exit and sovereignty

- For each critical system, write down how you would leave its supplier: data formats, time needed, cost and who does the work. Test the data export at least once a year.
- Check the legal jurisdiction of the supplier and its parent company, not only the data centre location.
- Classify data and map each class to permitted locations with the [data classification template](../templates/docs/data-classification.md).
- Keep the ability to run the most critical services on infrastructure you control. See [cloud, on-premises and air-gapped](../playbook/platform/cloud-on-prem-air-gapped.md).
- Sovereignty does not mean building everything. It means you can choose, change and audit.

## Open source and open standards

- Default to open standards for data and interfaces. Interoperability between ministries depends on them more than on any platform.
- Consider open source on equal terms with commercial software, including the cost of support.
- Publish code written with public money unless there is a written reason not to (security, policy, third-party rights). Publishing lets other ministries and governments reuse it, and makes procurement exits easier.
- Contribute fixes back to the open source projects you depend on, and fund maintenance of the ones that run national systems.

## Accessibility and inclusion

| Need | Practice (starting point) |
|---|---|
| Disability | meet WCAG 2.2 level AA; automated checks in CI plus a manual audit with assistive technology at least once a year |
| Low bandwidth | pages work on a slow mobile connection; set a page weight budget (for example under 500 KB for key journeys) and test on throttled networks |
| No smartphone or no data | offer USSD or SMS for the most used transactions, and an assisted channel (service centres, agents, phone) |
| Offline and intermittent connectivity | allow forms to be saved and submitted later; issue receipts that can be verified without a connection |
| Local languages | launch in the languages most of the population uses; budget for translation and testing with native speakers as running costs |
| Low digital confidence | test with real users, including older people and first-time users, before every major release |

A digital service that removes the paper or counter option before the digital one works for everyone moves cost onto the people least able to bear it.

## In-house capability

- Keep the roles that make decisions in the civil service: service owners, product managers, architects, security leads and enough senior engineers to review supplier work.
- Pay competitively for scarce skills through a digital pay framework if your rules allow one. Otherwise, the skills leave.
- Measure the share of critical systems where a civil servant can explain how it works and how to change it. Target 100% for Tier 1 systems.
- Use [hiring](../playbook/people/hiring.md), [career framework](../playbook/people/career-framework.md) and [skills gap](../playbook/people/skills-gap.md) for the practice.

## Assurance and spend controls

| Control | Make it useful by |
|---|---|
| Central spend control above a threshold | engaging the central digital authority during discovery, not at contract signature |
| Service assessment against the national service standard | assessing before public beta, before full launch and before retirement |
| Independent assurance gates on large programmes | publishing the gate criteria in advance; each gate can stop or reshape the programme |
| Audit office reviews | giving auditors read-only access to delivery evidence: [control mapping](../playbook/compliance/control-mapping.md) |

Ask for the same measures every quarter, no more than 12, as listed in [IT governance](../playbook/operating-model/it-governance.md). Use [board and executive reporting](board-and-executive-reporting.md) for the format.

## Decisions senior officials keep

In the UK, HM Treasury's Managing Public Money makes the accounting officer personally answerable to Parliament for four tests on spending: regularity, propriety, value for money and feasibility. If a minister asks for spending that fails one of them, the accounting officer can ask for a written ministerial direction, and the minister then answers for that spending. Many governments have an equivalent; find yours before a large programme starts.

| Decision | Keep it with | Starting rule |
|---|---|---|
| Approve a major programme | The accounting officer or senior responsible owner | Approve the full case, fund only the next phase. Each phase ends with something in production and fits one budget year. |
| Continue, rescope or stop at a gate | The senior responsible owner, advised by independent assurance | Decide on remaining cost and remaining value. Stop conditions are written in the business case as a measure, a threshold and a date. |
| Proceed when a test may fail (feasibility or value for money) | The accounting officer | Write an assessment against the four tests. Where it fails, seek a direction rather than proceed quietly. |
| Accept a risk outside appetite | The body that set the appetite, often the departmental board | Written, with an owner and an expiry date. HM Treasury's Orange Book sets out the principles. |
| Let an algorithm or AI make or shape a decision about a citizen | The service owner, with legal and the DPO | Human review for decisions with legal or similar effect, a route to challenge, and a public record of the tool. UK central government departments must publish records under the Algorithmic Transparency Recording Standard. |
| Sign a contract that would be hard to exit | The accounting officer, above the delegated limit | Exit terms and a tested data export before signature. |

Public programmes are hard to stop because stopping is visible and money already spent is easy to quote back. Agree with the minister at approval which result would end the programme, so a stop is the plan working, not a political failure. In the UK, summaries of accounting officer assessments for projects in the Government Major Projects Portfolio are published on GOV.UK; reading a few shows what a complete assessment covers.

## Funding continuous services in budget years

- Fund live services as running costs with a persistent team. A service without a team starts to decay at launch.
- Split capital and operating costs in every [business case](../playbook/strategy/business-case.md), because many treasuries fund them from different budgets.
- Plan delivery in phases that fit one budget year, each with a gate and something in production at the end.
- Ask for multi-year envelopes for shared platforms. Show the cost of stopping and restarting a team.
- Report value in public terms: transactions completed digitally, time saved for citizens, cost per transaction, completion rate.

## Cyber resilience of national systems

- Keep an inventory of systems the state cannot function without, with owners, dependencies and recovery targets.
- Test Tier 1 backups with an automated restore every month and a full restore exercise every quarter, and recover each Tier 1 service at another site at least once a year. See [backup and recovery](../playbook/reliability/backup-and-recovery.md).
- Rehearse a national-level incident each year with the national cyber authority. See [crisis leadership](crisis-leadership.md).
- Agree the ransomware position with legal and the national cyber authority before an attack, not during one. See the ransomware decisions in [crisis leadership](crisis-leadership.md).
- Plan the move to post-quantum cryptography for data that must stay secret for 10 years or more. See [post-quantum readiness](../playbook/security/post-quantum-readiness.md).
- Apply [third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md) to every supplier that runs a national system.

## Using this playbook across a whole government

| Step | Who | Output |
|---|---|---|
| 1. Adopt a national service standard and technology code of practice | central digital authority | published standard, based on the UK or US examples if none exists |
| 2. Set the default level | central digital authority | Assured for high-impact services (tax, health, justice, identity); Standard for most others |
| 3. Run the [self-assessment](../assessment/README.md) in each ministry | ministry CIOs | a baseline per ministry, committed to a shared repository |
| 4. Agree shared platforms and their owners | permanent secretaries | a short list of DPI building blocks with funded teams |
| 5. Adopt the templates as the government default, copied with `tools/adopt.sh` | central digital authority | one pull request template, one incident process, one data classification scheme |
| 6. Review progress every quarter | digital board | the measures above and the next 5 actions per ministry |

## Common mistakes

| Mistake | Fix |
|---|---|
| Every ministry buys its own identity, payments and hosting | Fund shared platforms with product owners and service levels. |
| A large multi-year contract with one supplier for everything | Smaller lots, shorter terms, exit terms from day one. |
| Team disbanded at launch | Fund a persistent service team from running costs. |
| Digital channel launched and counters closed the same day | Keep assisted channels until digital completion rates show they are no longer needed. |
| Services built only in the official language for the newest phones | Test with users on low-cost devices, slow networks and in local languages. |
| Assurance as a document review at the end | Gates with published criteria and the power to stop. |
| A failing programme continued because of what it has already cost | Decide on remaining cost and value; agree the stop result with the minister at approval. |

## Templates

- [Data classification](../templates/docs/data-classification.md)
- [Transition charter](../templates/strategy/transition-charter.md)
- [Business case](../templates/strategy/business-case.md)
- [Board engineering report](../templates/leaders/board-engineering-report.md)
- [Vendor risk questionnaire](../templates/docs/vendor-risk-questionnaire.md)

## Sources

- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
- UK Technology Code of Practice: https://www.gov.uk/guidance/the-technology-code-of-practice
- US Digital Services Playbook: https://playbook.cio.gov/
- X-Road, Nordic Institute for Interoperability Solutions: https://x-road.global
- Unified Payments Interface, National Payments Corporation of India: https://www.npci.org.in
- GovStack: https://www.govstack.global
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/
- UK NCSC, Board Toolkit: https://www.ncsc.gov.uk/collection/board-toolkit
- HM Treasury, Managing Public Money: https://www.gov.uk/government/publications/managing-public-money
- HM Treasury, accounting officer assessments: guidance: https://www.gov.uk/government/publications/accounting-officer-assessments
- HM Treasury and Government Finance Function, The Orange Book, Management of Risk: Principles and Concepts: https://www.gov.uk/government/publications/orange-book
- UK Algorithmic Transparency Recording Standard hub: https://www.gov.uk/government/collections/algorithmic-transparency-recording-standard-hub
