# Decision making

Match the weight of the process to how hard the decision is to undo and how much it can break. Decide reversible, contained decisions fast and inside the team. Slow down only for decisions that are expensive to reverse or affect many teams, customers or regulators: run a pre-mortem, write a decision record, set a deadline, then commit. Most slow organisations treat every decision as irreversible; most reckless ones treat every decision as reversible.

## When to use this

- A decision has been "under discussion" for more than two weeks.
- People reopen decisions that were already made.
- A small change needs the same approvals as a platform migration.
- A bad outcome led to blame for a decision that was sound when it was made.
- You are about to make a choice that will be hard to reverse: a cloud provider, a core database, a vendor contract, a reorganisation, a security exception.

## Step 1: classify the decision

Jeff Bezos's 2015 letter to Amazon shareholders splits decisions into Type 1, one-way doors that are hard or impossible to reverse, and Type 2, two-way doors that you can walk back through. Most decisions are Type 2. Add a second axis, blast radius, and you get the process weight.

| | Small blast radius (one team, internal) | Large blast radius (many teams, customers, regulators, money) |
|---|---|---|
| **Two-way door** (reversible within a day or a sprint, no data loss) | **Light.** The team decides today. One line in the team log. | **Medium.** Owner decides within 1 week after consulting affected teams. Short decision record. Reversal plan stated. |
| **One-way door** (reversal takes months, loses data, breaks contracts or trust) | **Medium.** Owner decides within 2 weeks. Decision record with options. Peer review by a principal engineer. | **Heavy.** Pre-mortem, decision record with at least 3 options, review at the architecture or leadership forum, decision within 4 to 6 weeks. |

Time limits are starting points. Tune them, but always set one.

Signs a decision is a one-way door: it changes a data format others depend on, signs a contract longer than 1 year, deletes data, changes a public API, moves people between teams, or creates a regulatory commitment. Many one-way doors can be turned into two-way doors: a pilot, a feature flag, a contract break clause, an abstraction layer. Look for that first.

## Step 2: know which domain you are in

Cynefin, described by David Snowden and Mary Boone in Harvard Business Review in 2007, says the right way to decide depends on the kind of situation. Engineering leaders face all of them, sometimes in the same week.

| Domain | What it looks like | How to decide | Engineering example |
|---|---|---|---|
| Clear (called Simple in the 2007 article) | Cause and effect are obvious; a known answer exists | Sense, categorise, respond. Apply the standard. | Rotate a leaked secret; apply a patched base image |
| Complicated | Cause and effect can be found with analysis or experts | Sense, analyse, respond. Ask experts, compare options. | Choose a database for a known workload; capacity planning |
| Complex | Cause and effect are clear only in hindsight | Probe, sense, respond. Run small safe-to-fail experiments. | Adopting code assistants; a new team structure; a new product market |
| Chaotic | No clear cause and effect; harm is happening now | Act, sense, respond. Stabilise first, analyse later. | A major outage or a ransomware attack in its first hour |
| Disorder | You do not know which domain you are in | Break the problem into parts and place each part | A failing programme with technical, people and supplier problems mixed together |

The common failure is treating a complex problem as complicated: commissioning a long analysis when only an experiment will tell you the answer. The opposite failure is running experiments on a clear problem that already has a standard answer.

## Step 3: run a pre-mortem for heavy decisions

Gary Klein described the pre-mortem in Harvard Business Review in 2007. It takes 45 to 60 minutes.

1. State the decision and the plan (5 minutes).
2. Tell the group: "It is 12 months from now. This decision has failed badly. Write down every reason why." Each person writes alone, in silence (10 minutes).
3. Go round the room, one reason per person per round, until the lists are empty (15 minutes). The most senior person goes last.
4. Group the reasons and pick the 3 to 5 most likely or most damaging (10 minutes).
5. For each, agree a change to the plan, an early warning sign to watch, or an accepted risk with an owner (15 minutes).

The pre-mortem works because it makes doubt a task instead of disloyalty. Record the results in the decision record.

## Step 4: write it down

Write a decision record for every one-way door and every medium or heavy decision. Use the format in [decision records](../playbook/architecture/decision-records.md) for technical decisions and the same structure for organisational ones: context, options, decision, consequences, and a review date. Who is allowed to decide what is set out in [decision rights](../playbook/operating-model/decision-rights.md); check it before you start, not after.

## Step 5: time-box and commit

