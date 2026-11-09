# Green software

"Our board has a carbon target and nobody knows what software contributes to it." Measure the carbon intensity of your main services with the Software Carbon Intensity (SCI) specification, then reduce it with the same changes that cut cost and latency: use less hardware, use it more fully, and run flexible work when and where electricity is cleaner. Treat carbon as a property of the system you can measure per unit of work, not as a marketing claim.

## Outcomes

Starting points. Tune them to your organisation.

- An SCI score, per a stated functional unit, is published internally for the top 3 services by compute use, and recalculated every quarter.
- SCI per functional unit falls quarter on quarter for those services, or the reason it rose is recorded.
- Average CPU utilisation of always-on compute is tracked, with a target set from your own baseline.
- 100% of non-production environments shut down outside working hours unless an exception is recorded.
- Hardware refresh decisions on-premises include embodied carbon, not only performance per watt.

## The Software Carbon Intensity specification

The Green Software Foundation's SCI specification is published as ISO/IEC 21031:2024. It gives a rate, not a total:

SCI = ((E x I) + M) per R

| Term | Meaning |
|---|---|
| E | Energy used by the software, in kWh |
| I | Carbon intensity of the electricity used, in grams of CO2 equivalent per kWh, location-based |
| M | Embodied emissions of the hardware, the share attributed to this software |
| R | The functional unit: per API call, per user, per transaction, per job |

Because SCI is a rate per functional unit, it rewards efficiency. Buying offsets or renewable energy certificates does not lower the SCI score. Only using less energy, cleaner energy or less hardware does.

## Ways to reduce it

| Lever | Examples |
|---|---|
| Energy efficiency | Fix slow queries and hot code paths, cache, reduce data transfer, choose efficient runtimes for heavy workloads |
| Hardware efficiency | Rightsize, raise utilisation, consolidate under-used servers, extend hardware life where performance allows |
| Carbon awareness | Run batch jobs, training and backups at times or in regions with lower grid carbon intensity, where data residency rules allow |
| Less work | Delete unused features, data and environments. Set retention periods. Avoid running large models where a smaller one or a simple rule does the job. |

Most of these also cut cost, so tie this work to [FinOps](finops.md) and [scaling](../architecture/scaling.md).

## Practice

### Foundation

- Use your cloud provider's carbon reporting, or your data centre's energy figures, to see the baseline.
- Shut down idle and non-production resources. Rightsize. These are free wins.

### Standard

- Calculate SCI for the top services by compute, with the functional unit stated. Store the method and inputs in the repository so others can repeat it.
- Measure energy where you can: for Kubernetes, a tool such as Kepler (a CNCF project) estimates energy per workload.
- Include carbon and energy in [RFCs](../architecture/rfcs.md) for compute-heavy designs, including AI features (see [building with AI](../ai/building-with-ai.md)).
- Make batch and scheduled workloads carbon-aware where the business can accept the delay.

### Assured

- Methods, data sources and assumptions behind any published figure are documented and reviewable. Figures used in sustainability or regulatory reports go through the same review as financial figures.
- Public sector: follow national sustainable technology guidance and procurement rules.
- Hardware procurement and disposal records support embodied carbon estimates and responsible disposal.

## Cloud, on-premises and air-gapped

- Public cloud: provider tools give estimates. Check their method, scope and delay before using them in reports.
- On-premises: you control the data. Meter power at rack or server level where possible and get grid intensity from your electricity supplier or national grid data.
- Air-gapped: grid intensity data must be transferred in on a schedule. Carbon-aware shifting of work is usually limited to time, not region.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Reporting only offsets or certificates | Report SCI, which only falls when software uses less energy or hardware. |
| A one-off carbon estimate in a slide | Repeatable calculation in the repository, recalculated quarterly. |
| Comparing SCI scores across unrelated services | Compare a service with its own history, per the same functional unit. |
| Moving work to another region without checking residency rules | Data residency first, carbon second. |

## Templates

- [RFC template](../../templates/docs/rfc.md)
- [ADR template](../../templates/docs/adr.md)

## Sources

- Green Software Foundation, Software Carbon Intensity specification: https://sci.greensoftware.foundation/
- ISO/IEC 21031:2024, Information technology, Software Carbon Intensity (SCI) specification (ISO catalogue: https://www.iso.org)
- Green Software Foundation: https://greensoftware.foundation/
- Kepler, Kubernetes-based Efficient Power Level Exporter: https://sustainable-computing.io/
