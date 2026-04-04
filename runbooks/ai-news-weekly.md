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

Copy this checklist into `task.md` at project creation and update it throughout the session.

### Phase 0: Setup

- [ ] `git fetch origin --prune` run (retry up to 4× on network failure)
- [ ] All branch project numbers scanned (local + remote)
- [ ] New project number assigned (lowest existing - 1)
- [ ] Project folder created: `projects/NNNN-YYYY-MM-DD-ai-news-feed/`
- [ ] `sections/` subdirectory created
- [ ] `task.md` created as the **very first file** — before anything else
- [ ] `task.md` includes: original request, week date range, empty progress checklist
- [ ] Initial commit made (folder + task.md)

### Phase 0.5: Previous Edition Review

- [ ] Previous edition README.md TOC read — know what was covered
- [ ] Previous edition §12 Signals "Watch" items noted — check if any developed
- [ ] Previous edition Voice Tracker reviewed — know who was active/inactive
- [ ] Previous edition §11 Model Updates reviewed — don't repeat announcements
- [ ] Stories from previous editions flagged as **do not retell**

### Phase 1: Research

- [ ] Agent 1 launched: **Model releases** (new models, updates, pricing, benchmarks)
- [ ] Agent 2 launched: **Developer tools** (Copilot, Cursor, Windsurf, Claude Code, VS Code, JetBrains)
- [ ] Agent 3 launched: **Security / supply chain** (CVEs, attacks, safety research, regulation)
- [ ] Agent 4 launched: **Jobs / industry** (layoffs, hiring, funding, acquisitions, productivity)
- [ ] Agent 5 launched: **Thought leaders** (Karpathy, Willison, Andreessen, Orosz, Swyx, etc.)
- [ ] Agent 6 launched: **Research papers** (arXiv, conferences, studies)
- [ ] All 6 agents launched in a single parallel batch
- [ ] Direct `WebSearch` queries run for breaking/same-day news while agents work
- [ ] Key articles fetched with `WebFetch` for exact quotes and details
- [ ] 403'd sources logged in `pending.md` for user to check
- [ ] All 6 agents completed and findings reviewed
- [ ] Stories triaged: in-window ✅ vs. out-of-window ❌ vs. already covered ❌

### Phase 2: Outline

- [ ] Week theme chosen (2–3 word label, e.g., "The Unraveling")
- [ ] `outline.md` created with all 12 sections mapped
- [ ] Every major story assigned to exactly one section
- [ ] Key quotes candidates listed with attribution and source URL
- [ ] Signals classified: 🔴 Critical / 🟠 Warning / 🟢 Emerging / 🔵 Watch
- [ ] Cross-reference opportunities noted (links to previous editions)
- [ ] Outline committed

### Phase 3: Writing — README Sections

#### Section structure (repeat for each)
- [ ] Section file created: `sections/NN-slug.md`
- [ ] Heading includes date range and source links
- [ ] Lead paragraph states what happened and why it matters
- [ ] Subsections break the story into digestible parts
- [ ] Tables used for comparative data, timelines, numbers
- [ ] Blockquotes used for exact quotes with attribution + source URL
- [ ] "Why this matters" closing paragraph included
- [ ] Cross-reference to previous edition added where relevant

#### Individual sections
- [ ] `sections/01-narrative.md` — Week thesis, convergence table, unifying thread, deepest signal
- [ ] `sections/02-*.md` through `sections/08-*.md` — Thematic deep-dives (6–7 sections)
- [ ] `sections/09-voices.md` — Voice Tracker with ✅/❌ status, quotes, summary table
- [ ] `sections/10-model-updates.md` — Short-form updates by company/tool
- [ ] `sections/11-jobs.md` — Data tables, three narratives framework, hiring vs. layoffs
- [ ] `sections/12-signals.md` — Color-coded signals + Key Quotes of the Week
- [ ] Sections committed in batches of 2–3 (never let more than 3 uncommitted)

#### README assembly
- [ ] README.md frontmatter written (title, date, status: draft, tags, explorers metadata)
- [ ] AI authorship disclaimer included after first `#` heading
- [ ] Previous edition link included
- [ ] Explorer dashboard link included (GitHub Pages URL)
- [ ] Table of Contents with all 12 sections
- [ ] All sections concatenated into README.md via `cat`
- [ ] Word count verified (target: 6,000–8,000 words)
- [ ] Assembled README committed

### Phase 4: Explorer Dashboard

