#!/usr/bin/env bash
# Claude Code pre-commit hook — scans staged files for secrets & PII.
# Registered in .claude/settings.json as a PreCommit hook.
# Auto-installs gitleaks if not present.
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/../.." && pwd)"

exec "${REPO_DIR}/scripts/scan-secrets.sh" --staged
