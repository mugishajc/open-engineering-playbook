# Change management

Replace the weekly change advisory board (CAB) for routine changes with automated controls that run on every change: peer review, passing CI, and a deployment pipeline that records who changed what and when. These controls catch more problems than a meeting reading change tickets, and they produce the evidence auditors need for ISO/IEC 27001:2022 control 8.32 and SOC 2 CC8.1 as a side effect. Keep human approval boards for the small number of changes that are risky across teams.

## Outcomes

Starting points. Tune them to your risk.

- 100% of production changes go through version control and the deployment pipeline. Changes made by hand in production are zero, outside declared emergencies.
- 100% of merged changes have at least one approving reviewer who is not the author.
- At least 90% of production changes are classed as standard and need no meeting.
- Every emergency change has a retrospective review within 2 working days.
- For any production deployment, the change record (pull request, reviewer, CI run, deployer, time) can be produced in under 5 minutes.
- Change fail rate and failed deployment recovery time are reported monthly (see [metrics](../measurement/metrics.md)).

## Why the weekly CAB goes

The research programme behind the DORA metrics found that approval by an external body, such as a manager or a CAB, did not improve stability and was linked to slower delivery. Peer review plus automated testing did better. Large changes batched for a weekly meeting are harder to review, harder to roll back and fail more often. Small changes reviewed by people who understand the code are safer.

Neither ISO/IEC 27001 nor SOC 2 requires a CAB. Both require that changes are controlled: planned, tested, approved, recorded and reversible.

## Change types

| Type | What it covers | Approval | Example |
|---|---|---|---|
| Standard | Low-risk, repeatable, pre-approved by policy. Goes through the normal pipeline. | Peer review by someone other than the author, plus green CI. No meeting. | Application release, dependency update, configuration change behind a feature flag |
| Normal | Higher risk, unusual, or affects other teams. | Standard controls, plus a second reviewer from the affected team or platform, plus a written rollback plan. Scheduled. | Schema migration on a large table, network or firewall change, change to authentication, new data flow to a third party |
| Emergency | Needed now to stop or prevent harm during an incident. | Incident commander approves. One reviewer if available; otherwise reviewed after. | Hotfix during a SEV1, blocking an attacking IP range |

Teams move a change type from normal to standard by showing a track record: for example 10 successful changes of that type with automated tests and rollback.

## Practice

### Foundation

1. **Everything in version control.** Application code, infrastructure as code, configuration and database migrations (see [source control](../delivery/source-control.md)).
2. **Protected main branch.** No direct pushes. Every change merges by pull request with at least one approval and passing checks (see [code review](../delivery/code-review.md)).
3. **Deploy from the pipeline only.** Production credentials live in the pipeline, not on laptops.
4. **Small changes.** Aim for pull requests under 400 changed lines. Small changes are easier to review and roll back.
5. **Know how to undo.** Every deployment can be rolled back by redeploying the previous version (see [rollbacks](rollbacks.md)).

### Standard

1. **Automated controls replace the meeting** for standard changes:

   | Control | How it runs | Evidence it produces |
   |---|---|---|
   | Peer review | Branch protection or ruleset requires 1 approval (2 for sensitive paths via CODEOWNERS); author cannot approve own change | Pull request with reviewer, comments, approval time |
   | Automated tests and checks | CI must pass: build, tests, security scans, policy checks (see [continuous integration](../delivery/continuous-integration.md)) | CI run linked to commit SHA |
   | Traceability | Pull request links to an issue or ticket; commit message follows a convention | Ticket to pull request to commit to deployment chain |
   | Controlled deployment | Pipeline deploys an immutable, signed artifact; progressive rollout with automatic rollback on SLO breach | Deployment log with artifact digest, environment, time, actor |
   | Separation of duties | Author cannot merge without another approval; pipeline, not the author, holds production credentials | Ruleset configuration and audit log |
   | Change calendar | Generated from deployment logs, not typed by hand | Searchable list of changes per service |