#### HTML structure
- [ ] `explorer.html.part_01_head` written — DOCTYPE, CSS, header, readme banner
- [ ] Part 01 committed
- [ ] `explorer.html.part_02_body` written — sidebar, stats grid, signal radar, themes, voice map
- [ ] Part 02 committed
- [ ] `explorer.html.part_03_tail` written — quotes, voice tracker table, JS, closing tags
- [ ] Part 03 committed
- [ ] Parts concatenated: `cat explorer.html.part_* > explorer.html && rm explorer.html.part_*`
- [ ] Final explorer.html committed

#### Dashboard content checks
- [ ] Stats grid: 8 key numbers from the week, correctly colored (red/orange/green)
- [ ] Signal radar: matches §12 signals (no stale items from drafts)
- [ ] Theme coverage bars: reflect actual section coverage
- [ ] Voice map: positions are defensible (cautious↔accelerationist × individual↔institutional)
- [ ] Voice tooltips: name + key topic for each dot
- [ ] Key quotes: match the quotes in §12 exactly
- [ ] Voice tracker table: matches §9 voice list (same voices, same ✅/❌ status)
- [ ] All links point to the correct project folder (not previous edition)
- [ ] README banner links use the correct branch/path
- [ ] Design system: dark theme, correct CSS variables, no external dependencies

#### Screenshot
- [ ] Playwright screenshot taken at 1280×720:
  ```bash
  npx playwright screenshot --viewport-size="1280,720" \
    "file:///absolute/path/to/explorer.html" \
    "projects/NNNN-.../explorer-screenshot.png"
  ```
- [ ] Screenshot committed

### Phase 5: Sources & Index

- [ ] `sources.md` created with URLs organized by section number
- [ ] Every source in the README has a corresponding entry in sources.md
- [ ] 403'd sources noted with `*(403)*` annotation
- [ ] `python3 scripts/build-index.py` run
- [ ] Output verified: correct project count, README.md + projects/README.md + index.json updated
- [ ] All index files committed together with sources.md

### Phase 6: Fact-Check

#### Quotes
- [ ] Every blockquote verified against original source
- [ ] Exact wording confirmed (not paraphrased)
- [ ] Attribution correct (name, title, outlet)
- [ ] Quotes that couldn't be verified against primary source flagged or removed

#### Numbers and dates
- [ ] Download counts verified against authoritative source (npm, company blog, registry)
- [ ] Dollar amounts verified (funding rounds, revenue, capex)
- [ ] Layoff numbers verified against multiple sources, ranges noted where sources disagree
- [ ] Dates verified (watch for timezone shifts — UTC vs. EST can move events by a day)
- [ ] Model benchmark scores verified against original leaderboard/paper
- [ ] Percentages and multipliers verified (e.g., "2.74×" — is this from a specific study?)

#### Claims
- [ ] Every "first ever" / "largest" / "most" superlative verified
- [ ] Attribution claims verified (e.g., "Microsoft attributed to Sapphire Sleet")
- [ ] Technical details verified (file sizes, line counts, version numbers)
- [ ] Company responses verified as actual quotes, not summaries

#### Corrections
- [ ] All corrections logged in the commit message
- [ ] README rebuilt after corrections
- [ ] Explorer updated if any stats changed
- [ ] New screenshot taken if explorer stats changed

### Phase 7: Cross-References

- [ ] Every story that continues from a previous edition has a link to the original section
- [ ] Links use relative paths: `../9984-.../README.md#section-anchor`
- [ ] Links are woven into natural prose (not standalone "see also" lists)
- [ ] Previous "Watch" signals that materialized are noted
- [ ] Voice tracker references previous activity where relevant
- [ ] Jobs data references trend line across editions

### Phase 8: Date Window Audit (Final Pass)

- [ ] Every story in §1–§8 happened within the edition's week window
- [ ] No studies/papers from before the week window are cited as "this week's news"
- [ ] Stories from previous editions are referenced via links, not retold
- [ ] Aggregate stats (not tied to a specific this-week publication) are removed
- [ ] Voice Tracker quotes are from this week (not previous interviews)
- [ ] §10 Model Updates: every item has a date within the window
- [ ] §12 Signals: every signal references a this-week event

### Phase 9: Final Packaging

- [ ] README.md frontmatter `status: draft` (user will change to `complete`)
- [ ] `task.md` updated with final progress and key stories summary
- [ ] `pending.md` lists: 403'd sources, editorial tasks for user, coverage gaps
- [ ] `python3 scripts/build-index.py` run one final time
- [ ] All files committed
- [ ] `git log --oneline` reviewed — commit history tells a clean story
- [ ] Branch pushed (only with explicit user permission per CLAUDE.md rules)

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
