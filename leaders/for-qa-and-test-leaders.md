# For QA and test leaders

Run quality as an engineering capability, not a department at the end of the line. Measure it by what reaches users: escaped defects, change fail rate and failed deployment recovery time, not test cases executed. Spend your people's time on risk analysis, exploration, tooling, specialist testing and coaching, and let the teams who write the code own its automated tests. In regulated and public services, make the evidence a by-product of the pipeline so audits do not need a test phase.

## When to use this

- You lead a QA or test function, or have just been hired to "fix quality".
- Releases wait days or weeks for a test phase, and defects still escape.
- Leadership asks why you need testers if developers write tests, or if AI writes them.
- Testing is outsourced and you pay for test cases, not results.
- A regulator, auditor or customer asks for test evidence and it takes weeks to assemble.
- Your testers mostly run manual regression scripts and you need a plan for their skills.

The practice behind this page is in [quality engineering](../playbook/quality/quality-engineering.md), [test strategy](../playbook/quality/test-strategy.md), [test automation](../playbook/quality/test-automation.md), [performance testing](../playbook/quality/performance-testing.md), [security testing](../playbook/quality/security-testing.md), [accessibility testing](../playbook/quality/accessibility-testing.md), [exploratory and acceptance testing](../playbook/quality/exploratory-and-acceptance-testing.md) and [test data and environments](../playbook/quality/test-data-and-environments.md). This page covers the leadership decisions around them.

## The first 90 days

Use [first 90 days](first-90-days.md) for the general method. For a quality leader, collect these numbers in the first 30 days, before proposing changes:

| Measure | Where it comes from |
|---|---|
| Escaped defects in the last 6 months, by severity and by the layer that should have caught them | Incident and defect records, postmortems |
| Change fail rate and failed deployment recovery time (DORA metrics) | Deployment and incident data; see [metrics](../playbook/measurement/metrics.md) |
| Time work waits in a "ready for test" or "in QA" column | The team boards |
| Days of manual regression per release, and people involved | Release records, interviews |
| Pull request pipeline duration, flaky and quarantined tests | CI data |
| Test environment and test data problems per week | CI failure classification, if it exists; interviews if not |
| What each tester spends their week on | A one-week time diary, shared openly |

Then pick 2 or 3 changes for days 30 to 90. Common first moves: remove the "in QA" column with a work-in-progress limit, start the flaky-test policy, run risk workshops for the two highest-risk products, and move one manual regression pack into automated checks owned by the team.

## Choosing an operating model

| Model | How it works | Fits | Watch out for |
|---|---|---|---|
| Central test team | Development hands builds to a separate team | Rarely. Some supplier acceptance and independent verification | Queues, late feedback, blame |
| Embedded testers | One tester per team who tests the team's work | A step away from the central model | The tester becomes the team's queue and safety net |
| Quality engineering | Teams own their tests; one quality engineer supports 2 or 3 teams; a small enabling team owns frameworks, environments, data and specialist methods | Most product organisations | Needs developers who accept test ownership and leaders who back it |
| Outsourced testing | A supplier runs tests for you | Peak load, specialist skills (performance, accessibility, penetration testing), independence | Knowledge leaves; paying for activity, not outcomes |

