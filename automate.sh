#!/usr/bin/env bash
set -Eeuo pipefail

echo "Starting safe Supreme Omni Engine sync..."
if ! git rev-parse --is-inside-work-tree >/dev/null 2>&1; then
  echo "Error: run this script from inside the repository." >&2
  exit 1
fi
current_branch="$(git branch --show-current)"
if [[ "$current_branch" != "main" ]]; then
  echo "Error: refusing to push from '$current_branch'. Switch to main first." >&2
  exit 1
fi

git add -A
if ! git diff --cached --quiet; then
  git commit -m "chore: sync repository ($(date -u +%Y-%m-%dT%H:%M:%SZ))"
fi
# A normal push rejects non-fast-forward updates. Never rewrite remote history.
git push origin HEAD:main
echo "GitHub sync completed with a non-force push."
if [[ -n "${RENDER_DEPLOY_HOOK:-}" ]]; then
  echo "Triggering Render deployment..."
  curl --fail --silent --show-error --request POST "$RENDER_DEPLOY_HOOK"
  echo
echo "Render deployment hook accepted the request."
else
  echo "RENDER_DEPLOY_HOOK is not set; deployment was not triggered."
fi
