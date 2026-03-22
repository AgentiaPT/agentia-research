---
title: "Git Secret Detection & Sensitive Information Leak Prevention"
date: 2026-03-17
status: complete
tags: [security, secrets, pre-commit, PII, devops, tools, gitleaks]
---

# Git Secret Detection & Sensitive Information Leak Prevention

> ✨ This project was authored by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

Comprehensive landscape analysis of tools, practices, and patterns for preventing secrets and sensitive data from leaking into git repositories. Special attention to AI-authored content risks and PII detection beyond traditional API key scanning.

## Implementation

This research resulted in a full defense-in-depth implementation for this repo:

| Layer | What | Files |
|-------|------|-------|
| **Pre-commit hook** | Gitleaks v8.24.2 with custom PII rules | `.githooks/pre-commit`, `.gitleaks.toml` |
| **Claude Code hook** | Auto-installs gitleaks + sets hooks path | `.claude/hooks/session-start.sh` |
| **CI pipeline** | Gitleaks + TruffleHog (with verification) | `.github/workflows/secret-scan.yml` |
| **Server-side** | GitHub Push Protection (free for public repos) | Enable in repo Settings > Security |

### Custom PII Rules (`.gitleaks.toml`)

Beyond the 150+ default secret patterns, we added rules for:
- Email addresses (with allowlist for noreply, example.com, etc.)
- US phone numbers (requires separators to avoid DOI/URL false positives)
- Social Security Numbers
- Credit card numbers (Visa, Mastercard, Amex)
- Public IPv4 addresses (private ranges allowlisted)
- Passport numbers, driver's license numbers
- Date of birth patterns
- US street addresses

### Scripts

- `scripts/install-gitleaks.sh` — Downloads pinned v8.24.2 binary with SHA256 checksum verification
- `scripts/scan-secrets.sh` — Wrapper for staged (`--staged`), full repo (`--full`), or diff (`--diff`) scans

### Gitleaks Trust Audit

Gitleaks v8.24.2 is safe: fully offline, MIT-licensed, 25k stars, no CVE history. **Caveat**: the original creator (Zach Rice) has stated he no longer controls the repo; he created **Betterleaks** as a successor at Aikido Security. We pin to v8.24.2 and do not auto-update.

---

## Table of Contents

