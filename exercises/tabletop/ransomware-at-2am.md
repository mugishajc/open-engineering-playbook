# Tabletop: ransomware at 2 a.m.

Files are being encrypted across the network in the middle of a weekend night, the backups are not where everyone thought they were, and by breakfast the attackers claim to hold personal data. This scenario tests whether you can isolate fast, keep talking when chat and email are gone, restore from a copy the attacker could not reach, and meet a regulator's clock while executives ask whether to pay.

| | |
|---|---|
| Audience | On-call engineers, infrastructure and security leads, the CTO or CIO, legal or the data protection officer, communications. Executives join from T+60. |
| Time | 90 minutes (10 brief, 60 play, 20 debrief). Add 15 for the optional injects. |
| Read first | [Backup and recovery](../../playbook/reliability/backup-and-recovery.md), [incident management](../../playbook/reliability/incident-management.md), [crisis leadership](../../leaders/crisis-leadership.md) |
| Facilitator notes | [Facilitator guide](facilitator-guide.md) |

## Setup

The organisation is a regional logistics company: 900 staff, 14 warehouses, about 1,100 deliveries a day, and an engineering and IT team of 25. Its warehouse management system runs on a virtualisation cluster in its own data centre. Staff sign in to email, chat and the wiki through one directory service. Backups go nightly to a backup server in the same data centre, and the warehouse database is also copied to a cloud storage account with a 30-day object lock. The last restore test from that cloud copy was 7 months ago.

It is Saturday. The on-call engineer is Daniel. The head of infrastructure, Grace, is at a wedding two hours' drive away. All organisations, people and numbers here are fictional.

## Injects

### T+0 (02:07): the first call

The night supervisor at the largest warehouse phones the IT on-call number. Handheld scanners cannot reach the warehouse system. On the office PC, every file on the shared drive ends in `.lck` and a text file called `RESTORE-FILES.txt` sits in every folder. Monitoring shows disk activity on the file server at 100% for the last 40 minutes.

**Decide:**
- Is this an incident? What severity? Who is incident commander?
- What do you isolate first, and who has the authority to pull network connections at 02:10 on a Saturday?
- Do you shut machines down or leave them running? (Evidence in memory is lost on shutdown.)

### T+15 (02:22): the directory is gone

Daniel cannot sign in to chat or email. The directory servers are encrypted. The wiki with the runbooks sat behind the same sign-in. Grace's phone goes to voicemail.

**Decide:**
- Where does the response team talk now? Who has the phone numbers?
- Who is the incident commander while Grace is unreachable? Is that written down anywhere?
- Do you have an offline copy of the runbook and the escalation list?

### T+30 (02:37): the backups

Daniel reaches the backup server. Its repository is encrypted too: the backup console used a directory account with administrator rights. The cloud copy of the warehouse database shows a successful upload at 01:00, before the encryption started. Nobody on the call has the credentials for the cloud backup account. The shared drives, the HR system and the directory itself were never copied to the cloud.

**Decide:**
- What can you restore, from where, and in what order?
- Someone suggests restoring the directory servers from last night's local snapshot to "get everyone back online". Do you?
- Who must approve a restore into production during an active attack?

### T+60 (03:07): the ransom note

Security reads `RESTORE-FILES.txt`. The attackers demand payment within 48 hours. They claim to have copied 380 GB, including payroll records for all 900 staff and customer delivery addresses, and they post a sample file list on a leak site.

**Decide:**
- Is this now a personal data breach? When did the regulator's clock start? (Under GDPR Article 33 it is 72 hours from becoming aware.)
- Who wakes the CEO, the data protection officer, legal and the cyber insurer? Who calls law enforcement?
- Who decides whether to engage with the attackers, and on what advice? (The UK NCSC and US CISA advise against paying. Payment may also breach sanctions rules; the US Treasury OFAC published an advisory on this in 2021. Take legal advice.)

### T+120 (04:07): the restore estimate

