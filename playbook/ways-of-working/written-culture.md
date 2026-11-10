# Written culture

Write first, meet second. Default to a document, not a meeting. A written proposal forces the author to think clearly before asking for other people's time, lets reviewers respond when they do their best thinking, and leaves a record that new team members can read months later. Companies that run on writing - Amazon (six-pagers), Stripe (written proposals before meetings), GitLab (handbook-first) - consistently report faster decisions across more time zones with fewer misunderstandings.

## Outcomes

Starting targets. Tune them after one quarter of data.

| Signal | Starting target |
|---|---|
| Decisions that have a written record (decision record, design doc or RFC) | At least 80% of decisions that affect more than one team |
| Time from proposal to decision | Median under 5 working days for standard decisions |
| Meeting hours per IC per week | Under 10 hours |
| Meeting hours per engineering manager per week | Under 15 hours |
| Design docs reviewed async before any synchronous discussion | 100% |
| New engineers who can find the reasoning behind any recent decision within 30 minutes | At least 90% |

## Practice

### Foundation

#### Writing as the default medium

Every proposal, design change or decision starts as a written document. The document is the thinking, not a summary of thinking done elsewhere. Before booking a meeting, write the problem, the options you considered, your recommendation and the risks. Share it and give reviewers at least 24 hours to read and comment.

Meetings are for three things: resolving disagreements that two rounds of written comments did not settle, building relationships, and urgent coordination during incidents. Everything else is better in writing.

#### Where documents live

Pick one place and put everything there. A wiki, a docs folder in the repository, or a shared drive. The choice matters less than the rule: one place, searchable, version-controlled or with edit history. If someone asks "where is the decision about X?" the answer is always the same location.

- **In-repo docs** (a `docs/` folder or an `rfcs/` folder): best for decisions tied to code, because they travel with the code and get reviewed in pull requests. See [decision records](../architecture/decision-records.md) and [RFCs](../architecture/rfcs.md).
- **A wiki or shared docs tool** (Notion, Confluence, Google Docs, a GitLab wiki): best for cross-team proposals and onboarding material.
- **Never Slack, Teams or email.** Chat is for coordination, not decisions. A decision made in a chat thread is invisible to anyone who was not in the thread and to everyone who joins later.

#### Async review with SLAs

Set clear expectations for response times:

| Action | SLA |
|---|---|
| Acknowledge a document shared for review | Same working day |
| Leave substantive comments | Within 1 working day |
| Approve, reject or request changes to a proposal | Within 2 working days |
| Author responds to all comments | Within 1 working day |

If a reviewer cannot meet the SLA, they say so and delegate to someone else. Silence is not consent and silence is not rejection. The author follows up after the SLA expires.

#### Meeting budgets

Track meeting hours per team. Set a budget and review it monthly.

| Role | Weekly meeting budget |
|---|---|
| Individual contributor | 10 hours maximum, target under 8 |
| Engineering manager | 15 hours maximum |
| Director or VP | No fixed cap, but protect at least 2 hours of uninterrupted time per day |

Every recurring meeting has an owner, a written agenda shared 24 hours ahead, and written notes published within 1 working day. Cancel any meeting where the agenda is empty. Review every recurring meeting quarterly and drop any that no one defends with a concrete outcome it produces.

### Standard

#### Design docs before discussion

For any change that takes more than a few days of work, affects more than one service, or changes a public API or data schema, write a design doc before starting work. The design doc is not a formality. It is where the hard thinking happens.

A design doc contains:

1. **Context.** What problem are we solving and why now?
2. **Goals and non-goals.** What is in scope and what is not.
3. **Options considered.** At least two, with trade-offs.
4. **Recommendation.** Which option and why.
5. **Risks and mitigations.** What could go wrong.
6. **Open questions.** What you need reviewers to help with.

Share the doc and give reviewers 2 working days. Hold a meeting only if written comments surface a genuine disagreement. The meeting resolves the disagreement; the author updates the doc with the outcome. The doc is the record, not the meeting.

#### Running a writing culture

