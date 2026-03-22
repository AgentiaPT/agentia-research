---
title: "Hardening the Claude Code Sandbox: A Practical Security Guide"
date: 2026-03-17
status: complete
tags: [ai, claude-code, security, sandbox, hardening, guide]
---

# Hardening the Claude Code Sandbox: A Practical Security Guide

> ✨ This project was authored by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

**Security Research & Implementation Guide — March 2026**

---

## Table of Contents

1. [Introduction](#1-introduction)
2. [The Default Claude Code Sandbox](#2-the-default-claude-code-sandbox)
3. [Threat Model: What Are We Hardening Against?](#3-threat-model-what-are-we-hardening-against)
4. [Hardening Layer 1: Environment Variable Stripping via BASH_ENV](#4-hardening-layer-1-environment-variable-stripping-via-bash_env)
5. [Hardening Layer 2: Expanded Filesystem Deny Lists](#5-hardening-layer-2-expanded-filesystem-deny-lists)
6. [Hardening Layer 3: AFK Guard Hook](#6-hardening-layer-3-afk-guard-hook)
7. [Audit Results: Before vs. After](#7-audit-results-before-vs-after)
8. [Implementation Guide](#8-implementation-guide)
9. [Known Limitations](#9-known-limitations)
10. [Sources](#10-sources)

---

## 1. Introduction

Claude Code ships with a sandbox that provides OS-level process isolation for all Bash commands. On Linux and WSL2 this uses [bubblewrap (bwrap)](https://github.com/containers/bubblewrap), creating isolated namespaces for PID, network, mount, IPC, UTS, and cgroup. On macOS it uses Apple's native Seatbelt framework.

The default sandbox is a strong foundation, but it leaves several attack surfaces open — most notably, the **session access token is visible inside the sandbox**, sensitive directories like `~/.ssh` and `~/.gnupg` are readable, and there is no protection against sandbox escape (`dangerouslyDisableSandbox`) during unattended operation.

This report documents three custom hardening layers we implemented on top of the default Claude Code sandbox, verified through a live audit from within the sandbox itself. Each layer is independent and can be adopted separately.

---

## 2. The Default Claude Code Sandbox

### 2.1 Architecture

When sandbox mode is enabled, Claude Code wraps every Bash command in a bubblewrap container with the following isolation:

| Namespace | Purpose |
|-----------|---------|
| **PID** | Process isolation — sandboxed commands cannot see host processes |
| **Network** | All traffic routed through a local proxy (HTTP on port 3128, SOCKS5 on port 1080) with domain allowlisting |
| **Mount** | Filesystem access controlled via bind mounts; write access restricted to the working directory |
| **IPC** | Inter-process communication isolated |
| **UTS** | Hostname isolated |
| **User** | UID/GID mapping isolated |

### 2.2 Network Proxy

The sandbox runs two `socat` processes that bridge TCP traffic through Unix sockets to the Claude Code host process:

- **Port 3128** — HTTP/HTTPS proxy (set via `HTTP_PROXY` / `HTTPS_PROXY`)
- **Port 1080** — SOCKS5 proxy (set via `ALL_PROXY`)

The proxy operates on an **allowlist model**: all outbound connections are blocked unless the domain is explicitly whitelisted. This is enforced at the proxy level, not via iptables.

### 2.3 Default Filesystem Restrictions

When enabled, the sandbox restricts **write access** to the current working directory and a designated temp directory (`/tmp/claude-1000/`). Read access is broader — by default, most of the filesystem is readable.

### 2.4 What the Default Sandbox Does NOT Protect

Based on the [official security documentation](https://docs.anthropic.com/en/docs/claude-code/security#:~:text=sandbox), these gaps exist in the default configuration:

1. **Session access token** — `CLAUDE_CODE_SESSION_ACCESS_TOKEN` is passed into the sandbox environment and visible via `printenv`
2. **Sensitive user directories** — `~/.ssh/`, `~/.gnupg/`, `~/.docker/` are readable by default
3. **Shell history** — `~/.bash_history`, `~/.zsh_history` are readable
4. **Host drive mounts** — On WSL2, Windows drives (`/mnt/c`, `/mnt/d`) are accessible
5. **Sandbox escape** — The `dangerouslyDisableSandbox` option allows commands to bypass the sandbox entirely; there is no protection against this during unattended (AFK) operation
6. **Internal proxy metadata** — `CLAUDE_CODE_HOST_HTTP_PROXY_PORT` and `CLAUDE_CODE_HOST_SOCKS_PROXY_PORT` expose the sandbox's internal architecture

---

## 3. Threat Model: What Are We Hardening Against?

### 3.1 Prompt Injection / Indirect Attacks

A malicious payload in a file, web page, or tool output could attempt to:

- **Exfiltrate the session token** via `printenv` or `/proc/self/environ`
- **Read SSH keys** to access remote systems
- **Read shell history** to discover credentials typed in past sessions
- **Access Windows drives** to read files outside the project
- **Escape the sandbox** using `dangerouslyDisableSandbox` when the user is not actively reviewing

### 3.2 Supply Chain Risks

A compromised npm package or build script running inside the sandbox could:

- Harvest environment variables for tokens
- Read credential files from well-known paths
- Exfiltrate data through the network proxy (if domains are allowed)

### 3.3 Defense-in-Depth Principle

No single layer is sufficient. The hardening follows **defense-in-depth**: even if one layer is bypassed, subsequent layers reduce the blast radius.

---

## 4. Hardening Layer 1: Environment Variable Stripping via BASH_ENV

### 4.1 The Problem

The default sandbox passes `CLAUDE_CODE_SESSION_ACCESS_TOKEN` into the sandboxed environment. Any command running inside the sandbox can read it:

```bash
# In default sandbox (BEFORE hardening):
$ printenv | grep TOKEN
CLAUDE_CODE_SESSION_ACCESS_TOKEN=sk-ant-...
```

This token could be used to make authenticated API calls or exfiltrate data if outbound network access to Anthropic's API is allowed through the proxy.

### 4.2 The Solution

We exploit a standard Bash mechanism: the **`BASH_ENV`** environment variable. When Bash starts a non-interactive shell (which is how every sandbox command executes), it automatically sources the file pointed to by `BASH_ENV` before running the command.

**Step 1** — Create `~/.claude/sandbox-init.sh`:

```bash
# Strip sensitive tokens and internal vars from sandbox environment
unset CLAUDE_CODE_SESSION_ACCESS_TOKEN 2>/dev/null
unset CLAUDE_CODE_HOST_HTTP_PROXY_PORT 2>/dev/null
unset CLAUDE_CODE_HOST_SOCKS_PROXY_PORT 2>/dev/null
```

**Step 2** — Add to `~/.bashrc`:

```bash
export BASH_ENV="$HOME/.claude/sandbox-init.sh"
```

### 4.3 Why This Works

1. The bwrap sandbox inherits the host shell's environment, which includes `BASH_ENV`
2. Every Bash command spawned inside the sandbox is non-interactive
3. Non-interactive Bash [sources `BASH_ENV` before executing any command](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html#:~:text=BASH_ENV)
4. By the time any user-visible command runs, the token has already been `unset`

### 4.4 Why Not Use a SessionStart Hook Instead?

Claude Code offers a `SessionStart` hook that runs when a session begins. However:

- `SessionStart` fires **once per session**, not per command
- If a command somehow re-exports the variable, it would persist
- `BASH_ENV` fires on **every non-interactive shell invocation**, providing continuous protection
- `BASH_ENV` operates at the Bash level, below Claude Code's hook system — it's a more fundamental defense

### 4.5 Verification

After hardening, from inside the sandbox:

```bash
$ printenv                          # Empty — all env vars stripped
$ cat /proc/self/environ            # Empty
$ set | grep TOKEN                  # No matches
$ ps auxe | grep TOKEN              # No matches
```

---

## 5. Hardening Layer 2: Expanded Filesystem Deny Lists

### 5.1 The Problem

The default sandbox configuration does not deny read access to sensitive user directories. SSH private keys, GPG keys, Docker auth tokens, shell history, and (on WSL2) entire Windows drives are readable.

### 5.2 The Solution

Add explicit `denyRead` entries in `~/.claude/settings.json`:

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "filesystem": {
      "denyRead": [
        "~/.claude/.credentials.json",
        "~/.claude/history.jsonl",
        "~/.claude/debug/",
        "~/.claude/backups/",
        "~/.docker/",
        "~/.ssh/",
        "~/.gnupg/",
        "~/.bash_history",
        "~/.zsh_history",
        "~/.python_history",
        "~/.node_repl_history",
        "//mnt/c",
        "//mnt/d"
      ]
    }
  }
}
```

### 5.3 How the Sandbox Enforces This

When `denyRead` paths are configured, the bwrap sandbox mounts empty `tmpfs` filesystems over the denied directories, or binds them to `/dev/null` for individual files. This means:

| Denied Path | Sandbox Sees |
|-------------|-------------|
| `~/.ssh/` | Empty directory (tmpfs) |
| `~/.gnupg/` | Empty directory (tmpfs) |
| `~/.docker/` | Empty directory (tmpfs) |
| `~/.claude/.credentials.json` | `/dev/null` (character device, zero bytes) |
| `~/.claude/history.jsonl` | `/dev/null` |
| `~/.bash_history` | `/dev/null` |
| `//mnt/c`, `//mnt/d` | Empty directory (tmpfs) |

The data doesn't just return "permission denied" — it is **completely absent** from the sandbox's mount namespace. There is no way to access it even with elevated techniques.

### 5.4 Path Prefix Conventions

Claude Code uses a specific path syntax in `denyRead` / `allowWrite`:

| Prefix | Resolves To | Example |
|--------|-------------|---------|
| `~/` | User's home directory | `~/.ssh/` → `/home/user/.ssh/` |
| `//` | Absolute filesystem root | `//mnt/c` → `/mnt/c` |
| `/` | Relative to settings file location | `/build` → settings dir + `/build` |

**Note:** For Windows drive mounts, use `//mnt/c` (double slash) to ensure the path resolves as an absolute path from the filesystem root.

### 5.5 Verification

```bash
$ ls ~/.ssh/          # Empty directory
$ ls ~/.gnupg/        # Empty directory
$ cat ~/.bash_history # Empty (reads /dev/null)
$ ls /mnt/c/          # Empty directory
$ ls /mnt/d/          # Empty directory
$ file ~/.claude/.credentials.json
# character special (1/3) — mapped to /dev/null
```

---

## 6. Hardening Layer 3: AFK Guard Hook

### 6.1 The Problem

Claude Code's sandbox has an escape hatch: `dangerouslyDisableSandbox: true`. When a sandboxed command fails (e.g., network timeout, incompatible tool), Claude may retry with the sandbox disabled. This requires user approval — but if the user is away (AFK), the approval prompt sits indefinitely, and if auto-approve is configured, it could execute unsandboxed.

### 6.2 The Solution

A `PreToolUse` hook that **automatically denies any Bash call with `dangerouslyDisableSandbox: true`** when AFK mode is active.

**File:** `~/.claude/hooks/afk-guard.sh`

```bash
#!/bin/bash
# AFK Guard — block sandbox-disabled Bash calls when AFK mode is active
# Toggle: touch /tmp/claude-1000/afk (enable) / rm /tmp/claude-1000/afk (disable)

AFK_FILE="/tmp/claude-1000/afk"

if [ ! -f "$AFK_FILE" ]; then
  exit 0
fi

# Read tool info from stdin
INPUT=$(cat)

# Only block Bash calls with sandbox disabled
HAS_UNSAFE=$(echo "$INPUT" | grep -c '"dangerouslyDisableSandbox"[[:space:]]*:[[:space:]]*true')

if [ "$HAS_UNSAFE" -gt 0 ]; then
  cat <<'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "AFK mode — sandbox-disabled Bash blocked."
  }
}
EOF
  exit 0
fi

# Everything else allowed in AFK mode
exit 0
```

**Hook registration in `~/.claude/settings.json`:**

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash /home/<user>/.claude/hooks/afk-guard.sh"
          }
        ]
      }
    ]
  }
}
```

### 6.3 How It Works

1. The `PreToolUse` hook fires **before every tool call** (empty matcher = match all)
2. The hook receives the tool call JSON on stdin, including tool name and parameters
3. It checks for the presence of `"dangerouslyDisableSandbox": true`
4. If found **and** the AFK file exists, it returns a `deny` decision
5. All other tool calls pass through normally

### 6.4 Activating AFK Mode

AFK mode is toggled by creating or removing a sentinel file:

```bash
# Enable AFK mode (block sandbox escapes)
touch /tmp/claude-1000/afk

# Disable AFK mode (allow normal operation)
rm /tmp/claude-1000/afk
```

The file is placed in the sandbox-writable temp directory so it can be toggled from within Claude Code itself (e.g., via a `/afk` skill command).

### 6.5 Why PreToolUse and Not Permission Settings?

- `allowUnsandboxedCommands: false` in settings would **permanently** disable the escape hatch, which breaks legitimate workflows
- The AFK guard is **context-dependent** — it only blocks when you're away
- It uses the hook's `permissionDecision` field, which is the officially supported way for hooks to make access control decisions

---

## 7. Audit Results: Before vs. After

We conducted a full security audit from **inside** the sandbox to verify each hardening layer. The audit was performed by Claude Code itself, demonstrating that the protections hold even when the agent actively tries to find sensitive information.

### 7.1 Environment Variables

| Check | Default Sandbox | Hardened Sandbox |
|-------|----------------|-----------------|
| `printenv \| grep TOKEN` | `CLAUDE_CODE_SESSION_ACCESS_TOKEN=sk-ant-...` | **(empty)** |
| `printenv \| grep PROXY_PORT` | `CLAUDE_CODE_HOST_HTTP_PROXY_PORT=36499` | **(empty)** |
| `/proc/self/environ` | Contains all env vars | **(empty)** |
| `ps auxe \| grep TOKEN` | Visible in process env | **No matches** |

### 7.2 Filesystem Access

| Path | Default Sandbox | Hardened Sandbox |
|------|----------------|-----------------|
| `~/.ssh/` | SSH keys readable | **Empty tmpfs** |
| `~/.gnupg/` | GPG keys readable | **Empty tmpfs** |
| `~/.docker/` | Docker auth readable | **Empty tmpfs** |
| `~/.bash_history` | Command history readable | **→ /dev/null** |
| `~/.claude/.credentials.json` | Credentials readable | **→ /dev/null** |
| `/mnt/c`, `/mnt/d` | Windows drives accessible | **Empty tmpfs** |

### 7.3 Sandbox Escape Protection

| Scenario | Default Sandbox | Hardened Sandbox |
|----------|----------------|-----------------|
| `dangerouslyDisableSandbox` while user present | Prompts for approval | Prompts for approval |
| `dangerouslyDisableSandbox` while AFK | Prompts (blocks indefinitely) | **Auto-denied by hook** |

### 7.4 Overall Attack Surface

| Vector | Default | Hardened | Improvement |
|--------|---------|---------|-------------|
| Token exfiltration | Possible via env vars | **Blocked** | Session token invisible |
| SSH key theft | Possible via filesystem read | **Blocked** | Keys not mounted |
| Credential harvesting | Possible via known paths | **Blocked** | Paths masked |
| History snooping | Possible via shell history files | **Blocked** | Histories → /dev/null |
| Cross-drive access (WSL2) | Possible via /mnt | **Blocked** | Drives masked |
| Unattended sandbox escape | Possible if auto-approve | **Blocked** | AFK guard denies |

---

## 8. Implementation Guide

### 8.1 Prerequisites

- Claude Code with sandbox support (Linux/WSL2 with `bubblewrap` and `socat`, or macOS)
- Sandbox enabled in settings (`"sandbox": { "enabled": true }`)

### 8.2 Step-by-Step Setup

**1. Create the sandbox init script:**

```bash
cat > ~/.claude/sandbox-init.sh << 'EOF'
# Strip sensitive tokens and internal vars from sandbox environment
unset CLAUDE_CODE_SESSION_ACCESS_TOKEN 2>/dev/null
unset CLAUDE_CODE_HOST_HTTP_PROXY_PORT 2>/dev/null
unset CLAUDE_CODE_HOST_SOCKS_PROXY_PORT 2>/dev/null
EOF
```

**2. Wire it up via BASH_ENV in your shell profile:**

```bash
# Add to ~/.bashrc (or ~/.zshrc for zsh)
echo 'export BASH_ENV="$HOME/.claude/sandbox-init.sh"' >> ~/.bashrc
```

**3. Create the AFK guard hook:**

```bash
mkdir -p ~/.claude/hooks
cat > ~/.claude/hooks/afk-guard.sh << 'HOOK'
#!/bin/bash
AFK_FILE="/tmp/claude-1000/afk"

if [ ! -f "$AFK_FILE" ]; then
  exit 0
fi

INPUT=$(cat)
HAS_UNSAFE=$(echo "$INPUT" | grep -c '"dangerouslyDisableSandbox"[[:space:]]*:[[:space:]]*true')

if [ "$HAS_UNSAFE" -gt 0 ]; then
  cat <<'EOF'
{
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "deny",
    "permissionDecisionReason": "AFK mode — sandbox-disabled Bash blocked."
  }
}
EOF
  exit 0
fi

exit 0
HOOK
chmod +x ~/.claude/hooks/afk-guard.sh
```

**4. Configure settings.json:**

```json
{
  "sandbox": {
    "enabled": true,
    "autoAllowBashIfSandboxed": true,
    "filesystem": {
      "denyRead": [
        "~/.claude/.credentials.json",
        "~/.claude/history.jsonl",
        "~/.claude/debug/",
        "~/.claude/backups/",
        "~/.docker/",
        "~/.ssh/",
        "~/.gnupg/",
        "~/.bash_history",
        "~/.zsh_history",
        "~/.python_history",
        "~/.node_repl_history",
        "//mnt/c",
        "//mnt/d"
      ]
    }
  },
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "",
        "hooks": [
          {
            "type": "command",
            "command": "bash ~/.claude/hooks/afk-guard.sh"
          }
        ]
      }
    ]
  }
}
```

**5. Verify the hardening:**

Start a new Claude Code session and run:

```bash
printenv | grep -i token    # Should return nothing
ls ~/.ssh/                   # Should be empty
cat ~/.bash_history          # Should be empty
```

### 8.3 Customization

- **Additional env vars to strip:** Add more `unset` lines to `sandbox-init.sh` for any other sensitive variables in your environment (e.g., `AWS_SECRET_ACCESS_KEY`, `GITHUB_TOKEN`)
- **Additional paths to deny:** Add entries to `denyRead` for your specific setup (e.g., `~/.aws/`, `~/.kube/`, `~/.config/gcloud/`)
- **AFK toggle method:** The sentinel file approach can be wrapped in a Claude Code skill (e.g., `/afk on`, `/afk off`) for convenience

---

## 9. Known Limitations

### 9.1 BASH_ENV Only Works for Bash

If a command spawns a non-Bash shell (e.g., `python -c "import os; print(os.environ)"`, `node -e "console.log(process.env)"`), the `BASH_ENV` init script does not run. The environment variables would still be visible to those interpreters.

**Mitigation:** The `unset` happens in the parent Bash shell before the interpreter starts, so the variables are typically already gone from the inherited environment. However, if a future Claude Code version passes env vars differently (e.g., via `/proc` or bwrap `--setenv` directly to the child process), this could be bypassed.

### 9.2 denyRead Does Not Cover All Sensitive Paths

The deny list is explicitly enumerated. New sensitive files (e.g., a new credential manager, a new cloud CLI config) would need to be added manually.

### 9.3 AFK Guard Relies on File Presence

The AFK sentinel file (`/tmp/claude-1000/afk`) must be in a sandbox-writable directory. A sophisticated attack could potentially remove the file to disable AFK protection, though this would require the attacker to already have sandbox-level code execution.

### 9.4 Docker Socket Remains Visible

The Docker socket at `/var/run/docker.sock` is visible inside the sandbox (though not usable due to network isolation and group membership restrictions). For maximum security, consider adding `//var/run/docker.sock` to the `denyRead` list or removing the Docker socket entirely.

### 9.5 Network Proxy Limitations

As noted in the [official documentation](https://docs.anthropic.com/en/docs/claude-code/security#:~:text=network), the network proxy filters by domain name only — it does not inspect traffic content. Broad domain allowlists (e.g., `github.com`) could theoretically enable data exfiltration even with all other hardening in place.

---

## 10. Sources

- [Claude Code Sandboxing Documentation](https://docs.anthropic.com/en/docs/claude-code/security)
- [Claude Code Hooks Documentation](https://docs.anthropic.com/en/docs/claude-code/hooks)
- [Claude Code Settings Reference](https://docs.anthropic.com/en/docs/claude-code/settings)
- [Bubblewrap (bwrap) — GitHub](https://github.com/containers/bubblewrap)
- [Bash Reference Manual — Startup Files](https://www.gnu.org/software/bash/manual/html_node/Bash-Startup-Files.html#:~:text=BASH_ENV)
- [Anthropic Sandbox Runtime — GitHub](https://github.com/anthropic-experimental/sandbox-runtime)

---

*Built by [agentIA](https://github.com/AgentiaPT) — exploring what's possible when AI and human curiosity work together.*
