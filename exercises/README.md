# Exercises

Reading a practice is not the same as being able to do it at 02:00 with the chat system down. These exercises let you practise the playbook before a real incident, review or board meeting tests it: alone in 20 minutes, as a team in 90, or as a leadership group in an hour. Each one links back to the page that teaches the practice, so every mistake points to something to read.

## What is here

| Format | What it is | Who | Time |
|---|---|---|---|
| [True or false](true-or-false/README.md) | About 150 statements across all fourteen areas plus leaders. Myths that sound right, facts that sound wrong. Play on GitHub or in a terminal with [`quiz.py`](quiz.py). | Anyone | 10 to 20 minutes |
| [Katas](#katas) | Short, focused practice on one skill, with a model answer to compare against | One person or a pair | 30 to 45 minutes |
| [Tabletop exercises](#tabletop-exercises) | A bad day rehearsed around a table: a scenario, timed injects, decisions, a scored debrief | A team of 4 to 10, with a facilitator | 60 to 90 minutes |
| [Decision games](#decision-games) | Choose-your-path decisions for leaders, with the consequences of each option revealed | A leader alone, or a leadership group | 30 to 45 minutes |

### Katas

| Kata | You practise | Minutes |
|---|---|---|
| [Review this pull request](katas/review-this-pull-request.md) | Finding seven seeded problems in a short diff: security, migrations, tests, naming, size | 30 |
| [Find the contributing factors](katas/find-the-contributing-factors.md) | Turning an incident timeline into factors and class-level actions, not blame | 40 |
| [Error budget math](katas/error-budget-math.md) | Budgets, burn rates, alert thresholds and dependency limits, with worked answers | 30 to 40 |
| [Write the ADR](katas/write-the-adr.md) | Writing a decision record that someone who disagrees would still call fair | 45 |
| [Threat model a feature](katas/threat-model-a-feature.md) | STRIDE on a "share by link" feature that crosses four trust boundaries | 45 |

### Tabletop exercises

Start with the [facilitator guide](tabletop/facilitator-guide.md). It covers roles, timing, injects, rules, the debrief and how to turn findings into actions.

| Scenario | Tests | Minutes |
|---|---|---|
| [Ransomware at 2 a.m.](tabletop/ransomware-at-2am.md) | Isolation, out-of-band communication, immutable backups, the ransom question, the 72-hour clock | 90 |
| [Cloud region outage](tabletop/cloud-region-outage.md) | Fail over or wait, what a standby region really needs, reconciling money, failing back | 90 |
| [The chatbot leaks data](tabletop/chatbot-leaks-data.md) | AI kill switches, retrieval permissions, prompt injection against tools, sensitive data breach | 90 |
| [Actively exploited vulnerability: the CRA clock](tabletop/actively-exploited-vulnerability-cra-clock.md) | The EU Cyber Resilience Act 24-hour early warning, staged mitigation, shipping a fix under pressure | 90 |
| [Bad deploy at peak](tabletop/bad-deploy-at-peak.md) | Roll back or roll forward, schema changes that block rollback, the error budget policy | 75 |
| [Key engineer resigns](tabletop/key-engineer-resigns.md) | Key-person risk, knowledge transfer in four weeks, what a resignation says about the team | 60 |
| [Supplier breach](tabletop/supplier-breach.md) | Knowing what a supplier can reach, cutting it off without stopping the business, your clock not theirs | 90 |
| [The quantum question from the board](tabletop/quantum-question-from-the-board.md) | Explaining a long-term risk honestly, cheap work now, procurement that will outlast 2035 | 60 |

### Decision games

| Game | The decision | Minutes |
|---|---|---|
| [Monolith or microservices](decision-games/monolith-or-microservices.md) | A slow, tangled monolith and a plan for fourteen services | 30 |
| [Build, buy or adopt](decision-games/build-buy-or-adopt.md) | A public agency's sign-in system with a data residency rule | 30 |
| [Cloud exit](decision-games/cloud-exit.md) | A cloud bill that tripled and a spreadsheet that promises 60% savings | 30 |
| [AI pilot to production](decision-games/ai-pilot-to-production.md) | A bank's credit memo assistant and a three-week deadline | 30 |

## How to use them

### Alone

1. Take the true or false quiz for your area. Note the three pages it suggests.
2. Do one kata a week. Write your answer before you open the `<details>` blocks; the value is in the attempt, not in reading the answer.
3. Repeat a kata a month later on your own system: review your last pull request, find the contributing factors in your last postmortem, compute your own service's error budget.

### As a team

- **Monthly, 45 minutes:** one kata done in pairs, then 15 minutes comparing answers. Review and threat modelling work best this way.
- **Quarterly, 90 minutes:** one tabletop exercise. The [incident management](../playbook/reliability/incident-management.md) page sets a starting target of a game day or tabletop every quarter. Rotate the incident commander.
- **After a real incident:** run the closest tabletop scenario within two months, with the actions from the postmortem in place, to check they work.

### As a leadership group

- **Twice a year, 60 to 90 minutes:** a tabletop with the executive team: ransomware, supplier breach or the quantum question. Read [crisis leadership](../leaders/crisis-leadership.md) first.
- **Before a large decision:** play the matching decision game as a group, each person choosing alone first, then compare. Disagreement in the room is useful data. See [decision making](../leaders/decision-making.md).
- **New leaders:** the four decision games and the quantum tabletop make a good first-month set alongside the [first 90 days](../leaders/first-90-days.md) plan.

## Running a session

| Before | During | After |
|---|---|---|
| Pick the exercise for a real gap: a recent near miss, an audit finding, a new regulation | Keep to time. A missed decision is a finding, not a reason to extend. | Write down 3 to 7 actions, each with one owner and a date |
| Book the right people, including someone from outside the team for tabletops | No blame. Test the system, the runbooks and the decision rights, not people. | Put actions in the normal backlog with an `exercise` or `tabletop` label |
| Use your real runbooks, contact lists and dashboards, not fictional ones | Say decisions out loud and record them | Track completion like postmortem actions; review overdue items monthly |
| Print injects or answers if people will be away from screens | Score the rubric together at the end | Reuse the inject that exposed a gap in the next exercise to test the fix |

## What to do afterwards

- **Record it.** Date, exercise, attendees, scores and actions. The trend across quarters matters more than any one score.
- **Fix classes, not instances.** An action that updates one phone number helps once. An action that checks every escalation list against the leavers list each quarter keeps helping. See [root cause analysis](../playbook/reliability/root-cause-analysis.md).
- **Keep evidence where it is needed.** For regulated and public sector organisations, exercise records are evidence for incident readiness and business continuity controls. See [control mapping](../playbook/compliance/control-mapping.md).
- **Write your own.** The best scenario is the incident you nearly had. Copy the layout of any file here, change the organisation and the injects, and keep the links to the playbook.

## Contributing exercises

New scenarios, katas and decision games are welcome. Use fictional organisations with neutral descriptions, mark all numbers as fictional, link every recommendation to a playbook page, and hide answers in `<details>` blocks. Run `python3 tools/plain_lint.py exercises` before you open a pull request. See [CONTRIBUTING.md](../CONTRIBUTING.md).
