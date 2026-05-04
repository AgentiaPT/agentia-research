# Research: GitHub Copilot Usage-Based Billing (Deep Dive)

## Key Facts

- **Announced:** April 27, 2026, by Mario Rodriguez (GitHub CPO)
- **Effective date:** June 1, 2026
- **Core change:** Premium Request Units (PRUs) replaced by **GitHub AI Credits** (1 credit = $0.01 USD)
- **Base plan prices unchanged:** Pro $10/mo, Pro+ $39/mo, Business $19/user/mo, Enterprise $39/user/mo
- **Credit allotments match plan price:** Pro gets $10 (1,000 credits), Pro+ gets $39 (3,900 credits), Business $19/user (1,900 credits), Enterprise $39/user (3,900 credits)
- **Code completions and Next Edit suggestions remain unlimited** — do NOT consume AI Credits
- **Fallback to cheaper models eliminated** — when credits run out, usage stops (no more degraded mode)
- **Copilot code review now dual-billed:** consumes both AI Credits AND GitHub Actions minutes (private repos only)
- **Pooled credits for orgs:** unused individual capacity shared across the organization
- **Preview bill launching early May 2026** — projected cost visibility before transition
- **Annual plan subscribers:** remain on PRU-based pricing until plan expiration, then transition to monthly usage-based

## The New Model

### How AI Credits Work
- Credits consumed based on **token usage** (input + output + cached tokens) at published API rates per model
- Different models cost different amounts — heavier models burn credits faster
- Orgs can set budgets at enterprise, cost center, and individual user levels
- When included pool exhausted, orgs choose: allow overage at published rates OR hard cap

### Token Rates (Per 1M Tokens)
| Model | Input | Cached Input | Output |
|-------|-------|--------------|--------|
| GPT-4.1 / GPT-4o | $2.00 | $0.50 | $8.00 |
| Claude Sonnet 4/4.5/4.6 | $3.00 | $0.30 | $15.00 |
| Claude Opus | ~$15.00 | — | ~$75.00 |

### Legacy Multiplier Context (Annual Plan Subscribers Only)
- Claude Sonnet: **9× multiplier** (one request = 9 PRUs)
- Claude Opus: **27× multiplier** (one request = 27 PRUs)
- These multipliers increase on June 1 for annual-only subscribers still on PRU system

### Example Session Cost
- 100K input tokens + 20K output tokens on Claude Sonnet 4.6 = ~60 credits ($0.60)
- A few heavy chat sessions per day could exhaust the 1,000 credits/month Pro allotment

### What's Included vs. What Costs Credits
| Feature | Credits? | Notes |
|---------|----------|-------|
| Code completions | ❌ Free | Unlimited on paid plans |
| Next Edit suggestions | ❌ Free | Unlimited on paid plans |
| Chat (all models) | ✅ Yes | Token-metered |
| Agentic coding sessions | ✅ Yes | Heaviest consumer |
| Copilot CLI | ✅ Yes | Token-metered |
| Code review | ✅ Yes | ALSO consumes Actions minutes (private repos) |

## Timeline

- **~April 20, 2026:** GitHub pauses new sign-ups for Copilot Pro, Pro+, Student plans; tightens usage limits (reliability measures)
- **April 27, 2026:** Official announcement — usage-based billing blog post published; code review Actions minutes changelog published same day
- **Early May 2026:** Preview bill experience launches on Billing Overview page
- **May 20, 2026:** Deadline to cancel and receive prorated refund if changes are unsuitable
- **June 1, 2026:** Usage-based billing goes live for all monthly subscribers
- **June–August 2026:** Promotional credits for Business ($30/user/mo) and Enterprise ($70/user/mo) — significantly above normal allotments
- **Annual plan expiration (varies):** Annual subscribers transition to Copilot Free at expiry, can opt into monthly plan earlier with prorated credit

## Preceding Changes (Context)