The engineer restoring the warehouse database into a clean, isolated network reports progress. At the current rate, the restore takes 11 hours. The documented RTO for this system is 1 hour. Three large retail customers need deliveries loaded by Monday 06:00.

**Decide:**
- Do you restore to the clean network, or speed it up by restoring onto existing (possibly infected) hosts?
- Can the warehouses work on paper for 24 hours? Who decides?
- What do you tell the three customers, and when?

### T+240 (06:07): the journalist

A reporter from the regional newspaper calls the main switchboard. Drivers are posting photos of trucks waiting at the gates. She asks: "Is it a cyber attack? Has customer data been stolen? Are you paying?" She publishes at 08:00 with or without a comment.

**Decide:**
- Who speaks for the company? What do you say, and what do you not say?
- Do staff know what to say if a driver or customer asks them?

### Optional injects

- **T+45:** An engineer finds the attackers' first sign-in: a contractor's VPN account, 19 days ago. Every backup on the local server is inside that window.
- **T+150:** The cloud backup account's administrator password is in a password file on the encrypted shared drive.
- **T+180:** The insurer's response firm asks you not to rebuild anything until they have imaged the disks.

## Discussion questions

1. How long would it take your organisation to reach the person who can approve disconnecting the whole network?
2. Which of your backups could an attacker with domain administrator rights delete today?
3. When did you last time a full restore of your most important system? Did it meet the RTO?
4. Who in your organisation decides on paying a ransom? Is that written down before the day?
5. Which systems do you rebuild from clean images and infrastructure as code, and which only from backups?

## What good looks like

- SEV1 declared within 15 minutes, with a named incident commander and a deputy when the first choice is unreachable ([incident management](../../playbook/reliability/incident-management.md)).
- An out-of-band channel and an offline escalation list that do not depend on the directory, chat or email ([incident management: cloud, on-premises and air-gapped](../../playbook/reliability/incident-management.md#cloud-on-premises-and-air-gapped)).
- Affected segments isolated, and evidence preserved (disk snapshots, memory where possible) before rebuilding.
- Restore from the immutable copy into a clean, isolated environment; hosts rebuilt from known-good images, not from operating system backups ([backup and recovery: ransomware](../../playbook/reliability/backup-and-recovery.md#ransomware)).
- Legal or the data protection officer told within 1 hour of suspecting personal data impact; the 72-hour clock tracked from awareness.
- The ransom decision taken by the executive team on legal advice, not by the incident commander at 03:00 ([crisis leadership](../../leaders/crisis-leadership.md)).
- Customer and press messages from pre-approved wording, with the time of the next update ([incident update template](../../templates/docs/incident-update.md)).

## Scoring rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Declaration and command | No clear commander by T+30 | Commander named, no deputy or handover | SEV1 and commander by T+15, deputy named, handover logged |
| Containment | Systems left connected past T+30 | Partial isolation, evidence lost | Segments isolated early, evidence preserved first |
| Communication channel | Team lost contact | Ad hoc phone calls | Pre-agreed out-of-band channel and offline contact list used |
| Recovery | Restored onto possibly infected hosts | Clean restore planned but order unclear | Clean environment, immutable copy, restore order by business priority |
| Regulatory and legal | Personal data impact not raised | Raised after T+120 | Legal and DPO told within 1 hour, clock recorded from awareness |
| External communication | Journalist got "no comment" or a guess | Holding statement improvised | Pre-approved statement, one spokesperson, staff briefed |

Maximum 12.

## Follow-up actions

- Move at least one copy of every Tier 1 and Tier 2 data store to immutable storage in a separate trust domain, and test that production credentials cannot delete it ([backup and recovery](../../playbook/reliability/backup-and-recovery.md)).
- Time a full restore of the most important system this month. If it misses the RTO, change the design or the RTO.
- Print and store an offline escalation list, restore runbook and backup credentials under two-person control.
- Agree in advance who decides on ransom engagement and which legal advisers to call.
- Draft holding statements for press, customers and staff, and get them approved now.
- Review contractor and VPN accounts against [access control](../../playbook/security/access-control.md): MFA, expiry and least privilege.
