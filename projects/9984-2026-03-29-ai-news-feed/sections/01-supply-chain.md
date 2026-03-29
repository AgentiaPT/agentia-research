## 1. The Supply Chain Reckoning — LiteLLM, Trivy, and the TeamPCP Campaign

### The Attack Chain
**March 19–24 | [LiteLLM Security Update](https://docs.litellm.ai/blog/security-update-march-2026) · [Snyk](https://snyk.io/articles/poisoned-security-scanner-backdooring-litellm/) · [Datadog Security Labs](https://securitylabs.datadoghq.com/articles/litellm-compromised-pypi-teampcp-supply-chain-campaign/) · [The Hacker News](https://thehackernews.com/2026/03/teampcp-backdoors-litellm-versions.html) · [Kaspersky](https://www.kaspersky.com/blog/critical-supply-chain-attack-trivy-litellm-checkmarx-teampcp/55510/) · [Wiz](https://www.wiz.io/blog/threes-a-crowd-teampcp-trojanizes-litellm-in-continuation-of-campaign) · [SANS Institute](https://www.sans.org/blog/when-security-scanner-became-weapon-inside-teampcp-supply-chain-campaign)**

A threat group called **TeamPCP** turned a security scanner into a weapon — and used it to backdoor one of the most widely deployed AI proxy libraries in the world. The attack earned **CVE-2026-33634 (CVSS 9.4)** and represents the most sophisticated AI supply chain attack to date.

The timeline reads like a heist:

| Date | Step |
|------|------|
| **Feb 20** | A GitHub account called **hackerbot-claw** was created — a self-described "autonomous security research agent powered by claude-opus-4-5" using the **OpenClaw** attack framework. It loaded a vulnerability pattern index with 9 classes and 47 sub-patterns and began scanning public repos for exploitable CI/CD misconfigurations. |
| **Feb 28** | hackerbot-claw found that Trivy's `apidiff.yaml` workflow used the `pull_request_target` trigger — a [known dangerous pattern](https://www.stepsecurity.io/blog/hackerbot-claw-github-actions-exploitation) flagged since November 2025 but never fixed. The bot forked the repo, opened a PR, and extracted a Personal Access Token (PAT) for the `aqua-bot` service account with org-wide write access to all 33+ Aqua Security repositories. |
| **Mar 1** | Aqua Security disclosed the breach and rotated credentials — but **the rotation was incomplete**. The attacker retained access through tokens that survived the process. |
| **March 19** | Using surviving credentials, TeamPCP force-pushed malicious commits to 76 of 77 `trivy-action` release tags via the `aqua-bot` account. Any CI/CD pipeline referencing a Trivy tag silently pulled attacker code. |
| **March 20** | Stolen npm tokens fed a self-propagating worm (**CanisterWorm**) that infected 66+ npm packages. |
| **March 23** | Checkmarx KICS GitHub Actions compromised via the same stolen CI/CD secrets. |
| **March 24** | LiteLLM's CI/CD pipeline pulled the compromised Trivy without version pinning, which exfiltrated the `PYPI_PUBLISH` token. Two backdoored versions (1.82.7 and 1.82.8) were published to PyPI. |

The malware was a three-stage payload:

1. **Credential harvesting** — environment variables, SSH keys, cloud credentials, Kubernetes data, Docker configs, shell history, CI/CD secrets, and crypto wallets
2. **Data exfiltration** — AES-256 + RSA-4096 hybrid encryption to `models.litellm[.]cloud`
3. **Persistence** — a systemd unit (`sysmon.service`) beaconing to `checkmarx[.]zone/raw`

The most insidious detail: the malware abused Python's `.pth` file mechanism to execute on **every Python invocation**, regardless of whether LiteLLM was imported. Install the package once, and every Python process on the machine becomes a credential harvester.

### Scale and Response

LiteLLM has approximately **95 million monthly PyPI downloads** and is present in **36% of cloud environments** according to Wiz Research. The compromised versions were live for approximately **5.5 hours** (10:39–16:00 UTC on March 24) before PyPI quarantined the package. An estimated **500,000 credentials were reportedly stolen** according to SlowMist's analysis.

The attackers used **ICP blockchain canisters** as command-and-control infrastructure — the first documented abuse of decentralized infrastructure for supply chain C2. When community members reported the compromise in GitHub issue #24512, attackers reportedly flooded the thread with bot comments from compromised accounts to suppress the discussion.

Post-attack, TeamPCP reportedly pivoted to active extortion, working through ~300 GB of stolen credentials and collaborating with the **LAPSUS$** extortion group. LiteLLM paused all new releases pending a full supply-chain review. Customers using the official Docker image were unaffected due to pinned dependencies.

### The Broader Pattern

The HiddenLayer 2026 AI Threat Landscape Report (March 19) found that **autonomous agents now account for more than 1 in 8 reported AI breaches**. Malware in public model and code repositories was the most cited breach source (35%), yet **93% of respondents still use open repositories**. The LiteLLM attack validates every concern in that report — and adds a new one: your security scanner can be the attack vector.

**Why this matters:** An AI agent found the vulnerability in a security tool, which was then weaponized to backdoor an AI proxy library. The attack didn't exploit a bug in LiteLLM's code — it exploited the **trust chain**: an unpinned dependency on a security scanner that itself was compromised by an autonomous bot. hackerbot-claw represents something new: **AI agents as offensive security tools**, systematically scanning for CI/CD misconfigurations at a scale no human team could match. The vulnerability in `apidiff.yaml` had been flagged for three months. A human attacker might never have found it. An AI agent scanning 47 vulnerability patterns across thousands of repos found it in days.
