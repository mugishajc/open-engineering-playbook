# Legacy modernisation

"Our core system is 20 years old, nobody wants to touch it, and every change takes months." Do not answer this with a big-bang rewrite. Replace the old system piece by piece behind a stable interface, using the strangler fig pattern, and ship value at every step so the programme can stop at any point and still have paid for itself. Rewrites that try to replace everything at once tend to run late, chase a moving target and arrive missing features nobody wrote down.

## Outcomes

Starting points. Tune them to your organisation.

- The first slice of functionality runs in production on the new path within 3 to 6 months of starting.
- Every quarter, a measurable share of traffic, transactions or users moves to the new path, and the old path's share falls.
- Change lead time for the modernised parts is at least 50% shorter than for the legacy parts, measured with the [DORA metrics](../measurement/metrics.md).
- Zero data loss and no unplanned downtime beyond the SLO during cutovers.
- Each retired legacy component is switched off and its infrastructure removed within 3 months of its last user moving.

## Decide what to do with each part

Not everything old needs replacing. Sort each component into one of these, and record the choice in an [ADR](decision-records.md).

| Option | When it fits |
|---|---|
| Retain | It works, rarely changes, and is supported. Leave it alone and wrap it with an API if others need it. |
| Retire | Few people use it. Confirm with usage data, then switch it off. Often the cheapest win. |
| Rehost | The hardware or data centre is the problem, not the code. Move it as is. |
| Replatform | Small changes (new database version, containers, managed runtime) remove most of the pain. |
| Refactor in place | The code is the problem but the design is sound. Improve it behind tests. |
| Replace with a product | The function is not what makes you different, for example payroll or general ledger. See [build, buy or adopt](../strategy/build-buy-adopt.md). |
| Rebuild incrementally | The function matters, changes often and the old design blocks change. Use the strangler fig. |

## The strangler fig, step by step

Martin Fowler named the pattern in 2004 after a vine that grows around a tree until it replaces it.

1. **Put a facade in front.** Route all calls to the legacy system through an API gateway, proxy or routing layer you control. Nothing changes for users yet.
2. **Capture current behaviour.** Write characterisation tests that record what the system does today, including its odd edge cases. Michael Feathers' "Working Effectively with Legacy Code" (2004) describes the technique.
3. **Pick a thin first slice.** Choose a capability that is valuable, fairly self-contained and low risk: a read-only enquiry, a new product line, one region.
4. **Build the slice on the new path.** Follow the [golden path](../platform/golden-paths.md). Give it its own data store if it can own the data.
5. **Run in parallel or shadow.** Copy read requests to the new path and compare responses with the old one before any user depends on it. For writes, either compare the computed result without committing it, or let the new path write only to its own isolated store with every external side effect (payments, messages, emails, partner calls) stubbed. A shadow request must never reach a real customer or partner.
6. **Shift traffic gradually.** Use the facade or feature flags to move 1%, then 10%, then 50%, then 100% of traffic, with a rollback at each step.
7. **Retire the old part.** Remove the code path, the data and the infrastructure. Update the catalogue.
8. **Repeat** with the next slice. Re-plan every quarter.

For changes inside one codebase, branch by abstraction does the same job: introduce an interface, move callers to it, build the new implementation behind it, switch over, delete the old one.

## Data is the hard part

- Decide which system is the source of truth for each data set at each stage. Write it down.
- Use change data capture or events to keep old and new stores in sync during transition. Avoid two-way sync where you can: it creates conflicts that are hard to resolve.
- Reconcile automatically. Run daily comparisons of record counts and totals between old and new stores, and alert on differences.
- Plan data migration as its own workstream with rehearsals on production-sized copies. See [database changes](../delivery/database-changes.md).

## Practice

### Foundation

- Write a one-page inventory: each legacy component, who uses it, how often it changes, what breaks, and the option chosen from the table above.
- Start with retire and the first strangler slice. Avoid parallel big programmes.
- Characterisation tests before changing anything.

### Standard

- An [RFC](rfcs.md) for the modernisation approach, with the slice order, the facade design and the data strategy.
- A modernisation dashboard: share of traffic on the new path, legacy change lead time versus new, incidents per path, cost per path.
- A fixed team owns both the legacy and the new path for each domain, so knowledge moves with the work.
- Funding is tied to slices delivered, not to a big end date. See [business case](../strategy/business-case.md).

### Assured

- Each cutover has a change record, a tested rollback plan and sign-off by the business owner (see [change management](../reliability/change-management.md)).
- Reconciliation reports are kept as evidence that no records were lost or altered.
- Regulators are told in advance where the change affects a critical or important function, as sector rules require (for example EU DORA for financial entities, which is unrelated to the DORA metrics research).
- Records retention obligations for legacy data are met before any data is deleted. Public bodies check their statutory records duties.

## Cloud, on-premises and air-gapped

- Many legacy systems run on-premises on platforms with no cloud equivalent (mainframes, older Unix systems). The facade and new slices can still run on-premises next to them. Moving to the cloud is a separate decision.
- In air-gapped environments, shadow traffic and data comparison must happen inside the enclave. Plan capacity for running both paths at once.
- Keep the hosting decision for each new slice in an ADR (see [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md)).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Big-bang rewrite with a single go-live date | Strangler fig with small slices, each in production. |
| New system copies every legacy feature, including the unused ones | Usage data first. Retire what nobody uses. |
| Legacy team and new team separate, and the legacy team leaves | One team per domain owns both paths. |
| Two-way data sync between old and new | One source of truth per data set per stage, one-way sync, daily reconciliation. |
| Old path never switched off | Retirement is part of each slice's definition of done. |
| Modernisation done "on the side" with no funding | Funded slices with outcomes in the business case. |

## Templates

- [ADR template](../../templates/docs/adr.md)
- [RFC template](../../templates/docs/rfc.md)
- [Tech debt register](../../templates/docs/tech-debt-register.csv)
- [Risk register](../../templates/strategy/risk-register.csv)

## Sources

- Martin Fowler, "Strangler Fig Application" (2004): https://martinfowler.com/bliki/StranglerFigApplication.html
- Martin Fowler, "Branch By Abstraction": https://martinfowler.com/bliki/BranchByAbstraction.html
- Michael Feathers, Working Effectively with Legacy Code, Prentice Hall (2004)
