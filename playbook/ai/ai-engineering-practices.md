# AI engineering practices

"We gave every engineer a code assistant and some teams now run coding agents. Output went up. So did review queues, rework and the cloud bill." Treat AI as a change to every stage of the software lifecycle, not a faster keyboard. Write specs that a person or an agent can follow, run agents with least privilege in a sandbox and without merge rights, keep human review and tests as the gate, version prompts, models and retrieval indexes like code, and judge the result by rework rate and change fail rate, not by how much code was produced.

This page covers how teams build software when AI takes part in the work, and how they ship AI features. The usage policy for assistants is in [code assistants](../people/code-assistants.md). Taking one AI feature from pilot to production is in [building with AI](building-with-ai.md). Attacks and defences are in [AI application security](ai-application-security.md).

## Outcomes

Starting points. Tune them to your organisation.

- Change fail rate and rework rate stay at or below each team's pre-adoption baseline for 2 consecutive quarters.
- Time to first review stays under 1 working day at the 90th percentile, as set in [code review](../delivery/code-review.md).
- Zero agent identities hold merge, admin or ruleset bypass permissions.
- 100% of changes to prompts, model versions, retrieval indexes and tool definitions pass an evaluation gate before release.
- Every repository where agents work has an agent instructions file reviewed in the last 6 months.
- AI spend per team and per feature is visible monthly, with alerts at 80% of budget.

## How the lifecycle changes

| Stage | What changes | Practice |
|---|---|---|
| Plan | Code is cheap, so a vague ticket produces a lot of wrong code quickly | Write specs with acceptance examples before work starts |
| Build | Agents can edit many files and run commands | Sandbox, scoped tokens, repository instructions |
| Review | Volume rises; generated code reads fluently even when wrong | Size limits, spec-first review, planned review capacity |
| Test | Assistants write tests that mirror the code, not the requirement | Tests from the spec; check each test fails without the change |
| CI/CD | Behaviour can change with no code change | Evaluation gates; prompts, models and indexes as release artifacts |
| Operate | Model calls add cost, latency and a new failure mode | Tracing, budgets, kill switches |
| On-call | Assistants can read logs and suggest fixes | Read-only first; a person approves every action |

## Specs that people and agents can follow

A good spec is the cheapest control you have. It tells the agent what to build and tells the reviewer what to check.

- **Problem and outcome.** One paragraph: who has the problem and what changes for them.
- **Acceptance examples.** Concrete inputs and expected results, written so they can become tests.
- **Constraints and non-goals.** Security rules, performance budget, files or modules that must not change.
- **Size.** One spec, one pull request, under about 400 changed lines. Split bigger work.
- **Where it lives.** In the tracker or the repository, linked from the pull request.

## Repository instructions for coding agents

Several coding agents read a Markdown file at the repository root, commonly named `AGENTS.md`, for project-specific instructions. Keep one in every repository where agents work.

```markdown
# AGENTS.md
## Build and test
- make setup; make test; make lint  (all must pass before a pull request)
## Layout
- src/api: HTTP handlers. src/domain: business rules, no I/O.
## Conventions
- Follow docs/adr. Reuse src/common before adding a helper.
- New dependencies need approval: open an issue first.
## Never
- Edit migrations already applied, CI workflows or CODEOWNERS.
- Add secrets, real customer data or production URLs.
```

- Keep it short (under about 150 lines) and specific. Add nested files for large subdirectories.
- Put it under [CODEOWNERS](../../templates/github/CODEOWNERS). A change to agent instructions is a change to how code gets written.
- Never put secrets in it. Assume anyone with read access, and any agent, sees it.

## Coding agents in the repository

| Control | Starting point |
|---|---|
| Identity | Each agent runs as its own bot or app identity with a named human owner, never a person's token |
| Token scope | Short-lived, one repository, `contents: write` and `pull-requests: write` at most |
| Merge rights | None. Rulesets require a human approval, and the agent is never a bypass actor. See [source control](../delivery/source-control.md). |
| Execution | A disposable container or VM, no route to production, outbound traffic limited to the git host and the package mirror |
| Secrets | None in the sandbox. Test credentials only. |
| Dependencies | Installed only from your internal mirror or proxy |
| Limits | Maximum run time, steps and spend per task |
| Audit | Every command and tool call logged with the task ID, kept at least 90 days |

