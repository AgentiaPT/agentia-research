## 2. Anthropic's Week from Hell — Claude Code, DMCA, and Congressional Fire

**March 31 – April 2 | [Axios](https://www.axios.com/2026/03/31/anthropic-leaked-source-code-ai) · [TechCrunch](https://techcrunch.com/2026/04/01/anthropic-took-down-thousands-of-github-repos-trying-to-yank-its-leaked-source-code-a-move-the-company-says-was-an-accident/) · [The Hill](https://thehill.com/policy/technology/5812881-gottheimer-presses-anthropic-ai-safety/)**

Days after the Mythos CMS leak [covered in last week's edition](../9984-2026-03-29-ai-news-feed/README.md#2-the-mythos-leak--anthropics-next-frontier-exposed), Anthropic's week got worse. Four cascading incidents turned the company into a case study in operational fragility at frontier AI labs.

### Act 1: The Claude Code Source Leak (March 31)

Anthropic accidentally bundled a **59.8MB source map file** into Claude Code version 2.1.88 on the npm registry. The root cause: Bun (the runtime) generates full source maps by default, and `*.map` was not excluded in `.npmignore`. The file pointed to a zip archive on Anthropic's cloud storage containing **the full source code — 1,906 files and 512,000 lines of TypeScript**.

An Anthropic spokesperson called it:

> "A release packaging issue caused by human error, not a security breach. No sensitive customer data or credentials were involved or exposed." — [CNBC](https://www.cnbc.com/2026/03/31/anthropic-leak-claude-code-internal-source.html#:~:text=A%20release%20packaging%20issue%20caused%20by%20human%20error)

The leaked code revealed **44 hidden feature flags** and unreleased capabilities, including:
- **KAIROS** — an autonomous daemon mode where Claude operates as a persistent, always-on background agent. Referenced 150+ times in the source. Includes "autoDream" — background memory consolidation that runs while the user is idle ([The Information](https://www.theinformation.com/newsletters/ai-agenda/claude-code-leak-reveals-always-kairos-agent) · [The New Stack](https://thenewstack.io/claude-code-source-leak/))
- **Coordinator Mode** — native multi-agent orchestration where a master Claude spawns parallel worker agents
- **ULTRAPLAN** — offloads planning to a remote Opus 4.6 session with up to 30 minutes of dedicated think time
- **Voice mode** with push-to-talk interface

### Act 2: The DMCA Fiasco (April 1)

Within hours, the leaked code became the **[fastest-growing repository in GitHub history](https://cybernews.com/tech/claude-code-leak-spawns-fastest-github-repo/#:~:text=fastest%20growing%20repository%20in%20GitHub%27s%20history)**. Anthropic filed DMCA takedown notices — but the blast radius was catastrophic.

GitHub executed the notice against approximately **8,100 repositories**, including legitimate forks of Anthropic's own publicly released Claude Code repository. Developers received takedown notices for simply forking the public repo or forks containing only skills, examples, and documentation.

Anthropic's head of Claude Code, **Boris Cherny**, retracted the bulk of the notices, limiting takedowns to one repository and 96 forks containing the actually leaked source. He acknowledged that the deploy process had manual steps that were mishandled, and said Anthropic had improved automation to prevent recurrence.

### Act 3: Congressional Scrutiny (April 2)

Rep. **Josh Gottheimer** (D-N.J.) [wrote to Anthropic CEO Dario Amodei](https://www.axios.com/2026/04/02/gottheimer-anthropic-source-code-leaks#:~:text=Gottheimer%20presses%20Anthropic%20on%20source%20code%20leaks%20and%20safety%20protocols), warning of potential national security risks:

> "Claude is a critical part of our national security operations. If it is replicated, we sacrifice the competitive edge we have worked so diligently to maintain in all facets of our national security."

Gottheimer also pointed to Anthropic's **narrowed safety policy** from late February, which removed a previous commitment to halt model development if capabilities outpace safety procedures — replacing it with "nonbinding but publicly-declared" goals.

### Act 4: The Malware Exploitation

Within 48 hours of the source code leak, threat actors created **fake GitHub repositories** advertising "unlocked enterprise features" from the leaked code. These repos delivered **Vidar infostealer** (steals credentials, credit card data, browser history) and **GhostSocks** (network traffic proxy malware). The leak didn't just embarrass Anthropic — it became a social engineering lure for malware distribution ([The Register](https://www.theregister.com/2026/04/02/trojanized_claude_code_leak_github/) · [BleepingComputer](https://www.bleepingcomputer.com/news/security/claude-code-leak-used-to-push-infostealer-malware-on-github/)).

### Why This Matters

This isn't a story about one company having a bad week. It's a stress test of whether frontier AI labs can operate at the speed they've chosen. Anthropic publishes the most rigorous AI safety research in the industry. If *they* can't keep their npm publishes clean, the question for the entire field is uncomfortable: **what are the rest of you leaking that nobody's found yet?**
