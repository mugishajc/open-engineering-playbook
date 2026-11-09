# Third-party and SaaS risk

Know every supplier and SaaS tool that touches your data or your production systems, check each one in proportion to the damage it could do, and put the important promises in the contract. SaaS tools are easy to sign up for with a credit card and are often never reviewed, and a breach at a supplier is a breach of your data. A tiered process lets you spend hours on the five suppliers that matter and minutes on the rest.

## Outcomes

Starting points. Tune them to your supplier base.

- 100% of suppliers that process personal or confidential data, or connect to production, are in one supplier register with an owner and a tier.
- Tier 1 suppliers are reviewed before contract and every 12 months; Tier 2 every 24 months.
- 100% of SaaS tools with company data use SSO, and SCIM where offered.
- Contracts with Tier 1 and Tier 2 suppliers require notice of a suspected security incident affecting your data or service within 24 hours of the supplier becoming aware (starting point), and within 4 hours for suppliers that support a function in scope of DORA or NIS2. They also cover data location, transfer mechanism, subprocessor notice and exit terms.
- Unapproved SaaS tools found by discovery are reviewed or removed within 30 days.
- Every Tier 1 supplier has a written exit plan reviewed every year, and a real data export and import into the alternative, timed, at least once a year. Paper walk-throughs count only for Tier 2.

## Supplier tiers

| Tier | Criteria (any one) | Due diligence |
|---|---|---|
| Tier 1 | Processes restricted or large volumes of personal data; runs or connects to production; outage stops a Tier 1 service; holds signing keys or credentials | Full questionnaire, evidence review (certificates, audit reports, pen test summary), contract clauses, exit plan, annual review |
| Tier 2 | Processes confidential data or small volumes of personal data; important but replaceable within weeks | Short questionnaire, certificate or audit report check, standard clauses, review every 2 years |
| Tier 3 | Public or internal data only; easy to replace | Owner confirms data class; SSO if available; no questionnaire |

Data classes come from [data security and privacy](../data/data-security-and-privacy.md).

## Practice

### Foundation

1. **One list.** A supplier register with name, owner, purpose, data shared, tier and renewal date. Start from finance records and SSO logs.
2. **SSO for every SaaS tool** that supports it, so leavers lose access in one place (see [access control](access-control.md)).
3. **Read the security page and the data processing terms** before signing up for anything that will hold customer data.
4. **Limit OAuth grants.** Review which third-party apps have access to your email, documents and code hosting. Remove the ones nobody owns.
5. **Export your data.** Know how to get your data out of each important tool, and try it once.

### Standard

1. **Tier at intake.** A short form (data class, production access, criticality) sets the tier before purchase. Procurement and finance do not pay invoices for Tier 1 or 2 tools without a completed review.
2. **Proportionate questionnaire.** Use the [vendor risk questionnaire](../../templates/docs/vendor-risk-questionnaire.md). Accept existing evidence instead of asking the same questions again: an ISO/IEC 27001 certificate with its statement of applicability scope, a SOC 2 Type II report, or a completed CSA CAIQ for cloud services.
   When you accept a SOC 2 Type II report, check: the period ended within the last 12 months (ask for a bridge letter for the gap); the service you buy is in scope; subservice organisations are included or have their own reports; every exception and the management response; and the complementary user entity controls, which become your controls. Record who checked and when.
3. **Contract clauses** for Tier 1 and 2 (starting points; your legal team owns the wording):
   - Notice of a suspected security incident affecting your data or service within 24 hours of the supplier becoming aware, and within 4 hours for suppliers that support a DORA or NIS2 function. Your own clocks start when you become aware, and a supplier on a 72-hour clause can use up your whole GDPR deadline before you hear (see [incident management](../reliability/incident-management.md)).
   - Data location and the transfer mechanism for each country (see [data security and privacy](../data/data-security-and-privacy.md), Foundation item 10); list of subprocessors with advance notice of changes.
   - Data processing terms that meet GDPR Article 28 or your local equivalent.
   - Vulnerability disclosure and patch commitments; SBOM on request for software you run (see [supply chain](supply-chain.md)).
   - Right to audit or to receive independent audit reports yearly.
   - Data return and deletion at exit, within a stated period.
