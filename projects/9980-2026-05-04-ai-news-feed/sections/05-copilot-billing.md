## 5. GitHub Copilot's Billing Earthquake — From Flat Subscriptions to Pay-Per-Token

**April 27 | [GitHub Blog](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) · [Visual Studio Magazine](https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx) · [InfoWorld](https://www.infoworld.com/article/4164236/github-shifts-copilot-to-usage-based-billing-signaling-new-cost-model-for-enterprise-ai-tools.html)**

On April 27, GitHub CPO Mario Rodriguez announced that Copilot is moving to **usage-based billing on June 1, 2026** — the most significant pricing change since Copilot launched in 2022. The flat "all-you-can-eat" era is officially over.

**What's Changing**

The core shift: a new currency called **GitHub AI Credits** (1 credit = $0.01) replaces premium request units. Every chat message, agentic session, CLI query, and code review now costs credits based on actual token consumption. The heavier the model, the faster credits burn.

- **Base subscription prices stay the same:** Pro $10/mo, Pro+ $39/mo, Business $19/user/mo, Enterprise $39/user/mo
- **Credit allotments match plan price:** Pro gets 1,000 credits ($10 worth), Pro+ gets 3,900 credits, Business 1,900/user, Enterprise 3,900/user
- **Code completions and Next Edit remain unlimited** — the most common daily workflow stays free
- **When credits run out, usage stops** — no more fallback to cheaper models, no degraded mode
- **Overage option:** organizations can allow pay-per-credit overage OR enforce a hard cap

**Token Rates by Model**

- **GPT-4.1 / GPT-4o** — $2.00 input / $8.00 output per 1M tokens
- **Claude Sonnet 4/4.5/4.6** — $3.00 input / $15.00 output per 1M tokens
- **Claude Opus** — ~$15.00 input / ~$75.00 output per 1M tokens

A practical example: 100K input + 20K output tokens on Claude Sonnet 4.6 ≈ 60 credits ($0.60). A few heavy agentic sessions per day could exhaust the entire Pro monthly allotment.

**The Dual-Billing Problem**

Starting June 1, **Copilot code review on private repositories consumes both AI Credits AND GitHub Actions minutes** — you're billed twice for the same feature. Public repos are exempt. This is architecturally justified (code review runs on Actions runners), but the optics are punishing for teams doing heavy AI-assisted PR review.

**The Timeline That Feels Like "Boiling the Frog"**

- **~April 20** — GitHub pauses new sign-ups for Pro, Pro+, and Student plans; tightens session limits
- **April 27** — Official usage-based billing announcement
- **Early May** — Preview billing dashboard launches (see projected costs before transition)
- **May 20** — Deadline to cancel for prorated refund
- **June 1** — Usage-based billing goes live for all monthly subscribers
- **June–August** — Promotional credits: Business gets $30/user/mo, Enterprise $70/user/mo (well above normal allotments)
- **After August** — Full usage costs hit; budget conversations begin

Annual plan subscribers keep legacy PRU-based pricing until plan expiration — but model multipliers increase on June 1 (Claude Sonnet: 9× per request, Opus: 27×).

**Community Reaction**

The developer response has been sharp:

- **"You will get less but pay the same price"** — Visual Studio Magazine headline capturing the dominant sentiment
- Power users feel specifically targeted — agentic workflows (Copilot's marquee feature) are now the most expensive thing to do
- "Switch to direct APIs" became common advice on Hacker News — if you're paying per token anyway, why not use the provider directly?
- Enterprise developers acknowledge lock-in protects GitHub: compliance, procurement, and ecosystem integration mean most orgs won't switch regardless
- Pragmatists note the old model was unsustainable — a multi-hour agentic session shouldn't cost the same as a quick autocomplete

**Competitive Context**

Every AI coding tool is converging on the same conclusion — unlimited flat-rate access is dead:

- **Cursor** — $20/mo hybrid (500 fast requests + unlimited slow); $200/mo Ultra for heavy users
- **Claude Code** — $20/mo (Pro, limited daily), $100/mo (Max), or pure pay-per-token via API
- **Copilot** — now most similar to cloud infrastructure billing: base allotment + overage

The difference: Copilot's advantage is ecosystem lock-in (PRs, Issues, Actions, code review all in one platform). Cursor offers multi-model flexibility. Claude Code offers the deepest reasoning and largest context windows. Price alone won't determine winners — workflow integration will.

**Why This Is a Main Story**

This isn't just a pricing change. It's the moment the industry acknowledged that **agentic AI can't be sold like a subscription SaaS product**. The economics don't work — a developer running four hours of autonomous coding burns through hundreds of dollars in compute. GitHub subsidizing that with a $10/month plan was always a land-grab strategy, not a business model. Now the land-grab is over, and the real economics are being passed to users.

For engineering managers: budget for AI tooling in 2026 is no longer a simple per-seat multiplication. It's infrastructure spending with variable costs that scale with how much your team actually uses the tools — exactly like cloud compute before it.

---
