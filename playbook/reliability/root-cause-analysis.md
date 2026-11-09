# Root cause analysis

Analyse incidents to find the set of conditions that made them possible, not a single root cause or a person to blame. In complex systems, failures need several things to go wrong at once: a change, a missing test, an alert that stayed quiet, a deadline, an unclear runbook. Fixing only the last step leaves the others in place, and the next incident uses them.

## Outcomes

Starting points. Tune them to your incident volume.

- Every SEV1 and SEV2 [postmortem](postmortems.md) lists at least 3 contributing factors, covering detection, response and recovery, not only the trigger.
- At least half of action items address a class of failure (for example "all configuration pushes", "all services using this client library"), not only the one bug.
- No postmortem names "human error" as a cause without the conditions that made the error likely.
- Repeat incidents with the same contributing factor within 6 months fall quarter on quarter.
- Every incident commander and postmortem facilitator is trained in at least one technique on this page.

## Why "root cause" is usually plural

- **The trigger is not the cause.** The deployment that broke production was the last event. The missing canary, the shared failure domain and the alert that paged the wrong team were all needed too.
- **Stopping at one cause is a choice.** Every chain of "why" can continue. Where you stop decides what you fix, so stop where action items become possible and useful, and look sideways as well as backwards.
- **Hindsight makes the path look obvious.** After the fact, the warning signs are clear. At the time, they were mixed in with hundreds of normal signals. Analysis that ignores this blames people and fixes nothing.

## Techniques

| Technique | What it does | Use when |
|---|---|---|
| Timeline reconstruction | Builds a minute-by-minute record in UTC from logs, chat, alerts and deployments, from the first signal to full recovery | Always. Every other technique starts here. |
| Contributing-factor analysis | Lists every condition that made the incident possible, worse or longer, grouped by detection, response and recovery | Always. This is the default for the postmortem. |
| 5 Whys | Asks "why?" repeatedly from the symptom | Only as a starting prompt. Used alone it follows one chain and stops at a person or one bug. Run it several times from different starting points. |
| Fishbone (Ishikawa) diagram | Groups possible causes into categories such as people, process, tools, environment, code, dependencies | When the team is stuck on one explanation and needs to see other categories. |
| CAST (Causal Analysis based on System Theory) | From Nancy Leveson's STAMP work at MIT. Models the system as a set of controls and feedback loops, and asks why each control did not prevent the loss | SEV1 incidents, safety-related systems, and repeated incidents where simple fixes have failed. |
| "How did it make sense at the time?" | From Sidney Dekker's *The Field Guide to Understanding Human Error*. Reconstructs what each person knew, saw and was under pressure to do | Whenever a person's action is part of the story. |

## Practice

### Foundation

1. Build the timeline first, from evidence, before anyone proposes a cause.
2. Ask three questions separately:
   - **Detection:** why did it take this long to know? Who noticed first, a user or a system?
   - **Response:** what slowed diagnosis and mitigation? Missing runbook, missing access, unclear ownership?
   - **Recovery:** why did restoring service take as long as it did? Was rollback possible? (see [rollbacks](rollbacks.md))
3. For each human action that contributed, write what the person knew at the time and why the action looked reasonable.
4. Write contributing factors in the [postmortem template](../../templates/docs/postmortem.md). Aim for 3 to 7.

### Standard

1. **Use more than one technique** for SEV1 incidents: timeline plus contributing factors as a minimum, plus a fishbone or CAST when the cause is disputed.
2. **Look for classes of failure.** For each factor, ask "where else does this condition exist?" If a configuration push skipped staged rollout here, which other configuration pipelines do the same? Write action items for the class.
3. **Tag every contributing factor** with a shared list (for example `change-config`, `change-code`, `capacity`, `dependency`, `alerting-gap`, `runbook-gap`, `access`, `knowledge`). Review tag counts every quarter. The top tags show where to invest.
4. **Trained facilitators.** People outside the team run the analysis for SEV1 incidents. They ask about conditions, not culprits, and challenge the first plausible story.
5. **Check the fix against the factor.** Each action item names the contributing factor it addresses. A factor with no action is an accepted risk; say so.

### Assured

Everything in Standard, plus:

1. **CAST for every SEV1** in safety-related, financial market or critical infrastructure systems. Record the control structure diagram with the postmortem.
2. **Trend reporting** to the risk committee every quarter: top contributing-factor tags, repeat incidents and overdue class-level actions.
3. **Independent review** of the analysis for incidents reported to a regulator. The regulator's final report and the internal analysis must agree.
4. These records support ISO/IEC 27001:2022 control 5.27 (learning from information security incidents) and SOC 2 CC7.4.

## Cloud, on-premises and air-gapped

- **Collect evidence before it expires.** Cloud logs, load balancer logs and container logs often have short default retention. Export what you need within 24 hours of the incident.
- **Air-gapped networks** often have less telemetry. Missing data is itself a contributing factor to detection; record it.
- **Vendor-caused incidents.** Ask the vendor for their analysis, and still analyse your own conditions: single vendor, no fallback, no staged adoption of their updates.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Root cause: engineer ran the wrong command" | Ask why the command was possible, easy and not caught. Those are the factors. |
| 5 Whys run once, ending at one bug | Run it from several starting points, or use contributing-factor analysis. |
| Analysis starts before the timeline exists | Timeline first, from evidence. |
| Action item fixes only the bug that triggered it | Ask where else the condition exists; fix the class. |
| Detection and recovery factors ignored | Analyse detection, response and recovery as three separate questions. |
| Same people always facilitate their own incidents | Facilitator from outside the team for SEV1. |

## Templates

- [Postmortem](../../templates/docs/postmortem.md)
- [Incident update](../../templates/docs/incident-update.md)

## Sources

- Nancy Leveson, *Engineering a Safer World: Systems Thinking Applied to Safety*, MIT Press, 2011 (open access).
- Nancy Leveson, *CAST Handbook: How to Learn More from Incidents and Accidents*, MIT Partnership for Systems Approaches to Safety and Security, 2019: http://psas.scripts.mit.edu/home/get_file.php?name=CAST_handbook.pdf
- Sidney Dekker, *The Field Guide to Understanding Human Error*, 3rd edition, CRC Press, 2014: https://www.routledge.com/The-Field-Guide-to-Understanding-Human-Error/Dekker/p/book/9781472439055
- Google, *Site Reliability Engineering*, "Postmortem Culture: Learning from Failure": https://sre.google/sre-book/postmortem-culture/
