# Versioning and changelogs

Version anything other people depend on with Semantic Versioning 2.0.0, write commit messages in Conventional Commits 1.0.0, and generate a changelog in Keep a Changelog 1.1.0 style from those commits. A version number is a promise about compatibility; the changelog is how users check it. Remove nothing from a public interface without a deprecation period.

## Outcomes

| Signal | Starting target |
|---|---|
| Releases with a changelog entry | 100% |
| Squash commits on `main` that follow Conventional Commits | 100%, enforced by the pull request title check |
| Breaking changes shipped in a minor or patch release | Zero |
| Deprecations announced before removal | 100%, with at least one minor release and 6 months of notice |
| Time from merge to a published release (libraries) | Under 1 week |

## Choosing a scheme

| Scheme | Format | Use when |
|---|---|---|
| Semantic Versioning 2.0.0 | `MAJOR.MINOR.PATCH`, for example `2.4.1` | Libraries, SDKs, APIs, CLIs, anything with a compatibility promise |
| Calendar Versioning | For example `2026.11.0` or `26.11` | Products released on a schedule where compatibility is not the main message: operating system images, on-premises suites, data sets |
| Build or commit identifier | Commit SHA or build number | Internal services deployed continuously and never consumed as a dependency |

SemVer rules in short:

- `MAJOR` when you make an incompatible change to the public interface.
- `MINOR` when you add backward-compatible functionality, including deprecations.
- `PATCH` for backward-compatible bug fixes.
- `0.y.z` is for initial development: anything may change. Move to `1.0.0` when others depend on you in production.
- Pre-releases use a hyphen: `1.4.0-rc.1`. Build metadata uses a plus sign and does not affect precedence: `1.4.0+build.512`.
- Define your public interface in writing (API, CLI flags, config file format, database schema if customers touch it). SemVer means nothing without it.

## Conventional Commits

Format: `type(optional scope)!: description`, then optional body and footers.

| Type | Effect on version | Example |
|---|---|---|
| `feat` | Minor | `feat(export): add CSV export for invoices` |
| `fix` | Patch | `fix(auth): reject expired refresh tokens` |
| `feat!` or footer `BREAKING CHANGE:` | Major | `feat(api)!: remove v1 orders endpoint` |
| `docs`, `test`, `refactor`, `perf`, `build`, `ci`, `chore`, `style`, `revert` | None by default | `ci: pin checkout action to SHA` |

With squash merge, only the pull request title must follow the format. The [pr-title workflow](../../templates/github/workflows/pr-title.yml) checks it.

## Practice

### Foundation

- Pick a scheme from the table and write it in the README.
- Squash merge with Conventional Commit titles. See [source control](source-control.md).
- Keep a `CHANGELOG.md` in [Keep a Changelog](../../templates/repo/CHANGELOG.md) form: newest first, one section per version with a date, entries grouped as Added, Changed, Deprecated, Removed, Fixed, Security. Keep an `Unreleased` section at the top if you edit by hand.
- Tag every release in Git: `v1.4.0`.
- Write changelog entries for humans: what changed for the user, not which file moved.

### Standard

- **Automate with release-please.** On every push to `main`, release-please opens or updates a release pull request that bumps the version and the changelog from Conventional Commits. Merging that pull request creates the tag and the GitHub release. Templates: [workflow](../../templates/github/workflows/release-please.yml), [config](../../templates/github/release-please-config.json), [manifest](../../templates/github/.release-please-manifest.json).
- **Monorepos.** Version each package separately with release-please manifest mode, unless packages always release together.
- **Breaking-change checks in CI** for published interfaces: API schema diff (OpenAPI, Protobuf), public symbol diff for libraries. A breaking change without `!` fails CI.
- **Deprecation policy.**
  1. Mark the feature deprecated in code, docs and the changelog `Deprecated` section, in a minor release.
  2. Emit a runtime warning or response header (for HTTP APIs, the `Deprecation` and `Sunset` headers) that names the replacement and the removal date.
  3. Keep the deprecated feature for at least one further minor release and at least 6 months (12 months for public-sector and regulated customers, as a starting point).
  4. Remove it only in the next major release, listed under `Removed`.
  5. Measure use of the deprecated feature before removal. If use is still high, extend and contact users.
- See [API standards](../architecture/api-standards.md) for API versioning.

### Assured

- Each release links the version to the commit SHA, the artifact digest, the SBOM and the provenance attestation.
- Changelog `Security` entries reference the CVE or advisory ID and the affected versions.
- Publish security advisories in a machine-readable format (CSAF 2.0 or OpenVEX) alongside the changelog for software customers install. See [vulnerability management](../security/vulnerability-management.md).
- Keep released versions immutable. Never re-tag or re-upload a version; publish a new patch.

## Cloud, on-premises and air-gapped

- release-please works with GitHub and GitHub Enterprise Server. It runs as an Action or as a CLI from an internal npm mirror on air-gapped runners.
- On GitLab, use GitLab's changelog API (driven by `Changelog:` commit trailers) or another Conventional Commits release tool such as semantic-release. The `release` stage in [`.gitlab-ci.yml`](../../templates/gitlab/.gitlab-ci.yml) creates a release from a tag and its changelog section.
- Ship the changelog inside offline bundles, so administrators in air-gapped sites can read it before they upgrade.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| "Bump the major to look important" | The version is a compatibility promise, not marketing. |
| A breaking change in a patch release | CI breaking-change check. Conventional Commits `!`. |
| Changelog that is a raw `git log` | Group by type, write for users, edit the release pull request. |
| Staying on `0.x` for years while customers run it in production | Release `1.0.0` and start keeping promises. |
| Removing a deprecated endpoint with no warning period | Follow the deprecation steps above. |
| Re-publishing a version with different content | Versions are immutable. Release a patch. |

## Templates

- [CHANGELOG.md](../../templates/repo/CHANGELOG.md)
- [release-please workflow](../../templates/github/workflows/release-please.yml)
- [release-please config](../../templates/github/release-please-config.json) and [manifest](../../templates/github/.release-please-manifest.json)
- [Pull request title check](../../templates/github/workflows/pr-title.yml)

## Sources

- Semantic Versioning 2.0.0: https://semver.org/spec/v2.0.0.html
- Conventional Commits 1.0.0: https://www.conventionalcommits.org/en/v1.0.0/
- Keep a Changelog 1.1.0: https://keepachangelog.com/en/1.1.0/
- Calendar Versioning: https://calver.org/
- release-please: https://github.com/googleapis/release-please
- release-please action: https://github.com/googleapis/release-please-action
- IETF RFC 8594, the Sunset HTTP header field: https://www.rfc-editor.org/rfc/rfc8594
- IETF RFC 9745, the Deprecation HTTP response header field: https://www.rfc-editor.org/rfc/rfc9745
- GitLab, changelogs: https://docs.gitlab.com/ee/user/project/changelogs.html
