# Incident management

Declare incidents early, run them with named roles, and communicate on a fixed schedule. Most of the damage in an incident comes from confusion: nobody knows who decides, customers hear nothing, and the legal team learns about a data breach days later. A small, practised process costs a few hours a quarter and cuts both the outage and the clean-up.

## Outcomes

Starting points. Tune them to your services and obligations.

- A suspected SEV1 or SEV2 is declared within 15 minutes of the first alert or report.
- Every SEV1 and SEV2 has a named incident commander within 5 minutes of declaration.
- Internal and external updates go out on the cadence in the table below in at least 90% of incidents.
- Legal or the data protection officer is told within 1 hour when an incident may involve personal data or a reportable security event.
- Every SEV1 and SEV2 has a [postmortem](postmortems.md).

## Severity levels

Pick the highest level that matches any one criterion. When unsure, choose the higher level; downgrading later is cheap.

| Level | Criteria (any one) | Who responds | Example |
|---|---|---|---|
| SEV1 | Core service down or unusable for most users. Data loss or corruption. Confirmed security breach or active exploitation. Safety, legal or regulatory impact likely. | Incident commander, operations lead, communications lead, scribe; executive informed within 30 minutes | Payments fail for all customers; ransomware detected on production hosts |
| SEV2 | Major feature broken or badly degraded for a significant share of users. SLO fast-burn alert (2% of budget in 1 hour). Suspected security incident under investigation. | Incident commander and operations lead; communications lead if customers notice | Search returns errors for one region; login takes over 30 seconds |
| SEV3 | Minor feature broken, a workaround exists, or a small number of users affected. Slow budget burn. | On-call engineer, who acts as commander | Export to CSV fails; one internal tool is down |
| SEV4 | No user impact yet: a near miss, a failed redundant component, an alert worth recording. | Owning team in working hours | One of three replicas lost; certificate expires in 7 days |

## Roles

| Role | Does | Does not |
|---|---|---|
| Incident commander (IC) | Owns the incident. Sets priorities, assigns roles, decides on mitigation (roll back, fail over, disable a feature), decides when it is over. | Debug or type commands during a SEV1. |
| Operations lead | Directs the technical work. Proposes mitigations to the IC. Coordinates the responders who change production. | Talk to customers or executives. |
| Communications lead | Writes internal and external updates on schedule. Answers stakeholders so responders are not interrupted. Brings in legal, privacy and support. | Make technical decisions. |
| Scribe | Keeps a timestamped log (UTC) of decisions, actions and findings in the incident channel or document. | Filter what is "important"; the log feeds the postmortem. |

In a small team one person can hold several roles. In a SEV1 the incident commander and the operations lead must be different people. Hand over a role explicitly ("I am handing IC to Amina; Amina, please confirm") and log it.

## Practice

### Foundation

1. Write the severity table above into your repository and agree it with the team in one meeting.
2. Create one place incidents start: a chat channel per incident (for example `#inc-2026-11-09-checkout`) or a shared document.
3. **Mitigate first, diagnose later.** The first question is "what is the fastest safe way to stop the harm?" Rolling back the last change is usually the answer; [rollbacks](rollbacks.md) gives the decision rule and time limit.
4. Keep a status page hosted outside your own infrastructure, so it stays up when you are down.
5. After the incident, write a short postmortem with the [template](../../templates/docs/postmortem.md).

### Standard

1. **Anyone can declare.** Any engineer, support agent or manager can declare an incident without permission. Declaring is never punished, even if it turns out to be nothing.
2. **Tooling.** A command or form opens the channel, pages the right rotation, starts the log and creates the postmortem stub. The [incident update template](../../templates/docs/incident-update.md) gives the wording.
3. **Communication cadence** (starting points):

   | Level | Internal update | External update (status page, key customers) |
   |---|---|---|
   | SEV1 | Every 30 minutes | Within 30 minutes of declaration, then every 60 minutes |
   | SEV2 | Every 60 minutes | Within 60 minutes if customers are affected, then every 2 hours |
   | SEV3 | At start and at resolution | Only if customers report it |
   | SEV4 | None | None |

   Every update says when the next update will come, even if nothing has changed.
4. **Incident commander rotation.** Train at least 4 people per 50 engineers as incident commanders. Run a game day or tabletop exercise every quarter.
5. **Change freeze during SEV1.** Only changes approved by the IC reach production until the incident is resolved.
6. **Close properly.** The IC declares the incident resolved, records the end time and assigns the postmortem owner before the channel goes quiet.
7. **Changes to configuration and content are changes.** The July 2024 CrowdStrike Falcon incident came from a content configuration update, not a code release, and it crashed Windows hosts worldwide. Treat feature flags, rules files and configuration pushes with the same staged rollout and fast rollback as code (see [change management](change-management.md)).

### Assured

Everything in Standard, plus:

