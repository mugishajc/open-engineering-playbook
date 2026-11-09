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
12. **Expand acronyms.** Spell out an acronym the first time it appears on a page, for example "recovery time objective (RTO)", unless the page links to the [glossary](GLOSSARY.md). Add new terms to the glossary.
13. **One term per idea.** Use the terms in the table below. Readers of a second language assume two words mean two things.

## Words we do not use

These words are vague, overused, or signal text that was not written with care. The check in CI fails on every word in [`tools/plain-language.txt`](tools/plain-language.txt). The table shows the most common ones. Some words in the table, such as "journey" and "ecosystem", have exact uses ("user journey", a package ecosystem setting), so the list leaves them out and reviewers catch the vague uses.

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

## Terms we use

| Use | Not | Note |
|---|---|---|
| golden path | paved road | the [glossary](GLOSSARY.md) lists "paved road" as an alias |
| decision record (ADR) | architecture decision, design record | |
| Startup, Scale-up, SME (capital) when naming a profile | startup, scale-up | lower case for the general idea: "a startup with 12 engineers" |
| Tier 1, Tier 2, Tier 3 | tier 1, T1 | T1 only inside tables short of space |
| public sector (noun), public-sector (before a noun) | | "the public sector", "a public-sector body" |
| pull request (GitHub) or merge request (GitLab) | PR, MR | write both on pages that apply to both |
| DORA metrics; EU DORA regulation | DORA alone | always say which one |

## Page layout

Every page in `playbook/` follows the same shape so readers can scan:

```
# Title

Opening paragraph: the decision and the reason, in three sentences or fewer.

## Outcomes
Measurable signs that the practice is working.

## Practice
### Foundation   (SME, solo, startup)
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
python3 tools/plain_lint.py          # banned words and dashes
python3 tools/check_structure.py     # every page has the sections above
```

Both checks run on every pull request. They need Python 3.11 or later.
