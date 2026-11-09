# AI architecture patterns

"Every team calls the model provider directly, with its own keys, prompts and retry logic. We cannot see the cost, swap a model or say where the data went." Start with the simplest pattern that meets the need: one model call that returns structured output. Add retrieval when answers must come from your own data, tools and agents only when the task really needs several steps, and a shared gateway as soon as a second team uses models. Each extra layer adds latency, cost and attack surface, so each one must earn its place with an evaluation result.

## Outcomes

Starting points. Tune them to your organisation.

- 100% of model traffic in production passes through a gateway that logs, limits and attributes cost.
- Every AI feature has a written cost budget and p95 latency budget per request, and alerts at 80% of each.
- Every AI feature can fail over to a second model or a non-AI path, tested at least once a quarter.
- Retrieval never returns a document the requesting user is not allowed to read: zero findings in tests and audits.
- Every agent has a written limit on steps, run time and spend, and a list of tools it may call.

## Choosing a pattern

| Pattern | Use it when | Do not use it when |
|---|---|---|
| Direct call with structured output | Classify, extract, summarise or draft from input you already have | The answer needs facts the model does not have |
| Retrieval-augmented generation (RAG) | Answers must come from your documents or current data, with sources users can check | A database query or keyword search answers the question |
| Workflow with model steps | The steps are known in advance and the model fills in parts | You cannot write the steps down at all |
| Tool-using agent | The steps depend on what the agent finds, and tools are safe to retry | The task moves money or changes records without a person approving |
| Multi-agent workflow | Subtasks are independent and can be evaluated separately | One agent with good tools would do; more agents means more cost and harder debugging |

## Reference patterns

### Direct call with structured output

Send one request, ask for a fixed schema (typed fields, an enum of allowed values), and validate the result in code before anything uses it. Retry once on a schema failure, then fall back. This pattern covers more use cases than teams expect, and it is the easiest to evaluate, cache and secure.

### Retrieval-augmented generation

- **Chunking.** Split documents on their structure (headings, sections, table rows), not on a fixed character count. Keep the title and source with each chunk.
- **Hybrid search.** Combine keyword search with vector search, then rerank. Keyword search finds exact terms such as product codes and names that embeddings miss.
- **Freshness.** Give each index build an ID that names its data snapshot and embedding model. Update it incrementally, and propagate deletions within a set time (starting point: 24 hours), so erased personal data stops appearing in answers.
- **Access control at retrieval time.** Filter by the requesting user's permissions in the query itself, not after generation. Use a separate index per tenant where data must never mix. See [AI application security](ai-application-security.md).
- **Evaluate retrieval on its own.** Measure whether the right documents appear in the top results before measuring answer quality. Poor retrieval cannot be fixed by a better prompt.

### Tool-using agents and multi-agent workflows

- **Prefer a workflow to a free agent.** Code decides the order of steps; the model fills in the parts that need judgement. It is cheaper, faster and easier to test.
- **Bounded autonomy.** Set a maximum number of steps, run time and spend per task. Stop and hand over to a person when a limit is reached.
- **Approval steps.** Actions that are irreversible, external or above a value threshold wait for a person, who sees the exact action and parameters.
- **Idempotent tools.** Each write tool accepts an idempotency key, so a retry or a repeated plan does not send two payments or two emails.
- **Least privilege per tool.** Read-only by default, scoped credentials, and the end user's permissions checked in code.

### Model gateway

One service between your applications and every model, hosted or self-hosted. Build it or buy it, but have only one.

| Function | What it does |
|---|---|
| Routing | Sends each request to the right model by task, cost and data class |
| Quotas | Rate limits and spend caps per user, team, tenant and feature |
| Logging | Records model, version, tokens, latency, cost and trace ID |
| Redaction | Masks personal data and secrets before requests leave your network |
| Fallback | Retries on another provider or a self-hosted model when the first fails or is too slow |
| Data rules | Blocks a data class from going to a model not approved for it |

Keep business logic and prompts out of the gateway. It is plumbing, owned by a platform team. See [developer platform](../platform/developer-platform.md).

### Caching

- **Exact cache:** key on model version, prompt version, parameters and input. Safe and cheap.
- **Semantic cache:** returns a stored answer for a similar question. Use it only for questions with one correct answer (help-centre questions, for example), within one tenant and one permission scope, with a tested similarity threshold.
- **Invalidate** every cached entry when the model, prompt or index version changes, and set a time-to-live.

### Batch or real-time

| Choose | When | Benefit |
|---|---|---|
| Real-time | A person is waiting for the answer | Stream the response; set timeouts |
| Batch | Nightly classification, enrichment, evaluation runs, back-filling an index | Lower cost where providers offer batch pricing, no latency pressure, easier retries |

