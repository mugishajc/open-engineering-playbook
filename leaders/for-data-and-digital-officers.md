# For chief data and chief digital officers

Tie every piece of data work to a business outcome someone already measures. Give each important data set a named owner who is judged on its quality. Fund a few data products, not a platform with no customers. Agree in writing what you own and what the CTO or CIO owns before the first budget round: most failures in this role come from a split nobody wrote down. A chief digital officer, who owns services and channels rather than data, starts at [chief digital officers](#chief-digital-officers).

## When to use this

- You are new in a chief data officer or chief digital officer role and need a plan for the first year.
- Data work is funded as a cost centre and the board asks what it returned.
- Every report gives a different number for the same thing, and nobody owns the definition.
- AI pilots stall because the data is missing, wrong or not cleared for that use.
- You are unsure where your remit ends and the CTO's or CIO's begins.

The engineering practice behind this page lives in [data governance](../playbook/data/data-governance.md), [data quality](../playbook/data/data-quality.md), [data security and privacy](../playbook/data/data-security-and-privacy.md) and [AI governance](../playbook/ai/ai-governance.md). This page covers the leadership decisions around them.

## Data strategy tied to outcomes

A data strategy that lists technologies is a shopping list. Start from the three to five outcomes the executive team already tracks, then work back to the data each one needs.

| Step | Question | Output |
|---|---|---|
| 1 | Which business outcomes will data work move this year? | 3 to 5 outcomes, each with an executive owner and a measure already on the company scorecard |
| 2 | Which decisions or processes drive each outcome? | a named decision (for example credit approval, stock reorder, patient discharge) |
| 3 | What data does each decision need, and how good is it today? | data sets with current quality scores (see below) |
| 4 | What is the smallest data product that improves the decision? | 1 to 3 data products per outcome, each with an owner |
| 5 | What must be true of governance, platform and skills to deliver them? | the enabling work, sized and funded only to the extent the products need it |

Write the result on one page with the [data strategy on a page](../templates/leaders/data-strategy-on-a-page.md) template. Review it each quarter in your [operating rhythm](operating-rhythm.md).

## Data products and ownership

A data product is a data set or service with a named owner, known consumers, a documented meaning, a quality target and a change process. It is not a table in a warehouse that one analyst understands.

| Property | Minimum (starting point) |
|---|---|
| Owner | one named person in the business domain that produces the data, accountable for fitness for use |
| Consumers | listed; at least one consumer outside the owning team, otherwise it is not yet a product |
| Definition | every field defined in the catalogue, with units and allowed values |
| Quality target | 2 to 4 measured dimensions with thresholds (for example completeness 99%, freshness under 24 hours) |
| Contract | a [data contract](../playbook/data/data-quality.md) covering schema, meaning and notice of breaking changes (30 days as a starting point) |
| Access rule | derived from the [classification](../templates/docs/data-classification.md), not negotiated per request |
| Retirement | a rule for when the product is withdrawn and how consumers are told |

Ownership sits with the domain that creates the data. The central data team runs the catalogue, shared tooling and standards. Data mesh is one way to push this further for large organisations with many domains; adopt it only after ownership and contracts work at small scale.

## Governance that teams accept

Teams accept governance that answers their questions faster than they could alone. They route around governance that adds a queue.

| Do | Do not |
|---|---|
| set rules once per classification level, so access follows the label | review every access request in a committee |
| generate catalogue entries from schemas and infrastructure code | ask teams to fill in a catalogue by hand |
| publish decisions on definitions (what counts as an "active customer") within 10 working days of the question | leave definitions to whoever builds the report |
| measure the time from access request to access granted; target under 2 working days for internal data | measure governance by the number of policies written |
| put a steward inside each domain team | run stewardship as a separate department |

Use DAMA-DMBOK to check you have not missed an area. Use the EDM Council's Data Management Capability Assessment Model (DCAM) if you need a structured maturity assessment that regulators and auditors recognise. Neither is a plan; pick the areas your outcomes need.

## Data quality as an operational metric

Report data quality the way operations reports uptime: per data product, against a target, with a trend.

| Measure | How to collect | Starting target |
|---|---|---|
| Share of critical data products meeting all quality thresholds | automated checks in pipelines, see [data quality](../playbook/data/data-quality.md) | 95% of days |
| Data incidents (a consumer acted on wrong data) | incident records, same process as [incident management](../playbook/reliability/incident-management.md) | trend down quarter on quarter |
| Time to detect a data quality failure | check timestamp minus time the bad data arrived | under 1 hour for critical products |
| Share of breaking changes announced through a contract | contract change log | 100% |
| Definitions in dispute | open items in the definitions log | none older than 30 days |

Put the first two measures on the executive scorecard. Data quality without an operational owner degrades quietly until an audit or a model exposes it.

## AI readiness of data

Before approving an AI use case, check the data against these questions. Each "no" is work to plan, not a reason to stop.

| Question | Where it is answered |
|---|---|
| Is the data cleared for this use (training, fine-tuning, retrieval, prompting) and this provider? | catalogue entry, [data governance](../playbook/data/data-governance.md) |
| Is there a lawful basis, and is a data protection impact assessment needed? | privacy review, [data security and privacy](../playbook/data/data-security-and-privacy.md) |
| Does the data represent the people and cases the system will serve? | [data quality for AI](../playbook/data/data-quality.md) |
| Can you trace lineage from source data to model output? | lineage in the catalogue |
| Is there a labelled evaluation set owned by the business? | [building with AI](../playbook/ai/building-with-ai.md) |
| Is the use case in the AI register with a risk tier? | [AI governance](../playbook/ai/ai-governance.md), [use case assessment](../templates/docs/ai-use-case-assessment.md) |

## Measuring the value of data work

Count value where the business already counts it. Avoid "number of dashboards" and "terabytes managed".

| Value type | Example measure | Who confirms it |
|---|---|---|
| Better decisions | change in the outcome measure for the decision the product supports, against a baseline period | the executive owner of the outcome |
| Cost removed | hours of manual reconciliation removed, using a before and after time study | finance partner |
| Risk reduced | regulatory findings closed; personal data stores with enforced retention | risk or audit |
| Revenue enabled | new product or channel that could not run without the data product | commercial owner |
| Speed | time from question to trusted answer | the people asking |

Use the [business case](../playbook/strategy/business-case.md) method: low, expected and high scenarios, commit to the low one, check at 6 and 12 months.

## Chief digital officers

A chief digital officer owns how the organisation serves people through digital channels: the services, the user experience and the move from paper or counters to online. The two roles share an acronym and little else. If this is your role, the data sections above are for the colleague you will depend on most.

| Decision | Starting point | Read |
|---|---|---|
| Who owns each service | one named service owner per end-to-end service (for example "renew a licence"), judged on completion rate and user satisfaction, not on a project delivered | [Product partnership](../playbook/ways-of-working/product-partnership.md) |
| How services are funded | persistent product teams funded each year, not projects that end at launch | [Portfolio and capacity](../playbook/strategy/portfolio-and-capacity.md) |
| User research | every team talks to users at least every 2 weeks; test with people who use assistive technology, low-cost phones and slow networks | [For government](for-government.md) |
| Channel shift | a target per service for the share of transactions completed online, with the assisted channel kept for people who need it | [Transition playbook](../playbook/strategy/transition-playbook.md) |
| Accessibility | WCAG 2.2 level AA as the floor for every public service | [Public sector compliance](../playbook/compliance/public-sector.md) |
| The split with the CIO or CTO | you own the service and its outcomes; they own the platforms and engineering capacity; agree capacity each quarter | [Decision rights](../playbook/operating-model/decision-rights.md) |

In the first 90 days, list the ten services with the most transactions, name an owner for each, and measure where users drop out.

## Splitting responsibilities with the CTO or CIO

There is no single correct split. There must be a written one. Agree it in the first 60 days and record it in your [decision rights](../playbook/operating-model/decision-rights.md).

| Area | Common default owner | Notes |
|---|---|---|
| Data strategy and outcome targets | chief data officer | agreed with the executive team |
| Definitions, catalogue, classification policy | chief data officer | stewards sit in the domains |
| Data platform (storage, pipelines, compute) | CTO or CIO | the chief data officer is the main customer and sets requirements |
| Data products | the business domain that produces the data | the chief data officer sets standards; the domain owns delivery |
| Security controls on data | CISO | the chief data officer owns classification; the CISO owns enforcement |
| Privacy compliance | data protection officer | independent of the chief data officer where law requires |
| AI use case approval | AI governance group | the chief data officer confirms data readiness |
| Digital channels and customer experience (chief digital officer) | chief digital officer | engineering capacity usually sits with the CTO; agree capacity allocation in [portfolio planning](../playbook/strategy/portfolio-and-capacity.md) |

## Regulation to plan for

This is not legal advice. Read the text and talk to your counsel.

| Law | What it means for a data leader |
|---|---|
| EU Data Governance Act, Regulation (EU) 2022/868 (applies from 24 Sep 2023) | rules for re-use of protected public sector data, data intermediation services and data altruism organisations |
| EU Data Act, Regulation (EU) 2023/2854 (applies from 12 Sep 2025) | users of connected products and related services can access and share the data they generate; rules on switching between data processing services; fairness of data-sharing contract terms |
| Data protection laws: EU GDPR, UK GDPR, Kenya Data Protection Act 2019, Rwanda Law No 058/2021, Nigeria Data Protection Act 2023, Brazil LGPD, India DPDP Act 2023, California CCPA/CPRA | lawful basis, purpose limitation, retention, rights of individuals, impact assessments, cross-border transfer rules |
| EU AI Act, Regulation (EU) 2024/1689, as amended by Regulation (EU) 2026/1744 | data and data governance duties for high-risk systems. Prohibited practices apply from 2 Feb 2025. High-risk obligations apply from 2 Dec 2027 (Annex III) and 2 Aug 2028 (AI in Annex I products). New prohibitions on non-consensual intimate imagery and child sexual abuse material apply from 2 Dec 2026. Check EUR-Lex before you plan |

Keep a register of which laws apply to which data products. Most of the evidence comes from the catalogue, the contracts and the retention jobs you already run.

## First-year plan

Adapt the timing to your organisation. Use [first 90 days](first-90-days.md) for the listening phase.

| Period | Focus | Exit criteria |
|---|---|---|
| Days 1 to 90 | listen, map outcomes, agree the split with CTO, CIO and CISO | written responsibility split (by day 60); top 5 outcomes agreed; list of critical data sets with owners named |
| Months 4 to 6 | first 2 or 3 data products tied to outcomes | each product has an owner, contract and quality target; quality reported weekly |
| Months 7 to 9 | governance that scales | catalogue generated from code for at least 50% of production stores; access by classification |
| Months 10 to 12 | prove value, plan year two | value measured against baselines; data quality on the executive scorecard; year-two strategy on one page |

## Common mistakes

| Mistake | Fix |
|---|---|
| A data platform built before anyone needs it | Fund the platform to serve named data products, then grow it. |
| A governance council that meets monthly to approve access | Rules per classification level; measure time to access. |
| Data quality reported once a year in an audit | Automated checks and a weekly trend. |
| Value claimed as "insight" with no measure | Tie each product to an outcome measure owned by an executive. |
| No written split with the CTO or CIO | Agree it in the first 60 days and publish it. |
| AI pilots approved before the data is cleared for that use | Run the AI readiness questions first. |

## Templates

- [Data strategy on a page](../templates/leaders/data-strategy-on-a-page.md)
- [Data classification](../templates/docs/data-classification.md)
- [AI use case assessment](../templates/docs/ai-use-case-assessment.md)
- [Strategy one-pager](../templates/strategy/strategy-one-pager.md)
- [RACI](../templates/strategy/raci.csv)

## Sources

- DAMA International, DAMA-DMBOK: https://www.dama.org
- EDM Council, Data Management Capability Assessment Model (DCAM): https://edmcouncil.org
- Regulation (EU) 2022/868, Data Governance Act: https://eur-lex.europa.eu/eli/reg/2022/868/oj
- Regulation (EU) 2023/2854, Data Act: https://eur-lex.europa.eu/eli/reg/2023/2854/oj
- Regulation (EU) 2016/679, GDPR: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Regulation (EU) 2024/1689, AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Regulation (EU) 2026/1744, Digital Omnibus on AI, amending the AI Act: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- Zhamak Dehghani, "Data Mesh", O'Reilly Media, 2022.
