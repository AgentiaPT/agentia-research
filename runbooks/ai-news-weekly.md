# AI × Software Engineering — Weekly News Update Runbook

This runbook documents the end-to-end process for producing the weekly "AI × Software Engineering" news update. It was captured from the actual session that produced the [March 30 – April 4, 2026 edition](../projects/9983-2026-04-04-ai-news-feed/README.md) and codifies the workflow so future sessions can replicate it efficiently.

---

## Overview

Each edition is a ~6,000–8,000 word thematic analysis of the week's AI × software engineering news, published as:
- **README.md** — the main narrative (12 sections)
- **explorer.html** — interactive visual dashboard
- **sources.md** — full citation index
- **task.md** — session continuity and intent tracking
- **outline.md** — section plan and story mapping

Editions are **ongoing** projects under `projects/NNNN-YYYY-MM-DD-ai-news-feed/`.

---

## Phase 0: Setup (~2 minutes)

### Create the project folder

1. **Fetch all remote refs** to avoid number collisions:
   ```bash
   git fetch origin --prune
   ```

2. **Scan all branches for existing project numbers:**
   ```bash
   (ls -d projects/[0-9][0-9][0-9][0-9]-* 2>/dev/null; \
    git branch -r | grep 'origin/' | while read b; do \
      git ls-tree -d --name-only "$b" -- projects/ 2>/dev/null \
      | grep -E '^projects/[0-9]{4}-'; \
    done) | sed 's|projects/\([0-9]\{4\}\)-.*|\1|' | sort -u
   ```

3. **Assign the next number** (lowest existing - 1) and create the folder:
   ```bash
   mkdir -p projects/NNNN-YYYY-MM-DD-ai-news-feed/sections
   ```

4. **Create task.md immediately** — before anything else. Include:
   - Original request
   - Week date range
   - Empty progress checklist

5. **Commit and continue.**

### Review previous editions

Read the previous 1–2 editions to understand:
- What stories were already covered (to avoid retelling)
- Which voices were tracked
- What signals were flagged as "watch" (may have developed)
- The narrative arc (each week builds on the last)

This is **critical** — the #1 editorial mistake is retelling stories from previous weeks.

---

## Phase 1: Research (~10 minutes)

### Launch parallel research agents

Spawn **6 research agents simultaneously**, each covering a different topic area:

| Agent | Coverage |
|---|---|
| **Model releases** | New models, updates, capability announcements, pricing changes, benchmark results |
| **Developer tools** | Copilot, Cursor, Windsurf, Claude Code, VS Code, JetBrains, agentic coding tools |
| **Security / supply chain** | Vulnerabilities, attacks, AI safety research, prompt injection, malware |
| **Jobs / industry** | Layoffs, hiring, funding rounds, acquisitions, enterprise adoption, productivity studies |
| **Thought leaders / voices** | Named individuals: Karpathy, Willison, Andreessen, Orosz, Swyx, Theo, etc. |
| **Research papers** | arXiv papers, studies, conference proceedings relevant to AI × software engineering |

Each agent prompt should:
- Specify the exact date range (e.g., "March 30 to April 4, 2026")
- List specific search queries to run
- Request structured output: what happened, when, source URL, key quotes, why it matters

### Direct searches while agents run

While background agents work, run direct `WebSearch` queries for:
- Breaking news from today/yesterday
- Specific companies (OpenAI, Anthropic, Google, Meta, Microsoft)
- Follow-up on previous edition's "watch" signals

### Fetch and verify sources

Use `WebFetch` on key articles to extract exact quotes, dates, and details. Many sources will return 403 — track these in `pending.md` for the user to check manually.

---

## Phase 2: Outline (~3 minutes)

Create `outline.md` with:

1. **Week theme** — a 2-3 word thematic label (e.g., "The Unraveling")
2. **12 sections mapped to stories** — each section gets a title, subtitle, and bullet points
3. **Story-to-section assignment** — every major story assigned to exactly one section
4. **Key quotes candidates** — best quotes from the week, attributed and sourced
5. **Signals classification** — 🔴 Critical / 🟠 Warning / 🟢 Emerging / 🔵 Watch

### The 12-section structure

| # | Section | Content |
|---|---|---|
| 1 | **The Week's Narrative** | Synthesized thesis, convergence table, unifying thread, deepest signal |
| 2–8 | **Thematic deep-dives** | 6–7 sections, one per major story cluster. Each has: lead paragraph, subsections, tables, blockquotes, "why this matters" |
| 9 | **Voice Tracker** | Who said what this week. Active (✅) and inactive (❌) voices with quotes and sources |
| 10 | **Model & Tool Updates** | Short-form updates organized by company/tool |
| 11 | **Jobs & Economic Impact** | Data tables, narratives, hiring vs. layoffs |
| 12 | **Signals & Radar** | Color-coded signals + Key Quotes of the Week |

### Date window discipline

**Only include stories clearly within the edition's week window.** This is the most common editorial mistake. Rules:

- If a story was covered in a previous edition → **don't retell it**. Reference it with a link: `[covered last week](../9984-.../README.md#section-anchor)`.
- If a study/paper was published before the week window → **don't include it** even if it's relevant.
- If ongoing fallout from a previous story has *new developments* this week → **cover the new development only**, with a brief cross-reference to the original.
- Aggregate stats (e.g., "53% of AI code has security holes") that aren't tied to a specific this-week publication → **don't include**.

Commit the outline.

---

## Phase 3: Writing (~15 minutes)

### Write section by section

Write each section as a separate file in `sections/`:
```
sections/01-narrative.md
sections/02-anthropic.md
...
sections/12-signals.md
```

**Commit after every 2–3 sections.** This is non-negotiable — if the session drops, committed work is saved.

