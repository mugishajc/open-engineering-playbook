# For small and medium businesses

Put a small number of security controls in place first, because they block the most common attacks and cost little: multi-factor sign-in on every account, automatic updates, backups with one copy kept offline and a restore you have tested, separate admin accounts, encrypted devices, a password manager and protected email. Then manage your software subscriptions and your IT provider with the same care as any other supplier you could not trade without. Most of the rest of this playbook is for organisations that build software; you can skip it until you do.

## When to use this

This page is for owners, managing directors and office or IT managers of clinics, schools, law and accounting firms, shops, logistics firms, hotels, manufacturers, cooperatives and NGOs. You probably have one IT person, or an outside IT provider, or both.

- You do not know whether your business could survive losing its computers or data for a week.
- Your IT provider has the keys to everything and you have never read the contract.
- Staff use many online tools and nobody has a list.
- You hold customer, patient, student or member data and are unsure what the law requires.

The [SME profile](../profiles/sme.md) turns this page into a week 1 to year 1 plan.

## The essential controls

Do these first. Each one is cheap compared with a single bad week.

You do not need to do the technical steps yourself. Give this table to your IT person or provider, and ask for proof of each item in the "Check it by" column: a screenshot, a report or a demonstration. Ask again every 3 months.

| Control | What to do (starting point) | Check it by |
|---|---|---|
| Multi-factor authentication (MFA) | turn it on for email, banking, accounting, cloud storage, remote access and every admin account; prefer an app or security key over SMS | 100% of staff accounts on the email system show MFA enabled |
| Automatic updates | turn on automatic updates for operating systems, browsers and office software; replace devices that no longer get security updates | no device running an unsupported operating system |
| Backups with an offline copy | back up business data every day; keep at least one copy offline or on storage that cannot be changed or deleted for a set period; include cloud services such as email and file sharing | a restore of a full folder and one key system tested every 3 months, with the time it took written down |
| Separate admin accounts | staff use normal accounts every day; admin rights only on separate accounts used for admin tasks; at least 2 people can reach admin access in an emergency | list of admin accounts reviewed every 3 months; no more than needed |
| Device encryption | turn on full-disk encryption on every laptop and phone that holds business data; enable remote wipe | every device in the inventory shows encryption on |
| Password manager | give every staff member a business password manager; no shared passwords in spreadsheets or chat | shared accounts stored in the manager, with access by person |
| Email security | turn on the email provider's spam and malware filtering; publish SPF, DKIM and DMARC records for your domain; train staff to report suspicious messages | DMARC set to quarantine or reject once reports show legitimate mail passes |
| Leavers process | remove access on the person's last day, including personal devices and shared passwords | access removed within 1 working day for 100% of leavers |
| Router and firewall | change the default admin password on the internet router; turn on the firewall on every computer; close remote access that nobody uses | no device or router still uses its factory password |

See [access control](../playbook/security/access-control.md), [secrets](../playbook/security/secrets.md) and [backup and recovery](../playbook/reliability/backup-and-recovery.md) for more detail.

## How these map to recognised schemes

If a customer, insurer or funder asks which standard you follow, these schemes cover the same ground. Pick the one your market recognises.

| Scheme | Who publishes it | Fit for small businesses |
|---|---|---|
| UK Cyber Essentials | UK NCSC | five technical control themes: firewalls, secure configuration, user access control, malware protection, security update management; certification available; required for some UK central government contracts |
| Cyber Essentials (US) | US CISA | a guide for leaders of small businesses and local governments, with actions for leaders and for staff |
| NIST Cybersecurity Framework 2.0 (Feb 2024) | US NIST | six functions: Govern, Identify, Protect, Detect, Respond, Recover; free Small Business Quick-Start Guides |
| SME cybersecurity guidance | ENISA (EU Agency for Cybersecurity) | guidance written for small and medium businesses in the EU |

