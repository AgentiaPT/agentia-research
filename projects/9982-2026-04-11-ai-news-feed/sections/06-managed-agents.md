## 6. Claude Managed Agents — Anthropic's Infrastructure Play

**April 8 | [Anthropic](https://www.anthropic.com/news/managed-agents) · [SiliconANGLE](https://siliconangle.com/2026/04/08/anthropic-launches-claude-managed-agents-speed-ai-agent-development/) · [Unite.AI](https://www.unite.ai/anthropic-launches-managed-agents-to-run-enterprise-ai-workloads/) · [Kingy AI](https://kingy.ai/ai/claude-managed-agents-anthropics-boldest-infrastructure-play-yet-and-why-it-changes-everything-for-ai-developers/)**

Anthropic launched **Claude Managed Agents** in public beta — a suite of composable APIs that provides the infrastructure for running production-grade AI agents at scale. This is Anthropic's play to own the layer between models and applications, compressing months of agent infrastructure engineering into days.

### Architecture

The system separates three concerns:

| Component | Role |
|---|---|
| **The Brain** | Claude handles reasoning, planning, and decision-making |
| **The Hands** | Sandboxed code execution, file operations, tool use |
| **The Session** | Persistent event log maintaining state across interactions |

This decoupling means developers don't need to build sandbox infrastructure, credential management, session persistence, scaling, or error recovery. Anthropic handles all of it.

### Pricing and Access

- **$0.08 per agent runtime hour** (on top of standard Claude API token pricing)
- Public beta — available now via the Anthropic API
- Early adopters: **Notion**, **Asana**, **Sentry**, **Rakuten**

### The Advisor Tool

Alongside Managed Agents, Anthropic shipped the **Advisor Tool** — a system that lets different Claude models take on different roles within the same workflow. A fast model handles triage, a reasoning model handles planning, and a specialist model handles execution. This is multi-model orchestration without the developer managing the routing.

### Why This Matters

At $0.08/hour, agent infrastructure is approaching commodity pricing. The comparison:

| Option | Setup Time | Cost |
|---|---|---|
| Build your own agent infrastructure | 2–6 months | Engineering salaries + cloud costs |
| Claude Managed Agents | Days | $0.08/hr + tokens |

This directly competes with OpenAI's Assistants API and Google's Vertex AI agents, but Anthropic's bet is that the combination of Claude's code understanding (80.8% SWE-bench) and managed infrastructure will be the deciding factor for enterprises already invested in the Claude ecosystem.

The timing is strategic: launch managed agent infrastructure the same week you announce $30B in revenue and 1,000+ enterprise customers spending $1M+ each. The message to enterprises is clear — Anthropic isn't just a model provider, it's a platform.
