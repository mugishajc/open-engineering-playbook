# Testing

Write automated tests that let you merge to `main` and deploy without a manual test phase. Most tests should be fast and run on every pull request (or merge request on GitLab); a smaller set of slower tests checks that real components work together. A flaky test is a defect: quarantine it within 24 hours and fix or delete it within 14 days. This page sets the base rules and numbers; the [quality](../quality/quality-engineering.md) pages build on them and do not repeat them.

## Outcomes

Starting targets. Tune them to your system.

| Signal | Starting target |
|---|---|
| Unit and component tests run time on a pull request | Under 5 minutes |
| Flaky tests quarantined | Within 24 hours of the first confirmed flake |
| Quarantined tests fixed or deleted | Within 14 days |
| Pull requests that change behaviour without a test change | Near zero, and each one explained in the description |
| Line coverage on changed code | At least 80% (a floor, not a goal) |
| Production incidents where a test would have caught the defect | Tracked in postmortems, trending down |
| Manual regression test phase before a release | None for services you deploy yourself |

## Pyramid or trophy

Both shapes say the same thing: use the cheapest test that gives you confidence. They differ on where most tests sit.

| Shape | Most tests are | Fits | Watch out for |
|---|---|---|---|
| Pyramid | Unit tests of single functions or classes | Libraries, domain logic, algorithms, money and date calculations | Tests coupled to internals, so every refactor breaks them |
| Trophy | Integration tests of a component through its public interface, with real dependencies where cheap (a real database in a container) | Web services and front ends where most bugs live at boundaries | Slow suites if every test starts a full stack |

Starting rule: test domain logic with unit tests, test each service through its API with a real database, test across services with contract tests, and keep end-to-end tests to the few user paths that earn money or carry legal risk (for example sign-up, payment, submission of a regulated form).

| Layer | Runs on | Target time |
|---|---|---|
| Static checks (types, lint, formatting) | Every commit, pre-commit and CI | Under 1 minute |
| Unit and component | Every pull request | Under 5 minutes |
| Integration (service plus real database, queue, cache) | Every pull request | Under 10 minutes in total CI |
| Contract | Every pull request on both sides | Under 2 minutes |
| End-to-end (5 to 20 critical paths) | Before deploy to production, and on a schedule | Under 15 minutes |
| Performance, load, security scans | Nightly, and before major releases | Set per system |

## Practice

### Foundation

