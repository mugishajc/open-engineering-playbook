# SME profile

For small and medium businesses that use software but do not build it. Put the essential security controls in place in the first week. Get your data, suppliers and backups under control in the first quarter. Then run a one-page IT plan each year. Most practice areas in this playbook are for organisations with their own engineers, so this profile skips them until you have some. The leadership view is in [for small and medium businesses](../leaders/for-small-and-medium-businesses.md).

## Who this is for

- Clinics, schools, law and accounting firms, shops, logistics firms, hotels, manufacturers, cooperatives and NGOs.
- No in-house software developers. One IT person, an outside IT provider, or the owner doing it alone.
- Business systems are bought as online subscriptions or packaged software: email, accounting, payroll, booking, stock control, practice management.
- If you start to employ developers or commission custom software, move to the [solo](solo.md) or [startup](startup.md) profile for that work and keep this one for the rest of the business.
- If a regulator inspects how you handle data or systems (health, financial services, telecoms), also read the short [SME section of the regulated overlay](regulated.md#with-the-sme-profile). Do not try to apply the whole overlay.

## How to use this page if you are not technical

You decide and check; your IT person or provider does the technical work. For each row below, ask them to do it and to show you proof: a short report from the admin console, a demonstration, or a screenshot with the date showing. The "Read" column points first to the plain-language page for owners. Links marked "for your IT person" go to the detailed practice pages.

The rows in each table are in order: the first row removes the most risk for the least effort.

## Target level by area

| Area | Target | Go higher early when |
|---|---|---|
| Strategy | Foundation (one-page yearly IT plan) | You are choosing a core system that will run the business for years |
| Operating model | Foundation (who owns IT decisions, written down) | You have more than one IT person or provider |
| Product | Skip | You sell your own software or digital service |
| Project management | Foundation (a one-page plan before a big IT change) | You replace a core system or change IT provider |
| Ways of working | Skip | You employ developers |
| Delivery | Skip | You employ developers or commission custom software |
| Quality | Skip | You commission custom software; then require tests in the contract |
| Reliability | Foundation (backups and restore tests, incident plan) | Downtime of one system stops all trading |
| Security | Foundation (the essential controls) | A customer, insurer or public contract asks for a certification |
| Data | Foundation (data list, classification, retention) | You hold health, children's or financial data |
| AI | Foundation (rules for staff use of AI tools) | An AI tool makes or supports decisions about customers or staff |
| Architecture | Skip | You commission or integrate several systems |
| Platform | Skip | You employ developers |
| People | Foundation (onboarding and leavers process for accounts) | You hire IT staff |
| Measurement | Skip | You employ developers |
| Compliance | Foundation (data protection duties, supplier contracts) | A regulator or large customer audits you |

## Week 1

| Do this | Read | Template |
|---|---|---|
| Turn on multi-factor authentication for email, banking, accounting and every admin account; start with email | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls) | |
| Check backups exist for files, email and key systems, and that one copy is offline or cannot be deleted | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls); for your IT person: [backup and recovery](../playbook/reliability/backup-and-recovery.md) | |
| Turn on automatic updates on every computer and phone; list devices that no longer get updates | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls) | |
| Make sure the business, not a person or provider, owns the domain name, email admin account and backups | [Managing an outside IT provider](../leaders/for-small-and-medium-businesses.md#managing-an-outside-it-provider) | |
| Print the first-hour incident plan and fill in the emergency contacts | [The first hour of an incident](../leaders/for-small-and-medium-businesses.md#the-first-hour-of-an-incident) | [first-hour-plan.md](../templates/sme/first-hour-plan.md) |

## Month 1

| Do this | Read | Template |
|---|---|---|
| Test a restore of one folder and one key system; write down how long it took | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls); for your IT person: [backup and recovery](../playbook/reliability/backup-and-recovery.md) | |
| Give staff a business password manager; move shared passwords into it | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls) | |
| Give admins separate admin accounts; remove admin rights from daily accounts | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls); for your IT person: [access control](../playbook/security/access-control.md) | |
| Turn on device encryption and remote wipe for laptops and phones | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls) | |
| Set up email filtering and SPF, DKIM and DMARC records for your domain; change the router's factory password | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls) | |
| List every online service the business uses, with owner, data held, cost and renewal date | [Choosing and leaving software subscriptions](../leaders/for-small-and-medium-businesses.md#choosing-and-leaving-software-subscriptions) | [online-services.csv](../templates/sme/online-services.csv) |
| Write a leavers process: all access removed on the last working day | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls) | |
| Write a one-page downtime procedure: how you keep seeing patients, teaching or taking payment with no computers | [The first hour of an incident](../leaders/for-small-and-medium-businesses.md#the-first-hour-of-an-incident) | [first-hour-plan.md](../templates/sme/first-hour-plan.md) |

## Quarter 1

| Do this | Read | Template |
|---|---|---|
| Review the IT provider contract for ownership, access, backups, incident notice and exit | [Managing an outside IT provider](../leaders/for-small-and-medium-businesses.md#managing-an-outside-it-provider) | |
| Record what personal data you hold, why, where and for how long; publish a privacy notice | [Data protection duties](../leaders/for-small-and-medium-businesses.md#data-protection-duties) | [data-classification.md](../templates/docs/data-classification.md) |
| Agree with staff which AI tools they may use and what data must never go into them | [Data protection duties](../leaders/for-small-and-medium-businesses.md#data-protection-duties) | [staff-ai-use-policy.md](../templates/sme/staff-ai-use-policy.md) |
| Send the vendor questionnaire to services that hold personal or financial data | [Choosing and leaving software subscriptions](../leaders/for-small-and-medium-businesses.md#choosing-and-leaving-software-subscriptions) | [vendor-risk-questionnaire.md](../templates/docs/vendor-risk-questionnaire.md) |
| Write down your top five IT risks with an owner each, for example "we lose all patient records" or "our only IT person leaves" | No reading needed | [risk-register.csv](../templates/strategy/risk-register.csv) |
| Run a 30-minute phishing and password session for all staff | [A simple yearly IT plan](../leaders/for-small-and-medium-businesses.md#a-simple-yearly-it-plan-and-budget) | |

## Year 1

| Do this | Read | Template |
|---|---|---|
| Write a one-page IT plan and budget; review it once a year | [A simple yearly IT plan](../leaders/for-small-and-medium-businesses.md#a-simple-yearly-it-plan-and-budget) | |
| Test a restore every 3 months and compare the time with how long the business can cope without the system | [The essential controls](../leaders/for-small-and-medium-businesses.md#the-essential-controls) | |
| Export data from your most important service and check you can open it elsewhere | [Choosing and leaving software subscriptions](../leaders/for-small-and-medium-businesses.md#choosing-and-leaving-software-subscriptions) | |
| Ask your IT provider or IT person the eight yearly questions, and record the answers | [Questions to ask your IT provider](../leaders/for-small-and-medium-businesses.md#questions-to-ask-your-it-provider-every-year) | [it-provider-questions.md](../templates/sme/it-provider-questions.md) |
| Rehearse the first-hour incident plan with the people named in it, for 30 minutes: "our files are encrypted, what do we do?" | [The first hour of an incident](../leaders/for-small-and-medium-businesses.md#the-first-hour-of-an-incident) | |
| Gain a recognised certification if customers, insurers or public contracts ask for one (for example UK Cyber Essentials) | [Recognised schemes](../leaders/for-small-and-medium-businesses.md#how-these-map-to-recognised-schemes) | |
| Before you replace a system or change IT provider, write a one-page plan: an owner, a date range, a tested way back to the old way, and what would make you stop | [Projects and products](../playbook/project-management/projects-and-products.md#foundation) | [project-charter.md](../templates/project/project-charter.md) |
| Replace devices that will stop getting security updates in the next year | [A simple yearly IT plan](../leaders/for-small-and-medium-businesses.md#a-simple-yearly-it-plan-and-budget) | |

## Skip at this size

| Skip | Why | Revisit when |
|---|---|---|
| Delivery, quality, platform and architecture pages | They are for teams that write and run their own software. | You employ developers or commission custom software |
| Code review, CI and release templates | Nothing to review or release. | Same as above; then use the [startup](startup.md) profile for that work |
| Service level objectives and on-call | Your suppliers hold the service levels. Put them in the contracts. | You run a system customers use directly, around the clock |
| Change advisory board | A short note of what changed and when is enough for a small team. | A regulator requires one |
| Delivery metrics | They measure software teams. | You employ developers |
| Product management pages | They are for teams that build and sell their own software. | You sell your own software or digital service |
| Data governance roles, catalogues and data contracts | A one-page data list does the job. | Several systems share the same customer data and disagree |
| Post-quantum and zero trust programmes | Your suppliers carry most of this work. Ask them about it at renewal. | You hold data that must stay secret for 10 years or more |

## Check your progress

Most owners can skip the assessment: the five numbers below are enough. If your IT person or provider wants a fuller check, the [assessment](../assessment/README.md) has an `sme` profile. It asks 19 questions written for a business without developers, leaves out the seven areas this page marks Skip, and lists the essential controls first:

```bash
python3 assessment/assess.py --init --profile sme > my-answers.toml
python3 assessment/assess.py --answers my-answers.toml
```

Each quarter, ask your IT person or provider for these five numbers and write them in your IT plan.

| Number | Target |
|---|---|
| Share of staff accounts with multi-factor authentication | 100% |
| Devices that no longer get security updates | zero |
| Days since the last successful restore test | under 90 |
| Online services without a named owner in the business | zero |
| Leavers whose access was not removed on their last working day | zero |
