## 3. Anthropic's Three-Bug Postmortem — When "Nerfing" Was Actually Engineering Debt

**April 23 | [Anthropic Engineering](https://www.anthropic.com/engineering/april-23-postmortem#:~:text=update%20on%20recent%20Claude%20Code%20quality%20reports) · [The Register](https://www.theregister.com/2026/04/23/anthropic_says_it_has_fixed/#:~:text=Anthropic%20admits%20it%20dumbed%20down%20Claude) · [Kingy AI](https://kingy.ai/ai/clients-were-right-anthropic-admits-claude-code-got-dumber-not-claude-post-mortem/#:~:text=Clients%20Were%20Right) · [Livemint](https://www.livemint.com/technology/tech-news/did-anthropic-dumb-down-claude-code-post-mortem-reveals-the-three-bugs-that-crippled-performance-11777013226388.html#:~:text=three%20bugs%20that%20crippled%20performance)**

**Anthropic** published a detailed engineering postmortem on April 23, confirming what **Claude Code** users had been reporting for seven weeks: the model *was* getting dumber — but not because anyone touched the weights. Three independent product-layer changes, introduced between **March 4 and April 16**, compounded into what felt like a systematic intelligence downgrade across **Claude Code**, **Agent SDK**, and **Cowork**. The core inference API and direct model access were never affected.

### The Three Bugs

| # | Change | Introduced | Fixed | Duration | Root Cause |
|---|--------|-----------|-------|----------|------------|
| 1 | **Reasoning effort downgrade** | Mar 4 | Apr 7 | 34 days | Default silently switched from `high` → `medium` to reduce UI-freezing latency spikes |
| 2 | **Cache-clearing bug** | Mar 26 | Apr 10 | 15 days | Optimization to clear stale thinking state after idle sessions instead cleared it *every turn* |
| 3 | **Verbosity-reduction prompt** | Apr 16 | Apr 20 | 4 days | System prompt capped responses at ~25 words between tool calls, starving reasoning bandwidth |

The timeline matters. Bug 1 ran solo for **22 days** before Bug 2 stacked on top of it. For the **12-day overlap** between March 26 and April 7, users experienced *both* reduced reasoning depth and aggressive context amnesia — making the model appear forgetful, repetitive, and incapable of maintaining coherent multi-step plans. Bug 1 was fixed April 7; Bug 2 continued alone until April 10. Then, just six days after Bug 2 was fixed, Bug 3 arrived and re-introduced a different flavor of degradation. The cumulative effect: from March 4 through April 20, there was **not a single day** when Claude Code ran without at least one active regression.

### The Wrong Tradeoff

The reasoning effort change was an intentional product decision, not an accident. Anthropic's engineering team explained that `high` reasoning effort sometimes caused latency severe enough to make the Claude Code UI appear frozen, burning through usage limits faster than users expected. Their fix — silently lowering the default — traded intelligence for responsiveness.

> "On March 4, we changed Claude Code's default reasoning effort from high to medium to reduce the very long latency — enough to make the UI appear frozen — some users were seeing in high mode. **This was the wrong tradeoff.** We reverted this change on April 7 after users told us they'd prefer to default to higher intelligence and opt into lower effort for simple tasks."
>
> — [Anthropic Engineering](https://www.anthropic.com/engineering/april-23-postmortem#:~:text=This%20was%20the%20wrong%20tradeoff)

The cache-clearing bug was more insidious. An optimization designed to clear Claude's internal thinking state from sessions idle for over an hour contained a logic error that triggered the clearing **every conversational turn** for the remainder of the session. The result: Claude lost track of its own reasoning history mid-conversation, producing the exact "amnesia" symptoms users described — wrong tool calls, repeated work, and inexplicable context loss. Because the bug's severity varied by session length and idle patterns, it appeared inconsistent across users and evaded internal evaluations.

The verbosity prompt, introduced on April 16 — the [same day Opus 4.7 launched](../9982-2026-04-11-ai-news-feed/README.md#13-breaking--claude-opus-47-ships-today) — was the shortest-lived but perhaps most revealing failure. Quick internal evals showed no degradation, but real-world multi-session coding work exposed a **~3% performance drop** on coding tasks. The lesson: synthetic benchmarks and spot-checks missed what sustained professional use caught immediately.

### What Was NOT the Problem

Anthropic was explicit: **model weights were never changed**. The underlying Claude models — including the freshly-launched Opus 4.7 — performed identically throughout. Every regression traced to the product orchestration layer: default parameter choices, caching logic, and system prompt engineering. The distinction matters because it separates this incident from the recurring "silent nerfing" narrative that has plagued every major AI lab. This wasn't throttling, cost-cutting, or capability degradation at the model level. It was, in Anthropic's framing, engineering debt compounding faster than their evaluation infrastructure could catch it.

### Community Reaction: Vindication, Then Praise

The developer community's response came in two waves. First, vindication. For weeks, users reporting degradation had been met with suggestions to adjust their `/effort` settings or told the issues were subjective. **Kingy AI** captured the mood with its headline: ["Clients Were Right: Anthropic Admits Claude Code Got Dumber"](https://kingy.ai/ai/clients-were-right-anthropic-admits-claude-code-got-dumber-not-claude-post-mortem/#:~:text=Clients%20Were%20Right). **The Register** was less diplomatic: ["Anthropic admits it dumbed down Claude with 'upgrades'"](https://www.theregister.com/2026/04/23/anthropic_says_it_has_fixed/#:~:text=Anthropic%20admits%20it%20dumbed%20down%20Claude).

Then came the second wave: genuine praise for the postmortem's transparency. Unlike vague acknowledgments common in the industry, Anthropic published specific dates, technical root causes, and an unambiguous admission of fault. As a goodwill measure, the company [reset usage limits](https://www.livemint.com/technology/tech-news/did-anthropic-dumb-down-claude-code-post-mortem-reveals-the-three-bugs-that-crippled-performance-11777013226388.html#:~:text=usage%20limits%20reset) for all subscribers — a concrete acknowledgment that users had burned through caps on a degraded product.

### Why This Matters

This postmortem is the clearest evidence yet that **the product layer around a model can matter as much as the model itself**. Opus 4.7's weights were world-class throughout this entire episode — and it didn't matter, because the orchestration code between the user and the model was silently sabotaging every interaction. For engineering teams building on AI APIs, the lesson is sobering: your model provider's product decisions — default parameters, caching strategies, system prompts — are invisible dependencies that can degrade your application without warning and without any change to the model you're calling. The fix isn't just better evals. It's treating product-layer changes with the same rigor as model deployments — because to the user, they're indistinguishable.
