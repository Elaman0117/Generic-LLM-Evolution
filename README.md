# LLM Leaderboard — 综合能力 vs 发布时间

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.2422，即前沿左端点 GPT-4）为 0：综合能力 ≥ 该级的 430 个模型入图，154 个能力低于第一级的不出现在图中；发布时间大于品牌前沿最大值的模型同样不入图（表列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 发布时间 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max with fallback) | 1.0000 | 2026-09-22 | 0.9767 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh with fallback) | 0.9942 | 2026-09-22 | 0.9767 | ❌ |
| 3 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (max with fallback) | 0.9793 | 2026-09-28 | 0.9941 | ❌ |
| 4 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 0.9777 | 2026-09-01 | 0.9180 | ✅ |
| 5 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9709 | 2026-09-01 | 0.9180 | ❌ |
| 6 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9667 | 2026-09-03 | 0.9234 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9624 | 2026-09-03 | 0.9234 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 4 Argon (high) | 0.9597 | 2026-09-30 | 1.0000 | ❌ |
| 9 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high with fallback) | 0.9531 | 2026-09-22 | 0.9767 | ❌ |
| 10 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9439 | 2026-09-03 | 0.9234 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9388 | 2026-07-24 | 0.8179 | ✅ |
| 12 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9386 | 2026-09-01 | 0.9180 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (max) | 0.9364 | 2026-09-29 | 0.9971 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (xhigh) | 0.9277 | 2026-09-29 | 0.9971 | ❌ |
| 15 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9242 | 2026-07-24 | 0.8179 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9225 | 2026-06-09 | 0.7156 | ✅ |
| 17 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium with fallback) | 0.9209 | 2026-09-22 | 0.9767 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9206 | 2026-09-03 | 0.9234 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (high) | 0.9179 | 2026-09-29 | 0.9971 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9106 | 2026-07-24 | 0.8179 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9096 | 2026-07-09 | 0.7823 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.8999 | 2026-09-01 | 0.9180 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (xhigh with fallback) | 0.8950 | 2026-09-28 | 0.9941 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (medium) | 0.8851 | 2026-09-29 | 0.9971 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8772 | 2026-09-03 | 0.9234 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.8769 | 2026-09-22 | 0.9767 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.8725 | 2026-09-02 | 0.9207 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.8672 | 2026-09-02 | 0.9207 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8626 | 2026-09-01 | 0.9180 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8598 | 2026-07-24 | 0.8179 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8537 | 2026-07-09 | 0.7823 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8530 | 2026-08-18 | 0.8808 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.8488 | 2026-09-02 | 0.9207 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8444 | 2026-09-02 | 0.9207 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8435 | 2026-07-09 | 0.7823 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8397 | 2026-07-16 | 0.7988 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8362 | 2026-04-23 | 0.6220 | ✅ |
| 38 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8361 | 2026-08-12 | 0.8653 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8309 | 2026-08-12 | 0.8653 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8305 | 2026-07-09 | 0.7823 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8249 | 2026-05-28 | 0.6905 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.8215 | 2026-09-21 | 0.9738 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6.1 Sol (low) | 0.8189 | 2026-09-29 | 0.9971 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.8181 | 2026-09-22 | 0.9767 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.8161 | 2026-09-18 | 0.9652 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8135 | 2026-08-12 | 0.8653 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8131 | 2026-04-16 | 0.6091 | ✅ |
| 48 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.8070 | 2026-08-26 | 0.9018 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8063 | 2026-03-05 | 0.5370 | ✅ |
| 50 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8028 | 2026-04-23 | 0.6220 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8028 | 2026-09-02 | 0.9207 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8025 | 2026-07-09 | 0.7823 | ❌ |
| 53 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (high with fallback) | 0.8012 | 2026-09-28 | 0.9941 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8010 | 2026-08-13 | 0.8678 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.8003 | 2026-09-21 | 0.9738 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.7984 | 2026-08-03 | 0.8425 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.7950 | 2026-09-21 | 0.9738 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.7940 | 2026-09-22 | 0.9767 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low with fallback) | 0.7923 | 2026-09-22 | 0.9767 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.7911 | 2026-08-13 | 0.8678 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7870 | 2026-05-19 | 0.6722 | ❌ |
| 62 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7869 | 2026-02-05 | 0.4935 | ✅ |
| 63 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.7771 | 2026-07-24 | 0.8179 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.7725 | 2026-08-12 | 0.8653 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.7699 | 2026-08-05 | 0.8475 | ❌ |
| 66 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.7694 | 2026-06-30 | 0.7617 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (high) | 0.7683 | 2026-05-19 | 0.6722 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.7636 | 2026-07-08 | 0.7800 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.7609 | 2026-09-22 | 0.9767 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.7577 | 2026-07-09 | 0.7823 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.7567 | 2026-04-23 | 0.6220 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.7527 | 2026-06-16 | 0.7307 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (low) | 0.7501 | 2026-09-21 | 0.9738 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7477 | 2026-08-26 | 0.9018 | ❌ |
| 75 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7468 | 2026-02-19 | 0.5148 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7453 | 2026-08-13 | 0.8678 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7448 | 2026-02-05 | 0.4935 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7413 | 2026-04-07 | 0.5929 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7294 | 2025-11-18 | 0.3882 | ✅ |
| 80 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7274 | 2026-04-30 | 0.6351 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7262 | 2026-07-09 | 0.7823 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7248 | 2026-04-08 | 0.5947 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7231 | 2026-07-09 | 0.7823 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7166 | 2025-12-11 | 0.4164 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7163 | 2026-07-09 | 0.7823 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7161 | 2025-12-11 | 0.4164 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash (high) | 0.7152 | 2026-07-21 | 0.8107 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7150 | 2026-04-20 | 0.6164 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7128 | 2026-07-09 | 0.7823 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (medium with fallback) | 0.7101 | 2026-09-28 | 0.9941 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7071 | 2026-09-02 | 0.9207 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7020 | 2026-03-10 | 0.5451 | ❌ |
| 93 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7012 | 2025-11-24 | 0.3954 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7003 | 2026-08-13 | 0.8678 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.6982 | 2026-04-23 | 0.6220 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (non-reasoning, high) | 0.6961 | 2026-04-16 | 0.6091 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.6938 | 2026-09-10 | 0.9427 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.6855 | 2025-12-17 | 0.4241 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.6821 | 2026-08-12 | 0.8653 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.6811 | 2026-05-19 | 0.6722 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.6807 | 2026-09-22 | 0.9767 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.6806 | 2026-09-22 | 0.9767 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6785 | 2026-03-05 | 0.5370 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6775 | 2026-08-12 | 0.8653 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.6745 | 2026-08-14 | 0.8704 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.6715 | 2026-04-20 | 0.6164 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6706 | 2026-04-02 | 0.5841 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6702 | 2026-04-30 | 0.6351 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6674 | 2026-03-18 | 0.5584 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.6674 | 2026-07-09 | 0.7823 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6646 | 2026-08-21 | 0.8886 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6645 | 2026-07-31 | 0.8351 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6622 | 2025-12-11 | 0.4164 | ❌ |
| 114 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6568 | 2026-02-17 | 0.5117 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6558 | 2026-04-24 | 0.6239 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6489 | 2025-09-23 | 0.3267 | ✅ |
| 117 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6441 | 2026-07-09 | 0.7823 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6439 | 2026-02-11 | 0.5025 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6427 | 2026-07-16 | 0.7988 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6423 | 2026-04-24 | 0.6239 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Flash | 0.6419 | 2026-09-21 | 0.9738 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.6401 | 2026-06-01 | 0.6988 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5.5 (low with fallback) | 0.6379 | 2026-09-28 | 0.9941 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6366 | 2025-11-13 | 0.3823 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6321 | 2026-06-01 | 0.6988 | ❌ |
| 126 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.6319 | 2026-09-22 | 0.9767 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6308 | 2025-11-13 | 0.3823 | ❌ |
| 128 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6288 | 2026-07-09 | 0.7823 | ❌ |
| 129 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6210 | 2026-03-27 | 0.5737 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6205 | 2026-04-07 | 0.5929 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6189 | 2025-08-07 | 0.2823 | ✅ |
| 132 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6184 | 2026-06-30 | 0.7617 | ❌ |
| 133 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (non-reasoning, high) | 0.6116 | 2026-02-05 | 0.4935 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6112 | 2026-03-15 | 0.5534 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.6097 | 2026-07-14 | 0.7940 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6094 | 2025-07-10 | 0.2585 | ✅ |
| 137 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.6057 | 2026-09-03 | 0.9234 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (low) | 0.6045 | 2026-08-18 | 0.8808 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6030 | 2026-06-12 | 0.7220 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6026 | 2026-06-16 | 0.7307 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6021 | 2026-04-30 | 0.6351 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nex.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.6018 | 2026-06-02 | 0.7009 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6006 | 2026-05-05 | 0.6447 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.5998 | 2026-09-22 | 0.9767 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.5989 | 2025-05-22 | 0.2213 | ✅ |
| 146 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.5981 | 2026-03-17 | 0.5567 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.5915 | 2025-08-07 | 0.2823 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5895 | 2026-05-19 | 0.6722 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5893 | 2026-02-24 | 0.5226 | ❌ |
| 150 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5890 | 2025-12-16 | 0.4228 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5868 | 2026-03-19 | 0.5601 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5862 | 2025-04-16 | 0.1971 | ✅ |
| 153 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.5855 | 2026-04-22 | 0.6201 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5842 | 2026-08-12 | 0.8653 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.5841 | 2026-07-09 | 0.7823 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5824 | 2026-04-01 | 0.5823 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (non-reasoning) | 0.5810 | 2026-07-09 | 0.7823 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.5808 | 2026-04-24 | 0.6239 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.5795 | 2026-09-10 | 0.9427 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.5786 | 2026-04-22 | 0.6201 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.5779 | 2026-06-30 | 0.7617 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.5776 | 2026-01-27 | 0.4803 | ❌ |
| 163 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5769 | 2025-08-07 | 0.2823 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5744 | 2025-08-05 | 0.2805 | ❌ |
| 165 | <img src="https://artificialanalysis.ai/img/logos//img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.5741 | 2026-08-30 | 0.9126 | ❌ |
| 166 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, high) | 0.5727 | 2026-02-17 | 0.5117 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5722 | 2025-11-06 | 0.3742 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (non-reasoning) | 0.5702 | 2025-11-24 | 0.3954 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (non-reasoning) | 0.5697 | 2026-06-30 | 0.7617 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling (xhigh) | 0.5673 | 2026-07-15 | 0.7964 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (non-reasoning, low) | 0.5673 | 2026-02-17 | 0.5117 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (non-reasoning) | 0.5651 | 2026-04-20 | 0.6164 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5640 | 2025-11-18 | 0.3882 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.5639 | 2026-03-17 | 0.5567 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.5622 | 2026-09-22 | 0.9767 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking-machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.5606 | 2026-07-30 | 0.8326 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5597 | 2026-08-10 | 0.8602 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.5591 | 2026-08-06 | 0.8500 | ❌ |
| 179 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.5564 | 2026-04-24 | 0.6239 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5556 | 2025-11-13 | 0.3823 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B (non-reasoning) | 0.5550 | 2026-07-09 | 0.7823 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5547 | 2026-04-22 | 0.6201 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5517 | 2025-08-07 | 0.2823 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5517 | 2026-04-23 | 0.6220 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5476 | 2025-09-29 | 0.3329 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5463 | 2026-02-12 | 0.5040 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5456 | 2026-08-14 | 0.8704 | ❌ |
| 188 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (non-reasoning) | 0.5452 | 2026-04-07 | 0.5929 | ❌ |
| 189 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5450 | 2026-06-04 | 0.7050 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5449 | 2026-03-30 | 0.5789 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5380 | 2025-11-19 | 0.3894 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5373 | 2026-02-16 | 0.5102 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5328 | 2026-03-27 | 0.5737 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (medium) | 0.5321 | 2026-03-17 | 0.5567 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sktelecom.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5317 | 2026-08-12 | 0.8653 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5313 | 2026-08-14 | 0.8704 | ❌ |
| 197 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5312 | 2025-12-23 | 0.4319 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5311 | 2026-01-26 | 0.4788 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5309 | 2026-03-18 | 0.5584 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5279 | 2026-07-06 | 0.7754 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5270 | 2026-07-21 | 0.8107 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5258 | 2026-02-24 | 0.5226 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5224 | 2026-07-09 | 0.7823 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5216 | 2026-05-29 | 0.6926 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (non-reasoning) | 0.5205 | 2026-01-27 | 0.4803 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5193 | 2025-12-16 | 0.4228 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5181 | 2026-03-17 | 0.5567 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5173 | 2026-09-03 | 0.9234 | ❌ |
| 209 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5143 | 2025-12-22 | 0.4306 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5135 | 2025-12-01 | 0.4039 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (non-reasoning) | 0.5135 | 2025-12-17 | 0.4241 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (non-reasoning) | 0.5125 | 2026-09-22 | 0.9767 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (non-reasoning) | 0.5093 | 2026-02-11 | 0.5025 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5093 | 2026-08-20 | 0.8860 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5070 | 2026-04-16 | 0.6091 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5064 | 2026-06-30 | 0.7617 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (non-reasoning) | 0.5062 | 2026-04-23 | 0.6220 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (non-reasoning) | 0.5026 | 2026-02-16 | 0.5102 | ❌ |
| 219 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.5025 | 2026-04-02 | 0.5841 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.4982 | 2026-02-24 | 0.5226 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4961 | 2025-09-19 | 0.3227 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.4955 | 2025-05-22 | 0.2213 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4892 | 2025-02-19 | 0.1641 | ✅ |
| 224 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (non-reasoning) | 0.4878 | 2026-02-24 | 0.5226 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (non-reasoning) | 0.4874 | 2025-09-29 | 0.3329 | ❌ |
| 226 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4866 | 2025-12-01 | 0.4039 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4856 | 2026-05-14 | 0.6623 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4848 | 2026-02-02 | 0.4891 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.4828 | 2026-09-11 | 0.9455 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4818 | 2026-08-12 | 0.8653 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.4785 | 2026-08-04 | 0.8450 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (non-reasoning) | 0.4755 | 2026-08-14 | 0.8704 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.4754 | 2026-04-02 | 0.5841 | ❌ |
| 234 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (non-reasoning) | 0.4725 | 2026-03-05 | 0.5370 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4722 | 2025-10-26 | 0.3617 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4689 | 2025-11-11 | 0.3799 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.4688 | 2025-08-07 | 0.2823 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4686 | 2025-04-16 | 0.1971 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4686 | 2024-12-05 | 0.1271 | ✅ |
| 240 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4675 | 2026-08-10 | 0.8602 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Mini 4 | 0.4670 | 2026-09-22 | 0.9767 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.4660 | 2026-07-09 | 0.7823 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.4659 | 2026-09-22 | 0.9767 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (non-reasoning) | 0.4601 | 2026-06-16 | 0.7307 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (non-reasoning) | 0.4574 | 2026-04-24 | 0.6239 | ❌ |
| 246 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (non-reasoning) | 0.4545 | 2026-04-22 | 0.6201 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4532 | 2025-02-24 | 0.1669 | ❌ |
| 248 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4520 | 2026-06-25 | 0.7505 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (non-reasoning) | 0.4504 | 2025-05-22 | 0.2213 | ❌ |
| 250 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4486 | 2026-06-30 | 0.7617 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4474 | 2026-04-29 | 0.6333 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4462 | 2026-05-08 | 0.6505 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4448 | 2025-09-25 | 0.3288 | ❌ |
| 254 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4405 | 2025-09-29 | 0.3329 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4398 | 2025-11-27 | 0.3990 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4396 | 2025-11-11 | 0.3799 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (non-reasoning) | 0.4382 | 2025-12-11 | 0.4164 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (non-reasoning) | 0.4364 | 2026-09-10 | 0.9427 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4363 | 2025-10-15 | 0.3497 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4355 | 2026-05-20 | 0.6742 | ❌ |
| 261 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (non-reasoning) | 0.4352 | 2026-07-09 | 0.7823 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (non-reasoning) | 0.4344 | 2026-02-24 | 0.5226 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4334 | 2025-06-05 | 0.2314 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4324 | 2026-09-03 | 0.9234 | ❌ |
| 265 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (non-reasoning) | 0.4301 | 2025-02-24 | 0.1669 | ❌ |
| 266 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4291 | 2025-11-03 | 0.3707 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4240 | 2025-05-20 | 0.2199 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4238 | 2025-10-29 | 0.3651 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4195 | 2026-06-29 | 0.7595 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (non-reasoning) | 0.4190 | 2026-04-22 | 0.6201 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (non-reasoning) | 0.4188 | 2025-10-15 | 0.3497 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4168 | 2026-04-02 | 0.5841 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4161 | 2025-09-05 | 0.3090 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4155 | 2025-11-13 | 0.3823 | ❌ |
| 275 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (non-reasoning) | 0.4148 | 2026-04-24 | 0.6239 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.4147 | 2025-09-23 | 0.3267 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4135 | 2025-11-27 | 0.3990 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4129 | 2025-09-22 | 0.3257 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (non-reasoning) | 0.4123 | 2026-03-10 | 0.5451 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4119 | 2026-04-23 | 0.6220 | ❌ |
| 281 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4112 | 2026-03-03 | 0.5338 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4084 | 2025-11-26 | 0.3978 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (non-reasoning) | 0.4062 | 2025-12-01 | 0.4039 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (non-reasoning) | 0.4044 | 2026-04-23 | 0.6220 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4043 | 2025-08-07 | 0.2823 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4022 | 2025-08-07 | 0.2823 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (non-reasoning) | 0.4014 | 2025-12-22 | 0.4306 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4002 | 2025-11-26 | 0.3978 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (non-reasoning) | 0.3998 | 2026-04-16 | 0.6091 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.3964 | 2026-03-02 | 0.5321 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (non-reasoning) | 0.3963 | 2026-04-07 | 0.5929 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3947 | 2025-09-30 | 0.3339 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.3931 | 2026-04-09 | 0.5965 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3928 | 2025-08-21 | 0.2949 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3922 | 2025-07-28 | 0.2736 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3878 | 2026-06-03 | 0.7029 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.3871 | 2026-03-02 | 0.5321 | ❌ |
| 298 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.3868 | 2025-10-29 | 0.3651 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3864 | 2025-09-23 | 0.3267 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3836 | 2025-08-28 | 0.3014 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3826 | 2025-07-11 | 0.2594 | ❌ |
| 302 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3812 | 2025-05-28 | 0.2256 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3779 | 2025-12-31 | 0.4425 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (non-reasoning) | 0.3756 | 2025-09-25 | 0.3288 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B (non-reasoning) | 0.3742 | 2026-04-02 | 0.5841 | ❌ |
| 306 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3728 | 2025-08-07 | 0.2823 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.3719 | 2025-10-21 | 0.3562 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (non-reasoning) | 0.3715 | 2026-02-24 | 0.5226 | ❌ |
| 309 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3709 | 2025-04-14 | 0.1958 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (non-reasoning) | 0.3692 | 2025-11-13 | 0.3823 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3689 | 2025-10-29 | 0.3651 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (non-reasoning) | 0.3688 | 2025-12-16 | 0.4228 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3678 | 2026-01-19 | 0.4688 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (non-reasoning) | 0.3643 | 2025-09-30 | 0.3339 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3642 | 2026-08-25 | 0.8992 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3605 | 2025-09-30 | 0.3339 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (non-reasoning) | 0.3600 | 2026-04-30 | 0.6351 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (non-reasoning) | 0.3579 | 2026-03-02 | 0.5321 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3566 | 2026-03-30 | 0.5789 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (non-reasoning) | 0.3565 | 2026-09-22 | 0.9767 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3556 | 2025-07-22 | 0.2685 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3546 | 2025-09-25 | 0.3288 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepcogito.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3543 | 2025-11-18 | 0.3882 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3537 | 2026-03-11 | 0.5468 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (non-reasoning) | 0.3517 | 2026-07-09 | 0.7823 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3503 | 2025-11-25 | 0.3966 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3497 | 2026-02-20 | 0.5164 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (non-reasoning) | 0.3492 | 2026-04-02 | 0.5841 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3487 | 2025-02-19 | 0.1641 | ❌ |
| 330 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3479 | 2025-12-08 | 0.4126 | ❌ |
| 331 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (non-reasoning) | 0.3472 | 2025-09-22 | 0.3257 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3447 | 2026-03-19 | 0.5601 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3431 | 2025-08-07 | 0.2823 | ❌ |
| 334 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (non-reasoning) | 0.3425 | 2026-08-13 | 0.8678 | ❌ |
| 335 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.3372 | 2026-09-03 | 0.9234 | ❌ |
| 336 | <img src="https://artificialanalysis.ai/img/logos//img/logos/arcee.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3371 | 2026-04-01 | 0.5823 | ❌ |
| 337 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3363 | 2025-09-18 | 0.3217 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3360 | 2025-09-05 | 0.3090 | ❌ |
| 339 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3305 | 2026-09-07 | 0.9344 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (non-reasoning) | 0.3297 | 2025-09-29 | 0.3329 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (non-reasoning) | 0.3273 | 2025-09-25 | 0.3288 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3270 | 2026-08-11 | 0.8627 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (non-reasoning) | 0.3265 | 2025-08-21 | 0.2949 | ❌ |
| 344 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3260 | 2026-08-06 | 0.8500 | ❌ |
| 345 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3229 | 2025-08-05 | 0.2805 | ❌ |
| 346 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3227 | 2025-08-20 | 0.2940 | ❌ |
| 347 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3199 | 2025-07-25 | 0.2710 | ❌ |
| 348 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (non-reasoning) | 0.3171 | 2025-05-20 | 0.2199 | ❌ |
| 349 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3157 | 2024-08-06 | 0.0825 | ✅ |
| 350 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3156 | 2026-07-23 | 0.8155 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.3153 | 2025-07-21 | 0.2677 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3128 | 2025-06-17 | 0.2404 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (non-reasoning) | 0.3090 | 2025-11-19 | 0.3894 | ❌ |
| 354 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3082 | 2025-08-07 | 0.2823 | ❌ |
| 355 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3080 | 2026-06-09 | 0.7156 | ❌ |
| 356 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3075 | 2026-03-16 | 0.5550 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B (non-reasoning) | 0.3069 | 2026-06-03 | 0.7029 | ❌ |
| 358 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3063 | 2025-09-23 | 0.3267 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3045 | 2025-03-05 | 0.1719 | ❌ |
| 360 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3034 | 2025-10-13 | 0.3476 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3034 | 2026-05-25 | 0.6844 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (non-reasoning) | 0.3032 | 2026-05-25 | 0.6844 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.3026 | 2025-12-15 | 0.4215 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3021 | 2024-11-18 | 0.1198 | ❌ |
| 365 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.2987 | 2025-12-17 | 0.4241 | ❌ |
| 366 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.2959 | 2026-05-26 | 0.6864 | ❌ |
| 367 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2958 | 2025-01-31 | 0.1541 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2952 | 2025-07-28 | 0.2736 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2951 | 2025-06-17 | 0.2404 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (non-reasoning) | 0.2925 | 2026-03-17 | 0.5567 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (non-reasoning) | 0.2922 | 2026-03-02 | 0.5321 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.2905 | 2024-11-20 | 0.1206 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china-mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2905 | 2026-04-15 | 0.6073 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2903 | 2025-09-11 | 0.3148 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2886 | 2025-05-07 | 0.2109 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2882 | 2025-06-17 | 0.2404 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos//img/logos/naver.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2881 | 2025-12-26 | 0.4359 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (non-reasoning) | 0.2864 | 2025-09-19 | 0.3227 | ❌ |
| 379 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.2859 | 2025-12-05 | 0.4089 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (non-reasoning) | 0.2856 | 2025-12-31 | 0.4425 | ❌ |
| 381 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (non-reasoning) | 0.2852 | 2026-03-17 | 0.5567 | ❌ |
| 382 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.2851 | 2026-02-03 | 0.4905 | ❌ |
| 383 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (non-reasoning) | 0.2846 | 2025-11-27 | 0.3990 | ❌ |
| 384 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2829 | 2025-12-11 | 0.4164 | ❌ |
| 385 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.2825 | 2026-04-06 | 0.5911 | ❌ |
| 386 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.2815 | 2026-08-25 | 0.8992 | ❌ |
| 387 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.2805 | 2025-01-31 | 0.1541 | ❌ |
| 388 | <img src="https://artificialanalysis.ai/img/logos//img/logos/prime-intellect.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2762 | 2025-11-27 | 0.3990 | ❌ |
| 389 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2760 | 2026-06-10 | 0.7178 | ❌ |
| 390 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2753 | 2026-02-10 | 0.5010 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2737 | 2026-01-28 | 0.4817 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2734 | 2025-10-03 | 0.3370 | ❌ |
| 393 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2729 | 2025-08-05 | 0.2805 | ❌ |
| 394 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2718 | 2024-07-23 | 0.0782 | ✅ |
| 395 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2710 | 2025-04-30 | 0.2062 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2706 | 2026-04-21 | 0.6183 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.2699 | 2025-12-15 | 0.4215 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (non-reasoning) | 0.2698 | 2026-04-03 | 0.5858 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2696 | 2026-02-10 | 0.5010 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2.5 | 0.2629 | 2026-09-08 | 0.9372 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (non-reasoning) | 0.2625 | 2025-10-29 | 0.3651 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2618 | 2025-09-11 | 0.3148 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2615 | 2025-10-21 | 0.3562 | ❌ |
| 404 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2601 | 2026-04-29 | 0.6333 | ❌ |
| 405 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2598 | 2025-08-27 | 0.3005 | ❌ |
| 406 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2588 | 2025-04-14 | 0.1958 | ❌ |
| 407 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2582 | 2025-01-20 | 0.1485 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2573 | 2025-12-05 | 0.4089 | ❌ |
| 409 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2565 | 2025-10-08 | 0.3422 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2564 | 2025-03-25 | 0.1835 | ❌ |
| 411 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2562 | 2026-04-03 | 0.5858 | ❌ |
| 412 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2561 | 2025-12-11 | 0.4164 | ❌ |
| 413 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2560 | 2025-12-04 | 0.4076 | ❌ |
| 414 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2539 | 2025-12-02 | 0.4051 | ❌ |
| 415 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2531 | 2025-08-12 | 0.2868 | ❌ |
| 416 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.2529 | 2025-10-14 | 0.3486 | ❌ |
| 417 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2513 | 2025-08-05 | 0.2805 | ❌ |
| 418 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2511 | 2026-01-20 | 0.4702 | ❌ |
| 419 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2497 | 2025-04-05 | 0.1902 | ❌ |
| 420 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2490 | 2025-07-25 | 0.2710 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2487 | 2025-02-05 | 0.1567 | ❌ |
| 422 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (non-reasoning) | 0.2486 | 2026-01-19 | 0.4688 | ❌ |
| 423 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2477 | 2025-08-05 | 0.2805 | ❌ |
| 424 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2459 | 2025-06-30 | 0.2505 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2449 | 2025-06-10 | 0.2351 | ❌ |
| 426 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2433 | 2025-07-10 | 0.2585 | ❌ |
| 427 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2428 | 2025-08-06 | 0.2814 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2422 | 2024-10-22 | 0.1090 | ❌ |
| 429 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (non-reasoning) | 0.2422 | 2025-11-26 | 0.3978 | ❌ |
| 430 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2422 | 2023-03-14 | 0.0000 | ✅ |
| 431 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (non-reasoning) | 0.2417 | 2026-03-16 | 0.5550 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (non-reasoning) | 0.2406 | 2025-08-27 | 0.3005 | ❌ |
| 433 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2372 | 2025-07-30 | 0.2753 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2370 | 2026-05-28 | 0.6905 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2362 | 2025-10-03 | 0.3370 | ❌ |
| 436 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2360 | 2025-12-09 | 0.4139 | ❌ |
| 437 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (non-reasoning) | 0.2356 | 2025-12-08 | 0.4126 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.2338 | 2025-09-22 | 0.3257 | ❌ |
| 439 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2332 | 2026-08-25 | 0.8992 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2297 | 2025-04-28 | 0.2049 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2289 | 2025-08-11 | 0.2859 | ❌ |
| 442 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2282 | 2025-10-28 | 0.3640 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2272 | 2024-11-18 | 0.1198 | ❌ |
| 444 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tii.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2258 | 2026-01-04 | 0.4479 | ❌ |
| 445 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2248 | 2025-04-07 | 0.1915 | ❌ |
| 446 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2160 | 2026-04-02 | 0.5841 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2158 | 2024-12-03 | 0.1262 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2157 | 2025-12-09 | 0.4139 | ❌ |
| 449 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2152 | 2026-08-04 | 0.8450 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2150 | 2025-12-12 | 0.4177 | ❌ |
| 451 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2141 | 2026-03-06 | 0.5386 | ❌ |
| 452 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2132 | 2025-07-15 | 0.2627 | ❌ |
| 453 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.2117 | 2025-12-05 | 0.4089 | ❌ |
| 454 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2112 | 2025-08-18 | 0.2922 | ❌ |
| 455 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2087 | 2025-09-19 | 0.3227 | ❌ |
| 456 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (non-reasoning) | 0.2086 | 2025-06-17 | 0.2404 | ❌ |
| 457 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (non-reasoning) | 0.2070 | 2025-07-25 | 0.2710 | ❌ |
| 458 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2050 | 2025-08-27 | 0.3005 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2040 | 2025-05-21 | 0.2206 | ❌ |
| 460 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2033 | 2024-12-03 | 0.1262 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2005 | 2025-09-17 | 0.3207 | ❌ |
| 462 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2003 | 2025-03-18 | 0.1794 | ❌ |
| 463 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.1999 | 2025-01-20 | 0.1485 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.1997 | 2024-12-26 | 0.1365 | ❌ |
| 465 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1993 | 2024-09-19 | 0.0969 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1984 | 2025-09-17 | 0.3207 | ❌ |
| 467 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.1982 | 2026-02-11 | 0.5025 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1979 | 2025-10-14 | 0.3486 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.1969 | 2026-03-02 | 0.5321 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1964 | 2025-04-28 | 0.2049 | ❌ |
| 471 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1960 | 2025-06-10 | 0.2351 | ❌ |
| 472 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1921 | 2024-07-24 | 0.0785 | ❌ |
| 473 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1913 | 2025-07-09 | 0.2577 | ❌ |
| 474 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1912 | 2025-03-13 | 0.1765 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1906 | 2025-07-10 | 0.2585 | ❌ |
| 476 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.1905 | 2025-06-20 | 0.2427 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (non-reasoning) | 0.1903 | 2025-04-28 | 0.2049 | ❌ |
| 478 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1890 | 2024-10-15 | 0.1064 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1864 | 2025-10-14 | 0.3486 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1854 | 2024-03-04 | 0.0439 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (non-reasoning) | 0.1838 | 2025-03-18 | 0.1794 | ❌ |
| 482 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (non-reasoning) | 0.1821 | 2025-07-29 | 0.2745 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.1817 | 2025-04-05 | 0.1902 | ❌ |
| 484 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1806 | 2025-04-28 | 0.2049 | ❌ |
| 485 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1801 | 2024-07-23 | 0.0782 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (non-reasoning) | 0.1799 | 2025-08-18 | 0.2922 | ❌ |
| 487 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.1790 | 2025-04-28 | 0.2049 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (non-reasoning) | 0.1784 | 2025-04-28 | 0.2049 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1783 | 2025-03-17 | 0.1788 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (non-reasoning) | 0.1780 | 2025-08-11 | 0.2859 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (non-reasoning) | 0.1779 | 2026-04-02 | 0.5841 | ❌ |
| 492 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1744 | 2025-04-28 | 0.2049 | ❌ |
| 493 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1730 | 2025-12-02 | 0.4051 | ❌ |
| 494 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1725 | 2026-01-13 | 0.4603 | ❌ |
| 495 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1708 | 2025-09-22 | 0.3257 | ❌ |
| 496 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1702 | 2025-08-07 | 0.2823 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (non-reasoning) | 0.1691 | 2025-08-06 | 0.2814 | ❌ |
| 498 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1648 | 2025-11-20 | 0.3905 | ❌ |
| 499 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1641 | 2025-01-20 | 0.1485 | ❌ |
| 500 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1637 | 2025-01-20 | 0.1485 | ❌ |
| 501 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1634 | 2025-10-30 | 0.3662 | ❌ |
| 502 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1627 | 2026-04-29 | 0.6333 | ❌ |
| 503 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (non-reasoning) | 0.1619 | 2025-07-09 | 0.2577 | ❌ |
| 504 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (non-reasoning) | 0.1618 | 2026-03-02 | 0.5321 | ❌ |
| 505 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1595 | 2026-03-16 | 0.5550 | ❌ |
| 506 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (non-reasoning) | 0.1588 | 2025-08-27 | 0.3005 | ❌ |
| 507 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1585 | 2025-10-08 | 0.3422 | ❌ |
| 508 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (non-reasoning) | 0.1563 | 2025-07-15 | 0.2627 | ❌ |
| 509 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1546 | 2024-12-06 | 0.1275 | ❌ |
| 510 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1544 | 2025-04-14 | 0.1958 | ❌ |
| 511 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1538 | 2024-07-23 | 0.0782 | ❌ |
| 512 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1534 | 2024-12-03 | 0.1262 | ❌ |
| 513 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1530 | 2026-02-25 | 0.5242 | ❌ |
| 514 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1519 | 2025-07-07 | 0.2561 | ❌ |
| 515 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1500 | 2026-03-06 | 0.5386 | ❌ |
| 516 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1494 | 2024-07-18 | 0.0768 | ❌ |
| 517 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1486 | 2025-01-30 | 0.1536 | ❌ |
| 518 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (non-reasoning) | 0.1483 | 2025-10-28 | 0.3640 | ❌ |
| 519 | <img src="https://artificialanalysis.ai/img/logos//img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1463 | 2026-07-24 | 0.8179 | ❌ |
| 520 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1446 | 2026-04-29 | 0.6333 | ❌ |
| 521 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (non-reasoning) | 0.1438 | 2025-04-28 | 0.2049 | ❌ |
| 522 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1429 | 2025-12-02 | 0.4051 | ❌ |
| 523 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (non-reasoning) | 0.1412 | 2025-12-15 | 0.4215 | ❌ |
| 524 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1380 | 2025-09-22 | 0.3257 | ❌ |
| 525 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1376 | 2025-10-14 | 0.3486 | ❌ |
| 526 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1357 | 2026-05-11 | 0.6564 | ❌ |
| 527 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1336 | 2025-05-29 | 0.2263 | ❌ |
| 528 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (non-reasoning) | 0.1319 | 2025-04-28 | 0.2049 | ❌ |
| 529 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1309 | 2025-04-28 | 0.2049 | ❌ |
| 530 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1273 | 2024-12-12 | 0.1301 | ❌ |
| 531 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1264 | 2025-05-20 | 0.2199 | ❌ |
| 532 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1243 | 2025-08-14 | 0.2885 | ❌ |
| 533 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1199 | 2025-03-12 | 0.1759 | ❌ |
| 534 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1192 | 2024-04-18 | 0.0534 | ❌ |
| 535 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1187 | 2024-09-25 | 0.0990 | ❌ |
| 536 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1168 | 2024-09-25 | 0.0990 | ❌ |
| 537 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1153 | 2025-11-20 | 0.3905 | ❌ |
| 538 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1137 | 2025-12-02 | 0.4051 | ❌ |
| 539 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1087 | 2026-01-05 | 0.4493 | ❌ |
| 540 | <img src="https://artificialanalysis.ai/img/logos//img/logos/reka.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1082 | 2025-03-10 | 0.1747 | ❌ |
| 541 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1078 | 2025-09-09 | 0.3129 | ❌ |
| 542 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1077 | 2025-09-23 | 0.3267 | ❌ |
| 543 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (non-reasoning) | 0.1068 | 2025-04-28 | 0.2049 | ❌ |
| 544 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1058 | 2026-03-02 | 0.5321 | ❌ |
| 545 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1035 | 2025-12-11 | 0.4164 | ❌ |
| 546 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1033 | 2025-05-23 | 0.2220 | ❌ |
| 547 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1020 | 2025-07-07 | 0.2561 | ❌ |
| 548 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1006 | 2026-01-20 | 0.4702 | ❌ |
| 549 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0938 | 2025-09-02 | 0.3061 | ❌ |
| 550 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0924 | 2025-11-20 | 0.3905 | ❌ |
| 551 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0914 | 2025-07-15 | 0.2627 | ❌ |
| 552 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0913 | 2025-03-13 | 0.1765 | ❌ |
| 553 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0908 | 2025-10-28 | 0.3640 | ❌ |
| 554 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0897 | 2024-09-25 | 0.0990 | ❌ |
| 555 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0891 | 2024-02-26 | 0.0426 | ❌ |
| 556 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0886 | 2025-04-28 | 0.2049 | ❌ |
| 557 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (non-reasoning) | 0.0853 | 2026-03-02 | 0.5321 | ❌ |
| 558 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (non-reasoning) | 0.0844 | 2025-07-15 | 0.2627 | ❌ |
| 559 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0836 | 2025-03-12 | 0.1759 | ❌ |
| 560 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0826 | 2025-10-07 | 0.3412 | ❌ |
| 561 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0800 | 2025-09-22 | 0.3257 | ❌ |
| 562 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0793 | 2026-04-29 | 0.6333 | ❌ |
| 563 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0751 | 2024-04-23 | 0.0545 | ❌ |
| 564 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B (non-reasoning) | 0.0717 | 2025-04-16 | 0.1971 | ❌ |
| 565 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0691 | 2026-01-05 | 0.4493 | ❌ |
| 566 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0684 | 2025-10-28 | 0.3640 | ❌ |
| 567 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0674 | 2025-10-28 | 0.3640 | ❌ |
| 568 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0655 | 2025-07-10 | 0.2585 | ❌ |
| 569 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0649 | 2025-04-28 | 0.2049 | ❌ |
| 570 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0646 | 2024-04-18 | 0.0534 | ❌ |
| 571 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0622 | 2023-09-27 | 0.0188 | ❌ |
| 572 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0603 | 2025-03-12 | 0.1759 | ❌ |
| 573 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (non-reasoning) | 0.0567 | 2025-04-28 | 0.2049 | ❌ |
| 574 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0565 | 2024-11-26 | 0.1232 | ❌ |
| 575 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0561 | 2025-03-13 | 0.1765 | ❌ |
| 576 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0552 | 2025-09-02 | 0.3061 | ❌ |
| 577 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0532 | 2025-06-26 | 0.2474 | ❌ |
| 578 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0510 | 2025-10-28 | 0.3640 | ❌ |
| 579 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0478 | 2024-09-25 | 0.0990 | ❌ |
| 580 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.0458 | 2026-09-03 | 0.9234 | ❌ |
| 581 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (non-reasoning) | 0.0438 | 2025-04-28 | 0.2049 | ❌ |
| 582 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0361 | 2025-06-26 | 0.2474 | ❌ |
| 583 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0357 | 2026-02-17 | 0.5117 | ❌ |
| 584 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | 2025-01-20 | 0.1485 | ❌ |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 12 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 4 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 10 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 12 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 9 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 5 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 3 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且发布时间 ≤（更早），且至少一项严格更优）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.2422，即前沿左端点 GPT-4）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（指数）

