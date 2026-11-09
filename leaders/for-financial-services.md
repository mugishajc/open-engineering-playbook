# For financial services technology and risk leaders

Organise technology around the business services customers and markets depend on, set how much disruption each can tolerate, and prove with tests that you stay inside those limits. Build the controls supervisors expect into the delivery pipeline so that evidence is a by-product of normal work, not a project before each inspection. Treat cloud providers, core banking vendors and AI models as risks you manage with registers, validation and tested exits, because supervisors hold the firm accountable for them, not the supplier.

## When to use this

This page is for CTOs, CIOs, chief risk officers (CROs) and heads of architecture at banks, insurers, payment firms and other financial entities.

- You need to show a supervisor that important business services stay within impact tolerances.
- You are an EU financial entity and must evidence compliance with the Digital Operational Resilience Act (EU DORA).
- Most of your critical services now run on one or two cloud providers.
- You plan to replace or modernise a core banking or policy administration system, or a mainframe.
- Risk and engineering argue about whether frequent releases are safe.
- AI models are entering credit, fraud, pricing or customer service decisions.

EU DORA here means Regulation (EU) 2022/2554. It is unrelated to the DORA software delivery metrics. The engineering controls are in [regulated industries](../playbook/compliance/regulated-industries.md) and [control mapping](../playbook/compliance/control-mapping.md); this page covers the leadership decisions.

## Operational resilience

The Basel Committee's Principles for Operational Resilience (March 2021) and the UK approach (PRA SS1/21 and FCA PS21/3) share one method. UK firms had to be able to remain within impact tolerances by 31 March 2025.

Two newer UK rules matter to technology leaders. From 18 Mar 2027, FCA firms report operational incidents and material third-party arrangements under one regime (FCA PS26/2, with parallel PRA and Bank of England rules). Since 1 Jan 2025, HM Treasury can designate critical third parties, such as cloud providers, for direct oversight by the regulators (PRA PS16/24, FCA PS24/16). Designation does not move your own accountability for the services you buy.

| Step | What to do | Owner | Starting point |
|---|---|---|---|
| 1. Identify important business services | services whose disruption would cause intolerable harm to customers or market integrity, or threaten the firm's safety and soundness | business, with risk | a short list, each with a named executive owner |
| 2. Set impact tolerances | the maximum tolerable disruption, expressed as time and, where useful, volume or value | business executive, approved by the board | "payments to customers restored within N hours" |
| 3. Map the service | people, processes, technology, facilities, data and suppliers the service needs | architecture and service owners | generated from the service catalogue and dependency data, not drawn once by hand |
| 4. Test with severe but plausible scenarios | regional cloud outage, ransomware, loss of a key supplier, corrupted data | technology and risk | each important service tested at least once a year |
| 5. Fix vulnerabilities found | where a scenario shows the tolerance would be breached | named owner, date | tracked in the [risk register](../templates/strategy/risk-register.csv) |
| 6. Self-assess and report | yearly, approved by the board | CRO and CTO | evidence linked, not described |

Link impact tolerances to engineering targets. Each important business service needs [service level objectives](../playbook/reliability/service-levels.md) stricter than its tolerance, tested [backup and recovery](../playbook/reliability/backup-and-recovery.md), and rehearsed [incident management](../playbook/reliability/incident-management.md).

## EU DORA mapped to the playbook

EU DORA applies from 17 Jan 2025. Read the regulation and its technical standards; this table shows where the playbook helps you produce evidence.

| EU DORA area | What supervisors look for | Playbook pages |
|---|---|---|
| ICT risk management (Chapter II) | a framework approved by the management body; asset inventory; protection, detection, response, recovery; backup and restore testing; learning from incidents | [IT governance](../playbook/operating-model/it-governance.md), [secure development](../playbook/security/secure-development.md), [access control](../playbook/security/access-control.md), [backup and recovery](../playbook/reliability/backup-and-recovery.md), [change management](../playbook/reliability/change-management.md) |
| ICT-related incident management and reporting (Chapter III) | classification of incidents; reporting of major incidents to the competent authority; root cause analysis | [incident management](../playbook/reliability/incident-management.md), [postmortems](../playbook/reliability/postmortems.md), [root cause analysis](../playbook/reliability/root-cause-analysis.md), [crisis leadership](crisis-leadership.md) |
| Digital operational resilience testing (Chapter IV) | a testing programme; threat-led penetration testing (TLPT) for entities identified by authorities, with TIBER-EU as the reference framework | [testing](../playbook/delivery/testing.md), [vulnerability management](../playbook/security/vulnerability-management.md), [production readiness](../playbook/reliability/production-readiness.md), [rollbacks](../playbook/reliability/rollbacks.md) |
| ICT third-party risk (Chapter V) | a register of information on all ICT third-party arrangements; due diligence; contract terms; exit strategies; concentration risk | [third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md), [build, buy or adopt](../playbook/strategy/build-buy-adopt.md), [vendor questionnaire](../templates/docs/vendor-risk-questionnaire.md) |
| Information sharing (Chapter VI) | voluntary sharing of threat intelligence in trusted communities | [vulnerability management](../playbook/security/vulnerability-management.md) |

