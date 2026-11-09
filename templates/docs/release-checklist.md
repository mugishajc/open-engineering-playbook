# Release checklist

Use this for any release step that is not yet automated. Each time you tick an item by hand, ask whether CI could do it instead. Aim to automate one item per month until the list is short. Delete items that do not apply to your product.

See [release management](../../playbook/delivery/release-management.md) for the policy behind this list.

| Field | Value |
|---|---|
| Release version | |
| Release date and time (with time zone) | |
| Release owner | |
| Approver (Assured: not the author of the changes) | |
| Change record or ticket | |
| Rollback owner (on call during rollout) | |

## 1. Before the release

- [ ] All changes are merged to `main` (or cherry-picked to `release/x.y` from `main`) and CI is green on the release commit.
- [ ] The release pull request (release-please) is reviewed and the changelog reads well for users.
- [ ] The version follows SemVer: breaking changes only in a major version, and each is listed.
- [ ] Deprecations announced in this release name the replacement and the earliest removal date.
- [ ] The artifact is built by CI, signed, and has an SBOM and provenance. Record the digest: `sha256:`
- [ ] Database migrations are backward compatible with the running version (expand step only). Destructive steps are scheduled for a later release.
- [ ] Migrations were tested on a production-sized dataset. Longest step took: ___ minutes.
- [ ] A backup completed and a restore was tested within the last ___ days (required before any destructive migration).
- [ ] New behaviour is behind a feature flag with a rollout plan and a named owner.
- [ ] Dashboards and alerts for the changed services are open and working.
- [ ] Runbooks and on-call notes are updated for new failure modes and kill switches.
- [ ] Support and customer-facing teams know what is changing and when.
- [ ] No freeze window or major business event overlaps the rollout (check the calendar).

## 2. Rollback criteria (agree before you start)

Roll back first, investigate second, if any of these happen during rollout:

| Signal | Threshold | Window |
|---|---|---|
| Error rate (5xx or failed jobs) | Above ___% or ___ times the previous version | 10 minutes |
| Latency (95th percentile) | Above ___ ms | 10 minutes |
| Error budget burn rate | Above ___ | 1 hour |
| Business metric (for example checkouts per minute) | Below ___ | 15 minutes |
| Any data integrity or security concern | Any | Immediate |

Rollback method: [ ] redeploy previous artifact  [ ] turn off flag `___`  [ ] other: ___

## 3. During the rollout

- [ ] Announce the start in the team channel with version and expected duration.
- [ ] Deploy to staging and run smoke tests.
- [ ] Production canary or first batch at ___%. Watch for ___ minutes against the criteria above.
- [ ] Increase to ___%, then ___%, then 100%, checking criteria at each step.
- [ ] Turn on feature flags in the planned order: internal users, then ___%, then everyone.
- [ ] Record the time each step completed.

## 4. After the release

- [ ] Tag and release notes are published.
- [ ] Release announced to users where they will see it (changelog, status page, email or in-product note).
- [ ] Deployment record updated with version, digest, time and approver.
- [ ] Monitoring watched for ___ hours after reaching 100%.
- [ ] Clean-up issues opened: remove release flags within 30 days of reaching 100%, schedule contract migrations.

## 5. For software customers install (on-premises and LTS)

- [ ] Install and upgrade tested from every supported version on every supported platform.
- [ ] Offline bundle prepared: packages, images, checksums, signatures, SBOM, release notes and verification instructions.
- [ ] Verification works without internet access (cosign key pair or GPG).
- [ ] Security fixes back-ported to every supported LTS line.
- [ ] Support policy page updated with this version's end-of-support date.
- [ ] Security advisories published (CSAF 2.0 or OpenVEX) where this release fixes a vulnerability.

## 6. If you rolled back

- [ ] Roll back, confirm the service is healthy, then announce.
- [ ] Open an incident if users were affected. See [incident management](../../playbook/reliability/incident-management.md).
- [ ] Write down what the criteria caught and what they missed. Update this checklist.
