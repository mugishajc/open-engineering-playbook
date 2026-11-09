# Control mapping

Do the engineering work once and show the evidence many times. Each practice in this playbook produces records as a side effect of normal work: pull request history, CI logs, signed SBOMs, postmortems. This page maps those practices to the frameworks auditors and regulators ask about, so one body of evidence answers many questionnaires.

> **Not legal advice.** This mapping is a starting point for discussion with your compliance, legal and audit teams. Frameworks change and their scope depends on your sector, size and country. Check the current text of each law on EUR-Lex or the official publisher, and confirm control numbers against the edition your auditor uses.

## Outcomes

Starting points. Tune them to your organisation.

- At least 80% of audit evidence requests are answered by a link or a query to a system of record (repository, CI, ticketing, logs), not by screenshots.
- Engineering time spent on an annual audit falls year on year. Track it in hours.
- Every control owned by engineering maps to at least one playbook practice and one evidence source.
- Evidence is retained for the period your strictest obligation requires.

## How to read the tables

- **ISO/IEC 27001:2022** numbers are Annex A controls unless marked "Clause".
- **SOC 2** codes are AICPA Trust Services Criteria (CC = common criteria, A = availability, C = confidentiality, PI = processing integrity, P = privacy).
- **NIST SSDF** codes are practices from SP 800-218 v1.1, grouped as PO (Prepare the Organization), PS (Protect the Software), PW (Produce Well-Secured Software) and RV (Respond to Vulnerabilities).
- **SLSA** refers to version 1.2: the Build track (L1 to L3, unchanged in substance from v1.1) and the Source track.
- **OSPS Baseline** is mapped at control family level only: AC (access control), BR (build and release), DO (documentation), GV (governance), LE (legal), QA (quality), SA (security assessment), VM (vulnerability management). Check control IDs at the source.
- **EU CRA** is Regulation (EU) 2024/2847 and applies to manufacturers of products with digital elements.
- **NIS2** is Directive (EU) 2022/2555. References are to Article 21(2) risk management measures, Article 12 coordinated vulnerability disclosure and Article 23 reporting. National transposition laws apply, not the directive directly. For DNS, TLD registries, cloud, data centre, content delivery network, managed service and managed security providers, online marketplaces, search engines, social networks and trust service providers, Implementing Regulation (EU) 2024/2690 sets the Article 21 measures and the significant incident criteria in detail and applies directly. Map to its Annex, not only to Article 21.
- **EU DORA** is the Digital Operational Resilience Act, Regulation (EU) 2022/2554, for financial entities. It is unrelated to the DORA software delivery metrics. Supervisors test the ICT risk management articles against the regulatory technical standards in Commission Delegated Regulation (EU) 2024/1774, so the table cites both: "Art." is the Regulation and "RTS Art." is the delegated regulation. The small entities listed in DORA Art. 16(1), such as small and non-interconnected investment firms, use the simplified framework in Art. 16 and Title III of the RTS (Arts. 28 to 41) instead.
- "n/a" means no direct mapping. The practice may still support the framework indirectly.

## Table 1: standards and frameworks

