# Building with AI

"Our AI pilots demo well and never reach production." Treat a feature built on a large language model (LLM) like any other production system, with one addition: its output is probabilistic, so you must measure quality with evaluations (evals) before launch and keep measuring after. Set a quality bar, a cost budget and a latency budget before you build, design a fallback for when the model fails, and log prompts and outputs with the same care as any personal data. Most pilots stall because nobody defined "good enough" or tested it.

## Outcomes

Starting points. Tune them to your organisation.

- Every AI feature has a written eval set and a pass threshold agreed with the product owner before launch.
- Evals run in CI on every change to prompts, models, retrieval or tools. A drop below the threshold blocks the release.
- Cost per request and p95 latency stay within the budgets set in the design. Alerts fire at 80% of budget.
- 100% of AI features have a tested fallback path and a kill switch.
- Every AI feature is in the AI inventory with an owner and a risk classification (see [AI governance](ai-governance.md)).

## From pilot to production

| Stage | Exit criteria |
|---|---|
| 1. Problem and assessment | A real user problem, a measurable success metric, a [use case assessment](../../templates/docs/ai-use-case-assessment.md) covering data, risk and legal basis. A non-AI baseline considered. |
| 2. Prototype | Works on 20 to 50 hand-picked examples. Rough cost and latency per request known. |
| 3. Eval set and threshold | A labelled set covering normal, edge and adversarial cases: at least 100 to start, 200 to 500 before launch, with a 50 to 200 case gating subset for CI. Sizes are set in [quality engineering](../quality/quality-engineering.md#in-the-ai-era). Pass threshold agreed. |
| 4. Hardening | Fallbacks, guardrails, rate limits, observability, security review against the OWASP Top 10 for LLM Applications (see [AI application security](ai-application-security.md)). |
| 5. Limited release | Behind a feature flag to a small group. Online metrics and user feedback collected. |
| 6. General release | Eval threshold met, budgets met, owner and on-call in place, governance sign-off. |

## Evals

- **Offline evals** run on a fixed, versioned data set: exact-match checks where answers are well defined, rubric scoring where they are not, and safety checks (refusals, leakage, prompt injection).
- **Model-graded evals** (one model scoring another) scale well but drift. Check them against human labels on a sample of at least 50 cases a month per feature.
- **Online evals** after launch: user feedback, task success rate, escalation to a human, and a weekly human review of a random sample of outputs.
- Add every production failure to the eval set. The eval set is the regression test suite for model behaviour.

## Building the eval set from production

The strongest eval sets grow from real use, not only from pre-launch imagination. Some practitioners call this eval-driven development. The term is useful, but the practice works best when the eval set grows from real failures rather than from guesses about what might go wrong.

1. **Start small.** Write 20 to 50 cases by hand covering the happy path, known edge cases and obvious adversarial inputs.
2. **Launch to a small group** behind a feature flag. Collect prompts, outputs and user feedback.
3. **Sample production weekly.** Pull a random sample of inputs and outputs from the previous week's logs. Have a person label each output as correct, partly correct or wrong, with a short reason.
4. **Add every failure.** When a user reports a bad output or the weekly sample finds one, add it to the eval set with the expected answer. The eval set becomes the regression suite for model behaviour.
5. **Grow to launch size.** By the time you reach 200 to 500 labelled cases, you have a set that reflects how real users use the feature, not only how you imagined they would.
6. **Keep growing after launch.** Sample and label monthly. Retire cases that no longer represent current use. Version the set in git so you can compare scores over time.

The eval set is never finished. It grows with the product.

## Prompting, retrieval or fine-tuning

| Approach | Use it when | Cost and risk |
|---|---|---|
| Prompting a general model | The task is general and the model already knows enough | Cheapest to start. Behaviour changes with model versions. |
| Retrieval (RAG) | Answers must come from your documents, current data or sources users can check | Retrieval quality limits answer quality. Access controls must apply to retrieved content. |
| Fine-tuning | You need a consistent format, style or narrow skill, and have thousands of good examples | Training cost, data governance, retraining when the base model changes |
| Small specialised model or classic ML | High volume, narrow task, strict latency or cost | More engineering, much lower run cost |

Start with prompting plus retrieval. Fine-tune only when evals show a gap that the cheaper options cannot close.

## Cost and latency budgets

- Set a cost per request and a monthly budget in the design. Track tokens in and out per request, cache repeated prompts and answers, and route simple requests to smaller models.
- Set a p95 latency target per user flow. Stream responses where users wait. Set timeouts on every model call.
- Limit input size, output size and agent loop iterations. Unbounded consumption is both a cost and a security risk.

## Fallbacks and control

- Every AI feature has a fallback: a smaller or different model, a cached answer, a non-AI path, or a hand-off to a person.
- A kill switch (feature flag) turns the feature off in under 5 minutes without a deployment.
- Pin model versions. Treat a model upgrade as a change: run the evals, roll out gradually, keep the previous version available.
- Validate and encode model output before it reaches a browser, a database, a shell or another system.
- Agents that take actions use least-privilege tools, confirm destructive actions with a person, and log every tool call.

## Observability

- Trace each request across retrieval, model calls and tool calls. The OpenTelemetry semantic conventions for generative AI define common attributes for model, token counts and operations.
- Log prompts, retrieved context and outputs for debugging and evals, with masking of personal data, access controls and a retention period you can justify. These logs often contain the most sensitive data in the system.
- Dashboards per feature: request volume, error rate, latency, tokens and cost, fallback rate, user feedback, eval score trend.

## Practice

### Foundation

- Write down the user problem, success metric, cost and latency budgets. Build a 100-example eval set and run it before every release.
- Use an approved model provider under a business agreement that excludes your data from training.
- A kill switch and a simple fallback.

### Standard

- Evals in CI with a blocking threshold. Online evaluation and weekly human sampling.
- A shared AI gateway (built or bought) that handles authentication, rate limits, model routing, caching, logging and cost allocation.
- Security review against the OWASP Top 10 for LLM Applications and the threats catalogued in MITRE ATLAS, with a [threat model](../../templates/docs/threat-model.md).
- AI features registered in the service catalogue and the AI inventory.

### Assured

- AI risk management aligned with the NIST AI Risk Management Framework (Govern, Map, Measure, Manage) and its Generative AI Profile (NIST AI 600-1), or with an ISO/IEC 42001 management system.
- Eval results, model versions, data sources and approvals kept as records for each release.
- Human oversight designed in and documented for decisions that affect people's rights, money, health or access to services.
- EU AI Act obligations assessed per use case. Transparency duties (Article 50) apply from 2 Aug 2026; high-risk obligations from 2 Dec 2027 (Annex III) or 2 Aug 2028 (regulated products), as set by the 2026 Digital Omnibus on AI. See [AI governance](ai-governance.md) and check EUR-Lex before you plan.

## Cloud, on-premises and air-gapped

- **Public cloud:** hosted model APIs are the fastest start. Check data retention, training use, region and residency terms.
- **Sovereignty:** where law, contract or risk rules out sending data abroad or to a third party, self-host open-weight models on your own GPUs with an inference server such as vLLM. You take on capacity planning, model updates and security of the weights.
- **Air-gapped:** self-hosted only. Transfer model weights, eval sets and libraries through the normal process with checksums and signatures (see [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md)). Run evals inside the enclave before each model change.
- Check the licence of every model's weights before production use. Some open-weight licences restrict commercial use or user numbers.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "It looked good in the demo" | Eval set and pass threshold before launch. |
| Silent model upgrades by the provider | Pin versions. Rerun evals before switching. |
| No budget, then a surprise invoice | Cost per request and monthly budget with alerts. |
| AI where a rule or a search would do | Compare with a non-AI baseline in the assessment. |
| Prompts and outputs logged with personal data, kept forever | Masking, access control and a retention period. |
| Agent with broad credentials | Least-privilege tools, human confirmation for destructive actions. |

## Templates

- [AI use case assessment](../../templates/docs/ai-use-case-assessment.md)
- [Threat model](../../templates/docs/threat-model.md)
- [Production readiness review](../../templates/docs/production-readiness-review.md)

## Sources

- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/
- MITRE ATLAS: https://atlas.mitre.org/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1, Generative AI Profile: https://doi.org/10.6028/NIST.AI.600-1
- ISO/IEC 42001:2023, AI management systems: https://www.iso.org/standard/81230.html
- EU Artificial Intelligence Act, Regulation (EU) 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- OpenTelemetry semantic conventions for generative AI: https://opentelemetry.io/docs/specs/semconv/gen-ai/
