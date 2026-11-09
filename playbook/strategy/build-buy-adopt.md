# Build, buy, adopt or partner

Build only what differentiates you. For everything else, compare buying a product, adopting open source and partnering with a supplier, using a weighted scoring matrix and total cost of ownership over 3 to 5 years, including the cost of leaving. Prefer options built on open standards that you can run where your data must live.

## Outcomes

Starting points. Tune them to your organisation.

- Every choice above an agreed threshold (for example 50,000 CU over three years, or any system holding personal or classified data) has a scored comparison and a decision record.
- Every chosen option has a written, costed exit plan. For critical systems, the exit plan is tested at least once every two years.
- At least 90% of production data in third-party systems can be exported in an open or documented format within 30 days.
- The number of overlapping tools for the same job falls each year, tracked on the [tech radar](../architecture/tech-radar.md).

## The four options

| Option | Meaning | Choose it when | Watch out for |
|---|---|---|---|
| Build | Your engineers write and run it | it is a core differentiator, or nothing available fits a hard constraint | you own maintenance for its whole life |
| Buy | Commercial product or SaaS, licensed | the need is common and a mature product exists | pricing changes, data location, exit cost |
| Adopt | Open source, run by you, optionally with paid support | a healthy project exists and you can operate it | project health, your operating skills, licence terms |
| Partner | A supplier builds or runs it for you under contract | you lack the skills and need speed, or it is not core | knowledge loss, contract lock-in, outsourcing rules |

Most real choices mix options, for example adopting an open source database with a paid support contract.

## Scoring matrix

Agree weights before scoring options. Scores run from 1 (poor) to 5 (strong). Weighted score = weight x score. The weights below are a starting point. Public sector and Regulated users should raise sovereignty and exit.

| Criterion | Weight | What a 5 looks like |
|---|---|---|
| Fit to requirements | 20 | meets all must-have requirements without custom work |
| Total cost of ownership (3 to 5 years) | 15 | lowest TCO including exit |
| Exit cost and lock-in | 15 | data and configuration export in open formats, no proprietary runtime |
| Sovereignty and hosting options | 10 | runs on-premises, in-country and air-gapped, under your jurisdiction |
| Open standards | 10 | uses published standards (for example OCI, OpenTelemetry, SQL, OpenID Connect, SPDX or CycloneDX) |
| Security and supply chain | 10 | signed releases, published SBOM, vulnerability disclosure policy, OpenSSF Scorecard checked |
| Operability | 10 | your team can run, patch and recover it with current skills |
| Project or supplier health | 10 | active maintainers or stable supplier, clear roadmap, support terms that cover your hours |
| **Total** | **100** | |

Illustrative example (fictional figures) for an internal secrets store:

| Criterion | Weight | Build | Buy (SaaS) | Adopt (open source) |
|---|---|---|---|---|
| Fit | 20 | 3 (60) | 5 (100) | 4 (80) |
| TCO | 15 | 2 (30) | 3 (45) | 4 (60) |
| Exit and lock-in | 15 | 5 (75) | 2 (30) | 4 (60) |
| Sovereignty | 10 | 5 (50) | 2 (20) | 5 (50) |
| Open standards | 10 | 3 (30) | 3 (30) | 4 (40) |
| Security | 10 | 2 (20) | 4 (40) | 4 (40) |
| Operability | 10 | 2 (20) | 5 (50) | 3 (30) |
| Health | 10 | 2 (20) | 4 (40) | 4 (40) |
| **Total** | 100 | **305** | **355** | **400** |

Treat a gap of less than 10% between the top two as a tie. Settle ties on exit cost and sovereignty.

## Total cost of ownership

Count every year of the period, for every option, in the same currency.

```
TCO = acquisition + implementation + (run + change) x years + exit
```

| Component | Includes |
|---|---|
| Acquisition | licences or subscription, hardware, procurement effort |
| Implementation | integration, data migration, training, security review |
| Run (per year) | hosting, support contracts, on-call, licences, staff time to operate |
| Change (per year) | upgrades, patching, keeping up with breaking changes |
| Exit | data export, rewrite of integrations, parallel running, contract notice period, retraining |

Rules:

- Price staff time at the loaded hourly cost, not salary only.
- For Build, include maintenance after year one. Plan for at least 15% to 25% of the initial build effort per year as a starting assumption, then correct it with your own history.
- For SaaS, model price increases explicitly. Use the contract's cap, or assume a rise if there is none.
- For Adopt, include the cost of tracking upstream releases and of paid support if you need guaranteed response times.
- Show exit cost even if you never plan to leave. Regulators and auditors ask for it.

## Lock-in and sovereignty checks

Answer each question yes or no. Two or more "no" answers for a critical system need a written risk acceptance.

1. Can we export all our data and configuration in a documented format without the supplier's help?
2. Can we run it on-premises or in a country we choose?
3. Is the supplier's access to our data and systems limited, logged and subject to our jurisdiction?
4. Does it work with our identity provider over an open standard (OpenID Connect or SAML)?
5. Can it run disconnected from the internet, including licence checks and updates?
6. If the supplier stops trading, do we keep a working copy (source escrow, open source licence or perpetual licence)?
7. Do we have at least one alternative that could replace it within 12 months?

## Practice

### Foundation

Solo and Startup. Default to buy or adopt for anything that is not your product. Use a short list of five criteria: fit, cost, exit, security, operability. Record the choice in a [decision record](../architecture/decision-records.md). Revisit when cost or scale changes by a factor of two.

### Standard

Scale-up and Enterprise. Use the full scoring matrix. Compare at least three options. Platform and security teams score their criteria independently. Add the result to the [tech radar](../architecture/tech-radar.md). Consolidate overlapping tools once a year.

### Assured

Regulated and Public sector. Everything in Standard, plus:

- Treat Partner and most Buy choices for important functions as outsourcing. Do due diligence and keep a register of third-party arrangements. See [regulated industries](../compliance/regulated-industries.md).
- Test the exit plan for critical systems every two years: export real data and restore it elsewhere.
- Public sector: follow open standards and open source policies and publish the code you build where policy allows. See [public sector](../compliance/public-sector.md).
- Procurement and legal review every contract for data location, audit rights, sub-processors, termination and transition assistance.

## Cloud, on-premises and air-gapped

Many SaaS products cannot run on-premises or air-gapped at all. Score them 1 on sovereignty for those environments and treat them as unavailable if the environment is mandatory. For adopted open source in air-gapped sites, count the effort to mirror packages, images and vulnerability data and to verify signatures offline. Check that commercial support covers on-premises installations and response times in your time zone. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Building a commodity tool because it seems easy | Score maintenance for five years. It rarely wins. |
| Buying on licence price alone | Use full TCO including exit. |
| Adopting an abandoned project | Check release history, maintainer count and Scorecard results first. |
| Weights chosen after scoring | Agree and record weights before anyone scores. |
| No exit plan | Make a costed exit plan a condition of the decision. |

## Templates

- [Decision record](../../templates/docs/adr.md)
- [Business case](../../templates/strategy/business-case.md)
- [Risk register](../../templates/strategy/risk-register.csv)

## Sources

- UK Technology Code of Practice: https://www.gov.uk/guidance/the-technology-code-of-practice
- UK Open Standards principles: https://www.gov.uk/government/publications/open-standards-principles
- OpenSSF Scorecard: https://scorecard.dev
- Regulation (EU) 2022/2554 (Digital Operational Resilience Act): https://eur-lex.europa.eu/eli/reg/2022/2554/oj
