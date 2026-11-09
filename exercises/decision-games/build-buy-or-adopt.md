# Decision game: build, buy or adopt

You lead technology at a public agency that must replace the sign-in system for its staff and for millions of citizens. A SaaS vendor has a polished demo, a systems integrator has a friendly bid, your own engineers want to build it, and an open source project would do most of the job if you can run it. The law says identity data stays in the country. Choose, then see what happens.

| | |
|---|---|
| Who | CIOs, CTOs, chief architects, procurement leads and public sector technology advisers. Play alone, or as a group with procurement and security in the room. |
| Time | 30 minutes alone; 45 minutes as a group |
| Practice it teaches | [Build, buy or adopt](../../playbook/strategy/build-buy-adopt.md), [public sector](../../playbook/compliance/public-sector.md), [access control](../../playbook/security/access-control.md), [cloud, on-premises and air-gapped](../../playbook/platform/cloud-on-prem-air-gapped.md) |

## The situation

A national social security agency runs an identity system built in-house 12 years ago. It handles sign-in for 6,000 staff and about 4 million citizens who use the benefits portal. It does not support modern multi-factor authentication, its original developers have left, and an audit has rated it a high risk. All organisations, people and numbers here are fictional.

- The national data protection law and a government cloud policy require citizen identity data to be stored and processed in the country.
- The agency runs two government data centres. No major identity SaaS vendor has an in-country region.
- Budget is approved for three years. The audit committee wants the old system retired within 18 months.
- The agency's platform team has 8 engineers; two have run open source infrastructure in production.
- The national digital identity scheme is expected to offer federation through OpenID Connect within two years.

Four proposals are on the table.

**A. Build.** The agency's engineers write a new identity service. "We know our users and we keep full control."

**B. Buy SaaS.** A leading identity SaaS vendor offers its product, hosted in a neighbouring country, with a contractual promise to add an in-country region "within 24 months".

**C. Adopt open source with support.** Deploy Keycloak, an open source identity and access management project, in both government data centres, with a paid support contract from a local company and two more engineers hired.

**D. Partner.** A national systems integrator builds and runs a custom identity solution on its own framework under a 7-year managed service contract.

Choose before you open the consequences.

<details>
<summary>Consequences of A: build</summary>

Identity looks simple and is not: password storage, MFA, account recovery, session management, OpenID Connect and SAML, brute-force protection, audit logging, accessibility of every sign-in page. After 14 months the team has staff sign-in working and the citizen side half done. A penetration test finds two serious flaws in account recovery. The agency now owns a security-critical product for its whole life, with maintenance of at least 15% to 25% of the build effort every year, and the same key-person risk that made the old system a problem.

Identity is not what makes a social security agency different. The [build, buy or adopt](../../playbook/strategy/build-buy-adopt.md#the-four-options) page reserves Build for core differentiators.

</details>

<details>
<summary>Consequences of B: buy SaaS</summary>

The product is excellent and the staff pilot goes well. Then legal confirms that hosting citizen identity data abroad breaches the data protection law today, whatever the vendor promises for 24 months from now. The agency could use the SaaS for staff only, but that leaves the citizen half, the larger and riskier half, unsolved. Exit is also costly: user records can be exported, but password hashes in the vendor's format and its custom rules cannot.

On the scoring matrix, B scores 1 on sovereignty. When a hosting rule is mandatory, the [build, buy or adopt](../../playbook/strategy/build-buy-adopt.md#cloud-on-premises-and-air-gapped) page says to treat such options as unavailable, not as low-scoring.

</details>

<details>
<summary>Consequences of C: adopt open source with support</summary>

Keycloak supports OpenID Connect, SAML, MFA and federation, and it runs in the agency's own data centres. The first 4 months go into building the deployment properly: high availability across both data centres, a tested upgrade process, backups of the identity configuration, and monitoring. Staff move over at month 7, citizens in phases from month 10. The old system is retired at month 16.

The cost is real. The agency must track upstream releases and apply security updates quickly, keep skills in at least two people per critical task, and fund the support contract every year. When the national identity scheme offers OpenID Connect federation, connecting it is configuration, not a new project.

</details>

<details>
<summary>Consequences of D: partner</summary>

The integrator delivers on time, and the service runs. But the custom framework belongs to the integrator, the source code is not delivered under the contract, and the export format for user data is "to be agreed at exit". In year 5 the integrator raises prices and the agency finds that no other supplier can take over without a rebuild. The agency has replaced one locked-in identity system with another.

Partnering can be the right call when skills are missing, but the [lock-in and sovereignty checks](../../playbook/strategy/build-buy-adopt.md#lock-in-and-sovereignty-checks) would have flagged three or more "no" answers here before signature.

</details>

## The scoring matrix

The agency raised the weights for sovereignty and exit, as the playbook suggests for public sector. Scores run from 1 (poor) to 5 (strong); weighted score = weight x score. These are the scores the agency's panel agreed after the consequences above were known.

| Criterion | Weight | A Build | B Buy SaaS | C Adopt | D Partner |
|---|---|---|---|---|---|
| Fit to requirements | 15 | 2 (30) | 5 (75) | 4 (60) | 4 (60) |
| Total cost of ownership | 15 | 1 (15) | 3 (45) | 4 (60) | 2 (30) |
| Exit cost and lock-in | 15 | 4 (60) | 2 (30) | 5 (75) | 1 (15) |
| Sovereignty and hosting | 20 | 5 (100) | 1 (20) | 5 (100) | 4 (80) |
| Open standards | 10 | 3 (30) | 4 (40) | 5 (50) | 2 (20) |
| Security and supply chain | 10 | 2 (20) | 5 (50) | 4 (40) | 3 (30) |
| Operability | 10 | 2 (20) | 5 (50) | 3 (30) | 4 (40) |
| Project or supplier health | 5 | 2 (10) | 4 (20) | 4 (20) | 3 (15) |
| **Total** | **100** | **285** | **330** | **435** | **290** |

C leads by more than 10%, so it is not a tie. B is also excluded outright by the hosting rule.

## What the playbook recommends, and why

**C, adopt with paid support,** for this agency. The [build, buy or adopt](../../playbook/strategy/build-buy-adopt.md) page says: build only what differentiates you; compare the rest with a weighted matrix and total cost of ownership over 3 to 5 years, including the cost of leaving; prefer open standards you can run where your data must live. Identity is not a differentiator for a social security agency, the hosting rule is mandatory, and an open source project with a support contract is the only option that meets the rule, keeps exit cheap and follows open standards.

The answer changes with the facts. If the law allowed hosting abroad and the agency had no platform team, B could win. Write the decision, its drivers and its exit plan in an [ADR](../../templates/docs/adr.md), and check the [public sector](../../playbook/compliance/public-sector.md) guidance on open standards and publishing code.

## Debrief questions

1. Did you set the weights before you looked at the options? Would you have chosen differently if you had scored first?
2. What is the exit plan for your current identity provider, and has anyone tested it?
3. Which of your systems was built in-house even though it is not a differentiator? What does it cost each year?
