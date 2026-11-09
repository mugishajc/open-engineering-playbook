<!--
Open Engineering Playbook merge request template. Copy to .gitlab/merge_request_templates/Default.md
and set it as the project default in Settings > Merge requests.
Title format (checked in CI): type(scope): description
Example: feat(invoices): add CSV export
Delete any section that does not apply, and say why in one line.
-->

## What and why

<!-- What does this change do, and why is it needed now? -->

Closes #

## How tested

- [ ] Unit or component tests added or updated
- [ ] Tested locally or in a review app:

## Risk and rollback

- Risk level: low / medium / high
- Behind a feature flag: no / yes (flag name:)
- Database migration: no / yes (backward compatible with the running version: yes / no)
- Rollback plan: <!-- revert this merge request, turn off the flag, or describe the steps -->

## Checklist

- [ ] The merge request is small enough to review well (aim for under about 400 changed lines)
- [ ] I reviewed my own diff first
- [ ] Pipeline is green
- [ ] Docs, runbook or changelog updated where users or operators will notice the change
- [ ] No secrets, credentials or personal data in code, tests, logs or screenshots
- [ ] Security-sensitive change (auth, crypto, payments, personal data, CI, infrastructure): specialist reviewer added
- [ ] I understand and can explain every line, including any code produced with tools or code assistants

/assign me
