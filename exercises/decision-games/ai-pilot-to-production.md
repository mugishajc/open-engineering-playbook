# Decision game: AI pilot to production

An AI pilot wowed the executive committee, and the CEO wants it live for every credit officer before quarter-end, in three weeks. It was tested on twelve hand-picked cases, nobody knows what it costs per request, and it reads customers' financial data through a model hosted in another country. Choose a path, then see where each one leads.

| | |
|---|---|
| Who | CTOs, chief data or digital officers, heads of risk and compliance, product owners and AI leads |
| Time | 30 minutes alone; 45 minutes as a group with risk and compliance present |
| Practice it teaches | [Building with AI](../../playbook/ai/building-with-ai.md), [AI governance](../../playbook/ai/ai-governance.md), [AI application security](../../playbook/ai/ai-application-security.md), [AI use case assessment](../../templates/docs/ai-use-case-assessment.md) |

## The situation

A regional bank lends to small businesses, many of them sole traders. Its innovation team built a pilot in six weeks: an assistant that reads a loan application, the bank statements and the accounts, then drafts the credit memo and suggests "approve", "decline" or "refer". Credit officers take about 3 hours per memo today. All organisations, people and numbers here are fictional.

- The demo used 12 applications chosen by the team. The memos were good. Nobody measured how often they were wrong.
- The pilot calls a hosted language model in another country through a developer's API key.
- There is no eval set, no cost estimate per memo, no logging plan and no fallback.
- 140 credit officers would use it. Quarter-end is in three weeks; the CEO has mentioned it to the board.
- Many applicants are sole traders, so assessing their creditworthiness means assessing natural persons. The EU AI Act lists creditworthiness evaluation of natural persons among its high-risk uses (Annex III). The bank's supervisor also expects model risk management for models used in credit decisions (the US Federal Reserve's SR 11-7 guidance is a widely used reference).

## Round 1: what do you do?

**A. Limited release first.** Build an eval set, move to approved hosting and data terms, add logging and a kill switch, then release to 10 officers behind a feature flag. The board hears "controlled use with measured results" at quarter-end, not "live", and the other 130 officers wait 10 weeks or more.

**B. Launch to all 140 officers in three weeks.** Officers save hours per memo from day one. Every memo is still signed by a credit officer, who stays accountable for the decision. Fix problems as real use shows them, as the bank does with any new tool.

**C. Narrow the scope first.** Ship only the extraction part: pull figures from statements and accounts into the memo template, with sources. Drop the approve or decline suggestion for now. Extraction is easy to check against the documents and leaves the decision with the officer.

**D. Build in-house.** Customer financial data never leaves the bank. Fine-tune an open-weight model on the bank's own past memos, hosted in its data centre. It solves residency for good and builds a capability competitors cannot buy.

Pick one before you open the consequences.

<details>
<summary>Consequences of A: limited release first</summary>

Weeks 1 to 4: the team labels 300 past applications with the memos that experienced officers wrote, sets pass thresholds with the head of credit (figures must match sources in at least 99% of fields; the suggestion must agree with the final human decision in a stated share of cases), and moves to an approved model provider under a business agreement that excludes training on the bank's data and meets its data residency rules. Cost per memo is measured and budgeted. Every prompt, retrieved document and output is logged with personal data masked.

Weeks 5 to 10: 10 officers use it behind a feature flag. Memo time drops for them, and the weekly human review finds two failure types, which go into the eval set. The governance board classifies the use as high-risk and opens the documentation it needs.

The CEO tells the board at quarter-end that the assistant is in controlled use with measured results, not that it is live everywhere. That is a less exciting sentence and a much safer one.

</details>

<details>
<summary>Consequences of B: launch to all in three weeks</summary>

Usage is high in week one. In week three, an internal audit sample of 40 memos finds that 6 contain figures that do not match the bank statements, and in 3 the suggestion was "approve" for applications that breach the bank's own lending policy. Officers under time pressure had signed them. The compliance team asks whether the bank has deployed a high-risk AI system without the required risk management, human oversight design, logging and documentation. The answer is yes.

The feature is switched off, but there is no kill switch, so it takes a deployment. Customer financial data has been sent abroad under a developer's personal terms of service, which nobody reviewed. "A person signs it" did not amount to human oversight: officers were not shown sources, were not trained on the system's limits, and had no time to check.

</details>

<details>
<summary>Consequences of C: narrow the scope first</summary>

Extraction with sources is easier to evaluate (does the figure match the document?) and keeps the credit decision with the officer. It may also fall outside the high-risk category if it only prepares information and does not evaluate creditworthiness; the governance team must confirm that, and the answer may change as the product grows. Officers save a large part of the 3 hours on data entry.

This is a strong path when combined with A: ship extraction first through the same eval, flag and logging steps, and treat the recommendation as a separate, later, higher-risk release.

</details>

<details>
<summary>Consequences of D: build in-house</summary>

The data residency problem disappears, but six months go into GPU procurement, training data cleaning and model work before anyone knows whether the task needs fine-tuning at all. The bank still needs an eval set, logging, a kill switch and governance, so D does not remove any of A's work; it adds to it. The [building with AI](../../playbook/ai/building-with-ai.md#prompting-retrieval-or-fine-tuning) page says to start with prompting and retrieval and fine-tune only when evals show a gap that cheaper options cannot close.

Self-hosting can be the right answer where law or risk rules out any external provider. Decide that from the use case assessment, not as a reflex.

</details>

## What the playbook recommends, and why

**A, ideally with C's narrower scope as the first release.** The [building with AI](../../playbook/ai/building-with-ai.md#from-pilot-to-production) page sets the path: problem and assessment, prototype, eval set and threshold, hardening, limited release, general release. This pilot tried to jump from stage 2 to stage 6. The playbook's diagnosis applies: most pilots stall because nobody defined "good enough" or tested it.

Before limited release, the bank needs:

| Gate | Evidence |
|---|---|
| Use case assessment | Data, legal basis, risk classification, non-AI baseline ([template](../../templates/docs/ai-use-case-assessment.md)) |
| Eval set and threshold | 100 to 500 labelled cases, threshold agreed with the head of credit |
| Hosting and data terms | Approved provider, no training on bank data, residency met |
| Security | [Threat model](../../templates/docs/threat-model.md) with section 6; output validated; no secrets in prompts ([AI application security](../../playbook/ai/ai-application-security.md)) |
| Control | Kill switch under 5 minutes, fallback to the manual process, cost and latency budgets |
| Governance | Risk classification under the EU AI Act and model risk rules; human oversight designed, not assumed ([AI governance](../../playbook/ai/ai-governance.md)). Check EUR-Lex for the current application dates of high-risk obligations. |

For the CEO conversation, see [decision making](../../leaders/decision-making.md): a three-week deadline for a decision that is hard to reverse, in a regulated activity, is the time to slow down on purpose.

## Debrief questions

1. Which of your AI pilots has an eval set with a pass threshold agreed by the business owner?
2. What does "human in the loop" mean in your organisation? Do reviewers have the time, sources and training to disagree with the model?
3. Who decides the risk classification of a new AI use case, and how long does it take?
4. How many developers' personal API keys are calling external model providers with company data today?
