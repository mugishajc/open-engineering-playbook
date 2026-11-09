# Public sector

Government technology teams face the same engineering problems as everyone else, plus procurement rules, budget years, accessibility law, data residency, records duties and the need to account to the public. Build on open standards and open source by default, buy in a way that keeps the option to leave, and meet a published service standard for anything citizens use. Most of the playbook practices apply unchanged; this page lists what to add.

## Outcomes

Starting points. Tune them to your organisation.

- Every citizen-facing service passes an assessment against your national service standard before public launch, and again before major changes.
- Every public service meets WCAG 2.2 level AA, checked with automated tests in CI and a manual audit at least once a year.
- Every contract for a critical system includes data export in documented formats, source code or escrow terms, and transition assistance.
- At least 80% of new code is published openly, unless a written exemption applies (security, policy or third-party rights).
- Personal and classified data stays in approved jurisdictions, confirmed by an inventory reviewed every 6 months.

## Procurement

| Practice | What to do |
|---|---|
| Open standards first | Require published, royalty-free standards for data formats and interfaces where they exist. The UK Open Standards principles are a model. |
| Open source first | Consider open source on equal terms with commercial products. Publish the code you write unless there is a clear reason not to, as the UK Technology Code of Practice and Service Standard expect. |
| Short contracts, small lots | Prefer contracts of 1 to 2 years with options to extend, split into lots that smaller suppliers can bid for. |
| Exit built in | Contract for data export, documentation, knowledge transfer and a transition period. Price the exit in the [build, buy or adopt](../strategy/build-buy-adopt.md) comparison. |
| Own the code | Make sure the public body owns or has an open licence to code written for it. |
| Start early | Begin procurement during the Assess phase of the [transition playbook](../strategy/transition-playbook.md). Use framework agreements where they exist. |

## Budget years and funding

- Plan delivery in phases that fit inside one budget year where possible, with a gate at year end.
- Separate capital and operating spending in every [business case](../strategy/business-case.md). Many public bodies fund them from different budgets.
- Fund persistent teams for live services, not projects that end at launch. A service that loses its team at launch starts to decay.
- Ask for multi-year commitments for platforms and shared services. Show the cost of stopping and restarting.

## Accessibility

- Target WCAG 2.2 level AA as the minimum for every public web and mobile service.
- In the EU, public sector websites and apps fall under Directive (EU) 2016/2102, and the European Accessibility Act applies to many private-sector products and services from 28 Jun 2025. Both rely on the harmonised standard EN 301 549, which currently references WCAG 2.1 level AA; targeting WCAG 2.2 AA meets it and covers the newer criteria. In the US, Section 508 applies to federal technology.
- Run automated accessibility checks in [continuous integration](../delivery/continuous-integration.md). They catch only part of the problems, so add manual testing with assistive technology and testing with disabled users.
- Publish an accessibility statement for each service and update it after each audit.

## Data residency and sovereignty

