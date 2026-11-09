# Resilience testing

Inject real faults on a schedule, starting in staging, to check that the system survives the failures you designed for. A tabletop tests decisions; a game day tests the system. Claims such as "rollback under 15 minutes", "a zone failure is invisible to users" and "readiness reflects real health" stay untested until you break something on purpose and watch.

## Outcomes

Starting points. Tune them to your services.

- Every Tier 1 service has a written fault hypothesis for each failure in its design (instance lost, zone lost, dependency slow, dependency down) and has tested at least one in the last quarter.
- Every game day has a written hypothesis, a blast radius limit, abort criteria and a named stop person before it starts.
- 100% of game day findings get an owner and a date, tracked like postmortem actions (see [postmortems](postmortems.md)).
- Tier 1 services complete a zone or site failover in production at least once a year.
- No game day causes unplanned user impact beyond its stated blast radius. If one does, it stops and gets a postmortem.

## Practice

### Foundation

1. **Kill one instance in staging every month** while traffic runs, and check that users would see no errors. This tests readiness, retries and the disruption budget.
2. **Run the rollback drill as a fault test.** Deploy a deliberately broken build to staging and time the rollback (see [rollbacks](rollbacks.md)).
3. **Write down what you expected before you start.** "If one pod dies, error rate stays under 0.1% and p99 latency under 800 ms." A test without a hypothesis is a demonstration.

### Standard

1. **Quarterly game day in production, in working hours.** Pick one hypothesis per game day. Examples: a dependency adds 2 seconds of latency; one zone loses all its nodes; the cache is flushed; the database fails over.
2. **Safety rules, written in the plan:**
   - Start in staging. Move to production only after the staging run passes.
   - Limit the blast radius: one service, one zone, a share of traffic, or a set duration.
   - Set abort criteria tied to the SLO (for example, stop if the burn rate passes 6 for 5 minutes) and name the stop person, who is not running the experiment.
   - Announce the game day to on-call, support and dependent teams. Never run one during a freeze, an open incident or a peak period.
   - Stop at the first unexpected user impact. Restore first, analyse after.
3. **Tools.** LitmusChaos and Chaos Mesh (CNCF projects) on Kubernetes, or the cloud provider's fault injection service. On VMs and on-premises, scripted actions such as stopping a service, adding latency with `tc netem` or blocking a port with a firewall rule are enough.
4. **Test the degraded modes and overload behaviour** set out in [scaling](../architecture/scaling.md#overload-protection): shed load, turn on a degraded mode, cut retries, and check that traffic comes back in steps.
5. **Test the monitoring.** Stop a scrape target or the Collector and check that the absent-data alert fires (see [observability](../architecture/observability.md)).

### Assured

1. **Annual zone or site failover in production** for Tier 1 services, timed against the failover RTO (see [backup and recovery](backup-and-recovery.md)).
2. **Records.** Keep the plan, hypothesis, results and actions. They are evidence for ISO/IEC 27001:2022 control 5.30 (ICT readiness for business continuity) and, for EU financial entities, the digital operational resilience testing required by DORA (Regulation (EU) 2022/2554).
3. **Change control.** Production game days are normal changes with a rollback plan (see [change management](change-management.md)).

## Cloud, on-premises and air-gapped

- Cloud: provider fault injection services can stop instances, add latency or simulate a zone outage within limits you set. Check which actions they cannot simulate, such as a failure of the provider's own control plane.
- On-premises: pull a network cable, power off a host or fail a storage path in a maintenance window. Physical tests find what software tests miss: wrong cabling, a single power feed, a switch with no spare.
- Air-gapped: install fault injection tools from internal mirrors. Test that failover works with no outside dependency, including time, DNS and certificate services.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Chaos in production before staging passes | Staging first, then production with a blast radius limit. |
| Game day with no hypothesis or abort criteria | Write both, and name the stop person, before starting. |
| Only tabletops, never a real fault | Tabletops test decisions. Add one real fault test per quarter. |
| Findings recorded and never fixed | Track them like postmortem actions, with owners and dates. |
| Failover tested only in the direction that works | Fail over and fail back, and time both. |

## Templates

- [Runbook](../../templates/docs/runbook.md): record "Last exercised" for each procedure.
- [Postmortem](../../templates/docs/postmortem.md): for any game day that caused unplanned impact.
- [Tabletop facilitator guide](../../exercises/tabletop/facilitator-guide.md)

## Sources

- Principles of Chaos Engineering: https://principlesofchaos.org/
- LitmusChaos (CNCF): https://litmuschaos.io/
- Chaos Mesh (CNCF): https://chaos-mesh.org/
- AWS Fault Injection Service: https://docs.aws.amazon.com/fis/
- Azure Chaos Studio: https://learn.microsoft.com/en-us/azure/chaos-studio/
- Google SRE book, "Testing for Reliability": https://sre.google/sre-book/testing-reliability/
