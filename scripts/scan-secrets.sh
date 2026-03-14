#!/usr/bin/env bash
# Scan staged files (or full repo) for secrets and PII.
# Usage:
#   ./scripts/scan-secrets.sh              # scan staged changes (pre-commit mode)
#   ./scripts/scan-secrets.sh --full       # scan entire repo
#   ./scripts/scan-secrets.sh --diff HEAD  # scan specific diff
set -uo pipefail  # no -e: we handle exit codes manually

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
REPO_DIR="$(cd "$SCRIPT_DIR/.." && pwd)"
CONFIG="${REPO_DIR}/.gitleaks.toml"

# Auto-install gitleaks if missing
export INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"
export PATH="${INSTALL_DIR}:${PATH}"

if ! command -v gitleaks &>/dev/null; then
    echo "gitleaks not found, installing..."
    if ! bash "${SCRIPT_DIR}/install-gitleaks.sh"; then
        echo "ERROR: Failed to install gitleaks. Commit blocked for safety."
        exit 1
    fi
fi

MODE="${1:---staged}"
EXIT_CODE=0

case "$MODE" in
    --staged)
        echo "Scanning staged changes for secrets & PII..."
        gitleaks protect --staged --config "$CONFIG" --redact --verbose || EXIT_CODE=$?
        ;;
    --full)
        echo "Scanning full repository for secrets & PII..."
        gitleaks detect --source "$REPO_DIR" --config "$CONFIG" --redact --verbose || EXIT_CODE=$?
        ;;
    --diff)
        REF="${2:-HEAD}"
        echo "Scanning diff against ${REF} for secrets & PII..."
        gitleaks detect --source "$REPO_DIR" --config "$CONFIG" --redact --verbose --log-opts="${REF}" || EXIT_CODE=$?
        ;;
    *)
        echo "Usage: $0 [--staged|--full|--diff <ref>]"
        exit 1
        ;;
esac

if [ $EXIT_CODE -eq 0 ]; then
    echo "No secrets or PII detected."
else
    echo ""
    echo "=========================================="
    echo "BLOCKED: Secrets or PII detected!"
    echo "=========================================="
    echo ""
    echo "Options:"
    echo "  1. Remove the sensitive data and re-stage"
    echo "  2. Add an allowlist entry to .gitleaks.toml (if false positive)"
    echo "  3. SKIP=gitleaks git commit -m '...' (escape hatch, use sparingly)"
fi
exit $EXIT_CODE
