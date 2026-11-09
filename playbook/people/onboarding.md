# Onboarding

Plan a new engineer's first 90 days before they arrive: accounts ready on day one, a working build on day one, a first merged pull request in the first week, and clear goals at 30, 60 and 90 days. Every week a new hire spends waiting for access or guessing what to do is paid salary with no output and a poor first impression. Treat onboarding as a process you measure and improve, and let each new hire improve it for the next one.

## Outcomes

Starting points. Tune them to your organisation.

- 100% of accounts and hardware ready before the start date.
- The new engineer builds and runs the main system locally (or in a cloud development environment) on day one.
- Time to first merged pull request: 5 working days or less (3 for a Startup).
- Time to first change in production: 10 working days or less.
- New hires rate onboarding at least 4 out of 5 at day 30 and day 90, and every new hire makes at least one fix to the onboarding docs.

## The plan

| When | Goals |
|---|---|
| Before day one | Accounts created through the identity provider from a role template. Laptop imaged and shipped. Buddy named. First-week calendar sent. |
| Day one | Meet manager and buddy. Log in everywhere. Clone, build and run tests for the main repository. Read the team's README, [principles](../principles.md) and the on-call overview. |
| First week | First pull request merged: a small, real fix chosen in advance (a "good first issue"). Sit with the buddy through one code review and one deploy. Complete required security and privacy training. |
| First 30 days | Ship at least 3 changes to production. Read the team's architecture decision records (ADRs) and the architecture overview. Join code review as a second reviewer. Fix something in the onboarding docs. Take the [true-or-false quiz](../../exercises/true-or-false/README.md) for the team's areas and discuss the misses with the buddy. |
| First 60 days | Own a small feature from design to production. Review pull requests as a primary reviewer. Shadow one on-call rotation. |
| First 90 days | Work independently on normal tasks. Take a primary on-call shift if the team runs on-call, after at least 1 shadow rotation. Give written feedback on onboarding to the manager. |

## Practice

### Foundation

- A one-page onboarding checklist in the repository, based on the [onboarding checklist template](../../templates/docs/onboarding-checklist.md).
- A README that gets a new engineer from clone to running tests in under 1 hour (see [documentation](documentation.md)).
- A buddy who is not the manager and who has at least 2 hours a day free in week one.
- 3 to 5 labelled "good first issue" tickets ready at all times.

### Standard

- Access is granted automatically from role-based groups in the identity provider. No one waits on a chain of tickets.
- A cloud development environment or a scripted local setup that takes under 30 minutes.
- Track time to first merged pull request and time to first production change for every hire. Review the numbers each quarter.
- Short surveys at day 30 and day 90. The same 5 questions each time so results can be compared.
- A recorded walkthrough of the architecture, refreshed when the architecture changes.
- Managers hold a 30-, 60- and 90-day check-in with written goals.
- Add each new hire to the team skills matrix at day 30 and plan pairing for the gaps (see [skills gap](skills-gap.md)).

### Assured

- Access follows least privilege. No production access until required training is complete and recorded. Production access is time-bound and approved (see [access control](../security/access-control.md)).
- Training completion, policy acknowledgements and screening checks required by your policy are recorded with dates, as audit evidence.
- An access review at day 90 confirms the new engineer holds only what the role needs.
- Leaver process mirrors joiner process: privileged access removed within 4 hours of the departure time and all other access within 1 working day, with evidence (the targets in [access control](../security/access-control.md)). This supports ISO/IEC 27001 and SOC 2 access control requirements; see [control mapping](../compliance/control-mapping.md).

## Cloud, on-premises and air-gapped

- Air-gapped or classified work often needs security clearance, which can take weeks or months. Give the new engineer useful work on an unclassified network meanwhile: a mirror of the codebase without sensitive data, the docs, the training.
- Install development tools from internal mirrors and test the setup script on a clean machine on the isolated network every quarter. A setup that silently downloads from the internet will fail on day one.
- Keep onboarding docs on the internal docs site, not on a public wiki.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Read the wiki" as the whole plan | A written 90-day plan with named goals and a buddy. |
| Accounts requested on the start date | Requested from a role template when the offer is signed. |
| First task is a large feature | First task is small, real and chosen in advance. |
| Setup instructions nobody has followed for a year | Every new hire follows them and fixes what is wrong. CI runs the setup script. |
| Production access on day one "to save time" | Access after training, scoped to the role, time-bound where possible. |

## Templates

- [Onboarding checklist](../../templates/docs/onboarding-checklist.md)
- [Contributing guide](../../templates/repo/CONTRIBUTING.md)

## Sources

- DORA capabilities, including documentation quality and learning culture: https://dora.dev/capabilities/
- Matthew Skelton and Manuel Pais, Team Topologies (2019), on team cognitive load: https://teamtopologies.com/
