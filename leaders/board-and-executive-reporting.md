# Board and executive reporting

Give the board one page: a scorecard of no more than 12 measures, one per row, each with a trend and a threshold, the top risks in business terms, the status of key programmes, and the one or two decisions you need from them. Boards govern risk and investment; they cannot govern what they cannot read in ten minutes. Report bad news early, in the same format as good news, with what you are doing about it.

This page is for the CTO, CIO and chief architect who report to a board, an executive committee, an audit committee, or an accounting officer in government. This page is the single source for the board scorecard; [IT governance](../playbook/operating-model/it-governance.md) explains the governance model behind it.

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

In the UK, the Cyber Governance Code of Practice (DSIT and NCSC, April 2025) sets out the actions boards and directors should take on cyber risk, in five principles: risk management; strategy; people; incident planning, response and recovery; and assurance and oversight. The NCSC Board Toolkit supports it with questions boards should ask. Read both before your first report, so you answer the questions your board will be told to ask. Outside the UK, use them as a checklist even where they are not expected.

## The one-page scorecard

Show each measure with the last 4 quarters, the threshold from the risk appetite, and a status. Thresholds below are illustrative starting points; set your own with the board. One measure per row, no more than 12 rows.

| Area | Measure | Example threshold |
|---|---|---|
| Programmes | Major programmes: forecast cost to complete against approved budget | Within 10% of the approved budget, or a revised budget approved |
| Programmes | Major programmes: forecast date range (85% confidence) against plan | Inside the plan, or a re-plan approved |
| Reliability | Tier 1 services that met their SLO for the quarter | 100%, with a recovery plan for any miss |
| Reliability | Major incidents (SEV1) | No more than 2 per quarter |
| Security | Actively exploited (CISA KEV) or critical vulnerabilities on internet-facing systems past their fix deadline | Zero: exploited ones fixed within 72 hours, other critical ones within 7 days |
| Resilience | Tier 1 services with a full restore exercise in the last quarter, within the recovery time objective | 100% (see [backup and recovery](../playbook/reliability/backup-and-recovery.md)) |
| Cost | Run cost against budget | Within 5% of budget |
| People | Critical roles with no successor, or open for more than 90 days | Zero without a plan |
| Risk | Risks outside appetite | Zero without an approved treatment plan |
| Audit and regulatory findings | Overdue findings, and the age of the oldest | Zero overdue by more than 90 days |
| AI | AI systems in production overdue for review | Zero |
| End of life | Systems on unsupported software without a funded retirement date | Zero |

Below the table, write three sentences: what changed since last time, what worries you, and what you need from the board. Put customer hours lost, incident detail and the risk register extract in the appendix.

**DORA metrics belong in the executive committee pack, not on the board scorecard.** Boards govern risk, investment and outcomes; they cannot act on change lead time or deployment frequency, and a board target on them invites gaming. The executive committee pack also carries privileged access without phishing-resistant multi-factor authentication, unit cost trends and attrition. Boards see these only as context for a programme or a risk.

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
| "We have a low appetite for cyber risk." | "No actively exploited vulnerability on an internet-facing system stays open for more than 72 hours, and no other critical one for more than 7 days, without an approved exception." |
| "Systems should be highly available." | "Tier 1 services lose no more than 4 hours of unplanned downtime per quarter." |
| "We manage supplier risk." | "No single supplier supports more than two critical services without a tested exit plan." |
| "We use AI responsibly." | "No AI system makes a decision with legal or similar effect on a person without human review." |

Write 5 to 10 statements, have the board approve them, review them every year, and show each one as a scorecard threshold.

## What reaches the board, and how fast

Agree these thresholds with the chair and the audit committee chair in writing, before you need them. The numbers are starting points; tie each one to a scorecard threshold.

| Event | Who is told | By when |
|---|---|---|
| A cyber incident or outage that may be material, reportable to a regulator, or front-page news | CEO, then the chair and audit committee chair | CEO within 24 hours; the chairs the same day the CEO decides it may be material |
| A major programme forecast moves outside tolerance (cost more than 10% over the approved budget, or the 85% date past the plan) | Sponsor and CEO; the board as a decision paper | Within 24 hours to the CEO; the board at its next meeting, or sooner if money must be released |
| A risk moves outside appetite with no approved treatment | Risk owner and the executive committee; the board on the scorecard | Next executive meeting; next board meeting |
| A regulator, auditor or supervisor raises a finding rated high | Audit committee chair | Within 5 working days |
| A request to accept a risk outside appetite | The body that set the appetite | Before the risk is taken, never after |

## What the board decides

