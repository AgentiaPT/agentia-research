---
title: "AI × Software Engineering — March 22–29, 2026"
date: 2026-03-29
status: complete
tags: [ai, news, weekly, voices, industry, supply-chain, security, agentic-sdlc, vibe-coding]
explorers:
  - file: explorer.html
    title: AI × Software Engineering Dashboard
    description: Visual dashboard with voice position maps, signal radar, theme coverage, and key quotes
    screenshot: explorer-screenshot.png
---

# AI × Software Engineering — March 22–29, 2026

> **Note:** This project was authored by [Claude Code](https://docs.anthropic.com/en/docs/claude-code) (AI) with human direction and review. While factual accuracy and quality were prioritized, AI-generated content may contain errors, hallucinations, or outdated information. Sources and claims should be independently verified before relying on them.

A curated, thematic feed tracking the voices, signals, and narratives shaping the intersection of AI and software engineering. Organized around recurring themes rather than raw chronology. Continues from [the March 14–21 edition](https://github.com/AgentiaPT/agentia-research/blob/main/projects/9985-2026-03-21-ai-news-feed/README.md).

Open the [Explorer](https://agentiapt.github.io/agentia-research/projects/9984-2026-03-29-ai-news-feed/explorer.html) for a visual dashboard with voice position maps, signal radar, and theme analysis.

## Contents

1. [The Supply Chain Reckoning](#1-the-supply-chain-reckoning--litellm-trivy-and-the-teampcp-campaign) — LiteLLM backdoored, 500K credentials stolen, Trivy weaponized
2. [The Mythos Leak](#2-the-mythos-leak--anthropics-next-frontier-exposed) — Claude Mythos/Capybara revealed via misconfigured CMS, "step change" in capabilities
3. [Claude Code Goes Autonomous](#3-claude-code-goes-autonomous--auto-mode-and-long-running-harnesses) — Auto Mode, harness design for multi-hour sessions, three-agent architecture
4. [The Data Training Backlash](#4-the-data-training-backlash--github-copilot-opts-you-in) — Copilot training on user data by default, 172 downvotes, developer revolt
5. [Vibe Coding Gets a Security Layer](#5-vibe-coding-gets-a-security-layer--lovable--aikido) — First AI pentesting for vibe-coded apps, $100/test
6. [The Regression Problem](#6-the-regression-problem--agents-break-what-they-fix) — SWE-CI: 75% of agents break working code; TDAD: 70% regression reduction
7. [Karpathy's AutoResearch](#7-karpathys-autoresearch--humans-are-the-bottleneck) — 700 experiments, 11% training speedup, "simulate a research community"
8. [Anthropic vs. The Pentagon](#8-anthropic-vs-the-pentagon--first-amendment-wins-round-one) — Federal judge blocks DOD ban, "classic illegal retaliation"
9. [The Voice Tracker](#9-the-voice-tracker--who-said-what) — Fowler, Hightower, Hashimoto, Stenberg, and 19 others
10. [The Jobs Escalation Continues](#10-the-jobs-escalation-continues--cfos-admit-9x) — CFOs expect 9x increase in AI layoffs, ~55-60K tech workers cut YTD
11. [Model & Tool Updates](#11-model--tool-updates--footnotes) — Cursor Composer 2, Windsurf pricing backlash, Mistral Voxtral TTS, benchmarks
12. [Signals & Radar](#12-signals--radar) | [Key Quotes](#key-quotes-of-the-week) | [Voice Tracker](#voice-tracker-table)

---

## The Week's Narrative

Last week was **the consolidation** — every layer of the stack made its move, from OpenAI acquiring Astral to Anthropic's hidden Antspace PaaS. The specification revolution was declared. Comprehension debt was coined.

This week is **the reckoning**. The AI-accelerated software ecosystem discovered that speed without verification isn't just risky — it's actively dangerous. Three stories converge on the same lesson:

| Layer | Who | What Broke |
|-------|-----|------------|
| **Supply chain** | TeamPCP | Poisoned a security scanner (Trivy) to backdoor LiteLLM — est. 500K credentials stolen in 5.5 hours |
| **Model security** | Anthropic | Misconfigured CMS leaked ~3,000 internal documents including Claude Mythos, their most capable model |
| **Code quality** | SWE-CI paper | 75% of AI coding agents break previously working code during long-term maintenance |
| **Data trust** | GitHub | Opted all Copilot users into training data collection by default, triggering mass backlash |

The unifying thesis: **the tools are getting more powerful (Mythos, Auto Mode, autoresearch), but the guardrails aren't keeping pace.** A security scanner became a weapon. A CMS default exposed a frontier model. Agents that pass all tests still break code in production. GitHub assumed users would accept silent data collection.

The counterpoint is equally real: Anthropic shipped Auto Mode with a reasoning-blind classifier. Lovable integrated AI pentesting. The TDAD paper showed test-driven agent development cuts regressions by 70%. The builders are learning — but the lessons are being taught by incidents, not by foresight.

The deepest signal: **Karpathy's autoresearch** reframes the entire conversation. While practitioners debate whether AI coding agents are reliable enough for production, Karpathy ran 700 autonomous experiments and declared humans the bottleneck. The gap between "agents as coding assistants" and "agents as autonomous researchers" is closing faster than the safety infrastructure can follow.

---

## 1. The Supply Chain Reckoning — LiteLLM, Trivy, and the TeamPCP Campaign

### The Attack Chain
**March 19–24 | [LiteLLM Security Update](https://docs.litellm.ai/blog/security-update-march-2026) · [Snyk](https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/) · [Datadog Security Labs](https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-teampcp-supply-chain-campaign/) · [The Hacker News](https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html) · [Kaspersky](https://www.kaspersky.com/blog/critical-supply-chain-attack-trivy-litellm-checkmarx-teampcp/55510/) · [Wiz](https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign) · [SANS Institute](https://www.sans.org/blog/when-security-scanner-became-weapon-inside-teampcp-supply-chain-campaign)**

A threat group called **TeamPCP** turned a security scanner into a weapon — and used it to backdoor one of the most widely deployed AI proxy libraries in the world. The attack earned **CVE-2026-33634 (CVSS 9.4)** and represents the most sophisticated AI supply chain attack to date.

The timeline reads like a heist:

| Date | Step |
|------|------|
| **March 19** | TeamPCP compromised Aqua Security's `trivy-action` GitHub Action by force-pushing malicious commits to 76 of 77 release tags via a stolen `aqua-bot` service account. The poisoned binary harvested CI/CD secrets from every repository that ran Trivy. |
| **March 20** | Stolen npm tokens fed a self-propagating worm (**CanisterWorm**) that infected 66+ npm packages. |
| **March 23** | Checkmarx KICS GitHub Actions compromised via the same stolen CI/CD secrets. |
| **March 24** | LiteLLM's CI/CD pipeline pulled the compromised Trivy without version pinning, which exfiltrated the `PYPI_PUBLISH` token. Two backdoored versions (1.82.7 and 1.82.8) were published to PyPI. |

The malware was a three-stage payload:

1. **Credential harvesting** — environment variables, SSH keys, cloud credentials, Kubernetes data, Docker configs, shell history, CI/CD secrets, and crypto wallets
2. **Data exfiltration** — AES-256 + RSA-4096 hybrid encryption to `models.litellm[.]cloud`
3. **Persistence** — a systemd unit (`sysmon.service`) beaconing to `checkmarx[.]zone/raw`

The most insidious detail: the malware abused Python's `.pth` file mechanism to execute on **every Python invocation**, regardless of whether LiteLLM was imported. Install the package once, and every Python process on the machine becomes a credential harvester.

### Scale and Response

LiteLLM has approximately **95 million monthly PyPI downloads** and is present in **36% of cloud environments** according to Wiz Research. The compromised versions were live for approximately **5.5 hours** (10:39–16:00 UTC on March 24) before PyPI quarantined the package. An estimated **500,000 credentials were reportedly stolen** according to SlowMist's analysis.

The attackers used **ICP blockchain canisters** as command-and-control infrastructure — the first documented abuse of decentralized infrastructure for supply chain C2. When community members reported the compromise in GitHub issue #24512, attackers reportedly flooded the thread with bot comments from compromised accounts to suppress the discussion.

Post-attack, TeamPCP reportedly pivoted to active extortion, working through ~300 GB of stolen credentials and collaborating with the **LAPSUS$** extortion group. LiteLLM paused all new releases pending a full supply-chain review. Customers using the official Docker image were unaffected due to pinned dependencies.

### The Broader Pattern

The HiddenLayer 2026 AI Threat Landscape Report (March 19) found that **autonomous agents now account for more than 1 in 8 reported AI breaches**. Malware in public model and code repositories was the most cited breach source (35%), yet **93% of respondents still use open repositories**. The LiteLLM attack validates every concern in that report — and adds a new one: your security scanner can be the attack vector.

**Why this matters:** The AI ecosystem's dependency graph is now a target-rich environment. LiteLLM sits between AI applications and model providers — compromising it gives attackers access to API keys for OpenAI, Anthropic, Google, and every other LLM provider. The attack didn't exploit a bug in LiteLLM's code. It exploited the **trust chain** — an unpinned dependency on a security scanner that itself was compromised. The lesson: in the AI supply chain, the security tools are now attack surfaces.

---

## 2. The Mythos Leak — Anthropic's Next Frontier Exposed

**March 26 | [Fortune](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/) · [Fortune (cybersecurity)](https://fortune.com/2026/03/27/anthropic-leaked-ai-mythos-cybersecurity-risk/) · [The Decoder](https://the-decoder.com/anthropic-leak-reveals-new-model-claude-mythos-with-dramatically-higher-scores-on-tests-than-any-previous-model/) · [CoinDesk](https://www.coindesk.com/markets/2026/03/27/anthropic-s-massive-claude-mythos-leak-reveals-a-new-ai-model-that-could-be-a-cybersecurity-nightmare) · [WinBuzzer](https://winbuzzer.com/2026/03/27/anthropic-confirms-leaked-mythos-model-step-change-reasoning-xcxwbn/)**

A misconfigured content management system exposed nearly **3,000 internal Anthropic documents** to the public internet — including draft blog posts revealing a model Anthropic has never publicly acknowledged: **Claude Mythos** (internally also called **"Capybara"**).

The leak was discovered by security researchers **Roy Paz** (LayerX Security) and **Alexandre Pauwels** (University of Cambridge), who found that a default CMS setting automatically made uploaded files publicly accessible. Anthropic confirmed the leak the same day, calling Mythos a **"step change"** in AI capabilities and **"the most capable we've built to date."**

### What the Drafts Reveal

Mythos sits **above the existing Opus line** — a new tier entirely. The draft blog post states:

> "Compared to our previous best model, Claude Opus 4.6, Capybara gets dramatically higher scores on tests of software coding, academic reasoning, and cybersecurity, among others" — [Fortune](https://fortune.com/2026/03/26/anthropic-says-testing-mythos-powerful-new-ai-model-after-data-leak-reveals-its-existence-step-change-in-capabilities/#:~:text=dramatically%20higher%20scores%20on%20tests%20of%20software%20coding)

The cybersecurity angle is what makes this leak extraordinary. Internal documents describe Mythos as:

> "currently far ahead of any other AI model in cyber capabilities" — [Fortune](https://fortune.com/2026/03/27/anthropic-leaked-ai-mythos-cybersecurity-risk/#:~:text=currently%20far%20ahead%20of%20any%20other%20AI%20model%20in%20cyber%20capabilities)

And warn that it:

> "presages an upcoming wave of models that can exploit vulnerabilities in ways that far outpace the efforts of defenders" — [Fortune](https://fortune.com/2026/03/27/anthropic-leaked-ai-mythos-cybersecurity-risk/#:~:text=presages%20an%20upcoming%20wave%20of%20models)

### Cost and Release Strategy

The drafts acknowledge the model is **"very expensive for us to serve, and will be very expensive for our customers to use."** Anthropic says it's working to make it **"much more efficient before any general release."**

Current availability: early access with select customers focused on cybersecurity defense applications. The planned release strategy is cyber defense organizations first, broader availability later.

Two draft versions exist — one using "Mythos," the other "Capybara" — suggesting the final branding hadn't been decided when the documents leaked. Anthropic called them **"early drafts of content that were being considered for publication."**

### Market Reaction

The iShares Expanded Tech-Software Sector ETF (IGV) dropped nearly **3%** following the leak. Bitcoin fell to **$66,000**, partially attributed to concerns about AI cybersecurity capabilities.

### The Competitive Context

The timing is charged. OpenAI reportedly finished pretraining its own next-generation model (codenamed **"Spud"**) on March 25 — one day before the Mythos leak — and shut down Sora to free computing capacity. Both companies are racing ahead of planned 2026 IPOs, with Bloomberg reporting Anthropic is considering an IPO as soon as **October 2026**.

### The Irony

A company building frontier AI models — including one described as having unprecedented cybersecurity capabilities — got breached by a **CMS default setting**. The leak wasn't a sophisticated attack. It was a misconfiguration. The same class of vulnerability that AI pentesting tools like Lovable + Aikido (see [Section 5](#5-vibe-coding-gets-a-security-layer--lovable--aikido)) are designed to catch.

---

## 3. Claude Code Goes Autonomous — Auto Mode and Long-Running Harnesses

Two Anthropic engineering posts this week paint a picture of where autonomous coding is headed — and what breaks along the way.

### Auto Mode
**March 25 | [Anthropic Engineering](https://www.anthropic.com/engineering/claude-code-auto-mode) · [TechCrunch](https://techcrunch.com/2026/03/24/anthropic-hands-claude-code-more-control-but-keeps-it-on-a-leash/) · [SiliconANGLE](https://siliconangle.com/2026/03/24/anthropic-unchains-claude-code-auto-mode-allowing-choose-permissions/) · [Engadget](https://www.engadget.com/ai/anthropic-releases-safer-claude-code-auto-mode-to-avoid-mass-file-deletions-and-other-ai-snafus-142500615.html) · [The AI Insider](https://theaiinsider.tech/2026/03/25/anthropic-introduces-auto-mode-for-claude-to-advance-autonomous-ai-coding-with-built-in-safeguards/)**

The problem Auto Mode solves is surprisingly mundane: **users approve 93% of permission prompts**. That approval fatigue means the permission system protects against almost nothing while interrupting everything. Auto Mode replaces human approval with model-based classifiers that autonomously approve file edits and bash commands.

The architecture is a **two-layer defense**:

1. **Server-side prompt-injection probe** — scans tool outputs before they enter the agent's context, catching injected instructions from external content
2. **Transcript classifier** (running on Sonnet 4.6) — evaluates each action against decision criteria using a two-stage process: fast single-token filter, then chain-of-thought reasoning if flagged

The key design choice: the classifier is **reasoning-blind**. It sees only user messages and tool calls, never Claude's own reasoning. This prevents the agent from "talking the classifier into" allowing dangerous actions — a failure mode Anthropic observed during development.

**Safety backstop:** 3 consecutive denials or 20 total denials stops the model and escalates to human. In headless mode (`claude -p`), the process terminates entirely.

Anthropic disclosed the error rates openly: **0.4% false positive rate** (safe actions blocked) and **17% false-negative rate** (overeager actions allowed). The asymmetry is intentional — they'd rather let some borderline actions through than block legitimate workflows.

**How to enable:** `claude --enable-auto-mode` or toggle with **Shift+Tab** during a session. Available as a research preview on Claude Team plan, with Enterprise and API rollout planned shortly after.

### Harness Design for Long-Running Application Development
**March 24 | [Anthropic Engineering](https://www.anthropic.com/engineering/harness-design-long-running-apps)**

The companion post by **Prithvi Rajasekaran** describes what happens when you let Claude Code run for hours instead of minutes — and why a single agent fails at it.

The solution is a **three-agent architecture** inspired by GANs:

| Agent | Role |
|-------|------|
| **Planner** | Decomposes the user's request into structured sprints with acceptance criteria |
| **Generator** | Writes code, runs builds, iterates on implementation |
| **Evaluator** | Uses Playwright to interact with the live running app like a human QA engineer |

The GAN insight: separating generation from evaluation proved more effective than making generators self-critical. Left to evaluate their own work:

> "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work — even when, to a human observer, the quality is obviously mediocre" — [Anthropic Engineering](https://www.anthropic.com/engineering/harness-design-long-running-apps#:~:text=confidently%20praising%20the%20work)

The most surprising finding: **context anxiety**. Claude Sonnet 4.5 exhibited this so strongly that conversation compaction (summarizing earlier context) was insufficient — full **context resets** (clean-slate fresh conversations) were essential for sustained quality.

**Cost comparison:** A single agent produced a barely-functional prototype in 20 minutes for **$9**. The full harness ran for 6 hours, cost **$200**, and delivered a polished, genuinely useful application.

**Model evolution matters:** Moving from Sonnet 4.5 to Opus 4.6 allowed removing sprint decomposition entirely, since Opus 4.6 could sustain coherent work across a two-hour build without context degradation.

### The Autonomous Pipeline

Three Claude Code features shipped in March 2026 now form a **fully autonomous PR pipeline**: Code Review (catches issues), Auto Mode (acts without human approval), and Auto-Fix (generates fix PRs from review feedback). Combined with the harness architecture, Claude Code is no longer a coding assistant — it's an autonomous development system with multiple specialized agents, self-evaluation, and hours-long sustained execution.

---

## 4. The Data Training Backlash — GitHub Copilot Opts You In

**March 25 | [GitHub Blog](https://github.blog/news-insights/company-news/updates-to-github-copilot-interaction-data-usage-policy/) · [GitHub Changelog](https://github.blog/changelog/2026-03-25-updates-to-our-privacy-statement-and-terms-of-service-how-we-use-your-data/) · [The Register](https://www.theregister.com/2026/03/26/github_ai_training_policy_changes/) · [Help Net Security](https://www.helpnetsecurity.com/2026/03/26/github-copilot-data-privacy-policy-update/) · [HotHardware](https://hothardware.com/news/github-reverses-course-and-will-train-ai-on-your-copilot-data-unless-you-opt-out) · [Community Discussion #188488](https://github.com/orgs/community/discussions/188488)**

GitHub updated its Privacy Statement and Terms of Service to use Copilot interaction data for AI model training **by default** — a reversal from its previous opt-in stance. The change takes effect **April 24, 2026**.

### What's Collected

The scope is broad: inputs, outputs, code snippets, code context around the cursor, comments and documentation, file names, repository structure, navigation patterns, Copilot chat interactions, and feedback signals (thumbs up/down).

The **private repo nuance** is the part developers missed in the announcement: GitHub does not use private repository content *at rest* for training, but interaction data generated **while working in** a private repo — prompts, suggestions, code snippets during Copilot use — may be collected. The distinction between "your private code" and "your interaction with AI while editing private code" is thinner than it sounds.

### Who's Affected

| Tier | Opted In? |
|------|-----------|
| Free | **Yes**, by default |
| Pro | **Yes**, by default |
| Pro+ | **Yes**, by default |
| Business | No — exempt |
| Enterprise | No — exempt |
| Students | No — exempt |
| Teachers | No — exempt |

Data may be shared with GitHub affiliates including **Microsoft**. It will **not** be shared with third-party AI model providers.

### The Developer Reaction

The [GitHub community discussion](https://github.com/orgs/community/discussions/188488) tells the story:

- **172 downvotes** on the announcement
- **66 comments**, overwhelmingly negative
- **59 thumbs-down** emoji reactions vs. **3 rocket ships**
- The only endorsement came from **Martin Woodward**, GitHub's VP of Developer Relations

**Opt-out path:** Settings → Copilot → Features → Privacy → "Allow GitHub to use my data for AI model training" → set to "Disabled." Users who previously opted out of product improvement data collection retain that preference.

### The Pattern

This follows a familiar playbook: **Meta** began training on public Facebook and Instagram posts. **LinkedIn** opted users into AI training. **Reddit** licensed user content to Google. In each case, the platform changed defaults to opt-in rather than asking for consent.

The difference with GitHub: developers are the most privacy-aware user base on the internet, and code is among the most sensitive data a professional produces. The backlash was predictable, immediate, and quantifiable in that community discussion thread.

**Why this matters:** Developer trust in platforms is a finite resource. GitHub built Copilot's reputation partly on the promise that your code stays private. This policy change doesn't violate that promise technically — but it erodes it perceptibly. In a market where Cursor, Windsurf, and Claude Code are viable alternatives, trust erosion has competitive consequences.

---

## 5. Vibe Coding Gets a Security Layer — Lovable + Aikido

**March 24 | [Aikido Blog](https://www.aikido.dev/blog/lovable-aikido-pentesting) · [DEV Community](https://dev.to/solobillions/lovable-just-added-ai-pentesting-heres-what-it-means-for-every-other-vibe-coder-27ka) · [AiToolsBee](https://aitoolsbee.com/news/ai-pentesting-comes-to-lovable-with-aikido-agent-based-security/)**

Lovable integrated **Aikido's autonomous penetration testing** directly into its build flow — billed as **"the world's first penetration testing for vibe coding."**

### How It Works

Aikido deploys a **swarm of specialized agents** against your live application. They probe login flows, attempt to access other users' data, chain small weaknesses into exploit paths, test APIs, and adapt to app responses in real-time. The checks cover the OWASP Top 10, privilege escalation, and data exposure.

This complements Lovable's existing **Security Scanner**, which catches exposed secrets and misconfigured database policies before publishing. The distinction: the scanner is like code review for theoretical issues. Aikido shows **what a hacker can actually do** with the live app.

**Pricing:** $100 per test at launch, with periodic free **"Security Weekends."** Access via Settings → Connectors → Shared Connectors in the Lovable project.

### Why It Matters

Traditional pentests assume mature applications, dedicated security budgets, and weeks of lead time — none of which apply to vibe-coded apps. A month earlier, **Escape.tech** scanned 5,600 vibe-coded apps and found:

- **2,000+** vulnerabilities
- **400** exposed secrets
- **10.3%** of Lovable apps had critical Row-Level Security (RLS) flaws before version 2.0

The attack surface created by vibe coding is real and growing. Lovable's response — embedding automated pentesting into the platform itself — is the first serious attempt to close the gap. But it has a significant limitation: **it only protects apps built and hosted on Lovable.** If you migrate or use multiple tools, the protection doesn't follow.

**The bigger signal:** Security is becoming a platform-level feature, not a developer responsibility. As vibe coding lowers the barrier to building apps, the security floor has to rise with it — or the apps produced become a liability at scale.

---

## 6. The Regression Problem — Agents Break What They Fix

Two papers published in March converge on the same uncomfortable finding: AI coding agents that pass all tests on individual patches still break codebases over time. The question isn't whether agents can fix bugs — it's whether they can maintain software.

### SWE-CI: 75% Break Working Code
**March 4 | [arXiv:2603.03823](https://arxiv.org/abs/2603.03823) · [AwesomeAgents](https://awesomeagents.ai/news/alibaba-swe-ci-ai-coding-agents-long-term-maintenance/)**

Authors **Jialong Chen, Xander Xu** (equal contributors), **Hu Wei, Chuan Chen, Bing Zhao** (Sun Yat-sen University & Alibaba Group) built the first benchmark on the **Continuous Integration loop** — not isolated patches, but sequential commits to the same codebase over months.

The setup: **18 models from 8 providers** across **100 tasks drawn from 68 real Python repositories**, each spanning approximately **233 days and 71 consecutive commits**. The benchmark introduces **EvoScore**, a metric that penalizes short-term optimization and weights later iterations more heavily.

The results:

- **75% of AI coding agents** break previously working code during long-term maintenance — even when their patches initially pass all tests
- Only **two Claude Opus models** exceed a 50% zero-regression rate
- **Every other model** falls below 25%

The implication: passing tests on a single PR is necessary but radically insufficient. Codebases are evolving systems, and agents that optimize locally can degrade globally.

### TDAD: Test-Driven Agentic Development
**March 18 | [arXiv:2603.17973](https://arxiv.org/abs/2603.17973)**

Authors **Pepe Alonso and Victor A. Braberman** offer a mitigation: build a **dependency graph between source code and tests** so agents know which tests to verify before committing patches.

The results on SWE-bench Verified:

- **70% reduction** in test-level regressions (6.08% → 1.82%)
- Issue-resolution rate improved from **24% to 32%** when deployed as an agent skill

But the most provocative finding is the **TDD prompting paradox**: giving agents procedural TDD instructions *without* targeted test context actually **increased** regressions to 9.94% — worse than no intervention at all. Agents need to know **which tests** to check, not **how** to do TDD. Process without context is counterproductive.

### The Quality Data

Broader industry data reinforces the pattern:

- AI generates **42% of code** but correlates with **23.5% more incidents** and **30% higher failure rates**
- AI makes PR review times **91% longer** (more PRs, slower reviews) and slows experienced developers by **19%**

**Why this matters:** The AI coding debate has been stuck on "can agents write code?" The answer is clearly yes. The real question — "can agents maintain software?" — is getting its first rigorous answer, and it's a sobering one. The SWE-CI benchmark shifts the evaluation from "does this patch work?" to "does this patch work without breaking everything else?" That's the difference between a coding assistant and a software engineer.

---

## 7. Karpathy's AutoResearch — Humans Are the Bottleneck

**March 7–8 (released); March 23 (continued coverage) | [GitHub: karpathy/autoresearch](https://github.com/karpathy/autoresearch) · [VentureBeat](https://venturebeat.com/technology/andrej-karpathys-new-open-source-autoresearch-lets-you-run-hundreds-of-ai) · [Fortune (March 17)](https://fortune.com/2026/03/17/andrej-karpathy-loop-autonomous-ai-agents-future/) · [Fortune (March 21)](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/) · [WinBuzzer](https://winbuzzer.com/2026/03/23/karpathy-humans-bottleneck-ai-research-xcxwbn/) · [NextBigFuture](https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html)**

While practitioners debate whether AI coding agents are reliable enough for production (see [Section 6](#6-the-regression-problem--agents-break-what-they-fix)), Andrej Karpathy ran 700 autonomous experiments and declared humans the bottleneck.

### The Framework

**autoresearch** is a 630-line Python script (MIT License) that automates ML experimentation overnight. The loop: an AI agent modifies code → trains for 5 minutes → evaluates results → keeps or discards changes → repeats. That's approximately **12 experiments per hour, 100+ overnight**.

Over two continuous days, the agent conducted **700 experiments** and discovered **20 optimizations** that improved training time for a small language model by **11%**.

The key constraint — and what makes it work: a **single objectively testable metric**. The agent doesn't need to understand what "good code" looks like. It needs a number that goes up or down. This is why Janakiram MSV coined it the **"Karpathy Loop"**: agent + single metric + time limit.

### The Quotes

On March 23, Karpathy framed the thesis:

> "To get the most out of the tools that have become available now, you have to remove yourself as the bottleneck" — [WinBuzzer](https://winbuzzer.com/2026/03/23/karpathy-humans-bottleneck-ai-research-xcxwbn/#:~:text=remove%20yourself%20as%20the%20bottleneck)

In a Fortune interview from the No Priors podcast (March 21), he revealed he hasn't typed a line of code **"probably since December"**, calling it **"an extremely large change."** He described his current mindset:

> "I'm just like in the state of psychosis of trying to figure out what's possible, trying to push it to the limit" — [Fortune](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/#:~:text=state%20of%20psychosis)

On the relationship to historical neural architecture search:

> "Neural architecture search as it existed then is such a weak version of this that it's in its own category of totally useless by comparison. This is an *actual* LLM writing arbitrary code, learning from previous experiments, with access to the internet" — [NextBigFuture](https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html#:~:text=totally%20useless%20by%20comparison)

### The Scaling Vision

Karpathy's stated next step:

> "large-scale asynchronous collaboration between agents. Our goal is not to simulate a single PhD student, but to simulate a complete research community composed of countless PhD students" — [NextBigFuture](https://www.nextbigfuture.com/2026/03/andrej-karpathy-on-code-agents-autoresearch-and-the-self-improvement-loopy-era-of-ai.html#:~:text=simulate%20a%20complete%20research%20community)

### Community Response

- **58,000+ GitHub stars** and **8.6 million views** on the announcement within days
- **Varun Mathur** (CEO, Hyperspace AI) distributed the loop across a peer-to-peer network — on March 8–9, **35 autonomous agents** ran **333 experiments** completely unsupervised
- **Shopify CEO Tobias Lutke** reported a **19% performance gain** after 37 overnight experiments using autoresearch
- Karpathy also revealed **"Dobby the House Elf"** — a home automation agent that controls his home via WhatsApp

### The Tension

autoresearch works because ML training has a clean scalar metric. Most software engineering doesn't. The SWE-CI paper (Section 6) shows that agents struggle precisely where metrics are ambiguous — maintaining complex codebases where "correct" isn't a single number. Karpathy's loop is a proof of concept for domains with clear optimization targets. Extending it to general software development remains an open problem.

**Why this matters:** Karpathy isn't just proposing a tool — he's proposing a **workflow paradigm**. The human sets the objective function, the agents explore the search space. This inverts the traditional relationship: instead of humans writing code and AI assisting, humans define metrics and AI does all the work. For domains where that inversion is possible, the productivity gap between "human in the loop" and "human sets the loop" may be orders of magnitude.

---

## 8. Anthropic vs. The Pentagon — First Amendment Wins Round One

**March 26 | [CNBC](https://www.cnbc.com/2026/03/26/anthropic-pentagon-dod-claude-court-ruling.html) · [CNN](https://www.cnn.com/2026/03/26/business/anthropic-pentagon-injunction-supply-chain-risk) · [TechCrunch](https://techcrunch.com/2026/03/26/anthropic-wins-injunction-against-trump-administration-over-defense-department-saga/) · [NPR](https://www.npr.org/2026/03/26/nx-s1-5762971/judge-temporarily-blocks-anthropic-ban) · [Defense One](https://www.defenseone.com/policy/2026/03/judge-pentagon-anthropic-ban-retaliation/412463/)**

Federal judge **Rita F. Lin** (San Francisco) blocked the Pentagon from enforcing its ban on doing business with Anthropic, finding the government's actions constituted:

> "classic illegal First Amendment retaliation" — [CNBC](https://www.cnbc.com/2026/03/26/anthropic-pentagon-dod-claude-court-ruling.html#:~:text=classic%20illegal%20First%20Amendment%20retaliation)

And were:

> "arbitrary and capricious" — [CNN](https://www.cnn.com/2026/03/26/business/anthropic-pentagon-injunction-supply-chain-risk#:~:text=arbitrary%20and%20capricious)

The ruling's most quoted passage:

> "Nothing in the governing statute supports the Orwellian notion that an American company may be branded a potential adversary and saboteur of the U.S. for expressing disagreement with the government" — [NPR](https://www.npr.org/2026/03/26/nx-s1-5762971/judge-temporarily-blocks-anthropic-ban#:~:text=Orwellian%20notion)

### Background

Anthropic had a **$200 million Pentagon contract** but refused to allow Claude to be used for **fully autonomous weapons** or **domestic mass surveillance**. The Department of Defense then designated Anthropic as a **"supply chain risk"** — effectively blacklisting the company from all government contracts.

The judge found this designation was retaliation for Anthropic's public policy positions, not a legitimate security concern. The government has **7 days to appeal** to the Ninth Circuit.

### The Broader Context

This case sits at the intersection of AI ethics, defense procurement, and First Amendment law. It establishes a precedent: AI companies can set usage restrictions on their models without being designated as national security threats. The ruling doesn't say the Pentagon must use Claude — it says the Pentagon can't punish Anthropic for having principles about how Claude is used.

The timing — the same week as the Mythos leak — creates a striking juxtaposition. Anthropic is simultaneously fighting for the right to restrict its models' use in weapons systems while building a model described internally as having unprecedented cybersecurity capabilities. The company is navigating the tension between capability and responsibility in real-time, in public, with legal force behind both sides.

---

## 9. The Voice Tracker — Who Said What

### Simon Willison — Supply Chain Security Week
**Very active | [simonwillison.net](https://simonwillison.net/)**

Willison's week was dominated by the LiteLLM supply chain attack. Multiple posts:

- **March 24** — Linked Andrew Nesbitt's [Package Managers Need to Cool Down](https://simonwillison.net/2026/Mar/24/package-managers-need-to-cool-down/) — arguing for dependency cooldown periods before installing updated packages, directly inspired by the LiteLLM attack.
- **March 25** — Covered both the **LiteLLM hack analysis** (46,996 downloads of exploited packages in 46 minutes) and **Claude Code Auto Mode** (new permissions mode as alternative to `--dangerously-skip-permissions`). Also linked to [Thoughts on slowing the fuck down](https://simonwillison.net/2026/Mar/25/thoughts-on-slowing-the-fuck-down/) via Mario Zechner on agentic engineering trends.
- **March 26** — [My minute-by-minute response to the LiteLLM malware attack](https://simonwillison.net/2026/Mar/26/response-to-the-litellm-malware-attack/) — Callum McMahon's Claude transcripts used during the vulnerability response. Also linked [Quantization from the ground up](https://simonwillison.net/2026/Mar/26/quantization-from-the-ground-up/) — Sam Rose's interactive essay on LLM quantization.
- **March 27** — "Vibe coding SwiftUI apps is a lot of fun"

**Theme:** The security tools are now the attack surface. Willison's cooldown proposal is the most concrete policy response to emerge from the LiteLLM incident.

### Addy Osmani — The Code Agent Orchestra
**Active | [addyosmani.com](https://addyosmani.com/blog/)**

- **March 26** — Co-hosted the third **O'Reilly AI CodeCon: Software Craftsmanship in the Age of AI**. His talk "[Orchestrating Coding Agents](https://talks.addy.ie/oreilly-codecon-march-2026/)" covered three tiers of agentic tools (single-agent, multi-agent local, cloud-based) and coordination patterns.

> "Almost nobody's figured out how to make everything work together as smoothly as possible. [...] And that's the actual hard problem here. Not generation, but coordination" — [Addy Osmani](https://www.oreilly.com/radar/what-developers-actually-need-to-know-right-now/#:~:text=Not%20generation%2C%20but%20coordination)

Published the companion blog post "[The Code Agent Orchestra](https://addyosmani.com/blog/code-agent-orchestra/)" — key finding: **three focused agents consistently outperform one generalist agent working three times as long.**

### Martin Fowler — Both Booster and Doomer
**Active | [martinfowler.com](https://martinfowler.com/)**

- **March 26** — Published a Fragment discussing Anthropic's study interviewing ~80,000 users about AI opinions. Key insight: people are not neatly divided into optimist/pessimist camps but:

> "organized around what they value — financial security, learning, human connection — watching advancing AI capabilities while managing both hope and fear at once" — [martinfowler.com](https://martinfowler.com/fragments/2026-03-26.html#:~:text=organized%20around%20what%20they%20value)

His personal stance: asked whether he's an AI booster or doomer, he answers **"yes"** — both fascinated and worried:

> "powerful technologies rarely yield simple consequences" — [martinfowler.com](https://martinfowler.com/fragments/2026-03-26.html#:~:text=powerful%20technologies%20rarely%20yield%20simple%20consequences)

- **March 24** — Published on **Architecture Decision Records (ADRs)**: writing them "helps clarify thinking, particularly with groups of people."

### Andrej Karpathy — Autoresearch Continues
**Active | [GitHub](https://github.com/karpathy/autoresearch) · [Fortune](https://fortune.com/2026/03/21/andrej-karpathy-openai-cofounder-ai-agents-coding-state-of-psychosis-openclaw/) · [WinBuzzer](https://winbuzzer.com/2026/03/23/karpathy-humans-bottleneck-ai-research-xcxwbn/)**

See [Section 7](#7-karpathys-autoresearch--humans-are-the-bottleneck) for full coverage. Key quotes this week: **"humans are the bottleneck"** and **"state of psychosis of trying to figure out what's possible."**

### Kent Beck — Nobody Knows
**Active | [tidyfirst.substack.com](https://tidyfirst.substack.com/)**

- **~March 25** — "[Nobody Knows](https://tidyfirst.substack.com/p/nobody-knows)" — kicks off a new series called **"Still Burning"** — "Honest conversations about fear, uncertainty, and what it means to build things when the ground keeps shifting." From the episode: "Old skills are losing leverage, and nobody has the answers."

Ongoing themes: AI as an "unpredictable genie," TDD as a superpower when working with agents, and **"programming deflation"** — knowing what's worth building becomes the scarce skill.

### Kelsey Hightower — KubeCon EU Amsterdam
**Present | [CNCF](https://www.cncf.io/blog/2025/08/05/kubecon-cloudnativecon-europe-2026-returning-to-amsterdam-23-26-march/)**

- **March 23–26** — Present at **KubeCon + CloudNativeCon Europe 2026** in Amsterdam (13K+ attendees from 100+ countries). Participated in the opening session. The event spotlighted GitOps, service mesh patterns, real-world AI integration, and cost-aware observability.

### Daniel Stenberg — NTLM, the Beast
**Active | [daniel.haxx.se](https://daniel.haxx.se/)**

- **March 22** — Blog post on NTLM authentication: **"The NTLM authentication method was always a beast."** NTLM broke the HTTP paradigm by authenticating the connection instead of the request, indirectly causing many security issues. curl has recorded **seven past security vulnerabilities** in NTLM-related code. He wrote the original curl NTLM implementation in 2003.
- **March 26** — curl virtual meeting.
- **March 27** — HTTP/3 talk for the scania.js user group in Stockholm.

### Mitchell Hashimoto — AI Bug Fix Economics
**Earlier March, discussed this week | [Medium](https://medium.com/@andreangeorgiev/ai-made-us-faster-did-it-make-us-better-2166e140038e)**

Used Codex 5.3 to fix a six-month-old Ghostty GTK4 flicker bug. The AI found the root cause in GNOME's C source code in **45 minutes for $4.14**. Hashimoto described it as an **80/20 split**: AI handled 80% (synthesizing thousands of lines of GTK4 source, tracing commits, identifying root cause) while he handled 20% (review, judgment, cleanup). But the AI also **quietly introduced two new bugs** while fixing the hard one.

Updated Ghostty's AI contribution policy:

> "AI assisted PRs are now only allowed for accepted issues. Drive-by AI PRs will be closed without question. Bad AI drivers will be banned from all future contributions" — [Mitchell Hashimoto on X](https://x.com/mitchellh/status/2014433315261124760)

Also: appointed to **Vercel's board of directors** (March 18) at the company's $9.3B valuation.

### Voices Not Active This Week

No confirmed March 22–29 posts from: **Steve Yegge**, **Gergely Orosz**, **Ethan Mollick**, **Grady Booch**, **Patrick Debois**, **Charity Majors**, **Dave Farley**, **DHH**, **ThePrimeagen**, **Bryan Cantrill**, **Jaana Dogan**, **Mike Mason**, **Max Woolf**, **Chelsea Troy**.

*Note: Yegge and Orosz had major pieces earlier in March (Yegge on "eight levels of AI adoption" and the Pragmatic Engineer podcast; Orosz's Steve Yegge interview). Debois presented at Sonar Summit. These are noted for continuity but fall outside the March 22–29 window.*

---

## 10. The Jobs Escalation Continues — CFOs Admit 9x

**March 24 | [Fortune](https://fortune.com/2026/03/24/cfo-survey-ai-job-cuts-productivity-paradox-2026/) · [TechTimes](https://www.techtimes.com/articles/315282/20260321/tech-layoffs-surge-while-ai-jobs-soar-key-trends-shaping-2026-tech-industry.htm) · [IBTimes](https://www.ibtimes.co.uk/ai-driven-layoffs-2026-tech-sector-1788111) · [CNN](https://www.cnn.com/2026/03/02/business/ai-tech-jobs-layoffs)**

The layoff numbers keep climbing, but this week's Fortune CFO survey added a new dimension: the people controlling budgets are privately planning much deeper cuts than public statements suggest.

### The Numbers

| Metric | Figure |
|--------|--------|
| Tech workers laid off in 2026 YTD | **~55,000–60,000** (varies by tracker) |
| Directly attributed to AI/automation | **~9,200** (~1 in 5) |
| Pace vs. 2025 | Running ahead of full-year total of 245,953 |

### Major Cuts

- **Amazon** — ~16,000 cuts YTD (2,700 from cloud operations)
- **Block** — 4,000 layoffs (**40% of workforce**) to "move faster with smaller teams using AI"
- **Atlassian** — 1,600 layoffs (10% of workforce) announced March 11
- **Google** — 1,200 roles eliminated in advertising
- **Microsoft** — 800 program managers cut
- **Meta** — Reportedly considering cuts of up to 15,000

### The CFO Survey

The Fortune CFO survey (March 24) contains the week's most alarming data point: employers reported approximately **55,000 AI-attributed layoffs** in 2025. CFOs privately expect a **9x increase** in AI-related layoffs this year.

- **55%** of hiring managers expect layoffs at their companies
- **44%** identified AI as the primary driver

### The Counterbalance

AI jobs are booming with **56% wage premiums**. Fastest-growing roles: AI safety researchers, enterprise AI strategists, human-AI interaction designers.

The pattern is now unmistakable: AI creates fewer, more expensive jobs while eliminating more, less expensive ones. The net effect on total employment is negative, but the effect on total payroll may be neutral — or even positive. The question is whether the workers displaced can transition to the new roles. The CFO survey suggests the industry isn't waiting to find out.

---

## 11. Model & Tool Updates — Footnotes

### OpenAI Shuts Down Sora
**March 24 | [TechCrunch](https://techcrunch.com/2026/03/24/openais-sora-was-the-creepiest-app-on-your-phone-now-its-shutting-down/) · [CNN](https://edition.cnn.com/2026/03/24/tech/openai-sora-video-app-shutting-down) · [CNBC](https://www.cnbc.com/2026/03/24/openai-shutters-short-form-video-app-sora-as-company-reels-in-costs.html) · [Variety](https://variety.com/2026/digital/news/openai-shutting-down-sora-video-disney-1236698277/)**

Sam Altman announced the shutdown of Sora, just six months after launch. The numbers: **$15 million/day** in inference costs against only **$2.1 million in total lifetime revenue**. Disney, which had signed a three-year deal and committed **$1 billion** to OpenAI, terminated its partnership. Compute redirected toward robotics and the mysterious successor codenamed **"Spud."** Multiple competitors (Runway Gen-4, Kling 3.0, Google Veo 3.1) had already matched or exceeded Sora's quality.

### JetBrains 2026.1 — The Agentic IDE Wave
**March 26 | [JetBrains Blog](https://blog.jetbrains.com/idea/2026/03/intellij-idea-2026-1/) · [DevClass](https://www.devclass.com/ai-ml/2026/03/26/jetbrains-shifts-to-agentic-dev-with-central-retires-pair-programming/5211637)**

JetBrains shipped 2026.1 across IntelliJ IDEA, GoLand, CLion, and other IDEs with a major theme: **open AI agent integration**.

- **Agent Client Protocol (ACP)** support — Cursor, Copilot, Codex, Claude Agent, and dozens of external agents now work natively via one-click install from the new ACP Registry
- **Junie CLI** (Beta) — LLM-agnostic coding agent usable from terminal, any IDE, CI/CD, and GitHub/GitLab
- **BYOK** (Bring Your Own Key) — connect personal OpenAI or Anthropic accounts without a JetBrains AI subscription
- **Code With Me sunset** — 2026.1 is the last version to support the human pair programming feature, as JetBrains shifts fully to agentic development with its upcoming **"Central"** platform

The Code With Me sunset is symbolically loaded: JetBrains is retiring its *human* pair programming tool to make room for *agent* pair programming. The transition from human-to-human collaboration to human-to-agent collaboration is now explicit in product strategy.

### AI Bots Surpass Human Internet Traffic
**March 26 | [CNBC](https://www.cnbc.com/2026/03/26/ai-bots-humans-internet.html) · [TechCrunch](https://techcrunch.com/2026/03/19/online-bot-traffic-will-exceed-human-traffic-by-2027-cloudflare-ceo-says/)**

HUMAN Security's State of AI Traffic report confirmed automated traffic has officially eclipsed human users. Key numbers: automated traffic grew **23.5% YoY** vs. 3.1% for humans. AI agent traffic exploded **7,851%**. LLM traffic (ChatGPT, Claude, Gemini) grew **187%** in 2025. Cloudflare CEO Matthew Prince predicted bot traffic will exceed human traffic by 2027 — it arrived early.

### Google Gemini — Chat History Import & Free Code Assist
**March 26 | [Bloomberg](https://www.bloomberg.com/news/articles/2026-03-26/google-gemini-adds-tool-to-make-it-easier-to-switch-from-chatgpt) · [Google Blog](https://blog.google/innovation-and-ai/technology/developers-tools/gemini-code-assist-free/)**

Google released tools letting Gemini users upload chat history from ChatGPT and Claude — a direct play to capture switchers. Separately, **Gemini Code Assist became fully free** for individual developers with **180,000 code completions/month** (vs. typical 2,000 on free tiers), working across VS Code, JetBrains, and Android Studio.

### Cursor
**[Fortune](https://fortune.com/2026/03/21/cursor-ceo-michael-truell-ai-coding-claude-anthropic-venture-capital/) · [WinBuzzer](https://winbuzzer.com/2026/03/20/cursor-unveils-composer-2-for-cheaper-ai-coding-xcxwbn/)**

- **Composer 2 model** (March 20) — Cursor's own AI model for multi-file edits, priced below rivals
- **Self-hosted cloud agents** (March 25) — code, build outputs, and secrets stay on internal machines
- **Bugbot Autofix** — graduated from reviewer to fixer, **35%+ of suggestions merged**
- **$2B annualized revenue** (Feb 2026), doubling from $1B in 3 months. 2M+ total users, 1M+ paying

### Windsurf
**[Windsurf Changelog](https://windsurf.com/changelog)**

- Now owned by **Cognition AI** after ~$250M acquisition (Dec 2025)
- **Pricing change** (March 19) — credit-based to quota-based billing with daily/weekly refresh limits, triggering significant user backlash
- 1M+ active users, 70M+ lines of AI-written code daily

### Model Releases
- **Mistral Voxtral TTS** (March 26) — open-source text-to-speech, 9 languages, small enough for a smartwatch — [TechCrunch](https://techcrunch.com/2026/03/26/mistral-releases-a-new-open-source-model-for-speech-generation/)
- **NVIDIA Nemotron 3** — open-weight leader at 60.47% SWE-bench Verified — [NVIDIA](https://nvidianews.nvidia.com/news/nvidia-debuts-nemotron-3-family-of-open-models)
- **Xiaomi MiMo-V2-Pro** — 1T parameters, 1M context, agent-focused
- **Alibaba Qwen 3.5 Small** — 9B model scores 81.7 on GPQA Diamond, Apache 2.0

### Copilot Updates
- **Agentic Code Review** (March 5) — full project context analysis, auto-generates fix PRs
- **Coding agent** starts 50% faster, adds semantic code search
- **Student plan** updated (March 13) with new model lineup
- **CLI v1.0.12** (March 26) — lower memory, `/undo` command, multi-session support

### Claude Code Rate Limit Controversy
**March 26 | [MacRumors](https://www.macrumors.com/2026/03/26/claude-code-users-rapid-rate-limit-drain-bug/)**

Users flooded GitHub and Reddit reporting sessions burning out in minutes instead of hours. Anthropic confirmed they were **"adjusting 5-hour session limits during peak hours."** The rate limit controversy coincided with the Auto Mode launch, creating a perception gap: Anthropic shipped autonomous capabilities while simultaneously throttling the resources needed to use them.

### Policy
- **White House National AI Policy Framework** (March 20) — 7 pillars, federal preemption of state laws, industry-led standards — [White House](https://www.whitehouse.gov/wp-content/uploads/2026/03/03.20.26-National-Policy-Framework-for-Artificial-Intelligence-Legislative-Recommendations.pdf)
- **EU AI Act** — Council agreed March 13 to streamline rules, extending high-risk AI timeline by 16 months — [EU Council](https://www.consilium.europa.eu/en/press/press-releases/2026/03/13/council-agrees-position-to-streamline-rules-on-artificial-intelligence/)

---

## 12. Signals & Radar

### Critical Signals 🔴

| Signal | Evidence |
|--------|----------|
| **Supply chain attacks now chain through security tools** | TeamPCP weaponized Trivy (a security scanner) to backdoor LiteLLM. The tools meant to protect the ecosystem became the attack vector. |
| **Frontier model details leaked via basic misconfiguration** | Anthropic's CMS default exposed ~3,000 internal documents including Claude Mythos. No sophisticated attack — just a setting left on "public." |

### Warning Signals 🟠

| Signal | Evidence |
|--------|----------|
| **75% agent regression rate in long-term maintenance** | SWE-CI paper shows agents that pass all tests still break codebases over time. Only Claude Opus exceeds 50% zero-regression. |
| **Platform data defaults eroding developer trust** | GitHub opted all Copilot users into training data collection. 172 downvotes, near-universal community backlash. |
| **Rate limit throttling undermines autonomous capabilities** | Anthropic shipped Auto Mode while simultaneously throttling session limits during peak hours. |
| **Sora's $15M/day cost collapse** | OpenAI shut down Sora after six months — inference costs 7x higher than total lifetime revenue. Economics of large generative models remain brutal. |

### Emerging Signals 🟢

| Signal | Evidence |
|--------|----------|
| **AI pentesting for vibe-coded apps** | Lovable + Aikido: automated security testing integrated into the build flow. $100/test. |
| **Reasoning-blind classifiers for agent safety** | Claude Code Auto Mode uses a classifier that can't see the agent's reasoning — preventing self-justification of dangerous actions. |
| **Autonomous research loops entering production** | Karpathy's autoresearch: 700 experiments, 11% speedup. Shopify CEO reports 19% gains. Varun Mathur ran 35 agents on 333 experiments unsupervised. |
| **Three-agent architecture for sustained coding** | Anthropic's Planner/Generator/Evaluator pattern enables 6-hour coherent sessions at $200. |
| **Agent coordination > agent generation** | Osmani: "Not generation, but coordination" is the hard problem. Three focused agents outperform one generalist. |
| **Human pair programming → agent pair programming** | JetBrains sunsets Code With Me, replaces with ACP agent integration. The product strategy is now explicit. |

### Watch Signals 🔵

| Signal | Evidence |
|--------|----------|
| **Anthropic IPO timeline** | Bloomberg reports October 2026 consideration. |
| **Pentagon appeal in Ninth Circuit** | Government has 7 days to appeal Judge Lin's injunction. Precedent for AI company usage restrictions at stake. |
| **Mythos/Capybara general availability** | Anthropic working to make it "much more efficient" before release. Timeline unknown. |
| **AI bots > human traffic** | HUMAN Security confirms automated traffic eclipsed human users. AI agent traffic grew 7,851% YoY. |
| **Google's free Gemini Code Assist** | 180K completions/month free — 90x the typical free tier. Pricing pressure on Copilot, Cursor, Windsurf. |

---

## Key Quotes of the Week

> "To get the most out of the tools that have become available now, you have to remove yourself as the bottleneck"
> — **Andrej Karpathy** · [WinBuzzer](https://winbuzzer.com/2026/03/23/karpathy-humans-bottleneck-ai-research-xcxwbn/)

> "Nothing in the governing statute supports the Orwellian notion that an American company may be branded a potential adversary and saboteur of the U.S. for expressing disagreement with the government"
> — **Judge Rita F. Lin** · [NPR](https://www.npr.org/2026/03/26/nx-s1-5762971/judge-temporarily-blocks-anthropic-ban)

> "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work — even when, to a human observer, the quality is obviously mediocre"
> — **Anthropic Engineering** · [Anthropic](https://www.anthropic.com/engineering/harness-design-long-running-apps)

> "Almost nobody's figured out how to make everything work together as smoothly as possible. [...] And that's the actual hard problem here. Not generation, but coordination"
> — **Addy Osmani** · [O'Reilly Radar](https://www.oreilly.com/radar/what-developers-actually-need-to-know-right-now/)

> "Powerful technologies rarely yield simple consequences"
> — **Martin Fowler** · [martinfowler.com](https://martinfowler.com/fragments/2026-03-26.html)

> "AI assisted PRs are now only allowed for accepted issues. Drive-by AI PRs will be closed without question. Bad AI drivers will be banned from all future contributions"
> — **Mitchell Hashimoto** · [X](https://x.com/mitchellh/status/2014433315261124760)

> "Old skills are losing leverage, and nobody has the answers — not even the people who've been doing this for 30 years"
> — **Kent Beck** · [Tidy First?](https://tidyfirst.substack.com/p/nobody-knows)

---

## Voice Tracker Table

| Voice | Active This Week | Key Topic | Source |
|-------|-----------------|-----------|--------|
| Simon Willison | ✅ Mar 22–27 | Supply chain cooldown, LiteLLM response, Auto Mode | [simonwillison.net](https://simonwillison.net/) |
| Addy Osmani | ✅ Mar 26 | Code Agent Orchestra, O'Reilly AI CodeCon | [addyosmani.com](https://addyosmani.com/blog/code-agent-orchestra/) |
| Martin Fowler | ✅ Mar 24, 26 | Anthropic AI study, ADRs, "both booster and doomer" | [martinfowler.com](https://martinfowler.com/) |
| Andrej Karpathy | ✅ Mar 23 | AutoResearch, "humans are bottleneck", "state of psychosis" | [WinBuzzer](https://winbuzzer.com/2026/03/23/karpathy-humans-bottleneck-ai-research-xcxwbn/) |
| Kent Beck | ✅ ~Mar 25 | "Nobody Knows" / Still Burning series | [tidyfirst.substack.com](https://tidyfirst.substack.com/) |
| Kelsey Hightower | ✅ Mar 23–26 | KubeCon EU Amsterdam | [CNCF](https://www.cncf.io/) |
| Daniel Stenberg | ✅ Mar 22, 26, 27 | NTLM beast, curl meeting, HTTP/3 talk | [daniel.haxx.se](https://daniel.haxx.se/) |
| Mitchell Hashimoto | 📌 Earlier Mar | Ghostty AI bug fix ($4.14), Vercel board, AI PR policy | [X](https://x.com/mitchellh/) |
| Steve Yegge | ❌ | (Mar 11: Pragmatic Engineer podcast, "eight levels") | — |
| Gergely Orosz | ❌ | (Mar 11: Steve Yegge interview) | — |
| Ethan Mollick | ❌ | (Mar 12: "Shape of the Thing") | — |
| Grady Booch | ❌ | (Mar 19: InfoWorld profile) | — |
| Patrick Debois | ❌ | (Mar: Sonar Summit, Context Flywheel) | — |
| Charity Majors | ❌ | (Mar 9: SRECon, "clarity is the scarce resource") | — |
| Dave Farley | ❌ | (Feb: Aviator podcast, "bigger than agile") | — |
| DHH | ❌ | — | — |
| ThePrimeagen | ❌ | (Mar 20: The Standup #050) | — |
| Bryan Cantrill | ❌ | — | — |
| Jaana Dogan | ❌ | — | — |
| Mike Mason | ❌ | — | — |
| Max Woolf | ❌ | — | — |
| Chelsea Troy | ❌ | — | — |
| Clive Thompson | 📌 Earlier Mar | (Mar 12: NYT Magazine "Coding After Coders") | — |

---

