#!/usr/bin/env bash
# adopt.sh: copy the Open Engineering Playbook templates into a repository.
#
# Never overwrites a file that already exists in the target: it prints SKIP
# and moves on, so it is safe to run again after the playbook adds new templates.
# It copies whatever files exist under templates/, so new templates need no
# change to this script.
#
#   templates/github/*     -> .github/            (--platform github)
#                             release-please files go to the repository root
#                             rulesets/*.json -> docs/repository-rules/
#                             (GitHub does not read rulesets from files;
#                             the script prints the command to import it)
#   templates/gitlab/*     -> .gitlab/            (--platform gitlab)
#                             .gitlab-ci.yml goes to the repository root
#   templates/repo/*       -> repository root
#   templates/docs/*       -> docs/templates/
#   templates/security/*   -> only with --with-security:
#                             workflows/*  -> .github/workflows/  (github)
#                             gitlab-*.yml -> .gitlab/ci/         (gitlab)
#   tools/plain_lint.py and tools/plain-language.txt -> tools/
#                             (the pre-commit hook in .pre-commit-config.yaml
#                             runs them)
#
# Only one ruleset is copied: the team ruleset (one approving review), or the
# solo ruleset with --solo. Only one dependency update bot is copied:
# Dependabot (default on GitHub) or Renovate (default on GitLab).
#
# Works with bash 3.2 (macOS) and later. No network access.

set -euo pipefail

usage() {
  cat <<'EOF'
Usage: tools/adopt.sh --target DIR --platform github|gitlab [options]

Copy the playbook templates into the repository at DIR. Existing files are kept.

Options:
  --target DIR        repository to copy into (must already exist)
  --platform NAME     github or gitlab
  --with-security     also copy the supply chain workflows (SBOM, signing,
                      OpenSSF Scorecard)
  --solo              GitHub only: copy the solo ruleset, which lets the
                      owner merge their own pull request once checks pass
  --updates NAME      dependabot or renovate: the one update bot to copy
                      (default: dependabot on GitHub, renovate on GitLab)
  --dry-run           print what would be copied, write nothing
  --templates DIR     use another templates folder (default: the one next to
                      this script)
  -h, --help          show this help

Output lines:
  COPY   file copied
  WOULD  file would be copied (dry run)
  SKIP   file already exists in the target, left untouched
  NOTE   something to know, nothing copied
EOF
}

die() {
  printf 'adopt: %s\n' "$1" >&2
  printf 'Run with --help for usage.\n' >&2
  exit 2
}

script_dir=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
templates="${script_dir}/../templates"
target=""
platform=""
with_security=0
dry_run=0
solo=0
updates=""

while [ $# -gt 0 ]; do
  case "$1" in
    --target)
      [ $# -ge 2 ] || die "--target needs a directory"
      target="$2"; shift 2 ;;
    --target=*)
      target="${1#*=}"; shift ;;
    --platform)
      [ $# -ge 2 ] || die "--platform needs github or gitlab"
      platform="$2"; shift 2 ;;
    --platform=*)
      platform="${1#*=}"; shift ;;
    --templates)
      [ $# -ge 2 ] || die "--templates needs a directory"
      templates="$2"; shift 2 ;;
    --templates=*)
      templates="${1#*=}"; shift ;;
    --with-security)
      with_security=1; shift ;;
    --solo)
      solo=1; shift ;;
    --updates)
      [ $# -ge 2 ] || die "--updates needs dependabot or renovate"
      updates="$2"; shift 2 ;;
    --updates=*)
      updates="${1#*=}"; shift ;;
    --dry-run)
      dry_run=1; shift ;;
    -h|--help)
      usage; exit 0 ;;
    *)
      die "unknown option: $1" ;;
  esac
done

[ -n "$target" ] || die "--target is required"
[ -n "$platform" ] || die "--platform is required"
case "$platform" in
  github|gitlab) ;;
  *) die "--platform must be github or gitlab, not '$platform'" ;;
esac
if [ -z "$updates" ]; then
  if [ "$platform" = "github" ]; then updates="dependabot"; else updates="renovate"; fi
fi
case "$platform:$updates" in
  github:dependabot|github:renovate|gitlab:renovate) ;;
  gitlab:dependabot) die "Dependabot does not run on GitLab. Use --updates renovate." ;;
  *) die "--updates must be dependabot or renovate, not '$updates'" ;;
esac
if [ "$solo" -eq 1 ] && [ "$platform" != "github" ]; then
  die "--solo applies to GitHub rulesets only. On GitLab, set approvals to 0 in the protected branch settings."
fi
[ -d "$target" ] || die "target directory does not exist: $target"
[ -d "$templates" ] || die "templates directory not found: $templates"

target=$(cd "$target" && pwd)
templates=$(cd "$templates" && pwd)

copied=0
skipped=0

