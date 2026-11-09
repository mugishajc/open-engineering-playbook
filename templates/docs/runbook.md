# Runbook: <service name>

<!--
How to use: one runbook per service, stored next to the code (docs/runbook.md) so it changes
with the service. Every paging alert links to its section here. Keep commands copy-ready.
Review after every incident and at least every 6 months. Keep an offline copy for Tier 1.
Guidance: playbook/reliability/on-call.md and playbook/reliability/production-readiness.md
-->

| Field | Value |
|---|---|
| Service | |
| Tier | Tier 1 / Tier 2 / Tier 3 |
| Owning team | |
| On-call rotation | |
| Escalation | Primary, then secondary after 10 min, then <manager>, then incident commander rotation |
| Last reviewed | YYYY-MM-DD by <name> |
| Last exercised (game day or drill) | YYYY-MM-DD |
| Source repository | |
| Service catalogue entry | |

## What it does

Two or three sentences: what users get from this service, and what breaks for them when it fails.

## Service levels

| SLO | Target | Dashboard |
|---|---|---|
| Availability | 99.9% over 28 days | <link> |
| Latency | 99% of requests under <n> ms | <link> |

## Architecture and dependencies

- Diagram: <link>
- Runs on: <cluster, region, site, hosts>
- Data stores: <name, tier, backup schedule>
- Critical dependencies and what happens when each is down:

| Dependency | If it is down | What to do |
|---|---|---|
| | | |

## Dashboards and logs

- Main dashboard: <link>
- Logs query: `<query>`
- Traces: <link>

## Alerts

One section per paging alert. The alert's `runbook_url` points to the anchor.

### <AlertName>

- **What it means:** <symptom users feel>
- **Declare an incident if:** <impact condition, and the severity>
- **Check first:** <dashboard panel, query, the change feed for recent deploys, flags and configuration>
- **Likely causes:** <ranked list>
- **Mitigate:**
  ```bash
  <copy-ready command>
  ```
- **Confirm it worked:** <metric and expected value within N minutes>
- **Do not:** <the obvious action that makes this worse, and why, for example restarting the primary database>
- **Escalate if:** <condition, and to whom>

## Common procedures

GitOps: each change below is made in Git at <path to the environment directory>. If you must change the cluster directly, the incident commander approves pausing auto-sync for this one Application first, you log it in the incident channel, and you put the change in Git and turn auto-sync back on before the incident closes. Otherwise self-heal reverts your change within minutes. See playbook/delivery/gitops-and-deployment.md.

### Roll back a deployment

Target: under 15 minutes. See playbook/reliability/rollbacks.md. Roll back any recent change on the affected path; you do not need proof it caused the incident.

```bash
# Rollout in progress (canary): return traffic to the stable version at once
kubectl argo rollouts abort <rollout> -n <namespace>
# Otherwise: <command to redeploy the previous version>
# Then revert the change in Git so self-heal does not bring it back
```

How to confirm it worked: <metric or check>.

### Disable a feature (kill switch)

```bash
<flag command>
```

### Scale up or down

```bash
<command>
```

### Restore data from backup

RPO <n>. RTO for failover <n>; RTO for restore from backup <n>. Last restore test at production size: YYYY-MM-DD, took <n>.

```bash
<restore command, to an isolated target first>
```

### Rotate credentials

```bash
<command>
```

### Fail over to another region or site

Steps, who approves, how to fail back.

## Using AI assistants during an incident

<!-- Delete this section if your organisation does not allow assistants in operations.
Guidance: playbook/ai/ai-engineering-practices.md and playbook/ai/ai-application-security.md -->

Approved assistant for operations: <tool, and the data classes it may see>. It runs under its own identity, not yours, with read-only access.

Allowed without asking (read-only):

- Summarise the alert, recent deployments and the change log for this service.
- Query dashboards, logs and traces through <read-only integration>, and explain what the results show.
- Search this runbook, past postmortems and decision records for similar incidents.
- Draft the incident update for a human to edit (see the incident update template).

Always done by a human, never by the assistant:

- Any command in this runbook that changes state: rollback, failover, scaling, flag changes, restores, credential rotation.
- Running a command the assistant suggested. Read it, check it against this runbook, then run it yourself.
- Declaring, downgrading or closing an incident, and any message sent to customers or regulators.
- Granting or using elevated access.

Do not paste secrets, tokens or customer personal data into the assistant. If logs contain them, use the masked view.

Record in the incident timeline: each assistant suggestion that you acted on, what you checked before acting, and the outcome. Note suggestions that were wrong; they go into the postmortem and help tune the tool.

## Access needed

What access an on-call engineer needs, and how to get it just in time.

## Known issues

| Issue | Workaround | Ticket |
|---|---|---|
| | | |
