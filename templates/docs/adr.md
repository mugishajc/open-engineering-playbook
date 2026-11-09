---
# Architecture decision record, MADR 4.0 layout.
# Save as docs/decisions/NNNN-short-title.md. Delete these comment lines.
# status: proposed | accepted | rejected | deprecated | superseded by ADR-NNNN
status: proposed
date: YYYY-MM-DD
decision-makers: [names or roles, from your decision rights]
consulted: [people or teams whose opinion was sought]
informed: [people or teams told about the outcome]
---

# NNNN. Short title as a decision, for example "Use PostgreSQL for the orders service"

## Context and problem statement

What situation forces a decision now? Describe the problem in 2 to 5 sentences.
State facts and constraints (load, team skills, deadlines, regulation, hosting model).
Link the RFC, incident or ticket that started this.

## Decision drivers

<!-- Optional. Delete for small decisions. -->

- Driver 1, for example "must run air-gapped"
- Driver 2, for example "team of 4 must operate it"
- Driver 3, for example "personal data must stay in-country"

## Considered options

- Option A
- Option B
- Option C
- Do nothing (keep the current approach)

## Decision outcome

Chosen option: "Option A", because it is the only one that meets drivers 1 and 3, and its cost (see below) is acceptable.

### Consequences

- Good, because ...
- Bad, because ... (every ADR names at least one cost or risk)
- Neutral, because ...

### Confirmation

How will we know the decision is being followed and still works?
For example: an architecture test in CI, a review checklist item, a metric with a threshold, a review date.

Review date: YYYY-MM-DD (default 24 months from acceptance)

## Pros and cons of the options

<!-- Optional. Use when there were real alternatives. -->

### Option A

- Good, because ...
- Bad, because ...

### Option B

- Good, because ...
- Bad, because ...

### Option C

- Good, because ...
- Bad, because ...

## More information

<!-- Optional. -->

- Related ADRs: supersedes ADR-NNNN / superseded by ADR-NNNN / related to ADR-NNNN
- RFC: link
- Risk register entry (Assured): ID and owner
- Security and privacy sign-off (Assured): name, date
- Threat model (Assured, if security-relevant): link
