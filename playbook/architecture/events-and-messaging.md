# Events and messaging

Use a message broker only when work can finish later or another team must react to a change, and then assume every message can be lost, delivered twice or delivered out of order. Publish through a transactional outbox, make every consumer idempotent in the same transaction as its side effect, and send messages that keep failing to a dead-letter queue that someone watches. Without these three controls, events move failures from a visible error to silent missing or duplicated data, such as a second payment or an order nobody ships.

## Outcomes

Starting points. Tune them to your volumes and business risk.

- 100% of services that change their database and publish an event do it through an outbox, not two separate writes.
- 100% of consumers deduplicate on the event ID inside the same transaction as their side effect.
- Every queue and topic has an owner, a dead-letter queue, an alert on dead-lettered messages and an alert on the age of its oldest unprocessed message.
- No dead-lettered message waits more than 1 working day for a decision: replay, fix or discard with a reason.
- Every event type has a schema in the registry, and no incompatible change reaches production.

## Event, command or request

| Message | Meaning | Who decides | Example |
|---|---|---|---|
| Request (synchronous call) | "Answer me now" | The caller waits | Check stock before showing the basket |
| Command | "Please do this" | One named receiver | `ChargeCard` sent to payments |
| Event | "This happened" | Each subscriber decides for itself | `OrderPlaced`, read by billing, email and analytics |

Use a synchronous call when the user waits for the answer. Use a command when exactly one service must act. Use an event when the publisher should not know who reacts. An event named like an instruction (`SendWelcomeEmail`) is a command in disguise.

## Rules

### Publishing: the transactional outbox

A service cannot write to its database and to a broker in one atomic step. If it writes the database and then crashes, the event is lost. If it publishes first and the transaction then rolls back, consumers act on something that never happened.

1. In the same database transaction as the state change, insert the event into an `outbox` table.
2. A relay reads the outbox in order and publishes to the broker. It can poll the table, or read the database change log with a change data capture tool (Debezium is one open source example).
3. The relay marks or deletes rows only after the broker confirms. It may publish a row twice after a crash, which is why consumers deduplicate.
4. Alert when the oldest unpublished outbox row is older than 1 minute (starting point).

### Consuming: idempotent, in one transaction

