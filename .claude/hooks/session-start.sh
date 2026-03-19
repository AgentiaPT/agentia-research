#!/bin/bash
set -euo pipefail

# --- Configure git hooks path (works on all environments) ---
# Use .githooks/ for pre-commit secret scanning (gitleaks + PII detection)
REPO_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")/../.." && pwd)"
git -C "$REPO_DIR" config core.hooksPath .githooks 2>/dev/null || true

# --- Install gitleaks if missing ---
export INSTALL_DIR="${HOME}/.local/bin"
export PATH="${INSTALL_DIR}:${PATH}"
if ! command -v gitleaks &>/dev/null; then
  bash "${REPO_DIR}/scripts/install-gitleaks.sh" || echo "Warning: gitleaks install failed (will retry on first commit)"
fi

# Only run Playwright setup in remote (Claude Code web) environments
if [ "${CLAUDE_CODE_REMOTE:-}" != "true" ]; then
  exit 0
fi

# Install Playwright and browsers
pip install -q playwright || pip3 install -q playwright
playwright install chromium
