# Source control

Use trunk-based development: everyone merges small changes into one protected default branch at least once a day, through a reviewed pull request. Keep long-lived release branches only for software that customers install and run themselves, where you must patch an old version. Protect the default branch with rules the platform enforces, not with a wiki page people forget.

## Outcomes

Starting targets. Tune them to your context and measure them every quarter.

| Signal | Starting target |
|---|---|
| Median age of a branch when it merges | Under 2 days |
| Branches older than 7 days | Fewer than 10% of open branches |
| Direct pushes to the default branch | Zero, outside a logged break-glass process |
| Repositories with a named owner in CODEOWNERS | 100% |
| Repositories with branch protection or a ruleset on the default branch | 100% |
| Merge conflicts that take more than 30 minutes to resolve | Rare enough that nobody can name the last one |

## Practice

### Foundation

- **One default branch, called `main`.** All work starts from it and returns to it.
- **Short-lived branches.** Create a branch per change, open a pull request early, merge within 2 days. Long work is split into small, safe steps. Hide unfinished behaviour behind a [feature flag](feature-flags.md) instead of keeping it on a branch.
- **Squash merge by default.** The pull request title becomes the commit message on `main`, written in [Conventional Commits](versioning-and-changelogs.md) form (`feat: add export to CSV`). This gives a linear, readable history and a clean input for changelog tools.
- **Protect `main`.** No force pushes, no deletion, no direct pushes, at least one approving review, CI must pass. On GitLab, use protected branches. On GitHub, use the [team ruleset](../../templates/github/rulesets/default-branch.json).
- **Import the ruleset; a file in the repository does nothing.** GitHub does not read rulesets from files. Import the JSON once with `gh api -X POST repos/OWNER/REPO/rulesets --input default-branch.json`, or in Settings, Rules, Rulesets, New ruleset, Import a ruleset. Then check that a direct push to `main` is rejected. [`tools/adopt.sh`](../../tools/adopt.sh) prints the exact command.
- **Check your plan.** Rulesets and branch protection work on public repositories on every GitHub plan, but on private repositories only with GitHub Pro, Team or Enterprise. On GitHub Free with a private repository, nothing stops a direct push: upgrade, or rely on CI plus the `no-commit-to-branch` pre-commit hook and know that both can be skipped.
- **Never commit secrets.** Add a secret scanner as a pre-commit hook and in CI ([`.pre-commit-config.yaml`](../../templates/repo/.pre-commit-config.yaml)). If a secret lands in history, rotate it first, then clean history. Rewriting history does not un-leak a key. See [secrets](../security/secrets.md).
- **Ignore build output.** Commit a `.gitignore` and an [`.editorconfig`](../../templates/repo/.editorconfig). Store large binaries in Git LFS or an artifact repository, not in Git.
- **Solo engineers** still use pull requests. A pull request gives you a CI gate, a self-review step and a record of why a change happened. GitHub does not let you approve your own pull request, so the team ruleset would block every merge. Use the [solo ruleset](../../templates/github/rulesets/default-branch-solo.json) (`tools/adopt.sh --solo`): pull request and CI still required, no second approval. Switch to the team ruleset when a second engineer joins.

### Standard

- **Rulesets at organisation level.** Define default-branch rules once and apply them to every repository, so new repositories are protected on day one. Use repository-level rules only for exceptions, and record each exception.
- **Required status checks.** Name the exact CI jobs that must pass (for example `lint`, `test`, `build`, `pr-title`). Require branches to be up to date before merge, or use a merge queue when `main` is busy.
- **Bind each required check to the app that runs it.** A check matched by name alone can be satisfied by any integration or token that can post a status called `lint`. The templates set `integration_id` to 15368, the GitHub Actions app on github.com. On GitHub Enterprise Server, look up the ID on your server.
- **Bots that open pull requests need their own token.** Pull requests opened by the default `GITHUB_TOKEN` start CI only after a person approves the runs, so a required check waits on every update. Release and update bots use a GitHub App token. See the [release-please workflow](../../templates/github/workflows/release-please.yml).
- **Require linear history.** Allow squash or rebase merges, not merge commits, on `main`.
- **Code owners.** Every repository has a [`CODEOWNERS`](../../templates/github/CODEOWNERS) file that maps paths to teams, not individuals. Require code owner review on paths that carry risk: migrations, auth, CI, infrastructure.
- **Merge queue** when more than about 20 pull requests merge per day into one branch, or when `main` breaks because two green changes conflict.
- **Release branches only when justified.** See the table below.
- **Archive dead repositories.** Review repositories with no commits in 12 months. Archive them or name an owner.

#### When a release branch is justified

| Situation | Branching model |
|---|---|
| SaaS or internal service, you deploy every version yourself | Trunk only. Deploy from `main`. Roll back by redeploying the previous artifact. |
| Mobile app or desktop app with store review | Trunk, plus a short-lived `release/x.y` branch cut for store submission, deleted after the next release. |
| Software customers install on-premises, or with a Long Term Support (LTS) promise | Trunk, plus one `release/x.y` branch per supported version, kept until end of support. |
| Regulated release that must match an approved, audited build | Trunk, plus a tag on the exact commit that was approved. A branch only if you must patch that release. |

Rules for release branches:

1. Cut the branch from `main`. Never develop features on it.
2. Fix bugs on `main` first, then cherry-pick to the release branch (`git cherry-pick -x` records the source commit). The only exception is a fix for code that no longer exists on `main`.
3. Never merge a release branch back into `main`.
4. Protect release branches with the same ruleset as `main`.
5. Delete or archive the branch when the version reaches end of support. See [release management](release-management.md) for the LTS policy.

### Assured

- **Signed commits on protected branches.** Require signatures with the `required_signatures` rule. Engineers sign with SSH keys, GPG keys, or Sigstore `gitsign` for keyless signing tied to company identity. With squash merge, the platform signs the final commit, so also require signed commits on the pull request branch if you need author-level proof.
- **No bypass without a record.** Limit ruleset bypass to a break-glass group of 2 to 3 people. Every bypass creates a ticket that a second person reviews: within 2 working days for an emergency change during a declared incident, within 1 working day for any other bypass (see [change management](../reliability/change-management.md)).
- **Separation of duties.** The person who writes a change cannot be the only person who approves it. See [code review](code-review.md#assured).
- **Audit trail.** Export repository audit logs (ruleset changes, permission changes, bypasses, force pushes) to your log store and keep them for your records retention period.
- **Source provenance.** Track progress against the SLSA Source track (v1.2) so you can show that every change on a protected branch was reviewed and attributable. See [supply chain](../security/supply-chain.md).
- **Map to controls.** These practices give evidence for ISO/IEC 27001:2022 Annex A 8.4 (access to source code) and 8.32 (change management), and SOC 2 CC8.1. See [control mapping](../compliance/control-mapping.md).

## Monorepo or polyrepo

Choose by how your teams ship, not by fashion. Either works with trunk-based development.

| Factor | Monorepo | Polyrepo |
|---|---|---|
| Atomic change across many components | One pull request | Several coordinated pull requests |
| Shared code and tooling | Easy to share, easy to over-couple | Shared through versioned packages |
| CI cost | Needs build tooling that runs only affected targets (Bazel, Nx, Pants, Turborepo or similar) | Each repository builds its own small graph |
| Access control | Path-level, through CODEOWNERS and tooling | Repository-level, simpler to audit |
| Ownership boundaries | Need discipline and CODEOWNERS | Visible from the repository list |
| Good fit | One product, teams that change shared code often | Independent services, external contributors, strict access separation |

Starting rule: one repository per independently deployed service or library, unless several services always change together. If more than about 30% of pull requests need matching changes in another repository, consider merging those repositories.

## Cloud, on-premises and air-gapped

- **Self-hosted platforms.** GitLab self-managed, GitHub Enterprise Server, Gitea or Forgejo and Bitbucket Data Center all support protected branches, required reviews and code owners. Check the exact feature set of your edition before you write policy that depends on it.
- **Mirrors.** In air-gapped networks, mirror upstream open source repositories into the internal platform through a reviewed import process, and record the upstream commit hash.
- **Signing without internet.** Keyless `gitsign` needs a reachable Sigstore instance. Air-gapped teams use SSH or GPG signing keys, or run a private Sigstore deployment.
- **Backups.** A self-hosted Git server is a production system. Back it up and test restores. See [backup and recovery](../reliability/backup-and-recovery.md).

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| GitFlow-style `develop` branch for a web service you deploy yourself | Merge to `main` and deploy from it. Use flags to hide unfinished work. |
| Feature branches that live for weeks | Split the work. Merge behind a flag. Track branch age as a team metric. |
| Release branches merged back into `main` | Fix on `main` first, then cherry-pick to the release branch. |
| Branch protection set by hand per repository | Organisation-level rulesets, kept as code. |
| CODEOWNERS listing people who left | Use team handles. Review CODEOWNERS every quarter. |
| Admins who bypass protection "because it is faster" | Remove standing bypass. Use break-glass with a ticket. |
| Secrets removed from history and not rotated | Rotate first. Assume a pushed secret is public. |

## Templates

- [GitHub ruleset for the default branch, team](../../templates/github/rulesets/default-branch.json) and [solo](../../templates/github/rulesets/default-branch-solo.json)
- [GitHub CODEOWNERS](../../templates/github/CODEOWNERS)
- [GitLab CODEOWNERS](../../templates/gitlab/CODEOWNERS)
- [.editorconfig](../../templates/repo/.editorconfig)
- [.pre-commit-config.yaml](../../templates/repo/.pre-commit-config.yaml)
- [CONTRIBUTING.md](../../templates/repo/CONTRIBUTING.md)

## Sources

- Trunk-based development reference: https://trunkbaseddevelopment.com/
- GitHub, about rulesets: https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/about-rulesets
- GitHub REST API, repository rules: https://docs.github.com/en/rest/repos/rules
- GitHub, managing rulesets (import a ruleset): https://docs.github.com/en/repositories/configuring-branches-and-merges-in-your-repository/managing-rulesets/managing-rulesets-for-a-repository
- GitHub, triggering a workflow from a workflow (GITHUB_TOKEN limits): https://docs.github.com/en/actions/how-tos/write-workflows/choose-when-workflows-run/trigger-a-workflow
- GitHub, about code owners: https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-code-owners
- GitLab, protected branches: https://docs.gitlab.com/ee/user/project/protected_branches.html
- Git book, signing your work: https://git-scm.com/book/en/v2/Git-Tools-Signing-Your-Work
- Sigstore gitsign: https://github.com/sigstore/gitsign
- SLSA specification: https://slsa.dev/spec/
- Conventional Commits 1.0.0: https://www.conventionalcommits.org/en/v1.0.0/