- GitHub paused self-serve Copilot Business plan purchases
- Opus 4.7 restricted to Pro+ only; Opus 4.5/4.6 being removed from Pro+
- Session-based and 7-day usage limits tightened based on token consumption
- These were "reliability and performance measures" ahead of the billing transition

## Community Reaction

### Criticism / Pushback
- **"You will get less but pay the same price"** — headline from Visual Studio Magazine capturing dev sentiment
- **"The party's over"** — Hacker News thread sentiment; acknowledgment that subsidy-driven flat pricing was unsustainable but frustration at the transition
- **Predictability lost:** Developers frustrated that subscription is now variable-cost; must track token consumption or risk "bill shock"
- **Power users hardest hit:** Agentic workflows (Copilot's marquee feature) are the most expensive under the new model — exactly the use case GitHub was promoting
- **Dual billing for code review** seen as especially punitive — "bills you twice" (AI Credits + Actions minutes)
- **No rollover:** Unused credits don't carry over month to month
- Concerns about Opus access restrictions layered on top of billing changes

### Pragmatic / Positive Responses
- Some developers acknowledge the old model was unsustainable — a multi-hour agentic session shouldn't cost the same as a quick question
- Pooled credits for orgs seen as sensible — eliminates "stranded capacity"
- Budget controls and preview billing appreciated by enterprise admins
- Code completions remaining free protects the most common use case
- Promotional credits (June–Aug) give orgs time to adjust

### Notable Quotes / Sentiments
- "Switch to direct APIs, use fallback tools" — common pragmatic advice on HN
- Enterprise lock-in acknowledged: compliance/procurement ties to Microsoft will keep many organizations on Copilot regardless
- Individual developers and small teams more likely to explore alternatives (Cursor, Claude Code, direct API access)

## Competitive Context

### Comparison Table (2026 Pricing)
| Tool | Model | Individual Price | What You Get | Overage Model |
|------|-------|-----------------|--------------|---------------|
| **GitHub Copilot Pro** | Usage-based | $10/mo | 1,000 AI Credits + unlimited completions | Pay per additional credit |
| **GitHub Copilot Pro+** | Usage-based | $39/mo | 3,900 AI Credits + unlimited completions | Pay per additional credit |
| **Cursor Pro** | Hybrid | $20/mo | 500 fast requests + unlimited slow | Overage charges ~$40-50/mo for power users |
| **Cursor Ultra** | Hybrid | $200/mo | Frontier models, ultra-high limits | Included |
| **Claude Code (Pro)** | Usage-based | $20/mo | Limited daily usage | Subscription tier upgrade |
| **Claude Code (Max)** | Usage-based | $100/mo | Higher session caps | — |
| **Claude Code (API)** | Pure usage | Pay-per-token | $3/$15 per 1M tokens (Sonnet) | Direct metering |

### Key Differentiators
- **Copilot** now most similar to cloud infrastructure billing — pay for what you use, with a base allotment
- **Cursor** maintains hybrid model — flat fee for a request bucket, with overage (more predictable ceiling)
- **Claude Code** already usage-based (API) or tiered (subscriptions) — Copilot is converging toward this model
- **All three** are moving away from unlimited flat-rate access as agentic workloads make costs unpredictable for providers

### Strategic Positioning
- Copilot's advantage: deepest IDE integration + GitHub ecosystem lock-in (PRs, Issues, Actions, code review)
- Cursor's advantage: AI-native editor, multi-model flexibility, Composer for multi-file edits
- Claude Code's advantage: terminal-native agentic workflows, largest context windows, best at complex reasoning tasks

## Grandfathering / Transition Details

- **Annual plan subscribers:** Keep PRU-based pricing until plan expiration (but model multipliers increase June 1)
- **Monthly subscribers:** Automatically migrate June 1 — no opt-out
- **Promotional credits (Business/Enterprise):** June–August 2026 only — $30/user (Business) and $70/user (Enterprise) — up from normal $19/$39
- **Refund option:** Cancel before May 20 for prorated refund of unused subscription
- **Annual → Monthly conversion:** Can switch early; GitHub provides prorated credits for remaining annual plan value
- **New sign-ups paused:** Pro, Pro+, Student plans not accepting new subscribers (as of April 20)

## Sources

- [GitHub Blog: "GitHub Copilot is moving to usage-based billing"](https://github.blog/news-insights/company-news/github-copilot-is-moving-to-usage-based-billing/) — Official announcement by Mario Rodriguez, April 27, 2026
- [GitHub Blog: "Changes to GitHub Copilot Individual plans"](https://github.blog/news-insights/company-news/changes-to-github-copilot-individual-plans/) — Preceding reliability changes, paused sign-ups
- [GitHub Changelog: "Copilot code review will start consuming GitHub Actions minutes"](https://github.blog/changelog/2026-04-27-github-copilot-code-review-will-start-consuming-github-actions-minutes-on-june-1-2026/) — Dual-billing for code review
- [GitHub Docs: Models and Pricing](https://docs.github.com/en/copilot/reference/copilot-billing/models-and-pricing) — Token rates and model multipliers
- [GitHub Community Discussion #192948](https://github.com/orgs/community/discussions/192948) — Official FAQ thread
- [Visual Studio Magazine: "Devs Sound Off on Usage-Based Copilot Pricing Change"](https://visualstudiomagazine.com/articles/2026/04/27/devs-sound-off-on-usage-based-copilot-pricing-change-you-will-get-less-but-pay-the-same-price.aspx) — Developer reaction roundup
- [Hacker News Discussion](https://news.ycombinator.com/item?id=47923357) — Community debate and alternatives discussion
- [InfoWorld: "GitHub shifts Copilot to usage-based billing"](https://www.infoworld.com/article/4164236/github-shifts-copilot-to-usage-based-billing-signaling-new-cost-model-for-enterprise-ai-tools.html) — Enterprise AI cost model analysis
- [The New Stack: "GitHub Copilot usage billing"](https://thenewstack.io/github-copilot-usage-billing/) — Infrastructure cost perspective
- [The Register: "Microsoft's GitHub suspends Copilot account sign-ups"](https://www.theregister.com/2026/04/20/microsofts_github_grounds_copilot_account/) — Paused sign-ups coverage
- [GapVelocity: "GitHub Copilot's New Usage-Based Billing"](https://www.gapvelocity.ai/blog/github-copilots-new-usage-based-billing-what-changed-why-developers-are-upset-and-what-it-means) — Developer impact analysis

## Impact / Why It Matters

- **Fundamental shift in AI tool economics:** Signals the end of "all-you-can-eat" AI subscriptions industry-wide; agentic workloads make unlimited plans economically unviable for providers
- **Power users subsidized casual users under old model** — that cross-subsidy is ending, which punishes the most engaged (and most valuable) users
- **Agentic coding — Copilot's flagship direction — is now the most expensive feature to use**, creating a tension between product vision and pricing reality
- **Enterprise lock-in protects GitHub:** Compliance, procurement, and ecosystem integration mean most organizations won't switch — but individuals and small teams have real alternatives
- **Competitive pressure validated:** Cursor and Claude Code already operate on usage/tiered models; Copilot is converging to industry norm rather than leading
- **Code review dual-billing is a hidden cost multiplier:** Organizations running Copilot code review on many PRs will see both Actions minutes and AI Credits consumed, potentially significant for active repos
- **"Preview bill" is damage control:** Launching visibility tools before the switch attempts to prevent sticker shock, but also signals GitHub expects many users will be surprised by their true consumption
- **Promotional credits (June–Aug) are a grace period** — after August, organizations face full usage costs, likely triggering budget conversations and potential downgrades
- **Annual subscribers in limbo:** Protected temporarily but face worsening multipliers and eventual forced migration — the "grandfathering" is really just a delayed transition
- **Developer trust eroded:** Sequence of pausing sign-ups → tightening limits → eliminating fallback → announcing usage billing in rapid succession feels like a "boil the frog" strategy to many developers
