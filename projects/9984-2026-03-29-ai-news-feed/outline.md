# Edition Outline — March 22–29, 2026

## Section 1: The Supply Chain Reckoning — LiteLLM, Trivy, and the TeamPCP Campaign
- TeamPCP attack timeline: March 19 (Trivy compromise) → March 24 (LiteLLM backdoored)
- CVE-2026-33634 (CVSS 9.4), 5.5 hours on PyPI, ~500K credentials stolen
- Three-stage payload: credential harvester, K8s lateral movement, systemd persistence
- .pth file trick — executes on ANY Python invocation
- ICP blockchain canisters as C2 — first documented use
- 88 bot comments from 73 compromised accounts to suppress GitHub issue discussion
- LAPSUS$ collaboration, ~300GB stolen credentials
- Broader context: HiddenLayer report — 1 in 8 companies had AI breaches
- Voice: Simon Willison on supply chain trust (if available)

## Section 2: The Mythos Leak — Anthropic's Next Frontier Exposed
- March 26: misconfigured CMS leaked ~3,000 internal documents
- Claude Mythos / Capybara — new tier ABOVE Opus
- "Dramatically higher scores on software coding, academic reasoning, cybersecurity"
- "Currently far ahead of any other AI model in cyber capabilities"
- "Very expensive to serve" — working on efficiency before general release
- Two draft versions (Mythos vs Capybara naming)
- Market reaction: IGV ETF dropped ~3%, Bitcoin dropped to $66K
- Discovered by Roy Paz (LayerX) and Alexandre Pauwels (Cambridge)
- Context: OpenAI finished pretraining "Spud" on March 25
- Anthropic IPO consideration (Bloomberg, October 2026)
- Security irony: the company building frontier AI models got breached by a CMS default

## Section 3: Claude Code Goes Autonomous — Auto Mode and Long-Running Harnesses
### Auto Mode (March 25)
- Model-based classifiers auto-approve file edits and bash commands
- 93% of permission prompts were approved → approval fatigue
- Two-layer defense: server-side prompt-injection probe + transcript classifier (Sonnet 4.6)
- Reasoning-blind classifier — can't see Claude's own reasoning
- 3 consecutive denials or 20 total → escalate to human
- 0.4% false positive, 17% false negative (disclosed openly)
- Enable: `claude --enable-auto-mode` or Shift+Tab
- Research preview on Team plan

### Harness Design for Long-Running Apps (March 24)
- Anthropic engineering blog by Prithvi Rajasekaran
- Three-agent architecture: Planner, Generator, Evaluator
- GAN-inspired: separate generation from evaluation
- "Context anxiety" — Sonnet 4.5 needed full context resets, not just compaction
- Self-evaluation failure: "agents confidently praise mediocre work"
- Cost: single agent $9/20min (barely functional) vs full harness $200/6hr (polished)
- Opus 4.6 removed need for sprint decomposition — sustained 2-hour coherent sessions
- Evaluator uses Playwright to interact with live running app

### Other Claude Code updates
- `--bare` flag for scripted calls
- `--channels` permission relay for phone-based approval
- Claude Apps: interactive apps for iOS/Android

## Section 4: The Data Training Backlash — GitHub Copilot Opts You In
- March 25 announcement, effective April 24, 2026
- Default opt-IN for Free, Pro, Pro+ users
- Data collected: inputs, outputs, snippets, context, file names, repo structure, chat interactions
- Private repo nuance: interaction data while working in private repos IS collected
- Exempt: Business, Enterprise, students, teachers
- May share with Microsoft affiliates
- Community reaction: 172 downvotes, 66 negative comments, 59 thumbs-down
- Only GitHub VP Martin Woodward endorsed the change
- Opt-out path available but buried in settings
- Context: follows pattern of platform data grabs (Meta, LinkedIn, Reddit)
- Voice: developer trust erosion narrative

## Section 5: Vibe Coding Gets a Security Layer — Lovable + Aikido
- March 24: Lovable integrates Aikido autonomous pentesting
- "World's first penetration testing for vibe coding"
- Swarm of specialized agents probe live app: login flows, data access, API testing
- OWASP Top 10, privilege escalation, data exposure
- $100/test, periodic free "Security Weekends"
- Context: Escape.tech scanned 5,600 vibe-coded apps → 2,000+ vulns, 400 exposed secrets
- 10.3% of Lovable apps had critical RLS flaws before v2.0
- Limitation: only protects apps on Lovable platform
- Complements existing Security Scanner (code review vs live attack)

## Section 6: The Regression Problem — Agents Break What They Fix
### SWE-CI Paper (March 4, arXiv)
- 75% of AI coding agents break previously working code during maintenance
- First benchmark on Continuous Integration loop
- 18 models, 8 providers, 100 Python repos, ~233 days, ~71 commits each
- EvoScore metric — penalizes short-term optimization
- Only two Claude Opus models exceed 50% zero-regression rate
- Every other model below 25%

### TDAD Paper (March 18, arXiv)
- Test-Driven Agentic Development with graph-based impact analysis
- 70% reduction in test-level regressions (6.08% → 1.82%)
- TDD prompting paradox: procedural TDD instructions WITHOUT targeted test context INCREASED regressions to 9.94%
- Agents need to know WHICH tests to check, not HOW to do TDD
- Improved issue-resolution from 24% to 32%

### Broader quality data
- AI generates 42% of code but correlates with 23.5% more incidents
- 30% higher failure rates
- AI speeds reviews by 91% but slows experienced devs by 19%

