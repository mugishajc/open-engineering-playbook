# AI use-case assessment: [use case name]

<!-- Guidance: playbook/ai/ai-governance.md. Low-risk uses complete sections 1 and 2 only. Medium and high complete all sections. -->

| Field | Value |
|---|---|
| Register ID | [AI-...] |
| Use-case owner (accountable) | [name, role] |
| Team | [...] |
| Status | [idea, pilot, production, retired] |
| Date and version | [YYYY-MM-DD, v0.1] |
| Pilot end date (default 90 days) | [YYYY-MM-DD] |

## 1. Purpose and scope

- Problem this solves, in one sentence: [...]
- Who uses it: [staff, customers, citizens]
- Who is affected by its outputs: [...]
- What happens without it today: [...]
- Does it make or support decisions about people (hiring, credit, access to services, education)? [yes, no]
- Can it act on systems without a person approving each action (agent)? [yes, no; list tools and permissions]

## 2. Risk tier

Tick one. If in doubt, choose the higher tier and ask the AI governance lead.

- [ ] Not allowed (prohibited practice under EU AI Act Article 5 or local law): stop here.
- [ ] High (EU AI Act Article 6 and Annex III, or a safety component of a regulated product)
- [ ] Medium (transparency duties under Article 50, or real impact on customers or records)
- [ ] Low (minimal risk)

Reason for the tier: [...]

- Our role under the EU AI Act: [provider, deployer, both, not in scope]. If we put our name or trademark on a high-risk system, make a substantial modification to it, or change the intended purpose of a system so that it becomes high-risk, we become its provider (Article 25).
- If the use case falls under Annex III but we judge it not high-risk under Article 6(3): the documented reasoning [link] and the EU database registration reference (Articles 6(4) and 49(2)) [...]
- Can it act on production, customer data or money (including coding agents that run commands)? If yes, the internal tier is at least Medium, whatever the AI Act category.

## 3. Model and supplier

| Item | Value |
|---|---|
| Model(s) and version | [...] |
| Provider, hosting location and jurisdiction | [...] |
| Self-hosted or API | [...] |
| Contract covers data use, retention, training on our data, location | [yes, no, link] |
| Model or weights recorded in SBOM | [yes, no] |

## 4. Data

| Item | Value |
|---|---|
| Data sets used (training, fine-tuning, retrieval, prompts) | [...] |
| Highest classification (public, internal, confidential, restricted) | [...] |
| Personal data? Lawful basis? | [...] |
| Data owner approval | [name, date] |
| DPIA needed? Link | [...] |
| Known gaps or bias risks in the data | [...] |

## 5. Evaluation

| Measure | Method | Threshold to launch | Result |
|---|---|---|---|
| Task quality (for example accuracy on a labelled test set) | [...] | [...] | [...] |
| Error rate on groups that matter (fairness) | [...] | [...] | [...] |
| Prompt injection and misuse tests (OWASP LLM Top 10) | [...] | [no critical findings] | [...] |
| Cost per request and monthly cap | [...] | [...] | [...] |
| Latency | [...] | [...] | [...] |

## 6. Human oversight and transparency

- Human overseer role and how they can override or stop the system: [...]
- Actions that always need human approval: [...]
- How users are told they are dealing with AI or AI-generated content: [...]
- How affected people can challenge an outcome: [...]
- Fundamental rights impact assessment required (Article 27: public bodies, private entities providing public services, and deployers of credit scoring or life and health insurance pricing systems)? [yes, no; link]
- Solely automated decision with legal or similarly significant effect on a person (GDPR Article 22)? [yes, no]. If yes: the legal ground, and how a person obtains human review, expresses their view and contests the decision: [...]

## 7. Monitoring and incidents

- Production metrics and alert thresholds (quality, drift, cost, abuse): [...]
- Logs kept and retention: [...] (at least 6 months for high-risk systems, Articles 19 and 26(6); mask personal data at write time)
- Incident route: [team on-call, link]
- Serious incident reporting (high-risk, Article 73): who reports to the market surveillance authority, and the deadlines: 15 days from awareness, 2 days for a widespread infringement or serious and irreversible disruption of critical infrastructure, 10 days for a death: [...]
- Review date (6 to 12 months): [YYYY-MM-DD]

## 8. Decision

| Gate | Decision (go, go with conditions, no go) | Conditions | Decided by | Date |
|---|---|---|---|---|
| Pilot | [...] | [...] | [...] | [...] |
| Production | [...] | [...] | [...] | [...] |
| Independent review (high tier only) | [...] | [...] | [...] | [...] |