The enabling team in the quality engineering model follows the enabling team type in [team topology](../playbook/operating-model/team-topology.md#team-types): it builds capability in the stream-aligned teams and steps back, rather than doing the testing for them.

## The quality scorecard

Report these to executives monthly. Each has a starting target; the definitions come from the linked pages.

| Measure | Starting target |
|---|---|
| Escaped defects of severity 1 and 2 per month | Trending down quarter on quarter |
| Change fail rate (DORA metrics) | Falling against your own baseline; under 15% is a starting point from [quality engineering](../playbook/quality/quality-engineering.md) |
| Failed deployment recovery time (DORA metrics) | Falling against your own baseline; see [metrics](../playbook/measurement/metrics.md) |
| Manual regression days per release | Zero for services you deploy yourself |
| Flaky tests quarantined within 24 hours, fixed or deleted within 14 days | 100% |
| Pull request pipeline duration | Median under 10 minutes |
| Security findings past their fix-by SLA | Zero for P0 and P1 (the board threshold for exploited and critical findings); under 10% for P2 and below. See [vulnerability management](../playbook/security/vulnerability-management.md) |
| Public services with a current WCAG 2.2 AA audit and accessibility statement | 100% |
| Products with a test strategy reviewed in the last 6 months | 100% |

Do not report test cases executed, defects found by testers, pass rates or coverage percentages as goals. They reward activity and are easy to inflate. Coverage on changed lines is a floor in the pipeline, not a scorecard number.

## Making the case for investment

Leaders fund what they can see in money and risk. Build the case with the [business case](../playbook/strategy/business-case.md) method, with numbers from your own organisation:

- **Cost of the test phase**: people times days of manual regression per release, times releases per year. Add the delay cost of features waiting for it.
- **Cost of escapes**: hours spent on incidents and fixes for escaped defects, plus refunds, penalties and support load.
- **Risk reduced**: legal duties (accessibility, data protection, sector rules) and the evidence you can produce on demand.
- **The investment**: automation work by teams, a quality engineering enabling team, environments and data tooling, specialist tests.

Commit to the low scenario, and check at 6 and 12 months against the measures in the scorecard.

## Working with suppliers and outsourced testing

- **Contract for outcomes**: escaped defects, defect fix times, automation that runs in your pipeline. Do not pay per test case written or executed.
- **Your repositories, your tests.** Test code, data generators and results live in your repositories and pipeline, so they stay when the supplier leaves.
- **Supplier test evidence is input, not acceptance.** Keep your own acceptance tests for the risks you carry; see [exploratory and acceptance testing](../playbook/quality/exploratory-and-acceptance-testing.md#bought-software-suppliers-and-data-migration).
- **Plan the exit** from day one, as in [suppliers and contracts](../playbook/strategy/suppliers-and-contracts.md).

## The changing role of testers

Developers own automated checks. AI drafts tests. The judgement work grows: deciding what to test, finding what nobody thought of, and checking that the checks mean something.

When code is cheap to write, checking it becomes the constraint. Each engineer opens more pull requests, each one built faster than anyone could read it line by line. Four things follow for a quality function:

- **Examples before code.** The acceptance examples agreed in the three-amigos conversation become the specification the assistant works from. Someone with testing skill makes sure they include the edge cases and the "must not happen" cases. See [quality engineering](../playbook/quality/quality-engineering.md#foundation).
- **Review of tests, not only code.** Generated tests often assert whatever the code returns. Testers teach the [test review checklist](../playbook/quality/test-automation.md#reviewing-test-code) and spot-check generated tests in high-risk areas.
- **Risk triage of changes.** Not every change needs the same scrutiny. Use the [test strategy](../playbook/quality/test-strategy.md#risk-based-testing) risk scores to decide which changes get exploratory sessions and a second reviewer.
- **More exploration, not less.** Code written quickly from a short prompt has gaps nobody specified. Chartered exploratory sessions find them.

Measure the effect with rework rate, change fail rate and escaped defects against the baseline from before adoption, as [metrics](../playbook/measurement/metrics.md) describes.

| Skill | Why it matters now |
|---|---|
| Risk analysis and test design | Decides which of the many possible tests are worth writing, by people or AI |
| Exploratory testing | Finds what no script or model was told to look for |
| Automation architecture | Keeps suites fast, reliable and owned; see [test automation](../playbook/quality/test-automation.md) |
| Performance, security or accessibility testing | Specialist depth teams cannot keep on their own |
| Test data and privacy | Synthetic data and masking that keep the organisation out of legal trouble |
| Observability and production testing | Some failures only appear with real traffic |
| Evaluation design for AI features | Building evaluation sets, graders and thresholds is test design; see [quality engineering](../playbook/quality/quality-engineering.md#in-the-ai-era) |
| Coaching | Multiplies quality across 2 or 3 teams instead of testing for one |

Career paths: quality engineer to senior and staff quality engineer on the same levels as other engineers (see [career framework](../playbook/people/career-framework.md)); specialist tracks in performance, security testing or accessibility; moves into SRE, product or engineering management.

For testers who mostly run manual scripts today, plan a transition of 6 to 12 months (starting point): a skills matrix, paired work with developers, protected learning time, and a clear statement of which roles will change. Use the techniques in [skills gap](../playbook/people/skills-gap.md). Say plainly that the job is changing and that you will invest in people who want to change with it.

## AI and testing: what to tell the board

| Claim | Answer |
|---|---|
| "AI writes the tests, so we need fewer testers." | AI drafts tests quickly. Someone still decides what to test and checks each test fails without the change and asserts the requirement. Measure rework rate and change fail rate before cutting anyone; see [leading in the AI era](leading-in-the-ai-era.md#measuring-impact-with-data-not-anecdotes). |
| "Self-healing tests fix themselves." | They can also hide real defects. Every automatic change to a test needs a log and a person's approval. |
| "Our AI feature passed testing." | Ask for the evaluation set size, the thresholds, the variance across repeated runs and the human check on the graders. |
| "Code assistants make developers faster, so quality will improve." | Speed and quality are separate. Watch escaped defects and change fail rate against the pre-adoption baseline. |

## Regulated and public-sector duties

- **Independence.** Where rules require independent verification, separate who signs from who builds, not who tests from who builds. Keep automation with the developers.
- **Evidence.** Test results per release tied to the commit and artifact, traceability for regulated requirements, UAT sign-offs, penetration test reports, accessibility audits. Generate them from the pipeline; see [control mapping](../playbook/compliance/control-mapping.md).
- **Standards in contracts.** When a contract cites ISO/IEC/IEEE 29119, map its documents to artifacts you already produce rather than writing new ones.
- **Accessibility and security duties** are legal or contractual, not optional quality goals. See [accessibility testing](../playbook/quality/accessibility-testing.md#legal-duties) and [security testing](../playbook/quality/security-testing.md#assured).

## Common mistakes

| Mistake | Fix |
|---|---|
| Measuring the QA function by test cases executed and bugs found | Escaped defects, change fail rate, failed deployment recovery time. |
| Building a central automation team to write tests for other teams | Teams own their tests; an enabling team owns tooling and coaches. |
| Promising zero defects | Promise fast detection and recovery, and a falling escape rate. |
| Cutting testers because developers or AI now write tests | Move testers to risk, exploration, specialist testing and evaluation design first; measure before and after. |
| Treating UAT sign-off as the QA team's signature | The accountable business owner signs and owns the risk. |
| Outsourcing testing and the knowledge with it | Tests and results in your repositories and pipeline; contract for outcomes. |
| Assembling audit evidence by hand before each inspection | Evidence generated by the pipeline on every release. |

## Templates

- [Test strategy](../templates/quality/test-strategy.md)
- [Exploratory testing charter](../templates/quality/exploratory-charter.md)
- [Performance test plan](../templates/quality/performance-test-plan.md)
- [UAT sign-off](../templates/quality/uat-sign-off.md)
- [Production readiness review](../templates/docs/production-readiness-review.md)
- [Business case](../templates/strategy/business-case.md)

## Sources

- Nicole Forsgren, Jez Humble and Gene Kim, *Accelerate* (IT Revolution, 2018).
- DORA capabilities, test automation and test data management: https://dora.dev/capabilities/test-automation/ and https://dora.dev/capabilities/test-data-management/
- Lisa Crispin and Janet Gregory, *Agile Testing* (Addison-Wesley, 2009).
- Elisabeth Hendrickson, *Explore It!* (Pragmatic Bookshelf, 2013).
- Matthew Skelton and Manuel Pais, *Team Topologies* (IT Revolution, 2019).
- ISO/IEC/IEEE 29119-1:2022, Software and systems engineering: Software testing, Part 1: General concepts.
- ISTQB: https://www.istqb.org/