- **Every behaviour change has a test** that fails without the change. Bug fixes start with a test that reproduces the bug.
- **Tests run in CI on every pull request** and block merge when they fail. See [continuous integration](continuous-integration.md).
- **Tests are deterministic.** No dependence on wall-clock time, test order, random seeds you do not control, or the public internet. Inject a clock. Fix the seed and log it.
- **Tests clean up after themselves.** Each test creates its own data and does not rely on data from another test.
- **Test the public interface**, not private methods. Refactoring should not break tests.
- **Coverage is a floor, not a target.** Measure it. Fail CI if coverage on changed lines drops under the floor. Never set a team goal of "reach 100%": it produces tests that execute code without checking anything.
- **Review test code like product code.** The reviewer reads the tests first and asks: would this test fail without the change, does it assert an outcome the user or caller cares about, and does it build its own data? The full checklist is in [test automation](../quality/test-automation.md#reviewing-test-code).

### Standard

- **Contract tests between services.** When service A calls service B, A's expectations are recorded as a contract and B's CI verifies it. A provider cannot merge a change that breaks a consumer. Use consumer-driven contracts (for example Pact) for internal HTTP and message APIs, and schema checks (OpenAPI, AsyncAPI, Protobuf breaking-change detection) for published APIs. See [API standards](../architecture/api-standards.md).
- **Real dependencies in containers** for integration tests (database, queue, cache) using the same major version as production. Mocks of a database hide the bugs that matter: constraint violations, transaction isolation, query plans.
- **Flaky test policy.**
  1. A test that fails and then passes on retry with no code change is flaky.
  2. Within 24 hours, the owning team moves it to a quarantine suite that runs but does not block merge, and opens an issue with an owner and due date.
  3. Within 14 days, the owner fixes it or deletes it. A deleted test is replaced if the behaviour still matters.
  4. If the quarantined test guards a high risk (score 6 or 9 in the [test strategy](../quality/test-strategy.md#risk-based-testing)), that behaviour is now unprotected. Fix it within 2 working days, or cover it with a named manual check on each release until it is fixed.
  5. Track the number of quarantined tests per team. Any test past its 14-day date, or a count that rises 3 weeks in a row (starting point), is a signal to stop feature work and fix the suite.
  6. Do not add automatic retries to hide flakes. The only allowed retry is one rerun of the failed test, recorded, as [test automation](../quality/test-automation.md#flakiness-control) describes.
- **Diff coverage gate.** Require at least 80% line coverage on changed lines, and do not let total coverage fall by more than 1 percentage point in one pull request. Allow an explained override for generated code.
- **Mutation testing** on the most critical modules (pricing, permissions, tax rules) when coverage numbers look good but bugs still escape.
- **Test ownership.** Every test suite has an owning team in CODEOWNERS.

### Assured

- **Traceability.** Link each requirement or control to the tests that verify it. Keep the test results for each release as evidence, tied to the commit and the artifact digest.
- **Security testing in the pipeline**, with the blocking rules in [secure development](../security/secure-development.md#standard) and the methods in [security testing](../quality/security-testing.md). This gives evidence for ISO/IEC 27001:2022 Annex A 8.29 (security testing in development and acceptance) and NIST SSDF PW.8.
- **Independent test review** for safety- or money-critical code: a second person reviews that the tests cover the requirement, not only the code.
- **Accessibility testing** for public services, automated and manual, as in [accessibility testing](../quality/accessibility-testing.md).

## Test data and privacy

- **Tests build their own data** with factories or a seeded synthetic data set. Never copy production personal data into test environments by default.
- **Production-derived data** only through the approved masking pipeline, with an approval record and a deletion date. The rules are in [environments](environments.md#production-data-rules); the techniques and their limits are in [test data and environments](../quality/test-data-and-environments.md).
- **Keep test fixtures free of real secrets.** Use obviously fake values that secret scanners can be told to ignore.

## See also

- [Test strategy](../quality/test-strategy.md): which risks get which tests.
- [Test automation](../quality/test-automation.md): ownership, flakiness data, speed budgets, reviewing test code.
- [Quality engineering](../quality/quality-engineering.md): the team model and testing features built on language models.

## Cloud, on-premises and air-gapped

- Container images for test dependencies (databases, queues) must come from your internal registry mirror. Pin them by digest.
- Test frameworks and browsers for end-to-end tests come from the internal package mirror. Plan for browser updates: they are large and change often.
- Contract brokers (for example a self-hosted Pact Broker) and test reporting tools run inside the network.
- Software you ship to customers' on-premises sites needs an install and upgrade test on each supported platform version before release.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Retry 3 times" on the whole suite | Quarantine and fix. Record retries so flakes are visible. |
| Coverage target of 90% for every repository | Diff coverage floor. Review test quality, not only the number. |
| Shared staging used as the integration test bed | Containers per CI run. Ephemeral environments for end-to-end tests. |
| Hundreds of end-to-end tests that take an hour | Push checks down to unit, component and contract tests. Keep 5 to 20 critical paths. |
| Mocks of everything, including the database | Real dependencies in containers for integration tests. |
| Production database dump in a developer laptop | Synthetic data, approved masking, deletion date. |
| A separate QA team that tests after development is "done" | Engineers write tests with the change. See [quality engineering](../quality/quality-engineering.md). |

## Templates

- [CI workflow with test job](../../templates/github/workflows/ci.yml)
- [GitLab CI with test stage](../../templates/gitlab/.gitlab-ci.yml)
- [Pull request template with "how tested"](../../templates/github/PULL_REQUEST_TEMPLATE.md)

## Sources

- Mike Cohn, Succeeding with Agile (Addison-Wesley, 2009), origin of the test automation pyramid.
- Google engineering practices, reviewing tests: https://google.github.io/eng-practices/review/reviewer/looking-for.html
- Pact documentation: https://docs.pact.io/
- OpenAPI Specification: https://spec.openapis.org/oas/latest.html
- NIST SP 800-218 Secure Software Development Framework: https://csrc.nist.gov/projects/ssdf
- W3C Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
- ISO/IEC 27001:2022: https://www.iso.org/standard/27001
