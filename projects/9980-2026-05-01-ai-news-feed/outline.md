# AI × Software Engineering — Edition 9 Story Tracker

## Date Window: April 25 – May 1, 2026

> This is the main tracking document. Each story is a task. Sub-agents gathered facts, sources, and key quotes below. Status: ✅ = facts gathered, 🔍 = needs fact-check, ⚠️ = confidence concern.

---

## 🔴 TIER 1 — Lead Stories (Deep Dives)

### - [x] Story: Mini Shai-Hulud Supply Chain Worm (PyTorch Lightning + intercom-client + SAP)
- **Status:** ✅ Facts gathered
- **Date:** April 29–30, 2026
- **Sources:**
  - https://www.aikido.dev/blog/pytorch-lightning-pypi-compromise-mini-shai-hulud
  - https://www.kodemsecurity.com/resources/mini-shai-hulud-strikes-pytorch-lightning-and-intercom-client-inside-the-cross-ecosystem-supply-chain-attack
  - https://www.theregister.com/2026/04/30/supply_chain_attacks_sap_npm_packages
  - https://thehackernews.com/2026/04/pytorch-lightning-compromised-in-pypi.html
  - https://github.com/intercom/intercom-node/security/advisories/GHSA-54pg-9963-v8vg
- **Key Facts:**
  - PyTorch Lightning (`lightning` PyPI) v2.6.2 and 2.6.3 compromised — 8.3M monthly downloads
  - npm `intercom-client@7.0.4` compromised April 30, removed ~2 hours later
  - SAP Cloud Application Programming Model npm packages also hit
  - Injected via `__init__.py`; spawns background thread → downloads Bun JS runtime + 11MB obfuscated payload
  - Steals: SSH keys, AWS/GCP/Azure creds, GitHub/npm tokens, crypto wallets, VPN creds, Discord/Slack sessions
  - Worm propagation: harvests GitHub tokens, commits worm across up to 50 branches per repo, impersonates "Anthropic Claude Code" identity
  - Attribution: threat actor "TeamPCP"
  - Signature: "A Mini Shai-Hulud has Appeared"
- **Confidence:** high 🔍

### - [x] Story: OpenAI Ends Microsoft Azure Exclusivity → Models on AWS Bedrock
- **Status:** ✅ Facts gathered
- **Date:** April 28, 2026
- **Sources:**
  - https://www.cnbc.com/2026/04/28/openai-brings-models-to-aws-after-ending-exclusivity-with-microsoft.html
- **Key Facts:**
  - Ended ~7-year exclusive hosting agreement with Microsoft Azure
  - GPT-5.5, Codex, and frontier models now on Amazon Bedrock (limited preview)
  - Reported $38–50B multi-year cloud commitment with AWS
  - Microsoft retains "primary" partner status via non-exclusive license through 2032
  - New "Bedrock Managed Agents" service for OpenAI-powered agents
- **Confidence:** high 🔍

### - [x] Story: Mistral Medium 3.5 — 128B Dense Open-Weight Flagship + Vibe Coding Agents
- **Status:** ✅ Facts gathered
- **Date:** April 29, 2026
- **Sources:**
  - https://pulse24.ai/news/2026/4/29/23/mistral-ai-ships-medium-35-model
  - DEV Community, TestingCatalog, AIHola
- **Key Facts:**
  - 128B dense model, 256K context, open weights (modified MIT)
  - Self-hostable on 4 GPUs
  - Replaces Medium 3.1, Magistral, and Devstral 2
  - SWE-Bench Verified: 77.6%; τ³-Telecom: 91.4
  - API pricing: $1.50/$7.50 per million tokens
  - Simultaneously launched **Vibe** remote coding agents — async parallel coding sessions
  - New "Work mode" in Le Chat
- **Confidence:** high 🔍