| Essential control | UK Cyber Essentials theme | NIST CSF 2.0 function |
|---|---|---|
| MFA, separate admin accounts, leavers process, password manager | User access control | Protect |
| Automatic updates | Security update management | Protect |
| Email security, malware filtering | Malware protection | Protect, Detect |
| Device encryption, secure settings | Secure configuration | Protect |
| Router and firewall settings changed from defaults | Firewalls | Protect |
| Backups with offline copy and tested restore | outside the five themes | Recover |
| Incident first-hour plan | outside the five themes | Respond |

## Choosing and leaving software subscriptions

- Keep one list of every online service the business uses: what it is for, who owns it, what data it holds, what it costs and when it renews.
- Before you sign, check: can you export all your data in a common format (CSV, PDF, standard files)? Does it support MFA and single sign-on? Where is the data stored? What happens to your data if you stop paying?
- Prefer services where the business owns the account, not a member of staff.
- Each year, export the data from your most important service and check you could open it without that service.
- Use the [vendor risk questionnaire](../templates/docs/vendor-risk-questionnaire.md) for any service that holds personal or financial data. See [third-party and SaaS risk](../playbook/security/third-party-and-saas-risk.md).

## Managing an outside IT provider

| Topic | What the contract or agreement should say |
|---|---|
| Ownership | the business owns its accounts, domains, licences, data and passwords; the provider holds them on your behalf |
| Access | provider staff use named accounts with MFA, not one shared login; you can see who accessed what |
| Service levels | response times for urgent and normal issues; hours covered; how to escalate |
| Backups | what is backed up, how often, where, and a restore test every 3 months with a short written report to you |
| Security | which of the essential controls the provider runs, and how they report on them each month or quarter |
| Incidents | the provider tells you within a set time (for example 4 hours) if they suspect a breach, including a breach of their own systems |
| Exit | on termination, the provider hands over all admin credentials, documentation and data within a set time (for example 10 working days), and helps the next provider |

Keep a copy of the admin credentials for your email, domain name and backups in a sealed or separately stored form that the owner controls.

### Questions to ask your IT provider every year

Write the answers down and compare them with last year's. A good provider answers each one with a date, a number or a document.

1. When did you last restore our data from backup, and how long did it take?
2. Which of our accounts do not have multi-factor authentication yet?
3. Which of our devices no longer get security updates, and when will they be replaced?
4. Who on your staff can reach our systems, and how do you remove someone who leaves?
5. What security incidents or suspicious events did you see on our systems this year?
6. If we ended the contract tomorrow, how would you hand over our accounts, passwords and data, and how long would it take?
7. What would you change first if we gave you a little more budget?
8. Which of our systems depend on one person at your firm?

## Data protection duties

This is not legal advice. Most countries have a data protection law: for example the EU GDPR, UK GDPR, Kenya Data Protection Act 2019, Rwanda Law No 058/2021, Nigeria Data Protection Act 2023, Brazil LGPD, India DPDP Act 2023 or California CCPA/CPRA. Common duties:

- Know what personal data you hold, why, where and for how long. Use the [data classification template](../templates/docs/data-classification.md) as a one-page record.
- Tell people what you do with their data in a short privacy notice.
- Collect only what you need and delete it when the purpose ends.
- Register with your data protection authority if your law requires it.
- Report a personal data breach to the authority within the time your law sets. Under the GDPR, this is within 72 hours of becoming aware of it, where feasible, unless the breach is unlikely to put people at risk.
- Be careful with free AI tools: do not paste customer, patient or staff data into a service whose terms let it keep or reuse that data. See [AI governance](../playbook/ai/ai-governance.md).

See [data governance](../playbook/data/data-governance.md) for the fuller practice.

## The first hour of an incident

Print this and keep it with the emergency contact list.