### Writing conventions

- **Lead with the news**, not the context
- **Tables** for comparative data, timelines, numbers
- **Blockquotes** for exact quotes with attribution and source link
- **Bold** for key metrics, names, first mentions
- **Cross-references** to previous editions where stories connect (use relative links: `../9984-.../README.md#anchor`)
- **Source links** use `#:~:text=` fragment syntax when possible
- Every major claim needs a source link inline

### Assemble the README

After all sections are written:

```bash
head -38 README.md > README.md.header
cat README.md.header \
  sections/01-narrative.md <(echo -e "\n---\n") \
  sections/02-anthropic.md <(echo -e "\n---\n") \
  ... \
  sections/12-signals.md > README.md
rm README.md.header
```

The README header (frontmatter + TOC) is written first, sections are concatenated into it at the end.

---

## Phase 4: Explorer Dashboard (~10 minutes)

### Build explorer.html in parts

The interactive dashboard is a single self-contained HTML file (~600 lines). Write it in 3 parts:

| Part | Content |
|---|---|
| `explorer.html.part_01_head` | `<!DOCTYPE>` through `</style></head>`, header, readme banner |
| `explorer.html.part_02_body` | Layout, sidebar, stats grid, signal radar, theme bars, voice map |
| `explorer.html.part_03_tail` | Key quotes, voice tracker table, `</body></html>` |

Commit each part, then concatenate:
```bash
cat explorer.html.part_* > explorer.html && rm explorer.html.part_*
```

### Dashboard components

- **Stats grid** — 8 key numbers from the week (use colored values: red for alarming, green for positive)
- **Signal radar** — 🔴🟠🟢🔵 items from §12
- **Theme coverage bars** — horizontal bars showing relative coverage per theme
- **Voice position map** — 2D scatter (Cautious↔Accelerationist × Individual↔Institutional)
- **Key quotes** — blockquotes with colored left borders
- **Voice tracker table** — ✅/❌ status, name, topic, source link

### Design system

Use the repo's standard dark theme (see CLAUDE.md for CSS variables). All CSS/JS inline, no external dependencies.

### Screenshot

```bash
npx playwright screenshot --viewport-size="1280,720" \
  "file:///absolute/path/to/explorer.html" \
  "projects/NNNN-.../explorer-screenshot.png"
```

---

## Phase 5: Sources & Index (~2 minutes)

1. **Write `sources.md`** — organized by section number, with full URLs
2. **Run the index builder:**
   ```bash
   python3 scripts/build-index.py
   ```
3. **Commit** README.md, projects/README.md, projects/index.json, and explorer-screenshot.png together.

---

## Phase 6: Fact-Check (~10 minutes)

### Multi-pass verification

For every quote, number, date, and claim in the edition:

1. **Search for the exact claim** using `WebSearch` with the specific number/quote in quotes
2. **Cross-reference** against at least one additional source
3. **Fix any discrepancies** — common issues:
   - Download counts vary across sources (use the authoritative source, e.g., npm registry or Microsoft)
   - Quotes may be paraphrased — find the exact wording
   - Dates may be off by one (time zones)
   - Line counts, file counts, dollar amounts rounded differently across outlets

### Track corrections

Note every correction made and why. The commit message for the fact-check pass should list all fixes.

---

## Phase 7: Cross-References (~3 minutes)

Add links to previous editions wherever a story connects to earlier coverage. These create narrative continuity and help readers follow multi-week arcs.

**Pattern:** Brief context clause + relative link to the specific section anchor.

```markdown
After last week's [data training backlash](../9984-.../README.md#4-the-data-training-backlash),
GitHub pivoted to shipping capability.
```

**Where to add them:**
- Stories that are continuations of previous coverage
- Voices who were active in previous weeks
- Signals that moved from "watch" to "critical"
- Jobs/economic data that shows trend lines across weeks

---

## Phase 8: User Review

The edition ships as `status: draft`. The user adds:
- **Their picks** — top stories and commentary
- **Human commentary blocks** — `> 🧑‍💻 **RQuintino:**` blockquotes at natural breakpoints
- **Final approval** — status changes to `complete`

---

## Checklist

```
- [ ] Project folder created with task.md
- [ ] Previous editions reviewed for overlap
- [ ] 6 parallel research agents launched
- [ ] Outline.md with 12-section plan
- [ ] Sections written and committed incrementally
- [ ] README.md assembled from sections
- [ ] explorer.html built in parts, concatenated
- [ ] Screenshot taken (1280×720)
- [ ] sources.md written
- [ ] build-index.py run
- [ ] Fact-check pass (every quote, number, date)
- [ ] Cross-references to previous editions added
- [ ] Date window audit (no out-of-window stories)
- [ ] Status set to draft for user review
```

---

## Common Mistakes

| Mistake | Prevention |
|---|---|
| Retelling stories from previous editions | Review previous TOC before writing outline |
| Including old studies/stats not from this week | Check publication date of every study cited |
| Approximate quotes | Search for exact quote text in quotes |
| Wrong download/user counts | Use authoritative source (npm, company blog) |
| Forgetting to run build-index.py | It's in the checklist — run after every change to project READMEs |
| Explorer stats don't match README after edits | Update both in the same commit |
| Session timeout loses work | Commit after every 2–3 sections, use part files for HTML |

---

## Timing (Approximate)

| Phase | Time |
|---|---|
| Setup + review previous | 2 min |
| Research (parallel agents) | 10 min |
| Outline | 3 min |
| Writing (12 sections) | 15 min |
| Explorer dashboard | 10 min |
| Sources + index | 2 min |
| Fact-check | 10 min |
| Cross-references | 3 min |
| **Total** | **~55 min** |

User review and commentary are asynchronous and not included in the above.
