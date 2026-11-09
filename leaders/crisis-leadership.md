# Crisis leadership

In a major incident or cyber crisis, the executive's job is not to fix the system. It is to protect the incident commander's space to work, make the business decisions only executives can make, start the regulatory clocks on time, and communicate with staff, customers, regulators and the media on a fixed schedule. Keep a written decision log from the first minute. Practise twice a year, because the first hour of a real crisis is the wrong time to learn who decides.

The technical response is run by the incident commander, using [incident management](../playbook/reliability/incident-management.md). This page covers the executive layer above it: the CTO, CIO, CISO, CEO and their crisis team.

## When to use this

- A SEV1 incident affects customers, safety, money or data, or is likely to reach the media.
- A cyber attack is suspected: ransomware, data theft, a compromised supplier or a compromised identity provider.
- A regulator, law enforcement or a journalist contacts you about an incident.
- You are planning the next crisis exercise.

## Two layers, separate roles

| | Incident commander (technical) | Executive crisis lead |
|---|---|---|
| Owns | Restoring service, technical decisions, responder coordination | Business decisions, external communication, legal and regulatory duties, resources |
| Decides | Rollback, failover, which fix to try | Take services offline, notify regulators, engage outside responders, approve customer messages, ransom questions |
| Talks to | Responders, the executive liaison | Board, staff, customers, regulators, media, insurers, law enforcement |
| Must not | Brief the board directly during the incident | Join the technical bridge to ask for updates or direct the fix |

Appoint one executive liaison who sits on the technical bridge and carries information both ways. Executives get updates from the liaison on the schedule below, not by calling engineers.

## First hour checklist

Times are from the moment the crisis team is called. Starting points; rehearse and tune them.

| By minute | Action | Owner |
|---|---|---|
| 0 to 10 | Confirm an incident commander is in place. Name the executive crisis lead and the executive liaison. | CTO or CIO |
| 0 to 10 | Open the decision log (template below). Record the time of awareness: regulatory clocks start from it. | Crisis lead |
| 10 to 20 | Move to the out-of-band channel if chat, email or single sign-on may be compromised. | Crisis lead, CISO |
| 10 to 20 | Call legal counsel and the data protection officer. Ask: is personal data, a regulated service or a product with digital elements involved? | Crisis lead |
| 15 to 30 | Agree the first assessment: what is affected, who is harmed, is it still spreading, is it criminal? | Crisis lead with IC via liaison |
| 20 to 30 | Decide containment trade-offs the IC cannot: take a revenue system offline, cut a supplier connection, disable customer logins. | Crisis lead, CEO for major revenue impact |
| 20 to 40 | Notify the insurer (if a cyber policy exists) and check its requirements before engaging outside responders. | Legal, finance |
| 30 to 45 | Engage outside incident response or forensic support if needed. Preserve evidence before rebuilding. | CISO |
| 30 to 60 | First internal message to all staff: what we know, what to do, what not to say, where updates will come from. | Communications |
| 30 to 60 | First holding statement for customers and the status page. | Communications, approved by crisis lead |
| 45 to 60 | Brief the CEO and the board chair. Set the update schedule. | CTO or CIO |
| By 60 | List the regulatory clocks that may apply and their deadlines. | Legal |

## Decision log

Write every executive decision as it is made: time, decision, options considered, information available, who decided, who was consulted, and when it will be reviewed. The log protects people later, because it shows what was knowable at the time (see [decision making](decision-making.md)). It is also evidence for regulators, insurers and the after-action review. Keep a copy outside the affected systems.

## Communication

| Audience | First contact | Cadence | Channel | Approves |
|---|---|---|---|---|
| Incident responders | Via liaison only | As needed | Bridge | IC |
| Executive team and board chair | Within 60 minutes | Every 2 to 4 hours during SEV1 | Out-of-band call | Crisis lead |
| All staff | Within 60 minutes | At least twice a day | A channel that works if email is down; SMS tree if needed | Crisis lead |
| Customers or citizens | Holding statement within 60 minutes | At the times promised in each update | Status page hosted apart from the product, email, account managers | Crisis lead and legal |
| Regulators | Within the legal deadline; earlier contact is usually welcomed | As agreed with the regulator | Official reporting channel | Legal, accountable executive |
| Law enforcement and national CERT or cyber security centre | As soon as crime is suspected | As agreed | Official channel | Legal, CISO |
| Media | Only through the communications lead | When there is something new to say | Statement, not interviews, in the first day | CEO and legal |
| Key suppliers and partners | When their systems or data may be affected | As needed | Named contacts | Crisis lead |

