# AI governance

Many organisations have dozens of AI pilots, a few that reach production, and no clear view of which ones touch customers, personal data or decisions about people. Keep one register of AI use cases, classify each by risk, assess the higher-risk ones before production, and give each a named owner who monitors it. Make the process fast for low-risk uses, so teams do not route around it, and rigorous for the few that matter.

## Outcomes

Starting points. Tune them to your organisation.

- 100% of AI systems in production, including bought products with AI features and internal agents, are in the register with an owner and a risk tier.
- Low-risk use cases get a decision within 5 working days. High-risk use cases within 30 working days.
- Every medium- and high-risk system has documented evaluations, a named human oversight role and production monitoring before launch.
- Every staff member who uses or builds AI systems has completed AI literacy training appropriate to their role.
- At least half of pilots reach a clear go or no-go decision within 90 days, instead of running indefinitely.

## The register

Every AI use case gets one entry: purpose, owner, users affected, model and provider, data used, risk tier, status (idea, pilot, production, retired), and review date. Include bought software with AI features and agents that act on internal systems. Use the [AI use-case assessment](../../templates/docs/ai-use-case-assessment.md).

## Risk tiers

The playbook uses four tiers that line up with the EU AI Act categories. Organisations outside the EU can use the same tiers.

| Playbook tier | EU AI Act category | Examples | What is required (starting point) |
|---|---|---|---|
| Not allowed | prohibited practices (Article 5) | social scoring, certain manipulative or exploitative systems | do not build or buy |
| High | high-risk (Article 6 and Annex III, or safety components of regulated products) | hiring and worker management, credit scoring, access to essential public services, education admission | full assessment, risk management, data governance, technical documentation, logging, human oversight, accuracy and security testing, independent review |
| Medium | transparency obligations (Article 50) and internal systems with real impact | customer chatbots, generated content shown to the public, agents that change records | assessment, evaluations, disclosure to users, monitoring, human approval for irreversible actions |
| Low | minimal risk | code assistants, internal summarisation of non-sensitive text, spam filtering | register entry, acceptable use policy, data rules |

EU AI Act dates (check EUR-Lex for the consolidated text before you plan):

| Date | What applies |
|---|---|
| 1 Aug 2024 | Regulation (EU) 2024/1689 enters into force |
| 2 Feb 2025 | Prohibited practices (Article 5) and AI literacy (Article 4) |
| 2 Aug 2025 | Obligations for general-purpose AI models |
| 2 Aug 2026 | Transparency duties in Article 50, such as telling people they are dealing with an AI system. The Omnibus added transition time for marking AI-generated content in systems already on the market; check the final text for the date that applies to you. |
| 2 Dec 2027 | High-risk obligations for stand-alone (Annex III) systems, such as hiring, credit scoring and access to public services |
| 2 Aug 2028 | High-risk obligations for AI in products covered by the EU safety laws in Annex I |

The 2026 Digital Omnibus on AI, in force since 27 Jul 2026, set the high-risk dates above and adjusted some transparency timings. It also changed the AI literacy duty in Article 4; the Commission proposed a softer duty to support AI literacy, so check the wording of Regulation (EU) 2026/1744 before you rely on either version. Keep records of the training you give.

## Lifecycle

| Stage | Gate | Evidence |
|---|---|---|
| Idea | register entry, tier assigned | assessment section 1 |
| Pilot | data use approved, evaluation plan written, pilot end date set (default 90 days) | assessment sections 2 to 4 |
| Production | evaluations meet thresholds, oversight role named, monitoring live, security tested (see [AI application security](ai-application-security.md)) | evaluation report, [production readiness review](../../templates/docs/production-readiness-review.md) |
| Operation | monitoring of quality, drift, cost and incidents; review every 6 to 12 months | dashboards, incident records |
| Retirement | data and model disposal, users informed | decommission record |

## Management frameworks

- **ISO/IEC 42001:2023** sets out an AI management system: policy, roles, risk and impact assessment, life cycle controls, supplier controls and continual improvement. It is certifiable and pairs well with ISO/IEC 27001.
- **NIST AI Risk Management Framework 1.0** (Jan 2023) organises the work into four functions: Govern, Map, Measure and Manage. NIST AI 600-1 (Jul 2024) adds a Generative AI profile.

Pick one as the backbone. Use the other as a checklist. The [control mapping](../compliance/control-mapping.md) links playbook practices to both.

## Roles

| Role | Responsibility |
|---|---|
| Use-case owner | accountable for the system's purpose, risk and performance |
| AI governance lead | runs the register and the assessment process; reports to leadership |
| Independent reviewer | validates high-risk systems before production (model risk, second line or a separate team) |
| Human overseer | can monitor, override or stop the system in operation |
| Data owner | approves use of their data (see [data governance](../data/data-governance.md)) |
| CISO | approves security testing and incident handling for AI systems |

## Practice

### Foundation

Solo and Startup. Write a one-page acceptable use policy: which tools, which data may go into them, and who approves new uses. Keep a simple register. Do not put customer personal data into external AI services without a contract that covers it. See [code assistants](../people/code-assistants.md).

### Standard

Scale-up and Enterprise. The register, risk tiers and lifecycle above. A governance lead with a fixed review rhythm. Evaluations stored with the code. Monitoring for quality, cost and drift. Supplier checks for model providers through [third-party and SaaS risk](../security/third-party-and-saas-risk.md). Guidance for teams in [building with AI](building-with-ai.md).

### Assured

Regulated and Public sector. Everything in Standard, plus independent validation of high-risk systems, fundamental rights impact assessments where the EU AI Act requires them for deployers, model risk management aligned with your regulator's expectations, public transparency for AI used in decisions about citizens, and records kept for the required period.

## Cloud, on-premises and air-gapped

Many organisations cannot send data to hosted model APIs. Self-hosted open-weight models let you keep data in place, but you take on serving, patching, evaluation and capacity. Record model weights and their source in the SBOM as you would any dependency, and verify their integrity before import into an air-gapped network. Run evaluations inside the network on representative data.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Pilots with no end date | Set a 90-day pilot gate in the register. |
| Same heavy review for every use | Tier the process; low-risk uses get a quick path. |
| Banning all AI tools | Staff will use unapproved tools. Provide approved ones with data rules. |
| Governance that never sees production | Monitoring and periodic review are part of the gate. |
| Ignoring AI features in bought software | Include them in the register and supplier reviews. |

## Templates

- [AI use-case assessment](../../templates/docs/ai-use-case-assessment.md)
- [Code assistant policy](../../templates/docs/code-assistant-policy.md)
- [Data classification](../../templates/docs/data-classification.md)

## Sources

- EU AI Act, Regulation (EU) 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- ISO/IEC 42001:2023: https://www.iso.org/standard/81230.html
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1, Generative AI Profile: https://doi.org/10.6028/NIST.AI.600-1
- OWASP Top 10 for LLM Applications: https://genai.owasp.org
- MITRE ATLAS: https://atlas.mitre.org
