# Tabletop: the key engineer resigns

The one engineer who understands the system that matters most hands in their notice, the most important run of the year is seven weeks away, and you cannot match the offer. This scenario tests how you find key-person risk before it leaves, how much knowledge you can move in four weeks, what you do about the work only one person ever did, and what the resignation tells you about the team that stays.

| | |
|---|---|
| Audience | Engineering managers, team leads, the head of engineering, an HR partner. Optionally a senior engineer from the affected team. |
| Time | 60 minutes (10 brief, 35 play, 15 debrief) |
| Read first | [Skills gap](../../playbook/people/skills-gap.md), [knowledge sharing](../../playbook/people/knowledge-sharing.md), [sustainable pace](../../playbook/people/sustainable-pace.md), [documentation](../../playbook/people/documentation.md) |
| Facilitator notes | [Facilitator guide](facilitator-guide.md) |

## Setup

The organisation is the digital team of a national tax agency: 35 engineers, about a third of them contractors. The agency runs its services on-premises in two government data centres. Once a year, in March, a batch system calculates provisional assessments for 1.4 million taxpayers. The run takes four nights and has never been done without Joseph, a senior engineer with 11 years at the agency.

Joseph also renews the certificates for the online filing portal each year, by a manual process on a hardware security module, and runs the transfer of updates into the agency's isolated network. It is Monday, 20 January. The batch run starts on 10 March. All organisations, people and numbers here are fictional.

## Injects

### T+0 (Monday 09:00): the letter

Joseph hands his manager, Esther, a resignation letter. He has accepted an offer from a bank at about twice his civil service salary. His notice period is 20 working days; his last day is Friday 14 February. He is polite, tired and clear that he will not stay.

**Decide:**
- Who needs to know today, and who must not hear it from the corridor?
- What do you ask Joseph in the next conversation, and what do you avoid asking?
- What is the first thing you write down?

### T+15 (09:15): how deep is the hole?

Esther asks the team lead for a list of what only Joseph can do. In 15 minutes they find six items: the March batch run, the batch's error recovery, the certificate renewal, the isolated network transfer, the database tuning for the batch, and the relationship with the batch system's original supplier. Nobody has a skills matrix. Two of the six have runbooks; both are four years old.

**Decide:**
- Rank the six by risk and by date. Which must move before 14 February, and which can wait for a hire?
- Who are the two people (at least) who will learn each item? What do they stop doing to make room?
- Where does this go: team backlog, risk register, or both?

### T+30 (09:30): the certificate and the counter-offer

The certificate for the online filing portal expires on 12 February, two days before Joseph leaves. Last year's renewal took him a full day and needed two officials with smart cards present. HR confirms that pay above the band needs ministry approval, which takes about six weeks. Someone suggests hiring Joseph back as a consultant through a framework contract after he leaves.

**Decide:**
- Who does the certificate renewal, and when? Who watches and who types?
- Do you try to retain him, and with what? Is a consultancy contract allowed, and does it fix the problem or hide it?
- What do you tell the director-general about the March run?

### T+60 (10:00): what the exit interview reveals

In a one-to-one, Joseph says he has been the only person on call for the batch for four years, has not taken more than three days of leave in a row since 2022, and asked twice for someone to learn the system with him. Later that morning, two other senior engineers tell their team lead they are "also looking".

**Decide:**
- Is this a single resignation or a signal? What do you check?
- What changes for on-call and leave this week, not next quarter?
- How do you talk to the rest of the team about Joseph leaving?

### Optional injects

- **T+20:** Joseph has 8 days of unused leave and asks to take them in his notice period.
- **T+40:** The original supplier of the batch system says its last engineer who knew this version retired in 2024.
- **T+50:** Joseph's personal account turns out to be the administrator on the HSM management console and on the transfer workstation.

## Discussion questions

1. For your three most critical systems, who can operate and change each one unaided? Is it ever only one person?
2. When did a critical once-a-year task last run with someone other than the usual person watching, then doing?
3. Which administrator accounts belong to a person rather than a role or a team?
4. What does your on-call and leave data say about who carries the load?
5. If your best engineer resigned tomorrow, what would their exit interview say?

## What good looks like

- A team skills matrix that showed a bus factor of 1 long before the letter, with key-person risk in the risk register ([skills gap](../../playbook/people/skills-gap.md)).
- Knowledge transfer by pairing on the real work: the new owners do the certificate renewal with Joseph watching, not the other way round ([knowledge sharing](../../playbook/people/knowledge-sharing.md)).
- Runbooks written by the learners, reviewed by Joseph, tested by someone who was not in the room ([documentation](../../playbook/people/documentation.md), [runbook template](../../templates/docs/runbook.md)).
- A rehearsal of the batch run on production-sized data before 10 March, with the supplier on standby.
- Personal administrator accounts replaced by role accounts; Joseph's access removed on his last day ([access control](../../playbook/security/access-control.md)).
- On-call load and leave spread now, and a career path for the engineers who stay ([sustainable pace](../../playbook/people/sustainable-pace.md), [career framework](../../playbook/people/career-framework.md)).
- A consultancy contract, if used, has a defined handover goal and an end date, not an open-ended dependency.

## Scoring rubric

| Criterion | 0 | 1 | 2 |
|---|---|---|---|
| Risk identification | No list by T+30 | List made, not ranked | Ranked by risk and date, recorded in the risk register |
| Transfer plan | "Ask Joseph to write it all down" | Pairing planned without freeing time | Named learners, time freed, learners do the work |
| Certificate renewal | Left to Joseph alone | Done together, not documented | New owners renew with Joseph watching; runbook updated |
| Access and accounts | Not considered | Removed on last day only | Personal admin accounts converted to role accounts before he leaves |
| Retention and signal | Ignored the other two engineers | Counter-offer only | Load, leave and growth addressed for the team that stays |

Maximum 10.

## Follow-up actions

- Build a team skills matrix for every critical system this quarter and record any bus factor below 2 in the [risk register](../../templates/strategy/risk-register.csv).
- Rotate every once-a-year task: the next run is done by someone who did not do the last one, with the previous owner watching.
- Replace personal administrator accounts with role accounts and break-glass procedures.
- Review on-call and leave data each quarter for people carrying more than their share.
- Add "who else can do this?" to the [onboarding checklist](../../templates/docs/onboarding-checklist.md) and to every [production readiness review](../../templates/docs/production-readiness-review.md).
