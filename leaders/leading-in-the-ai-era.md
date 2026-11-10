# Leading in the AI era

AI does not fix a weak engineering organisation. It makes it faster at whatever it already does, good or bad, and the 2025 DORA report describes AI in exactly these terms: an amplifier of existing strengths and weaknesses. So the leader's job is not to buy tools and announce targets. It is to make five decisions explicitly, fund work in stages with exit criteria, protect the skills pipeline, and judge results against a measured baseline rather than anecdotes or usage counts.

## When to use this

This page is for CEOs, CTOs, CIOs, Chief Data and Chief Digital Officers, board members and government technology leaders.

- The board or minister has asked "what is our AI strategy?" and the honest answer is a list of pilots.
- Teams use code assistants and AI features, and you cannot say whether delivery, quality or cost got better.
- You are under pressure to cut headcount on the promise of AI productivity.
- You must decide where data may go: a hosted model, a self-hosted one, or none.
- You are writing next year's budget and AI is a line with no outcome attached.

The practice pages behind this one: [AI governance](../playbook/ai/ai-governance.md), [building with AI](../playbook/ai/building-with-ai.md), [AI engineering practices](../playbook/ai/ai-engineering-practices.md), [AI architecture patterns](../playbook/ai/ai-architecture-patterns.md), [AI application security](../playbook/ai/ai-application-security.md), [code assistants](../playbook/people/code-assistants.md) and [agile in the AI era](../playbook/ways-of-working/agile-in-the-ai-era.md).

## The five decisions only leaders can make

Teams cannot make these for you. If you do not decide, each team decides differently, and you find out after an incident.

| Decision | The question | A good answer looks like | Go deeper |
|---|---|---|---|
| Where AI creates value here | Which three to five business outcomes could AI move, by how much, and how would we know? | Named outcomes with a baseline today, an owner and a non-AI alternative considered | [AI use case assessment](../templates/docs/ai-use-case-assessment.md) |
| Risk appetite | Which uses do we encourage, which need review, which do we refuse? | A written statement per risk tier, for example "no AI decision with legal effect on a person without human review" | [AI governance](../playbook/ai/ai-governance.md) |
| Data readiness | Is the data these use cases need owned, classified, of known quality and lawful to use? | Data owners named, classification applied, quality measured for the data in scope | [Data governance](../playbook/data/data-governance.md), [data quality](../playbook/data/data-quality.md) |
| Build, buy or adopt for models | Hosted model, a product with AI built in, an open-weight model we run, or our own fine-tuned model? | A choice per use case, scored on the same matrix as any other platform, with an exit plan | [Build, buy or adopt](../playbook/strategy/build-buy-adopt.md) |
| Sovereignty: where data may go | Which data classes may leave our network, our country or our contracted providers? | A table of data class against allowed model locations, signed off by legal and security | [Code assistants: data classification](../playbook/people/code-assistants.md), [cloud, on-premises and air-gapped](../playbook/platform/cloud-on-prem-air-gapped.md) |

### Model sourcing options

| Option | Choose it when | Watch out for |
|---|---|---|
| Hosted model API under a business agreement | Speed matters and the data class allows it | Retention and training terms, region, price changes, model retirement dates |
| Product with AI features (SaaS) | The use case is common: meeting notes, search, support tooling | AI features switched on by the vendor without review; include them in the register |
| Open-weight model you host | Data cannot leave, the network is air-gapped, or volume makes per-call pricing expensive | GPU capacity, patching, evaluation and model licences become your job |
| Fine-tuning or training your own | Evals show a gap that prompting and retrieval cannot close, and you have thousands of good examples | Cost, data governance, and retraining every time the base model changes. Rarely the first step. |

## Funding: pilots with exit criteria, then platforms

Fund AI like any uncertain investment: small bets with stop points, then shared capability once the bets prove out.

