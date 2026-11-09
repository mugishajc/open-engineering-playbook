# Test strategy

The problem: "We have 4,000 test cases and a 60-page test plan, and defects still reach production in places nobody thought about." Write a short test strategy for each product, driven by risk: list what can go wrong, how much it would hurt and whom, and pick the cheapest check that would catch each risk at the earliest point. Spend the most effort where likelihood and impact are both high, and write down what you chose not to test, so the gap is a decision and not an accident.

## Outcomes

Starting points. Tune them to your product and risk.

| Signal | Starting target |
|---|---|
| Products and Tier 1 or Tier 2 services with a test strategy of 1 to 3 pages, reviewed in the last 6 months | 100% |
| High risks (score 6 or 9 below) mapped to at least one automated check or a named manual activity with an owner | 100% |
| Escaped defects classified by the test layer that should have caught them, reviewed monthly | 100% above the severity threshold |
| Change fail rate (DORA metrics) | Under 15%, as in [quality engineering](quality-engineering.md) |
| Manual regression phase before a release | None for services you deploy yourself |
| Regulated functions with requirements traced to tests and results kept per release | 100% at Assured |

## What a test strategy answers

A test strategy is not a list of test cases. It answers nine questions in plain words. The [test strategy template](../../templates/quality/test-strategy.md) has a section for each.

| Question | What a good answer looks like |
|---|---|
| What are we protecting? | The 3 to 5 quality characteristics that matter most for this product, picked from ISO/IEC 25010:2023 (for example functional suitability, security, performance efficiency, interaction capability) |
| What can go wrong? | A risk table scored for likelihood and impact, with who is harmed |
| Which checks catch each risk, and at which layer? | Each high risk mapped to a layer: unit, component, contract, integration, end to end, exploratory, specialist, production monitoring |
| Who does what? | Developers, quality engineers, product owner, specialists and users, by name or role |
| Where do tests run, with what data? | Environments and data sources; see [test data and environments](test-data-and-environments.md) |
| What blocks a release? | Gates in the pipeline, plus the few human activities that must happen first |
| What evidence do we keep? | Test results tied to commit and artifact digest; sign-offs; reports |
| What do we not test, and why? | Accepted risks with an owner, reviewed with the strategy |
| When do we review this? | A date, plus triggers: new data class, new integration, major architecture change, an escaped high-severity defect |

## Risk-based testing

Test effort follows product risk. ISO/IEC/IEEE 29119 takes this risk-based approach as its default.

1. **Run a 60-minute risk workshop** with product, engineering, a quality engineer, and support or operations. Use the ISO/IEC 25010 characteristics as prompts so security, accessibility and performance are not forgotten. Add risks from past incidents and escaped defects.
2. **Score each risk** for likelihood (1 to 3) and impact (1 to 3). Anchor both scales so scores are comparable across teams:

   | Score | Impact | Likelihood |
   |---|---|---|
   | 3 | Money calculated or moved wrongly, a legal duty broken, personal data exposed, harm to safety, or a Tier 1 outage | New or complex code, a new team or technology, frequent change, or defects here in the last 6 months |
   | 2 | An important feature fails and a workaround exists | Moderate change or complexity, some test coverage today |
   | 1 | Cosmetic, or a minor inconvenience | Simple, stable code with good tests and no recent defects |

3. **Set test depth from the score** (likelihood times impact):

   | Score | Depth (starting point) |
   |---|---|
   | 6 or 9 | Automated checks at two layers or more, a chartered exploratory session each release that touches it, specialist review (security, performance or accessibility) where relevant, and a production alert on the outcome |
   | 3 or 4 | Automated checks at the cheapest layer that catches it, and exploratory testing when the area changes |
   | 1 or 2 | Covered by smoke checks, or accepted and recorded |

   One override: a risk with impact 3 always gets at least one automated check and a production alert, even when its likelihood is 1. Multiplying hides rare events that you cannot afford.

