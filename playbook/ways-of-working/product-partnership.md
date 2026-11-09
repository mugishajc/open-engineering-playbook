# Product partnership

The problem: "Engineering is a feature factory." Product hands over specifications, engineering builds them, nobody checks whether they worked, and technical debt only gets attention after an outage. Make product, design and engineering jointly own outcomes: decide together what problem to solve, agree a visible split of capacity, and judge success by a change in user or business metrics, not by features shipped.

## Outcomes

Starting targets. Tune them to your product.

| Signal | Starting target |
|---|---|
| Roadmap items stated as an outcome with a metric | At least 80% |
| Shipped features reviewed against their metric | 100% within 1 quarter of release |
| Engineers who took part in user research or support in the last quarter | Every engineer on product teams |
| Capacity split between roadmap, maintenance and unplanned work | Agreed, published and measured monthly |
| Features switched off or removed because they did not work | More than zero per year (if zero, you are not checking) |

## How the roles split

| Decision | Product leads | Engineering leads | Design leads | Decided together |
|---|---|---|---|---|
| Which problem to solve and why now | Yes | | | Input from all |
| How to solve it within the appetite | | Yes (technical) | Yes (experience) | Shape together |
| Quality bar and non-functional requirements | | Yes | | Agree with product |
| Capacity for maintenance, reliability and debt | | Yes | | Agree split with product |
| What ships and when | | | | Yes |
| Whether it worked | | | | Yes, against the agreed metric |

Record these in your [decision rights](../operating-model/decision-rights.md). A common model is the "product trio" (product manager, designer and tech lead) who make discovery decisions together.

## Practice

### Foundation

- **Start from a problem.** Each piece of work begins with: who has the problem, how we know, what will change if we solve it, and how we will measure it. Use the [feature request form](../../templates/github/ISSUE_TEMPLATE/feature_request.yml) for this.
- **Engineers hear users directly.** Every engineer joins at least one user interview, support shadowing session or usability test per quarter. In a startup, the founders and engineers do support themselves.
- **One shared backlog** with product and engineering work in it. Maintenance and debt are visible, ordered and discussed in the same meeting as features.
- **Check results.** For each shipped feature, look at its metric after 2 to 6 weeks and write one line: worked, did not work, unclear. Remove or change what did not work.

### Standard

- **Product trio per team** that meets at least weekly on discovery: what we learned, what to test next.
- **Capacity split** agreed per quarter in the categories from [portfolio and capacity](../strategy/portfolio-and-capacity.md), for example 60% features, 20% reliability (including unplanned work), 15% technical debt, 5% platform. Product orders the feature share; engineering decides how the debt and platform shares are spent and reports what they bought. See [planning and forecasting](planning-and-forecasting.md).
- **Error budgets as the shared rule for reliability.** When a service exhausts its error budget, the team shifts effort to reliability until it recovers, by prior agreement with product, not by negotiation during the incident. See [service levels](../reliability/service-levels.md).
- **Outcome roadmaps.** Show Now, Next and Later as problems and outcomes. Dates appear only as forecast ranges.
- **Shared metrics.** Product and engineering leaders review the same dashboard: product outcomes, DORA delivery metrics and reliability. See [metrics](../measurement/metrics.md).
- **Technical work in business terms.** Engineers explain maintenance and platform work by what it changes: risk removed, lead time cut, cost avoided. See [business case](../strategy/business-case.md).
- **Experiments behind flags.** Test ideas with a share of users before building them in full. See [feature flags](../delivery/feature-flags.md).

### Assured

- **Regulatory requirements are product requirements.** Accessibility, data protection, audit and records duties enter the backlog with owners and acceptance criteria, not as late sign-offs.
- **Public services:** follow the service standard that applies. The UK Government Service Standard starts with "understand users and their needs" and expects a multidisciplinary team; the US Digital Services Playbook starts with "understand what people need". See [public sector](../compliance/public-sector.md).
- **Risk acceptance** by the product owner for known gaps is written down, time-limited and reviewed, with engineering's assessment attached.

## Cloud, on-premises and air-gapped

For software customers install, product and engineering need direct feedback from the sites that run it: telemetry the customer has agreed to, support tickets and regular customer advisory sessions. In air-gapped deployments there is no telemetry, so plan structured feedback calls and upgrade surveys instead.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Product writes specifications, engineering estimates and builds | Product trio shapes the solution together. |
| "Tech debt sprint" once a year | Standing capacity split, measured monthly. |
| Success measured by features shipped | Outcome metric agreed before work starts and reviewed after release. |
| Engineers never meet a user | Quarterly research or support session per engineer. |
| Reliability work negotiated during an outage | Error budget policy agreed in advance. |
| Product manager acts as a ticket writer for stakeholders | Product owns problem selection and says no with evidence. |

## Templates

- [Feature request form](../../templates/github/ISSUE_TEMPLATE/feature_request.yml)
- [Team working agreement](../../templates/docs/team-working-agreement.md)
- [Strategy one-pager](../../templates/strategy/strategy-one-pager.md)

## Sources

- Teresa Torres, *Continuous Discovery Habits* (Product Talk, 2021).
- Marty Cagan, *Inspired*, second edition (Wiley, 2017).
- Google SRE workbook, implementing SLOs and error budget policy: https://sre.google/workbook/implementing-slos/
- UK Government Service Standard: https://www.gov.uk/service-manual/service-standard
- US Digital Services Playbook: https://playbook.cio.gov/
- DORA metrics: https://dora.dev/guides/dora-metrics-four-keys/
