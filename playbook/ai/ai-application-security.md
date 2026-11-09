# AI application security

Treat every input to a language model as untrusted, every output as untrusted, and every tool an AI agent can call as a privilege that needs least-privilege scoping, logging and, for anything irreversible, a human approval. Organisations are wiring models into support desks, internal search and code pipelines faster than they are securing them, and the main attack, prompt injection, has no complete fix inside the model. The defences that work sit outside the model: in permissions, in output handling, in approval steps and in monitoring.

## Outcomes

Starting points. Tune them to your use cases.

- 100% of AI features in production have a threat model covering the OWASP Top 10 for LLM Applications 2025 (see the [threat model template](../../templates/docs/threat-model.md)).
- 100% of AI agents run under their own non-human identity with scoped, short-lived credentials; zero agents use a person's credentials.
- 100% of agent actions that move money, delete data, send messages outside the organisation or change production need human approval.
- Every AI feature has an evaluation suite, including adversarial prompts, that runs in CI before each model, prompt or tool change.
- Prompts, model outputs, tool calls and approvals are logged with trace IDs and kept for at least 90 days (starting point).
- Every AI feature has a spending cap and rate limits per user and per tenant.

## The OWASP Top 10 for LLM Applications 2025, with a control for each

| Risk | What goes wrong | Control that does not rely on the model behaving |
|---|---|---|
| LLM01 Prompt Injection | Instructions hidden in user input, documents, web pages or emails change what the model does | Least-privilege tools; treat retrieved content as data; human approval for high-impact actions; isolate untrusted content from privileged agents (see below) |
| LLM02 Sensitive Information Disclosure | Model reveals personal data, secrets or other users' data | Retrieve only documents the requesting user may read (enforce permissions at retrieval); never put secrets in prompts; mask personal data in inputs and logs; output filters for known secret patterns |
| LLM03 Supply Chain | Compromised models, adapters, datasets or libraries | Pin model versions and hashes; use models from trusted sources; scan model files (prefer safe formats such as safetensors over pickle); SBOM for AI components (see [supply chain](../security/supply-chain.md)) |
| LLM04 Data and Model Poisoning | Training, fine-tuning or retrieval data is manipulated | Provenance and access control on training and RAG sources; review before content enters an index; evaluate after every data change |
| LLM05 Improper Output Handling | Model output is executed or rendered: SQL, shell, HTML, file paths | Treat output as user input: validate against a schema, encode for the context, parameterise queries, never pass to `eval` or a shell; sandbox any code execution |
| LLM06 Excessive Agency | Agent has more tools, permissions or autonomy than the task needs | Smallest tool set per task; read-only by default; scoped credentials; human approval for irreversible actions; rate limits per tool |
| LLM07 System Prompt Leakage | Instructions, internal logic or credentials in the system prompt are exposed | Assume the system prompt is public. Keep secrets and authorisation logic out of it; enforce rules in code |
| LLM08 Vector and Embedding Weaknesses | Retrieval leaks data across users or tenants, or returns poisoned content | Per-tenant indexes or enforced metadata filters; permission checks at query time; validate and attribute sources before indexing |
| LLM09 Misinformation | Model states false things confidently; users act on them | Ground answers in cited sources; show the sources; evaluate factual accuracy; human review for legal, medical, financial or safety outputs |
| LLM10 Unbounded Consumption | Abuse drives cost or denial of service; model extraction by bulk queries | Per-user and per-tenant rate limits, token limits and spending caps; timeouts; alerts on cost anomalies |

OWASP also publishes a separate Top 10 for Agentic Applications (for 2026). MITRE ATLAS catalogues real attack techniques against AI systems; use it in threat modelling and red teaming.

## Prompt injection: design so the model cannot do much harm

No prompt wording, filter or classifier reliably stops prompt injection. Design as if injection will succeed sometimes.

1. **Separate privilege from untrusted content.** An agent that reads untrusted content (email, web pages, uploaded files, tickets from customers) should not also hold powerful tools. Split the work: a quarantined step that reads and summarises without tools, and a privileged step that acts only on structured, validated output.
2. **Constrain outputs to structure.** Ask the model for a fixed schema (an enum of actions, typed fields), and validate it in code before anything acts on it.
3. **Authorise in code, not in the prompt.** The application checks whether the end user may perform the action, using the user's identity, not the agent's.
4. **Limit where data can go.** Block or allow-list outbound URLs, email recipients and file destinations, so injected instructions cannot send data out (for example by asking the model to render an image URL with data in the query string).
5. **Human approval** for actions that are irreversible, external or above a value threshold. Show the approver the exact action and parameters, not the model's summary.
6. **Filters are a second layer.** Input and output classifiers catch common attacks and reduce noise. They are not the control.