### - [x] Story: OpenAI Misses Q1 Revenue & User Growth Targets → AI Stock Selloff
- **Status:** ✅ Facts gathered
- **Date:** April 28, 2026
- **Sources:**
  - https://www.cnbc.com/2026/04/28/openais-revenue-growth-estimates-fall-short-report.html
  - https://www.cnbc.com/2026/04/27/stock-market-today-live-updates.html
- **Key Facts:**
  - Failed to meet internal Q1 2026 revenue goals
  - Missed 1B weekly active ChatGPT users target
  - $600B+ committed infrastructure spending (incl. $300B Oracle deal)
  - CFO Sarah Friar raised affordability concerns
  - Triggered selloff: ARM −8%, Nvidia −1.6%, Oracle −4%, Nasdaq −0.9%
  - Increased ChatGPT Plus subscriber churn reported
- **Confidence:** high 🔍

### - [x] Story: US House Investigation into PRC AI Model Security (Cursor/Anysphere & Airbnb)
- **Status:** ✅ Facts gathered
- **Date:** April 29, 2026
- **Sources:**
  - https://homeland.house.gov/2026/04/29/chairmen-garbarino-moolenaar-announce-joint-investigation-into-national-security-risks-posed-by-prc-ai-models/
  - https://www.semafor.com/article/04/29/2026/house-committee-probes-cursor-parent-airbnb-over-chinese-ai
  - https://www.nextgov.com/artificial-intelligence/2026/04/house-panels-probe-airbnb-anysphere-over-use-chinese-ai-models/413207/
- **Key Facts:**
  - Joint probe: Homeland Security Committee + Select Committee on China
  - Letters sent to Anysphere (Cursor) and Airbnb
  - Focus: Cursor's Composer 2 built on Kimi (Moonshot AI, Beijing)
  - Concerns: unauthorized model distillation, IP theft, safety guardrail stripping
  - Follows White House memo on PRC industrial-scale distillation
- **Confidence:** high 🔍

### - [x] Story: Musk v. OpenAI Trial Begins (Sam Altman, $130B Lawsuit)
- **Status:** ✅ Facts gathered
- **Date:** April 27–28, 2026
- **Sources:**
  - https://www.cnbc.com/2026/04/28/openai-trial-elon-musk-sam-altman-live-updates.html
- **Key Facts:**
  - Jury selection began April 27 in Oakland
  - Musk testified April 28
  - Centers on OpenAI's nonprofit-to-profit conversion
  - $130B damages claimed
  - Altman released "AGI principles" April 26 ahead of trial
  - Expected witnesses: Satya Nadella, Ilya Sutskever
- **Confidence:** high 🔍

---

## 🟡 TIER 2 — Section-worthy Stories

### - [x] Story: Cursor SDK Public Beta — TypeScript Library for Programmatic AI Agents
- **Status:** ✅ Facts gathered
- **Date:** April 29, 2026
- **Sources:**
  - https://www.marktechpost.com/2026/04/29/cursor-introduces-a-typescript-sdk-for-building-programmatic-coding-agents-with-sandboxed-cloud-vms-subagents-hooks-and-token-based-pricing/
- **Key Facts:**
  - `@cursor/sdk` — TypeScript library for programmatic coding agents
  - Supports local, Cursor cloud VMs, or self-hosted workers
  - Compatible with Composer-2, GPT-4, Claude, custom models
  - Can open PRs, push branches, connect MCP tools, run hooks, spawn subagents
  - Token-based pricing
- **Confidence:** high

### - [x] Story: GitHub Copilot in Visual Studio — Cloud Agent + Debugger Agent
- **Status:** ✅ Facts gathered
- **Date:** April 30, 2026
- **Sources:**
  - https://github.blog/changelog/2026-04-30-github-copilot-in-visual-studio-april-update/
  - https://devblogs.microsoft.com/visualstudio/visual-studio-april-update-cloud-agent-integration/
