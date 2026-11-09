# Horizon scan: 2026 to 2030

Leaders are asked to plan for AI regulation, quantum-safe cryptography, new software liability, agentic systems, rising costs and sovereignty all at once, with no clear way to tell which ones need action this year. Run a short horizon scan twice a year: list the shifts, date the ones with legal deadlines, and start the slow, cheap preparation now. This page gives a starting scan; replace it with your own.

## Outcomes

Starting points. Tune them to your organisation.

- A horizon scan is reviewed every 6 months and feeds the Next and Later horizons of the [technical strategy](technical-strategy.md).
- Every item with a legal deadline has an owner and a plan dated at least 12 months before the deadline.
- A cryptographic inventory covers at least 80% of production systems by the end of the first year.
- Every AI system in production is in a register with a risk classification (see [AI governance](../ai/ai-governance.md)).

## How to run the scan

1. List shifts that could change how you build, run or buy software in the next 5 years. Use regulators' publications, standards bodies and your own incident history, not vendor forecasts.
2. For each, record what is known (with dates and sources) and what is uncertain.
3. Score impact (1 to 5) and certainty (1 to 5). Items scoring 4 or more on both go to Now or Next.
4. For each item, name a "no-regret" first step: work that pays off whatever happens.
5. Assign an owner and a review date. Link actions into the strategy.

Time box: 2 days for a Scale-up, 1 to 2 weeks for an Enterprise. Solo and Startup: one hour, and focus on items your customers' contracts will require.

## The 2026 scan