| Playbook practice | ISO/IEC 27001:2022 | SOC 2 | NIST SSDF | SLSA | OSPS |
|---|---|---|---|---|---|
| [Source control](../delivery/source-control.md) | 8.4, 8.9, 8.32 | CC6.1, CC8.1 | PS.1 | Source track | AC |
| [Code review](../delivery/code-review.md) | 5.3, 8.28, 8.32 | CC8.1 | PW.7 | Source track | QA |
| [Testing](../delivery/testing.md), [quality engineering](../quality/quality-engineering.md) | 8.29, 8.33 | CC8.1 | PW.8 | n/a | QA |
| [Continuous integration](../delivery/continuous-integration.md) | 8.25, 8.29 | CC8.1 | PO.3, PW.6 | Build L1 to L3 | BR |
| [Release management](../delivery/release-management.md) | 8.32 | CC8.1 | PS.2, PS.3 | Build provenance | BR |
| [GitOps and deployment](../delivery/gitops-and-deployment.md) | 8.9, 8.32 | CC8.1 | PS.1 | n/a | BR |
| [Infrastructure as code](../delivery/infrastructure-as-code.md) | 8.9, 8.32 | CC7.1, CC8.1 | PO.5 | n/a | n/a |
| [Versioning and changelogs](../delivery/versioning-and-changelogs.md) | 8.32 | CC8.1 | PS.3 | n/a | DO |
| [Feature flags](../delivery/feature-flags.md) | 8.32 | CC8.1 | n/a | n/a | n/a |
| [Environments](../delivery/environments.md) | 8.31, 8.33 | CC6.1, CC8.1 | PO.5 | n/a | n/a |
| [Database changes](../delivery/database-changes.md) | 8.13, 8.32 | CC8.1 | n/a | n/a | n/a |
| [Service levels](../reliability/service-levels.md) | 8.6, 8.16 | A1.1, CC7.2 | n/a | n/a | n/a |
| [Incident management](../reliability/incident-management.md) | 5.5, 5.24 to 5.28, 6.8 | CC7.3 to CC7.5 | n/a | n/a | n/a |
| [Postmortems](../reliability/postmortems.md) | 5.27 | CC7.4, CC7.5 | RV.3 | n/a | n/a |
| [On-call](../reliability/on-call.md) | 5.24, 5.26, 8.16 | CC7.2, CC7.4 | n/a | n/a | n/a |
| [Production readiness](../reliability/production-readiness.md) | 5.30, 8.27, 8.29 | A1.2, CC7.1, CC8.1 | PW.1, PW.9 | n/a | n/a |
| [Backup and recovery](../reliability/backup-and-recovery.md) | 5.29, 5.30, 8.13, 8.14 | A1.2, A1.3 | n/a | n/a | n/a |
| [Change management](../reliability/change-management.md) | 8.32 | CC8.1 | PO.4 | n/a | n/a |
| [Secure development](../security/secure-development.md) | 8.25 to 8.29 | CC7.1, CC8.1 | PO.1, PW.1, PW.2, PW.5, PW.9 | n/a | SA |
| [Supply chain](../security/supply-chain.md) | 5.21, 8.19, 8.30 | CC6.8, CC8.1, CC9.2 | PS.2, PS.3, PW.4 | Build L2 to L3 | BR |
| [Secrets](../security/secrets.md) | 5.17, 8.15, 8.24 | CC6.1 | PO.5, PS.1 | n/a | BR |
| [Dependencies](../security/dependencies.md) | 5.21, 8.8, 8.19 | CC6.8, CC7.1, CC9.2 | PW.4, RV.1 | n/a | QA |
| [Vulnerability management](../security/vulnerability-management.md) | 5.7, 8.8 | CC7.1 | RV.1 to RV.3 | n/a | VM |
| [Access control](../security/access-control.md) | 5.15 to 5.18, 8.2, 8.5, 8.18 | CC6.1 to CC6.3 | PO.5, PS.1 | n/a | AC |
| [Zero trust](../security/zero-trust.md) | 5.15, 8.1, 8.5, 8.16, 8.20, 8.22 | CC6.1, CC6.6 | PO.5 | n/a | n/a |
| [Post-quantum readiness](../security/post-quantum-readiness.md) | 8.24 | CC6.1, CC6.7 | n/a | n/a | n/a |
| [Third-party and SaaS risk](../security/third-party-and-saas-risk.md) | 5.19 to 5.23 | CC9.2 | PO.1 | n/a | n/a |
| [Decision records](../architecture/decision-records.md) | 8.27, 8.32 | CC8.1 | PW.1, PW.2 | n/a | n/a |
| [Observability](../architecture/observability.md) | 8.15, 8.16, 8.17 | CC7.2 | n/a | n/a | n/a |
| [Developer platform](../platform/developer-platform.md), [golden paths](../platform/golden-paths.md) | 8.9, 8.25, 8.31, 8.32 | CC8.1 | PO.3 | Build L2 to L3 | BR |
| [Data governance](../data/data-governance.md) | 5.9, 5.12, 5.13, 5.33, 5.34 | C1.1, P series | n/a | n/a | n/a |
| [Data quality](../data/data-quality.md) | n/a | PI1 series | n/a | n/a | n/a |
| [Data security and privacy](../data/data-security-and-privacy.md) | 5.12, 5.14, 5.34, 8.10 to 8.12, 8.24, 8.33 | C1.1, C1.2, P series | n/a | n/a | n/a |
| [AI governance](../ai/ai-governance.md) | see Table 3 | CC3.2 | n/a | n/a | n/a |
| [AI application security](../ai/ai-application-security.md) | 8.25, 8.28, 8.29 | CC7.1 | PW.1, PW.7, PW.8 | n/a | SA |
| [Building with AI](../ai/building-with-ai.md), [code assistants](../people/code-assistants.md) | 8.28 | CC8.1 | PW.7 | n/a | n/a |
| [Onboarding](../people/onboarding.md), [documentation](../people/documentation.md) | 5.37, 6.3 | CC1.4, CC2.2 | PO.2 | n/a | DO |
| [Technical strategy](../strategy/technical-strategy.md), [engineering governance](../operating-model/engineering-governance.md) | 5.1, 5.4, 5.8 | CC1, CC3, CC5 series | PO.1, PO.2, PO.4 | n/a | GV |
| [IT governance](../operating-model/it-governance.md) | 5.1, 5.4, 5.31, 5.35, Clause 9.3 | CC1, CC2, CC4 series | PO.1, PO.2 | n/a | GV |
| [Architecture practice](../architecture/architecture-practice.md) | 8.27 | CC8.1 | PW.1, PW.2 | n/a | SA |
| [Portfolio and capacity](../strategy/portfolio-and-capacity.md) | 5.8 | CC3.2 | PO.1 | n/a | n/a |
| [Build, buy, adopt or partner](../strategy/build-buy-adopt.md) | 5.19 to 5.23 | CC9.2 | PO.1, PW.4 | n/a | LE |
| [Metrics](../measurement/metrics.md) | Clause 9.1 | CC4.1 | PO.4 | n/a | n/a |