1. **A regulatory clock checklist** that the communications lead opens at declaration. Each clock starts when the organisation becomes aware, not when the investigation ends. The legal team decides whether a report is required; the IC's job is to tell them early.

   | Regime | Who reports | What triggers it | Deadline |
   |---|---|---|---|
   | EU GDPR Art. 33 (and UK GDPR) | Data controller | Personal data breach | To the supervisory authority without undue delay and, where feasible, within 72 hours of becoming aware. Art. 34: tell affected people without undue delay when the risk to them is high. |
   | EU Cyber Resilience Act Art. 14 (Regulation (EU) 2024/2847), from 11 Sep 2026 | Manufacturers of products with digital elements | Actively exploited vulnerability, or severe incident affecting the security of the product | Early warning within 24 hours; notification within 72 hours; final report within 14 days of a fix being available (vulnerability) or within 1 month (severe incident). Submitted through the single reporting platform run by ENISA. |
   | EU NIS2 Directive Art. 23 ((EU) 2022/2555) | Essential and important entities, as defined in national law | Significant incident | Early warning within 24 hours; incident notification within 72 hours; final report within 1 month. National laws add detail. |
   | EU DORA (Regulation (EU) 2022/2554) | EU financial entities | Major ICT-related incident | Its own classification criteria and deadlines, set in technical standards under Art. 20: initial notification within 4 hours of classifying the incident as major and no later than 24 hours after becoming aware of it; intermediate report within 72 hours; final report within 1 month. Confirm current timelines with your compliance team. |
   | Other data protection laws | Varies | Personal data breach | Many laws have their own clocks, for example Kenya, Nigeria, Brazil and India. List the ones that apply to you, with deadlines, in this checklist. |

   This table is not legal advice. Check the current text of each law.
2. **Evidence.** Keep the incident log, chat export, timeline and decisions for the retention period your regulator or auditor requires. This supports ISO/IEC 27001:2022 controls 5.24 to 5.28 and SOC 2 CC7.3 to CC7.5.
3. **Security incidents have a parallel track.** Preserve evidence before rebuilding hosts (snapshot disks, export logs). Bring in the security lead as a co-commander. NIST SP 800-61 Rev. 3 describes the security incident response process in CSF 2.0 terms.
4. **Customer notification approvals.** Pre-approve wording for common cases so the communications lead does not wait for sign-off during a SEV1.

## In the AI era

AI assistants can save responders time during an incident. They can also act fast on a wrong idea. Give them the scribe's and researcher's jobs, not the operator's.

- **Good uses.** Summarise the incident channel for someone joining late. Draft the next status update for the communications lead to edit. Search logs, traces, recent deployments, past postmortems and runbooks, and show the sources it used. Build the first draft of the postmortem timeline from the log.
- **Read-only by default.** The assistant's credentials can read telemetry, tickets and documents. They cannot change production, configuration, flags or access.
- **A human approves every action.** If an assistant proposes a command, rollback or flag change, a named responder reads it, decides and runs it. The scribe logs it as that person's action. The incident commander's authority does not move to a tool.
- **Treat output as a lead, not a finding.** Check every claimed cause against the evidence it cites before acting. A fluent summary can be wrong.
- **Mind the data.** Incident channels hold customer data, secrets pasted by mistake and security details. Use only assistants approved for that data class (see [code assistants](../people/code-assistants.md)), and keep a security incident's details out of any tool outside your control.
- **AI features fail too.** When an AI feature itself misbehaves (harmful output, data leak, runaway cost), the fastest mitigation is usually its kill switch or a rollback to the previous prompt or model version. See [release management](../delivery/release-management.md#in-the-ai-era), [AI engineering practices](../ai/ai-engineering-practices.md) and [AI architecture patterns](../ai/ai-architecture-patterns.md).

## Cloud, on-premises and air-gapped

- **Out-of-band channel.** If chat, email or single sign-on runs on the affected infrastructure, you lose them in the incident. Keep a second channel that does not depend on them (a phone bridge, a separate messaging tenant) and test it in every game day.
- **Offline contact list.** Keep a printed or offline copy of the escalation list and the regulator contact details.
- **Runbooks reachable without the network.** In air-gapped environments, keep runbooks in the same isolated network and mirror them to a laptop that responders can use from outside.
- **Vendor support.** For on-premises products, know the support contract number and escalation path before you need it.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Waiting to be sure before declaring | Declare at "probably". Downgrade later. |
| The most senior engineer acts as IC and debugs at the same time | Split the roles. The IC coordinates; others type. |
| Silence on the status page while engineers investigate | Post within 30 minutes for SEV1, and give the time of the next update. |
| Legal learns about a breach on day 4 | Notify legal or the DPO within 1 hour of suspecting personal data impact. The 72-hour clock has already started. |
| Status page hosted on the same cluster as the product | Host it with a separate provider or on separate infrastructure. |
| Rollback impossible because a schema change went out with the code | Separate schema changes from code changes. See [database changes](../delivery/database-changes.md). |

## Templates

- [Incident update](../../templates/docs/incident-update.md): internal and external wording by stage.
- [Postmortem](../../templates/docs/postmortem.md), with [root cause analysis](root-cause-analysis.md) for the analysis itself
- [Runbook](../../templates/docs/runbook.md)

## Sources

- Google, *Site Reliability Engineering*, "Managing Incidents": https://sre.google/sre-book/managing-incidents/
- Google, *The Site Reliability Workbook*, "Incident Response": https://sre.google/workbook/incident-response/
- NIST SP 800-61 Rev. 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management*: https://csrc.nist.gov/pubs/sp/800/61/r3/final
- Regulation (EU) 2016/679 (GDPR), Articles 33 and 34: https://eur-lex.europa.eu/eli/reg/2016/679/oj
- Regulation (EU) 2024/2847 (Cyber Resilience Act), Article 14: https://eur-lex.europa.eu/eli/reg/2024/2847/oj
- European Commission, Cyber Resilience Act overview: https://digital-strategy.ec.europa.eu/en/policies/cyber-resilience-act
- Directive (EU) 2022/2555 (NIS2), Article 23: https://eur-lex.europa.eu/eli/dir/2022/2555/oj
- Regulation (EU) 2022/2554 (DORA): https://eur-lex.europa.eu/eli/reg/2022/2554/oj
- CrowdStrike, preliminary post-incident review of the 19 July 2024 content update: https://www.crowdstrike.com/en-us/blog/falcon-content-update-preliminary-post-incident-report/