## Section 7: Karpathy's AutoResearch — Humans Are the Bottleneck
- Released March 7-8, continued coverage through March 22-29
- 630-line Python script, MIT license
- Agent modifies code → train 5 min → evaluate → keep/discard → repeat
- ~12 experiments/hour, 100+ overnight
- 700 experiments over two days, 20 optimizations, 11% training speed gain
- March 23: "To get the most out of the tools, you have to remove yourself as the bottleneck"
- "State of psychosis of trying to figure out what's possible"
- Hasn't typed a line of code "probably since December"
- The "Karpathy Loop": agent + single metric + time limit
- Scaling vision: "simulate a complete research community"
- 21K GitHub stars, 8.6M views
- Varun Mathur: 35 autonomous agents ran 333 experiments unsupervised
- Shopify CEO Lutke: 19% performance gain after 37 overnight experiments
- Dobby the House Elf — home automation agent via WhatsApp

## Section 8: Anthropic vs. The Pentagon — First Amendment Wins Round One
- March 26: Federal judge Rita F. Lin blocks Pentagon ban
- "Classic illegal First Amendment retaliation"
- "Arbitrary and capricious"
- "Nothing in the governing statute supports the Orwellian notion..."
- Background: $200M contract, Anthropic refused autonomous weapons + domestic surveillance
- DOD designated Anthropic as "supply chain risk"
- Government has 7 days to appeal to Ninth Circuit
- Broader context: AI companies navigating defense/ethics tensions

## Section 9: The Voice Tracker — Who Said What
### Active this week (March 22-29):
- **Martin Fowler** (Mar 26): Anthropic's 80K user study — "powerful technologies rarely yield simple consequences", answers "yes" to both booster and doomer. Also ADR piece (Mar 24).
- **Andrej Karpathy** (Mar 23): "humans are the bottleneck", autoresearch, "state of psychosis"
- **Kelsey Hightower** (Mar 23-26): KubeCon EU Amsterdam, 13K+ attendees
- **Daniel Stenberg** (Mar 22): NTLM authentication post, 7 curl CVEs from NTLM code. Mar 26 curl meeting, Mar 27 HTTP/3 talk.
- **Mitchell Hashimoto** (earlier March, discussed this week): Vercel board appointment, Ghostty AI bug fix ($4.14, 45 min), AI PR policy update

### Check remaining agents for:
- Simon Willison, Addy Osmani, Gergely Orosz, Steve Yegge
- Kent Beck, Ethan Mollick, Grady Booch, Patrick Debois
- Charity Majors, Dave Farley, DHH

## Section 10: The Jobs Escalation Continues — CFOs Admit 9x
- 59,121 tech workers laid off in 2026 YTD (704/day)
- 1 in 5 directly attributed to AI/automation (~9,200)
- Major cuts: Amazon 16K, Block 4K (40%), Atlassian 1.6K, Google 1.2K, Microsoft 800
- Meta considering up to 15K
- Fortune CFO survey (Mar 24): expect 9x increase in AI layoffs vs 2025
- 55% of hiring managers expect layoffs; 44% cite AI as primary driver
- Counterbalance: AI jobs booming with 56% wage premiums
- Fastest-growing: AI safety researchers, enterprise AI strategists

## Section 11: Model & Tool Updates — Footnotes
### Cursor
- Composer 2 model (Mar 20): own AI model for multi-file edits
- JetBrains integration via ACP (Mar 4)
- Self-hosted cloud agents (Mar 25)
- Bugbot Autofix: 35%+ suggestions merged
- $2B ARR, 2M+ users, 1M+ paying

### Windsurf
- Now owned by Cognition AI after ~$250M acquisition
- Pricing change (Mar 19): credit-based → quota-based, user backlash
- 1M+ active users, 70M+ lines AI code daily

### Model releases
- Claude 4.6 Opus: 75.6% SWE-bench, 1M context (beta)
- Gemini 3.1 Pro: 77.1% ARC-AGI-2
- Mistral Voxtral TTS (Mar 26): open-source speech, 9 languages
- NVIDIA Nemotron 3: open-weight leader at 60.47% SWE-bench
- Xiaomi MiMo-V2-Pro: 1T params, 1M context

### Copilot updates
- Agentic Code Review (Mar 5)
- Coding agent 50% faster startup
- Student plan update (Mar 13)
- CLI v1.0.12 (Mar 26)

### Policy
- White House National AI Policy Framework (Mar 20): 7 pillars, federal preemption
- EU AI Act Council position (Mar 13)

## Section 12: Signals & Radar
- 🔴 Critical: Supply chain attacks now chain through security tools themselves
- 🔴 Critical: Frontier model details leaked via basic infrastructure misconfiguration
- 🟠 Warning: 75% agent regression rate in long-term maintenance
- 🟠 Warning: Platform data training defaults eroding developer trust
- 🟢 Emerging: AI pentesting for vibe-coded apps
- 🟢 Emerging: Reasoning-blind classifiers for autonomous agent safety
- 🟢 Emerging: Autonomous research loops (Karpathy) entering production
- 🔵 Watch: Anthropic IPO timeline (October 2026)
- 🔵 Watch: Pentagon appeal in Ninth Circuit
- 🔵 Watch: Mythos/Capybara general availability timeline

## Key Quotes of the Week
- "To get the most out of the tools, you have to remove yourself as the bottleneck" — Karpathy
- "Nothing in the governing statute supports the Orwellian notion..." — Judge Rita F. Lin
- "When asked to evaluate work they've produced, agents tend to respond by confidently praising the work" — Anthropic
- "Powerful technologies rarely yield simple consequences" — Fowler
- TBD from remaining agent results

## Voice Tracker Table
- Full 23-voice table with status, last post date, key topic
