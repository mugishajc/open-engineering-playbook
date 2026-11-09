# Engineering governance

Govern with written standards, automated checks and a small review group that answers within a fixed time, not with a board every change must queue for. Review only the decisions that are hard to reverse or cross team boundaries. Every exception to a standard is written down, owned and expires.

## Outcomes

Starting points. Tune them to your organisation.

- Architecture reviews give a written answer within 5 working days of a complete request. At least 90% meet that limit.
- Fewer than 20% of decision records need a formal review. The rest follow existing standards.
- Every active waiver has an owner and an expiry date no more than 12 months away. No waiver is past its expiry.
- At least 80% of standards are checked automatically in CI or by policy as code, not by people.
- Every standard has been reviewed in the last 12 months or retired.

## What needs a review

Use a review when at least one is true:

1. The decision is hard or costly to reverse (data store, public API, hosting jurisdiction, core supplier).
2. It affects three or more teams.
3. It uses a technology in Hold or not on the [tech radar](../architecture/tech-radar.md).
4. It changes how a critical or regulated system handles personal data, money, safety or security controls.
5. It introduces an AI system in a high-risk use case (see [AI governance](../ai/ai-governance.md)).

Everything else follows the advice process: the deciding team asks the people affected and people with expertise for advice, records it in a [decision record](../architecture/decision-records.md), and decides.

## Architecture review that does not become a bottleneck

| Rule | Starting point |
|---|---|
| Review group size | 3 to 7 people: staff or principal engineers, a security representative, a platform representative |
| Request format | a decision record or [RFC](../architecture/rfcs.md), not a slide deck |
| Response time | written outcome within 5 working days; asynchronous by default |
| Meeting | 60 minutes weekly, only for items that need discussion |
| Outcomes | approve, approve with conditions, or return with specific questions. "No" must cite a standard or a risk. |
| Silence | if the group misses the deadline, the team may proceed and records that |
| Attendance | the requesting team presents; reviewers read before the meeting |

Measure the review group like any service: request count, time to outcome, share returned for rework. Publish the numbers each quarter.

## Communities of practice (guilds)

Communities of practice spread skills across teams: testing, front end, security champions, data, platform users.

- Each has a named facilitator with 10% of their time for it.
- They propose standards, but do not approve them. Approval follows [decision rights](decision-rights.md).
- They meet at a fixed rhythm (for example every 2 to 4 weeks) and publish notes.
- Close a community that has had no activity for 3 months.

## Standards lifecycle

Standards move through the same stages as the tech radar so engineers see one picture.

| Stage | Meaning | Radar ring | Enforcement |
|---|---|---|---|
| Proposed | written as an RFC, open for comment for 2 weeks | Assess | none |
| Trial | used by 1 to 3 teams to prove it | Trial | none, feedback collected |
| Adopted | the default for new work | Adopt | automated checks where possible; departures need a waiver |
| Deprecated | no new use; existing use has a migration date | Hold | new use blocked by checks |
| Retired | removed | removed | checks removed |

Each standard has: an owner, a reason (linked to the [technical strategy](../strategy/technical-strategy.md) where it applies), how it is checked, and a review date.

## Exceptions and waivers

A waiver allows a team to depart from a standard for a stated time.

- **Who can grant it:** the standard's owner, or the CISO for security standards. See row 10 in [decision rights](decision-rights.md).
- **Required fields:** standard, system, reason, risk, compensating control, owner, granted by, granted on, expiry.
- **Expiry:** 6 months by default, 12 months at most. Renewal needs a new decision, not a date change.
- **Register:** one register for all waivers, visible to all engineers.
- **Review:** list waivers that expire in the next 30 days every month. Report expired waivers to the head of engineering.
- **Signal:** more than five active waivers for the same standard means the standard needs changing.

## Practice

### Foundation

Solo and Startup. Write a short list of standards (languages, databases, hosting, security basics) in the repository. Use decision records for hard-to-reverse choices. Use automated checks in CI. No review board is needed.

### Standard

Scale-up and Enterprise. A review group with the rules above, the standards lifecycle, a waiver register, and communities of practice for the main disciplines. Standards checked by policy as code wherever possible. Quarterly report on review times, waivers and standard coverage.

### Assured

Regulated and Public sector. Everything in Standard, plus:

- Keep review outcomes, waivers and standard versions as records.
- Link each standard to the controls it supports in [control mapping](../compliance/control-mapping.md).
- Require independent review (second line or internal audit) of waivers for security and resilience standards.
- Use automated change approval with evidence instead of a weekly change board. See [regulated industries](../compliance/regulated-industries.md).

## Cloud, on-premises and air-gapped

Standards must say which environments they apply to. A standard that requires a SaaS scanner cannot apply in an air-gapped network without an offline alternative. Each standard lists its on-premises and air-gapped equivalent, or states that it does not apply there. Waivers for air-gapped networks often last longer because updates move slowly. Keep the 12-month maximum and renew deliberately.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Review board every change must queue for | Review only by the criteria above. Everything else uses the advice process. |
| Standards that nobody checks | Automate the check or retire the standard. |
| Waivers that never expire | Required expiry and monthly expiry report. |
| Governance by slide deck | Decision records and RFCs in version control. |
| Guilds that set rules | Guilds propose; decision rights decide. |

## Related

- [IT governance](it-governance.md): how this page fits board-level governance (ISO/IEC 38500, COBIT 2019, ITIL 4).
- [Architecture practice](../architecture/architecture-practice.md): quality attributes, fitness functions and review triggers.

## Templates

- [Decision record](../../templates/docs/adr.md)
- [RFC](../../templates/docs/rfc.md)
- [Tech radar](../../templates/architecture/tech-radar.csv)
- [Risk register](../../templates/strategy/risk-register.csv)

## Sources

- Thoughtworks Technology Radar: https://www.thoughtworks.com/radar
- Michael Nygard, "Documenting Architecture Decisions", 2011: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
- UK GDS Way: https://gds-way.digital.cabinet-office.gov.uk/