- **Key Facts:**
  - Cloud agent: "Assign task, close IDE, get PR"
  - Runs via GitHub Actions-backed infrastructure
  - New Debugger Agent validates bug fixes against live runtime
  - User-level custom agents in `%USERPROFILE%/.github/agents/`
  - "Copilot cloud agent" rebrand
- **Confidence:** high

### - [x] Story: CVE-2026-26268 — Critical RCE in Cursor via Git Hooks
- **Status:** ✅ Facts gathered
- **Date:** April 28, 2026 (disclosure wave)
- **Sources:**
  - https://novee.security/blog/cursor-ide-cve-2026-26268-git-hook-arbitrary-code-execution/
  - https://hackread.com/cursor-ai-ide-vulnerability-code-execution-git-hooks/
  - https://www.csoonline.com/article/4164250/critical-cursor-bug-could-turn-routine-git-into-rce.html
- **Key Facts:**
  - CVSS 9.9 (Critical); versions prior to 2.5
  - Malicious bare git repository with pre-commit hook
  - AI agent autonomously triggers git operations → executes hook without user interaction
  - Patched in Cursor v2.5 (February 2026); full disclosure April 28
- **Confidence:** high

### - [x] Story: Anthropic Launches Claude Security (AI Vulnerability Scanner)
- **Status:** ✅ Facts gathered
- **Date:** April 30, 2026
- **Sources:**
  - https://www.securityweek.com/anthropic-unveils-claude-security-to-counter-ai-powered-exploit-surge/
  - https://siliconangle.com/2026/04/30/anthropic-announces-claude-security-public-beta-find-fix-software-vulnerabilities/
- **Key Facts:**
  - Public beta for Claude Enterprise customers, powered by Opus 4.7
  - Scans repos/branches; traces data flows (not just pattern matching)
  - Confidence-rated findings with reproduction paths and patches
  - Partners: CrowdStrike, Microsoft Security, Palo Alto Networks, SentinelOne, Wiz
  - Available via Claude.ai sidebar
- **Confidence:** high

### - [x] Story: Google Cloud Managed MCP Servers GA — 50+ Servers
- **Status:** ✅ Facts gathered
- **Date:** April 28, 2026
- **Sources:**
  - https://cloud.google.com/blog/products/ai-machine-learning/google-managed-mcp-servers-are-available-for-everyone
- **Key Facts:**
  - 50+ Google-managed MCP servers GA
  - Cover BigQuery, Cloud Storage, Firestore, Vertex AI, etc.
  - Supported by Gemini CLI, Claude, ChatGPT, LangChain
  - Built-in Cloud IAM, audit logging, centralized discovery
  - Protocol governed by Agentic AI Foundation (AAIF) under Linux Foundation
- **Confidence:** high

### - [x] Story: Apple CLAUDE.md Leak in Support App
- **Status:** ✅ Facts gathered
- **Date:** April 30, 2026
- **Sources:**
  - https://tech.yahoo.com/ai/claude/articles/apple-using-claude-inside-company-114500152.html
  - https://onejailbreak.com/blog/apple-accidentally-revealed-using-claude-ai/
- **Key Facts:**
  - Apple Support iOS app v5.13 shipped two internal CLAUDE.md config files
  - Reveals internal AI system codenamed "Juno AI"
  - Shows: Swift actors, AsyncStream, Keychain session persistence, "SAComponents" UI library
  - Silent 5.13.1 hotfix issued; no public statement
  - No user data leaked — engineering practices exposed
- **Confidence:** high

### - [x] Story: IBM Launches "IBM Bob" — AI-First Enterprise Development Partner
- **Status:** ✅ Facts gathered
- **Date:** April 28, 2026
- **Sources:**
  - https://newsroom.ibm.com/2026-04-28-introducing-ibm-bob-ai-development-partner-that-takes-enterprises-from-ai-assisted-coding-to-production-ready-software
