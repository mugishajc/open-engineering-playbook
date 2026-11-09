# Test automation

The problem: "Our end-to-end suite takes two hours, fails one run in three, and nobody trusts a red build." Treat test automation as a product with an architecture: put each check at the lowest layer that can catch the defect, keep end-to-end tests to a few critical journeys, give every suite an owner and a time budget, and control flakiness with data. Test code is production code: reviewed, refactored and deleted when it stops earning its run time.

## Outcomes

Starting points. Tune them after a month of data.

| Signal | Starting target |
|---|---|
| Pull request pipeline duration | Median under 10 minutes, 90th percentile under 15, as in [continuous integration](../delivery/continuous-integration.md) |
| Flaky tests quarantined | Within 24 hours of the first confirmed flake |
| Quarantined tests fixed or deleted | Within 14 days |
| Runs on `main` that fail only because of a flaky test | Under 2% |
| End-to-end tests | 5 to 20 critical paths, under 15 minutes |
| Test suites with an owning team in CODEOWNERS | 100% |
| Mutation score on the most critical modules | Measured, with a floor set from the first baseline and not falling |

## Architecture: layers and ownership

The layers, what runs where and their time budgets are set in [testing](../delivery/testing.md#pyramid-or-trophy). Use them. This table adds what each layer is for and who owns it.

| Layer | Catches | Must not do | Owner |
|---|---|---|---|
| Static checks | Type errors, unsafe patterns, formatting | Replace review of logic | Team; rules from the platform team |
| Unit | Wrong logic in rules, calculations, parsers | Network, disk or database I/O | Developer of the change |
| Component (service through its API, real database in a container) | Wrong queries, constraints, serialisation, error handling | Call other teams' live services | Owning team |
| Contract | Breaking changes between consumer and provider | Test business logic of the provider | Consumer writes, provider verifies |
| End to end | Broken wiring of the whole journey | Check every rule again; set up data through the user interface | Team that owns the journey |
| Production checks (synthetic probes, SLO alerts) | Failures only real traffic and real dependencies show | Write real customer data | Team, with SRE |

Quality engineers build and maintain the framework, shared libraries, reporting and test environments, and coach. They do not write other teams' tests. A separate automation team that writes tests for code it does not own produces suites nobody maintains.

## Design rules for test code

- **One behaviour per test**, named for what the caller sees: `refund_is_rejected_after_90_days`. Arrange, act, assert, in that order.
- **Each test builds its own data** with factories or builders, and works when tests run in parallel and in any order. No shared accounts or fixtures that other tests change.
- **No fixed sleeps.** Wait for a condition with a timeout. Prefer frameworks with built-in waiting, such as Playwright.
- **Find screen elements the way users do**: by role and accessible name, or by a dedicated test ID. Never by CSS path or layout position. Role-based locators also catch some accessibility defects.
- **Set up through the API, test through the screen.** An end-to-end test that creates its customer through five screens is slow and fails for reasons unrelated to what it tests.
- **Fake third parties at the boundary**, with service virtualisation (for example WireMock) or the provider's sandbox, and keep the fakes honest with contract tests (for example Pact).
- **Control time and randomness.** Inject a clock, fix and log seeds. See [testing](../delivery/testing.md#foundation).
- **Assert outcomes, not calls.** A test that only checks a method was called proves the code ran, not that it worked.
- **Same standards as product code**: linting, review, code owners, no duplication without reason. See the review checklist below.

## Reviewing test code

Reviewers read the tests before the code (see [code review](../delivery/code-review.md)). A test that passes whatever the code does is worse than no test, because it adds run time and false confidence. Check each new or changed test for these points:

| Check | What a failure looks like |
|---|---|
| It fails without the change | The test passes on the parent commit too, so it proves nothing about this change |
| It asserts the requirement, not the current output | The expected value was copied from what the code returned, including its bug |
| It asserts an outcome | Only "method was called" or "no exception" checks |
| It sits at the cheapest layer that catches the defect | A rule checked through the screen that a unit test could check |
| It owns its data and is parallel-safe | Shared user, fixed record ID, or reliance on another test's leftovers |
| It waits for conditions, not time | `sleep(5)` or a fixed timeout as the wait |
| Its name says the behaviour | `test_refund_2` instead of `refund_is_rejected_after_90_days` |
| A deleted or weakened assertion has a reason | Assertions removed to make a red build green |

Look hardest at changes that delete tests, loosen assertions, add skips or raise timeouts. Make those visible in the pull request description.

## Flakiness control

The policy is in [testing](../delivery/testing.md#standard): quarantine within 24 hours, fix or delete within 14 days, no hidden retries. Run it with data.

1. **Detect.** When a test fails, rerun only that test once in a separate step, and record the result. Fail then pass on the same commit marks it flaky: the build continues, the test is flagged, and the 24-hour quarantine clock starts. Fail twice is a real failure and blocks merge. Report every rerun. Nightly runs of the whole suite, several times in random order on an unchanged commit, find flakes before they hit a pull request.
2. **Measure.** Flake rate per test is flaky failures divided by runs over the last 14 days. Rank tests by flake rate times run count: a test that runs 500 times a day hurts more.
3. **Find the cause.** Most flakes fall into a few classes:

   | Cause | Typical fix |
   |---|---|
   | Waiting for time instead of a condition | Wait for the element, event or state |
   | Order dependence or shared state | Own data per test; reset state; run in random order to find it |
   | Clock, time zone or locale | Inject a clock; set time zone and locale in the test |
   | Unstable environment or third party | Container per run; fake at the boundary |
   | Resource limits on CI runners | Right-size runners; limit parallelism per runner |
   | A real race condition in the product | Fix the product. Users will hit it too. |

4. **Report weekly** per team: quarantined tests, overdue tests, flaky failure rate on `main`. A rising number is a signal to stop feature work, as [testing](../delivery/testing.md#standard) says.

## Speed budgets

Treat each layer's time budget like an error budget. When a layer stays over its budget for 2 weeks (starting point), the owning team spends time getting it back before adding more tests to it.

- **Run only what a change affects**, using build tools that know the dependency graph, and run everything on `main` and nightly.
- **Shard and parallelise.** Split suites by recorded duration, not by file count. Parallel runs need parallel-safe tests: give each worker its own database or schema, its own queue names and its own ports, and never let two workers write the same record.
- **Reuse containers** within a run; start dependencies once per shard, not once per test. Reset state between tests with transactions rolled back or tables truncated, not by restarting the container.
- **Watch the cost of parallelism.** More shards cut wall-clock time but add start-up time per shard and runner cost. When a shard spends more than a quarter of its time starting up (starting point), use fewer, longer shards.
- **Push checks down.** When an end-to-end test catches a rule error, add a unit test for the rule and remove the rule from the end-to-end test.
- **Review the slowest 10% of tests each quarter.** Delete tests that duplicate cheaper coverage. A deleted test is replaced if the behaviour still matters.

## Proving the tests work

Passing tests show the code ran. These show the tests would notice a defect.

| Method | What it shows | Tools (examples) |
|---|---|---|
| Diff coverage floor | Changed code was executed by some test | Coverage tools; floor of 80% on changed lines, from [testing](../delivery/testing.md#standard) |
| Mutation testing | Tests fail when the code is deliberately broken | PIT (Java), Stryker (JavaScript, C#, Scala), mutmut (Python) |
| Property-based testing | Rules hold for generated inputs, including ones nobody thought of | QuickCheck, Hypothesis, fast-check |
| Contract verification | Fakes match the real provider | Pact |
| Failing-first check | A new test fails without the change | Run the test against the parent commit, in review or in CI |

Run mutation testing on the modules where a defect is most expensive (money, permissions, eligibility rules), not on everything. It is slow and its value is concentrated.

## Choosing tools

- **Same language as the product code**, so developers maintain the tests.
- **Runs locally and in CI the same way**, from one command. See [continuous integration](../delivery/continuous-integration.md#foundation).
- **Works offline** from your internal mirror, if you have air-gapped sites.
- **Standard result formats** (JUnit XML is the common one) so reports and evidence do not depend on one vendor.
- **Examples:** Playwright, Cypress or Selenium WebDriver for browsers; Espresso, XCUITest or Appium for mobile; Testcontainers for real dependencies; Pact for contracts. Which devices and browsers to run them on is a strategy decision; see [test strategy](test-strategy.md#platform-and-device-coverage).
- **Record-and-playback and low-code tools** can help people without coding skills write a few checks. They become expensive when the suite grows, because the tests are hard to review, reuse and refactor. Do not make them the main approach for a product you build.

## In the AI era

- **Assistants draft tests quickly.** Each generated test must fail without the change and assert the requirement, not whatever the code returns. Generated tests often copy the code's current output into the expected value, bug included. Apply the [review checklist](#reviewing-test-code) and run the failing-first check in CI. See [test-driven development](test-driven-development.md#standard).
- **More changes, same test budget.** When assistants raise the number of pull requests per engineer, the pipeline runs more often. Affected-only runs and the speed budgets above matter more, not less.
- **"Self-healing" locators** change a test when the screen changes. Log every heal and have a person approve it, or they will hide real defects, such as a button that moved where users cannot find it.
- **AI triage of failures** can group failures and suggest likely causes. Use it to rank work, not to mark tests flaky automatically.
- **Testing features built on language models** needs evaluation sets with thresholds, not exact-match assertions. The sizes and rules are in [quality engineering](quality-engineering.md#in-the-ai-era).

## Practice

### Foundation

- Unit and component tests in CI on every pull request, blocking merge.
- A handful of end-to-end smoke checks on the most important journey, run after each deploy.
- No fixed sleeps, no shared test data, no dependence on the public internet.
- Record every rerun, so flakes are visible from the start.

### Standard

- The layers, budgets and owners above, written into the [test strategy](test-strategy.md).
- A flaky-test dashboard per team and the 24-hour and 14-day policy enforced, as in [testing](../delivery/testing.md#standard).
- Test code reviewed against the checklist above; deleted or weakened assertions called out in the description.
- Contract tests between services; real dependencies in containers.
- Affected-only runs and sharding to stay inside the 10-minute pull request budget.
- Mutation testing on critical modules, and a quarterly review of the slowest tests.
- Quality engineers own the framework and coach; teams own their tests.

### Assured

- Test results stored per release with commit and artifact digest, as in [quality engineering](quality-engineering.md#assured).
- Test tools that produce regulatory evidence are pinned and their versions recorded. In life sciences, follow your computer system validation approach (for example ISPE GAMP 5) for those tools.
- A second reviewer checks that tests for safety-critical or money-critical code cover the requirement, not only the code.

## Cloud, on-premises and air-gapped

- Browsers for end-to-end tests are large and change often. In air-gapped networks, mirror the exact browser builds your framework version expects, and update them on a schedule.
- Cloud device farms receive your app build and any test data you send. Treat them as a third party with the same approval as any other data transfer. On-premises, keep a small device lab with the devices your users have.
- Self-hosted runners need enough CPU and memory for parallel browsers. Under-sized runners are a common cause of flakes.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| A two-hour end-to-end suite that checks every rule through the screen | Push rules down to unit and component tests. Keep 5 to 20 journeys. |
| Automatic retries on the whole suite | Rerun one failed test once, record it, quarantine flakes. |
| A central automation team writes tests for other teams | Teams own tests. Quality engineers own tooling and coaching. |
| Locators by CSS path or XPath of layout | Role and accessible name, or test IDs. |
| Tests that share one test user | Each test creates its own data. |
| Coverage percentage as the team goal | Diff coverage floor plus mutation testing on critical code. |
| Test code nobody reviews | Same review and code owners as product code. |

## Templates

- [Test strategy](../../templates/quality/test-strategy.md)
- [CI workflow with test job](../../templates/github/workflows/ci.yml)
- [CODEOWNERS](../../templates/github/CODEOWNERS)
- [Pull request template (how tested)](../../templates/github/PULL_REQUEST_TEMPLATE.md)

## Sources

- Mike Cohn, *Succeeding with Agile* (Addison-Wesley, 2009), the test automation pyramid.
- Martin Fowler, "Eradicating Non-Determinism in Tests" (2011): https://martinfowler.com/articles/nonDeterminism.html
- Koen Claessen and John Hughes, "QuickCheck: A Lightweight Tool for Random Testing of Haskell Programs", ICFP 2000.
- Hypothesis documentation: https://hypothesis.readthedocs.io/
- PIT mutation testing: https://pitest.org/
- Stryker mutator: https://stryker-mutator.io/
- Pact documentation: https://docs.pact.io/
- Testcontainers: https://testcontainers.com/
- Playwright, locators: https://playwright.dev/docs/locators
- DORA capability, test automation: https://dora.dev/capabilities/test-automation/