- **Templates.** Provide a design doc template, a decision record template and a meeting notes template. People write more when the blank page is not blank. See [documentation](../people/documentation.md).
- **Review norms.** Comment on the content, not the prose style. Label comments as in code review: blocking, suggestion, question. See [code review](../delivery/code-review.md).
- **Writing as a skill.** Include clear writing in the engineering career framework. Promote engineers who write well, not only engineers who code well. See [career framework](../people/career-framework.md).
- **Executives write too.** Strategy documents, quarterly plans and post-incident reviews are written by the responsible leader, not delegated to a coordinator. The act of writing is the act of deciding.

#### Standups and status updates

Replace verbal standups with written async updates. Each person posts a short update - what they did, what they plan to do, what is blocked - in a shared channel or tool at the start of their working day. This takes 5 minutes instead of 15, works across time zones, and creates a searchable record.

Keep a synchronous standup only if the team is co-located, the standup is under 10 minutes, and the team agrees it adds value beyond the written update. Never hold a standup just because Scrum says so.

### Assured

#### Writing as a control

In regulated environments, written records become audit evidence.

- Every design decision that affects security, privacy, data handling or financial controls has a design doc with an explicit approval by the responsible person. The approval is in the document's history, not in a separate email.
- Meeting notes for governance forums (architecture review, change advisory, risk committee) are published within 1 working day, list attendees, decisions and action items, and are retained for the records retention period.
- Decision records use the format in [decision records](../architecture/decision-records.md) and are stored in version control so the full history is available to auditors.
- The written record is the source of truth. If a verbal discussion changes a decision, the document is updated before the change takes effect.

This gives evidence for ISO/IEC 27001:2022 Annex A 5.37 (documented operating procedures), SOC 2 CC2.2 (communication for internal control) and NIST SSDF PO.1.1 (define and document security requirements). See [control mapping](../compliance/control-mapping.md).

## Cloud, on-premises and air-gapped

Written culture works everywhere. The only variable is the document platform.

| Environment | Recommended tools |
|---|---|
| Cloud | Any shared docs tool (Google Docs, Notion, Confluence) plus in-repo docs for code-adjacent decisions |
| On-premises | Self-hosted wiki (Confluence Data Center, GitLab wiki, BookStack, Wiki.js) plus in-repo docs |
| Air-gapped | In-repo docs (the repository is the collaboration platform), a self-hosted wiki with no external dependencies, or a shared network drive with agreed folder structure |

In air-gapped environments, async review SLAs may need to be longer if access to the document store requires being on the network. Adjust the SLAs, but keep the principle: write before you meet.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Can we just hop on a call?" as the first response to any question | Require a written problem statement before booking a meeting. If you can answer in writing, do. |
| Decisions made in Slack threads that disappear after 90 days | Move every decision to a decision record or design doc within 1 working day. |
| Verbal-only standups that nobody remembers by Thursday | Switch to written async updates. Keep a synchronous standup only if the team votes to keep it. |
| Design docs written after the code is done | Require the design doc before the first pull request for any multi-day change. |
| Documents nobody reads because they are too long | Set a length guide: 1 page for a decision record, 2 to 5 pages for a design doc, 6 pages maximum for a strategy proposal. |
| One person takes notes for every meeting and burns out | Rotate the note-taker. Better yet, cancel the meeting and write the proposal instead. |
| Writing culture used to avoid difficult conversations | Some conversations need a room, a whiteboard and eye contact. Use writing for proposals and decisions; use meetings for conflict resolution and relationship building. |

## Templates

- [Decision record template](../../templates/docs/decision-record.md)
- [RFC template](../../templates/docs/rfc.md)
- [Design doc template](../../templates/docs/design-doc.md)
- [Meeting notes template](../../templates/docs/meeting-notes.md)

## Sources

- Amazon, Working Backwards: https://www.aboutamazon.com/about-us/leadership-principles
- GitLab, handbook-first documentation: https://handbook.gitlab.com/handbook/handbook-usage/
- Stripe, writing culture: https://slab.com/blog/stripe-writing-culture/
- Cal Newport, A World Without Email, 2021
- Basecamp, Shape Up: https://basecamp.com/shapeup
- Google engineering practices, design docs: https://google.github.io/eng-practices/
