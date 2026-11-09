# Data quality

Two dashboards show different revenue figures, a report breaks after an upstream schema change, and an AI pilot fails because its training data was incomplete. Treat data like code: define what "good" means for each important data set, test it automatically in the pipeline, set service levels for it, and handle data failures as incidents with an owner. Fix problems at the source, not in each consumer.

## Outcomes

Starting points. Tune them to your organisation.

- Every data set used for a business-critical report or an AI system has written quality rules and automated tests.
- At least 95% of pipeline runs pass their quality tests. Failures block publication of the bad data.
- Freshness meets the agreed target (for example, data no older than 24 hours) at least 99% of the time.
- Data incidents are detected by tests or monitors, not by consumers, at least 80% of the time.
- Every data incident has an owner within 1 working hour and a postmortem if it reached a decision-maker or a customer.

## Quality dimensions

| Dimension | Question | Example test |
|---|---|---|
| Completeness | Are required values present? | `customer_id` is never null |
| Validity | Do values follow the rules? | `country` is a valid ISO 3166 code |
| Accuracy | Do values match reality? | sample of addresses matches a trusted source |
| Consistency | Do related data sets agree? | order totals equal the sum of order lines |
| Uniqueness | Are there unwanted duplicates? | one row per `invoice_id` |
| Timeliness | Is the data fresh enough? | latest partition is less than 24 hours old |

Choose the two or three dimensions that matter most for each data set. Testing everything everywhere wastes effort.

## Data contracts

A data contract is an agreement, kept in version control, between the team that produces a data set and the teams that use it. It covers:

- schema, with types and meaning of each field;
- quality rules and service levels (freshness, completeness);
- owner and support contact;
- classification and allowed uses (see [data governance](data-governance.md));
- change process: how breaking changes are announced and how long the old version stays.

Check contracts in the producer's [continuous integration](../delivery/continuous-integration.md) so a breaking change fails the build before it reaches consumers. Version contracts with [Semantic Versioning](../delivery/versioning-and-changelogs.md).

## Testing and monitoring

- **In the pipeline:** run quality tests after each load or transform, before publishing. Open source tools such as Great Expectations, Soda Core and dbt tests are examples.
- **In production:** monitor volume, freshness, null rates and distribution changes. Alert the owning team, not a shared inbox.
- **Lineage:** record where each data set comes from and what depends on it, for example with OpenLineage, so you can find the impact of a failure in minutes.
- **Service levels:** set objectives for freshness and completeness and track them like any other [service level](../reliability/service-levels.md).

## Data quality for AI

AI systems amplify data problems. Before training, fine-tuning or building a retrieval index:

- record the source, date range and known gaps of each data set;
- test for missing groups, label errors and duplicates between training and test sets;
- check that the data is allowed to be used for this purpose;
- keep the exact version used, so results can be reproduced.

In production, monitor input drift and compare it with the training data. See [AI governance](../ai/ai-governance.md).

## Data incidents

Handle data failures with the normal [incident management](../reliability/incident-management.md) process. Severity depends on who used the bad data: a wrong figure in a board pack or a regulatory return is a high-severity incident even if no system was down. Write a [postmortem](../reliability/postmortems.md) and fix the cause at the source.

## Practice

### Foundation

Solo and Startup. Add not-null, uniqueness and freshness tests to the few tables that matter most. Fail the pipeline on test failure. Name an owner for each critical table.

### Standard

Scale-up and Enterprise. Data contracts for every shared data set, checked in CI. Quality tests in every pipeline. Freshness and completeness objectives with alerts to owning teams. Lineage for critical reports and AI systems. Monthly review of data incidents.

### Assured

Regulated and Public sector. Everything in Standard, plus documented data quality controls for regulatory reporting, reconciliation between source systems and reports, evidence of test results kept for the retention period, and independent review of quality controls for data used in high-risk AI systems.

## Cloud, on-premises and air-gapped

The practice is the same everywhere. In air-gapped networks, run quality tools and lineage storage inside the network. Where data moves across a network boundary, check counts and checksums on both sides of the transfer.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Consumers clean data themselves, each in their own way | Fix at the source; publish the rule in the contract. |
| Quality checked by eye before a meeting | Automated tests in the pipeline. |
| Alerts go to a shared mailbox nobody reads | Route to the owning team's on-call. |
| Silent schema changes | Contracts checked in CI. |
| Training data with no record of its source | Version and document every data set used for AI. |

## Templates

- [Data classification](../../templates/docs/data-classification.md)
- [Postmortem](../../templates/docs/postmortem.md)
- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml)

## Sources

- DAMA International, DAMA-DMBOK: https://www.dama.org
- OpenLineage: https://openlineage.io
- EU AI Act, Regulation (EU) 2024/1689, Article 10 (data and data governance): https://eur-lex.europa.eu/eli/reg/2024/1689/oj
- Semantic Versioning 2.0.0: https://semver.org
