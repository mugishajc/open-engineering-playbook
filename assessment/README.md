# Maturity assessment

The assessment turns the Open Engineering Playbook's practice levels into a yes or no checklist you keep in git. You answer 84 questions in a TOML file, the script tells you the level each of the 14 practice areas has reached, the level your profile calls for, and the next five things to do. Because the answers are a text file, every quarter's result is a commit you can diff, review and show an auditor.

Python 3.11 or later, standard library only. No network access, no account, no data leaves your machine.

## Run it

```bash
# 1. Write a blank answers file. Every answer starts as false.
python3 assessment/assess.py --questions assessment/questions.toml --init --profile startup > my-answers.toml

# 2. Edit my-answers.toml: set your profile and overlays, then set each answer to true
#    only when you can point to the evidence.

# 3. Score it.
python3 assessment/assess.py --questions assessment/questions.toml --answers my-answers.toml
python3 assessment/assess.py --questions assessment/questions.toml --answers my-answers.toml --format json --output report.json
```

Try it first on [example-answers.toml](example-answers.toml), a fictional startup of 12 engineers.

| Option | What it does |
|---|---|
| `--questions FILE` | The question bank. Defaults to `questions.toml` next to the script. |
| `--answers FILE` | Your answers file. |
| `--format markdown` or `json` | Report format. Markdown is the default. |
| `--output FILE` | Write the report or the blank answers file here instead of standard output. |
| `--init` | Write a blank answers file, every id set to false with the question as a comment. |
| `--profile NAME` | The profile written into the blank file by `--init`. |
| `--force` | Let `--init` replace an existing `--output` file. |
| `--allow-missing` | Count unanswered questions as false instead of failing. Useful after the question bank grows. |
| `--actions N` | How many next actions to list. Default 5. |
| `--link-base URL` | Prefix for playbook links in the report, for example `https://github.com/mugishajc/open-engineering-playbook/blob/main/`. |
| `--check` | Exit with code 1 when any area is below its target. Use it in CI. |

Exit codes: 0 for a report, 1 when `--check` finds an area below target, 2 for invalid input. Invalid input includes an unknown question id (the error suggests the closest real one), a missing answer, a value that is not `true` or `false`, and an unknown profile or overlay.

## The answers file

```toml
profile = "startup"          # solo, sme, startup, scale-up or enterprise
overlays = []                # add "public-sector" and/or "regulated" when they apply

[answers]
# [foundation] Is the default branch protected, so changes land only through a pull or merge request?
"delivery.protected-default-branch" = true
```

Nested tables work too: `[answers.delivery]` followed by `protected-default-branch = true` is the same answer.

## How scoring works

Each question belongs to one practice area (the part of the id before the full stop) and one level: Foundation, Standard or Assured.

1. **Level reached.** An area reaches a level only when every question at that level, and every question at each level below it, is true. An area with one Foundation question false is "Below Foundation", however many Standard questions are true. A level with no questions in an area is never reached.
2. **Target.** Solo and Startup aim for Foundation. Scale-up and Enterprise aim for Standard. Any overlay (`public-sector` or `regulated`) sets the target to Assured.
3. **Gap.** The number of levels between the level reached and the target, per area.
4. **Next actions.** All false questions at or below the target, ordered by level first (every Foundation gap before any Standard gap), then the weakest area first, then the order in the question bank. If fewer than five remain, the list continues with questions above your target, marked as beyond your target.

There is no weighted score. A single number hides which control is missing, and auditors and teams both need to know that.

## Use it in a quarterly review

1. A week before the review, each team lead updates the team's answers file in a pull request. A peer from another team reviews it and asks for evidence on any answer that changed to true.
2. Merge the pull request. Generate the report with `--format markdown` for people and `--format json` if you combine teams.
3. In the review, spend the time on the next actions, not the table. Pick at most three per team for the next quarter and put them in the team's plan with an owner.
4. If an answer is true but the evidence is weak, set it back to false. An honest Below Foundation is worth more than a false Standard.

## Track it in git over time

Keep the answers files in a repository, one per team or one for the organisation:

```
assessments/
  payments.toml
  platform.toml
  reports/
```

- The commit history is the record. `git log -p assessments/payments.toml` shows when each answer changed and who changed it.
- `git diff v2026-q3 v2026-q4 -- assessments/` shows a quarter's progress. Tag each quarter.
- Add a CI job that runs the assessment with `--check` on the main branch if you want a failing build when a team falls below its target. Most organisations use it as a report, not a gate, for the first year.
- Question ids never change once published, so old answers files keep working. When new questions are added, run with `--allow-missing` once, then add the new ids.

## Change the questions

`questions.toml` is plain TOML. Fork it to tune numbers (for example, a review time limit of two working days instead of one) or add questions for your own rules. Each question needs an `id` of the form `area.short-name`, a `level`, the question `text`, the `action` to take when the answer is false, and a `link` to the page that explains it. Keep 4 to 6 questions per area and at least one per level, so every level is reachable.

Run the tests after any change:

```bash
python3 -m unittest discover -s assessment/tests
```