## Practice

### Foundation

1. **Inventory** every AI feature and agent: model, provider, data it sees, tools it can call, owner.
2. **No secrets in prompts** and no production credentials given to agents.
3. **Read-only first.** Start agents with read-only tools. Add write tools one at a time with approval.
4. **Treat output as untrusted** wherever it is rendered, stored or executed.
5. **Spending caps** and rate limits at the provider and in your gateway.
6. **Data rules.** Check what the provider does with your inputs (retention, training) and match it to your data classification (see [data security and privacy](../data/data-security-and-privacy.md)).

### Standard

1. **Non-human identities for agents.** Each agent has its own identity, owner and scoped, short-lived credentials (see [access control](../security/access-control.md) and [secrets](../security/secrets.md)). When an agent acts for a user, it carries the user's authorisation too, and the narrower of the two applies.
2. **Tool gateway.** All tool calls pass through a gateway that checks policy, applies rate limits, records the call and enforces approval rules. Tools are versioned and reviewed like APIs, including tools exposed through protocols such as the Model Context Protocol.
3. **Evaluations in CI.** A test set of normal tasks, edge cases and known attacks (injection, data leakage, jailbreaks) runs on every change to the model version, prompt, retrieval set or tools. Block the release on regression.
4. **Red teaming** before launch and every 6 months for customer-facing features, using OWASP and MITRE ATLAS techniques.
5. **Logging and tracing.** Log prompts, retrieved document IDs, outputs, tool calls, approvals and costs, linked by a trace ID, with personal data masked. Alert on unusual tool use and cost spikes (see [observability](../architecture/observability.md)).
6. **Kill switch.** A feature flag disables each AI feature or tool in under 5 minutes (see [rollbacks](../reliability/rollbacks.md)).

### Assured

Everything in Standard, plus:

1. **Risk management framework.** Run AI risk management under ISO/IEC 42001 or the NIST AI Risk Management Framework (Govern, Map, Measure, Manage), using NIST AI 600-1 for generative AI risks. See [AI governance](ai-governance.md).
2. **EU AI Act.** High-risk systems must meet requirements for accuracy, robustness and cybersecurity, logging and human oversight. Timelines changed in 2026; check EUR-Lex for current dates (see [AI governance](ai-governance.md)).
3. **Independent testing** of high-impact agents before launch and after major changes.
4. **Evidence.** Threat models, evaluation results, red team reports, approval logs and incident records kept for the audit period.

## Cloud, on-premises and air-gapped

- **Self-hosted models** remove the data transfer to a provider but add model supply chain work: verify hashes of model files on import, scan them, and pin versions.
- **Air-gapped:** evaluations, red team prompt sets and model updates move through the approved transfer process. Log and alert inside the network; the controls on this page do not need the internet.
- **Hosted APIs:** route all calls through your own gateway for logging, limits and data rules, rather than letting each team call the provider directly.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "The system prompt tells it not to do that" | Enforce in code and permissions. Assume the prompt can be overridden. |
| Agent runs with a developer's personal token | Own identity, scoped and short-lived. |
| Agent reads customer emails and can send payments | Split untrusted reading from privileged acting; approval for payments. |
| Model output inserted into HTML or SQL | Encode, validate, parameterise. |
| RAG index shared across tenants with no filters | Per-tenant index or enforced permission filters at query time. |
| No evaluations; changes tested by trying a few prompts | Evaluation suite in CI, including attacks. |

## Templates

- [Threat model](../../templates/docs/threat-model.md)
- [AI use case assessment](../../templates/docs/ai-use-case-assessment.md)
- [Code assistant policy](../../templates/docs/code-assistant-policy.md)

## Sources

- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/resource/owasp-top-10-for-llm-applications-2025/
- OWASP Top 10 for Agentic Applications for 2026: https://genai.owasp.org/resource/owasp-top-10-for-agentic-applications-for-2026/
- MITRE ATLAS: https://atlas.mitre.org/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- NIST AI 600-1, *Generative Artificial Intelligence Profile*: https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.600-1.pdf
- ISO/IEC 42001:2023: https://www.iso.org/standard/42001
- Regulation (EU) 2024/1689 (AI Act): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
