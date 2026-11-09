# Rollbacks

Make every change undoable in minutes, decide between rolling back and rolling forward with a time limit rather than a debate, and practise rollbacks before you need them. The fastest way to end most incidents is to undo the last change. That only works if the change was designed to be undone and the team has done it recently.

## Outcomes

Starting points. Tune them to your services.

- Any production deployment of a Tier 1 or Tier 2 service can be rolled back in under 15 minutes, measured in the last game day.
- When a deployment causes an incident, the decision to roll back or roll forward is made within 15 minutes of linking the incident to the change.
- At least 80% of rollbacks on Tier 1 services are triggered automatically by canary analysis or SLO burn, not by a person.
- Every service runs a rollback drill at least once a quarter.
- Time to rollback (from decision to previous version serving all traffic) is recorded for every rollback and reported monthly.

## Roll back or roll forward

Default to rolling back. Roll forward only when all of these are true.

```text
Is the incident linked to a recent change (code, configuration, content, schema)?
 |
 +-- No  --> follow the incident process; rollback is not the answer.
 |
 +-- Yes --> Can the previous version run safely against the current data and schema?
              |
              +-- No  --> roll forward with a fix, or restore data (see "When rollback is impossible").
              |
              +-- Yes --> Roll back now, unless ALL of these hold:
                           - the fix is known, small and already reviewed,
                           - it can be in production within 30 minutes,
                           - the error budget can absorb 30 more minutes of impact.
                          If someone is still "nearly there" after 30 minutes, roll back.
```

The 30-minute limit is a starting point. Set it per tier, write it in the runbook, and let the incident commander enforce it.

## Practice

### Foundation

1. **Immutable, versioned artifacts.** Every build produces a versioned artifact (container image digest, package version). Rolling back means redeploying the previous artifact, not rebuilding old code.
2. **Keep the last good version deployable.** The pipeline has a one-step "deploy previous version" action. Test it once now.
3. **Separate schema changes from code changes.** Ship the database change first, in its own release, in a backward-compatible form (see [database changes](../delivery/database-changes.md)).
4. **Feature flags as kill switches** for risky features. Turning a flag off is the fastest rollback there is (see [feature flags](../delivery/feature-flags.md)).
5. **Record the time** each rollback takes.

### Standard

1. **Design every change to be rollback-safe.**

   | Change | Rollback-safe pattern |
   |---|---|
   | Database schema | Expand and contract: add new columns or tables first, deploy code that writes both, backfill, switch reads, then remove the old structure in a later release |
   | API | Add fields and endpoints; never remove or change meaning in the same release. Version breaking changes (see [API standards](../architecture/api-standards.md)) |
   | Configuration | Versioned in git, deployed by the pipeline, with the previous version one command away |
   | Content and rules files | Staged rollout with canaries, same as code. The July 2024 CrowdStrike incident came from a content update, not code |
   | Message and event formats | Consumers accept old and new formats before producers switch |
   | Infrastructure | Plan reviewed in the pull request; destructive changes split out and reviewed separately (see [infrastructure as code](../delivery/infrastructure-as-code.md)) |

2. **Automated rollback.** Progressive delivery tools compare the new version against the old on error rate and latency, and roll back without a person. Argo Rollouts and Flagger do this on Kubernetes; most managed deployment services offer a similar feature. As a starting point, hold the canary at 1% of traffic for at least 10 minutes (5% or more if 1% gives too few requests to compare), then increase in steps (see [GitOps and deployment](../delivery/gitops-and-deployment.md)). Abort when the canary's error rate is clearly worse than the baseline's, for example more than twice the baseline rate over the step.
3. **Tie rollback to SLOs.** A fast-burn SLO alert during or within 1 hour of a deployment triggers an automatic or one-click rollback (see [service levels](service-levels.md)).
4. **Game days.** Once a quarter, each team rolls back a production deployment on purpose in working hours, including the database and configuration parts, and times it. Fix what was slow.
5. **Measure.** Track time to rollback and the share of rollbacks that were automatic. These feed failed deployment recovery time (see [metrics](../measurement/metrics.md)).

### Assured

Everything in Standard, plus:

1. **A rollback plan in every normal change** (see [change management](change-management.md)), reviewed with the change and tested in a pre-production environment that has production-like data volume.
2. **Rollback evidence.** Deployment logs show the rollback, who or what triggered it, and when. Auditors use this for ISO/IEC 27001:2022 control 8.32 and SOC 2 CC8.1.
3. **Irreversible changes need a named approver** and a data recovery plan before they start.

## When rollback is impossible

Some changes cannot be undone by redeploying. Plan for them in advance.

| Situation | Approach |
|---|---|
| Mobile apps | Users keep old versions. Use server-side feature flags and remote configuration as the kill switch. Keep APIs backward compatible with every app version still supported. Use staged rollout in the app stores. Support a minimum-version check that can force an upgrade. |
| Firmware and devices | Use A/B partitions so a failed update boots the previous image. Stage rollouts by device cohort. Never ship firmware that cannot accept a further update. |
| Software shipped to customers on-premises | Publish an upgrade path and a tested downgrade or restore path. Back up before upgrade, automatically. Release notes state clearly when a version cannot be downgraded. |
| Destructive data migrations | Take a backup or snapshot right before, test the restore, and keep the old data read-only until the new path is proven for at least one full business cycle. |
| Data sent to third parties, emails, payments | Cannot be recalled. Gate them behind flags and send to a small group first. Plan compensating actions (correction notices, refunds). |

## Cloud, on-premises and air-gapped

- **Keep previous artifacts inside the network.** In air-gapped environments, the registry or mirror must retain at least the last 3 releases of every service; rollback cannot wait for a new transfer.
- **On-premises capacity.** Blue-green deployments need room for two copies of the service. If you lack capacity, use rolling updates with a fast rollback path, and test it.
- **Managed cloud services** sometimes upgrade underneath you and cannot be rolled back. Pin versions where the provider allows it and test upgrades in a non-production environment first.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Rollback means rebuilding an old commit | Redeploy the previous immutable artifact. |
| Schema and code change in one release | Expand and contract across releases. |
| "We are nearly there" for two hours | 30-minute limit, enforced by the incident commander. |
| Rollback never practised | Quarterly drill, timed. |
| Configuration changed by hand on servers | Configuration in git, deployed by the pipeline. |
| Mobile release with no kill switch | Server-side flags and backward-compatible APIs. |

## Templates

- [Runbook](../../templates/docs/runbook.md): include a rollback section.
- [Release checklist](../../templates/docs/release-checklist.md)
- [Production readiness review](../../templates/docs/production-readiness-review.md)

## Sources

- Argo Rollouts documentation: https://argo-rollouts.readthedocs.io/
- Flagger documentation: https://docs.flagger.app/
- Google, *Site Reliability Engineering*, "Release Engineering": https://sre.google/sre-book/release-engineering/
- CrowdStrike, preliminary post-incident review of the 19 July 2024 content update: https://www.crowdstrike.com/en-us/blog/falcon-content-update-preliminary-post-incident-report/
