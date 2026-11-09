# Continuous integration

Run an automated pipeline on every pull request and every merge to `main` that lints, tests and builds the change, and block merge until it passes. Keep the pull request pipeline under 10 minutes, because slow CI makes people batch changes and skip checks. Treat the pipeline as production code: pin what it runs, give it the least privilege it needs, and review changes to it.

## Outcomes

Starting targets. Tune them after a month of data.

| Signal | Starting target |
|---|---|
| Pull request pipeline duration | Median under 10 minutes, 90th percentile under 15 minutes |
| Time `main` stays red | Fixed or reverted within 30 minutes |
| Pipeline success rate on `main` | Above 95% |
| Third-party actions or CI includes pinned to a full commit SHA or digest | 100% at Standard and above |
| Workflows with explicit, minimal token permissions | 100% |
| Build artifacts produced outside CI and deployed to production | Zero |

## Practice

### Foundation

- **One pipeline, run on every pull request and every push to `main`.** Stages: lint, test, build. Use [`ci.yml`](../../templates/github/workflows/ci.yml) or [`.gitlab-ci.yml`](../../templates/gitlab/.gitlab-ci.yml).
- **Required checks.** Name the jobs that must pass in the default-branch ruleset. A pipeline that does not block merge is a report, not a control.
- **Same commands locally and in CI.** CI calls `make lint`, `make test`, `make build` (or your task runner). Engineers run the same targets on their machines. No logic lives only in CI YAML.
- **Fail fast.** Run the cheapest checks first. Cancel superseded runs on the same branch.
- **Fix `main` first.** If `main` goes red, the person whose change broke it fixes or reverts within 30 minutes. Revert is the default; fix forward is the exception.
- **Validate pull request titles** against Conventional Commits with [`pr-title.yml`](../../templates/github/workflows/pr-title.yml), because the title becomes the squash commit message and drives the changelog.
- **Pin language and tool versions** in the repository (`.tool-versions`, `.nvmrc`, `go.mod` toolchain line, `pyproject.toml`), and commit lockfiles.

### Standard

- **Under 10 minutes.** Get there with:
  - **Caching** of dependency downloads keyed on the lockfile hash. Never cache build outputs that a hash does not fully describe.
  - **Parallel jobs** and test sharding.
  - **Affected-only builds** in monorepos, using build tooling that knows the dependency graph.
  - **Moving slow suites** (full end-to-end, load tests) to post-merge or scheduled runs, with alerts to the owning team.
- **Hermetic builds.** A build uses only declared, pinned inputs: lockfiles, pinned base images by digest, pinned toolchains. It does not fetch "latest" anything. The same commit produces the same artifact. Aim for reproducible builds where your toolchain supports them.
- **Pin third-party actions by full commit SHA.** Tags can move; a SHA cannot. Keep the version in a comment so update tools can bump it:
  ```yaml
  - uses: actions/checkout@<full-40-character-sha> # v4
  ```
  The playbook templates use major version tags so they work when copied; switch to SHAs before you rely on them. Renovate (`helpers:pinGitHubActionDigests`) and Dependabot can keep SHAs up to date.
- **Least-privilege tokens.** Set `permissions: contents: read` at the top of every workflow and grant more only to the job that needs it. Set `persist-credentials: false` on checkout unless a later step pushes. On GitLab, limit the `CI_JOB_TOKEN` allowlist.
- **No long-lived cloud keys in CI.** Use OpenID Connect (OIDC) federation from the CI platform to the cloud provider, with roles scoped to one repository and one branch or environment.
- **Untrusted input.** Never interpolate pull request titles, branch names or issue text directly into shell commands. Pass them through environment variables. Do not run code from forks with secrets or write tokens (avoid `pull_request_target` with checkout of the pull request head).
- **CI configuration has code owners.** Changes to workflows and pipeline includes need review from the platform or security team.
- **Dependency update bots** ([Dependabot](../../templates/github/dependabot.yml) or [Renovate](../../templates/repo/renovate.json)) keep actions, images and packages current.
- **Build once, deploy many.** CI produces one versioned artifact (image or package) per commit. Every environment deploys that same artifact. See [environments](environments.md).

### Assured

- **Provenance.** CI generates signed build provenance for each artifact and signs the artifact. Target SLSA Build L2 at Standard and L3 at Assured. See [supply chain](../security/supply-chain.md).
- **SBOM** in CycloneDX or SPDX for every release artifact.
- **Isolated runners.** Use ephemeral runners that are destroyed after each job. Production deployment jobs run on dedicated runners that untrusted pull request jobs cannot use.
- **Protected environments.** Deployment to production needs approval from someone other than the author and runs only from `main` or a release tag.
- **Pipeline changes are changes.** Treat workflow edits like production changes, with code owner review and a record. This supports ISO/IEC 27001:2022 Annex A 8.32 and 8.25, SOC 2 CC8.1, and NIST SSDF PO.3 (implement supporting toolchains) and PS.1 (protect all forms of code).
- **OpenSSF Scorecard** runs weekly on every repository. Checks such as Pinned-Dependencies, Token-Permissions, Dangerous-Workflow and Branch-Protection map directly to this page.

