# Board and executive reporting

Give the board one page: a scorecard of 8 to 12 measures with a trend and a threshold, the top risks in business terms, the status of key programmes, and the one or two decisions you need from them. Boards govern risk and investment; they cannot govern what they cannot read in ten minutes. Report bad news early, in the same format as good news, with what you are doing about it.

This page is for the CTO, CIO and chief architect who report to a board, an executive committee, an audit committee, or an accounting officer in government. It builds on the board measures in [IT governance](../playbook/operating-model/it-governance.md).

## When to use this

- You are preparing your first board or executive committee report.
- Board members ask questions that show they did not understand the last report.
- The audit committee has asked for a cyber security or technology risk briefing.
- You need the board to accept a risk, fund debt reduction, or approve a security investment.

## What boards and executive committees need

| They need | So you give them | Not |
|---|---|---|
| To know whether technology supports the business plan | Delivery and key programme status against plan | A list of projects |
| To know the risks are understood and inside appetite | Top 5 risks with trend, owner and treatment, measured against the risk appetite | Every risk in the register |
| To oversee cyber security as a business risk | Security posture against agreed thresholds and incident history | Tool names and scanner counts |
| To approve spend with confidence | Cost trend, investment mix and the return on major programmes | Line-by-line invoices |
| To know the organisation can keep running | Resilience tests done, results, and gaps | Assurances without evidence |
| To make decisions | A clear ask, options and your recommendation | Information with no ask |

The UK NCSC Board Toolkit is written for board members, not technologists. It groups cyber security into topics such as risk management, the threat, suppliers, culture and incident response, each with questions boards should ask. Read it before your first report, so you answer the questions your board will be told to ask.

## The one-page scorecard

Show each measure with the last 4 quarters, the threshold from the risk appetite, and a status. Thresholds below are illustrative starting points; set your own with the board.

| Area | Measure | Example threshold |
|---|---|---|
| Delivery | Change lead time and deployment frequency for tier 1 services (DORA) | Lead time under 1 week |
| Delivery | Key programmes on track against their forecast range | At least 80% |
| Reliability | Tier 1 services that met their SLO for the quarter | 100%, with a recovery plan for any miss |
| Reliability | Major incidents (SEV1) and customer hours lost | No more than 2 per quarter |
| Security | Critical vulnerabilities on internet-facing systems past their fix deadline | Zero older than 7 days |
| Security | Privileged accounts without phishing-resistant multi-factor authentication | Zero |
| Resilience | Tier 1 services with a successful restore and failover test in the last 6 months | 100% |
| Cost | Run cost against budget and unit cost trend | Within 5% of budget |
| People | Attrition, key-person risks and critical open roles | Attrition below the agreed rate; no critical role open over 90 days |
| Major risks | Risks outside appetite | Zero without an approved treatment plan |
| AI | AI systems in production by risk tier, and those overdue for review | Zero overdue |
| End of life | Systems on unsupported software | Each has a funded retirement date |

Below the table, write three sentences: what changed since last time, what worries you, and what you need from the board.

## Explaining risk in business terms

Translate every technical risk into the consequence the board already governs: revenue, cost, customers, legal exposure, reputation, or the ability to deliver the plan.

| Topic | Technical framing (avoid) | Business framing (use) |
|---|---|---|
| Technical debt | "The monolith has poor test coverage and tight coupling." | "New features in payments take [N] times longer than elsewhere, and [share] of changes there cause an incident. Fixing it costs [teams] for [quarters] and returns that capacity by [date]." See [technical debt](../playbook/architecture/technical-debt.md). |
| Security risk | "We have hundreds of high CVEs." | "Customer records could be exposed through [N] internet-facing systems that are behind on patches. We will close the gap by a stated date; until then we accept the risk with these compensating controls." |
| AI risk | "The model hallucinates." | "The customer assistant gave wrong answers in a stated share of test cases. We have a human review step for refunds and an off switch. The EU AI Act may apply; legal is assessing by a stated date." See [AI governance](../playbook/ai/ai-governance.md). |
| Supplier risk | "Single-vendor lock-in." | "If this supplier fails, these services stop for an estimated period, and we have no tested exit plan." See [third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md). |
| End of life | "The OS is out of support." | "From a stated date we receive no security fixes for the systems that run billing." |

Square brackets mark where your own measured data goes. The examples show the shape of the sentence, not real figures. Say how confident you are in each number.

## Risk appetite statements

A risk appetite statement tells the organisation how much of a given risk the board will accept. It is only useful when it is measurable and linked to a scorecard measure.

| Weak | Measurable |
|---|---|
| "We have a low appetite for cyber risk." | "No critical vulnerability on an internet-facing system remains unpatched for more than 7 days without an approved exception." |
| "Systems should be highly available." | "Tier 1 services lose no more than 4 hours of unplanned downtime per quarter." |
| "We manage supplier risk." | "No single supplier supports more than two critical services without a tested exit plan." |
| "We use AI responsibly." | "No AI system makes a decision with legal or similar effect on a person without human review." |

Write 5 to 10 statements, have the board approve them, review them every year, and show each one as a scorecard threshold.

## How to report bad news

1. **Early.** Tell the chair or the CEO within 24 hours of a material incident or a programme going off track. Do not wait for the next meeting.
2. **In the same format.** A red status in the scorecard, not a separate slide that looks like an excuse.
3. **Facts, impact, actions, asks.** What happened, what it means for the business, what you are doing with dates, and what you need from the board.
4. **Own it.** Say what you could have done differently. Do not name individuals.
5. **Follow up.** Report progress on the actions at every meeting until they close.

## Audit committee questions to expect

Prepare written answers with evidence for each.

- What are our most important systems and data, and how do we know they are protected?
- How do we know our backups work? When did we last restore one?
- Who can access production and customer data, and how often do we review that access?
- What are our top technology risks, and which are outside appetite?
- Which audit findings are overdue, and why?
- How quickly could we detect and respond to an attack? When did we last exercise it?
- Which suppliers could hurt us most, and what is our exit plan?
- What regulatory reporting duties apply to us, and could we meet the deadlines?
- How do we control the use of AI, including code assistants?
- What would you do with more budget, and what would you stop with less?

## Common mistakes

| Mistake | Fix |
|---|---|
| 30-slide technical update | One page plus an appendix the board can skip |
| Measures without thresholds | Every measure links to a risk appetite statement or a target |
| Only green | A report that is always green is not believed. Show the reds and the plan. |
| Jargon | Test the page on a non-technical colleague before it goes out |
| No ask | End with the decision or guidance you need, or say "for information only" |
| Different numbers from the finance or risk reports | Agree sources with finance and risk before the meeting |

## Templates

- [Board engineering report](../templates/leaders/board-engineering-report.md)
- [Quarterly engineering review](../templates/leaders/quarterly-engineering-review.md)
- [Risk register](../templates/strategy/risk-register.csv)
- [Business case](../templates/strategy/business-case.md)

## Sources

- UK NCSC, Board Toolkit: https://www.ncsc.gov.uk/collection/board-toolkit
- ISO/IEC 38500, Governance of IT for the organization: https://www.iso.org
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
- Google SRE book, service level objectives: https://sre.google/sre-book/service-level-objectives/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
