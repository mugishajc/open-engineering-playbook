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
- **Check first:** <dashboard panel, query, recent deployments>
- **Likely causes:** <ranked list>
- **Mitigate:**
  ```bash
  <copy-ready command>
  ```
- **Escalate if:** <condition, and to whom>

## Common procedures

### Roll back a deployment

Target: under 15 minutes. See playbook/reliability/rollbacks.md.

```bash
<command to redeploy the previous version>
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

RPO <n>, RTO <n>. Last restore test: YYYY-MM-DD.

```bash
<restore command, to an isolated target first>
```

### Rotate credentials

```bash
<command>
```

### Fail over to another region or site

Steps, who approves, how to fail back.

## Access needed

What access an on-call engineer needs, and how to get it just in time.

## Known issues

| Issue | Workaround | Ticket |
|---|---|---|
| | | |