| Shift | What is known | When it bites | No-regret steps to start now | Playbook page |
|---|---|---|---|---|
| Post-quantum cryptography | NIST published FIPS 203 (ML-KEM), FIPS 204 (ML-DSA) and FIPS 205 (SLH-DSA) on 13 Aug 2024 and selected HQC as an extra key encapsulation mechanism in Mar 2025. NIST IR 8547 plans to deprecate quantum-vulnerable algorithms such as RSA and ECC at 112-bit security after 2030 and disallow them after 2035. | Now for data that must stay secret for 10 years or more, because attackers can record traffic today and decrypt it later ("harvest now, decrypt later"). | Build a cryptographic inventory (CBOM in CycloneDX). Make algorithms configurable. Ask suppliers for their migration plans. | [post-quantum readiness](../security/post-quantum-readiness.md) |
| AI regulation | The EU AI Act (Regulation (EU) 2024/1689) entered into force on 1 Aug 2024. Prohibited practices apply from 2 Feb 2025; general-purpose AI model obligations from 2 Aug 2025. The Digital Omnibus on AI, Regulation (EU) 2026/1744 (in force 27 Jul 2026), defers high-risk obligations to 2 Dec 2027 (stand-alone, Annex III) and 2 Aug 2028 (embedded in regulated products). Transparency duties under Article 50 were not deferred. Dates as of Nov 2026; check EUR-Lex for changes. | Prohibitions and AI literacy now; high-risk duties from late 2027. | Keep an AI use-case register. Classify each use case. Adopt a management approach such as ISO/IEC 42001 or the NIST AI RMF. | [AI governance](../ai/ai-governance.md) |
| EU Cyber Resilience Act | Regulation (EU) 2024/2847 entered into force 10 Dec 2024. Reporting of actively exploited vulnerabilities and severe incidents applies from 11 Sep 2026 (early warning within 24 hours, notification within 72 hours). Most other obligations apply from 11 Dec 2027. | Reporting now; full product obligations Dec 2027. | SBOMs for every release, a vulnerability disclosure policy, a 24-hour triage path, security updates for the support period. | [vulnerability management](../security/vulnerability-management.md), [supply chain](../security/supply-chain.md) |
| Software liability | The CRA makes manufacturers responsible for the security of products with digital elements. The revised EU Product Liability Directive (EU) 2024/2853 brings software within the definition of a product. Member states must apply it to products placed on the market from 9 Dec 2026. | From Dec 2026 for new products; national laws add detail. | Keep evidence of secure development. Document support periods. Review contracts with legal. | [secure development](../security/secure-development.md), [control mapping](../compliance/control-mapping.md) |
| Agentic systems | AI agents that call tools and act on systems are entering production. OWASP publishes a Top 10 for LLM Applications (2025) and a separate Top 10 for Agentic Applications. MITRE ATLAS catalogues attacks on AI systems. | Now, wherever an agent can change data or spend money. | Least privilege for agents, human approval for irreversible actions, logging of every tool call, limits on spend and rate. | [AI application security](../ai/ai-application-security.md), [building with AI](../ai/building-with-ai.md) |
| Skills shift | Code assistants change how engineers learn and review. The evidence on productivity is mixed (see [agile in the AI era](../ways-of-working/agile-in-the-ai-era.md#what-the-evidence-says)). Cutting junior hiring now reduces the senior engineers available later. | Already under way. | Structured hiring, review standards for generated code, deliberate practice for junior engineers. | [hiring](../people/hiring.md), [code assistants](../people/code-assistants.md), [career framework](../people/career-framework.md) |
| Energy and cost | The Software Carbon Intensity specification is published as ISO/IEC 21031:2024. The FinOps Foundation framework (Inform, Optimize, Operate) and the FOCUS billing data specification make cloud cost data comparable. AI workloads raise both cost and energy use. | Now, in budgets and disclosure requests. | Tag resources by owner. Report cost per service. Measure carbon intensity for the largest workloads. | [FinOps](../platform/finops.md), [green software](../platform/green-software.md) |
| Sovereignty | Public bodies and regulated firms ask where data and operators sit, and under which law. | Procurement cycles over the next 1 to 3 years. | Data residency inventory, exit plans, open standards, tested on-premises options for critical systems. | [build, buy, adopt or partner](build-buy-adopt.md), [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md) |
| EU Data Act cloud switching | Regulation (EU) 2023/2854 applies from 12 Sep 2025. Cloud contracts must allow switching with at most two months' notice and a 30-day transition in most cases. Switching charges are limited to direct cost until 12 Jan 2027 and abolished from that date. | Now for new contracts; renewals over the next 1 to 3 years. | Re-price exit costs in every cloud business case. Add switching terms at renewal. | [suppliers and contracts](suppliers-and-contracts.md) |
| Zero trust | NIST SP 800-207 (2020) defines the architecture. The CISA Zero Trust Maturity Model v2.0 (2023) has five pillars: Identity, Devices, Networks, Applications and Workloads, Data. | Ongoing; often a condition of public contracts. | Strong identity for people and workloads, short-lived credentials, no flat networks. | [zero trust](../security/zero-trust.md) |

## Lessons from recent incidents

These incidents changed what "normal" engineering practice should cover.

| Incident | Lesson | Playbook page |
|---|---|---|
| CrowdStrike Falcon content update, July 2024, crashed Windows hosts worldwide | Staged rollouts and canaries apply to configuration and content, not only code. | [GitOps and deployment](../delivery/gitops-and-deployment.md) |
| xz-utils backdoor, CVE-2024-3094, 2024 | Maintainer trust and build reproducibility matter. Know who maintains what you depend on. | [supply chain](../security/supply-chain.md), [dependencies](../security/dependencies.md) |
| Log4Shell, CVE-2021-44228, December 2021 | You cannot fix what you do not know you run. SBOMs turn a hunt of weeks into a query. | [vulnerability management](../security/vulnerability-management.md) |

## Practice

### Foundation

Solo and Startup. Once a year, read this table and pick the two items your customers will ask about first. For most, that is CRA reporting and SBOMs, and an AI use policy.

### Standard

Scale-up and Enterprise. A named owner runs the scan every 6 months with staff and principal engineers, security and legal. Results feed the strategy review. Track the no-regret steps as strategy actions.

### Assured

Regulated and Public sector. Everything in Standard, plus a link from each item to the risk register, legal review of dates and scope, and board-level reporting on items with legal deadlines.

## Cloud, on-premises and air-gapped

Air-gapped and on-premises systems change slowly, so start early. Cryptographic migration needs hardware security modules, firmware and libraries that support the new algorithms, and those purchases take time. Agentic and AI systems inside a classified network need local models and offline evaluation. Sovereignty shifts usually favour on-premises or in-country options: test them before you need them.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Scanning vendor forecasts | Use regulators, standards bodies and your own data. |
| A scan with no owners | Every item gets an owner and a first step. |
| Waiting for final dates | Start no-regret work now. Dates move; inventories are always useful. |
| One big programme for every trend | Run each shift through the strategy as a normal action. |

## Templates

- [Strategy one-pager](../../templates/strategy/strategy-one-pager.md)
- [Risk register](../../templates/strategy/risk-register.csv)
- [Cryptographic inventory](../../templates/docs/crypto-inventory.csv)
- [AI use-case assessment](../../templates/docs/ai-use-case-assessment.md)

## Sources

- NIST post-quantum cryptography: https://csrc.nist.gov/projects/post-quantum-cryptography
- NIST IR 8547 (initial public draft), Transition to Post-Quantum Cryptography Standards: https://csrc.nist.gov/pubs/ir/8547/ipd
- EU AI Act, Regulation (EU) 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Digital Omnibus on AI, Regulation (EU) 2026/1744: https://eur-lex.europa.eu/eli/reg/2026/1744/oj
- EU Data Act, Regulation (EU) 2023/2854: https://eur-lex.europa.eu/eli/reg/2023/2854/oj
- EU Cyber Resilience Act: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- Product Liability Directive (EU) 2024/2853: https://eur-lex.europa.eu/eli/dir/2024/2853/oj
- OWASP Top 10 for LLM Applications: https://genai.owasp.org
- MITRE ATLAS: https://atlas.mitre.org
- NIST SP 800-207: https://csrc.nist.gov/pubs/sp/800/207/final
- CISA Zero Trust Maturity Model: https://www.cisa.gov/zero-trust-maturity-model
- Green Software Foundation, Software Carbon Intensity: https://sci.greensoftware.foundation
- FinOps Foundation framework: https://www.finops.org/framework/
- FOCUS specification: https://focus.finops.org