# Each map_* function takes a path relative to its template folder and prints
# the destination relative to the target. Printing nothing means "not used".
map_github() {
  case "$1" in
    # release-please reads these from the repository root by default.
    release-please-config.json|.release-please-manifest.json) printf '%s' "$1" ;;
    # GitHub does not read rulesets from the repository. Keep the reviewed
    # copy under docs/ and import it with the command printed at the end.
    rulesets/default-branch.json)
      [ "$solo" -eq 1 ] || printf 'docs/repository-rules/default-branch.json' ;;
    rulesets/default-branch-solo.json)
      [ "$solo" -eq 0 ] || printf 'docs/repository-rules/default-branch-solo.json' ;;
    rulesets/*) ;;
    dependabot.yml)
      [ "$updates" != "dependabot" ] || printf '.github/dependabot.yml' ;;
    *) printf '.github/%s' "$1" ;;
  esac
}

map_gitlab() {
  case "$1" in
    .gitlab-ci.yml) printf '.gitlab-ci.yml' ;;
    *) printf '.gitlab/%s' "$1" ;;
  esac
}

map_repo() {
  case "$1" in
    renovate.json) [ "$updates" != "renovate" ] || printf 'renovate.json' ;;
    *) printf '%s' "$1" ;;
  esac
}

map_docs() {
  printf 'docs/templates/%s' "$1"
}

map_security() {
  case "$platform:$1" in
    github:workflows/*) printf '.github/%s' "$1" ;;
    gitlab:gitlab-*) printf '.gitlab/ci/%s' "$1" ;;
    *) ;;
  esac
}

copy_one() {
  local src="$1" rel="$2"
  local dest="${target}/${rel}"
  if [ -e "$dest" ] || [ -L "$dest" ]; then
    printf 'SKIP   %s (already exists)\n' "$rel"
    skipped=$((skipped + 1))
    return 0
  fi
  if [ "$dry_run" -eq 1 ]; then
    printf 'WOULD  %s\n' "$rel"
  else
    mkdir -p "$(dirname "$dest")"
    cp "$src" "$dest"
    printf 'COPY   %s\n' "$rel"
  fi
  copied=$((copied + 1))
}

# copy_tree NAME MAPPER: copy every file under templates/NAME through MAPPER.
copy_tree() {
  local name="$1" mapper="$2"
  local dir="${templates}/${name}"
  local file rel dest
  if [ ! -d "$dir" ]; then
    printf 'NOTE   templates/%s not found, nothing to copy from it\n' "$name"
    return 0
  fi
  while IFS= read -r -d '' file; do
    rel="${file#"${dir}"/}"
    dest=$("$mapper" "$rel")
    [ -n "$dest" ] || continue
    copy_one "$file" "$dest"
  done < <(find "$dir" -type f ! -name '.DS_Store' ! -name '.gitkeep' -print0 | sort -z)
}

if [ "$dry_run" -eq 1 ]; then
  printf 'Dry run: nothing will be written.\n'
fi
printf 'Copying playbook templates into %s (%s)\n\n' "$target" "$platform"

copy_tree "$platform" "map_${platform}"
copy_tree repo map_repo
copy_tree docs map_docs
if [ "$with_security" -eq 1 ]; then
  copy_tree security map_security
fi
# The plain-language pre-commit hook needs these two files.
for tool in plain_lint.py plain-language.txt; do
  if [ -f "${script_dir}/${tool}" ]; then
    copy_one "${script_dir}/${tool}" "tools/${tool}"
  fi
done

# Work out OWNER/REPO for the ruleset command from the origin remote, if any.
repo_slug="OWNER/REPO"
if [ -d "${target}/.git" ] && command -v git >/dev/null 2>&1; then
  origin=$(git -C "$target" remote get-url origin 2>/dev/null || true)
  case "$origin" in
    *github.com[:/]*)
      slug="${origin#*github.com[:/]}"
      slug="${slug%.git}"
      case "$slug" in
        */*) repo_slug="$slug" ;;
      esac
      ;;
  esac
fi
ruleset_file="docs/repository-rules/default-branch.json"
[ "$solo" -eq 0 ] || ruleset_file="docs/repository-rules/default-branch-solo.json"

verb="copied"
[ "$dry_run" -eq 0 ] || verb="would be copied"
security="no"
[ "$with_security" -eq 0 ] || security="yes"

printf '\nSummary: %d file(s) %s, %d skipped because they already exist.\n' "$copied" "$verb" "$skipped"
printf 'Platform: %s. Security workflows: %s. Update bot: %s.\n' "$platform" "$security" "$updates"
if [ ! -d "${target}/.git" ]; then
  printf 'Note: %s is not the root of a git repository.\n' "$target"
fi
if [ "$copied" -gt 0 ]; then
  printf '\nNext steps:\n'
  step=1
  printf '  %d. Replace the placeholder team names in CODEOWNERS.\n' "$step"; step=$((step + 1))
  printf '  %d. Read each copied file and adjust the numbers to your team.\n' "$step"; step=$((step + 1))
  if [ "$platform" = "github" ]; then
    printf '  %d. Branch protection is NOT on yet. GitHub does not read rulesets from\n' "$step"
    printf '     files. Import it once, from the repository root:\n'
    printf '       gh api -X POST repos/%s/rulesets --input %s\n' "$repo_slug" "$ruleset_file"
    printf '     or Settings > Rules > Rulesets > New ruleset > Import a ruleset.\n'
    printf '     Rulesets work on public repositories on every plan, and on private\n'
    printf '     repositories only with GitHub Pro, Team or Enterprise.\n'
    if [ "$solo" -eq 1 ]; then
      printf '     The solo ruleset needs no second reviewer. When a second engineer\n'
      printf '     joins, rerun without --solo, import the team ruleset and delete\n'
      printf '     the solo one in Settings > Rules > Rulesets.\n'
    else
      printf '     The team ruleset needs a second person to approve. Working alone?\n'
      printf '     Rerun with --solo for the solo ruleset.\n'
    fi
    step=$((step + 1))
    printf '  %d. Release pull requests need a GitHub App token so CI runs on them.\n' "$step"
    printf '     Set-up steps are at the top of .github/workflows/release-please.yml.\n'
    step=$((step + 1))
  fi
  printf '  %d. Use one dependency update bot (%s). If the repository already has\n' "$step" "$updates"
  printf '     the other one configured, delete its file.\n'
  step=$((step + 1))
  if [ "$platform" = "gitlab" ] && [ "$with_security" -eq 1 ]; then
    printf '  %d. Add the files under .gitlab/ci/ to the include list in .gitlab-ci.yml.\n' "$step"
  fi
  printf '  Review the changes with git status before you commit.\n'
fi