1. [Tool Comparison Matrix](#tool-comparison-matrix)
2. [Detailed Tool Profiles](#detailed-tool-profiles)
3. [GitHub Built-in Secret Scanning](#github-built-in-secret-scanning)
4. [AI-Authored Content Risks](#ai-authored-content-risks)
5. [Custom PII Patterns](#custom-pii-patterns)
6. [Pre-commit Framework Integration](#pre-commit-framework-integration)
7. [Recommended Architecture](#recommended-architecture)

---

## Tool Comparison Matrix

| Tool | GitHub Stars | Language | Detection Method | Config Format | Pre-commit Support | Verification | False Positive Rate | Maintenance |
|------|-------------|----------|-----------------|---------------|-------------------|--------------|-------------------|-------------|
| **Gitleaks** | ~24,400 | Go | Regex (150+ patterns) | TOML | Native | No | Low-Medium | Active |
| **TruffleHog** | ~24,500 | Go | Regex + Entropy + Verification (800+ detectors) | YAML/CLI | Via wrapper | Yes (live API calls) | Low (verified) | Active (commercial backing) |
| **detect-secrets** | ~3,700+ | Python | Regex + Entropy + Keyword (27 plugins) | JSON baseline | Native | No | Medium (tunable) | Active (Yelp) |
| **git-secrets** | ~13,000 | Bash | Regex | CLI patterns | Native (git hooks) | No | Low | Maintenance mode |
| **secretlint** | ~1,300 | TypeScript | Regex (pluggable rules) | JSON (.secretlintrc) | Via pre-commit | No | Low | Active |
| **Trivy** | ~24,000+ | Go | Regex + Keywords | YAML | Via CI (not pre-commit) | No | Medium | Active (Aqua Security) |
| **ggshield** | ~2,000+ | Python | ML + Regex (500+ types) | YAML/.gitguardian | Native | Yes (API-based) | Low | Active (commercial) |

---

## Detailed Tool Profiles

### Gitleaks

> **Best for**: Fast pre-commit scanning, CI/CD pipelines, teams wanting simple setup.

- **Repository**: [github.com/gitleaks/gitleaks](https://github.com/gitleaks/gitleaks)
- **How it works**: Pure regex-based matching against 150+ built-in patterns. Each rule defines a pattern and optional keywords. No entropy analysis by default (but entropy thresholds can be configured per-rule).
- **Config format**: TOML (`gitleaks.toml`)
  ```toml
  title = "gitleaks config"

  [extend]
  useDefault = true

  [[rules]]
  id = "custom-api-key"
  description = "Custom API Key"
  regex = '''(?i)custom[_-]?api[_-]?key\s*[:=]\s*['"]?([a-zA-Z0-9]{32,})'''
  tags = ["custom", "api-key"]

  [allowlist]
  paths = [
    '''\.env\.example''',
    '''tests/fixtures/''',
  ]
  ```
- **Pre-commit integration**: First-class support via `.pre-commit-config.yaml`:
  ```yaml
  repos:
    - repo: https://github.com/gitleaks/gitleaks
      rev: v8.24.2
      hooks:
        - id: gitleaks
          args: ['--config', '.gitleaks.toml']
  ```
  Also works as native git hook: `gitleaks protect --staged --redact`
- **Strengths**: Fastest scanner, minimal resource usage, ideal for pre-commit. Uses Go's regexp package.
- **Weaknesses**: No credential verification (cannot tell if a detected key is live). Regex-only means some novel patterns may be missed. Go regexp has some limitations vs PCRE (no lookaheads).
- **Skip mechanism**: `SKIP=gitleaks git commit -m "..."`

### TruffleHog

> **Best for**: Deep scanning, credential verification, post-commit/CI scanning, security audits.

- **Repository**: [github.com/trufflesecurity/trufflehog](https://github.com/trufflesecurity/trufflehog)
- **How it works**: Layered detection model combining entropy checks, regex patterns, credential context, and **live API verification**. Over 800 purpose-built detectors, each targeting a specific credential type.
- **Detection pipeline**:
  1. Entropy analysis flags high-randomness strings
  2. Regex patterns match known credential formats
  3. **Verification** -- attempts to authenticate against the relevant API
  4. Results classified as: **verified** (credential is live), **unverified** (detected but not confirmed), **unknown** (verification failed)
- **Config format**: CLI flags + custom detector YAML. Custom detectors support entropy thresholds, regex for full match and captured secret, and excluded word lists.
- **Scanning sources**: Git repos, GitHub/GitLab orgs, Docker images, S3, GCS, filesystems, CircleCI, TravisCI.
- **Pre-commit**: Not designed as a pre-commit hook (too slow/resource-intensive). Best used in CI/CD or scheduled scans.
- **Strengths**: Credential verification is a game-changer -- eliminates most false positives by confirming if secrets are live. Deepest coverage (800+ types). Custom webhook-based verification for internal credentials.
- **Weaknesses**: Resource-intensive, long scan times. Not suitable for fast pre-commit feedback. Commercial enterprise features.
- **Custom verification via webhook**:
  ```yaml
  # TruffleHog sends JSON POST with regex matches to your endpoint
  # 200 OK = secret verified, anything else = unverified
  ```

### detect-secrets (Yelp)

> **Best for**: Enterprise teams with legacy codebases, baseline-driven incremental adoption.

- **Repository**: [github.com/Yelp/detect-secrets](https://github.com/Yelp/detect-secrets)
- **How it works**: Three detection strategies:
  1. **Regex-based** rules for structured secrets (AWS keys, GitHub tokens)
  2. **Entropy detection** using Base64 and Hex analysis for random-looking strings
  3. **Keyword detection** flagging variable names tied to hardcoded credentials (e.g., `password =`, `secret_key =`)
- **Config format**: JSON baseline file (`.secrets.baseline`)
  ```bash
  # Generate baseline
  detect-secrets scan > .secrets.baseline

  # Audit baseline (label true/false positives)
  detect-secrets audit .secrets.baseline

  # Pre-commit check against baseline
  detect-secrets-hook --baseline .secrets.baseline
  ```
- **27 built-in plugins** covering AWS, Azure, GitHub, Slack, Stripe, private keys, high entropy strings, and more.
- **Baseline approach**: The key innovation. Instead of demanding all existing secrets be fixed immediately, detect-secrets accepts the current state as a baseline and prevents new secrets from being introduced. This is critical for large legacy codebases.
- **False positive management**:
  - Inline allowlisting: `# pragma: allowlist secret` at end of line
  - Pre-line allowlisting: `// pragma: allowlist nextline secret` before the line
  - Auditing workflow to label results and optimize plugin signal-to-noise ratio
  - Analytics to quantify plugin effectiveness
- **Pre-commit integration**:
  ```yaml
  repos:
    - repo: https://github.com/Yelp/detect-secrets
      rev: v1.5.0
      hooks:
        - id: detect-secrets
          args: ['--baseline', '.secrets.baseline']
  ```
- **Strengths**: Baseline approach is pragmatic for adoption. Entropy detection catches novel secrets. Plugin system is extensible. Enterprise-proven at Yelp scale.
- **Weaknesses**: Entropy and keyword plugins generate more false positives than pure regex tools. Python-based (slower than Go tools). No credential verification.

### git-secrets (AWS Labs)

> **Best for**: AWS-centric teams needing simple credential protection.

- **Repository**: [github.com/awslabs/git-secrets](https://github.com/awslabs/git-secrets)
- **How it works**: Regex-based scanning of commits, commit messages, and file diffs. Primarily targets AWS credentials but supports custom patterns.
- **Config format**: CLI-based pattern registration (stored in `.gitconfig`):
  ```bash
  git secrets --register-aws           # Register AWS patterns
  git secrets --add 'CUSTOM_PATTERN'   # Add custom regex
  git secrets --install                # Install hooks
  ```
- **Pre-commit**: Installs as native git hooks (pre-commit, commit-msg, prepare-commit-msg).
- **Strengths**: Dead simple for AWS shops. Zero config for basic AWS credential protection. Lightweight bash implementation.
- **Weaknesses**: Limited to regex only. No entropy analysis. Narrow default pattern set (AWS-focused). In maintenance mode -- no major new features. Does not integrate with the pre-commit framework natively (uses its own hook installer).

### secretlint

> **Best for**: JavaScript/TypeScript teams wanting linter-style secret detection.

- **Repository**: [github.com/secretlint/secretlint](https://github.com/secretlint/secretlint)
- **How it works**: Pluggable rule-based architecture. No built-in rules -- you install rule packages and configure them.
- **Config format**: JSON (`.secretlintrc.json`):
  ```json
  {
    "rules": [
      { "id": "@secretlint/secretlint-rule-preset-recommend" },
      { "id": "@secretlint/secretlint-rule-aws" },
      { "id": "@secretlint/secretlint-rule-npm" }
    ]
  }
  ```
- **Pre-commit integration**: Works with pre-commit framework or as npm script.
- **Strengths**: Linter-style UX familiar to JS developers. Pluggable architecture. Each rule documents why it detects something as a secret. TypeScript implementation.
- **Weaknesses**: Smaller community and pattern coverage vs Gitleaks/TruffleHog. Requires explicit rule package installation. Node.js dependency.

### Trivy (Secret Scanning Mode)

> **Best for**: Teams already using Trivy for container/IaC scanning who want unified tooling.

- **Repository**: [github.com/aquasecurity/trivy](https://github.com/aquasecurity/trivy)
- **How it works**: Built-in rules using regex + keyword matching. Keywords enable a fast pre-filter (string compare) before running regex. Uses Go regexp (multi-line mode with `(?m)` for `^`/`$`).
- **Config format**: YAML (`trivy-secret.yaml`):
  ```yaml
  rules:
    - id: "custom-secret"
      category: CustomSecret
      title: "Custom API Key"
      severity: HIGH
      keywords:
        - "custom_api"
      regex: "custom_api_key\\s*=\\s*['\"]([^'\"]+)"
      allow-rules:
        - id: "allow-test"
          description: "Allow test fixtures"
          regex: "test_.*"
  ```
- **False positive management**: Allow rules per-rule with regex and path matching. Can disable specific rule IDs via `disable-rules` list.
- **Strengths**: Unified scanner (containers, IaC, secrets, vulnerabilities). Active development by Aqua Security. Good for CI/CD.
- **Weaknesses**: Not designed for pre-commit (oriented toward container/image scanning). Secret scanning is secondary to its core container scanning mission. Medium false positive rate.

### ggshield (GitGuardian)

> **Best for**: Teams wanting ML-powered detection with commercial support.

- **Repository**: [github.com/GitGuardian/ggshield](https://github.com/GitGuardian/ggshield)
- **How it works**: Sends code to GitGuardian's API for ML-powered analysis. Detects 500+ secret types. Combines pattern matching with machine learning for context-aware detection.
- **Pre-commit integration**:
  ```yaml
  repos:
    - repo: https://github.com/GitGuardian/ggshield
      rev: v1.34.0
      hooks:
        - id: ggshield
          language: python
          stages: [pre-commit]
  ```
- **Features**: `--all-secrets` mode, `--ignore-known-secrets`, SARIF output, scan merge files.
- **Strengths**: ML-powered detection catches generic/obfuscated secrets. Historical scanning. Dashboard for tracking and remediation. Low false positive rate.
- **Weaknesses**: Requires API key (sends code to external service). Free tier has limitations. Not fully offline-capable.

---

## GitHub Built-in Secret Scanning

### Current State (March 2026)

GitHub now offers two standalone products (split from Advanced Security in April 2025):

1. **GitHub Secret Protection** -- $19/month per active committer
2. **GitHub Code Security** -- separate product

### Push Protection

Push protection is **free for all public repositories** and enabled by default. For private repos, it requires GitHub Secret Protection.

**How it works**: Scans code during `git push` (server-side), before content enters the repository. If a secret is detected, the push is blocked with an explanation.

**Current coverage** (March 2026):
- **254 token types** detected total
- **39 detectors with push protection enabled by default** (including Airtable, Databricks, Heroku, PostHog, Shopify)
- **28 new detectors added March 2026** from 15 providers (Lark, Vercel, Snowflake, Supabase, etc.)
- Validity checks for Airtable, DeepSeek, npm, Pinecone, Sentry tokens

**Custom patterns** (August 2025 GA): Organizations can define custom regex patterns and include them in push protection. Only applies to repos with Secret Protection enabled.

### Limitations

1. **Coverage gaps**: ~254 token types with only ~97 having push protection. No generic secret detection (random API keys, passwords without known patterns).
2. **50MB push size limit**: Large migrations can bypass detection.
3. **Bypassable**: Developers can bypass with justification (configurable per-org). Delegated bypass feature exists.
4. **No PII detection**: Only targets API keys/tokens, not personal data.
5. **No pre-commit**: Server-side only -- secrets already exist in local git history before push protection catches them.
6. **No historical scanning** in free tier: Only scans new pushes.
7. **Private repos require paid plan**: Full features need $19/committer/month.

### Comparison with Third-Party Tools

| Feature | GitHub Push Protection | Gitleaks | TruffleHog | ggshield |
|---------|----------------------|----------|------------|----------|
| Pre-commit (local) | No | Yes | No | Yes |
| Server-side | Yes | No | No | No |
| Verification | Some (validity checks) | No | Yes (800+) | Yes (API) |
| Custom patterns | Yes (paid) | Yes (TOML) | Yes (YAML) | Yes |
| PII detection | No | With custom rules | No | No |
| Generic secrets | No | With entropy rules | Yes (entropy) | Yes (ML) |
| Offline | N/A | Yes | Yes | No |
| Cost | Free (public) / $19/mo | Free | Free / Enterprise | Free tier / Paid |

---

## AI-Authored Content Risks

### The Problem

AI coding assistants (GitHub Copilot, Claude Code, ChatGPT) introduce unique risks:

1. **Training data leakage**: LLMs may reproduce API keys, tokens, or credentials seen in training data.
2. **PII in generated content**: Models may generate realistic-looking personal data (names, emails, phone numbers, addresses) that could be real people's data from training.
3. **Prompt injection in code**: AI-generated code may contain injected credentials or backdoors.
4. **Scraped content reproduction**: AI may reproduce content from web scraping that contains personal information.

### Scale of the Problem

- [Lasso Security research](https://www.lasso.security/blog/lasso-research-reveals-13-of-generative-ai-prompts-contain-sensitive-organizational-data#:~:text=13%25%20of%20GenAI%20Prompts%20Leak%20Sensitive%20Data) (Feb 2025): **13% of GenAI prompts contain sensitive organizational data**
- [Keysight research](https://www.keysight.com/blogs/en/tech/nwvs/2025/08/04/pii-disclosure-in-user-request#:~:text=8.5%25%20of%20prompts): **8.5% of prompts** to tools like ChatGPT/Copilot included sensitive information
- **11.2%** of prompts containing personal data were flagged, often including email addresses and payment info

### Prevention Strategies for AI-Authored Code

1. **Pre-commit scanning**: Run secret + PII scanners on all commits regardless of author (human or AI).
2. **Layered detection**: Combine regex (structured patterns) with entropy (random strings) and NLP/ML (semantic understanding).
3. **Content sanitization**: Tools like [DataFog](https://github.com/DataFog/datafog-python) and [PII-PALADIN](https://github.com/jeeem/PII-PALADIN) combine NER (Named Entity Recognition) with regex for comprehensive PII detection.
4. **DLP integration**: Enterprise tools like Microsoft Purview, Symantec DLP, or Google Cloud DLP for pre-ingestion scanning.
5. **Multilingual awareness**: Traditional regex tools are not multilingual or semantic -- they miss obfuscated or translated leaks. ML-based approaches are needed for comprehensive coverage.

### Recommended AI-Content Pre-commit Pipeline

```
AI generates code
    |
    v
[Gitleaks] -- catches known secret patterns (API keys, tokens)
    |
    v
[Custom PII rules] -- catches emails, phones, SSNs, etc.
    |
    v
[Entropy check] -- catches random high-entropy strings
    |
    v
[Optional: NLP/ML PII detector] -- catches semantic PII
    |
    v
Commit allowed (or blocked with explanation)
```

---

## Custom PII Patterns

### Gitleaks Custom Rules for PII Detection

These patterns extend beyond default secret detection to catch personally identifiable information. Add to your `gitleaks.toml`:

```toml
[extend]
useDefault = true

# --- Email Addresses ---
[[rules]]
id = "email-address"
description = "Email address detected"
regex = '''[a-zA-Z0-9._%+\-]+@[a-zA-Z0-9.\-]+\.[a-zA-Z]{2,}'''
tags = ["pii", "email"]
[rules.allowlist]
regexes = [
  '''noreply@''',
  '''example\.(com|org|net)''',
  '''@users\.noreply\.github\.com''',
  '''test@test''',
]

# --- US Phone Numbers ---
[[rules]]
id = "us-phone-number"
description = "US phone number detected"
regex = '''(?:\+?1[-.\s]?)?\(?[2-9]\d{2}\)?[-.\s]?\d{3}[-.\s]?\d{4}'''
tags = ["pii", "phone"]
keywords = ["phone", "tel", "mobile", "cell", "fax", "contact"]

# --- Social Security Numbers ---
[[rules]]
id = "ssn"
description = "Social Security Number detected"
regex = '''\b\d{3}-\d{2}-\d{4}\b'''
tags = ["pii", "ssn"]
keywords = ["ssn", "social security", "social_security"]

# --- Credit Card Numbers ---
[[rules]]
id = "credit-card-visa"
description = "Visa credit card number"
regex = '''\b4\d{3}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'''
tags = ["pii", "credit-card"]
keywords = ["card", "credit", "visa", "payment"]

[[rules]]
id = "credit-card-mastercard"
description = "Mastercard credit card number"
regex = '''\b5[1-5]\d{2}[-\s]?\d{4}[-\s]?\d{4}[-\s]?\d{4}\b'''
tags = ["pii", "credit-card"]
keywords = ["card", "credit", "mastercard", "payment"]

[[rules]]
id = "credit-card-amex"
description = "American Express credit card number"
regex = '''\b3[47]\d{2}[-\s]?\d{6}[-\s]?\d{5}\b'''
tags = ["pii", "credit-card"]
keywords = ["card", "credit", "amex", "american express", "payment"]

# --- IPv4 Addresses ---
[[rules]]
id = "ipv4-address"
description = "IPv4 address detected"
regex = '''\b(?:(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\.){3}(?:25[0-5]|2[0-4]\d|[01]?\d\d?)\b'''
tags = ["pii", "network"]
keywords = ["ip", "address", "host", "server", "endpoint"]
[rules.allowlist]
regexes = [
  '''127\.0\.0\.1''',
  '''0\.0\.0\.0''',
  '''10\.\d+\.\d+\.\d+''',
  '''172\.(1[6-9]|2\d|3[01])\.\d+\.\d+''',
  '''192\.168\.\d+\.\d+''',
]

# --- US Physical Addresses (basic) ---
[[rules]]
id = "us-street-address"
description = "Possible US street address"
regex = '''\d{1,5}\s+[A-Z][a-zA-Z]+(?:\s+[A-Z][a-zA-Z]+)*\s+(?:St|Street|Ave|Avenue|Blvd|Boulevard|Dr|Drive|Ln|Lane|Rd|Road|Ct|Court|Pl|Place|Way|Cir|Circle)\.?'''
tags = ["pii", "address"]
keywords = ["address", "street", "avenue", "boulevard"]

# --- US ZIP Codes (contextual) ---
[[rules]]
id = "us-zipcode"
description = "US ZIP code in address context"
regex = '''\b\d{5}(?:-\d{4})?\b'''
tags = ["pii", "zipcode"]
keywords = ["zip", "postal", "zipcode"]

# --- Date of Birth patterns ---
[[rules]]
id = "date-of-birth"
description = "Date of birth pattern"
regex = '''(?i)(?:dob|date.of.birth|birthdate|birth.date)\s*[:=]\s*[\d/\-\.]+'''
tags = ["pii", "dob"]
```

### UK Trade PII Hooks

The [UK Trade pii-secret-check-hooks](https://github.com/uktrade/pii-secret-check-hooks) project provides a ready-made pre-commit hook for PII detection. Custom regexes are added one per line in a file, without start/end markers.

### Private AI Pre-commit Hook

[Private AI's pre-commit hook](https://github.com/privateai/pai-pre-commit-hook) reports all suspected PII in staged code and prevents commits. Supports extending detected entities via `--blocked-list` argument with space-separated entity type and regex pairs.

### GitLab Custom PII Rulesets

GitLab supports [custom PII detection rulesets](https://about.gitlab.com/blog/enhance-data-security-with-custom-pii-detection-rulesets/) that can be applied to secret detection pipelines. Organizations define patterns for emails, phone numbers, SSNs, etc. in TOML configuration files.

---

## Pre-commit Framework Integration

### Multi-Tool Configuration

Best practice is layering multiple tools in a single `.pre-commit-config.yaml`:

```yaml
repos:
  # --- Secret Detection (fast, regex-based) ---
  - repo: https://github.com/gitleaks/gitleaks
    rev: v8.24.2
    hooks:
      - id: gitleaks
        args: ['--config', '.gitleaks.toml']

  # --- Baseline Secret Detection (entropy + regex) ---
  - repo: https://github.com/Yelp/detect-secrets
    rev: v1.5.0
    hooks:
      - id: detect-secrets
        args: ['--baseline', '.secrets.baseline']

  # --- PII Detection ---
  - repo: https://github.com/uktrade/pii-secret-check-hooks
    rev: 0.4.0
    hooks:
      - id: pii-check

  # --- Additional checks ---
  - repo: https://github.com/pre-commit/pre-commit-hooks
    rev: v5.0.0
    hooks:
      - id: detect-private-key
      - id: check-added-large-files
        args: ['--maxkb=500']
```

### Key Integration Patterns

1. **Gitleaks for speed**: Runs first as the fastest scanner, catches known patterns.
2. **detect-secrets for depth**: Baseline approach catches entropy-based secrets Gitleaks might miss.
3. **PII hooks for personal data**: Specialized hooks catch non-secret sensitive data.
4. **`detect-private-key`**: Built-in pre-commit hook catches committed private keys.
5. **Large file check**: Prevents accidental binary/data file commits that might contain sensitive data.

### Skipping Hooks

```bash
# Skip specific hooks
SKIP=gitleaks,detect-secrets git commit -m "..."

# Skip all hooks (use sparingly)
git commit --no-verify -m "..."
```

### Global Installation

For organization-wide enforcement:

```bash
# Set up global hooks directory
git config --global core.hooksPath ~/.git-hooks

# Install pre-commit globally
pre-commit init-templatedir ~/.git-template
git config --global init.templateDir ~/.git-template
```

---

## Recommended Architecture

### Defense-in-Depth Strategy

```
Layer 1: IDE/Editor           -- Real-time warnings (VS Code extensions, etc.)
    |
Layer 2: Pre-commit (local)   -- Gitleaks + detect-secrets + PII rules
    |
Layer 3: Pre-push (local)     -- Optional deeper scan before push
    |
Layer 4: Server-side          -- GitHub Push Protection (free for public repos)
    |
Layer 5: CI/CD Pipeline       -- TruffleHog deep scan + verification
    |
Layer 6: Scheduled Scans      -- Bi-weekly full repository audit
    |
Layer 7: Monitoring           -- GitHub secret scanning alerts + dashboard
```

### Minimum Viable Setup (Free, Open Source)

For a team wanting basic protection with zero cost:

1. **Pre-commit**: Gitleaks with custom PII rules (TOML config)
2. **Server-side**: GitHub Push Protection (free on public repos)
3. **CI**: TruffleHog scan on PRs
4. **Scheduled**: Monthly `gitleaks detect --source .` full repo scan

### Enterprise Setup

1. **Pre-commit**: Gitleaks + detect-secrets (baseline) + ggshield
2. **Server-side**: GitHub Secret Protection ($19/committer/month) with custom patterns
3. **CI**: TruffleHog with verification + Trivy (container secrets)
4. **Monitoring**: GitGuardian dashboard for tracking, remediation, and compliance
5. **Training**: Developer security awareness, especially for AI tool usage

### For AI-Heavy Development Workflows

When using Claude Code, Copilot, or similar AI coding tools:

1. **Always run pre-commit hooks** -- AI-generated code is just as likely (or more) to contain secrets/PII.
2. **Add PII rules** to Gitleaks config beyond default secret patterns.
3. **Use entropy detection** (detect-secrets) to catch novel/unknown secret formats that AI might generate.
4. **Review AI-generated test data** -- AI often generates realistic-looking data that could be real PII from training data.
5. **Consider NLP-based PII detection** for content-heavy repositories (research, documentation).

---

## Sources

### Tool Repositories
- [Gitleaks](https://github.com/gitleaks/gitleaks)
- [TruffleHog](https://github.com/trufflesecurity/trufflehog)
- [detect-secrets (Yelp)](https://github.com/Yelp/detect-secrets)
- [git-secrets (AWS)](https://github.com/awslabs/git-secrets)
- [secretlint](https://github.com/secretlint/secretlint)
- [Trivy](https://trivy.dev/docs/latest/scanner/secret/)
- [ggshield (GitGuardian)](https://github.com/GitGuardian/ggshield)

### PII Detection Tools
- [Private AI pre-commit hook](https://github.com/privateai/pai-pre-commit-hook)
- [UK Trade pii-secret-check-hooks](https://github.com/uktrade/pii-secret-check-hooks)
- [DataFog PII detection](https://github.com/DataFog/datafog-python)
- [PII-PALADIN](https://github.com/jeeem/PII-PALADIN)
- [pii-scan (AWS Comprehend)](https://github.com/ventz/pii-scan)

### GitHub Documentation
- [About push protection](https://docs.github.com/en/code-security/secret-scanning/introduction/about-push-protection)
- [Defining custom patterns](https://docs.github.com/en/code-security/secret-scanning/using-advanced-secret-scanning-and-push-protection-features/custom-patterns/defining-custom-patterns-for-secret-scanning)
- [Secret scanning pattern updates March 2026](https://github.blog/changelog/2026-03-10-secret-scanning-pattern-updates-march-2026/)
- [GitHub Secret Protection launch (March 2025)](https://github.blog/changelog/2025-03-04-introducing-github-secret-protection-and-github-code-security/)
- [Custom patterns in push protection GA (August 2025)](https://github.blog/changelog/2025-08-19-secret-scanning-configuring-patterns-in-push-protection-is-now-generally-available/)

### Analysis & Comparisons
- [Gitleaks vs TruffleHog (2026) - AppSecSanta](https://appsecsanta.com/sast-tools/gitleaks-vs-trufflehog)
- [TruffleHog vs Gitleaks - Jit](https://www.jit.io/resources/appsec-tools/trufflehog-vs-gitleaks-a-detailed-comparison-of-secret-scanning-tools)
- [Best Secret Scanning Tools 2025 - Aikido](https://www.aikido.dev/blog/top-secret-scanning-tools)
- [Secret Scanning Tools 2026 - GitGuardian](https://blog.gitguardian.com/secret-scanning-tools/)
- [GitHub Push Protection Limitations - GitGuardian](https://blog.gitguardian.com/github-push-protection-enhancing-open-source-security-with-limitations-to-consider/)
- [Gitleaks pre-commit setup (2026)](https://www.d4b.dev/blog/2026-02-01-gitleaks-pre-commit-hook/)
- [Secret detection implementation guide (2026)](https://oneuptime.com/blog/post/2026-01-30-secret-detection/view)

### AI & PII Research
- [13% of GenAI prompts leak sensitive data - Lasso Security](https://www.lasso.security/blog/lasso-research-reveals-13-of-generative-ai-prompts-contain-sensitive-organizational-data)
- [PII disclosure in LLM requests - Keysight](https://www.keysight.com/blogs/en/tech/nwvs/2025/08/04/pii-disclosure-in-user-request)
- [LLM Privacy Protection Strategies 2025 - Protecto](https://www.protecto.ai/blog/llm-privacy-protection-strategies-2025)
- [Advanced LLM security: preventing secret leakage - Doppler](https://www.doppler.com/blog/advanced-llm-security)
- [GitLab custom PII detection rulesets](https://about.gitlab.com/blog/enhance-data-security-with-custom-pii-detection-rulesets/)