4. **Pick the layer.** Use the cheapest test that would catch the defect earliest. A tax rule belongs in a unit test; a broken database constraint in an integration test; a changed API field in a contract test; a confusing form in exploratory and usability testing; a changed prompt or model version in the evaluation set (see [quality engineering](quality-engineering.md#in-the-ai-era)). The layers and their time budgets are in [testing](../delivery/testing.md) and [test automation](test-automation.md).
5. **Rescore after every escaped defect** above your severity threshold, as part of the "learn from escapes" review in [quality engineering](quality-engineering.md#standard).

## Test design techniques the team should know

Automation decides how a test runs. Design techniques decide which cases are worth running. ISO/IEC/IEEE 29119-4 describes these and more. Every engineer who writes tests should be able to use the first four.

| Technique | Use it for | Example |
|---|---|---|
| Equivalence partitioning | Inputs that the code treats in groups | Ages 0 to 17, 18 to 64, 65 and over: one case per group |
| Boundary value analysis | Limits, where off-by-one errors live | 17, 18, 64 and 65; amounts at the limit and one unit over |
| Decision tables | Business rules with several conditions | Discount rules by customer type, order size and promotion |
| State transition | Workflows and lifecycles | An application moving from draft to submitted to approved, including illegal moves |
| Pairwise (combinatorial) | Many settings that interact | Browser, language, role and payment method without testing every combination |
| Property-based | Large input spaces | "Encoding then decoding returns the original" for any input; see [test-driven development](test-driven-development.md#standard) |

## Who does what

| Role | Owns |
|---|---|
| Developers | Unit, component, integration and contract tests for their change, in the same pull request |
| Quality engineer (one per 2 or 3 teams, as in [quality engineering](quality-engineering.md)) | The test strategy with the team, risk workshops, test tooling, exploratory sessions, coaching |
| Product owner | Acceptance criteria and examples; accepting risk that is not tested |
| Specialists (security, performance, accessibility) | Methods, tools and periodic deep tests; teams run the routine checks |
| Users and business owner | User acceptance and usability; see [exploratory and acceptance testing](exploratory-and-acceptance-testing.md) |
| Operations or SRE | Production checks, SLOs, resilience tests; see [resilience testing](../reliability/resilience-testing.md) |

## Release gates instead of test phases

Express entry and exit criteria as checks the pipeline enforces, plus a short list of named human activities. A typical Standard gate set:

- Required checks green: static analysis, unit, component, integration and contract tests, security scans with the blocking rules in [secure development](../security/secure-development.md#standard).
- End-to-end checks on the 5 to 20 critical paths green against the release artifact.
- No open defect of severity 1 or 2 (the scale in [exploratory and acceptance testing](exploratory-and-acceptance-testing.md#uat-that-is-not-a-rubber-stamp)) in the release scope, unless the product owner accepted it in writing.
- Chartered exploratory session done for each high-risk change.
- Performance and accessibility budgets met where the strategy names them.

## Platform and device coverage

Users meet your product on devices, browsers and networks you do not control. Choose the coverage from data and write it in the strategy.

- **Pick the matrix from your analytics**: the browsers, operating system versions and device models that together cover at least 90% of sessions (starting point), plus the lowest-specification device and oldest operating system you support. Review it every 6 months. Before you have analytics, use public market share for the countries you serve.
- **Emulators and simulators on every pull request, real devices before release.** Emulators miss real performance, camera, biometrics, push notifications, battery use and manufacturer changes to Android.
- **Old app versions keep calling your API.** Many users do not upgrade. Keep contract tests for every app version you still support, and test the forced-upgrade path before you need it.
- **Networks and interruptions**: slow and lossy networks, offline and back, an incoming call, the app sent to the background, low storage, a permission refused, large text and dark mode.
- **Install and upgrade**: a fresh install, and an upgrade from the oldest supported version with the user's data kept.
- **Store releases are slow to undo.** Use Google Play staged rollouts or Apple's phased release (7 days, automatic updates only; users can still update by hand), plus server-side [feature flags](../delivery/feature-flags.md), so a defect reaches a small share of users first.
- **Languages and formats**: every supported language, right-to-left scripts, long translations, and local date, number and currency formats.

Performance on low-cost devices is in [performance testing](performance-testing.md#front-ends-and-mobile); screen readers on mobile are in [accessibility testing](accessibility-testing.md#documents-mobile-apps-and-bought-software); device farms are in [test automation](test-automation.md#cloud-on-premises-and-air-gapped).

## Standards and certification

- **ISO/IEC/IEEE 29119** gives a shared vocabulary, test processes (part 2), documentation (part 3) and techniques (part 4). Use it as a checklist and to answer contracts that cite it. Do not produce every document it describes: a one-page strategy, pipeline results and a completion summary per release cover most needs.
- **ISTQB** certification gives a common vocabulary. It is not evidence that someone can test well. Hire on a practical exercise: give candidates a small feature and ask them to find the risks and design the tests.

## Practice

### Foundation

- One page per product, using the [template](../../templates/quality/test-strategy.md): the top 10 risks, the checks for each, what you do not test.
- Every behaviour change has a test, and every bug fix starts with a failing test. See [testing](../delivery/testing.md).
- A short exploratory session before each release, aimed at the highest risks.
- Watch production after each release: errors, the main user journey, user reports.
- **Solo and Startup:** the strategy can be a section in the README. Ten risks and their checks are enough.

### Standard

- A strategy per product or service, owned by the team with a quality engineer, reviewed every 6 months and on the triggers above.
- A 15-minute risk conversation for each epic or significant change, folded into refinement. Update the risk table.
- Release gates in the pipeline, as above. No separate test phase.
- Escaped defects classified by the layer that should have caught them. Add that check and rescore the risk.
- Non-functional budgets with owners: [performance](performance-testing.md), [security](security-testing.md) and [accessibility](accessibility-testing.md).

### Assured

- **A test policy for the organisation**: one page from the head of quality that sets the risk scale, evidence rules and independence rules every product strategy follows.
- **Traceability** from each regulated requirement or control to its tests and the result per release. Generate it from test tags and the pipeline, not by hand.
- **Independent verification** for high-risk changes: someone outside the team reviews the test evidence. See [quality engineering](quality-engineering.md#assured).
- **A test completion summary per release**, generated from pipeline results: what ran, what failed, open defects, accepted risks, who approved.
- **Contracts that cite standards.** When a contract or regulator names ISO/IEC/IEEE 29119 or a sector standard (for example IEC 62304 for medical device software or DO-178C for airborne software), map its required documents to the artifacts you already produce.
- **Bought and outsourced software.** The supplier's test evidence is an input, not your acceptance. Keep your own acceptance tests for the risks you carry.

## Cloud, on-premises and air-gapped

- The strategy names where each kind of test runs. In air-gapped networks, every test tool, browser, scanner and data generator must be in the internal mirror before the strategy depends on it.
- For software customers install, the supported platform matrix (operating systems, databases, browsers, versions) is part of the strategy, with an install and upgrade test on each. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A 60-page test plan nobody reads after approval | One to three pages, risk-driven, reviewed every 6 months. |
| Equal test effort on every feature | Score risks. Spend most effort on scores of 6 and 9. |
| Test cases counted as progress | Report risks covered and escaped defects instead. |
| Untested areas nobody chose | Write "not tested, and why" with an owner. |
| Strategy written by a test manager alone | The team writes it together in a risk workshop. |
| Every document in ISO/IEC/IEEE 29119 produced for every release | Map the standard to artifacts you already generate. |

## Templates

- [Test strategy](../../templates/quality/test-strategy.md)
- [Exploratory testing charter](../../templates/quality/exploratory-charter.md)
- [Performance test plan](../../templates/quality/performance-test-plan.md)
- [UAT sign-off](../../templates/quality/uat-sign-off.md)
- [Production readiness review](../../templates/docs/production-readiness-review.md)

## Sources

- ISO/IEC/IEEE 29119-1:2022, -2:2021, -3:2021 and -4:2021, Software and systems engineering: Software testing.
- ISO/IEC 25010:2023, product quality model: https://www.iso.org/standard/78176.html
- ISTQB glossary: https://glossary.istqb.org/
- Lisa Crispin and Janet Gregory, *Agile Testing* (Addison-Wesley, 2009).
- DORA capability, test automation: https://dora.dev/capabilities/test-automation/
- Apple, release a version update in phases: https://developer.apple.com/help/app-store-connect/update-your-app/release-a-version-update-in-phases/
- Google Play, release app updates with staged rollouts: https://support.google.com/googleplay/android-developer/answer/6346149
