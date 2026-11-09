# Suppliers and contracts

Manage suppliers after the selection decision, not only during it: renewals, service levels and exit terms decide much of what a supplier costs over its life. Tier suppliers by the services they support, give each strategic supplier a named owner and a quarterly review, and start renegotiation 9 to 12 months before each end date. Put exit, audit and price control terms into every contract at renewal, and price outsourced delivery on capacity or outcomes so efficiency gains reach you.

This page starts where [build, buy, adopt or partner](build-buy-adopt.md) ends. Security due diligence of suppliers is in [third-party and SaaS risk](../security/third-party-and-saas-risk.md).

## Outcomes

Starting points. Tune them to your organisation.

- Every supplier above an agreed spend, or supporting a tier 1 service, is in one register with a tier, an owner and a contract end date.
- 100% of strategic suppliers have a quarterly review against service levels, with written actions.
- Renegotiation of every strategic contract starts at least 9 months before its end or notice date. No strategic contract renews automatically by accident.
- Every strategic contract has a price increase cap, audit rights, termination assistance and a documented data export format.
- The number of suppliers for the same capability falls each year, tracked on the [application portfolio](../../templates/leaders/application-portfolio.csv).

## Tier suppliers by what they support

| Tier | Meaning | Management |
|---|---|---|
| Strategic | supports a tier 1 service or a critical function, hard to replace, or large spend | named executive owner, quarterly review, tested exit plan, renewal plan 12 months ahead |
| Important | supports tier 2 services or several teams | named owner, review twice a year, exit plan written |
| Commodity | easy to replace, low spend | standard terms, yearly check of use and cost |

Review the tiers once a year and whenever a supplier starts supporting a new critical service.

## The renewal calendar

1. List every contract with its end date, notice period and automatic renewal terms.
2. For strategic contracts, start 9 to 12 months before the notice date: check use against the licence, collect service level history, and price at least one alternative so the negotiation has a real fallback.
3. For important contracts, start 6 months before.
4. Decide renew, renegotiate, consolidate or exit at least 3 months before the notice date, and record the decision with its reason.
5. Report contracts ending in the next 18 months at the monthly cost review in the [operating rhythm](../../leaders/operating-rhythm.md).

## Terms to ask for

Ask legal and procurement to put these into every strategic contract at signing or renewal.

| Term | What it gives you |
|---|---|
| Price increase cap | a limit on yearly rises, for example tied to a published inflation index |
| Benchmarking clause | the right to compare prices with the market and reopen them |
| Service levels with credits | measurable targets and money back when they are missed |
| Audit rights | access for you, your auditors and, where law requires, your regulator |
| Data export | your data and configuration in a documented format, on request and at exit, at no extra charge |
| Termination assistance | help to move to another supplier for a stated period after notice |
| Sub-processor notice | advance notice of new sub-processors and locations, with a right to object |
| Escrow or open licence | source code escrow, an open source licence or a perpetual licence, for software you cannot replace quickly |
| Step-in rights (outsourcing) | the right to take over or appoint another provider if the supplier fails |
| Change of control | review or exit rights if the supplier is sold |

Regulated firms have more required terms. Financial entities in the EU must include the contractual terms in Article 30 of the Digital Operational Resilience Act. See [regulated industries](../compliance/regulated-industries.md).

## EU Data Act: cloud switching

The EU Data Act (Regulation (EU) 2023/2854) applies from 12 September 2025 and changes exit cost assumptions for cloud and other data processing services:

- Contracts must allow switching to another provider or to your own infrastructure, with a notice period of no more than two months and a transition period of no more than 30 calendar days in most cases.
- Until 12 January 2027, providers may charge switching fees that do not exceed their direct costs of switching. From 12 January 2027, they may not charge switching fees at all.

Re-price exit costs in every cloud business case. Add switching terms at renewal. Exit still costs your own time, parallel running and re-engineering: the Act removes the provider's switching fee, not your work.

## Outsourced delivery

Many organisations buy engineering capacity from partners on time-and-materials contracts. That pricing pays for effort, so any efficiency gain belongs to the supplier unless the contract says otherwise.

- **Move to capacity or outcome pricing at renewal:** a fixed price per team per month with agreed service levels, or a price per delivered outcome.
- **Same practices, same evidence.** The partner works to your definition of done, your pipeline, your [code review](../delivery/code-review.md) and [incident management](../reliability/incident-management.md) rules. Write it into the contract.
- **Keep knowledge in-house.** Your own staff own architecture decisions and the service catalogue. Rotate your engineers into supplier teams.
- **Plan the exit from day one:** documentation, access handover and a knowledge transfer period in the contract.

## Licence audits and true-ups

Software suppliers can audit your use and bill for any excess.

- Keep a licence inventory linked to the service catalogue, updated from systems (identity, hosts, containers), not by hand.
- Check use against entitlement every quarter for strategic suppliers. Remove unused licences before renewal.
- When a supplier announces an audit, route all contact through one owner and legal. Agree the scope and method in writing before data is shared.
- Watch licence changes on cloud migration, virtualisation and acquisitions; these often change what you owe.

## Practice

### Foundation

Solo and Startup. One list of suppliers with cost, owner and end date. Turn off automatic renewal where you can, or set a reminder 3 months before. Prefer monthly terms until a product proves itself.

### Standard

Scale-up and Enterprise. The tiers, the register, the renewal calendar and quarterly reviews of strategic suppliers. Consolidate overlapping suppliers once a year. Capacity or outcome pricing for outsourced delivery at the next renewal.

### Assured

Regulated and Public sector. Everything in Standard, plus a register of third-party arrangements as regulation requires, exit plans tested for critical services, regulator access rights in contracts, and procurement rules followed for every award and renewal. See [public sector](../compliance/public-sector.md) and [regulated industries](../compliance/regulated-industries.md).

## Cloud, on-premises and air-gapped

Cloud contracts carry commitment discounts that lock in spend; treat them as contracts with a renewal date and an owner (see [FinOps](../platform/finops.md)). On-premises and air-gapped estates depend on hardware and support contracts with long lead times; put hardware end-of-support dates in the renewal calendar, and check that support covers sites without internet access.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Contracts that renew automatically unnoticed | A renewal calendar with owners; start 9 to 12 months ahead for strategic contracts. |
| Negotiating with no alternative priced | Price at least one alternative before the negotiation. |
| Time-and-materials for long-running delivery | Capacity or outcome pricing, with your definition of done in the contract. |
| Exit plan written only at selection | Review and test it for strategic suppliers at least every two years. |
| Licence audit answered by whoever got the email | One owner and legal; agree scope before sharing data. |

## Templates

- [Application portfolio](../../templates/leaders/application-portfolio.csv)
- [Risk register](../../templates/strategy/risk-register.csv)
- [Vendor risk questionnaire](../../templates/docs/vendor-risk-questionnaire.md)

## Sources

- Regulation (EU) 2023/2854 (Data Act), Articles 25 and 29: https://eur-lex.europa.eu/eli/reg/2023/2854/oj
- Regulation (EU) 2022/2554 (Digital Operational Resilience Act), Article 30: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- UK Technology Code of Practice: https://www.gov.uk/guidance/the-technology-code-of-practice