## Table 2: EU law and the evidence each practice produces

| Playbook practice | EU CRA | NIS2 | EU DORA (Reg. 2022/2554, and RTS 2024/1774) | Evidence produced as a side effect |
|---|---|---|---|---|
| Source control | Annex I Part I | 21(2)(e), (i) | Art. 9(4)(e); RTS Arts. 16(1)(c), 17 | branch protection settings, repository audit log, signed commits, ruleset bypass log |
| Code review | Annex I Part I | 21(2)(e) | Art. 9(4)(e); RTS Arts. 16(3), 17(1)(b) | pull request history with an approver who is not the author, ruleset bypass log, deployment to pull request reconciliation report |
| Testing, quality engineering | Annex I Part II | 21(2)(e), (f) | Arts. 24, 25; RTS Art. 16(2) to (4) | CI test reports, test result history |
| Continuous integration | Annex I Part I | 21(2)(e) | Art. 9(4)(e); RTS Arts. 16, 17 | CI logs, build provenance attestations |
| Release management | Annex I Part II | 21(2)(e) | Art. 9(4)(e); RTS Art. 17 | signed artefacts, release notes, deployment log |
| GitOps and deployment | n/a | 21(2)(e) | Art. 9(4)(e); RTS Art. 17 | Git history of desired state, sync and rollout logs |
| Infrastructure as code | n/a | 21(2)(e) | Art. 9(4)(e); RTS Arts. 11(2)(b), 17 | plan output in pull requests, policy check results, drift reports |
| Versioning and changelogs | Annex I Part II | n/a | n/a | tags, changelog, security fix notes |
| Feature flags | n/a | n/a | Art. 9(4)(e); RTS Art. 17 | flag change audit log |
| Environments | n/a | 21(2)(e) | Art. 9; RTS Art. 8(2)(b)(v) to (vii) | environment configuration in code, access logs |
| Database changes | n/a | n/a | Arts. 9(4)(e), 12; RTS Art. 17 | migration files and run logs |
| Service levels | n/a | 21(2)(c) | Arts. 7, 11; RTS Art. 9 | SLO dashboards, error budget reports, capacity reports |
| Incident management | Art. 14 | 21(2)(b), Art. 23 | Arts. 14, 17 to 19; RTS Art. 22; Delegated Regulation (EU) 2025/301 | incident timeline, paging records, regulator notifications |
| Postmortems | n/a | 21(2)(b), (f) | Art. 13 | postmortem documents, tracked actions |
| On-call | n/a | 21(2)(b) | Arts. 10, 11 | rota, paging and acknowledgement logs |
| Production readiness | Annex I Part I | 21(2)(c), (e) | Arts. 9, 11; RTS Art. 16 | completed readiness reviews |
| Backup and recovery | n/a | 21(2)(c) | Arts. 11, 12; RTS Arts. 24 to 26 | backup job logs, restore test results |
| Change management | n/a | 21(2)(e) | Art. 9(4)(e); RTS Art. 17 | change records generated from pull request and deployment history, emergency change records, ruleset bypass log, deployment to pull request reconciliation report |
| Secure development | Annex I Part I | 21(2)(e) | RTS Art. 16 | threat models, static and dynamic analysis results |
| Supply chain | Annex I Part II (SBOM) | 21(2)(d) | Art. 28; RTS Arts. 10(2)(d), 16 | signed SBOMs, provenance, signature verification logs |
| Secrets | Annex I Part I | 21(2)(h), (i) | Art. 9(4)(d); RTS Arts. 6, 7 | secret scanning results, secrets store audit logs |
| Dependencies | Annex I Part II | 21(2)(d), (e) | Art. 9(4)(f); RTS Art. 10(2)(d) | dependency update pull requests, SBOM changes |
| Vulnerability management | Annex I Part II, Art. 14 | 21(2)(e), Art. 12 | Art. 9(4)(f); RTS Art. 10 | scan results (weekly for assets supporting critical or important functions, RTS Art. 10(2)), VEX statements, time to fix |
| Access control | Annex I Part I | 21(2)(i), (j) | Art. 9(4)(c), (d); RTS Arts. 20, 21 | access reviews, identity provider logs, MFA enrolment, privileged access grants |
| Zero trust | Annex I Part I | 21(2)(i), (j) | Art. 9(4)(b); RTS Arts. 11, 13 | policy decision logs, device posture reports |
| Post-quantum readiness | Annex I Part I | 21(2)(h) | RTS Arts. 6, 7 | cryptographic inventory (CBOM), migration plan |
| Third-party and SaaS risk | n/a | 21(2)(d) | Arts. 28(3), 28(8), 29, 30; Implementing Regulation (EU) 2024/2956 for the register | register of information, due diligence records, tested exit plans |
| Decision records | Annex I Part I | 21(2)(e) | Art. 6 | merged decision records |
| Observability | Annex I Part I | 21(2)(b) | Art. 10; RTS Arts. 12, 23 | logs, traces, alert history, clock synchronisation records |
| Developer platform, golden paths | n/a | 21(2)(e) | Art. 7; RTS Art. 16 | template versions, adoption reports |
| Data governance | n/a | 21(2)(i) | Art. 8; RTS Arts. 4, 5 | data catalogue, classification labels, data owner list |
| Data quality | n/a | n/a | n/a | data contract checks, quality test results |
| Data security and privacy | Annex I Part I | 21(2)(h), (i) | Art. 9(2); RTS Arts. 6, 11, 14 | DPIAs, deletion logs, access logs |
| AI governance | see Table 3 | 21(2)(a) | Art. 6 | AI use-case register, assessments, approvals |
| AI application security | Annex I Part I | 21(2)(e) | RTS Art. 16 | prompt injection test results, red-team findings |
| Building with AI, code assistants | n/a | n/a | n/a | pull request history showing human review, policy acknowledgements |
| Onboarding, documentation | n/a | 21(2)(g) | Art. 13(6); RTS Art. 19 | training records, runbooks |
| Strategy and governance | n/a | 21(2)(a), (f), Art. 20 | Arts. 5, 6 | approved strategy, waiver register, review outcomes |
| IT governance | n/a | Art. 20, 21(2)(a), (f) | Art. 5 | board reports, approved risk appetite, policy approvals |
| Architecture practice | Annex I Part I | 21(2)(e) | Arts. 6, 9 | quality attribute scenarios, fitness function results in CI, C4 diagrams as code |
| Portfolio and capacity | n/a | 21(2)(a) | Art. 6 | capacity split reports, portfolio review decisions |
| Build, buy, adopt or partner | n/a | 21(2)(d) | Arts. 28 to 30 | scored decisions, exit plans |
| Metrics | n/a | 21(2)(f) | Art. 13 | delivery metric dashboards |

