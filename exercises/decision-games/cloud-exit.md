# Decision game: cloud exit

The cloud bill has almost tripled in two years while revenue grew by less than half, and the CFO has a spreadsheet that says moving to your own hardware would cut it by 60%. The board wants a decision this quarter. Choose a path, then see what each one costs, including the parts the spreadsheet left out.

| | |
|---|---|
| Who | CTOs, CFOs, heads of infrastructure and platform, and finance partners. Best played with engineering and finance at the same table. |
| Time | 30 minutes alone; 45 minutes as a group |
| Practice it teaches | [FinOps](../../playbook/platform/finops.md), [cloud, on-premises and air-gapped](../../playbook/platform/cloud-on-prem-air-gapped.md), [transition playbook](../../playbook/strategy/transition-playbook.md), [business case](../../playbook/strategy/business-case.md) |

## The situation

An online learning platform serves video courses to 2 million learners. It has 120 engineers and has run entirely on one public cloud provider since it started. All organisations, people and numbers here are fictional; amounts are in currency units (CU).

- Cloud spend: 1.1 million CU two years ago, 2.9 million CU this year. Revenue grew 40% over the same period.
- About half the bill is video storage and transcoding, which runs at a steady level all year. The rest is the web platform, databases, and traffic that peaks at exam season to four times the normal load.
- Nobody owns the bill. Teams have no cost dashboards. Commitment discounts were last reviewed 18 months ago.
- The CFO's spreadsheet compares this year's cloud bill with the price of servers in a colocation facility and shows a 60% saving. It does not include staff, data transfer during the move, or the time to migrate.
- The platform team of 9 has never run hardware.

## Round 1: what do you do?

**A. Full exit.** Move everything to two colocation sites within 12 months.

**B. FinOps first.** Give one quarter to cost visibility, ownership and quick savings. Then decide with real numbers.

**C. Partial repatriation.** Move the steady video storage and transcoding to owned hardware; keep the web platform and peak-sensitive services in the cloud.

**D. Negotiate.** Sign a larger 3-year committed spend with the provider for a bigger discount, and change nothing else.

Pick one before you open the consequences.

<details>
<summary>Consequences of A: full exit</summary>

The first 6 months go to hiring hardware and network engineers, choosing sites and procurement. Hardware lead times push the first rack to month 5. Migration of the databases needs a parallel-run period, so for 9 months you pay for both. Exam season arrives at month 10 with on-premises capacity sized for normal load plus 30%; the platform falls over for two days, and the team sends traffic back to the cloud in a hurry.

At month 18 the move is done. The real saving, once staff, data transfer, double running and spare capacity are counted, is about a quarter of the old bill, not 60%, and it took 50% longer than planned. The team also spent 18 months on infrastructure instead of the product. The [transition playbook](../../playbook/strategy/transition-playbook.md) exists because big moves without a pilot and stop points look like this.

</details>

<details>
<summary>Consequences of B: FinOps first</summary>

Week 1: tag every resource by team and service, publish a cost dashboard per team, and name an owner for the bill. Weeks 2 to 8: the teams find test environments running all weekend, video renditions nobody watches stored in the most expensive storage class, oversized database instances and an expired commitment. Savings reach about 30% of the run rate by the end of the quarter, with no migration.

The quarter also produces what the CFO's spreadsheet lacked: unit cost (CU per learner per month, CU per hour of video stored and transcoded) and a clear split between steady and peaky workloads. Go to round 2 with those numbers.

</details>

<details>
<summary>Consequences of C: partial repatriation, now</summary>

The right shape of answer, chosen too early. Without cost visibility, the team moves the transcoding pipeline first and discovers that a third of the storage it planned to buy holds renditions that could simply be deleted. The hardware is oversized. Data transfer out of the cloud for the initial copy is a large one-off bill nobody budgeted. It still saves money in year two, but less than it would have after a quarter of FinOps.

</details>

<details>
<summary>Consequences of D: negotiate a bigger commitment</summary>

The discount is real, and the bill drops at once. But the waste is now locked in for 3 years: you have committed to paying for usage that cleanup would have removed. When a later FinOps effort cuts usage by 30%, the commitment means most of the saving never reaches the bill. Your negotiating position at renewal is also weaker, because you have shown no credible alternative.

Commitments belong after cleanup, sized to the steady baseline you have measured, as the [FinOps](../../playbook/platform/finops.md) page describes.

</details>

## Round 2: with real numbers

After the FinOps quarter, the bill run rate is about 2.0 million CU a year. Video storage and transcoding are 1.1 million CU of that, steady all year. A full total cost of ownership for owned hardware for that workload, over 5 years, including staff, two sites, support contracts, hardware refresh, migration and exit, comes to about 0.7 million CU a year.

**E. Move video storage and transcoding** to owned hardware over 9 months, with a pilot on one course catalogue first, and keep the rest in the cloud.

**F. Stay fully in the cloud,** now that the bill is under control, and buy commitments for the steady baseline.

<details>
<summary>Consequences of E and F</summary>

**E** saves about 0.4 million CU a year on paper, if the TCO holds. It adds a hardware operation the team has never run; the pilot exists to test that before the full move, with a stop decision if it does not hold. It also improves your negotiating position with the cloud provider. Use open formats (S3-compatible object storage, OCI containers) so the move is reversible.

**F** is also defensible. It avoids building a new skill set and keeps all engineers on the product. If the commitment discount for the steady baseline brings the cloud cost close to the owned-hardware TCO, the saving from E may not be worth the operational risk.

Both are good answers if they come with an exit plan and a review date. The difference is now a business choice with real numbers, which is where the decision should be.

</details>

## What the playbook recommends, and why

**B, then E or F on the numbers.** Visibility and ownership come first: you cannot decide where a workload should live if you do not know what it costs or why. The [FinOps](../../playbook/platform/finops.md) page covers the inform, optimise and operate phases. The [business case](../../playbook/strategy/business-case.md) and [build, buy or adopt](../../playbook/strategy/build-buy-adopt.md#total-cost-of-ownership) pages show how to count full TCO, including staff, migration and exit.

Where a move does make sense, it is usually for steady, predictable, storage- or compute-heavy workloads, not for peaky ones. Run it through the [transition playbook](../../playbook/strategy/transition-playbook.md): pilot, measurable exit criteria, a stop decision at each gate. Record the hosting decision per workload in an [ADR](../../templates/docs/adr.md), with the conditions that would make you move it again, as [cloud, on-premises and air-gapped](../../playbook/platform/cloud-on-prem-air-gapped.md) recommends.

## Debrief questions

1. Who owns your cloud bill today? Could each team tell you what it spent last month?
2. What is your unit cost (per customer, per transaction, per learner), and is it going up or down?
3. Which of your workloads are steady all year, and which have peaks? Where does each one live today?
4. If you had to leave your main provider, what would it cost, and how long would it take?
