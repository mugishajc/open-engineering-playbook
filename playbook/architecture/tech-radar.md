# Tech radar

Run an internal technology radar that says, for each tool, platform, technique and language you care about, whether teams should adopt it, trial it, assess it or hold off. The radar turns scattered opinions into one shared, dated list. It stops five teams choosing five message brokers, and it tells the platform team what to support on the [golden path](../platform/golden-paths.md).

## Outcomes

Starting points. Tune them to your organisation.

- The radar is reviewed and republished at least every 6 months (every quarter at Standard and above).
- Every entry has an owner, a ring, a quadrant and a one-paragraph reason. Every Adopt entry is supported on a golden path.
- New production use of a Hold entry drops to zero, except through a recorded exception.
- Every Hold entry still in production has a migration plan with a target date.

## Rings and quadrants

The format comes from the Thoughtworks Technology Radar. Keep the names so people recognise them.

| Ring | Thoughtworks meaning | Internal meaning in this playbook |
|---|---|---|
| Adopt | Strong default for the right use | Supported on the golden path. Use it without asking. |
| Trial | Worth pursuing on work that can handle the risk | Allowed for named teams, with an owner and an end date (default 6 months). |
| Assess | Worth exploring to understand the effect | Spikes and prototypes only. Not in production. |
| Hold | Proceed with caution | No new use. Existing use has a migration plan or a recorded exception. |

| Quadrant | Holds |
|---|---|
| Techniques | Practices and methods: trunk-based development, ADRs, contract testing |
| Platforms | Things you build on: Kubernetes, a database engine, a cloud service, a registry |
| Tools | Things you use to build and run: CI systems, scanners, OpenTelemetry Collector |
| Languages and frameworks | Programming languages and application frameworks |

## How entries move

| Move | Evidence required |
|---|---|
| New entry into Assess | A short proposal: problem it solves, what it replaces, who will assess it |
| Assess to Trial | A written spike result (one page) and a team willing to run it in production with an owner |
| Trial to Adopt | At least 2 teams in production for at least 3 months, golden path support, a runbook, an owner, and an [ADR](decision-records.md) |
| Any ring to Hold | An ADR that names the replacement and a migration plan with a date |
| Leave the radar | Nobody uses it and nobody is asking about it |

Do not skip rings, except to move something to Hold for a security or licence reason. A Trial that reaches its end date without a decision returns to Assess.

## Practice

### Foundation

- One Markdown page or one CSV file in the main repository. Start with 10 to 20 entries: the stack you run today plus the things people keep proposing.
- Review it twice a year in a 1-hour meeting. The tech lead decides disputed rings.
- Use the [radar CSV template](../../templates/architecture/tech-radar.csv).

### Standard

- Keep the radar as a CSV in its own repository. Changes arrive as pull requests, each with a reason.
- Publish it quarterly with the open source Build Your Own Radar tool, which reads the same five columns as the template: `name`, `ring`, `quadrant`, `isNew`, `description`.
- A small radar group (4 to 8 senior engineers from different teams, rotating yearly) curates the entries. The group prepares, the architecture forum approves (see [architecture practice](architecture-practice.md)).
- Every entry links to its owner and, for Adopt and Hold, to its ADR.
- The platform team's roadmap includes every Trial entry that is likely to reach Adopt within 2 quarters.
- Check new repositories against the radar in CI where it is cheap, for example by flagging Hold languages or base images.

### Assured

- The Adopt and Trial rings form the approved software list for procurement and security review. Anything else needs an exception.
- Each entry records licence, support model, end-of-life date where known, and whether it works on-premises and air-gapped.
- Exceptions for Hold entries go in a register with an owner, a risk rating and an expiry date of at most 12 months.
- Keep every published edition. Auditors and successors want to know what was approved when a system was built.

## Cloud, on-premises and air-gapped

- Record where each entry can run. A managed cloud database cannot be in Adopt for a team that must deploy air-gapped. Put the hosting limits in the description, or keep separate radars per hosting model if the lists diverge a lot.
- For air-gapped use, an entry should only reach Adopt when it can be installed from internal mirrors, licensed offline, updated through your transfer process and run without calling home. See [cloud, on-premises and air-gapped](../platform/cloud-on-prem-air-gapped.md).
- Build Your Own Radar is open source and can run on an internal host. A Markdown table generated from the CSV also works.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| The radar is a wish list of interesting tools | Every Adopt entry must be supported on the golden path. If the platform cannot support it, it is not Adopt. |
| Hold entries with no plan | A Hold entry without a migration plan or exception is incomplete. Owner fixes it before the next edition. |
| The radar becomes a gate that blocks all experiments | Assess is open to anyone for spikes. The radar governs production use. |
| Copying an external radar wholesale | External radars show what works elsewhere. Your rings depend on your skills, scale and hosting. |
| Published once, never updated | Calendar the review. An edition older than 12 months is a sign the practice has stopped. |

## Templates

- [Tech radar CSV](../../templates/architecture/tech-radar.csv)
- [ADR template](../../templates/docs/adr.md)

## Sources

- Thoughtworks Technology Radar: https://www.thoughtworks.com/radar
- Build Your Own Radar (open source tool and CSV format): https://github.com/thoughtworks/build-your-own-radar