4. **Shadow SaaS discovery.** Use SSO logs, expense data, browser extension or network data to find tools nobody reviewed. Review or block within 30 days.
5. **Continuous signals.** Watch for supplier breaches, expiring certificates and changes of ownership. A supplier acquired by another company is re-reviewed.
6. **Least privilege for integrations.** Supplier access to production uses its own identity, scoped permissions, logging and an expiry date. No shared admin accounts.

### Assured

Everything in Standard, plus:

1. **Concentration and exit.** For each Tier 1 supplier, document what happens if it fails or you must leave: alternative supplier, data export, time to switch. Review the plan every year and run a real, timed export and import into the alternative at least once a year. A paper walk-through counts only for Tier 2. Under DORA, exit plans for ICT services supporting critical or important functions must be "sufficiently tested" (Art. 28(8)).
2. **Regulated finance.** EU financial entities must keep a register of information on all contracts with ICT third-party service providers (DORA Art. 28(3), in the format set by Implementing Regulation (EU) 2024/2956), assess concentration risk (Art. 29), and include the key contract terms in Art. 30, with more terms for services supporting critical or important functions. Outsourcing rules from your supervisor also apply.
3. **NIS2.** Entities in scope must address supply chain security, including the security of relationships with direct suppliers, as part of their risk management measures (Directive (EU) 2022/2555, Article 21).
4. **Public sector.** Procurement frameworks, data residency and sovereignty rules often decide which suppliers are allowed at all (see [public sector](../compliance/public-sector.md)).
5. **Evidence.** Register, reviews, contracts and exceptions kept for the audit period. This supports ISO/IEC 27001:2022 controls 5.19 to 5.23 (supplier relationships and cloud services) and SOC 2 CC9.2.
6. **Post-quantum and AI questions** for suppliers of cryptographic products and AI services (see [post-quantum readiness](post-quantum-readiness.md) and [AI application security](../ai/ai-application-security.md)).

## Cloud, on-premises and air-gapped

- **Cloud providers** are Tier 1 suppliers. Use their published audit reports and shared responsibility documents, and record which controls are yours.
- **On-premises software suppliers** still matter: their updates and remote support sessions are an attack path. Require approval and logging for every remote support session.
- **Air-gapped networks** depend on suppliers for updates and media. Verify signatures on everything they deliver before import (see [supply chain](supply-chain.md)).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A 300-question spreadsheet sent to every supplier | Tier first. Tier 3 needs no questionnaire. |
| Questionnaire answers accepted without evidence | Ask for certificates, audit reports and their scope. |
| Review at signing, never again | Annual review for Tier 1; re-review on acquisition or breach. |
| SaaS bought on a credit card holds customer data | Intake form; finance checks tier before paying. |
| No way out of a critical supplier | Exit plan and tested data export. |

## Templates

- [Vendor risk questionnaire](../../templates/docs/vendor-risk-questionnaire.md)
- [Exit plan](../../templates/security/exit-plan.md)
- [Risk register](../../templates/strategy/risk-register.csv)

## Sources

- Regulation (EU) 2016/679 (GDPR), Article 28: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Regulation (EU) 2022/2554 (DORA), Articles 28 to 30: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Commission Implementing Regulation (EU) 2024/2956, register of information templates: https://eur-lex.europa.eu/eli/reg_impl/2024/2956/oj
- Directive (EU) 2022/2555 (NIS2), Article 21: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Cloud Security Alliance, Cloud Controls Matrix and CAIQ: https://cloudsecurityalliance.org/research/cloud-controls-matrix
- UK NCSC, supply chain security guidance: https://www.ncsc.gov.uk/collection/supply-chain-security
- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
