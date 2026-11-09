# Test-driven development

The problem: "We write tests after the code, if there is time, and they miss the cases that matter." Tests written last tend to confirm what the code already does. Use test-driven development (TDD) for logic where mistakes are expensive and the expected behaviour can be stated up front, and work in short cycles of test, code and refactor. Do not mandate it everywhere: use it where it pays, and judge the result by the tests and design you get, not by the ritual.

## Outcomes

Starting targets. TDD is a means; these measure the ends.

| Signal | Starting target |
|---|---|
| Bug fixes that start with a failing test reproducing the bug | 100% |
| Pull requests that change behaviour and include tests written for that behaviour | 100% |
| Core domain modules (pricing, permissions, tax, eligibility rules) with fast unit tests | 100% of public behaviour |
| Unit test suite run time for a single module | Under 10 seconds, so it can run on every save |
| Escaped defects in modules developed test-first, compared with the rest | Tracked; use it to decide where to extend TDD |

## The cycle

1. **Red.** Write one small test for the next piece of behaviour. Run it and watch it fail for the reason you expect.
2. **Green.** Write the simplest code that makes the test pass. Resist adding behaviour no test asks for.
3. **Refactor.** With all tests green, improve names, remove duplication and fix the design. Run the tests after each step.

Each cycle takes minutes, not hours. If you cannot get back to green within about 10 minutes, take a smaller step or revert.

## What the evidence says

TDD was described by Kent Beck in *Test-Driven Development: By Example* (2002). Controlled studies of its effect on quality and productivity give mixed results. One careful study (Fucci and others, IEEE Transactions on Software Engineering, 2017) found that working in short, steady cycles mattered more than whether the test was written before or after the code. Take two lessons from this: short cycles with fast tests are the core of the practice, and dogma about test order is not worth a team argument.

## When it pays and when it does not

| Use TDD | Do not force TDD |
|---|---|
| Business rules with clear inputs and outputs: money, dates, tax, permissions | Spikes and prototypes you will throw away (then delete them, or rewrite test-first) |
| Bug fixes: the failing test proves the bug and guards against its return | Visual layout and styling (use visual review and snapshot or screenshot checks) |
| Parsers, validators, state machines, algorithms | Exploring an unfamiliar API (write learning tests afterwards) |
| Public library interfaces, where the test is the first user | Glue code with no logic, covered by integration tests |
| Legacy code you are about to change (start with characterisation tests) | Generated code |

## Practice

### Foundation

- **Every bug fix starts with a failing test.** This is the cheapest TDD habit and the one with the clearest payoff. Make it a rule in the [team working agreement](../../templates/docs/team-working-agreement.md).
- **Fast tests.** Unit tests do no network, disk or database I/O, and run in milliseconds. Slow tests break the cycle.
- **Test behaviour, not implementation.** Name tests after what the user or caller sees (`rejects_expired_token`), not after methods.
- **Commit on green.** Small commits on a branch make it cheap to throw away a wrong step.
- **Learn it properly.** Run a half-day kata session for the team (for example a string calculator or bowling score kata) before expecting people to use TDD on production code.

### Standard

- **Outside-in for features.** Start with an acceptance test that describes the feature from the user's view (for example in Given/When/Then form, from behaviour-driven development), then drive the inner design with unit tests until the acceptance test passes. The acceptance examples come from the three-amigos conversation in [quality engineering](quality-engineering.md).
- **Characterisation tests for legacy code.** Before changing code with no tests, write tests that record what it does today, even if that behaviour looks wrong. Then change it safely. See Michael Feathers, *Working Effectively with Legacy Code*.
- **Property-based tests** for code with large input spaces (serialisers, parsers, financial calculations): state a rule that must hold for all inputs and let the tool generate cases.
- **Pair or ensemble on hard problems.** TDD with two people keeps steps small and catches missing cases early.
- **Review the tests first.** Reviewers read the tests before the code: do they describe the behaviour, would they fail without the change? See [code review](../delivery/code-review.md).
- **Code assistants.** Assistants can draft tests and code quickly. Write or approve the failing test yourself first, so the test encodes the requirement rather than mirroring whatever code was generated. See [code assistants](../people/code-assistants.md).

### Assured

- For safety- or money-critical logic, record the tests that verify each requirement and keep the results per release as evidence. See [quality engineering](quality-engineering.md#assured).
- Use mutation testing on these modules to show that the tests detect injected faults, not only that they execute the code.

## Cloud, on-premises and air-gapped

TDD needs only a local test runner. In air-gapped networks, make sure test frameworks, property-based testing libraries and mutation testing tools are in the internal package mirror, at pinned versions, before teams need them.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "We do TDD" mandated for all code, policed by commit order | Agree where it pays. Judge by test quality and escaped defects. |
| Large steps: an hour of code before the first green | Smaller tests. Revert and retry when stuck for 10 minutes. |
| Skipping refactor, so the design never improves | Refactor is a step in the cycle, not an optional extra. |
| Tests that mock every collaborator and assert call order | Test observable behaviour. Use real objects inside the module boundary. |
| Tests generated from the implementation | Write the failing test from the requirement first. |
| Slow unit tests that touch the database | Move I/O to integration tests. Keep unit tests in memory. |

## Templates

- [Team working agreement (bug fix rule, definition of done)](../../templates/docs/team-working-agreement.md)
- [Pull request template (how tested)](../../templates/github/PULL_REQUEST_TEMPLATE.md)

## Sources

- Kent Beck, *Test-Driven Development: By Example* (Addison-Wesley, 2002).
- Davide Fucci, Hakan Erdogmus, Burak Turhan, Markku Oivo and Natalia Juristo, "A Dissection of the Test-Driven Development Process: Does It Really Matter to Test-First or to Test-Last?", IEEE Transactions on Software Engineering, 2017.
- Michael Feathers, *Working Effectively with Legacy Code* (Prentice Hall, 2004).
- Dan North, Introducing BDD (2006): https://dannorth.net/introducing-bdd/