## Table 3: AI, zero trust and post-quantum frameworks

These frameworks cover areas the general security standards address only in part.

| Playbook practice | EU AI Act (Reg. (EU) 2024/1689) | ISO/IEC 42001:2023 | NIST AI RMF 1.0 | Evidence |
|---|---|---|---|---|
| [AI governance](../ai/ai-governance.md): register and risk classification | Art. 4 (AI literacy), Art. 5 (prohibited practices), Art. 6 and Annex III (high-risk), Art. 9 (risk management) | Clauses 4 to 10; Annex A.2 to A.5 | Govern, Map | AI use-case register, [use-case assessments](../../templates/docs/ai-use-case-assessment.md), approvals |
| AI governance: deployer duties | Art. 26 (deployers), Art. 27 (fundamental rights impact assessment) | Annex A.5, A.9 | Map, Manage | impact assessments, oversight assignments |
| [Data governance](../data/data-governance.md) and [data quality](../data/data-quality.md) for AI | Art. 10 (data and data governance) | Annex A.7 | Map, Measure | dataset records, lineage, quality test results |
| [AI application security](../ai/ai-application-security.md) | Art. 15 (accuracy, robustness, cybersecurity) | Annex A.6 | Measure, Manage; NIST AI 600-1 | evaluation results, red-team reports, OWASP LLM Top 10 test coverage |
| [Observability](../architecture/observability.md) for AI systems | Art. 12 (record-keeping), Art. 14 (human oversight) | Annex A.6 | Manage | inference logs, human override records |
| Transparency to users | Art. 13, Art. 50 | Annex A.8 | Govern | user notices, model and system documentation |

