# API standards

Describe every API in a machine-readable contract before you build it: OpenAPI 3.1 for HTTP APIs and AsyncAPI for event-driven ones. Apply one set of conventions for errors, pagination, idempotency, versioning and rate limits across the organisation, and check them in CI. Consumers then learn one pattern instead of one per team, and breaking changes are caught by a tool before a customer finds them.

## Outcomes

Starting points. Tune them to your organisation.

- 100% of APIs that other teams or customers call have a contract in the repository, linted in CI.
- Zero unannounced breaking changes reach production. CI blocks them unless the version changes.
- 100% of error responses use the Problem Details format (RFC 9457).
- API review for a new or changed API completes within 3 working days.
- Deprecated endpoints carry `Deprecation` and `Sunset` headers for the whole notice period.

## Conventions

### Contracts

| Kind of API | Contract format | Checks in CI |
|---|---|---|
| HTTP (REST) | OpenAPI 3.1 | Lint against the house ruleset (for example with Spectral). Diff against the main branch to detect breaking changes (for example with oasdiff). |
| Events and messages | AsyncAPI 3.0, with CloudEvents 1.0 as the envelope | Lint. Check schema compatibility against the schema registry. |
| gRPC | Protocol Buffers | Lint and breaking-change detection (for example with `buf`). |

The contract lives in the same repository as the service and changes in the same pull request as the code. Generate documentation and client code from it. Do not maintain them by hand.

### HTTP resources

- Paths are lowercase, plural nouns: `/v1/invoices/{invoiceId}/lines`. Actions that do not fit CRUD use a sub-resource or a verb suffix, chosen once for the organisation: `POST /v1/invoices/{id}:cancel` or `POST /v1/invoices/{id}/cancellation`.
- Pick one field naming style (`camelCase` or `snake_case`) for the whole organisation and enforce it in the linter.
- Use HTTP methods and status codes as RFC 9110 defines them. `GET` never changes state. `PUT` and `DELETE` are idempotent.
- Timestamps are RFC 3339 strings in UTC: `2026-03-01T09:30:00Z`. Dates without times are `YYYY-MM-DD`.
- Money is an object with a decimal string amount and an ISO 4217 currency code: `{"amount": "1250.00", "currency": "EUR"}`. Never a float. Use the number of decimal places ISO 4217 sets for each currency: two for EUR, KES and USD, none for JPY or RWF, three for BHD and KWD. Reject amounts with more places than the currency allows.
- Identifiers are opaque strings. Clients must not parse them.

### Errors

Every error response uses Problem Details for HTTP APIs (RFC 9457) with media type `application/problem+json`.

```json
{
  "type": "https://api.example.org/problems/insufficient-credit",
  "title": "Insufficient credit",
  "status": 422,
  "detail": "The order total 1250.00 EUR exceeds the remaining credit of 900.00 EUR.",
  "instance": "/v1/orders/ord_8f2k",
  "traceId": "4bf92f3577b34da6a3ce929d0e0e4736",
  "errors": [{ "pointer": "#/total/amount", "detail": "Exceeds credit limit" }]
}
```

- `type` is a stable URI per problem kind, documented in the API reference. Clients branch on `type`, never on `detail` text.
- Include the trace identifier (see [observability](observability.md)) so support can find the request.
- Never return stack traces, SQL or internal hostnames.

### Pagination

- Default to cursor pagination: the response returns `nextPageToken` (or `next_page_token`), the client sends it back as `pageToken`. An empty or missing token means the last page.
- Default page size 20, maximum 100 (starting points). Requests above the maximum are capped, not rejected.
- Offset pagination is acceptable only for small lists that rarely change.
- Do not return a total count by default. It is expensive on large tables. Offer it as an opt-in field.

### Idempotency

- Every `POST` that creates a resource, moves money or sends a message accepts an `Idempotency-Key` header. The IETF HTTPAPI working group has a draft standard for this header. Follow it.
- The server stores the key, a fingerprint of the request body and the response for at least 24 hours.
- Same key, same body: return the stored response. Same key, different body: reject with an error (the draft suggests 422). Same key while the first request is still running: reject with 409.
- Event consumers are idempotent too. Deduplicate on the CloudEvents `id` plus `source`, because brokers deliver at least once.

### Rate limits

- Return `429 Too Many Requests` (RFC 6585) with a `Retry-After` header when a client exceeds its limit.
- Publish limits per client tier in the API reference. Expose remaining quota in response headers. The IETF draft `RateLimit` and `RateLimit-Policy` header fields are the direction to follow.
- Clients retry with exponential backoff and jitter, and honour `Retry-After`.

### Versioning and deprecation

