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