| Playbook practice | Reference | What to show |
|---|---|---|
| [Zero trust](../security/zero-trust.md) | NIST SP 800-207; CISA Zero Trust Maturity Model v2.0 (pillars: Identity, Devices, Networks, Applications and Workloads, Data) | current and target maturity per pillar, policy decision logs |
| [Post-quantum readiness](../security/post-quantum-readiness.md) | NIST FIPS 203 (ML-KEM), FIPS 204 (ML-DSA), FIPS 205 (SLH-DSA); NIST IR 8547 transition timeline | cryptographic inventory, systems ranked by how long their data must stay secret, migration plan |

EU AI Act dates after the 2026 Digital Omnibus on AI (in force 27 Jul 2026): Article 50 transparency duties from 2 Aug 2026; high-risk obligations from 2 Dec 2027 for stand-alone (Annex III) systems and 2 Aug 2028 for systems embedded in regulated products. The full timeline is in [AI governance](../ai/ai-governance.md). Check EUR-Lex for the current text.

## Practice

### Foundation

Solo and Startup. Turn on the practices that generate evidence for free: protected branches, required reviews, tagged releases, and CI logs and attestations kept for at least 12 months. On GitHub, set the maximum retention and export logs and attestations to your own storage on a schedule, because the forge deletes them after at most 400 days (90 for public repositories). When a customer sends a security questionnaire, answer from this table and link to the evidence.