The board does not approve releases or designs. It keeps the decisions below and delegates the rest with written limits.

| The board keeps | With these inputs | Delegates to the executive |
|---|---|---|
| Risk appetite for technology, cyber, supplier and AI risk | 5 to 10 measurable statements, reviewed yearly | Controls that keep risk inside appetite |
| Approval of major programmes, one stage at a time | A business case with a low case, kill criteria and the next stage's cost only | Spending inside an approved stage |
| Continuing, rescoping or stopping a major programme at a gate | The forecast to finish at 85% confidence and the value still to come; money already spent is not an input | Day-to-day re-planning inside tolerance |
| Acceptance of a risk outside appetite | The options, the cost of reducing it, a named owner and an expiry date | Risks inside appetite |
| Appointing, setting objectives for and reviewing the technology leader | The ten [questions](../templates/leaders/questions-for-your-technology-leader.md) and 4 quarters of trends | Building the team below |

A decision paper to the board states the ask in one sentence, at least two options including "do nothing", the recommendation, the cost of the next stage only, the stop conditions, the risk if not approved, and the date by which a decision is needed. If any of these is missing, send it back.

## How to report bad news

1. **Early.** Tell the CEO within 24 hours of a material incident or a programme going off track. Do not wait for the next meeting. Agree in advance, in writing, when the chair or the audit committee chair is told directly.
2. **In the same format.** A red status in the scorecard, not a separate slide that looks like an excuse.
3. **Facts, impact, actions, asks.** What happened, what it means for the business, what you are doing with dates, and what you need from the board.
4. **Own it.** Say what you could have done differently. Do not name individuals.
5. **Follow up.** Report progress on the actions at every meeting until they close.

## Listed companies

If the company is listed, add three things to the reporting rhythm. Agree each with the general counsel and the company secretary.

- **Disclosure clocks.** A material incident can start a market disclosure duty. In the US, SEC Form 8-K Item 1.05 requires disclosure within four business days of determining that a cybersecurity incident is material. In the EU, the Market Abuse Regulation (Article 17) requires inside information to be disclosed as soon as possible. Write down who runs the materiality assessment, how fast, and how the time of the decision is recorded. See [crisis leadership](crisis-leadership.md).
- **Internal controls declaration.** Under the UK Corporate Governance Code 2024, Provision 29, the board declares in the annual report whether its material controls were effective, for financial years beginning on or after 1 January 2026. Agree with the audit committee which technology controls count as material (access to financial systems, change control, backup and recovery are common) and report on them each quarter.
- **Annual report.** Cyber risk and major technology programmes appear in the principal risks section. Use the same wording and numbers as the scorecard.

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
| Delivery metrics on the board scorecard | Keep DORA metrics in the executive committee pack |
| Only green | A report that is always green is not believed. Show the reds and the plan. |
| Jargon | Test the page on a non-technical colleague before it goes out |
| No ask | End with the decision or guidance you need, or say "for information only" |
| Whole programme approved in one vote | Ask for the next stage only, with kill criteria agreed now |
| The board hears of a material incident from the press | Agree the escalation thresholds with the chair in advance |
| Different numbers from the finance or risk reports | Agree sources with finance and risk before the meeting |

## Templates

- [Board engineering report](../templates/leaders/board-engineering-report.md)
- [Quarterly engineering review](../templates/leaders/quarterly-engineering-review.md)
- [Risk register](../templates/strategy/risk-register.csv)
- [Business case](../templates/strategy/business-case.md)

## Sources

- UK DSIT and NCSC, Cyber Governance Code of Practice, April 2025: https://www.gov.uk/government/publications/cyber-governance-code-of-practice
- UK NCSC, Board Toolkit: https://www.ncsc.gov.uk/collection/board-toolkit
- US SEC, Form 8-K Item 1.05, Material Cybersecurity Incidents (final rule, 2023): https://www.sec.gov/rules-regulations/2023/07/s7-09-22
- Regulation (EU) No 596/2014 (Market Abuse Regulation), Article 17: https://eur-lex.europa.eu/eli/reg/2014/596/oj
- Financial Reporting Council, UK Corporate Governance Code 2024: https://www.frc.org.uk/library/standards-codes-policy/corporate-governance/uk-corporate-governance-code/
- ISO/IEC 38500:2024, Governance of IT for the organization: https://www.iso.org/standard/81684.html
- DORA software delivery metrics: https://dora.dev/guides/dora-metrics-four-keys/
- Google SRE book, service level objectives: https://sre.google/sre-book/service-level-objectives/
- NIST AI Risk Management Framework: https://www.nist.gov/itl/ai-risk-management-framework
