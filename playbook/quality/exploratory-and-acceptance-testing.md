# Exploratory and acceptance testing

The problem: "User acceptance testing is two weeks where business users click through scripts we wrote for them, sign, and then find the real problems in the first week live." Scripts check what someone already thought of; the expensive defects are in what nobody thought of. Run exploratory testing as chartered, time-boxed sessions with written notes, aimed at the highest risks. Make user acceptance testing (UAT) a check by real users that the service does their job with their data and procedures, against criteria agreed before build, ending in a sign-off that records open defects and who accepted the risk. Neither replaces automated checks: they cover what scripts cannot.

## Outcomes

Starting points. Tune them to your product and risk.

| Signal | Starting target |
|---|---|
| Changes with a risk score of 6 or 9 (see [test strategy](test-strategy.md#risk-based-testing)) that get at least one chartered exploratory session before release | 100% |
| Exploratory sessions with written notes and a debrief | 100% |
| Defects found in exploration that now have an automated regression test, where one is possible | 100% |
| UAT started with every entry criterion met | 100% |
| UAT sign-offs that name the accountable business owner, open defects with severity, and accepted risks | 100% |
| Severity 1 or 2 defects found in the first 30 days live that UAT participants would have met in their normal work | Tracked per release, trending down |

## Exploratory testing

Exploratory testing is learning about the product, designing tests and running them at the same time, with each result shaping the next test. The term comes from Cem Kaner. Elisabeth Hendrickson's *Explore It!* (2013) describes how to do it with discipline.

### Charters and sessions

- **A charter** gives each session a mission. Hendrickson's form: "Explore *target* with *resources* to discover *information*." For example: "Explore the refund flow with two browser sessions on the same order to discover what happens when two staff refund at once."
- **A session** is 60 to 90 minutes, uninterrupted, by one person or a pair, against one charter. This is the session-based test management approach described by Jonathan Bach.
- **Notes** record what was covered, defects, questions, and anything that blocked testing. Use the [exploratory charter template](../../templates/quality/exploratory-charter.md).
- **A debrief** of 10 to 15 minutes with the developer or the team: what we covered, what we found, what we could not test, what to explore next.

### Where to look

Use these as prompts when writing charters:

- **Variables.** Anything that can change: fields, settings, roles, counts, sizes, timing, order of steps. Vary them deliberately.
- **Boundaries and data.** Zero, one, many, the maximum; names with apostrophes, hyphens and non-Latin scripts; very long input; leap days, time zone and daylight saving changes; currency rounding.
- **Interruptions.** Back button, refresh, double submit, network drop, session timeout, the phone locking mid-payment.
- **State.** Illegal transitions, cancelling halfway, resuming tomorrow, undo.
- **Concurrency.** Two users or two tabs editing the same record.
- **People.** A first-time user, an expert in a hurry, a screen reader user, someone on a low-cost phone and slow network, a user with the wrong role.
- **Integrations.** The third party slow, down, or returning something unexpected.
- **Past incidents.** Every postmortem in the area is a charter.

### Who explores, and when

Anyone with a charter can explore: quality engineers, developers, designers, product owners, support staff. Support staff know where users get stuck. Explore new features before release, risky changes, areas with recent incidents, and new integrations. Explore before UAT, so UAT is not the first time anyone looks.

An ensemble session (several people, one screen, one charter, rotating who drives) works well for a new feature or a bug bash before a launch.

## Acceptance testing

Several kinds of testing are called "acceptance". Keep them apart, because they answer different questions and have different owners.

| Kind | Question | Owner | Form |
|---|---|---|---|
| Story acceptance | Does this story do what we agreed? | Team and product owner | Examples agreed in the three-amigos conversation, automated as acceptance tests; see [test-driven development](test-driven-development.md#standard) |
| User acceptance (UAT) | Can the people who will use this do their job with it? | Business owner | Real users, real processes, realistic data |
| Operational acceptance | Can we run, support, monitor, back up and restore it? | Service owner and operations | The [production readiness review](../../templates/docs/production-readiness-review.md) |
| Contract or regulatory acceptance | Does the delivery meet the contract or the rule? | Contract owner, compliance | Acceptance tests written into the contract; regulator criteria |
| Beta | Does it work for real users at real scale? | Product owner | Private beta with invited users, then public beta, as in the GOV.UK Service Manual phases |

### UAT that is not a rubber stamp

1. **Agree the scope and acceptance criteria before build**, owned by the business owner. UAT checks fitness for the business purpose, not every detail the team already tested.
2. **Use real users** from each role that will use the service: frontline staff, supervisors, support, and people who use assistive technology. Not the project team, not the business analyst who wrote the requirements. Budget their time and back-fill their day jobs.
3. **Test their real work.** Give participants end-to-end business processes with the variations they meet ("a day in the life"), plus time to explore. Scripts written by testers that walk through the screens only confirm the screens exist.
4. **Use realistic data**: synthetic with the right shape, or masked through an approved process (see [test data and environments](test-data-and-environments.md)). For a system replacement, include migrated records from the old system.
5. **Meet entry criteria before starting**: automated tests green, no open severity 1 defects, environment stable with integrations connected (sandbox mode where needed), data loaded, participants trained.
6. **Agree severity definitions in advance**:

   | Severity | Meaning |
   |---|---|
   | 1 | A business process cannot be completed, money or data is wrong, or a legal duty is broken. No workaround. |
   | 2 | A process can be completed only with a workaround that is costly or error-prone |
   | 3 | A process works with a reasonable workaround, or a minor error |
   | 4 | Cosmetic |

7. **Separate defects from change requests.** Users will ask for things nobody agreed. A defect is a failure against the agreed criteria; a request for new or different behaviour is a change request. Triage both daily with the business owner. Change requests do not block exit; the business owner decides which ones must come before go-live.
8. **Exit criteria**: every critical business process completed end to end by users; no open severity 1; each open severity 2 has a workaround and a written risk acceptance by the business owner; results recorded.
9. **Sign-off is a decision, not a signature.** The business owner accepts, accepts with conditions, or rejects, and owns that decision. Use the [UAT sign-off template](../../templates/quality/uat-sign-off.md).
10. **Measure UAT** by what it missed: severity 1 and 2 defects in the first 30 days live that participants would have met in their normal work.

### UAT and continuous delivery

For a product you deploy yourself, UAT is continuous: users try changes in preview environments and behind [feature flags](../delivery/feature-flags.md), and the product owner accepts each story. A separate UAT phase is worth its cost when you replace a system, buy packaged software, receive a delivery from a supplier, or a regulator or contract requires it.

### Bought software, suppliers and data migration

- **Write acceptance tests before you sign the contract**, and tie payment milestones to passing them. The supplier's own test reports are evidence, not acceptance.
- **Configuration is code.** Packaged software configured for you needs UAT of your processes on your configuration.
- **Data migration acceptance**: reconcile record counts and control totals (balances, open cases, outstanding amounts) between old and new systems, compare a random sample of records field by field, and run at least 2 full rehearsals of the cutover (starting point), timed against the planned window.

## Practice

### Foundation

- A 60-minute exploratory session on each release, with a written charter and notes.
- Acceptance examples agreed for each non-trivial story before work starts.
- Let a few real users try changes in a preview environment before release, and watch them.

### Standard

- Chartered sessions for every high-risk change, with debriefs; findings become regression tests.
- Quality engineers coach others to explore and keep a bank of charters from incidents.
- Continuous UAT through previews, flags and beta; operational acceptance through production readiness reviews.
- A formal UAT phase only for replacements, packaged software, supplier deliveries and regulated releases, run by the rules above.

### Assured

- Formal UAT with entry and exit criteria, signed by the accountable business owner, and the evidence kept per release.
- Traceability from each regulated requirement to its UAT scenario and result.
- People who use assistive technology among UAT participants for public services.
- Contract acceptance tests for every supplier delivery, run by you or by a party independent of the supplier.

## Cloud, on-premises and air-gapped

- For software installed at customer sites, acceptance often has two stages: a factory acceptance test at the supplier, and a site acceptance test on the customer's own infrastructure. Plan both; most surprises appear at the site.
- In air-gapped networks, UAT happens on the classified network with data that cannot leave it. Plan participant access, devices and support on site.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Users execute scripts the test team wrote | Business processes from users' real work, plus time to explore. |
| UAT is the first time anyone tries the whole process | Exploratory sessions before UAT. |
| Project manager or project team signs UAT | The accountable business owner signs and owns the risk. |
| "Exploratory testing" means unrecorded clicking | Charter, time box, notes, debrief. |
| UAT environment without integrations or realistic data | Integrations in sandbox mode; realistic synthetic or masked data. |
| Sign-off with a long list of open defects and no owner | Exit criteria; each open severity 2 accepted in writing. |
| New requirements logged as defects, so UAT never exits | Triage daily; change requests go to the business owner, not the exit criteria. |
| A long UAT phase for every release of a product you deploy | Continuous acceptance through previews, flags and beta. |

## Templates

- [Exploratory testing charter](../../templates/quality/exploratory-charter.md)
- [UAT sign-off](../../templates/quality/uat-sign-off.md)
- [Production readiness review](../../templates/docs/production-readiness-review.md)
- [Test strategy](../../templates/quality/test-strategy.md)

## Sources

- Elisabeth Hendrickson, *Explore It! Reduce Risk and Increase Confidence with Exploratory Testing* (Pragmatic Bookshelf, 2013).
- Cem Kaner, Jack Falk and Hung Quoc Nguyen, *Testing Computer Software*, 2nd edition (1993).
- Jonathan Bach, "Session-Based Test Management", Software Testing and Quality Engineering magazine, November 2000.
- Lisa Crispin and Janet Gregory, *Agile Testing* (Addison-Wesley, 2009).
- GOV.UK Service Manual, phases of a service (discovery, alpha, beta, live): https://www.gov.uk/service-manual/agile-delivery
- ISTQB glossary (acceptance testing, operational acceptance testing): https://glossary.istqb.org/
