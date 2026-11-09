# Technical debt

"Everything takes longer than it should, and engineers keep asking for a refactoring quarter that never comes." Make technical debt visible in a register, describe each item by the cost it causes today (the interest), and pay it down continuously from a fixed share of every team's capacity. Debt you can name, price and rank is a normal business decision. Debt that lives only in engineers' complaints never gets funded.

## Outcomes

Starting points. Tune them to your organisation.

- Every team keeps a debt register with an owner, an interest estimate and a target date for each item.
- Each team spends 15% to 25% of capacity on debt and maintenance, every sprint or cycle, not in occasional "clean-up" quarters.
- The top 5 debt items by interest are reviewed with product leadership every quarter, and at least 2 are closed or reduced.
- Change lead time and change fail rate for the affected systems improve after debt work, measured with the [DORA metrics](../measurement/metrics.md).
- No item rated high risk is older than 2 quarters without a recorded decision to accept it.

## What counts as technical debt

Ward Cunningham introduced the metaphor in 1992: shipping code with known shortcuts is like borrowing money, and every later change pays interest until the debt is repaid. The useful part of the metaphor is interest. A messy module that nobody touches costs little. A messy module that every feature passes through costs a lot.

| Kind | Examples |
|---|---|
| Code | Duplicated logic, missing tests, unclear names, very large functions |
| Architecture | Tight coupling between services, a shared database across teams, wrong boundaries |
| Dependencies and platform | Unsupported language or framework versions, end-of-life operating systems, unpatched libraries |
| Delivery | Manual deployment steps, slow or flaky CI, missing environments |
| Operational | Missing monitoring, no runbooks, alerts nobody trusts |
| Documentation and knowledge | One person knows how it works, no ADRs for key choices |
| Security | Known weaknesses accepted under time pressure, outdated cryptography |

Not everything old or disliked is debt. If it does not slow change, cause incidents or carry risk, it is not costing you interest.

## Pricing the interest

Describe each item by what it costs now, in terms the business understands:

- **Time:** "Each change to billing needs 2 extra days of manual testing."
- **Failures:** "This module caused 3 of the last 10 incidents."
- **Risk:** "The framework loses security support in 9 months."
- **Opportunity:** "We cannot launch the new tariff until pricing is untangled."

Then estimate the cost to fix in engineer-weeks. Rank by interest divided by cost. Items with high interest and low cost go first.

## Practice

### Foundation

- A debt register in the repository, using the [tech debt register template](../../templates/docs/tech-debt-register.csv). Add an item whenever you take a shortcut on purpose, and link it from a code comment.
- Reserve a fixed share of capacity (start at 20%) for debt and maintenance. Protect it like any other commitment.
- Follow the boy scout rule: leave code you touch a little better, within the same pull request, when the change is small.

### Standard

- Each team ranks its register every quarter by interest and cost. Product and engineering leads agree the top items together (see [product partnership](../ways-of-working/product-partnership.md)).
- Dependency and platform debt is reduced automatically where possible: automated dependency updates, end-of-life tracking for runtimes (see [dependencies](../security/dependencies.md)).
- Debt that spans teams goes to the architecture forum. Large items get an [RFC](rfcs.md) or a [modernisation](legacy-modernisation.md) plan.
- Static analysis tracks trends (complexity, duplication, test coverage of changed code) per repository. Use trends to spot problems. Do not set a single score as a target.

### Assured

- High-risk debt items, especially security and end-of-life items, are entered in the organisation's risk register with an owner and an acceptance decision.
- Accepted security debt has an expiry date of at most 12 months and a compensating control.
- End-of-life software in production is reported to the risk owner each quarter. Regulated firms and public bodies often must show they run supported software.

## Cloud, on-premises and air-gapped

- On-premises and air-gapped systems collect platform debt faster, because updates need more effort to move in. Track operating system, runtime and database versions for each environment, and plan update windows in advance.
- End-of-life dates matter more where you cannot patch quickly. Start upgrades at least 6 months before support ends.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Asking for a "refactoring quarter" | Continuous capacity share, every cycle. |
| Debt described in engineering terms only ("it is ugly") | Price the interest in time, failures, risk or opportunity. |
| A register with hundreds of items nobody ranks | Rank quarterly. Close or delete items that cost nothing. |
| Rewriting a whole system to clear debt | Fix the highest-interest parts first. Use the strangler fig for large changes. |
| Code quality score set as a target | Track trends. Target outcomes such as lead time and change fail rate. |

## Templates

- [Tech debt register](../../templates/docs/tech-debt-register.csv)
- [ADR template](../../templates/docs/adr.md)
- [Risk register](../../templates/strategy/risk-register.csv)

## Sources

- Ward Cunningham, "The WyCash Portfolio Management System", OOPSLA 1992 experience report: https://c2.com/doc/oopsla92.html
- Martin Fowler, "Technical Debt Quadrant": https://martinfowler.com/bliki/TechnicalDebtQuadrant.html
- DORA capability, code maintainability: https://dora.dev/capabilities/code-maintainability/
