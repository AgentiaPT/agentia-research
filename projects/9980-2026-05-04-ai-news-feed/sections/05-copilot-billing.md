## 5. GitHub Copilot's Billing Earthquake — From Flat Subscriptions to Pay-Per-Token

**April 27 | [GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) · [Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx) · [InfoWorld](https://www.infoworld.com/article/4164236/github-shifts-copilot-to-usage-based-billing-signaling-new-cost-model-for-enterprise-ai-tools.html)**

On April 27, GitHub CPO Mario Rodriguez announced Copilot moves to **usage-based billing on June 1, 2026**. The flat "all-you-can-eat" era is over.

**What's Changing**

A new currency — **GitHub AI Credits** (1 credit = $0.01) — replaces premium request units. Every chat message, agentic session, CLI query, and code review costs credits based on token consumption.

- **Base prices unchanged:** Pro $10/mo, Pro+ $39/mo, Business $19/user/mo, Enterprise $39/user/mo
- **Credit allotments match plan price:** Pro gets 1,000 credits, Pro+ 3,900, Business 1,900/user, Enterprise 3,900/user
- **Code completions and Next Edit remain unlimited**
- **When credits run out, usage stops** — no fallback to cheaper models
- **Overage option:** orgs can allow pay-per-credit overage OR enforce a hard cap

**Token Rates by Model**

- **GPT-4.1 / GPT-4o** — $2.00 input / $8.00 output per 1M tokens
- **Claude Sonnet 4/4.5/4.6** — $3.00 input / $15.00 output per 1M tokens
- **Claude Opus** — ~$15.00 input / ~$75.00 output per 1M tokens

Practical example: 100K input + 20K output on Claude Sonnet 4.6 ≈ 60 credits ($0.60). A few heavy agentic sessions per day could exhaust the Pro monthly allotment.

**The Dual-Billing Problem**

Starting June 1, **Copilot code review on private repos consumes both AI Credits AND GitHub Actions minutes** — billed twice for the same feature. Public repos exempt. Architecturally justified (runs on Actions runners), but punishing for teams doing heavy AI-assisted PR review.

**Timeline**

- **~April 20** — GitHub pauses new sign-ups; tightens session limits
- **April 27** — Official announcement
- **Early May** — Preview billing dashboard launches
- **May 20** — Deadline to cancel for prorated refund
- **June 1** — Usage-based billing live for all monthly subscribers
- **June–August** — Promotional credits: Business $30/user/mo, Enterprise $70/user/mo
- **After August** — Full usage costs hit

Annual subscribers keep legacy PRU-based pricing until plan expiration — but model multipliers increase June 1 (Claude Sonnet: 9×, Opus: 27×).

**Community Reaction**

- **"You will get less but pay the same price"** — Visual Studio Magazine headline
- Power users feel targeted — agentic workflows (Copilot's marquee feature) are now the most expensive
- "Switch to direct APIs" became common Hacker News advice — if paying per token, why not use providers directly?
- Enterprise developers acknowledge lock-in: compliance and procurement mean most orgs won't switch
- Pragmatists note the old model was unsustainable — multi-hour agentic sessions shouldn't cost $10/month

**Competitive Context**

Every AI coding tool converging on the same conclusion — unlimited flat-rate is dead:

- **Cursor** — $20/mo hybrid (500 fast + unlimited slow); $200/mo Ultra
- **Claude Code** — $20/mo (Pro, limited), $100/mo (Max), or pure pay-per-token via API
- **Copilot** — most similar to cloud infrastructure billing: base allotment + overage

Copilot's advantage is ecosystem lock-in (PRs, Issues, Actions, code review). Cursor offers multi-model flexibility. Claude Code offers deepest reasoning and largest context. Price alone won't determine winners — workflow integration will.

---