| Stage | Fund | Exit criteria to move on | Stop if |
|---|---|---|---|
| Pilot (up to 90 days) | One small team, one use case | Eval set and threshold met on real data, cost per outcome estimated, owner for production named | No measurable effect against the baseline, or the data cannot lawfully be used |
| Limited production (1 to 2 quarters) | The owning team, plus security and data review | Outcome moved for real users, change fail rate and cost inside budget | The effect disappears at real volume |
| Platform | A shared model gateway, evaluation tooling, data access and guardrails | Two or more production use cases need the same capability | Fund only what at least two teams will use |

Most pilot failures are decided before the pilot starts: no baseline, no eval set, no owner for production. Refuse to fund a pilot without all three.

### Where to invest first

Not every task benefits equally. Prioritise by how well the task fits today's tools.

| Tier | Task shape | Examples | Controls needed |
|---|---|---|---|
| 1. High volume, narrow scope, clear right answer | Work where a correct output is easy to verify | Support triage, test generation, documentation updates, data entry checks | Eval set with pass threshold, sampling audit |
| 2. High volume, judgement needed, human review feasible | Work where a person checks each output before it acts | Code review assist, incident summarisation, draft communications | Human approval before action, confidence-based routing |
| 3. Low volume, high stakes, human decides | Work where the cost of a wrong answer is severe | Architecture decisions, hiring, incident response, regulatory filings | AI prepares options and evidence; a person decides |

Start with tier 1. Move to tier 2 once the team has built review habits and the measurement baseline from tier 1. Tier 3 is support, not automation: the AI assembles the briefing, the person makes the call.

### Before you approve an AI use case