## Third-party and cloud concentration risk

- Keep the register of ICT third-party arrangements as data, not a spreadsheet emailed before audits. Record which important business services each supplier supports.
- For each critical (Tier 1) supplier, hold a written exit plan, reviewed every year: target state, data export, time needed and cost. Run a real data export and import into the alternative, timed, at least once a year. Paper walk-throughs count only for Tier 2. DORA requires exit plans for ICT services supporting critical or important functions to be sufficiently tested (Art. 28(8)).
- Measure concentration: the share of important business services that depend on a single provider or region. Report it to the board every quarter with the risk appetite threshold.
- Design for the failure of one cloud region before designing for the failure of a whole provider. A multi-region design within one provider is cheaper and often enough; a multi-provider design must be justified by an impact tolerance.
- Read the contract for audit rights, incident notification times, sub-contracting and data location before signing, not at renewal.

## Model risk for AI

The US Federal Reserve's SR 11-7 (2011) guidance on model risk management is the reference many banks use worldwide. In the UK, PRA SS1/23 (effective May 2024) applies to banks with internal model approval and covers AI models: it expects a model inventory, risk tiering and an accountable senior manager. Use the two together; they agree on inventory and validation. In the EU, AI used to assess the creditworthiness of individuals is high-risk under the AI Act (Annex III, point 5(b)). Apply the three SR 11-7 elements to AI and language models, not only to statistical models.

| SR 11-7 element | Applied to AI systems |
|---|---|
| Model development, implementation and use | documented purpose and limits; evaluation sets owned by the business; [building with AI](../playbook/ai/building-with-ai.md) |
| Model validation | independent validation before production and after material change, including bias, robustness, prompt injection and data leakage tests; [AI application security](../playbook/ai/ai-application-security.md) |
| Governance, policies and controls | a model inventory that includes AI systems and vendor models; risk tiers; approval records; [AI governance](../playbook/ai/ai-governance.md) |

A vendor's model is still your model risk. Ask for evaluation evidence, change notices and the right to test.

## PCI DSS

PCI DSS v4.0.1 (June 2024) was current at the time of writing; check the PCI Security Standards Council site for later versions. The requirements that v4.0 had future-dated became mandatory on 31 March 2025.

- Reduce scope first: tokenise card data and keep it out of as many systems as possible. Every system removed from scope is a control you no longer evidence.
- Put the development requirements into the pipeline: secure development training, code review, vulnerability scanning and change control as covered in [secure development](../playbook/security/secure-development.md) and [code review](../playbook/delivery/code-review.md).
- Payment pages: keep an authorised inventory of scripts, with the reason for each and an integrity check (Req. 6.4.3), and detect changes to scripts and security headers at least weekly (Req. 11.6.1). If you use SAQ A, confirm you still meet the eligibility criterion on script attacks that the PCI SSC added in January 2025.
- Confirm scope at least every 12 months (Req. 12.5.2); MFA for all access into the cardholder data environment (Req. 8.4.2); 12 months of audit logs with the last 3 months immediately available (Req. 10.5.1).

## Core banking and mainframe modernisation

| Decision | Recommendation (starting point) |
|---|---|
| Replace in one cut-over or move in steps | in steps, using the strangler pattern, unless the vendor's product forces a single cut-over |
| What moves first | new products or a low-risk customer segment, not the general ledger |
| Coexistence | run old and new systems side by side, with reconciliation every day and an owner for every break |
| Data migration | rehearse the full migration at least 3 times on production-sized data before go-live; each rehearsal must reconcile to zero unexplained differences |
| Mainframe | decide per workload: keep and expose through APIs, rehost, refactor or retire; Gartner's TIME model (Tolerate, Invest, Migrate, Eliminate) helps sort the portfolio |
| Payments messaging | design new payment flows on ISO 20022 so data survives end to end |
| Rollback | a written rollback or fall-forward plan for each migration wave, timed in rehearsal |

