## 6. Karpathy's "Software 3.0" and the Yegge–Google Drama

**April 26–May 1 | [Sequoia Ascent](https://karpathy.bearblog.dev/sequoia-ascent-2026/) · [VentureBeat](https://venturebeat.com/orchestration/google-leaders-including-demis-hassabis-push-back-on-claim-of-uneven-ai-adoption-internally) · [Firstpost](https://www.firstpost.com/tech/googlers-want-better-agentic-tools-steve-yegge-reiterates-concerns-over-uneven-ai-adoption-at-google-14002858.html)**

Two stories that define where the developer profession stands in May 2026: a respected researcher declaring the old paradigm dead, and a veteran engineer exposing the gap between marketing and reality at the world's largest AI company.

### Karpathy at Sequoia Ascent — "Software 3.0" (Apr 30)

Andrej Karpathy's talk at Sequoia's annual AI summit crystallized a framework:

- **Software 1.0** — humans write explicit code
- **Software 2.0** — humans curate data, neural networks learn the code
- **Software 3.0** — humans write prompts and specs, AI agents write and maintain the code

Key claims:

- The **"agentic inflection point"** arrived December 2025 — the moment AI agents became reliable enough to own multi-step workflows end-to-end
- **"Vibe coding"** (his own coined term) was the transitional phase — humans vibing with AI on individual tasks. We've moved past it into **"agentic engineering"** — orchestrating teams of agents.
- **"Jagged intelligence"** — AI is superhuman at some tasks, incompetent at others, and the boundary is unpredictable. Engineers must develop intuition for where to trust and where to verify.
- The bottleneck is no longer execution but **"human understanding, management, and judgment"**
- Predicted: by end of 2026, most new code at top tech companies will be agent-generated with human review

**AutoResearch** (released Apr 26) — Karpathy's open-source framework where an AI agent proposes ML experiments, implements them, evaluates results, and keeps/reverts changes in a "ratchet loop." Claims ~700 autonomous experiments in 2 days on a single GPU, finding 11% efficiency improvements.

### Yegge vs. Google — The Two-Tier AI Adoption Drama (Week of Apr 20–27)

Steve Yegge's viral X thread (1.9M+ views, 4,500+ likes, 458 replies) dropped a bomb:

**The claim:** Google's internal AI adoption follows a "20/60/20" split — identical to industry average:
- 20% agentic adopters (mostly DeepMind, using Claude and advanced tooling)
- 60% basic assistant users (using Gemini for autocomplete)
- 20% refusers (don't touch AI at all)

**The allegation:** A "two-tier system" where DeepMind engineers use far more advanced agentic tools (including competitor products like Claude) than the rest of Google, which is locked into Gemini.

**The pushback:**
- **Demis Hassabis** called it "absolutely nonsense" and "clickbait"
- **Addy Osmani** countered with data: **40,000+ Google engineers** use agentic coding tools weekly
- Google leadership mobilized across multiple channels to dispute the framing

**Yegge doubled down:** cited anonymous Googlers confirming cultural friction, reported that internal tooling teams had been "sandbagged" by Gemini integration mandates, and released **Gas City v1.0** — an open-source MIT-licensed agent orchestration SDK as if to say "here's what a proper agentic framework looks like."

**Why this matters beyond the drama:** Every large enterprise has this same adoption gap. The question isn't whether AI tools work — it's whether organizations let their best engineers use the best tools, or force standardization on an inferior internal option for strategic reasons.

---
