#!/usr/bin/env bash
# adopt.sh: copy the Open Engineering Playbook templates into a repository.
#
# Never overwrites a file that already exists in the target: it prints SKIP
# and moves on, so it is safe to run again after the playbook adds new templates.
# It copies whatever files exist under templates/, so new templates need no
# change to this script.
#
#   templates/github/*     -> .github/            (--platform github)
#   templates/gitlab/*     -> .gitlab/            (--platform gitlab)
#                             .gitlab-ci.yml goes to the repository root
#   templates/repo/*       -> repository root
#   templates/docs/*       -> docs/templates/
#   templates/security/*   -> only with --with-security:
#                             workflows/*  -> .github/workflows/  (github)
#                             gitlab-*.yml -> .gitlab/ci/         (gitlab)
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
  --dry-run           print what would be copied, write nothing
  --templates DIR     use another templates folder (default: the one next to
                      this script)
  -h, --help          show this help

Output lines:
  COPY   file copied
  WOULD  file would be copied (dry run)
  SKIP   file already exists in the target, left untouched
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
  printf '%s' "$1"
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

verb="copied"
[ "$dry_run" -eq 0 ] || verb="would be copied"
security="no"
[ "$with_security" -eq 0 ] || security="yes"

printf '\nSummary: %d file(s) %s, %d skipped because they already exist.\n' "$copied" "$verb" "$skipped"
printf 'Platform: %s. Security workflows: %s.\n' "$platform" "$security"
if [ ! -d "${target}/.git" ]; then
  printf 'Note: %s is not the root of a git repository.\n' "$target"
fi
if [ "$copied" -gt 0 ]; then
  printf '\nNext steps:\n'
  printf '  1. Replace the placeholder team names in CODEOWNERS.\n'
  printf '  2. Read each copied file and adjust the numbers to your team.\n'
  if [ "$platform" = "gitlab" ] && [ "$with_security" -eq 1 ]; then
    printf '  3. Add the files under .gitlab/ci/ to the include list in .gitlab-ci.yml.\n'
  fi
  printf '  Review the changes with git status before you commit.\n'
fi