- **Key Facts:**
  - Orchestrates full SDLC: planning, coding, testing, deployment, modernization
  - 80,000+ IBM employees using it internally
  - Average 45% productivity gain (internal survey)
  - Case study: 30-day Java upgrade → 3 days (160+ hours saved)
  - Multi-model orchestration: routes across LLMs, open-source, Granite models
- **Confidence:** high

### - [x] Story: AWS "What's Next" Event — Amazon Quick, NEURA Robotics
- **Status:** ✅ Facts gathered
- **Date:** April 28, 2026
- **Sources:**
  - https://aws.amazon.com/blogs/aws/top-announcements-of-the-whats-next-with-aws-2026/
- **Key Facts:**
  - Amazon Quick: AI work assistant, integrates Google Workspace/Teams/Slack/Dropbox
  - Amazon Connect expanded: 4 vertical AI-agent solutions (Decisions, Talent, Customer, Health)
  - NEURA Robotics partnership for Physical AI at scale
  - Event co-headlined by AWS + OpenAI leadership
- **Confidence:** high

### - [x] Story: Meta Cuts 8,000 Jobs to Fund $115–145B AI Push
- **Status:** ✅ Facts gathered
- **Date:** April 25, 2026
- **Sources:**
  - https://finance.biggo.com/news/202604260222_Meta-cuts-8000-jobs-for-AI
  - https://tech.yahoo.com/general/article/tech-layoffs-2026-meta-cuts-8000-employees-now-up-to-115000-people-have-been-laid-off-across-tech-industries-this-year-144545072.html
- **Key Facts:**
  - ~8,000 employees laid off (~10% workforce); notifications May 20
  - 6,000 open reqs frozen
  - Record Q1: $56.31B revenue, $26.8B net income
  - 2026 AI capex: $115–145B (double 2025)
  - Severance: 16 weeks + 2/year of service
  - YTD tech layoffs hit 115K (up from 92K in one week)
- **Confidence:** high

### - [x] Story: Hugging Face LeRobot CVE-2026-25874 — Unauthenticated RCE
- **Status:** ✅ Facts gathered
- **Date:** April 28–29, 2026
- **Sources:**
  - https://thehackernews.com/2026/04/critical-cve-2026-25874-leaves-hugging.html
  - https://www.resecurity.com/en/blog/article/cve-2026-25874-hugging-face-lerobot-unauthenticated-rce-via-pickle-deserialization
- **Key Facts:**
  - CVSS 9.3–9.8; unsafe `pickle.loads()` on unauthenticated gRPC
  - All versions through 0.5.1 affected; unpatched at disclosure
  - gRPC uses `add_insecure_port()` — no TLS/auth by default
  - Impact: full server compromise, potential physical safety risk (robotics)
- **Confidence:** high

### - [x] Story: Anthropic 9 Claude Connectors for Creative Tools
- **Status:** ✅ Facts gathered
- **Date:** April 28, 2026
- **Sources:**
  - https://9to5mac.com/2026/04/28/anthropic-releases-9-new-claude-connectors-for-creative-tools-including-blender-and-adobe/
- **Key Facts:**
  - Nine connectors: Blender, Adobe Creative Cloud, Affinity, Ableton, Autodesk Fusion, SketchUp, Resolume, Splice
  - Enable Claude to automate creative workflows via native app APIs
  - Available in Claude Desktop + API
- **Confidence:** high

---

## 🟢 TIER 3 — Briefs / Model Updates / Signals

### - [x] Story: Claude Code v2.1.126 (May 1) — Project Purge, OAuth, Windows
- **Key Facts:** `claude project purge`, smarter `/model` picker, OAuth paste, PowerShell 7 default, images >2000px auto-downscale
- **Confidence:** high

### - [x] Story: Cursor v3.2.16 — Security Review Agents (Beta)
- **Key Facts:** Always-on Security Reviewer + Vulnerability Scanner on PRs; integrates with SAST/SCA
- **Confidence:** med