The person who starts an agent is the author of its pull request. Issue text, comments and file contents can carry prompt injection, so an agent that reads untrusted input never holds a token that can merge, release or read secrets. See [continuous integration](../delivery/continuous-integration.md#in-the-ai-era).

## Review, tests and evaluation

- **Review the spec match first, then the tests, then the code.** If the tests do not prove the acceptance examples, stop there. Full rules are in [code review](../delivery/code-review.md#in-the-ai-era).
- **Tests for code, evaluations for model behaviour.** Deterministic code gets ordinary tests. Features built on a model get an evaluation set with thresholds. See [quality engineering](../quality/quality-engineering.md#in-the-ai-era).
- **Check generated tests.** Each new test must fail without the change and assert the requirement, not whatever the code happens to return.

## Versioning and release

| Artifact | Version it as | Gate |
|---|---|---|
| Prompt and system instructions | Files in the repository | Evaluation set in CI |
| Model | Exact version identifier, never a moving alias | Full evaluation run, then canary |
| Retrieval index | Build ID naming the source data snapshot and embedding model | Retrieval evaluation, then canary |
| Tool definitions | Versioned like an API | Contract tests and evaluation |
| Guardrail configuration | Files in the repository | Safety cases in the evaluation set |
| Agent instructions file | Files in the repository | Code owner review |

Release them through the pipeline, canary them and keep the previous version loadable. See [release management](../delivery/release-management.md#in-the-ai-era) and [rollbacks](../reliability/rollbacks.md).

## Observability and cost

- **Trace every model call** with model and version, tokens in and out, latency, cost, cache hit and the trace ID of the request. OpenTelemetry has semantic conventions for generative AI. They are still evolving, so pin the version you emit. See [observability](../architecture/observability.md).
- **Mask personal data** in prompts and outputs before they reach logs, and set a retention period.
- **Budgets per team and per feature**, enforced at a gateway. Route simple work to smaller models, cache repeated calls and cap agent loops.
- **Review cost per outcome monthly:** cost per merged change, per resolved case, per answered query.

## Runbooks and on-call with AI assistants

1. **Read-only first.** The assistant summarises alerts, searches logs and drafts the incident timeline. It holds read-only credentials.
2. **Propose, do not act.** It suggests the runbook step or command. The on-call engineer checks it and runs it.
3. **Automate only pre-approved, reversible steps** (restart, scale out, toggle a kill switch), with every action logged and the incident commander informed.

The incident commander is always a person. See [incident management](../reliability/incident-management.md) and the [runbook template](../../templates/docs/runbook.md).

## Practice

### Foundation

- One approved assistant under the [code assistant policy](../../templates/docs/code-assistant-policy.md). Review, tests and size limits unchanged.
- An `AGENTS.md` in each active repository. Specs with acceptance examples for anything over a day's work.
- Record DORA metrics before adoption, so you have a baseline.

### Standard

- Agents run in sandboxes with their own identities, scoped tokens and no merge rights, enforced by rulesets.
- Evaluation gates in CI for every AI feature. Prompts, models and indexes versioned and released through the pipeline.
- Model calls traced; spend reported per team and feature through a shared gateway.
- Review capacity planned explicitly each cycle. Quarterly review of rework rate, change fail rate and review load.

### Assured

- Pull requests record whether generated code is included and what the author verified, where regulators or customers require traceability.
- Evaluation results, model versions, prompt versions and approvals kept per release as evidence. Map practices to NIST SP 800-218A.
- Agent action logs retained for the audit period. Agents on regulated systems limited to proposing changes.

## Challenges and how to overcome them

| Challenge | Practice that works | Metric to watch |
|---|---|---|
| Review overload | Pull requests under 400 lines, spec-first review, review time planned in capacity, review bots as a first pass only | Time to first review, open pull requests per reviewer |
| Rising rework and change fail rate | Slow generation down before adding more; tighter specs and tests; canary releases | Rework rate, change fail rate against baseline |
| Skill erosion in juniors | Juniors explain every change in review, pair with seniors, practise debugging without an assistant, join on-call as shadows | Skills matrix coverage, time for a junior to resolve an incident unaided |
| Inconsistent style and duplication | Conventions in `AGENTS.md`, shared libraries named there, linters and formatters in CI | Duplicate-code findings, new helpers added that already exist |
| Secrets, injected dependencies and invented packages (sometimes called slopsquatting) | Secret scanning with push protection, installs only from your mirror, new dependencies approved by a person | Secret scanning alerts, unapproved dependency attempts blocked |
| Licence and IP uncertainty | Public-code matching filters on, licence scanning in CI, legal advice on generated material | Licence scan findings per quarter |
| Cost growth | Budgets at the gateway, model routing, caching, loop limits | Cost per outcome, spend against budget |
| Vendor lock-in | Calls through a gateway with a provider-neutral interface; prompts and evaluations kept in your repository; a tested second model | Time to switch provider in a drill |
| Evaluations that do not reflect real use | Build evaluation sets from production samples and incidents; human review of a weekly sample | Agreement between offline scores and user feedback |

## Cloud, on-premises and air-gapped

- **Cloud:** hosted assistants and model APIs within your data classification rules, called through your own gateway.
- **On-premises:** self-hosted open-weight models behind the same gateway, so teams use one interface wherever the model runs.
- **Air-gapped:** agents, models, evaluation sets and package mirrors all inside the enclave. Model weights move through the approved transfer process with checksums. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Agent opens pull requests with a senior engineer's personal token | Own identity, scoped short-lived token, no merge rights |
| "The agent said the tests pass" | CI is the only source of truth for tests |
| Prompt edited in a provider console | Prompts live in the repository and ship through the pipeline |
| Model alias such as "latest" in production | Pin exact versions; upgrades go through evaluation and canary |
| Success measured as share of code generated | Rework rate, change fail rate and cost per outcome |

## Templates

- [Code assistant policy](../../templates/docs/code-assistant-policy.md)
- [Pull request template](../../templates/github/PULL_REQUEST_TEMPLATE.md)
- [Default branch ruleset](../../templates/github/rulesets/default-branch.json)
- [Runbook](../../templates/docs/runbook.md)
- [Threat model](../../templates/docs/threat-model.md)

## Sources

- DORA research, including the 2025 report "State of AI-assisted Software Development": https://dora.dev/research/
- AGENTS.md, an open format for guiding coding agents: https://agents.md/
- OpenTelemetry semantic conventions for generative AI: https://opentelemetry.io/docs/specs/semconv/gen-ai/
- NIST SP 800-218A, Secure Software Development Practices for Generative AI and Dual-Use Foundation Models: https://csrc.nist.gov/pubs/sp/800/218/a/final
- OWASP Top 10 for LLM Applications 2025: https://genai.owasp.org/llm-top-10/
- US Copyright Office, Copyright and Artificial Intelligence: https://www.copyright.gov/ai/