## In the AI era

- **Evaluation gates run like tests.** A product feature built on a language model has an evaluation set with pass thresholds (see [quality engineering](../quality/quality-engineering.md#in-the-ai-era)). CI runs it on every change to a prompt, model version, retrieval configuration or tool definition, and a failed threshold blocks merge exactly as a failed unit test does. Keep the gating set small enough to fit the 10-minute budget (often 50 to 200 cases) and run the full set nightly.
- **Pin the model.** CI calls a pinned model version, not an alias such as "latest", so a provider update cannot change results between two runs of the same commit. Record the model version in the build output.
- **Control evaluation cost.** Cache model responses keyed on prompt, input and model version for unchanged cases, and set a spending limit per pipeline run.
- **Generated tests are code.** Tests drafted by an assistant go through the same review as any other code. Check that each one fails without the change and asserts the requirement, not whatever the implementation happens to do. See [test-driven development](../quality/test-driven-development.md).
- **Coding agents get the least privilege of all.** An agent that runs in CI or opens pull requests uses a short-lived token scoped to one repository, with `contents: write` and `pull-requests: write` at most, no access to production secrets or deployment environments, and no bypass permission on rulesets. Its pull requests pass the same required checks and human approval as anyone else's. See [code review](code-review.md#in-the-ai-era).
- **Untrusted input reaches agents too.** Issue text, pull request descriptions and file contents can carry prompt injection. Never give an agent that reads untrusted input a token that can merge, release or read secrets.

See [AI engineering practices](../ai/ai-engineering-practices.md), [AI architecture patterns](../ai/ai-architecture-patterns.md) and [code assistants](../people/code-assistants.md).

## Cloud, on-premises and air-gapped

- **Self-hosted runners.** GitHub Enterprise Server, GitLab self-managed, Gitea or Forgejo Actions all support self-hosted runners. Run them as ephemeral containers or VMs, one job each, with no shared workspace between jobs.
- **Never use self-hosted runners for public repositories** that accept pull requests from forks. Anyone could run code on your network.
- **Mirrors for everything.** Actions, CI includes, container images, language packages and toolchains come from internal mirrors (Harbor, Nexus or Artifactory). Mirror third-party actions into an internal organisation and reference them by SHA.
- **Import process.** In air-gapped networks, new or updated dependencies cross the boundary through a reviewed import with malware scanning, checksum or signature checks, and a record of what came in.
- **Caches inside the network.** Run a shared dependency cache close to the runners. Measure cache hit rate; aim for over 80%.
- **Signing.** Use cosign with key pairs held in an internal KMS or HSM when keyless signing cannot reach a public Sigstore instance.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| 40-minute pipelines | Cache, parallelise, shard, move slow suites post-merge. Track duration weekly. |
| `uses: some-org/some-action@main` | Pin to a full SHA with a version comment. |
| Workflow-wide `permissions: write-all` | `contents: read` by default. Grant per job. |
| Cloud admin keys stored as CI secrets | OIDC federation with scoped roles. |
| `run: echo "${{ github.event.pull_request.title }}"` | Pass through `env:` and quote the variable. |
| CI logic that cannot run locally | Put logic in `make` or scripts. CI calls them. |
| Retrying the pipeline until it goes green | Treat flakes as defects. See [testing](testing.md). |
| Artifacts built on a laptop and uploaded | Only CI-built, signed artifacts deploy. |

## Templates

- [GitHub Actions CI workflow](../../templates/github/workflows/ci.yml)
- [Pull request title check](../../templates/github/workflows/pr-title.yml)
- [Dependabot configuration](../../templates/github/dependabot.yml)
- [Renovate configuration](../../templates/repo/renovate.json)
- [GitLab CI pipeline](../../templates/gitlab/.gitlab-ci.yml)
- [Pre-commit hooks](../../templates/repo/.pre-commit-config.yaml)

## Sources

- GitHub, security hardening for GitHub Actions: https://docs.github.com/en/actions/security-guides/security-hardening-for-github-actions
- GitHub, OpenID Connect in Actions: https://docs.github.com/en/actions/deployment/security-hardening-your-deployments/about-security-hardening-with-openid-connect
- GitLab CI/CD YAML reference: https://docs.gitlab.com/ee/ci/yaml/
- SLSA specification: https://slsa.dev/spec/
- OpenSSF Scorecard: https://scorecard.dev
- Reproducible Builds: https://reproducible-builds.org/
- NIST SP 800-218 Secure Software Development Framework: https://csrc.nist.gov/projects/ssdf
- Renovate documentation: https://docs.renovatebot.com/