Rules for every message: say what you know, what you do not know yet, what people should do, and when the next update will come. Never guess at cause or scale. Never blame a supplier or an individual in public.

## Regulatory clocks

Clocks start when the organisation becomes aware, not when the investigation ends. The table of regimes, triggers and deadlines (GDPR and UK GDPR, the EU Cyber Resilience Act, NIS2, the EU DORA regulation and others) is in [incident management](../playbook/reliability/incident-management.md). Sector rules are in [regulated industries](../playbook/compliance/regulated-industries.md) and [public sector](../playbook/compliance/public-sector.md); personal data duties are in [data security and privacy](../playbook/data/data-security-and-privacy.md). Legal decides whether a report is required. The executive's job is to make sure legal knows within 1 hour.

## Ransomware decisions

These are executive decisions. Take legal advice before each one.

1. **Do not decide about payment in the first hours.** First contain, preserve evidence, check backups, and assess what data was taken.
2. **Know the official position.** The UK NCSC and US CISA advise against paying. Paying does not guarantee that data will be decrypted or that stolen data will be deleted.
3. **Sanctions risk.** The US Treasury's Office of Foreign Assets Control (OFAC) published an advisory in 2021 warning that facilitating ransomware payments can breach sanctions rules. Other countries have similar rules. Legal must check this before any discussion of payment.
4. **Recovery first.** The decision usually depends on whether you can restore from immutable backups (see [backup and recovery](../playbook/reliability/backup-and-recovery.md)). Know your restore time for tier 1 services before a crisis.
5. **Report.** Report to law enforcement and the national cyber security agency, and meet the regulatory clocks, whatever you decide about payment.
6. **Record the reasoning** in the decision log, including advice received.

## Crisis exercises twice a year

- **Tabletop, twice a year, 2 to 3 hours.** The executive team, communications, legal, the CISO and an incident commander. Use a realistic scenario: ransomware with data theft, a supplier compromise, a cloud region outage, a failed release that corrupts data. Alternate scenarios.
- **Inject real constraints.** Email is down. The CEO is unreachable. A journalist calls at minute 40. The regulator's deadline falls on a public holiday.
- **Test the tools.** The out-of-band channel, the offline contact list, the status page and the decision log template.
- **Measure.** Time to name the crisis lead, time to notify legal, time to first staff and customer message. Targets: 10, 20 and 60 minutes, as starting points.
- **Free material.** The UK NCSC's Exercise in a Box and CISA's tabletop exercise packages provide ready scenarios.

## After-action review

Within 10 working days of the crisis ending, hold an after-action review of the executive response, separate from the technical [postmortem](../playbook/reliability/postmortems.md). Ask, without blame: what did we expect to happen, what happened, what worked, what did not, and what will we change? Review the decision log line by line: were decisions made at the right level and at the right time, with the information available? Assign every action an owner and a date, and report progress to the board until closed.

## Common mistakes

| Mistake | Fix |
|---|---|
| Executives join the technical bridge and ask for updates | One liaison, fixed update schedule |
| No record of who decided what | Open the decision log at minute 0 |
| Legal learns on day 3 | Call legal within the first 20 minutes |
| Rebuilding hosts before preserving evidence | Snapshot and export logs first; ask outside responders |
| Communications stop because there is nothing new | Every update says when the next one will come |
| Contact list on the encrypted file server | Offline and printed copies, tested in exercises |
| Exercise findings never closed | Track them like postmortem actions, reported to the board |

## Templates

- [Crisis decision log](../templates/leaders/crisis-decision-log.md)
- [Incident update](../templates/docs/incident-update.md)
- [Postmortem](../templates/docs/postmortem.md)
- [Runbook](../templates/docs/runbook.md)

## Sources

- UK NCSC, Incident management: https://www.ncsc.gov.uk/collection/incident-management
- UK NCSC, Mitigating malware and ransomware attacks: https://www.ncsc.gov.uk/guidance/mitigating-malware-and-ransomware-attacks
- UK NCSC, Exercise in a Box: https://www.ncsc.gov.uk/information/exercise-in-a-box
- UK NCSC, Board Toolkit: https://www.ncsc.gov.uk/collection/board-toolkit
- CISA, StopRansomware: https://www.cisa.gov/stopransomware
- CISA, Tabletop Exercise Packages: https://www.cisa.gov/resources-tools/services/cisa-tabletop-exercise-packages
- US Treasury OFAC, Updated Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments, 21 September 2021: https://ofac.treasury.gov/recent-actions/20210921
- NIST SP 800-61 Rev. 3, Incident Response Recommendations and Considerations for Cybersecurity Risk Management: https://csrc.nist.gov/pubs/sp/800/61/r3/final