### - [x] Story: Flowise CVE-2026-40933 — CVSS 10.0 RCE via MCP
- **Key Facts:** Versions through 3.0.13; command injection via custom MCP server config; patched in 3.1.0
- **Confidence:** high

### - [x] Story: Google Antigravity Prompt Injection → RCE (Disclosed)
- **Key Facts:** `find_by_name` parameter injection bypasses Secure Mode; native tools execute before sandbox; patched Feb, disclosed April 28
- **Confidence:** high

### - [x] Story: Apple CEO Transition (Cook → Ternus) Strategy Analysis
- **Key Facts:** Cook steps down April 20, Ternus effective Sept 1; hardware-AI convergence focus; $1B Gemini/Siri deal stays
- **Confidence:** high

### - [x] Story: DeepSeek V4 Open-Source Adoption Wave
- **Key Facts:** V4-Pro 1.6T total / 49B active; V4-Flash 284B / 13B active; Apache 2.0; ~1/20th cost of Opus 4.7
- **Confidence:** med (release was April 24; adoption week is new)

### - [x] Story: Deloitte "State of AI in the Enterprise 2026"
- **Key Facts:** 23% agentic today → 74% in 2 years; only 25% moved ≥40% experiments to production; 84% have NOT redesigned jobs for AI
- **Confidence:** high

### - [x] Story: Microsoft Build 2026 (June 2–3) Preview
- **Key Facts:** Ocean 11 autonomous agents, multi-model Copilot (Claude + MAI), Azure AI Studio GA
- **Confidence:** high

### - [x] Story: Google I/O 2026 (May 19–20) Preview
- **Key Facts:** Gemini 4.0, Gemini Nano 4, Android 17, Aluminum OS, Veo 4
- **Confidence:** med

### - [x] Story: Nebius Acquires Eigen AI ($643M)
- **Key Facts:** AI infrastructure M&A continues; Yandex-spinoff strengthens cloud/AI capabilities
- **Confidence:** med

### - [x] Story: Meta Acquires Assured Robot Intelligence
- **Key Facts:** Robotics AI startup; team joins Meta Superintelligence Labs; terms undisclosed
- **Confidence:** med

### - [x] Story: Opus 4.7 Reaches 83.5% SWE-bench — New Coding SOTA
- **Key Facts:** Surpasses GPT-5.4 (76.9%), Gemini 3.1 Pro (75.6%); GPT-5.5 leads ARC-AGI 2 at 85%
- **Confidence:** med

### - [x] Story: Gemini Robotics 1.5 → 1.6 Transition
- **Key Facts:** 1.5-preview shut down April 30; users directed to 1.6-preview
- **Confidence:** high

### - [x] Story: Gemini Chat-Based File Generation
- **Key Facts:** Generates PDFs, Word, Excel, Slides directly from chat; competes with Canvas/Artifacts
- **Confidence:** med

---

## 🗣️ VOICE TRACKER

### Active (April 25–May 1)

| Voice | Topic | Date | Source |
|-------|-------|------|--------|
| Karpathy | Agentic engineering at Sequoia AI Ascent | May 1 | franksworld.com |
| Simon Willison | OpenAI/Microsoft AGI clause + LLM 0.32a0 | Apr 27, 29 | simonwillison.net |
| Sam Altman | Musk trial + AGI principles | Apr 26–28 | CNBC |
| Gergely Orosz | AI changing OS/Ubuntu | Apr 28 | Pragmatic Engineer |
| Swyx | Physical AI episode (Applied Intuition) | Apr 27 | Latent Space podcast |
| Martin Fowler | Harness engineering for coding agents | Apr 29 | martinfowler.com/fragments |
| Ethan Mollick | AI reproducibility of academic papers | Apr 25 | One Useful Thing |
| Daniel Stenberg | "High Quality Chaos" + foss-north talk | Apr 28, 30 | daniel.haxx.se |
| Kent Beck | "Genies" framework — AI coding hygiene | ~May 1 | vladikk.com reference |
| Bryan Cantrill | "False productivity" essay (circulating) | ~Apr 13+ | simonwillison.net |
| Addy Osmani | AEO + Agent Skills open source | Late Apr | searchengineland.com |
| Kelsey Hightower | "Everyone is junior at AI" | Apr 2026 | theregister.com |