2. **Configuration and content are changes.** Feature flag changes, rule files, routing tables and content pushes go through review and staged rollout. The July 2024 CrowdStrike Falcon incident came from a content configuration update that crashed Windows hosts worldwide. The vendor's own review commits to a staggered deployment for that content, starting with a canary.
3. **Normal changes** get a short written plan in the pull request: risk, rollback steps, who is watching, when. No meeting unless reviewers ask for one.
4. **Emergency changes** are labelled in the pipeline. A second engineer reviews within 2 working days and records the outcome.
5. **Freezes are rare and short.** Freezes push changes into a big batch afterwards. If you freeze (for example around a national tax deadline), keep it to a few days and never more than 2 weeks, let security and incident fixes through as emergency changes, and restart with small batches. See [release management](../delivery/release-management.md).
6. **Use the change data.** Once a month, look at change fail rate by service and change type. Services with high failure rates get more controls; reliable change types get fewer.

### Assured

Everything in Standard, plus:

1. **Control mapping.** Write down how each automated control meets each requirement:

   | Requirement | Met by |
   |---|---|
   | ISO/IEC 27001:2022 8.32 Change management: changes are subject to change management procedures | Branch rulesets, CI gates, pipeline-only deployment, change type policy |
   | ISO/IEC 27001:2022 8.31 Separation of development, test and production environments | Separate accounts or clusters; production credentials only in the pipeline |
   | SOC 2 CC8.1: changes are authorised, designed, developed, configured, documented, tested, approved and implemented | Ticket link (authorised), pull request (designed, documented), CI (tested), approval (approved), deployment log (implemented) |

   See [control mapping](../compliance/control-mapping.md) for the wider map.
2. **No silent bypass.** Administrators are not exempt from rulesets. Every bypass is logged and alerted. A bypass outside a declared incident is reviewed within 1 working day, because it has no incident to explain it; an emergency change during an incident follows the 2-working-day rule above.
3. **Evidence on demand.** A script or report produces, for any period, each production deployment with its pull request, reviewers, CI run and deployer. Auditors sample from it instead of asking engineers for screenshots.
4. **Retention.** Keep change records for at least 12 months, or as long as your regulator requires.
5. **A risk-based board, not a weekly one.** If a regulator or policy requires a CAB, use it for normal changes that cross teams and for reviewing change data monthly. Standard changes are pre-approved by the board through the policy itself.

## Cloud, on-premises and air-gapped

- The same controls work on GitLab self-managed, GitHub Enterprise Server, Gitea or Forgejo, and Bitbucket Data Center. Each supports protected branches and required approvals.
- **Air-gapped transfers.** When artifacts cross into an isolated network, the transfer is a change. Sign artifacts on the connected side, verify signatures on the isolated side, and log both (see [supply chain](../security/supply-chain.md)).
- **Vendor-delivered changes** to on-premises products (patches, appliance updates) go through the normal change type with a test environment first.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Weekly CAB reads 80 tickets in an hour | Pre-approve standard changes by policy. Keep the board for cross-team risk. |
| Approval by a manager who did not read the code | Approval by a peer who did. |
| Change tickets typed by hand after the deployment | Generate change records from the pipeline. |
| Admins bypass branch protection "just this once" | No exemptions; bypasses alert and get reviewed. |
| Long freezes before holidays | Short freezes, small batches, fast rollback. |
| Configuration pushed to every host at once | Staged rollout for configuration and content, same as code. |

## Templates

- [Pull request template](../../templates/github/PULL_REQUEST_TEMPLATE.md)
- [Default branch ruleset](../../templates/github/rulesets/default-branch.json)
- [CODEOWNERS](../../templates/github/CODEOWNERS)
- [Release checklist](../../templates/docs/release-checklist.md)

## Sources

- DORA, capability "Streamlining change approval": https://dora.dev/capabilities/streamlining-change-approval/
- ISO/IEC 27001:2022, Annex A controls 8.31 and 8.32: https://www.iso.org/standard/27001
- AICPA, Trust Services Criteria (CC8.1): https://www.aicpa-cima.com/resources/download/2017-trust-services-criteria-with-revised-points-of-focus-2022
- CrowdStrike, preliminary post-incident review of the 19 July 2024 content update: https://www.crowdstrike.com/en-us/blog/falcon-content-update-preliminary-post-incident-report/