横轴为发布时间指数映射：x = (a^(b*t)-1)/(a^b-1)；t 为发布时间按最早和最大映射到 [0,1]；a = 1.901，b = 5.804，用 11 品牌前沿定出；mse = 0.002013。

- **函数端点**：最早发布 → x = 0；前沿最大发布 → x = 1；
- 横轴时间标签：2024-01, 2025-01, 2026-01, 2026-09
- 中位数位置 0.584；左 168 个，右 262 个
- 前沿最大发布时间 2026-09-30 → x = 1；大于该值的模型不入图，表格中有。

## 图中标注规则

品牌帕累托前沿模型全部标注。V13/V15/V16 规则：

1. **品牌公共前缀剔除（最长有效切点）**：品牌全部前沿模型共享的前导块被剔除 —— 切点须止于分界符（空格/连字符/下划线，如 'Claude '、'GPT-'、'GLM-'、'Grok '、'DeepSeek V4 '），或止于字母且每个名称在切点后紧跟数字（品牌/系列字母 + 版本号，如 'Kimi K|2.6'、'Qwen|3.8'、'MiMo-V|2.5'、'MiniMax-M|2.1'）—— 实例：Claude Opus 5 (high) → Opus 5 (high)、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5-Pro → 2.5-Pro；剔除后任一名称为空或产生重复标签则该切点作废，顺次尝试更短切点；
2. **(non-reasoning) → (non)**：思考程度中的 Non-reasoning 简写为 non（含组合式：Non-reasoning, high → non, high）；
3. **相邻同名 run 短标签（每次重新计算）**：品牌连线上连续 2 个以上顶点属于同一模型时，仅性能最低者（run 首位）保留全名，其后相邻的较高者只标思考程度（如 Opus 5 的 (low) (medium) (high) (xhigh) 序列仅首项带族名）；同名模型不相邻的重复出现不合并、保留全名 —— A-B(high)-B(xhigh)-C-B(max) 标注为 A-B(high)-(xhigh)-C-B(max)，因此交错家族（Gemini 3.7 / 3.8 Flash、Claude Fable 5.1 / Opus 5）始终可分辨。