| Minute | Do |
|---|---|
| 0 to 10 | Disconnect affected computers from the network (unplug the cable, turn off Wi-Fi), but do not switch them off unless your IT provider or a responder tells you to. Call your IT person or provider. |
| 10 to 20 | Name one person in charge. Start a written log: time, what was seen, what was done. |
| 20 to 40 | Change passwords for email and admin accounts from a clean device. Check the backups are safe and disconnected. |
| 40 to 60 | Call your cyber insurer if you have one, before engaging other firms. Decide who tells staff and customers, and what. Check if a data breach report to the authority is needed and when. |

If it is ransomware: national cyber agencies such as the UK NCSC and US CISA advise against paying, and payment may breach sanctions rules. Take legal advice. Report the incident to your national cyber agency or police. Use the [incident update template](../templates/docs/incident-update.md) for messages.

## A simple yearly IT plan and budget

Review once a year with your IT person or provider. Keep it to one page.

| Line | What to plan |
|---|---|
| Subscriptions and licences | the list above, with renewal dates; remove unused seats |
| Devices | replace devices before they stop getting security updates; plan a replacement cycle (for example laptops every 4 to 5 years) |
| Backups | storage cost and the quarterly restore tests |
| Security | MFA, password manager, email security, any certification you need |
| IT provider | the contract cost and service review dates |
| Training | a short session for all staff each year on phishing, passwords and reporting |
| Contingency | money set aside for an incident or urgent replacement; check your cyber insurance cover |
| One improvement | one bigger change for the year (for example moving files to a managed cloud service) |

## When to bring in specialist help

- You suspect a breach, ransomware or fraud: incident response specialists, through your insurer if you have one.
- You need a certification (for example Cyber Essentials) or a customer sends a long security questionnaire.
- You are about to build or commission your own software, website with payments, or app.
- You are choosing a core system (accounting, practice management, stock control) that will run the business for years. See [build, buy or adopt](../playbook/strategy/build-buy-adopt.md).
- You process sensitive data at scale: health, children's data, financial data.

## What you can skip

If you do not write software, skip delivery, quality, architecture, platform, the engineering parts of people and measurement, and most of the AI pages. Come back to them when you employ developers or commission custom software. The [SME profile](../profiles/sme.md) lists what to skip and when to revisit it.

## Common mistakes

| Mistake | Fix |
|---|---|
| MFA on some accounts but not email | Email resets every other password. Protect it first. |
| Backups that sit on the same network as the computers | Keep one copy offline or unchangeable, and test a restore. |
| The IT provider owns the domain name and admin accounts | Put them in the business's name and keep the credentials. |
| Everyone is an administrator on their own computer | Normal accounts for daily work; admin only when needed. |
| No list of online tools | One list, one owner per tool, reviewed yearly. |
| Paying a ransom before taking advice | Follow the first-hour plan and take legal advice. |

## Templates

- [Data classification](../templates/docs/data-classification.md)
- [Vendor risk questionnaire](../templates/docs/vendor-risk-questionnaire.md)
- [Incident update](../templates/docs/incident-update.md)
- [Questions for your technology leader](../templates/leaders/questions-for-your-technology-leader.md)
- [Risk register](../templates/strategy/risk-register.csv)

## Sources

- UK NCSC, Cyber Essentials: https://www.ncsc.gov.uk/cyberessentials/overview
- UK NCSC, Small Business Guide: https://www.ncsc.gov.uk/collection/small-business-guide
- US CISA, Cyber Essentials: https://www.cisa.gov/resources-tools/resources/cyber-essentials
- US NIST, Cybersecurity Framework 2.0 and Small Business Quick-Start Guides: https://www.nist.gov/cyberframework
- ENISA, the EU Agency for Cybersecurity: https://www.enisa.europa.eu
- Regulation (EU) 2016/679, GDPR (Article 33, breach notification): https://eur-lex.europa.eu/eli/reg/2016/679/oj
- US Treasury OFAC, Updated Advisory on Potential Sanctions Risks for Facilitating Ransomware Payments (2021): https://ofac.treasury.gov/recent-actions/20210921