- Brokers deliver at least once. Treat "exactly once" claims as exactly once inside the broker, not for your database or for emails and payments.
- Keep an `inbox` (processed events) table. In one transaction: check the event ID, apply the change, record the ID. A crash between a side effect and the record repeats the side effect.
- Keep processed IDs for longer than the broker's longest redelivery window (starting point: 7 days).
- For side effects outside your database (email, payment, partner call), pass the event ID to the other system as its idempotency key. See [API standards](api-standards.md#idempotency).

### Ordering

- Guarantee order only per key. Partition by the entity ID (order ID, account ID) so all events for one entity go to one partition, and one consumer handles them in sequence.
- Never rely on order across keys or across topics.
- Put a version number or timestamp from the source in every event. A consumer ignores an event older than the state it already holds.

### Retries, dead letters and back-pressure

- Retry with exponential backoff and jitter, capped at 5 attempts (starting point). Then move the message to a dead-letter queue.
- Alert on every dead-lettered message for money, orders and identity. For other flows, alert on a count per hour.
- Build the replay tool before you need it: list, inspect, replay one, replay a batch, discard with a reason. Log who did what.
- Alert on the age of the oldest message, not only on queue depth. A queue of 10 messages that are 3 hours old is an incident; 10,000 messages that are 2 seconds old may be normal.
- When consumers fall behind, slow producers (rate limits, smaller batches) rather than letting the backlog grow until storage or the retention period runs out.
- Set the broker's retention longer than your longest expected outage plus the time to recover (starting point: 7 days), or messages expire before anyone can replay them.

### Schemas and versions

- Describe every event with a schema (AsyncAPI, JSON Schema, Avro or Protobuf) in a schema registry that checks compatibility on publish. Use backward compatibility as the default mode.
- Add fields as optional. Never remove or rename a field, or change its meaning, in place. A breaking change is a new event type or a new major version in the type name, with the notice periods in [API standards](api-standards.md#versioning-and-deprecation).
- Use the CloudEvents attributes (`id`, `source`, `type`, `time`) as the envelope, so tools and consumers can read any event the same way.

### Processes that span services: sagas

A business process across several services (order, payment, stock, shipping) cannot use one database transaction. Model it as a saga: a sequence of local transactions, each with a compensating action that undoes its effect (refund the payment, release the stock).

| Style | How | Choose when |
|---|---|---|
| Choreography | Each service reacts to the previous service's event | 2 to 3 steps, one team, the flow rarely changes |
| Orchestration | One coordinator sends commands and tracks state | 4 or more steps, several teams, or you must answer "where is this order?" |

Write the compensating action for every step before you build the happy path. Some steps cannot be undone (an email sent, goods shipped): put them last.

## Practice

### Foundation

- Prefer a database table used as a queue, or one managed queue service, over running a broker cluster. Most small systems need durable background jobs, not event streaming.
- Even then: outbox, idempotent consumers, a retry cap and a dead-letter queue.

### Standard

- A schema registry with compatibility checks in CI and on publish.
- Dashboards per queue: publish rate, consume rate, oldest message age, dead-lettered count, outbox lag.
- A contract test for each event type between publisher and its main consumers.
- A game day each year that stops a consumer for an hour and checks that it catches up, that alerts fire, and that nothing is lost or duplicated. See [resilience testing](../reliability/resilience-testing.md).

### Assured

- Reconciliation jobs run daily for money, stock and identity flows: compare the source of truth with each downstream copy and alert on any difference. They are a standing control, not only a migration tool.
- Keep an audit trail of every replay and discard from a dead-letter queue, with the person and the reason.
- Classify event payloads like any other data store. Personal data in events lives as long as the broker's retention and every consumer's copy. See [data security and privacy](../data/data-security-and-privacy.md).

## Cloud, on-premises and air-gapped

- Managed queues and streams (for example Amazon SQS and SNS, Azure Service Bus, Google Pub/Sub) remove broker operations. The rules above still apply: they all deliver at least once in their default modes.
- On-premises and air-gapped sites usually run Apache Kafka, RabbitMQ or NATS. Plan disk for the retention period, replicate across at least 3 nodes in separate failure domains, and test broker upgrades like any Tier 1 change.
- Across a one-way transfer boundary, move batches of messages as files with a manifest and checksum, and process them with the same deduplication rules.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Write to the database, then publish to the broker | Transactional outbox. |
| Consumer checks "seen before?" in one step and acts in another | Record the ID and apply the change in one transaction. |
| Retry forever | Cap retries, then dead-letter with an alert. |
| Dead-letter queue nobody reads | Owner, alert and a 1-working-day decision rule. |
| Alerting on queue depth only | Alert on oldest message age. |
| Events that carry a whole database row "in case someone needs it" | Publish what happened and the fields consumers need. Large payloads leak data and couple teams. |
| A saga with no compensating actions | Write the undo step for each step first. |

## Templates

- [RFC template](../../templates/docs/rfc.md), for a new event type or a change in delivery guarantees
- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml), which lists the APIs and events a component provides and consumes

## Sources

- Hector Garcia-Molina and Kenneth Salem, "Sagas", ACM SIGMOD 1987: https://dl.acm.org/doi/10.1145/38713.38742
- Chris Richardson, transactional outbox pattern: https://microservices.io/patterns/data/transactional-outbox.html
- Debezium outbox event router: https://debezium.io/documentation/reference/stable/transformations/outbox-event-router.html
- CloudEvents specification: https://cloudevents.io/
- AsyncAPI Specification 3.0: https://www.asyncapi.com/docs/reference/specification/v3.0.0
- Apache Kafka documentation, partitions and ordering: https://kafka.apache.org/documentation/
- Amazon SQS, dead-letter queues: https://docs.aws.amazon.com/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-dead-letter-queues.html
