# Code assistants

Allow code assistants under a short written policy: security owns the list of approved tools, data classification decides what code and data may be sent to which tool, and the engineer who opens a change owns every line of it. The review bar does not change because a tool wrote the first draft. Measure the effect on delivery and stability honestly, because faster output does not by itself mean better outcomes.

## Outcomes

Starting points. Tune them to your organisation.

- 100% of assistant use goes through tools on the approved list. Unapproved tools are blocked at the network or identity layer where you can.
- Zero incidents of Restricted data or secrets sent to a tool not approved for that class.
- Change fail rate and rework rate (see [metrics](../measurement/metrics.md)) do not rise after adoption. If they do, act before expanding use.
- Every engineer completes the policy training (30 minutes) before getting access.
- The approved list and policy are reviewed at least every 6 months.

## The policy in seven rules

1. **Approved tools only.** Security owns the list, with input from legal, procurement and engineering. Personal accounts on consumer tools are not allowed for work code.
2. **Classification decides where code may go.** See the table below.
3. **You own every line.** The author can explain, test and support every line they submit, however it was produced. "The assistant wrote it" is not an answer in review or in a postmortem.
4. **The review bar is unchanged.** Same tests, same reviewers, same size limits, same security checks.
5. **No secrets or personal data in prompts.** Do not paste credentials, production data or customer records. Exclude secret files from the tool's context.
6. **Check what you add.** Verify every suggested dependency exists, is the intended package and is approved. Check licences on large generated blocks.
7. **Agents act with least privilege.** Tools that run commands or open pull requests run in a sandbox, with scoped tokens, no production credentials and a human approving every push to a shared branch.

## Data classification

Use your organisation's classification scheme. If you have none, start with the four classes below and adapt.

| Class | Examples | Assistants allowed |
|---|---|---|
| Public | Open source code, published docs | Any tool on the approved list |
| Internal | Most application code, internal docs | Approved tools under an enterprise agreement that excludes your data from model training and limits retention |
| Confidential | Security-sensitive code (authentication, cryptography, fraud rules), unreleased product code, customer configuration | Approved enterprise tools with contractual data residency and zero or minimal retention, or self-hosted models |
| Restricted | Secrets, personal data, production data, code on air-gapped networks. Government classified information follows its national scheme | Self-hosted models inside the same security boundary, or no assistant |

Self-hosted options mean open-weight models served on your own hardware with an inference server such as vLLM. They cost GPU capacity and operations effort, and model quality varies. Treat model weights as third-party software: check the licence, verify checksums, record the version and assess them before use.

## Choosing tools

Security assesses each tool before it goes on the list and records the answers.

| Question | Why it matters |
|---|---|
| Is our code or prompt data used to train models? Can we opt out by contract? | Training can expose your code to other users |
| How long are prompts and outputs retained, and where? | Retention and residency rules under data protection law |
| Does it support SSO, central administration and audit logs? | Joiners, leavers and evidence |
| Can we exclude files and repositories from its context? | Keeps secrets and sensitive code out |
| Does it filter suggestions that match public code, and what does the vendor's contract say about intellectual property claims? | Licence exposure |
| Can agents be restricted to a sandbox and limited permissions? | Limits damage from mistakes and prompt injection |

## Risks to manage

- **Licence and provenance.** Generated code can reproduce licensed code. Turn on public-code matching filters where offered and keep licence scanning in CI (see [dependencies](../security/dependencies.md)). Copyright in generated material is unsettled and varies by country. The US Copyright Office concluded in 2025 that material generated without sufficient human control over its expressive elements is not protected by copyright. Ask counsel what this means for your products.
- **Secret leakage.** Assistants read open files and sometimes whole workspaces, including `.env` files. Use the tool's exclusion settings, keep secrets out of repositories (see [secrets](../security/secrets.md)) and keep secret scanning with push protection on.
- **Invented dependencies.** Assistants sometimes suggest packages that do not exist. Attackers register such names. Install dependencies only from your proxy or mirror, and only approved ones.
- **Prompt injection.** Content the assistant reads (issues, web pages, comments, dependency files) can carry instructions. This is the top risk in the OWASP Top 10 for LLM Applications. Do not give agents credentials they do not need, and review what they did, not only what they say they did.
- **Insecure patterns.** Generated code repeats common mistakes: missing authorisation checks, string-built SQL, weak cryptography. Static analysis and security review stay mandatory.
- **Skill erosion.** People still need to understand the system. Keep design reviews, pairing and on-call learning, especially for new engineers.

