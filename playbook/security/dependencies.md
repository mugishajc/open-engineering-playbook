# Dependencies

Pin every dependency, commit the lockfile, let a bot open update pull requests every week, and fix vulnerable dependencies within agreed times. Most of the code you ship was written by someone else. Teams that update in small steps every week spend minutes per update; teams that wait a year spend weeks on one painful upgrade, usually in the middle of a security emergency.

## Outcomes

Starting points. Tune them to your stack.

- 100% of repositories commit a lockfile and use Renovate or Dependabot.
- At least 80% of patch and minor update pull requests merge within 7 days of opening.
- No production service runs a framework or runtime version past its end of support.
- Vulnerable dependencies are fixed within the SLAs in [vulnerability management](vulnerability-management.md) in at least 90% of cases.
- 100% of dependencies have a licence on the allow list or an approved exception.
- In on-premises and air-gapped networks, 100% of builds fetch packages only from the internal mirror.

## Practice

### Foundation

1. **Commit the lockfile** (`package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, `uv.lock`, `go.sum`, `Cargo.lock`, `Gemfile.lock`) and install from it in CI (`npm ci`, not `npm install`).
2. **Pin everything else** too: container base images by digest, CI actions by commit SHA, tool versions in a version file.
3. **Turn on an update bot.** Renovate or Dependabot, weekly, with patch and minor updates grouped into one pull request per ecosystem (see [Renovate configuration](../../templates/repo/renovate.json) and [Dependabot configuration](../../templates/github/dependabot.yml)).
4. **Tests decide.** If CI passes, merge the update. If you do not trust your tests to decide, fix the tests (see [testing](../delivery/testing.md)).
5. **Dependency scanning** in CI on every pull request.

### Standard

1. **Update SLAs** for routine updates (starting points):

   | Update type | Merge within |
   |---|---|
   | Patch and minor | 7 days |
   | Major version of a direct dependency | 90 days, or a tracked decision to stay |
   | Runtime and framework (language version, web framework) | Before end of support, with at least 3 months' margin |
   | Security fix | See [vulnerability management](vulnerability-management.md) |

2. **Wait a few days before adopting brand-new releases.** Malicious versions are often caught and removed within days. A minimum release age of 3 days (Renovate's `minimumReleaseAge`) is a starting point. Security fixes bypass the wait.
3. **Criteria for adding a new dependency.** Before adding, check: is it maintained (release in the last 12 months, more than one maintainer)? What is its OpenSSF Scorecard score? How many transitive dependencies does it bring? Is the licence allowed? Could 50 lines of your own code replace it? Record the answer in the pull request.
4. **Licence policy** using SPDX identifiers. An example to adapt with your legal team:

   | Category | Examples | Rule |
   |---|---|---|
   | Allow | MIT, Apache-2.0, BSD-2-Clause, BSD-3-Clause, ISC | Use freely |
   | Review | MPL-2.0, LGPL-2.1, LGPL-3.0, EPL-2.0 | Allowed with conditions on how you link and distribute |
   | Deny unless approved | GPL-2.0, GPL-3.0, AGPL-3.0, SSPL-1.0, no licence | Legal review for distributed or network-served products |

   The right policy depends on whether you distribute software, run it as a service or use it internally. This table is not legal advice.
5. **Dependency confusion and typosquatting.** Use scoped or namespaced package names for internal packages, configure package managers to fetch internal names only from your registry, and reserve your internal names on public registries.
6. **Ownership.** Each repository's update pull requests go to its owning team via CODEOWNERS. Unowned repositories are archived.

### Assured

Everything in Standard, plus:

1. **Approved component list** for Tier 1 systems, with each new direct dependency approved by a second reviewer.
2. **SBOM per release** (see [supply chain](supply-chain.md)) as the record of what was shipped.
3. **Evidence** of update times, exceptions and licence decisions kept for the audit period. This supports ISO/IEC 27001:2022 controls 8.8 (management of technical vulnerabilities) and 8.30 (outsourced development), and SSDF practice PW.4 (reuse well-secured software).
4. **End-of-life tracking.** A register of runtimes, frameworks and operating systems with support end dates, reviewed quarterly, with funded upgrade plans 6 months before each date.

## Cloud, on-premises and air-gapped

- **Internal mirror for everything.** Run a proxy registry (Nexus, Artifactory, Harbor for images, or a language-specific mirror) and point every build at it. This speeds builds, survives public registry outages and gives you one place to block a malicious package.
- **Quarantine new versions.** In air-gapped networks, new package versions pass a scan and the minimum release age on the connected side before transfer.
- **Update bots offline.** Renovate runs self-hosted against GitLab, Gitea, Forgejo, Bitbucket Data Center and GitHub Enterprise Server, and can read from your internal mirror.
- **Transfer cadence.** Import updates at least weekly. Monthly or slower imports make the security SLAs impossible to meet.

## Anti-patterns

| Anti-pattern | Fix |
|---|---|
| Version ranges without a lockfile | Commit the lockfile; install from it in CI. |
| Update bot pull requests pile up unread | Group updates, auto-merge patches with green CI, and track merge time. |
| One big upgrade every two years | Weekly small updates. |
| A 200-dependency package added for one helper function | Check the criteria before adding. |
| Builds pull directly from public registries in production CI | Internal mirror only. |
| Licence questions answered after the product ships | Licence check in CI on every pull request. |

## Templates

- [Renovate configuration](../../templates/repo/renovate.json)
- [Dependabot configuration](../../templates/github/dependabot.yml)
- [CODEOWNERS](../../templates/github/CODEOWNERS)

## Sources

- Renovate documentation, configuration options: https://docs.renovatebot.com/configuration-options/
- GitHub Docs, Dependabot: https://docs.github.com/en/code-security/dependabot
- SPDX License List: https://spdx.org/licenses/
- OpenSSF Scorecard: https://scorecard.dev
- NIST SP 800-218 (SSDF), practice PW.4: https://csrc.nist.gov/pubs/sp/800/218/final
