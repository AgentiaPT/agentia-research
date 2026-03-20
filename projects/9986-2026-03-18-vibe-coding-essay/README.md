# The Civilization That Forgot How to Code

*March 2026*

---

## I. The Tax on Progress

Around 370 BCE, Socrates made an argument against writing. In Plato's *Phaedrus*, he warned that the written word would ["create forgetfulness in the learners' souls"](https://fs.blog/an-old-argument-against-writing/#:~:text=create%20forgetfulness%20in%20the%20learners%27%20souls) — that people who relied on text would "appear as though they were all-knowing, but to actually be learners of nothing." They would become hearers of many things but knowers of nothing.

He was right. Oral cultures had prodigious memories. The Homeric bards could recite the 15,693 lines of the *Iliad* from memory — a capacity that literate cultures simply don't develop. Writing atrophied that capacity as surely as a cast atrophies a muscle.

And yet. Writing gave us law, science, history, philosophy, engineering, medicine. It gave us Socrates' own argument, preserved across twenty-four centuries in the very medium he warned against. Plato wrote the warning down. He used the new tool to argue against the new tool, because the alternative — letting the argument die with its speaker — was worse.

This pattern repeats. Every transformative technology in human history has demanded a tax paid in comprehension.

Agriculture gave us civilization but cost us the generalist survival skills of the hunter-gatherer. A modern human dropped in the wilderness would likely die. Metallurgy gave us tools but concentrated knowledge into guilds that jealously guarded their secrets — and when those guilds dissolved, the knowledge went with them. Damascus steel was manufactured for 1,100 years before the recipe [vanished entirely](https://www.worldatlas.com/ancient-world/10-ancient-technologies-we-still-can-t-replicate-today.html#:~:text=Damascus%20steel). We still can't fully replicate it. The division of labor — Adam Smith's [pin factory](https://en.wikipedia.org/wiki/Division_of_labour#Adam_Smith) — gave us 4,800 pins per worker per day instead of one, but no single worker understood the whole process. That was the point. That was the trade.

The pattern is consistent: as systems grow more powerful, they exceed individual comprehension. This isn't a design flaw. It's what power *is*. A system fully comprehensible to a single human mind is, by definition, limited to what a single human mind can hold. To go beyond that limit, you accept opacity. You pay the tax.

Every civilization that has advanced has paid it. The question has never been whether to pay. The question has always been: *are the terms fair?*

In February 2025, Andrej Karpathy — former director of AI at Tesla, founding member of OpenAI — posted a description of a new way of writing software. He called it "vibe coding." He described talking to an AI through a microphone, barely touching his keyboard. ["I 'Accept All' always,"](https://x.com/karpathy/status/1886192184808149383#:~:text=Accept%20All%20always) he wrote. "I don't read the diffs anymore." When bugs appeared, he copy-pasted the error messages with no comment. "The code grows beyond my usual comprehension," he said. When the AI couldn't fix something, he "just works around it or asks for random changes until it goes away."

The post got [4.5 million views](https://www.secondtalent.com/resources/vibe-coding-statistics/#:~:text=4.5%20million%20views). [Collins Dictionary named "vibe coding" its Word of the Year.](https://www.collinsdictionary.com/word-of-the-year)

Karpathy qualified his post — "it's not too bad for throwaway weekend projects" — but qualifications don't survive virality. What survived was the vibe. *Forget that the code even exists.* A new generation of developers heard the message: comprehension is optional. Ship it.

This essay argues that the comprehension tax is real, may be unavoidable, and has been worth paying at every prior turn in human history. It also argues that this time, the terms of the trade may be different — and we are signing without reading.

---

## II. The Vibes

Here is what it feels like.

You're tired. The feature has been sitting in your backlog for a week. You open your AI coding assistant and describe what you want in plain English. Forty seconds later, there's a complete implementation — tests included. You read the first few lines. They look reasonable. You run the tests. They pass. You skim the rest. You merge.

Three days later, someone asks you how the feature works. You open the file. You recognize the code the way you recognize a street you've driven down but never walked — the shape is familiar but the details aren't yours. You can't explain it. You wrote none of it. You understood none of it. And it works.

This is not a hypothetical. Addy Osmani, director of engineering at Google, [described the exact experience](https://addyosmani.com/blog/comprehension-debt/#:~:text=growing%20gap%20between%20how%20much%20code): "Claude implemented a feature I'd been putting off for days. The tests passed. I skimmed it, nodded, merged. Three days later I couldn't explain how it worked." He coined a term for what's accumulating: *comprehension debt* — ["the growing gap between how much code exists in your system and how much of it any human being genuinely understands."](https://addyosmani.com/blog/comprehension-debt/#:~:text=growing%20gap%20between%20how%20much%20code)

The arc of that experience — relief, then habit, then erosion, then dependency — is familiar to anyone who has used these tools daily. Karpathy named the first stage: the vibes. The later stages don't have names yet. But they have data.

In mid-2025, METR (Model Evaluation & Threat Research) ran a randomized controlled trial: 16 experienced open-source developers, 246 real tasks in codebases where they averaged five years of experience and 1,500+ prior commits. Tasks were randomly assigned to allow or disallow AI tools. The result: [allowing AI tools increased completion time by 19%](https://metr.org/blog/2025-07-10-early-2025-ai-experienced-os-dev-study/#:~:text=allowing%20AI%20actually%20increased%20completion%20time%20by%2019%25). AI made experienced developers *slower*.

But here's the finding that should unsettle you: before starting, the developers predicted AI would make them 24% faster. After finishing, they still believed it had made them 20% faster. The actual measurement: 19% slower. The perception gap is not small. It is a full inversion — developers cannot accurately assess their own AI-augmented productivity.

And yet: 69% of participants continued using the AI tools after the study ended. The *feeling* of productivity persists even when the measurement shows the opposite. This is dependency in its clinical sense — continued use despite evidence of harm, driven by subjective experience that contradicts objective measurement.

A separate study found Anthropic's own tools confirm the cost at the skill level. In a [randomized controlled trial published January 2026](https://www.anthropic.com/research/AI-assistance-coding-skills#:~:text=17%25%20lower), Anthropic — the company that builds Claude — tested 52 software engineers learning a new Python library. Those with AI access scored 50% on follow-up assessments. Those who coded by hand scored 67%. A 17-point gap — nearly two letter grades. Debugging skills showed the steepest decline, which is particularly concerning since catching AI-generated errors is the critical remaining human function.

But the study contained a more important finding buried in the usage data. Not all AI use was equal. Developers who used AI to ask *conceptual questions* — "how does this pattern work?" — retained nearly as much as the hand-coders, scoring 65%+. Developers who *delegated code generation* — "write this function for me" — scored below 40%. The difference wasn't the tool. It was the relationship to the tool. Inquiry preserved learning. Delegation destroyed it.

This distinction matters because it complicates the easy narratives on both sides. The optimist says "AI makes us more productive." The data says: maybe, for simple tasks; probably not, for complex ones; and you can't tell which you're experiencing. The pessimist says "AI makes us dumber." The data says: it depends entirely on whether you engage your brain or turn it off. The tool is not the variable. The human's posture toward the tool is the variable.

Bainbridge saw this coming. In 1983, Lisanne Bainbridge published ["Ironies of Automation"](https://ckrybus.com/static/papers/Bainbridge_1983_Automatica.pdf) in *Automatica*, a paper that has been cited over 1,800 times and remains unresolved. Her central irony: you automate a task because humans are unreliable at it, but the remaining human task — monitoring the automation and intervening when it fails — requires *more* skill than the original task, not less. The operator needs to be "more rather than less skilled." Meanwhile, the operator's skills are atrophying from disuse, because they spend their days monitoring rather than doing.

Forty years later, the irony has arrived in software. Developers become prompt-writers. Coding skills atrophy. When the AI generates a subtle concurrency bug that requires manual intervention, the developer can't diagnose it — because they never learned how the code works, or because they've forgotten. The task that remains after automation is the hardest task of all. And the automation itself ensures you're unprepared for it.

Annie Vella, a researcher at the University of Auckland, put empirical flesh on Bainbridge's skeleton. In a [longitudinal study of 158 professional software engineers across 28 countries](https://annievella.com/posts/the-middle-loop/), she tracked how AI tools were shifting where engineers spent their time. Five of six core development tasks — designing, writing, refactoring, testing, debugging, reviewing — showed participants reporting they spent *less* time on them. But the time didn't disappear. It migrated. Vella coined a term for where it went: ["supervisory engineering work — the effort required to direct AI, evaluate its output, and correct it when it's wrong."](https://annievella.com/posts/the-middle-loop/#:~:text=supervisory%20engineering%20work) Participants described the shift as "more design thinking," but their actual descriptions — directing, evaluating, correcting — were supervision, not creation. A qualitatively different form of work.

Martin Fowler, who highlighted Vella's research on his site, noted that improvements in AI models since her study finished have only [accelerated the shift to supervisory engineering](https://martinfowler.com/fragments/2026-03-16.html#:~:text=accelerated%20a%20shift%20to%20supervisory%20engineering). "This shift is a traumatic change to what we do and the skills we need," he wrote. "It doesn't mean 'the end of programming,' rather a change of what it means to be programming." The framing is precisely Bainbridge's irony, restated for 2026: the job is not disappearing. It is becoming harder — and we are less prepared for it.

A longitudinal neuroscience study offers a concrete analog. Dahmani and Bohbot (2020) tracked GPS users over three years and found that [greater lifetime GPS experience caused measurably worse spatial memory](https://www.nature.com/articles/s41598-020-62877-0#:~:text=greater%20lifetime%20GPS%20experience%20have%20worse%20spatial%20memory) — with the causal direction established. People didn't use GPS because they had bad spatial memory. GPS use *caused* the decline. The hippocampus, the brain structure responsible for spatial navigation, physically deteriorated with disuse.

Tim Requarth, a neuroscientist at NYU, sharpened this distinction in his essay ["Silicon Valley's Mythology of Human Amplification"](https://timrequarth.substack.com/p/silicon-valleys-mythology-of-human) — [highlighted by Fowler](https://martinfowler.com/fragments/2026-03-19.html). Steve Jobs called the computer "a bicycle for the mind." Satya Nadella, launching ChatGPT, upgraded the image: "we went from the bicycle to the steam engine." But as a cycling enthusiast wrote in 1878: with a bicycle, "you are traveling, not being traveled." A train passenger sits back. A cyclist puts in effort. Both arrive. Only one knows the road. Requarth's point: there is a difference between tools that extend capability and tools that replace it — between arriving with knowledge and arriving with nothing. Fowler, reflecting on this, [put it simply](https://martinfowler.com/fragments/2026-03-19.html#:~:text=I%20have%20no%20desire%20to%20let%20an%20LLM%20write%20this%20page): "I have no desire to let an LLM write this page."

The updated neuroscience on this point is more unsettling than the original "use it or lose it" framing. Recent work suggests that passivity is the *default* neural state. The [ability to exert control must be *learned* through practice](https://watchsound.medium.com/from-learned-dependence-to-learned-helplessness-effects-of-cognitive-offloading-in-the-ai-era-e0bc63b41dbe#:~:text=learned%20dependence%20into%20learned%20helplessness). Without experiencing agency — the struggle of debugging, the frustration of a failing test, the satisfaction of understanding *why* — the neural pathways for independent problem-solving never develop. For experienced developers, this means deskilling. For new developers who start with AI from day one, it means something worse: *non-skilling*. The capacity was never built.

There is a credible counterargument here, and it deserves honest engagement. The calculator wars of the 1970s–2000s produced the same fears: students would lose mental arithmetic. And a [2003 meta-analysis by Ellington](https://ivyleaguecenter.org/2024/03/12/over-reliance-on-calculators-a-heavy-burden-on-fundamental-education/#:~:text=premature%20introduction%20of%20calculators) found calculators caused "no apparent harm to math aptitude" when properly integrated. The key variable was pedagogy, not the tool.

But there's a difference between a calculator and an AI code generator that matters enormously. With a calculator, you can still see the problem and the answer. The abstraction is thin — a single arithmetic operation made faster. You type 247 × 18, you get 4,446, and you can verify by estimation that the answer is in the right ballpark. With vibe-coded software, the abstraction is total. You don't see the problem, the reasoning, or — often — the solution. You see an output and hope. It's not a tool augmenting your cognition. It's a tool replacing it.

Five independent research groups converged on the same finding in February 2026: [AI coding agents generate code 5–7x faster than human developers can comprehend it](https://byteiota.com/cognitive-debt-ai-coding-agents-outpace-comprehension-5-7x/#:~:text=5%E2%80%937x%20faster) — 140–200 lines of meaningful code per minute versus 20–40 for human reading. This is the comprehension gap quantified. The machine produces faster than the human can absorb. And unlike a calculator — where you can at least check the answer — a codebase is not one operation. It is thousands of interacting decisions, any of which could be wrong in ways that only manifest under specific conditions that testing may not cover.

Confidence in AI coding tools [dropped from 43% to 29%](https://byteiota.com/cognitive-debt-ai-coding-agents-outpace-comprehension-5-7x/#:~:text=5%E2%80%937x%20faster) in eighteen months. Usage climbed to 84%. People trust the tools less and use them more. That is the definition of dependency.

---

## III. The Forest Eating Its Soil

Individual deskilling is a personal problem. When it compounds across an industry, it becomes a structural one.

In the 1760s, the Kingdom of Saxony undertook what seemed like an obvious improvement: scientific forestry. The old forests were messy — a chaos of mixed species, undergrowth, deadwood, varied ages. Foresters couldn't even count the trees accurately, let alone optimize for timber yield. So they redesigned the forests. Monoculture rows. Single species. Uniform age. Clean lines. Maximum legibility for the bureaucrats who managed them.

James C. Scott's *Seeing Like a State* describes what happened next. The first generation of scientific forests were triumphant — [timber yields surged](https://en.wikipedia.org/wiki/Seeing_Like_a_State#:~:text=Formal%20order%20is%20always). The Prussian model spread across Europe. And then, a generation later, the forests began to die. The complex ecology that the scientific scheme "did not recognize" — the soil fungi, the insect populations, the nutrient cycling between species — turned out to be load-bearing. Removing the apparent disorder removed the invisible infrastructure. Scott called this destroyed knowledge *mētis* — the practical, local, informal understanding that formal systems depend on but cannot see, create, or maintain.

The parallel to AI-generated code is not metaphorical. It is structural.

Production codebases are full of what looks like disorder: mysterious null checks, weirdly specific timeouts, seemingly redundant database queries, exception handlers that catch errors that "should never happen." To an AI refactoring tool — or to a developer who has never worked in the codebase — these look like technical debt. Sloppy code to be cleaned up.

But experienced developers know that each of these is often a scar from a past battle. The null check exists because a specific customer's integration sends malformed data on the third Tuesday of every month. The timeout is set to 4,700 milliseconds because at 5,000 the upstream service sometimes drops the connection. The redundant query exists because a caching layer occasionally serves stale data and nobody could figure out why. This is Chesterton's Fence — the principle that you should [never remove a fence until you understand why it was built](https://fourweekmba.com/the-chestertons-fence-problem-ai-removing-things-it-doesnt-understand/#:~:text=Once%20AI%20removes%20Chesterton%27s%20Fences). AI sees a fence. It does not ask why.

Consider Roman concrete. The Pantheon has stood for nearly 2,000 years. Modern concrete, with maintenance, lasts about 100. In January 2023, MIT professor Admir Masic published a paper in *Science Advances* explaining why: Roman concrete contained lime clasts — white chunks created by ["hot mixing"](https://news.mit.edu/2023/roman-concrete-durability-lime-casts-0106#:~:text=hot%20mixing) raw quicklime directly with volcanic ash. When cracks formed, water seeped in, dissolved the lime, and recrystallized — a self-healing mechanism. For 1,500 years, modern scientists had examined these lime clasts and dismissed them as "evidence of sloppy mixing practices." The very feature that made Roman concrete superior was misidentified as a defect.

This is what happens when you lose the understanding of *why* something works. The feature becomes indistinguishable from the bug. The mētis disappears, and with it, the ability to tell order from disorder.

David Poll, who spent 5.5 years running the API council at Firebase, [makes a related point](https://martinfowler.com/fragments/2026-03-19.html#:~:text=Should%20this%20be%20part%20of%20my%20product) about the nature of code review. The most valuable feedback from that council was never "you have a bug in this spec." It was "this API implies a mental model that contradicts what you shipped last quarter" or "this deprecation strategy will cost more trust than the improvement is worth." Code review, properly understood, answers the question: "Should this be part of my product?" That is a judgment call — about coherence, about user trust, about strategic direction. No amount of production observability surfaces it, because the system can work perfectly and still be the wrong thing to have built. AI can catch bugs. It cannot yet judge whether the code *should exist*.

Now scale this dynamic from codebases to the industry itself.

In August 2025, economists Erik Brynjolfsson, Alex Chandar, and John Chen at the Stanford Digital Economy Lab published "Canaries in the Coal Mine," analyzing ADP payroll records for millions of U.S. workers. Their finding: [employment for software developers aged 22–25 declined nearly 20%](https://digitaleconomy.stanford.edu/wp-content/uploads/2025/08/Canaries_BrynjolfssonChandarChen.pdf#:~:text=employment%20for%20software%20developers%20aged%2022-25%20declined%20nearly%2020%25) from its late-2022 peak. Workers aged 30 and above in the same AI-exposed roles *grew* 6–13%. A [Harvard study](https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5425555#:~:text=junior%20employment%20declines%20sharply) by Guy Lichtinger and Seyed Mahdi Hosseini Maasoum, tracking 62 million workers across 285,000 firms, found junior employment dropping 9–10% within six quarters of companies adopting generative AI. Senior employment barely changed.

The numbers from Big Tech are starker. [Junior developers made up 32% of new hires in 2019. By 2026: 7%.](https://byteiota.com/developer-hiring-crisis-2026-40-worse-junior-drops-73/#:~:text=Junior%20hiring%20at%20Big%20Tech%20has%20collapsed) Entry-level developer opportunities are down approximately 67% since 2022. CS graduates now face 6.1% unemployment — nearly double the national average. Fifty-four percent of engineering leaders say they plan to hire fewer juniors due to AI copilots.

There is an agricultural term for this: eating the seed corn. You gain one season of extra food by consuming the grain set aside for next year's planting. Then there is no next year.

If you don't hire junior developers, you will someday never have senior developers. The pipeline that produces expertise — junior makes mistakes, senior explains why, junior absorbs tacit knowledge through practice and mentorship — is the apprenticeship chain that has transmitted craft knowledge for millennia. Stefania Druga called it ["the vanishing ladder of technical apprenticeship"](https://byteiota.com/developer-hiring-crisis-2026-40-worse-junior-drops-73/#:~:text=Junior%20hiring%20at%20Big%20Tech%20has%20collapsed) — AI eroding the structures that teach humans how to think, question, and build technical mastery.

AWS CEO Matt Garman [called replacing junior developers with AI](https://fortune.com/2025/12/16/aws-ceo-matt-garman-ai-displacing-junior-employees-dumbest-idea-amazon-layoffs/#:~:text=one%20of%20the%20dumbest%20things) "one of the dumbest things I've ever heard." He is not wrong. But fifty-four percent of his peers disagree.

The ecosystem damage extends beyond hiring. A [peer-reviewed analysis](https://arxiv.org/abs/2601.15494#:~:text=weakens%20the%20user%20engagement) published in January 2026 by researchers at Central European University, Bielefeld University, and the Kiel Institute found that vibe coding "decouples usage from engagement" with open-source software. AI agents select and assemble packages without developers reading documentation, filing bugs, or engaging with maintainers. Adam Wathan, creator of Tailwind CSS — one of the most popular open-source CSS frameworks — [disclosed in January 2026](https://devclass.com/2026/01/08/tailwind-labs-lays-off-75-percent-of-its-engineers-thanks-to-brutal-impact-of-ai/) that documentation traffic had dropped approximately 40% from early 2023 despite greater-than-ever usage. Revenue down 80%. The company laid off 75% of its engineering team.

This creates a doom loop: fewer engaged users means less motivation for maintainers, which means abandoned or degraded projects, which means AI tools have worse libraries to draw from, which means worse software. The ecosystem that made vibe coding possible is being consumed by vibe coding. The forest is eating its own soil.

There is a fair counterargument to all of this, and it should be stated plainly: comprehension was always partial. Before AI, most production codebases were barely understood by their maintainers. The average enterprise system is a geological formation — layers of code deposited by developers who left years ago, each layer only partially documented, each subsequent modification made with incomplete knowledge of the layers below. The "before" state was already messy. The golden age of full comprehension never existed.

This is true. But there was always a gradient back. You *could* read the code. You could step through it in a debugger. You could find the person who wrote it, or someone who worked with someone who wrote it. The knowledge was distributed across human minds but it *existed* in human minds. The comprehension was imperfect but real, and it could be rebuilt with effort.

What the 5–7x generation-to-comprehension gap creates is different in kind, not just degree. When code is produced faster than any human can absorb it — and when the people who might have understood it were never hired — the gradient back disappears. There is no person to ask. There is no institutional memory. There is the code, and there is the machine that wrote it. And as Osmani observed, nothing in current measurement systems captures this loss. Velocity metrics look immaculate. DORA metrics hold steady. PR counts are up. Code coverage is green. Organizations cannot see comprehension deficits because no artifact of how they measure output captures that dimension.

The forest looks fine. The soil is gone.

---

## IV. The Recursive Trap

Everything described so far — the deskilling, the pipeline collapse, the comprehension debt — has historical precedent. Civilizations have traded comprehension for capability before and survived. The question this section addresses is whether there is something categorically different about the current trade. I believe there is.

Consider the structure of every prior technology dependency:

Dependent on cars? You can walk. It's slow, but the capacity exists.
Dependent on GPS? You can read a map. The skill is rusty, but the tool is available.
Dependent on calculators? You can count on paper. It takes longer, but arithmetic doesn't vanish.
Dependent on writing? You can speak. Oral communication never disappeared.

In every case, the exit path from the dependency does not require the dependency itself. You can get back to the older, slower, less powerful mode without relying on the thing you're trying to exit.

Now: dependent on AI for understanding code? The only tool capable of analyzing a large AI-generated codebase at the speed required for production debugging is... AI. The exit requires the dependency.

This is what I call the recursive trap. The dependency is self-referential. And it has no obvious historical analog.

The closest parallel might be language itself. You cannot think about language without language. You cannot analyze your dependency on words using anything other than words. But language evolved *with* us — a co-adaptation over hundreds of thousands of years. The neural architecture for language is part of what makes us human. We had millennia to integrate it. AI code dependency is language-level entrenchment happening in months.

The recursive trap compounds through what might be called *incomprehension squared*. It is not merely that we don't understand the code AI generates. We don't understand the tool that generates it.

This is a historically unprecedented stack of opacity. [Three layers deep](https://www.anthropic.com/research/tracing-thoughts-language-model#:~:text=hours%20of%20human%20effort):

**Layer 1 — The model itself.** Nobody fully understands how frontier LLMs work. Not OpenAI. Not Anthropic. Not Google. Mechanistic interpretability — the attempt to reverse-engineer neural networks into human-understandable components — was named a [2026 Breakthrough Technology by MIT Technology Review](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/), reflecting both its importance and the urgency of the problem. Anthropic's own circuit-tracing research found it takes ["a few hours of human effort"](https://www.anthropic.com/research/tracing-thoughts-language-model#:~:text=hours%20of%20human%20effort) to understand the mechanisms behind prompts of tens of words. The leading interpretability technique — sparse autoencoders — was [deprioritized by Google DeepMind's safety team in March 2025](https://deepmindsafetyresearch.medium.com/negative-results-for-sparse-autoencoders-on-downstream-tasks-and-deprioritising-sae-research-6cadcfc125b9) after finding that SAE-reconstructed activations cause 10–40% performance degradation on downstream tasks, and that the technique underperformed simple linear probes on practical safety tasks like detecting harmful intent.

**Layer 2 — The training data.** We don't fully know what the models learned from. Web-scale datasets are too large to audit. Biases, errors, deprecated patterns, and security vulnerabilities in the training data propagate into generated code in ways nobody can trace.

**Layer 3 — The generated code.** Millions of lines now in production that no human wrote, no human reviewed in full, and no human fully understands.

An opaque system, trained on data we can't fully audit, produces code we don't read, which runs infrastructure we depend on. Compare this to every prior tool: a hammer — you understand the tool and its output. A calculator — you may not understand the circuitry, but you understand the math and can verify. A compiler — you may not understand every optimization pass, but you wrote the source code and can inspect the result. An LLM code generator — you don't understand the tool, you don't understand why it chose this particular implementation, and you may not understand the output. Opacity at every layer.

And the gap is widening, not closing. Models are getting bigger and more capable faster than interpretability research can keep up. The major AI labs can't even agree on whether interpretability is achievable at scale: Anthropic CEO Dario Amodei [aims to "reliably detect most AI model problems by 2027"](https://techcrunch.com/2025/04/24/anthropic-ceo-wants-to-open-the-black-box-of-ai-models-by-2027/#:~:text=reliably%20detect%20most%20AI%20model%20problems%20by%202027); Google DeepMind [deprioritized its leading technique](https://deepmindsafetyresearch.medium.com/negative-results-for-sparse-autoencoders-on-downstream-tasks-and-deprioritising-sae-research-6cadcfc125b9) after negative results; [OpenAI's Superalignment team was dissolved in May 2024](https://www.cnbc.com/2024/05/17/openai-superalignment-sutskever-leike.html), its head Jan Leike saying "safety culture and processes have taken a backseat to shiny products"; MIRI, the Machine Intelligence Research Institute, [effectively exited alignment research](https://intelligence.org/2024/01/04/miri-2024-mission-and-strategy-update/) and pivoted to governance advocacy, concluding that "the alignment problem is not on track to be solved" before smarter-than-human AI arrives. A [million-dollar bounty](https://www.technologyreview.com/2026/01/12/1130003/mechanistic-interpretability-ai-research-models-2026-breakthrough-technologies/) exists for progress on practical mechanistic interpretability. The existence of the bounty tells you how far the field has to go.

There is an objection worth engaging with here: "We don't understand the human brain either, but we trust human programmers." True. But human programmers can explain their reasoning. They have intent. You can ask them why they made a choice. An LLM's explanation of its own output is itself generated by the same opaque process — and Anthropic's research has shown that these explanations are sometimes [unfaithful](https://www.anthropic.com/research/tracing-thoughts-language-model#:~:text=hours%20of%20human%20effort): the model claims to perform a calculation with no internal evidence of the calculation occurring. When given answer hints, it works backward from the target. It doesn't explain. It confabulates.

The recursive trap creates a positive feedback loop with no natural governor. More AI-generated code enters production. Understanding it requires AI assistance. Using AI assistance generates more code. The human capacity for independent comprehension atrophies. More AI-generated code enters production.

There is a parallel to climate change here — but with a crucial difference. Climate change is a tragedy of the commons: individually rational decisions (burn fossil fuels) create collective catastrophic risk, the transition is gradual enough to be invisible day-to-day, there's no single villain, and by the time the damage is visible, the return path is closing. All of this applies to AI code dependency. But climate change does not make the tools for fixing climate change incomprehensible. Solar panels don't get harder to understand the more carbon you emit. AI dependency *does* make the tools for fixing AI dependency harder to use independently — because the more code AI generates, the more you need AI to understand it, the less capable you become of working without it. The problem and the solution are the same thing. That's the trap.

---

## V. The Terms of the Trade

If the loss of comprehension is the price of progress — and the historical record strongly suggests it is — then the question changes. It is no longer "should we pay?" We will pay. We always have. The question is whether the terms are fair.

Every prior comprehension trade that worked well for civilization shared certain features.

*The transition was slow enough for co-adaptation.* Writing emerged over millennia. Agriculture over centuries. Industrialization over decades. Each gave society time to develop institutions, norms, pedagogy, and corrective mechanisms. The printing press disrupted scriptoria — but it took generations, long enough for universities, copyright law, and journalism to evolve in response. Humans and their tools co-adapted.

*Collective comprehension survived even as individual comprehension was lost.* Nobody understands an entire jet engine. But the knowledge exists, distributed across thousands of engineers, in manuals, in training programs, in university curricula. The individual doesn't need to hold all of it. The collective does. And the collective can reconstitute any piece on demand — because it's stored in human minds and human artifacts, not in an opaque oracle.

*There was a path back, even if costly.* You can farm by hand. You can navigate by stars. You can do arithmetic on paper. The older, slower mode remains accessible. The dependency deepens, but it doesn't close behind you.

*The choice was made — imperfectly, incompletely, but recognizably — by the people affected.* Societies debated writing, printing, industrialization. Not always well. Not always in time. But there was at least a period of reckoning, of weighing gains against losses.

Now measure the current transition against these criteria.

**Speed.** AI coding tool adoption is measured in months. Karpathy posted his tweet in February 2025. By year's end, Collins Dictionary had named the concept its Word of the Year. Junior hiring had already collapsed. There is no time for co-adaptation. The deskilling is happening faster than pedagogy, policy, or professional norms can respond. The [vibe coding market grew from $2.96 billion in 2025 to a projected $12.3 billion by 2027](https://www.secondtalent.com/resources/vibe-coding-statistics/#:~:text=40%25%20fewer%20entry-level).

**Collective comprehension.** This is where the trade may be unprecedented. With prior technologies, individual comprehension was lost but collective comprehension survived — the knowledge remained in human minds, distributed but real. With AI-generated code, the "knowledge" exists in model weights. Model weights are non-deterministic (same prompt, different output), version-dependent (model update, different behavior), controlled by a third party (pricing, policy, shutdown risk), and resistant to inspection. This isn't a distributed repository of human knowledge. It's an oracle. When the oracle changes — and it will, with every model update — the "understanding" changes with it. There is no stable collective comprehension to fall back on.

**Reversibility.** The recursive trap, described in the previous section, suggests the path back may be closing. But more concretely: the apprenticeship pipeline is already breaking. Trade schools don't close and reopen on demand. Once the machinists retire and the curriculum is dropped, rebuilding takes a generation. The same dynamic applies to software: once the career ladder that produces experienced engineers is dismantled, you can't reassemble it by flipping a switch. Path dependence makes the trade progressively less reversible with each passing quarter.

**Who chooses.** This is perhaps the starkest departure. The transition to AI-generated code is not being debated. It is being marketed. The "choice" is made by shipping velocity, venture capital incentives, and quarterly earnings — not by democratic deliberation, professional consensus, or regulatory oversight. The companies that profit most from the dependency are the ones setting its terms. Every individual developer who adopts AI coding tools makes the locally rational choice. Collectively, they create an inescapable dependency that none of them voted for.

Against all of this stands a genuine, non-trivial case for hope. And it is worth stating without condescension.

Karpathy himself retreated. Within a year of coining "vibe coding," he called the original tweet ["a shower of thoughts throwaway tweet"](https://x.com/karpathy/status/2019137879310836075#:~:text=shower%20of%20thoughts%20throwaway%20tweet) and replaced the concept with ["agentic engineering"](https://thenewstack.io/vibe-coding-is-passe/) — adding *engineering* to emphasize that expertise, discipline, and structured oversight matter. "There is an art and science and expertise to it," he said. Even the coiner discovered that comprehension cannot be permanently outsourced. The vibes hit a wall.

In February 2026, about fifty practitioners, researchers, and technical leaders gathered in Deer Valley, Utah — the same mountains where the Agile Manifesto was signed twenty-five years earlier — for a workshop on [the future of software development](https://www.thoughtworks.com/en-us/about-us/events/the-future-of-software-development), hosted by Martin Fowler and Thoughtworks. They were often asked if they were writing a new manifesto. Fowler said no: "it's way too early" — "people are still experimenting with ideas, still trying stuff." But the conversations they had suggest that the profession is at least beginning to reckon with the terms of the trade.

The question that [surfaced in nearly every session](https://www.thoughtworks.com/en-us/insights/articles/reflections-future-software-engineering-retreat#:~:text=surfaced%20in%20nearly%20every%20session) was how to retain engineering discipline in the context of AI-driven development. One answer: test-driven development produces dramatically better results from AI coding agents, because when tests exist before the code, agents cannot cheat by writing tests that confirm broken behavior. Old discipline, it turns out, constrains new tools.

Chad Fowler, speaking at the same retreat, offered a more radical reframing. His concept of ["regenerative software"](https://www.linkedin.com/posts/fowlerchad_regenerative-software-activity-7408936914264698880-Edjv) accepts that AI-generated code will be disposable — but argues that this is a feature, not a bug, if the architecture is designed for it. "In a world where code can be generated quickly and cheaply, the real constraint has shifted. The problem is no longer producing code. The problem is replacing it safely." His "Phoenix Architecture" proposes systems built from components designed to be burned and regenerated, where the durable layer is not the code but the specifications, data ownership boundaries, and evaluation surfaces. "The most durable systems of the AI era will be built from code that is meant to die."

This is intellectually serious — and it concedes the central premise of this essay. If code is disposable, then comprehension of code is disposable too. What must be comprehended is the architecture, the specifications, the boundaries. The knowledge shifts up a layer of abstraction. The question is whether the humans maintain comprehension at *that* layer, or whether it, too, gets delegated.

Charity Majors, creator of Honeycomb and a leading voice on observability, pushed back on the Deer Valley retreat for [what it didn't discuss](https://martinfowler.com/fragments/2026-03-19.html#:~:text=relegating%20production%20to%20the%20realm%20of%20bugs%20and%20incidents). Fowler conceded the point and extended it: in a world of supervisory engineering, where humans no longer look over every semicolon, observability becomes not just useful but essential — perhaps the primary tool for understanding what AI-generated systems actually do. "I think it's likely we'll see a future where much of a developer's effort is figuring out what a system is doing and why it's behaving that way," he wrote, "where observability tools are the IDE." If you can't read the code, you watch the system. Production becomes the source of truth that source code used to be.

Anthropic's own deskilling study contained the seed of a different answer: AI used for *inquiry* preserved learning; AI used for *delegation* destroyed it. This maps to an emerging framework: the 70/30 rule. Use AI freely for 70% of coding — boilerplate, well-understood patterns, repetitive tasks. For the remaining 30% — novel problems, architecture decisions, debugging — work without the assistant first. Academic researchers at CHIWORK '26 have proposed ["purposeful friction"](https://arxiv.org/abs/2601.06030#:~:text=positive%20synergy%20in%20content%20creation) — designing AI tools that promote cognitive engagement rather than passive acceptance.

A major 2026 meta-review found that human-AI teams show [negative synergy in judgment and decision tasks](https://arxiv.org/abs/2601.06030#:~:text=positive%20synergy%20in%20content%20creation) but positive synergy in content creation and problem formulation. The distinction is precise: AI works when it augments human formulation. It fails when it replaces human judgment. The tool is not the problem. The relationship to the tool is the problem. And relationships can be designed.

But here is the honest caveat that the essay owes its reader: almost none of this is happening at scale. The market rewards speed. Friction is a cost. "Purposeful friction" is a research proposal, not a shipping product. Bainbridge showed in 1983 that when you automate the routine work, people don't actually do higher-order work — they become monitors. The liberation is theoretical; the deskilling is empirical. Learning modes have been introduced in some AI tools, which is an acknowledgment that the problem is real — but acknowledgment is not solution, and the incentive structure points away from slowness.

The question, then, is not whether the comprehension tax will be paid. It will. The question is whether we negotiate the terms — choosing what to automate and what to keep in human hands, building apprenticeship pipelines alongside automation, designing tools that teach rather than replace — or whether we accept whatever terms the market dictates. Right now, we are not negotiating. We are signing.

---

## VI. The Unsigned Contract

In the *Phaedrus*, Socrates warns that the written word will produce people who "appear as though they were all-knowing, but to actually be learners of nothing." Then Plato writes this down. He publishes it in dialogues — a literary form designed to preserve oral argument within the written medium. He uses the technology he mistrusts to articulate why he mistrusts it, because the alternative — letting the warning die unrecorded — would be worse.

We are in Plato's position. This essay was written with AI assistance. The author checked the diffs.

Michael Polanyi wrote in *The Tacit Dimension* (1966) that "we can know more than we can tell" — that tacit knowledge, the kind learned through practice rather than instruction, is the foundation of all expertise. Riding a bicycle. Recognizing a face. Debugging by instinct. You know how, but you cannot fully articulate how you know. Every prior technology preserved this tacit layer somewhere: in the craftsperson, the operator, the engineer. Someone always *knew*, even if they couldn't fully say.

AI-generated code inverts Polanyi's formulation. As Samuel Arbesman [observed](https://www.threadcounts.org/p/loom-xvii-the-polanyi-inversion#:~:text=We%20now%20can%20tell%20more%20than%20we%20know), we can now *tell* more than we know. The code exists. It runs. It produces outputs. But the tacit knowledge — the understanding of *why* it works, the instinct for where it might break, the hard-won intuition that comes from having built something yourself — was never formed. Not in the AI, which has no stable understanding. Not in the developer, who never wrote it. The artifact exists without the knowledge that would normally accompany it. The spell without the wizard.

This will be the condition of an increasing share of the infrastructure our civilization runs on. Not because the technology is too advanced to understand — we are not dealing with alien physics — but because we are choosing speed over comprehension, and the choice, once made enough times, becomes difficult to unmake.

The thing about a civilization that forgets how to code is not that everything breaks. That would be dramatic, visible, galvanizing. The thing is that everything keeps working — and nobody can tell you why. The dashboards are green. The metrics are up. The tests pass. And underneath, a gap is opening between what we have built and what we understand, growing wider with every commit, every accepted suggestion, every diff we don't read.

The trade is as old as civilization: capability for comprehension. We have always paid. We have generally paid well.

But we have never before signed the contract without reading it.

Accept all. Always.
