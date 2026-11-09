# Principles

Twelve principles sit under every page in this playbook. When a practice and a principle disagree, the principle wins and the practice gets fixed. When two principles pull in different directions, write down the trade-off in a decision record.

## 1. Outcomes over activity

Judge a practice by what it changes for users, operators and the business: faster recovery, fewer failed changes, lower cost, less risk. A practice that produces paperwork but no change in those numbers is a candidate for removal.

## 2. Small batches, fast feedback

Small changes are easier to review, test, ship and undo. Most delivery problems get smaller when the batch gets smaller. This holds for code, for migrations, for organisational change and for strategy.

## 3. Automate the control, keep the evidence

A control that relies on someone remembering is not a control. Put the rule in the pipeline, the repository settings or the platform, and let the system record that it ran. Auditors get better evidence and engineers get their time back.

## 4. Golden paths, not gates

Make the safe way the easy way. Teams that follow the [golden path](platform/golden-paths.md) (some call it the paved road) get speed and support for free. Teams that leave it can, but they own the extra work and write down why.

## 5. Write decisions down

Decisions that matter for more than a quarter get a short written record: the context, the options, the choice and the cost. Writing things down outlives the people who made the call and stops the same debate from happening every year.

## 6. Open standards and an exit plan

Prefer open standards, open formats and portable tools. Every major platform choice comes with a written exit plan and an estimate of what leaving would cost. This matters most for public bodies and for anyone who may have to run on-premises later.

## 7. Security is part of done

A change is not done until it is reviewed, tested, built from a known source and deployable without secrets in the code. Security work goes into the normal flow, not into a separate queue at the end.

## 8. Learn without blame

Incidents are information about the system, not verdicts on people. Postmortems look for contributing factors and fixes. People who report problems early are thanked.

## 9. Scale the practice to the context

A solo engineer and a central bank should not run the same process. The playbook gives three levels for every practice (Foundation, Standard, Assured) and profiles that pick a sensible level for you. Adopt the lowest level that controls your real risk. Levels never lower a legal duty. Records of processing, impact assessments, processor contracts, breach registers, transfer mechanisms and reporting deadlines apply from the day the law applies to you, at every level. See the [legal floor](data/data-security-and-privacy.md#legal-floor-applies-at-every-level).

## 10. The same practice in every environment

Public cloud, private cloud, on-premises and air-gapped networks need different tools but the same practice. Code review, signed builds and tested restores mean the same thing everywhere. Each page says what changes when you cannot reach the internet.

## 11. Measure systems and teams, never individuals

Delivery and reliability metrics describe how well a system of people and tools works. Using them to rank individuals destroys the data and the trust that produced it.

## 12. People own the code

Whoever opens a change owns every line of it, however it was produced: typed by hand, generated, copied or suggested by a code assistant. Ownership means they can explain it, test it and support it in production.