### Standard

Scale-up and Enterprise. Keep a control register that lists, for each control: owner, playbook practice, evidence source, query or link, retention period. Automate evidence collection from repositories, CI and ticketing on a schedule. Review the register every 6 months.

Prove that the population is complete, not only that the changes you can see were reviewed. Auditors test this first: forge admins can bypass rulesets, branch protection can be switched off for ten minutes, and people can change production from a console, `kubectl` or a break-glass account.

- Reconcile production deployments to approved pull requests every month. Every deployment in the deploy log matches a merged pull request with an approver who is not the author, or an emergency change record approved after the event.
- Alert on every ruleset or branch protection bypass and on any change to those settings. Keep the forge audit log entries as evidence.
- Keep the list of people who can bypass to 2 or 3, and review it every quarter.
- Compare cloud and cluster audit logs with the deploy log for changes made outside the pipeline. Each one becomes an emergency change record or an incident.

### Assured

Regulated and Public sector. Everything in Standard, plus:

- Give auditors read-only access to systems of record.
- Store evidence in write-once or tamper-evident storage for the retention period.
- Test a sample of controls each quarter (for example 25 changes) and record the result.
- Map national laws that transpose NIS2, and sector rules, into the register with legal sign-off.

## Cloud, on-premises and air-gapped

Evidence must live where the work happens. In air-gapped networks, keep CI logs, SBOMs and signatures inside the network and give auditors access there. Export only summaries that the security officer has approved. Make sure timestamps come from a trusted internal time source so evidence holds up.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A separate compliance project that recreates evidence by hand | Collect evidence from systems of record. |
| Screenshots as evidence | Links and queries that an auditor can rerun. |
| One mapping per framework, maintained by different teams | One register, many columns. |
| Treating the mapping as legal advice | Confirm scope and interpretation with counsel. |

## Templates

- [Risk register](../../templates/strategy/risk-register.csv)
- [Production readiness review](../../templates/docs/production-readiness-review.md)
- [AI use-case assessment](../../templates/docs/ai-use-case-assessment.md)
- [Data classification](../../templates/docs/data-classification.md)

## Sources

- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
- ISO/IEC 42001:2023: https://www.iso.org/standard/42001
- AICPA Trust Services Criteria (SOC 2): https://www.aicpa-cima.com/topic/audit-assurance/audit-and-assurance-greater-than-soc-2
- NIST SSDF: https://csrc.nist.gov/projects/ssdf
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST SP 800-207 Zero Trust Architecture: https://csrc.nist.gov/pubs/sp/800/207/final
- NIST post-quantum cryptography standards: https://csrc.nist.gov/projects/post-quantum-cryptography
- CISA Zero Trust Maturity Model: https://www.cisa.gov/zero-trust-maturity-model
- SLSA specification: https://slsa.dev/spec/
- OpenSSF OSPS Baseline: https://baseline.openssf.org
- EU Cyber Resilience Act: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- NIS2 Directive: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- EU Digital Operational Resilience Act: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- Commission Delegated Regulation (EU) 2024/1774, RTS on the ICT risk management framework: https://eur-lex.europa.eu/eli/reg_del/2024/1774/oj
- Commission Delegated Regulation (EU) 2025/301, RTS on major ICT-related incident reports: https://eur-lex.europa.eu/eli/reg_del/2025/301/oj
- Commission Implementing Regulation (EU) 2024/2690, NIS2 technical and methodological requirements: https://eur-lex.europa.eu/eli/reg_impl/2024/2690/oj
- GitHub Docs, retention period for GitHub Actions artifacts and logs: https://docs.github.com/en/organizations/managing-organization-settings/configuring-the-retention-period-for-github-actions-artifacts-and-logs-in-your-organization
- EU AI Act: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