1. Is it in the AI register with a risk tier from [AI governance](../playbook/ai/ai-governance.md#risk-tiers)?
2. Is a business owner accountable for the outcome, not only a technical owner for the system?
3. Is there a baseline for the outcome, and a non-AI option it was compared with?
4. Is the data lawful to use for this purpose, and allowed to go where the model runs?
5. Is there an eval set with a pass threshold agreed by the owner, and a stop condition with a date?
6. Can it act on production systems, customer data or money? If so, it is at least Medium tier, irreversible actions need a person's approval, and there is an off switch someone has tested.
7. Does it make or shape a decision about a person? If so, who reviews it, and how can the person challenge it?
8. What does it cost per outcome at expected volume, and who pays when volume grows?

Escalate to the executive committee, and report to the board, any High-tier use, any use that makes or shapes decisions with legal or similar effect on people, and any agent that can move money or change customer records without a person's approval. Low-risk uses get a decision within 5 working days and high-risk ones within 30, as set in [AI governance](../playbook/ai/ai-governance.md).

## Workforce and skills

AI changes what engineers spend their time on. It does not remove the need for people who understand the system.

| Topic | Do | Avoid |
|---|---|---|
| Reskilling | Give every engineer protected time (starting point: 4 hours a fortnight) to learn specs, evaluation, review of generated code and AI security | One-off launch training with nothing after |
| Junior pipeline | Keep hiring juniors. Pair them with seniors, have them explain every change they submit, and put them on call with a shadow | Freezing junior hiring because "AI does junior work". Today's juniors are the seniors you will need in five years. |
| Skill erosion | Keep design reviews, debugging without an assistant in learning exercises, and postmortems where people explain how the system works | Measuring people by output volume, which rewards accepting suggestions unread |
| Roles that change | Expect more time in problem framing, review, testing and operations; fewer hours typing | Cutting testers, reviewers or SREs to pay for tools. That is where the new bottleneck is. |

See [skills gap](../playbook/people/skills-gap.md), [career framework](../playbook/people/career-framework.md) and [onboarding](../playbook/people/onboarding.md).

## Measuring impact with data, not anecdotes

1. **Baseline first.** Record each team's DORA metrics, cost and user outcome measures for at least one quarter before rollout.
2. **Controlled rollout.** Roll out in waves by team. Assign teams to waves by a rule you write down before you start (for example alternate teams in the service catalogue), not by volunteering: early volunteers are usually the strongest teams and make any tool look good. Compare the change in each wave with the change in teams not yet started over the same period (a difference-in-differences comparison).
3. **Measure stability, not only speed.** Track all five DORA metrics. Watch change fail rate and rework rate most closely: rework rate is the share of deployments that are unplanned and caused by a production incident.
4. **Cost per outcome.** Tool and model spend divided by something the business values: cost per resolved support case, per processed claim, per change shipped without rework.
5. **User outcomes.** Task success, time to complete, complaints and escalations to a person.
6. **Ask the people.** A short survey each quarter on where tools help and where they cost time.

| Measure | Healthy sign | Warning sign |
|---|---|---|
| Change lead time and deployment frequency | Improve, while instability holds steady | Improve while change fail rate rises |
| Change fail rate and rework rate | Within 10% of baseline | More than 10% above baseline for 2 quarters in a row (the decision rule in [metrics](../playbook/measurement/metrics.md)): pause wider rollout |
| Review time and pull request size | Stable | Queues growing, pull requests getting larger |
| Cost per outcome | Falling or stable as volume grows | Total spend rising with no outcome attached |
| User outcome measure | Moving in the direction the business case promised | Unchanged after two quarters |

The [metrics](../playbook/measurement/metrics.md) page explains how to collect these. Never use them to rate individuals.

Public evidence is mixed: a 2025 randomised trial by METR found experienced open source developers were slower with AI tools while feeling faster, and DORA's 2024 and 2025 reports found AI adoption associated with lower delivery stability. See [agile in the AI era](../playbook/ways-of-working/agile-in-the-ai-era.md#what-the-evidence-says). Your own baseline is the only result that counts.

**Consult before you collect.** Assistant telemetry and delivery dashboards are built from individual events. Where employee representatives have rights over systems that can monitor performance or behaviour (in Germany, for example, the works council co-determines under section 87(1) no. 6 of the Works Constitution Act), agree the metric definitions, aggregation level and retention with them before collection starts. Everywhere, report at team level and delete individual event data you do not need.

## When the gain is real

The board will ask what happens to a measured gain. Decide the rule before the review, not after.

1. **Express the gain as capacity per team**, against the baseline, with the stability measures alongside. A gain with rising change fail rate is not a gain.
2. **Use it in this order:** first, the backlog the business already wants; second, growth absorbed without new hiring; third, less contractor and supplier spend; only then permanent roles, with HR and legal involved from the start.
3. **Do not announce role reductions before the measured review.** An announcement before the evidence gives people a reason to hide gains, and commits you to a number the data may not support.
4. **Consult where the law or agreements require it.** In the EU, Directive 2002/14/EC sets general duties to inform and consult employees, and some countries add more. Plan the time for consultation into the decision.
5. **Renegotiate effort-priced supplier contracts.** Under time-and-materials pricing, the supplier decides whether faster work means fewer billed days. Move to capacity or outcome pricing at renewal so the gain is not billed back to you. See [suppliers and contracts](../playbook/strategy/suppliers-and-contracts.md).
6. **Watch two warning measures for two quarters after any change:** attrition of senior engineers, and the number of junior engineers hired and promoted. If either falls sharply, slow down.

## Governance that enables

Governance works when the safe path is also the fast path. Keep one register of AI use, give low-risk uses a decision within 5 working days, and spend review effort on the few high-risk ones. Provide approved tools quickly, so nobody needs a personal account. Details: [AI governance](../playbook/ai/ai-governance.md).

## What not to do

| Do not | Why it backfires | Do instead |
|---|---|---|
| Mandate usage quotas ("everyone uses the assistant daily") | People meet the quota, not the goal. Usage tells you nothing about value. | Set outcome goals and let teams choose where tools help |
| Measure lines or share of code generated | Counts activity. More code is usually more cost and more to review. | DORA metrics, cost per outcome, user outcomes |
| Cut reviewers and testers to fund tools | Generation is cheap; verification is now the constraint | Protect and plan review capacity explicitly |
| Ban everything | Staff use personal accounts in secret, with no data controls | Approve one safe option fast and block the rest |
| Promise headcount savings before measuring | Locks the organisation into a number that the data may not support | Commit to a measured review after two quarters, with the rule in [when the gain is real](#when-the-gain-is-real) agreed in advance |
| Let every team build its own model integration | Duplicate cost, no central view of data flows or spend | One gateway once two teams need models |

## A 12-month plan

| Months | Actions | Evidence it is done |
|---|---|---|
| 1 to 3 | Write the five decisions down. Publish an acceptable use policy and approve one code assistant. Start the AI register. Baseline DORA metrics and costs. Pick 2 to 3 pilots with exit criteria. | Signed decisions, register live, baseline dashboard |
| 4 to 6 | Run pilots to their gates. Roll out assistants in waves. Train every engineer on review of generated code and AI security. Set up evaluation in CI for AI features. | Go or no-go decision per pilot, wave comparison data |
| 7 to 9 | Move proven pilots to limited production. Fund a shared gateway and evaluation tooling if two use cases need them. Update the career framework for changed roles. | Use cases in production with owners, cost per outcome reported |
| 10 to 12 | Review the year against the baseline. Stop what did not move outcomes. Refresh the risk appetite and the sovereignty table. Set next year's budget from the evidence. | Board report with measured results, next year's plan |

## Questions boards should ask

| # | Question | A worrying answer |
|---|---|---|
| 1 | Which business outcomes is AI meant to move, and what were they before we started? | Usage counts, licences bought or "productivity" with no baseline |
| 2 | What is our risk appetite for AI, and which uses have we refused? | No use has ever been refused |
| 3 | Where does our data go when staff or products use AI, and who approved it? | "The vendor says it is secure"; no table of data class against location |
| 4 | Has our change fail rate or rework rate risen since teams adopted code assistants? | Not measured, or only speed is reported |
| 5 | Which pilots did we stop this year, and why? | None stopped, or pilots still running after 90 days with no gate |
| 6 | What does AI cost us per outcome, and is that falling? | Only total spend, or no owner for the spend |
| 7 | Which AI systems make or shape decisions about customers, citizens or staff, and where is the human review? | No list, or "a person can override it" with no record of overrides |
| 8 | Are we still hiring and growing junior engineers? | Junior hiring frozen on the promise of AI |
| 9 | Could we switch model provider within a quarter if we had to? | No exit plan, or prompts and evals tied to one provider's tools |
| 10 | Do the EU AI Act or other rules apply to us, and by when? | "Legal is looking at it" with no date (check EUR-Lex for current dates) |

See [board and executive reporting](board-and-executive-reporting.md) for how to report the answers.

## Common mistakes

| Mistake | Fix |
|---|---|
| An "AI strategy" that is a list of tools | Start from three to five business outcomes with baselines |
| Pilots that run forever | 90-day gate with a go or no-go decision |
| Treating AI as an IT project | A business owner accountable for each outcome |
| Reading vendor productivity claims as your result | Measure your own teams against their own baseline |
| Data readiness discovered in month 6 | Check data ownership, quality and lawful basis before funding the pilot |
| Leaders who never use the tools | Use them yourself for a month so your judgement is first-hand |

## Templates

- [AI use case assessment](../templates/docs/ai-use-case-assessment.md)
- [Code assistant policy](../templates/docs/code-assistant-policy.md)
- [Business case](../templates/strategy/business-case.md)
- [Pre-mortem](../templates/leaders/pre-mortem.md)
- [Board engineering report](../templates/leaders/board-engineering-report.md)
- [OKR template](../templates/leaders/okr-template.md)

## Sources

- DORA research programme, including the 2025 report "State of AI-assisted Software Development": https://dora.dev/research/
- DORA metrics guide: https://dora.dev/guides/dora-metrics-four-keys/
- METR, "Measuring the Impact of Early-2025 AI on Experienced Open-Source Developer Productivity", July 2025: https://arxiv.org/abs/2507.09089
- Directive 2002/14/EC on informing and consulting employees: https://eur-lex.europa.eu/eli/dir/2002/14/oj
- Betriebsverfassungsgesetz (German Works Constitution Act), section 87: https://www.gesetze-im-internet.de/betrvg/__87.html
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
- ISO/IEC 42001:2023, AI management systems: https://www.iso.org/standard/81230.html
- EU Artificial Intelligence Act, Regulation (EU) 2024/1689: https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- UK NCSC, Board Toolkit: https://www.ncsc.gov.uk/collection/board-toolkit