- Keep an inventory of where each data set is stored and processed, and who can access it, including supplier staff. See [data governance](../data/data-governance.md).
- Classify data with the [data classification template](../../templates/docs/data-classification.md) and map each class to permitted hosting locations.
- Check the jurisdiction of the supplier as well as the data centre. A provider subject to foreign law may face foreign access orders. Customer-managed keys in the provider's own key service do not change that while the data is processed; see [data security and privacy](../data/data-security-and-privacy.md) for external key managers.
- Record the transfer mechanism for every copy or remote access outside the country. Remote support by supplier staff abroad is a transfer. Each data protection law below has its own transfer rule; the table in [data security and privacy](../data/data-security-and-privacy.md#laws-to-check) lists them.
- Data protection laws to check include the EU GDPR, UK GDPR, Kenya Data Protection Act 2019, Rwanda Law No 058/2021, Nigeria Data Protection Act 2023, Brazil LGPD, India DPDP Act 2023 and California CCPA/CPRA. This is not legal advice.

## Records and transparency

- Treat decision records, RFCs, release history and incident records as public records where your law says so. Apply the retention schedule from your records office.
- Build deletion and retention into systems from the start. Do not rely on manual clean-ups.
- Expect freedom of information requests. Write decision records so they can be released, keeping sensitive detail in separate, marked sections.
- Publish performance data for public services where policy requires it, such as uptime, completion rate and user satisfaction.
- For algorithmic or AI-assisted decisions about people, publish what the system does and how to challenge a decision. See [AI governance](../ai/ai-governance.md).

## Citizen-facing service standards

Use the national standard if one exists. Otherwise adopt one of these as a base:

| Standard | Core ideas |
|---|---|
| UK Government Service Standard | understand users, solve a whole problem, make the service accessible, use agile ways of working, iterate frequently, make new source code open, use open standards, operate a reliable service |
| US Digital Services Playbook | understand what people need, address the whole experience, make it simple, build iteratively, structure budgets and contracts to support delivery, default to open |

Assess services at three points: before a public test (beta), before full launch, and before retirement.

## Working with suppliers

- Keep at least one public servant with technical skills in each team that a supplier staffs. They own decisions and keep knowledge in-house.
- Use the same repositories, CI and [code review](../delivery/code-review.md) rules for supplier and staff engineers.
- Include [vulnerability disclosure](../../templates/docs/vulnerability-disclosure-policy.md), incident notification times and evidence access in contracts.
- Review supplier performance quarterly against delivery [metrics](../measurement/metrics.md), not only milestones.

## Practice

### Foundation

Small agencies and municipal teams. Adopt a service standard, publish code openly, meet WCAG 2.2 AA, keep a data inventory, and write exit terms into every contract.

### Standard

National agencies and large departments. Everything in Foundation, plus service assessments at each phase, a shared platform for common needs (identity, notifications, payments through approved providers, hosting), and a published technology code of practice.

### Assured

Defence, justice, health, tax and other high-impact services. Everything in Standard, plus security accreditation, classified hosting where required, independent assurance at each transition gate, and records kept for statutory periods.

## Cloud, on-premises and air-gapped

Classified environments are often air-gapped. Engineering practices still apply: version control, CI, signed artefacts and SBOMs run inside the network on self-hosted tools such as GitLab self-managed, Gitea or Forgejo, Harbor and HashiCorp Vault or OpenBao. Plan a controlled, logged import process for updates, packages and vulnerability data, with signature checks on the high side. Staff with clearance are scarce, so automate as much as possible. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Large multi-year contract with one supplier for everything | Smaller lots, shorter terms, exit clauses. |
| Accessibility tested once before launch | Automated checks in CI plus a yearly manual audit. |
| Team disbanded at launch | Fund a persistent service team. |
| Code owned by the supplier | Contract for public ownership or an open licence. |

## Templates

- [Data classification](../../templates/docs/data-classification.md)
- [Transition charter](../../templates/strategy/transition-charter.md)
- [Stakeholder map](../../templates/strategy/stakeholder-map.md)
- [Vulnerability disclosure policy](../../templates/docs/vulnerability-disclosure-policy.md)

## Sources

- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
- UK Technology Code of Practice: https://www.gov.uk/guidance/the-technology-code-of-practice
- UK Open Standards principles: https://www.gov.uk/government/publications/open-standards-principles
- UK GDS Way: https://gds-way.digital.cabinet-office.gov.uk/
- US Digital Services Playbook: https://playbook.cio.gov/
- W3C, Web Content Accessibility Guidelines (WCAG) 2.2: https://www.w3.org/TR/WCAG22/
- European Accessibility Act, Directive (EU) 2019/882: https://eur-lex.europa.eu/eli/dir/2019/882/oj
- Web Accessibility Directive, Directive (EU) 2016/2102: https://eur-lex.europa.eu/eli/dir/2016/2102/oj
- US Section 508: https://www.section508.gov
