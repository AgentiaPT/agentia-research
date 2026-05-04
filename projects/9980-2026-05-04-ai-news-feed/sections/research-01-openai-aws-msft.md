# Research: OpenAI on AWS + Microsoft–OpenAI Restructure

## Key Facts

- OpenAI's GPT-5.5, Codex, and Managed Agents are now available on AWS via Amazon Bedrock (limited preview as of Apr 28, 2026)
- Microsoft's ~7-year exclusive cloud deal with OpenAI has ended; OpenAI can now serve models on any cloud provider
- The "AGI clause" — which would have triggered a re-evaluation of Microsoft's rights if OpenAI declared AGI — has been removed entirely
- Microsoft's IP license to OpenAI models now runs through 2032 on fixed calendar dates, not tied to technical milestones
- OpenAI maintains a capped 20% revenue share back to Microsoft until 2030
- Microsoft no longer shares revenue with OpenAI for Azure-hosted products
- Azure remains first-ship partner (OpenAI products still ship first on Azure unless Azure cannot support the capability)
- Amazon invested $50 billion in OpenAI as part of the deal; part of OpenAI's $110B funding round (Feb 2026, also backed by SoftBank, Nvidia)
- The AWS deal includes a $138B eight-year cloud infrastructure contract and access to 2 GW of compute capacity (including Amazon's custom AI chips)
- GPT-5.5 pricing on Bedrock aligns with OpenAI's direct API: $5/M input tokens, $30/M output tokens (standard tier); batch/flex at 50% off; 1M context window
- Codex pricing matches GPT-5.5 tiers; a lighter GPT-5.2-Codex variant available at $1.75/M input, $14/M output
- AWS enterprise customers can apply existing cloud commitments toward OpenAI model usage

## Timeline

- **2019** — Microsoft's original exclusive cloud partnership with OpenAI begins
- **Feb 27, 2026** — OpenAI announces $110B funding round; Amazon's $50B investment disclosed
- **Apr 27, 2026** — Microsoft–OpenAI amended deal takes effect: exclusivity ends, AGI clause removed
- **Apr 28, 2026** — OpenAI models (GPT-5.5, GPT-5.4, Codex, Managed Agents) go live on Amazon Bedrock in limited preview
- **2030** — OpenAI's capped 20% revenue share to Microsoft expires
- **2032** — Microsoft's IP license to OpenAI models expires under new terms

## Sources

- [OpenAI Models on Amazon Bedrock (AWS official)](https://www.aboutamazon.com/news/aws/bedrock-openai-models) — announcement of GPT-5.5, Codex, and agents on Bedrock
- [OpenAI frontier models on Amazon Bedrock (AWS product page)](https://aws.amazon.com/bedrock/openai/) — technical details and integration info
- [Microsoft Loses OpenAI Exclusivity and AGI Clause in Amended Deal (Unite.AI)](https://www.unite.ai/microsoft-loses-openai-exclusivity-and-agi-clause-in-amended-deal/) — restructure analysis
- [Microsoft and OpenAI gut their exclusive deal (VentureBeat)](https://venturebeat.com/technology/microsoft-and-openai-gut-their-exclusive-deal-freeing-openai-to-sell-on-aws-and-google-cloud) — reporting on exclusivity ending
- [Amazon invests $50B in OpenAI, deepens AWS partnership (GeekWire)](https://www.geekwire.com/2026/amazon-invests-50b-in-openai-deepens-aws-partnership-with-expanded-100b-cloud-deal/) — investment and infrastructure details
- [OpenAI announces $110B funding round backed by Amazon, Nvidia (CNBC)](https://www.cnbc.com/2026/02/27/open-ai-funding-round-amazon.html) — funding round context
- [GPT-5.5 Pricing Breakdown (Apidog)](https://apidog.com/blog/gpt-5-5-pricing/) — detailed token pricing across tiers
- [Microsoft-OpenAI Deal Restructured: 4 Changes (MindStudio)](https://www.mindstudio.ai/blog/microsoft-openai-deal-restructured-4-changes-aws-bedrock) — developer impact analysis

## Impact / Why It Matters

- **Multi-cloud choice for developers**: Enterprises locked into AWS no longer need a separate Azure account to access OpenAI's best models; they can use existing IAM, VPC, and compliance tooling
- **Competitive pressure on model pricing**: AWS, Azure, and Google Cloud all competing to host OpenAI models creates downward pricing pressure and better terms for customers
- **End of vendor lock-in risk**: The AGI clause created legal uncertainty — if OpenAI declared AGI, Microsoft's rights could have changed overnight; that risk is now eliminated for all partners
- **Revenue model clarity**: Fixed calendar dates (2030 revenue share, 2032 IP license) replace ambiguous milestone triggers — better for investors and enterprise planning
- **Signal for the industry**: The largest AI lab choosing multi-cloud distribution validates that cloud-agnostic AI deployment is the future standard, not single-vendor lock-in
- **AWS becomes an AI model marketplace**: Bedrock now hosts Anthropic Claude, Meta Llama, Mistral, AND OpenAI models — one-stop shop for enterprise AI
- **OpenAI's path to IPO**: Breaking exclusivity and diversifying cloud revenue makes OpenAI a more independent, investable entity ahead of a potential public offering