- Additive changes do not need a new version: new optional fields, new endpoints, new enum values that clients were told to expect.
- Breaking changes need a new major version: removing or renaming a field, changing a type, making an optional field required, changing error `type` values, tightening validation.
- Public HTTP APIs put the major version in the path (`/v1/`). Internal APIs may do the same or version by media type. Pick one per organisation.
- Event schemas evolve only in backward-compatible ways. A breaking change is a new event type or a new major version in the type name.
- Announce deprecation with the `Deprecation` header (RFC 9745) and the removal date with the `Sunset` header (RFC 8594). Link the migration guide with a `Link` header.

| Consumer | Minimum notice from deprecation to removal (starting point) |
|---|---|
| Public or paying customers | 12 months |
| Partners and other organisations | 6 months |
| Internal teams | 3 months, or until the last caller has migrated, whichever is longer |

### Security

- Authenticate with OAuth 2.0 or OpenID Connect for users, and mutual TLS or short-lived tokens for services. No API keys in URLs.
- Authorise every request at object level. Broken object-level authorisation tops the OWASP API Security Top 10.
- TLS 1.2 or later on every hop, including inside the network.

## Practice

### Foundation

- OpenAPI contract in the repository for every API with an outside caller. Lint it in CI.
- Use the Problem Details format and the pagination and idempotency rules above.
- Breaking changes need a new version. One person reviews the contract change.

### Standard

- A house linter ruleset encodes these conventions. Every repository uses it through the [golden path](../platform/golden-paths.md).
- Breaking-change detection blocks merges unless the major version changes.
- API review: an API guild of 3 to 6 engineers reviews new APIs and major versions. Target 3 working days.
- APIs and event schemas are registered in the service catalogue (see the [catalogue entry template](../../templates/docs/service-catalog-entry.yaml)) with owner and lifecycle.
- A schema registry holds event schemas and enforces compatibility on publish.

### Assured

- API review sign-off is recorded in the pull request and includes security review for any API that handles personal or financial data.
- Every API states data classification, retention and the legal basis for any personal data it returns.
- Access logs for APIs in scope for audit are retained for the period your regulator requires, kept separate from application logs.
- Public sector: publish public APIs with open standards (OpenAPI), as the UK Technology Code of Practice and similar codes expect.

## Cloud, on-premises and air-gapped

- Gateways: a managed API gateway on public cloud, or a self-hosted gateway on-premises. The conventions do not change.
- Air-gapped: vendor the linter rulesets and tools into the internal registry. Host the schema registry (for example Apicurio Registry) and the API portal inside the network. Problem `type` URIs must resolve on the internal network, or at least be documented there.
- Clients across a one-way transfer boundary cannot get synchronous answers. Use file or message exchange with idempotent processing and explicit acknowledgement files.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Contract written after the code, or never | Contract in the same pull request. CI fails when code and contract disagree. |
| `200 OK` with `{"error": ...}` in the body | Real status codes and Problem Details. |
| Retries that create duplicate payments | `Idempotency-Key` on every unsafe `POST`. Test the retry path. |
| Silent breaking change in a "minor" release | Automated breaking-change detection in CI. |
| Deprecation announced only in a chat message | `Deprecation` and `Sunset` headers, changelog entry, direct notice to known consumers. |
| Each team designs its own error shape | One ruleset, enforced by the linter. |

## Templates

- [RFC template](../../templates/docs/rfc.md), for new public APIs and major versions
- [Service catalogue entry](../../templates/docs/service-catalog-entry.yaml), which lists the APIs a component provides and consumes

## Sources

- OpenAPI Specification 3.1: https://spec.openapis.org/oas/v3.1.0
- AsyncAPI Specification 3.0: https://www.asyncapi.com/docs/reference/specification/v3.0.0
- CloudEvents specification: https://cloudevents.io/
- RFC 9457, Problem Details for HTTP APIs: https://www.rfc-editor.org/rfc/rfc9457
- RFC 9110, HTTP Semantics: https://www.rfc-editor.org/rfc/rfc9110
- RFC 6585, Additional HTTP Status Codes (429): https://www.rfc-editor.org/rfc/rfc6585
- RFC 8594, The Sunset HTTP Header Field: https://www.rfc-editor.org/rfc/rfc8594
- RFC 9745, The Deprecation HTTP Response Header Field: https://www.rfc-editor.org/rfc/rfc9745
- IETF draft, The Idempotency-Key HTTP Header Field: https://datatracker.ietf.org/doc/draft-ietf-httpapi-idempotency-key-header/
- IETF draft, RateLimit header fields for HTTP: https://datatracker.ietf.org/doc/draft-ietf-httpapi-ratelimit-headers/
- OWASP API Security Top 10 (2023): https://owasp.org/API-Security/
- Kubernetes deprecation policy, a worked example of version support windows: https://kubernetes.io/docs/reference/using-api/deprecation-policy/
