# Incident update templates

<!--
How to use: the communications lead copies the matching block into the incident channel,
status page or customer email. Every update states when the next one will come.
Cadence (starting points): SEV1 internal every 30 min, external within 30 min then every 60 min;
SEV2 internal every 60 min, external within 60 min if customers are affected, then every 2 hours.
Guidance: playbook/reliability/incident-management.md
Times are in UTC. Replace everything in <angle brackets>.
-->

## Internal update

Post in the incident channel and the engineering announcements channel.

```text
[<SEV1|SEV2|SEV3>] <short title>: update <n> at <HH:MM> UTC

Status: <Investigating | Identified | Mitigating | Monitoring | Resolved>
Impact: <who is affected, what they cannot do, since when>
Current action: <what we are doing now, e.g. rolling back release 2026.11.09-3>
Decisions since last update: <e.g. failed over to site B at HH:MM>
Help needed: <e.g. a database engineer for the payments cluster | none>
Roles: IC <name>, Ops lead <name>, Comms <name>, Scribe <name>
Next update: <HH:MM> UTC or sooner if status changes
```

## Incident commander handover

Use when handing the IC or operations lead role to someone else. In a SEV1 longer than 4 hours, hand over at least every 4 to 6 hours. Post in the incident channel; the scribe logs it.

```text
IC handover at <HH:MM> UTC: <from> to <to>
Current status: <Investigating | Identified | Mitigating | Monitoring>
Impact now: <who is affected, what they cannot do>
Mitigation in progress: <what, who, expected result by HH:MM>
Decisions made: <with times>
Decisions pending: <what, by when, who decides>
Manual changes in force: <for example auto-sync paused on <app> at HH:MM | none>
Roles: Ops lead <name>, Comms <name>, Scribe <name>
Next update due: <HH:MM> UTC
Open questions: <list>
<to>: "I have command."
```

## Executive update

Send to the executive contact list for SEV1, and for SEV2 lasting over 2 hours.

```text
Subject: [<SEV1|SEV2>] <service> incident: <one-line status>

What is happening: <one sentence, no jargon>
Customer impact: <number or share of customers, which feature, since HH:MM UTC>
Regulatory or contractual exposure: <none known | possible personal data breach: legal informed at HH:MM>
What we are doing: <one sentence>
Expected next milestone: <e.g. rollback complete by HH:MM UTC>
Next update: <HH:MM> UTC
Incident commander: <name, phone>
```

## External updates (status page or customer email)

The communications lead or IC posts these without further approval. Set the component state each time: operational, degraded performance, partial outage or major outage. Plain language. Say what customers experience, not what broke internally. No blame on people or suppliers. Do not guess at causes or promise times you cannot meet.

### Investigating

```text
<Service or feature> - Investigating
We are investigating reports that <customers cannot sign in | payments are failing | pages load slowly>
since <HH:MM> UTC. We will post an update by <HH:MM> UTC.
```

### Identified

```text
<Service or feature> - Identified
We have found the cause of <the problem> affecting <which customers or regions> and are working on a fix.
<Workaround, if any.> Next update by <HH:MM> UTC.
```

### Monitoring

```text
<Service or feature> - Monitoring
A fix was applied at <HH:MM> UTC and <service> is working normally again. We are monitoring to make
sure the problem does not return. Next update by <HH:MM> UTC.
```

### Resolved

```text
<Service or feature> - Resolved
Between <HH:MM> and <HH:MM> UTC on <date>, <what customers experienced>. The problem is resolved.
<If data was affected: what happened to customer data and what customers need to do, if anything.>
We will publish a summary of what happened and what we are changing <within 5 working days | by date>.
We are sorry for the disruption.
```

## Regulatory notification checklist

Open at declaration when personal data, a security breach or a product vulnerability may be involved. Legal or the data protection officer decides whether to report; the communications lead makes sure they know early.

| Check | Answer |
|---|---|
| Time the organisation became aware (clocks start here) | |
| Personal data possibly involved? Legal or DPO informed at | |
| Applicable regimes (for example GDPR 72 hours; EU Cyber Resilience Act 24 hours early warning and 72 hours notification; NIS2 24 and 72 hours; DORA; national laws) | |
| Deadline for each, in UTC | |
| Owner for each submission | |
| Customers who must be notified under contract, with deadlines | |