See [legacy modernisation](../playbook/architecture/legacy-modernisation.md), [database changes](../playbook/delivery/database-changes.md), [transition playbook](../playbook/strategy/transition-playbook.md) and [technical due diligence](technical-due-diligence.md) for vendor assessment.

## Continuous delivery under regulation

Supervisors ask for control and evidence. They rarely require a weekly change board. Replace manual approvals for standard changes with automated controls (independent review, protected branches, signed artefacts, deployment records) and keep human boards for the small set of major changes. The full method, with how it satisfies ISO/IEC 27001 control 8.32 and SOC 2 CC8.1, is in [change management](../playbook/reliability/change-management.md). Measure change fail rate and failed deployment recovery time per change class, so risk can see that the faster path is also the safer one.

## Evidence for supervisors

Evidence for any single change can be produced within 1 hour; a sample of 25 changes within 1 working day. The same targets apply in [regulated industries](../playbook/compliance/regulated-industries.md) and the [regulated profile](../profiles/regulated.md).

| Supervisor asks | Evidence you should produce within 1 working day |
|---|---|
| Who approved this change and what was tested? | pull request, CI results, deployment record |
| Can you stay within tolerance if region X fails? | last scenario test report, with the measured recovery time |
| Which suppliers support this important business service? | extract from the register of information |
| How did you handle this incident? | incident timeline, report to the authority, postmortem and action status |
| Is this AI model validated? | model inventory entry, validation report, approval record |

Give internal audit and the second line read-only access to these systems so they can test controls directly. See [control mapping](../playbook/compliance/control-mapping.md).

## Common mistakes

| Mistake | Fix |
|---|---|
| Important business services defined by IT system instead of by customer outcome | Define the service from the customer's point of view, then map systems to it. |
| Impact tolerances set once and never tested | Scenario tests every year, with measured times. |
| Exit plans that exist only on paper | Run a real, timed export and import for Tier 1 suppliers every year. |
| AI models outside the model inventory | One inventory, with risk tiers, covering vendor and in-house models. |
| A big-bang core banking replacement | Strangler pattern, coexistence and rehearsed migrations. |
| Evidence assembled by hand before each inspection | Collect it from systems of record all year. |

## Templates

- [Risk register](../templates/strategy/risk-register.csv)
- [Vendor risk questionnaire](../templates/docs/vendor-risk-questionnaire.md)
- [Production readiness review](../templates/docs/production-readiness-review.md)
- [Board engineering report](../templates/leaders/board-engineering-report.md)
- [Technical due diligence checklist](../templates/leaders/technical-due-diligence-checklist.md)
- [Application portfolio](../templates/leaders/application-portfolio.csv)

## Sources

- Basel Committee on Banking Supervision, Principles for Operational Resilience (March 2021): https://www.bis.org/bcbs/publ/d516.htm
- Bank of England PRA, SS1/21 Operational resilience: impact tolerances for important business services: https://www.bankofengland.co.uk/prudential-regulation/publication/2021/march/operational-resilience-impact-tolerances-for-important-business-services-ss
- FCA, PS21/3 Building operational resilience: https://www.fca.org.uk/publications/policy-statements/ps21-3-building-operational-resilience
- FCA, PS26/2 Operational incident and third party reporting: https://www.fca.org.uk/publications/policy-statements/ps26-2-operational-incident-third-party-reporting
- PRA, PS16/24 Operational resilience: critical third parties to the UK financial sector: https://www.bankofengland.co.uk/prudential-regulation/publication/2024/november/operational-resilience-critical-third-parties-to-the-uk-financial-sector-policy-statement
- PRA, SS1/23 Model risk management principles for banks: https://www.bankofengland.co.uk/prudential-regulation/publication/2023/may/model-risk-management-principles-for-banks-ss
- Regulation (EU) 2022/2554 (Digital Operational Resilience Act): https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- European Central Bank, TIBER-EU framework: https://www.ecb.europa.eu/paym/cyber-resilience/tiber-eu/html/index.en.html
- Board of Governors of the Federal Reserve System, SR 11-7, Guidance on Model Risk Management: https://www.federalreserve.gov/supervisionreg/srletters/sr1107.htm
- PCI Security Standards Council, PCI DSS v4.0.1 and the SAQ A update of January 2025: https://www.pcisecuritystandards.org
- ISO 20022: https://www.iso20022.org
