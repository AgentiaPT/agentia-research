#!/usr/bin/env bash
# Claude Code PreToolUse hook — blocks git push commands.
#
# This runs BEFORE the Bash tool executes. If the command contains
# "git push", it exits non-zero to block execution and prints a
# warning the agent will see in its tool output.
#
# The agent can only push by setting ALLOW_PUSH=1 in the command,
# which it should only do when the user has explicitly said "push".

set -euo pipefail

# Read the tool input from stdin
INPUT="$(cat)"

# Extract the command being run
COMMAND="$(echo "$INPUT" | jq -r '.tool_input.command // empty' 2>/dev/null)"

# Only care about commands that contain "git push"
if echo "$COMMAND" | grep -qE '\bgit\s+push\b'; then
  # Allow if ALLOW_PUSH=1 is part of the command
  if echo "$COMMAND" | grep -qE 'ALLOW_PUSH=1'; then
    exit 0
  fi

  echo ""
  echo "⛔ BLOCKED: git push is not allowed without explicit user permission."
  echo ""
  echo "CLAUDE.md says: NEVER run git push unless the user explicitly asked."
  echo "Completing a task is NOT permission to push."
  echo "'Commit your work' is NOT permission to push."
  echo ""
  echo "If the user said 'push', 'push it', or 'send it', use:"
  echo "  ALLOW_PUSH=1 git push -u origin <branch>"
  echo ""
  exit 2
fi

exit 0
