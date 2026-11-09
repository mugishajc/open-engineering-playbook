<!-- plain-lint: ignore-file (this page has to quote the words it bans) -->
# Writing style

The playbook is read by solo engineers, CTOs, auditors, procurement officers and ministers' technical advisers. Most of them are busy and many read English as a second or third language. Every page is written for that reader.

## Rules

1. **Lead with the decision.** The first paragraph of every page says what to do and why. Background comes after.
2. **Short sentences.** Aim for under 25 words. One idea per sentence.
3. **Concrete over abstract.** "Review every pull request within one working day" beats "ensure timely reviews".
4. **Numbers you can check.** Every target is measurable. Every external claim links to its primary source. If a fact cannot be sourced, leave it out.
5. **Active voice, present tense.** "The author merges the change", not "the change is merged by the author".
6. **Plain words.** Use "use", not "utilise". Use "help", not "facilitate". Use "start", not "commence".
7. **No dashes as punctuation.** Do not use the em dash or the en dash. Use a comma, a colon, a full stop or brackets. For ranges write "1 to 5", not "1–5".
8. **No filler.** Cut "it is important to note", "in order to", "basically", "simply", "just".
9. **No hype.** The playbook does not "revolutionise" anything. Describe what a practice does and what it costs.
10. **No emojis** in the playbook or templates.
11. **British or American spelling is fine**, but stay consistent within one page.

## Words we do not use

These words are vague, overused, or signal text that was not written with care. The plain-language check in CI fails on them. The full list lives in [`tools/plain-language.txt`](tools/plain-language.txt).

| Instead of | Write |
|---|---|
| leverage | use |
| robust | reliable, tested, or say what it survives |
| seamless | say what the user no longer has to do |
| comprehensive | complete, or list what it covers |
| streamline | simplify, or say which step was removed |
| holistic | say which parts are included |
| best-in-class, world-class | say what makes it good, with evidence |
| empower | let, allow |
| ecosystem | tools, projects, community: name them |
| journey | process, plan, path |

## Page layout

Every page in `playbook/` follows the same shape so readers can scan:

```
# Title

Opening paragraph: the decision and the reason, in three sentences or fewer.

## Outcomes
Measurable signs that the practice is working.

## Practice
### Foundation   (solo, startup)
### Standard     (scale-up, enterprise)
### Assured      (regulated industries, public sector)

## Cloud, on-premises and air-gapped
What changes when you cannot reach the public internet or a hyperscaler.

## Anti-patterns
Common failures, each with the fix.

## Templates
Links into templates/.

## Sources
Primary sources only: standards bodies, official docs, peer-reviewed research.
```

A section can be skipped when it does not apply. Say so in one line rather than padding it.

## Checking your writing

```bash
python3 tools/plain_lint.py
```

The check runs on every pull request.