This page covers assistants that help engineers write code. For AI features inside your products, see [building with AI](../ai/building-with-ai.md).

## Measuring impact honestly

The 2025 DORA report, "State of AI-assisted Software Development", found that AI adoption is associated with higher software delivery throughput and also with increased delivery instability. Read the report itself before drawing conclusions for your teams.

- Track the five DORA metrics for teams before and after adoption, against each team's own baseline. Pay most attention to change fail rate and rework rate.
- Watch review load: pull request size, review time, and the number of review rounds. Larger, faster drafts can move the bottleneck to reviewers.
- Ask engineers, with a short survey every quarter, where the tools help and where they cost time.
- Do not use suggestion acceptance rates, "share of code generated" or lines of code as success measures. They count activity, not outcomes.
- Never track individuals' assistant use for performance ratings.

**What to measure.** Track these at team level against the team's own pre-adoption baseline.

| Metric | What it tells you |
|---|---|
| Cost per merged change | Total cost of the tool licence, model API calls and human review time, divided by merged pull requests. Compare to the pre-adoption cost of the same work. |
| Time from spec to merged pull request | End-to-end cycle time. A tool that speeds drafting but slows review may not improve it. |
| Rework rate | Share of deployments that are unplanned fixes for production problems (the fifth DORA metric). A rise means quality is falling faster than speed is rising. |
| Change fail rate | Share of deployments causing a failure in production. Track alongside rework rate. |
| Developer satisfaction | A short quarterly survey with the same questions each time. Ask where the tool helps and where it costs time. |
| Review wait time | Time from review request to first response. If it rises as output rises, review is the bottleneck. See [code review](../delivery/code-review.md#tiered-review-for-high-volume-agent-output). |

## Practice

### Foundation

- Write a one-page policy from the [code assistant policy template](../../templates/docs/code-assistant-policy.md). Pick one approved tool under a business agreement.
- Keep secret scanning, CI tests and code review exactly as they were.

### Standard

- Security owns the approved list and reviews it every 6 months. Access through SSO, revoked automatically on leaving.
- Classification rules enforced through repository-level exclusions and separate tool configurations for sensitive repositories.
- Agentic tools run only in sandboxed environments with scoped, short-lived tokens.
- Quarterly review of DORA metrics and survey results for teams using assistants.

### Assured

- Record assistant use per pull request (a checkbox in the pull request template) where your regulator or customer requires traceability.
- Tool assessments, contracts and data protection impact assessments are kept as evidence. The NIST SSDF community profile for generative AI (SP 800-218A) gives practices to map against.
- Restricted and classified work uses self-hosted models inside the security boundary, or none.
- Model and tool versions are recorded, so behaviour can be traced if a defect pattern appears.

## Cloud, on-premises and air-gapped

- Public cloud teams can use SaaS tools within the classification rules above.
- On-premises teams with data residency rules need a vendor region that meets them, or self-hosting.
- Air-gapped networks cannot reach SaaS tools. Use a self-hosted model inside the enclave, transferred as update media with verified checksums (see [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md)), or work without an assistant.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Banning all tools, so people use personal accounts in secret | Approve a safe option quickly and block the rest. |
| Approving tools without reading the data terms | Security assessment with recorded answers before approval. |
| Large generated pull requests waved through | Same size limits and review standard as any change. |
| Measuring success by percentage of code generated | DORA metrics, review load and developer surveys. |
| Agents with production credentials | Sandboxes, scoped tokens, human approval for pushes. |

## Templates

- [Code assistant policy](../../templates/docs/code-assistant-policy.md)
- [Pull request template](../../templates/github/PULL_REQUEST_TEMPLATE.md)

## Sources

- DORA research, including the 2025 report "State of AI-assisted Software Development": https://dora.dev/research/
- NIST SP 800-218A, Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: https://csrc.nist.gov/pubs/sp/800/218/a/final
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/
- US Copyright Office, Copyright and Artificial Intelligence: https://www.copyright.gov/ai/