### Evaluation and guardrail layers

Put checks around the model, not only inside the prompt: input checks (size, injection classifiers, data class), output checks (schema, policy, secret patterns, grounding in the retrieved sources), offline evaluation sets in CI and online sampling in production. Guardrails are a second layer. Permissions and approval steps are the control.

### Open protocols for tools, such as MCP

The Model Context Protocol (MCP) is an open protocol for connecting models and agents to tools and data through servers. It saves each team writing its own integrations, and it widens what an agent can reach.

- Treat every MCP server as third-party code with privileges. Keep an allow-list, pin versions and review updates.
- Tool descriptions are read by the model, so a malicious or changed description can steer it. Review them like code.
- Give each server its own scoped, short-lived credentials. A local server runs with the privileges of the user who started it.
- Do not let one agent combine untrusted input, access to sensitive data and a way to send data out. Remove at least one of the three.

### Self-hosted and on-premises models

Run open-weight models on your own hardware when data cannot leave, the network is air-gapped, or steady high volume makes per-call pricing expensive. Use an inference server (vLLM is one example), a model registry with checksums and licences, and capacity plans for GPUs. Smaller or quantised models cut cost and latency at some loss of quality: measure the loss with your evaluation set, not a public benchmark.

### Cost and latency budgets per request

Set the budget in the design and split it across the steps. Example starting points for an interactive feature:

| Step | Latency share | Watch |
|---|---|---|
| Retrieval and reranking | Up to 20% | Index size, number of results reranked |
| Model call | Up to 60% | Input and output tokens, model size |
| Tools and guardrails | Up to 20% | Number of tool calls, extra model calls for checks |

Stream the first tokens where a person waits. Derive the cost budget from the value of one outcome, so an expensive model is used only where it pays.

## When to change your architecture

| Trigger | Change |
|---|---|
| A second team or feature starts calling models | Add the gateway |
| Evaluations fail because the model lacks your facts | Add retrieval |
| A fixed workflow needs too many special cases | Allow an agent to choose steps, within limits |
| Cost per outcome exceeds the budget at real volume | Route to smaller models, add caching, move work to batch |
| Data class or law forbids sending data to a provider | Self-host for that workload |
| One provider outage stops a critical feature | Fallback to a second provider or a self-hosted model |

Change one layer at a time, behind a feature flag, and compare evaluation scores, cost and latency with the previous version before going further. The path most teams follow is: direct call, then gateway, then retrieval, then workflows with tools, then bounded agents, with self-hosting added per workload. See [scaling](../architecture/scaling.md) for the same principle in general systems.

## Practice

### Foundation

- Direct calls with structured output and validation. Timeouts, a fallback and a kill switch on every feature.
- A cost budget and a latency budget written in the design.

### Standard

- One gateway for all model traffic. Retrieval with permission filters at query time.
- Agents limited by steps, time and spend, with approval steps and idempotent tools.
- Traces across retrieval, model and tool calls (see [observability](../architecture/observability.md)). Fallback tested quarterly.

### Assured

- Architecture decisions for each AI feature recorded as [decision records](../architecture/decision-records.md), including data flows and model locations.
- Gateway logs kept as evidence of which data class went to which model. Independent review of agent permissions before launch.
- Self-hosted models for data that may not leave your boundary, with weights in the SBOM.

## Cloud, on-premises and air-gapped

Every pattern on this page works without the public internet if the model, index, gateway and evaluation sets run inside the network. Air-gapped teams import model weights and embedding models through the approved transfer process, with signatures and checksums, and run evaluations inside the enclave before each change. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md) and [building with AI](building-with-ai.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| An agent where a fixed workflow would do | Write the steps in code; use the model for judgement only |
| Permission filtering after generation | Filter at retrieval time |
| Semantic cache shared across tenants | Scope caches per tenant and permission set |
| Each team with its own provider keys | One gateway, one set of keys, cost per team |
| Any MCP server an engineer finds | Allow-list, pinned versions, reviewed tool descriptions |

## Templates

- [Decision record](../../templates/docs/adr.md)
- [Threat model](../../templates/docs/threat-model.md)
- [AI use case assessment](../../templates/docs/ai-use-case-assessment.md)

## Sources

- Model Context Protocol specification: https://modelcontextprotocol.io/
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/
- OpenTelemetry semantic conventions for generative AI: https://opentelemetry.io/docs/specs/semconv/gen-ai/
- NIST AI 600-1, Generative AI Profile: https://doi.org/10.6028/NIST.AI.600-1
- vLLM documentation: https://docs.vllm.ai/