4. **标签位置与序列同向（V15）**：品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上 —— 对前沿相邻对 A→B（B 更靠右上），标签位移的两个分量须同时 >= 0（至少是 (0,0)），既不得更左、也不得更低（只要有一个分量非负不算合格；V14 的投影规则会放过「更右但更低」，V15 起视为违反；同时点堆叠即：上方模型的标签既在上方、也不更左）；初始放置违反时就近重摆（不产生新的重叠、不破坏与前后邻居的同向关系，最多 6 轮；单标签重摆无解——标签被前后邻居夹死、局部约束盒为空——时，自动升级为以违规对为中心逐级扩大的窗口级联重排，整段相邻标签作为一个阶梯整体重排，修不好的配对在日志中报告）。

5. **标签摆放四级优先（V16）**：① 尽量多的标签骑在连线段上——点的右侧（去路段）或左侧（来路段）皆可，同一条线段允许容纳两个标签（各贴各的点）；目标骑线位仅被其他标签占据时触发「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线。② 骑不上线的标签在「假设线能放下该标签」的离点最近位置的上方或下方、与线平行摆放（右/左侧 × 上/下方四组合；互相掣肘的标签自然错开成对角组合）。③ 仍放不下时放在点的两条连线延长线上的最近点。④ 最后在两条连线夹角形成的扇区（连线前上方空白区）内就近放置，文字保持与邻近连线平行。

标注文字与连线平行且中轴线重合；文字下方不绘制连线，仅在文字两侧绘制（若两侧仍有区域）；文字使用品牌颜色，无边框、无背景。

## X：发布时间

**X = 发布时间（线性）**

发布时间为 releaseDate；左端为最早发布时间。

### 数据来源

**主数据源**: [Artificial Analysis Leaderboard](https://artificialanalysis.ai/leaderboards/models)（Status: All）  
**性能方法论**: [AA Performance Benchmarking](https://artificialanalysis.ai/methodology/performance-benchmarking)  
**模型数**: 584（总体帕累托前沿 19 个；图表入图 430 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，同时点按能力从低到高连接）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.2422，前沿左端点 GPT-4 即 (0,0)），能力低于该级的 154 个模型和发布时间大于品牌前沿最大值的模型不出现在图中；横轴为发布时间（线性）。
