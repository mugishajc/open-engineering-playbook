# Feature flags

Use feature flags to separate deploying code from releasing behaviour, so unfinished work can merge to `main` and new behaviour can reach users gradually and be turned off in seconds. Every flag has an owner, a type and an expiry date, because old flags turn into untested code paths and hidden configuration. Treat a flag change in production as a production change.

## Outcomes

Starting targets. Tune them to your flag volume.

| Signal | Starting target |
|---|---|
| Release flags removed after full rollout | Within 30 days of reaching 100% |
| Flags past their expiry date | Zero; each one has an issue and an owner |
| Time to turn off a misbehaving feature | Under 5 minutes, without a deploy |
| Active release flags per team | Under 20; more is a signal to clean up |
| Flags with a named owner and type | 100% |
| Production flag changes with an audit record | 100% at Standard and above |

## Flag types

| Type | Purpose | Expected life | Example |
|---|---|---|---|
| Release | Hide unfinished or new behaviour while it rolls out | Days to weeks | `checkout-new-address-form` |
| Experiment | Compare variants with measured outcomes | Weeks | `pricing-page-variant` |
| Operational (kill switch) | Turn off an expensive or risky path under load or failure | Long-lived, reviewed every 6 months | `disable-pdf-generation` |
| Permission or entitlement | Turn features on per customer, plan or region | Long-lived; this is product configuration, so model it as such | `tenant-has-advanced-reports` |

Do not mix types. A release flag that becomes a permission flag needs a new name, an owner and tests.

## Practice

### Foundation

- **Start simple.** A config file or environment variable read at startup is a feature flag. Move to a flag service when you need per-user targeting, gradual rollout or changes without a restart.
- **Safe default.** If the flag service is unreachable, every flag falls back to its safe value in code, usually "off" for new behaviour and "on" for kill switches that protect the system.
- **Name and register every flag** with owner, type, creation date and expiry date.
- **Test both paths.** CI runs tests with the flag on and off for any flag that changes behaviour.
- **Remove the flag** once the feature is fully released: delete the flag, the old code path and its tests in one pull request. Add the clean-up issue when you create the flag.
- **Keep secrets and permissions out of flags.** A flag is not an access control. Authorisation checks stay in code. See [access control](../security/access-control.md).

### Standard

- **Use a vendor-neutral API.** Code against OpenFeature so you can change flag providers without changing application code. Self-hostable options include flagd, Flagsmith and GrowthBook; managed services exist for teams that prefer them.
- **Gradual rollout.** Internal users, then 1%, 10%, 50%, 100%, with health checks at each step. Use stable bucketing (by user or tenant ID) so a user does not flip between variants.
- **Expiry enforcement.** CI or a scheduled job lists flags past their expiry date and opens issues for the owners. A flag more than 30 days past expiry blocks new flags for that team until cleaned up.
- **Audit log.** Every production flag change records who, when, old value, new value and reason.
- **Flags in incidents.** Kill switches are listed in the service runbook. On-call engineers may turn them off without approval. See [incident management](../reliability/incident-management.md).
- **Observability.** Tag logs, metrics and traces with the flag variants that served the request, so you can compare error rates per variant. See [observability](../architecture/observability.md).
- **Limit nesting.** No flag depends on another flag. If you need it, the design is wrong.

### Assured

- **Flag changes follow change management.** A production flag change that releases new behaviour to customers needs the same approval as a deploy, unless the change was pre-approved as part of the release plan with a defined rollout schedule. Kill switches used in an incident are exempt and reviewed afterwards. See [change management](../reliability/change-management.md).
- **Separation of duties.** The engineer who built the feature does not approve its release to all users.
- **Retain flag audit logs** for your records retention period and include them in change evidence. This supports ISO/IEC 27001:2022 Annex A 8.32 and SOC 2 CC8.1.
- **Regulatory features** (consent screens, data retention, accessibility changes) are not released by flag to a subset of users unless the law allows the old and new behaviour to co-exist.

## Cloud, on-premises and air-gapped

- Run the flag service inside the network (flagd, Flagsmith and GrowthBook can be self-hosted). Applications must not call an external flag service from an air-gapped network.
- For software customers install, ship flags as configuration that the customer's administrator controls, with documented defaults. Do not phone home for flag values.
- Cache flag values locally in each service so that a flag service outage does not take the application down.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Hundreds of flags nobody understands | Owner, type and expiry on every flag. Clean-up issue at creation. |
| Flag used as a permanent "if customer X" switch | Model entitlements as product configuration with tests. |
| Flag service outage takes down the app | Safe defaults in code and local caching. |
| Only the "on" path is tested | CI runs both paths until the flag is removed. |
| Flags that depend on flags | One flag per decision. Redesign. |
| Feature turned on for everyone with no audit trail | Audit log and change records for production flag changes. |

## Templates

- [Release checklist with flag rollout steps](../../templates/docs/release-checklist.md)
- [Runbook (list kill switches here)](../../templates/docs/runbook.md)

## Sources

- OpenFeature specification: https://openfeature.dev/specification/
- Pete Hodgson, Feature Toggles (aka Feature Flags): https://martinfowler.com/articles/feature-toggles.html
- flagd: https://flagd.dev/
- GrowthBook documentation: https://docs.growthbook.io/
- Flagsmith documentation: https://docs.flagsmith.com/
