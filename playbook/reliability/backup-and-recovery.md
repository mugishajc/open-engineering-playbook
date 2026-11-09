# Backup and recovery

Set a recovery point objective (RPO) and recovery time objective (RTO) for every service by tier, keep three copies of data with one that attackers cannot change or delete, and prove each backup by restoring it on a schedule. A backup that has never been restored is a hope, not a control. Ransomware groups now target backups first, so the copy you rely on must sit outside the trust domain of your production administrators.

## Outcomes

Starting points. Tune them to your data and obligations.

- Every data store has an owner, a tier, an RPO and an RTO written in the service catalogue.
- 100% of Tier 1 data stores have an automated restore test at least monthly, and a full restore exercise at least quarterly.
- Measured restore time is at or below the RTO in the last test for every Tier 1 store.
- At least one copy of every Tier 1 and Tier 2 backup is immutable or offline, with retention of at least 30 days.
- A disaster recovery exercise runs at least once a year for Tier 1 services, with a written report.

## Targets by tier

Tiers are defined in [production readiness](production-readiness.md). These targets are starting points; set yours from the cost of losing data and time.

| Tier | RPO (data you can lose) | RTO (time to restore service) | Restore test | Immutable copy retention |
|---|---|---|---|---|
| Tier 1 | 15 minutes | 1 hour | Automated monthly; full exercise quarterly | 30 days or more |
| Tier 2 | 4 hours | 8 hours | Quarterly | 30 days |
| Tier 3 | 24 hours | 72 hours | Yearly | 14 days |

An RPO under 15 minutes usually needs continuous replication or point-in-time recovery (database write-ahead log archiving), not periodic snapshots. Replication is not a backup: it copies deletions and encryption too.

## Practice

### Foundation

1. **List what to back up.** Databases, object storage and file shares, plus the things people forget: infrastructure-as-code state, secrets manager data, CI configuration, container registry contents, DNS zones, identity provider configuration and the git server itself.
2. **3-2-1.** Three copies of the data, on two different storage systems, with one copy off-site (another region, another provider or another building).
3. **Automate** backups. A backup that depends on a person remembering does not happen in the week it matters.
4. **Encrypt** backups, and store the keys separately from the backups. Losing the key is the same as losing the data, so keep a recovery copy of the key in escrow.
5. **Restore once now.** Pick the most important database and restore it to a scratch environment. Write down how long it took and what went wrong.

### Standard

1. **One immutable or offline copy.** Use object lock in compliance mode (for example S3 Object Lock or an S3-compatible store that supports it), write-once storage, or tape held offline. Nobody, including administrators, can shorten its retention.
2. **Separate the backup trust domain.** Backups live in a separate cloud account, subscription or storage system, with separate credentials and MFA. Production administrators cannot delete them. Backup administrators cannot change production.
3. **Automated restore tests.** A scheduled job restores the latest backup to an isolated environment, runs integrity checks (row counts, checksums, a sample query), records the duration and alerts on failure. Untested backups do not count towards your RPO.
4. **Point-in-time recovery** for Tier 1 databases (for example PostgreSQL WAL archiving with a tool such as pgBackRest, or the managed database's built-in feature).
5. **Retention.** Keep daily backups for 30 days and monthly backups for 12 months as a starting point. Attackers often stay unnoticed for weeks, so a 7-day retention can mean every backup is already compromised.
6. **Disaster recovery exercises.** Once a year, recover a Tier 1 service in another region or site from backups alone, using only the runbook. Twice a year, run a 2-hour tabletop exercise: "the primary site is gone; what do we do?"
7. **Monitor backups.** Alert when a backup job fails, when a backup is smaller than expected by more than 20%, or when no successful backup exists within the RPO.

### Assured

Everything in Standard, plus:

1. **Business continuity link.** RPO and RTO come from a business impact analysis signed by the business owner, not chosen by engineers alone.
2. **Evidence.** Keep backup job logs, restore test results and DR exercise reports for at least 12 months (starting point). They support ISO/IEC 27001:2022 controls 8.13 (information backup), 8.14 (redundancy), 5.29 (information security during disruption) and 5.30 (ICT readiness for business continuity), and SOC 2 availability criteria A1.2 and A1.3.
3. **Regulated finance.** EU financial entities must meet the backup, restoration and recovery requirements of the EU Digital Operational Resilience Act (Regulation (EU) 2022/2554, Article 12), including testing.
4. **Data residency.** Off-site copies stay in permitted jurisdictions. Record where each copy lives (see [data security and privacy](../data/data-security-and-privacy.md)).
5. **Deletion obligations.** When law requires deleting personal data, document how backups are handled: usually by letting them expire on schedule and preventing restored data from coming back into use.

## Ransomware

Plan as if an attacker has domain administrator rights in production.

- The immutable copy is the one that saves you. Test that it cannot be deleted with production credentials.
- Restore into a clean, isolated environment first. Scan and check the data before reconnecting to the network, or you restore the attacker too.
- Rebuild hosts from known-good images and infrastructure-as-code, not from backups of the operating system.
- Keep offline copies of the restore runbook, credentials for the backup system and contact lists. The wiki may be encrypted.
- Practise this exact scenario in a tabletop exercise once a year. CISA's #StopRansomware guide has a response checklist.

## Cloud, on-premises and air-gapped

- **Cloud:** use a separate account or subscription for backups, with object lock and cross-region copies. Check that provider-native snapshots can be exported; snapshots locked inside one account do not meet 3-2-1.
- **On-premises:** an S3-compatible object store with object locking, tape, or a separate backup appliance with its own authentication. Keep the off-site copy in another building at least far enough away to survive the same fire or flood.
- **Air-gapped:** the isolation helps against network attacks but not against insiders or removable media. Use offline media rotated off-site under two-person control, with a logged chain of custody.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "We have replication, so we have backups" | Replication copies deletions and encryption. Keep separate, versioned backups. |
| Backups in the same account with the same admin credentials | Separate trust domain and an immutable copy. |
| Restore never tested | Automated monthly restore for Tier 1. Untested backups do not count. |
| RTO set without timing a real restore | Time the restore. If it exceeds the RTO, change the design or the RTO. |
| Backup keys stored next to the backups | Separate key storage, with an escrowed recovery copy. |
| Only databases backed up | Include IaC state, secrets, CI, registries, DNS and identity configuration. |

## Templates

- [Runbook](../../templates/docs/runbook.md): include a restore procedure section.
- [Production readiness review](../../templates/docs/production-readiness-review.md): backup and restore evidence is a launch requirement.

## Sources

- CISA, *#StopRansomware Guide*: https://www.cisa.gov/stopransomware/ransomware-guide
- NIST SP 800-34 Rev. 1, *Contingency Planning Guide for Federal Information Systems*: https://csrc.nist.gov/pubs/sp/800/34/r1/upd1/final
- ISO/IEC 27001:2022, *Information security management systems*: https://www.iso.org/standard/27001
- Regulation (EU) 2022/2554 (DORA), Article 12: https://eur-lex.europa.eu/eli/reg/2022/2554/oj
