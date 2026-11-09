# Quality engineering

The problem: "QA is a bottleneck at the end." Work piles up waiting for a separate test team, releases slip, and defects still reach production. Make quality the whole team's job, built in while the code is written, and turn testers into quality engineers who coach, automate and explore rather than inspect at the end. Measure quality by what reaches users, not by how many test cases were executed.

## Outcomes

Starting targets. Tune them to your product and risk.

| Signal | Starting target |
|---|---|
| Time work waits in a "ready for test" or "in QA" column | Under 1 working day, then remove the column |
| Change fail rate (DORA) | Under 15% |
| Escaped defects (found by users or in production) per month | Tracked per team, trending down |
| Defects found by automated checks before merge, as a share of all defects found | Rising quarter on quarter |
| Manual regression phase before release | None for services you deploy yourself |
| Stories that meet the definition of done (tests, docs, observability) at merge | 100% |

## Why the status quo fails

A test phase at the end of a sprint or release has three costs. Feedback arrives days after the code was written, so fixes are slower. Work queues in front of a few testers, so lead time grows. Developers learn that someone else will catch their mistakes.

The research supports a different model. The DORA programme lists test automation and continuous testing as capabilities that predict better software delivery performance. *Accelerate* (Forsgren, Humble and Kim, 2018) reports that the better results came when developers create and maintain acceptance tests, not when tests are owned by a separate QA group or an outsourced party. Testers do not go away. Their work moves earlier and becomes more skilled.

## Practice

### Foundation

- **One definition of done** for the whole team: code reviewed, automated tests at the right level, CI green, docs and runbook updated, observable in production, behind a flag if not ready for users. Use the [team working agreement](../../templates/docs/team-working-agreement.md).
- **Developers write the tests** for their change, in the same pull request. See [testing](../delivery/testing.md) and [test-driven development](test-driven-development.md).
- **Agree acceptance criteria before work starts.** Product, engineering and whoever thinks most about testing (the "three amigos") spend 15 minutes on each non-trivial story: examples, edge cases, what must not happen.
- **No "in QA" column.** If your board has one, set a work-in-progress limit of 2 on it and swarm on what is stuck. Remove the column once it is usually empty.
- **Fix bugs before features** for any defect that affects users. A bug that waits a sprint is a choice; record it.
- **Solo and startup**: there is no tester. Write tests first for risky code, do a short exploratory session before each release, and watch production closely after it.

### Standard

- **Quality engineers, not gatekeepers.** People with testing expertise:
  - coach developers on test design and risk analysis;
  - build and maintain test tooling, test data and environments;
  - run time-boxed exploratory testing sessions (for example 60 to 90 minutes with a written charter) on new features;
  - own cross-cutting quality: accessibility, performance, security testing with specialists.
  A starting ratio is one quality engineer supporting 2 or 3 teams, not one per team doing manual checks.
- **Test across the four agile testing quadrants**: technology-facing checks that support the team (unit, component), business-facing checks that support the team (acceptance examples), business-facing critique of the product (exploratory, usability), technology-facing critique (performance, security, resilience).
- **Quality in production.** Some failures only appear with real traffic. Use [feature flags](../delivery/feature-flags.md), canary releases, synthetic checks on critical user paths, error tracking and [service level objectives](../reliability/service-levels.md). Fast detection and rollback are part of quality.
- **Learn from escapes.** For every escaped defect above a severity threshold, ask which cheaper check could have caught it, and add that check. Review the list monthly.
- **Non-functional quality has owners and budgets**: performance budgets (for example page weight, 95th percentile latency), accessibility against WCAG 2.2 AA, security checks. Check them in CI where you can.
- **Quality characteristics.** Use ISO/IEC 25010 as a checklist of what "quality" can mean (functional suitability, performance efficiency, compatibility, usability, reliability, security, maintainability, portability and more) when you agree non-functional requirements.

### Assured

- **Independent verification** where regulation or safety requires it: a person or team independent of the developers reviews test evidence for high-risk changes. Independence is about who signs, not about a hand-off queue. Keep test automation with the developers.
- **Test evidence as a record.** Keep test results per release, tied to the commit and artifact digest, for your retention period. This supports ISO/IEC 27001:2022 Annex A 8.29 and change evidence under 8.32.
- **Requirements traceability** for regulated functions: requirement or control, the tests that verify it, the result for each release.
- **Accessibility conformance** statements for public services, with dated manual testing. See [public sector](../compliance/public-sector.md).

## Cloud, on-premises and air-gapped

- Test tooling (browsers, device farms, load generators, accessibility checkers) must run inside the network. Plan for this before you pick tools.
- For software customers install, exploratory and upgrade testing on each supported customer platform is part of quality, and needs a lab that mirrors those platforms.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Testers receive builds at the end of the sprint | Testers join refinement and pair during development. |
| A separate automation team writes tests for other teams' code | Developers own automated tests. Quality engineers build tooling and coach. |
| Thousands of manual test cases re-run before each release | Automate the stable checks. Spend human time on exploratory testing. |
| Quality measured by test cases executed or bugs logged by testers | Measure escaped defects, change fail rate and recovery time. |
| "QA approved it" used to shift blame | The team owns quality. Postmortems are blameless. |
| Hardening sprint before each release | Definition of done includes tests. Fix the process that creates the backlog of defects. |

## Templates

- [Team working agreement (definition of done)](../../templates/docs/team-working-agreement.md)
- [Pull request template (how tested)](../../templates/github/PULL_REQUEST_TEMPLATE.md)
- [Release checklist](../../templates/docs/release-checklist.md)

## Sources

- DORA capability, test automation: https://dora.dev/capabilities/test-automation/
- DORA metrics: https://dora.dev/guides/dora-metrics-four-keys/
- Nicole Forsgren, Jez Humble and Gene Kim, *Accelerate* (IT Revolution, 2018).
- Lisa Crispin and Janet Gregory, *Agile Testing* (Addison-Wesley, 2009), the agile testing quadrants (after Brian Marick).
- ISO/IEC 25010:2023, product quality model: https://www.iso.org/standard/78176.html
- W3C Web Content Accessibility Guidelines 2.2: https://www.w3.org/TR/WCAG22/