### Inactive (no dated April 25–May 1 content confirmed)
- Marc Andreessen, Theo Browne, Steve Yegge, Kent C. Dodds, Guillermo Rauch, Aaron Levie, Teresa Torres, DHH, Chelsea Troy

---

## 📄 RESEARCH PAPERS

| Paper | arXiv ID | Key Finding | Date |
|-------|----------|-------------|------|
| TDD Governance | 2604.26615 | Governance-as-code for multi-agent LLM pipelines | Apr 29 |
| Agentic AI in SDLC | 2604.26275 | SWE-bench 1.96%→78.4%; 13–56% time savings | Apr 29 |
| Claw-Eval-Live | 2604.28139 | Best model only 66.7% on real business workflows | Apr 30 |
| Test Before You Deploy | 2604.27789 | LLM supply chain governance framework | Apr 30 |
| AI-Assisted Code Review | 2604.23251 | PR volume doubled; ~33% comment action rate | Apr 25 |
| RecursiveMAS | 2604.25917 | Latent-space multi-agent: −35–76% tokens, +8.3% accuracy | Apr 28 |
| DEFault++ | 2604.28118 | Transformer fault detection AUROC >0.96 | Apr 28 |
| Circuit-to-Verilog | 2604.27969 | Multimodal grounding for hardware code gen | Apr 28 |

---

## 📊 SECTION ASSIGNMENT (Draft)

| § | Section | Key Stories |
|---|---------|-------------|
| 1 | Narrative | Theme synthesis — all stories |
| 2 | Deep Dive: Supply Chain Siege | Mini Shai-Hulud, Flowise CVE, LeRobot CVE, prompt injection→RCE |
| 3 | Deep Dive: OpenAI's Multi-Front Week | Azure exclusivity ends, revenue miss, Musk trial, stock selloff |
| 4 | Deep Dive: Mistral Medium 3.5 & Coding Agent Wars | Mistral, Cursor SDK, IBM Bob, VS Cloud Agent |
| 5 | Deep Dive: The Congressional Probe | PRC AI investigation, Apple CLAUDE.md leak, security context |
| 6 | Deep Dive: Managed MCP & Enterprise Infrastructure | Google MCP GA, AWS event, Claude Security |
| 7 | Deep Dive: Layoffs & the AI Capex Paradox | Meta 8K, 115K YTD, Deloitte report |
| 8 | Research & Data | Papers (8 papers), SWE-bench scores |
| 9 | Voice Tracker | 12 active voices |
| 10 | Model & Tool Updates | Opus 83.5%, DeepSeek V4 adoption, Gemini updates, Claude Code, Connectors |
| 11 | Jobs & Economic Impact | Layoff stats, funding, M&A |
| 12 | Signals & Radar | Regulatory, market, tech signals |

---

## Notes

- **Mega news day April 28:** OpenAI multi-cloud, AWS event, IBM Bob, Cursor CVE disclosure, Hugging Face CVE, AI stock selloff — all on the same day
- **Theme candidates:** "The Great Unbundling" (OpenAI leaves Azure, everyone goes multi-model), "Attack Surface Week" (supply chain worms + CVEs + Congressional probe), "April 28" (the day everything dropped)
- **Overlap with previous edition:** Meta layoffs were mentioned briefly in Apr 17-24 as "Meta + Microsoft 20K+"; the specific 8K figure, severance terms, and May 20 date are new this week