- **Set the deadline when the decision is raised.** Light: same day. Medium: 1 to 2 weeks. Heavy: 4 to 6 weeks. If information is still missing at the deadline, the owner decides with what is known and records the uncertainty.
- **Do not wait for certainty on two-way doors.** Bezos's 2016 shareholder letter suggests deciding with about 70% of the information you wish you had. Waiting costs more than a reversible mistake.
- **Disagree and commit.** Andy Grove's High Output Management describes a process of free discussion, a clear decision, then full support from everyone, including those who argued against it. Bezos's 2016 shareholder letter uses the phrase "disagree and commit". Dissent goes on the record in the decision record; after that, people support the decision in their work.
- **Reopen only with new evidence.** A decision is reopened when its review date arrives or when a fact listed in the record changes, not because someone lost the argument.

## Decision quality is not outcome quality

A good decision can have a bad outcome, and a bad decision can get lucky. Daniel Kahneman's Thinking, Fast and Slow describes outcome bias and hindsight bias: people judge decisions by results they could not have known. Judge a decision by what was knowable at the time.

| Check | Question |
|---|---|
| Framing | Did we solve the right problem? |
| Options | Did we consider at least 3 real options, including "do nothing"? |
| Information | Did we seek evidence that could prove us wrong? |
| Reasoning | Are the trade-offs written down? |
| Process | Did the right people decide, at the right level, on time? |
| Commitment | Did we act on it fully? |

Review a sample of 5 to 10 past decisions each quarter against these checks, regardless of how they turned out.

## Biases to guard against

All from Kahneman's Thinking, Fast and Slow. Each has a cheap counter.

| Bias | How it shows up in engineering | Counter |
|---|---|---|
| Planning fallacy | Every estimate assumes the best case | Use the outside view: how long did similar projects take here? See [planning and forecasting](../playbook/ways-of-working/planning-and-forecasting.md). |
| Anchoring | The first number said in the room becomes the estimate | Estimate alone in writing before discussing |
| Sunk cost | "We have spent two years on this platform, we cannot stop now" | Ask: knowing what we know now, would we start this today? |
| Overconfidence | Narrow ranges on forecasts that turn out wrong | Give ranges with a stated confidence level and track how often you hit them |
| What you see is all there is | A decision built on the one dashboard that was available | Ask "what information would change our mind, and do we have it?" |
| Availability | Last month's outage dominates this year's priorities | Look at incident and risk data over 12 months |
| Loss aversion | Refusing to retire a system because someone will lose something | State the cost of keeping it as clearly as the cost of losing it |
| Halo effect | A respected engineer's proposal gets less scrutiny | Use the same review checklist for every proposal, whoever wrote it |
| Hindsight and outcome bias | Blame after a bad outcome | Judge decisions with the quality checks above |

## Common mistakes

| Mistake | Fix |
|---|---|
| Every decision goes to a committee | Classify first. Most decisions are light. |
| No owner, so the group "agrees" and nobody acts | One accountable person per decision, named at the start |
| Decisions with no deadline | Set the deadline when the decision is raised |
| Consensus required | Consult widely, then the owner decides. Consensus is a bonus, not a gate. |
| Decisions reopened by whoever was absent | Reopen only at the review date or with new evidence |
| Pre-mortem held after the decision is announced | Hold it before, while the plan can still change |

## Templates

- [Pre-mortem](../templates/leaders/pre-mortem.md)
- [Architecture decision record](../templates/docs/adr.md)
- [RACI](../templates/strategy/raci.csv)

## Sources

- Jeff Bezos, 2015 Letter to Shareholders, Amazon.com, Inc. (filed with the SEC in April 2016): https://www.sec.gov/Archives/edgar/data/1018724/000119312516530910/d168744dex991.htm
- Jeff Bezos, 2016 Letter to Shareholders, Amazon.com, Inc.
- David J. Snowden and Mary E. Boone, "A Leader's Framework for Decision Making", Harvard Business Review, November 2007: https://hbr.org/2007/11/a-leaders-framework-for-decision-making
- Gary Klein, "Performing a Project Premortem", Harvard Business Review, September 2007: https://hbr.org/2007/09/performing-a-project-premortem
- Daniel Kahneman, "Thinking, Fast and Slow", Farrar, Straus and Giroux, 2011.
- Andy Grove, "High Output Management", Random House, 1983.
- Michael Nygard, "Documenting Architecture Decisions", 2011: https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions
