#!/usr/bin/env bash
# Install gitleaks binary with checksum verification.
# Used by pre-commit hooks and CI scripts.
# Pinned to a specific version with known-good SHA256 checksums.
set -euo pipefail

GITLEAKS_VERSION="8.24.2"
INSTALL_DIR="${INSTALL_DIR:-$HOME/.local/bin}"

# Known-good SHA256 checksums for v8.24.2 (from official GitHub release checksums.txt)
# Verified 2026-03-17. To update: download checksums.txt from the release page.
declare -A CHECKSUMS=(
    ["gitleaks_8.24.2_linux_x64.tar.gz"]="fa0500f6b7e41d28791ebc680f5dd9899cd42b58629218a5f041efa899151a8e"
    ["gitleaks_8.24.2_linux_arm64.tar.gz"]="574a6d52573c61173add7ddb5e3cc68c0e82cb0735818a1eeb9a0a2de1643fbc"
    ["gitleaks_8.24.2_darwin_x64.tar.gz"]="bc3c46f8039ba716ba8461fa6745c9d1cfb90ca2f5f881d8d0cf66b7ba7b742c"
    ["gitleaks_8.24.2_darwin_arm64.tar.gz"]="90d13686937ac7429b97a3acbf1e1d0ce90d92ae2d0cf46a690bd8ae5230bea0"
)

if command -v gitleaks &>/dev/null; then
    INSTALLED="$(gitleaks version 2>/dev/null || echo 'unknown')"
    echo "gitleaks already installed: ${INSTALLED}"
    exit 0
fi

mkdir -p "$INSTALL_DIR"

OS="$(uname -s | tr '[:upper:]' '[:lower:]')"
ARCH="$(uname -m)"

case "$ARCH" in
    x86_64)  ARCH="x64" ;;
    aarch64) ARCH="arm64" ;;
    arm64)   ARCH="arm64" ;;
    *)       echo "ERROR: Unsupported architecture: $ARCH"; exit 1 ;;
esac

TARBALL="gitleaks_${GITLEAKS_VERSION}_${OS}_${ARCH}.tar.gz"
URL="https://github.com/gitleaks/gitleaks/releases/download/v${GITLEAKS_VERSION}/${TARBALL}"

# Verify we have a checksum for this platform
EXPECTED_HASH="${CHECKSUMS[$TARBALL]:-}"
if [ -z "$EXPECTED_HASH" ]; then
    echo "ERROR: No known checksum for ${TARBALL}"
    echo "Supported platforms: ${!CHECKSUMS[*]}"
    exit 1
fi

echo "Installing gitleaks v${GITLEAKS_VERSION} for ${OS}/${ARCH}..."
TMPDIR_DL="$(mktemp -d)"
trap 'rm -rf "$TMPDIR_DL"' EXIT

# Download with retry (up to 3 attempts)
for attempt in 1 2 3; do
    if curl -fsSL --retry 2 "$URL" -o "${TMPDIR_DL}/${TARBALL}"; then
        break
    fi
    if [ "$attempt" -eq 3 ]; then
        echo "ERROR: Failed to download gitleaks after 3 attempts"
        exit 1
    fi
    echo "Retry ${attempt}/3..."
done

# Verify SHA256 checksum
ACTUAL_HASH="$(sha256sum "${TMPDIR_DL}/${TARBALL}" | awk '{print $1}')"
if [ "$ACTUAL_HASH" != "$EXPECTED_HASH" ]; then
    echo "ERROR: Checksum verification FAILED!"
    echo "  Expected: ${EXPECTED_HASH}"
    echo "  Got:      ${ACTUAL_HASH}"
    echo "  File:     ${TARBALL}"
    echo ""
    echo "This could indicate a tampered download or a network issue."
    echo "Do NOT use this binary. Report this to the repository maintainer."
    rm -f "${TMPDIR_DL}/${TARBALL}"
    exit 1
fi
echo "Checksum verified: ${ACTUAL_HASH}"

# Extract and install
tar -xzf "${TMPDIR_DL}/${TARBALL}" -C "$TMPDIR_DL"
mv "${TMPDIR_DL}/gitleaks" "${INSTALL_DIR}/gitleaks"
chmod +x "${INSTALL_DIR}/gitleaks" 2>/dev/null || true  # chmod may fail on drvfs (already rwx)

# Verify the binary runs
if "${INSTALL_DIR}/gitleaks" version &>/dev/null; then
    echo "gitleaks v${GITLEAKS_VERSION} installed successfully to ${INSTALL_DIR}/gitleaks"
else
    echo "ERROR: Installed binary failed to execute"
    rm -f "${INSTALL_DIR}/gitleaks"
    exit 1
fi

# Ensure install dir is on PATH
if ! echo "$PATH" | grep -q "$INSTALL_DIR"; then
    echo "NOTE: Add ${INSTALL_DIR} to your PATH"
fi
