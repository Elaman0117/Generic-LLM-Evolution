# LLM Leaderboard — 综合能力 vs 发布时间

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.2433，即前沿左端点 GPT-4）为 0：综合能力 ≥ 该级的 418 个模型入图，152 个能力低于第一级的不出现在图中；发布时间大于品牌前沿最大值的模型同样不入图（表列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 发布时间 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max with fallback) | 1.0000 | 2026-09-22 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh with fallback) | 0.9956 | 2026-09-22 | 1.0000 | ❌ |
| 3 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 0.9796 | 2026-09-01 | 0.9399 | ✅ |
| 4 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9667 | 2026-09-01 | 0.9399 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9576 | 2026-09-03 | 0.9455 | ❌ |
| 6 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9560 | 2026-09-03 | 0.9455 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high with fallback) | 0.9556 | 2026-09-22 | 1.0000 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9408 | 2026-07-24 | 0.8374 | ✅ |
| 9 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9384 | 2026-09-03 | 0.9455 | ❌ |
| 10 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9344 | 2026-09-01 | 0.9399 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9340 | 2026-06-09 | 0.7327 | ✅ |
| 12 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9284 | 2026-07-24 | 0.8374 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium with fallback) | 0.9272 | 2026-09-22 | 1.0000 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.9188 | 2026-07-09 | 0.8010 | ❌ |
| 15 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.9182 | 2026-09-03 | 0.9455 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.9136 | 2026-07-24 | 0.8374 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.9089 | 2026-09-02 | 0.9427 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.9019 | 2026-09-01 | 0.9399 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.8915 | 2026-09-22 | 1.0000 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.8912 | 2026-09-02 | 0.9427 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8800 | 2026-09-03 | 0.9455 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8737 | 2026-07-16 | 0.8178 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8727 | 2026-07-24 | 0.8374 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8727 | 2026-09-02 | 0.9427 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8725 | 2026-07-09 | 0.8010 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8683 | 2026-09-01 | 0.9399 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8648 | 2026-08-12 | 0.8859 | ❌ |
| 28 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8641 | 2026-04-23 | 0.6368 | ✅ |
| 29 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8617 | 2026-08-12 | 0.8859 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8552 | 2026-08-18 | 0.9018 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8549 | 2026-08-12 | 0.8859 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8527 | 2026-07-09 | 0.8010 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.8508 | 2026-09-22 | 1.0000 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.8500 | 2026-09-21 | 0.9971 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8483 | 2026-07-09 | 0.8010 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.8483 | 2026-09-02 | 0.9427 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8473 | 2026-05-28 | 0.7069 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.8413 | 2026-09-21 | 0.9971 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8403 | 2026-04-23 | 0.6368 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.8400 | 2026-09-21 | 0.9971 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8325 | 2026-08-13 | 0.8885 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.8321 | 2026-09-18 | 0.9883 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.8315 | 2026-09-22 | 1.0000 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8298 | 2026-09-02 | 0.9427 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8289 | 2026-07-09 | 0.8010 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8281 | 2026-08-03 | 0.8626 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low with fallback) | 0.8227 | 2026-09-22 | 1.0000 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.8175 | 2026-08-05 | 0.8677 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.8146 | 2026-08-26 | 0.9234 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.8119 | 2026-08-12 | 0.8859 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.8084 | 2026-09-22 | 1.0000 | ❌ |
| 52 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.8053 | 2026-04-16 | 0.6236 | ✅ |
| 53 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.8014 | 2026-03-05 | 0.5497 | ✅ |
| 54 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.8001 | 2026-06-30 | 0.7799 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.8001 | 2026-05-19 | 0.6882 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.7977 | 2026-07-24 | 0.8374 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.7972 | 2026-07-08 | 0.7986 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.7927 | 2026-04-23 | 0.6368 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.7927 | 2026-06-16 | 0.7481 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7906 | 2026-05-19 | 0.6882 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7905 | 2026-02-05 | 0.5052 | ✅ |
| 62 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.7883 | 2026-07-09 | 0.8010 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.7826 | 2026-08-13 | 0.8885 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7819 | 2026-02-19 | 0.5270 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7660 | 2026-07-09 | 0.8010 | ❌ |
| 66 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7659 | 2026-07-09 | 0.8010 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7548 | 2026-08-26 | 0.9234 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7523 | 2026-07-21 | 0.8300 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7509 | 2026-07-09 | 0.8010 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7483 | 2026-02-05 | 0.5052 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7448 | 2026-04-07 | 0.6070 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7389 | 2026-07-09 | 0.8010 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.7335 | 2026-09-22 | 1.0000 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7328 | 2025-11-18 | 0.3974 | ✅ |
| 75 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7326 | 2026-09-02 | 0.9427 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7312 | 2026-08-13 | 0.8885 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7308 | 2026-04-30 | 0.6503 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7271 | 2026-04-08 | 0.6088 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7252 | 2026-08-12 | 0.8859 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7251 | 2026-08-13 | 0.8885 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7199 | 2025-12-11 | 0.4263 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.7196 | 2026-09-10 | 0.9652 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7194 | 2025-12-11 | 0.4263 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.7183 | 2026-04-20 | 0.6311 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.7182 | 2026-09-22 | 1.0000 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.7139 | 2026-05-19 | 0.6882 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.7085 | 2026-04-20 | 0.6311 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.7052 | 2026-03-10 | 0.5581 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.7044 | 2025-11-24 | 0.4047 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.7036 | 2026-08-14 | 0.8912 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.7012 | 2026-07-09 | 0.8010 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.6993 | 2026-04-16 | 0.6236 | ❌ |
| 93 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.6956 | 2026-04-23 | 0.6368 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6890 | 2026-08-21 | 0.9098 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.6887 | 2025-12-17 | 0.4341 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6859 | 2026-07-31 | 0.8550 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6842 | 2026-02-17 | 0.5239 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6816 | 2026-03-05 | 0.5497 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6792 | 2026-06-30 | 0.7799 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6782 | 2026-07-09 | 0.8010 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6776 | 2026-08-12 | 0.8859 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6772 | 2026-07-16 | 0.8178 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.6733 | 2026-06-01 | 0.7154 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6733 | 2026-04-30 | 0.6503 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.6725 | 2026-09-22 | 1.0000 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6705 | 2026-03-18 | 0.5716 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6695 | 2026-04-02 | 0.5980 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6694 | 2026-06-01 | 0.7154 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6659 | 2026-07-09 | 0.8010 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6652 | 2025-12-11 | 0.4263 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6625 | 2026-04-24 | 0.6387 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6567 | 2026-04-07 | 0.6070 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6519 | 2025-09-23 | 0.3345 | ✅ |
| 114 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6499 | 2026-04-24 | 0.6387 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6477 | 2026-04-30 | 0.6503 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6469 | 2026-02-11 | 0.5145 | ❌ |
| 117 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.6463 | 2026-09-22 | 1.0000 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6409 | 2025-11-13 | 0.3913 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.6406 | 2026-09-03 | 0.9455 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6380 | 2026-06-30 | 0.7799 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6353 | 2026-06-12 | 0.7392 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6337 | 2025-11-13 | 0.3913 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6279 | 2026-03-17 | 0.5699 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6239 | 2026-03-27 | 0.5873 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6217 | 2025-08-07 | 0.2890 | ✅ |
| 126 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.6173 | 2026-09-10 | 0.9652 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.6152 | 2026-07-09 | 0.8010 | ❌ |
| 128 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.6144 | 2026-02-05 | 0.5052 | ❌ |
| 129 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.6140 | 2026-03-15 | 0.5665 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.6135 | 2026-07-30 | 0.8525 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.6131 | 2026-04-22 | 0.6349 | ❌ |
| 132 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.6122 | 2025-07-10 | 0.2647 | ✅ |
| 133 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.6098 | 2026-04-22 | 0.6349 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.6091 | 2026-04-24 | 0.6387 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (low) | 0.6090 | 2026-08-18 | 0.9018 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.6076 | 2026-08-06 | 0.8703 | ❌ |
| 137 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.6075 | 2025-08-07 | 0.2890 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.6073 | 2026-09-22 | 1.0000 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.6069 | 2026-07-15 | 0.8154 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.6064 | 2026-04-24 | 0.6387 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.6043 | 2026-06-16 | 0.7481 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.6033 | 2026-05-05 | 0.6600 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos//img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.6032 | 2026-08-30 | 0.9343 | ❌ |
| 144 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.6017 | 2025-05-22 | 0.2265 | ✅ |
| 145 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5936 | 2026-08-12 | 0.8859 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5923 | 2026-05-19 | 0.6882 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5920 | 2026-02-24 | 0.5350 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5917 | 2025-12-16 | 0.4328 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.5916 | 2026-03-17 | 0.5699 | ❌ |
| 150 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5898 | 2026-08-10 | 0.8807 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5895 | 2026-03-19 | 0.5734 | ❌ |
| 152 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5889 | 2025-04-16 | 0.2018 | ✅ |
| 153 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nex.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.5887 | 2026-06-02 | 0.7175 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.5864 | 2026-07-14 | 0.8130 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5851 | 2026-04-01 | 0.5962 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5851 | 2026-04-22 | 0.6349 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.5831 | 2026-01-27 | 0.4917 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5810 | 2025-09-29 | 0.3407 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5795 | 2025-08-07 | 0.2890 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5790 | 2026-06-04 | 0.7218 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5770 | 2025-08-05 | 0.2872 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5753 | 2026-02-17 | 0.5239 | ❌ |
| 163 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5749 | 2025-11-06 | 0.3830 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5728 | 2025-11-24 | 0.4047 | ❌ |
| 165 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5699 | 2026-02-17 | 0.5239 | ❌ |
| 166 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5693 | 2026-08-14 | 0.8912 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5690 | 2026-02-16 | 0.5223 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5677 | 2026-04-20 | 0.6311 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5666 | 2025-11-18 | 0.3974 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5654 | 2026-07-21 | 0.8300 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5642 | 2026-06-30 | 0.7799 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sktelecom.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5600 | 2026-08-12 | 0.8859 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5597 | 2026-07-09 | 0.8010 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5589 | 2026-03-18 | 0.5716 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5584 | 2026-07-06 | 0.7939 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5582 | 2026-07-09 | 0.8010 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5581 | 2025-11-13 | 0.3913 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5554 | 2026-09-03 | 0.9455 | ❌ |
| 179 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5542 | 2025-08-07 | 0.2890 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5542 | 2026-04-23 | 0.6368 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5539 | 2026-08-14 | 0.8912 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5488 | 2026-02-12 | 0.5160 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5477 | 2026-04-07 | 0.6070 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5474 | 2026-03-30 | 0.5926 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5436 | 2026-04-16 | 0.6236 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5424 | 2026-07-09 | 0.8010 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5423 | 2026-06-30 | 0.7799 | ❌ |
| 188 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5405 | 2025-11-19 | 0.3986 | ❌ |
| 189 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (Non-reasoning) | 0.5390 | 2026-09-22 | 1.0000 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5372 | 2026-08-04 | 0.8652 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5346 | 2026-03-17 | 0.5699 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5341 | 2025-08-07 | 0.2890 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5336 | 2025-12-23 | 0.4421 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5336 | 2026-01-26 | 0.4902 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5316 | 2026-02-24 | 0.5350 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5283 | 2026-02-24 | 0.5350 | ❌ |
| 197 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5278 | 2026-05-29 | 0.7090 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5252 | 2026-08-20 | 0.9071 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5229 | 2026-01-27 | 0.4917 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5216 | 2025-12-16 | 0.4328 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5205 | 2026-03-17 | 0.5699 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5159 | 2025-12-17 | 0.4341 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5154 | 2025-12-22 | 0.4408 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5131 | 2025-12-01 | 0.4135 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.5121 | 2026-04-02 | 0.5980 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.5119 | 2026-03-27 | 0.5873 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.5117 | 2026-02-11 | 0.5145 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.5111 | 2026-08-14 | 0.8912 | ❌ |
| 209 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.5059 | 2026-09-11 | 0.9681 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.5058 | 2026-07-09 | 0.8010 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.5049 | 2026-02-16 | 0.5223 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.5048 | 2026-04-02 | 0.5980 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.5037 | 2026-09-22 | 1.0000 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.5032 | 2025-05-22 | 0.2265 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4986 | 2026-06-30 | 0.7799 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4984 | 2025-09-19 | 0.3304 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4983 | 2026-08-10 | 0.8807 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.4939 | 2026-04-23 | 0.6368 | ❌ |
| 219 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4914 | 2025-02-19 | 0.1680 | ✅ |
| 220 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4901 | 2026-02-24 | 0.5350 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4897 | 2025-09-29 | 0.3407 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4888 | 2025-12-01 | 0.4135 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4879 | 2026-05-14 | 0.6780 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4870 | 2026-02-02 | 0.5007 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4851 | 2026-08-12 | 0.8859 | ❌ |
| 226 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4819 | 2026-06-25 | 0.7684 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4798 | 2026-05-20 | 0.6903 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4773 | 2026-05-08 | 0.6660 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (Non-reasoning) | 0.4750 | 2026-09-10 | 0.9652 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4747 | 2026-03-05 | 0.5497 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4744 | 2025-10-26 | 0.3703 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4734 | 2025-06-05 | 0.2369 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4710 | 2025-11-11 | 0.3889 | ❌ |
| 234 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4707 | 2025-04-16 | 0.2018 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4707 | 2024-12-05 | 0.1300 | ✅ |
| 236 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4698 | 2026-04-29 | 0.6483 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4668 | 2026-09-03 | 0.9455 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4608 | 2025-10-15 | 0.3580 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4595 | 2026-04-24 | 0.6387 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4558 | 2026-07-09 | 0.8010 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4553 | 2025-02-24 | 0.1708 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4524 | 2025-05-22 | 0.2265 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4497 | 2025-11-27 | 0.4084 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4473 | 2026-06-16 | 0.7481 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4469 | 2025-09-25 | 0.3365 | ❌ |
| 246 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4464 | 2026-06-29 | 0.7775 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4459 | 2026-04-22 | 0.6349 | ❌ |
| 248 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4425 | 2025-09-29 | 0.3407 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4417 | 2025-11-11 | 0.3889 | ❌ |
| 250 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4416 | 2026-03-03 | 0.5464 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4402 | 2025-12-11 | 0.4263 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4381 | 2025-09-22 | 0.3334 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4320 | 2025-02-24 | 0.1708 | ❌ |
| 254 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4311 | 2025-11-03 | 0.3795 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4308 | 2025-11-27 | 0.4084 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4278 | 2026-02-24 | 0.5350 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4260 | 2025-05-20 | 0.2251 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4258 | 2025-10-29 | 0.3737 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4228 | 2026-03-02 | 0.5448 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4209 | 2026-04-22 | 0.6349 | ❌ |
| 261 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4207 | 2025-10-15 | 0.3580 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4180 | 2025-09-05 | 0.3163 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4174 | 2025-11-13 | 0.3913 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4167 | 2026-04-24 | 0.6387 | ❌ |
| 265 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4166 | 2025-09-23 | 0.3345 | ❌ |
| 266 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4155 | 2026-04-02 | 0.5980 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4142 | 2026-03-10 | 0.5581 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4138 | 2026-04-23 | 0.6368 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.4103 | 2025-11-26 | 0.4072 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.4081 | 2025-12-01 | 0.4135 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.4070 | 2026-04-09 | 0.6106 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.4063 | 2026-03-02 | 0.5448 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.4062 | 2026-04-23 | 0.6368 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.4062 | 2025-08-07 | 0.2890 | ❌ |
| 275 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.4051 | 2025-10-29 | 0.3737 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.4041 | 2025-08-07 | 0.2890 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.4033 | 2026-08-06 | 0.8703 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.4032 | 2025-12-22 | 0.4408 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.4020 | 2025-11-26 | 0.4072 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.3981 | 2026-04-07 | 0.6070 | ❌ |
| 281 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.3956 | 2026-04-16 | 0.6236 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3955 | 2026-06-03 | 0.7197 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3946 | 2025-08-21 | 0.3019 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3940 | 2025-07-28 | 0.2801 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3882 | 2025-09-23 | 0.3345 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3874 | 2026-09-07 | 0.9567 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3854 | 2025-08-28 | 0.3085 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.3853 | 2026-04-30 | 0.6503 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3844 | 2025-07-11 | 0.2655 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3830 | 2025-05-28 | 0.2309 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3822 | 2025-12-31 | 0.4530 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3820 | 2025-09-30 | 0.3418 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3811 | 2026-02-20 | 0.5286 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.3789 | 2026-04-02 | 0.5980 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (Non-reasoning) | 0.3783 | 2026-09-22 | 1.0000 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3773 | 2025-09-25 | 0.3365 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3749 | 2026-07-09 | 0.8010 | ❌ |
| 298 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3746 | 2025-08-07 | 0.2890 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3736 | 2025-10-21 | 0.3646 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.3735 | 2026-09-03 | 0.9455 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3732 | 2026-03-11 | 0.5597 | ❌ |
| 302 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3726 | 2025-04-14 | 0.2005 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos//img/logos/arcee.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3719 | 2026-04-01 | 0.5962 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3716 | 2026-08-25 | 0.9206 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3709 | 2025-11-13 | 0.3913 | ❌ |
| 306 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3706 | 2025-10-29 | 0.3737 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3696 | 2026-03-02 | 0.5448 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3695 | 2026-01-19 | 0.4799 | ❌ |
| 309 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3660 | 2025-09-30 | 0.3418 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.3658 | 2026-02-24 | 0.5350 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3647 | 2026-08-11 | 0.8833 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3622 | 2025-09-30 | 0.3418 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3603 | 2025-07-25 | 0.2774 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3582 | 2026-03-30 | 0.5926 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3572 | 2025-07-22 | 0.2748 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3562 | 2025-09-25 | 0.3365 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3561 | 2026-03-19 | 0.5734 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepcogito.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3559 | 2025-11-18 | 0.3974 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3529 | 2025-09-18 | 0.3293 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3519 | 2025-11-25 | 0.4060 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3508 | 2026-04-02 | 0.5980 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3506 | 2026-07-23 | 0.8349 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3503 | 2025-02-19 | 0.1680 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3495 | 2025-12-08 | 0.4224 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3488 | 2025-09-22 | 0.3334 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3479 | 2025-08-05 | 0.2872 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3447 | 2025-08-07 | 0.2890 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3400 | 2025-12-16 | 0.4328 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3376 | 2025-09-05 | 0.3163 | ❌ |
| 330 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3346 | 2026-03-16 | 0.5682 | ❌ |
| 331 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3312 | 2025-09-29 | 0.3407 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3294 | 2026-05-26 | 0.7027 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3288 | 2025-09-25 | 0.3365 | ❌ |
| 334 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3280 | 2025-08-21 | 0.3019 | ❌ |
| 335 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3252 | 2026-06-09 | 0.7327 | ❌ |
| 336 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3242 | 2025-08-20 | 0.3009 | ❌ |
| 337 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3217 | 2025-01-31 | 0.1577 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3207 | 2024-11-20 | 0.1235 | ✅ |
| 339 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3185 | 2025-05-20 | 0.2251 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3183 | 2026-08-25 | 0.9206 | ❌ |
| 341 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.3174 | 2026-04-06 | 0.6052 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3172 | 2024-08-06 | 0.0844 | ✅ |
| 343 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.3167 | 2025-07-21 | 0.2740 | ❌ |
| 344 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.3160 | 2025-12-15 | 0.4315 | ❌ |
| 345 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3142 | 2025-06-17 | 0.2461 | ❌ |
| 346 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3105 | 2025-11-19 | 0.3986 | ❌ |
| 347 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3096 | 2025-09-11 | 0.3223 | ❌ |
| 348 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3096 | 2025-08-07 | 0.2890 | ❌ |
| 349 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3083 | 2026-06-03 | 0.7197 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.3077 | 2025-09-23 | 0.3345 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.3076 | 2025-12-15 | 0.4315 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.3059 | 2025-03-05 | 0.1759 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.3048 | 2025-10-13 | 0.3558 | ❌ |
| 354 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.3048 | 2026-05-25 | 0.7006 | ❌ |
| 355 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.3046 | 2026-05-25 | 0.7006 | ❌ |
| 356 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.3034 | 2024-11-18 | 0.1226 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.3001 | 2025-12-17 | 0.4341 | ❌ |
| 358 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.2979 | 2026-03-02 | 0.5448 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.2973 | 2026-02-03 | 0.5022 | ❌ |
| 360 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2972 | 2025-01-31 | 0.1577 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2966 | 2025-07-28 | 0.2801 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2964 | 2025-06-17 | 0.2461 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs.svg" width="18" alt="Inception" /> Inception | Mercury 2.5 | 0.2963 | 2026-09-08 | 0.9595 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2956 | 2026-04-03 | 0.5998 | ❌ |
| 365 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2941 | 2025-11-27 | 0.4084 | ❌ |
| 366 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2938 | 2026-03-17 | 0.5699 | ❌ |
| 367 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2918 | 2026-04-15 | 0.6217 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2910 | 2026-06-10 | 0.7348 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2900 | 2025-05-07 | 0.2159 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2895 | 2025-06-17 | 0.2461 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos//img/logos/naver.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2894 | 2025-12-26 | 0.4462 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2877 | 2025-09-19 | 0.3304 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.2872 | 2025-12-05 | 0.4185 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2869 | 2025-12-31 | 0.4530 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2857 | 2025-03-25 | 0.1878 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2854 | 2026-03-17 | 0.5699 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2842 | 2025-12-11 | 0.4263 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2832 | 2025-01-20 | 0.1520 | ❌ |
| 379 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2826 | 2025-12-02 | 0.4147 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2812 | 2025-04-05 | 0.1947 | ❌ |
| 381 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2802 | 2025-08-12 | 0.2935 | ❌ |
| 382 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2781 | 2025-08-05 | 0.2872 | ❌ |
| 383 | <img src="https://artificialanalysis.ai/img/logos//img/logos/prime-intellect.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2774 | 2025-11-27 | 0.4084 | ❌ |
| 384 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2769 | 2026-04-29 | 0.6483 | ❌ |
| 385 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2766 | 2026-02-10 | 0.5129 | ❌ |
| 386 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2749 | 2026-01-28 | 0.4931 | ❌ |
| 387 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2746 | 2025-10-03 | 0.3450 | ❌ |
| 388 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2746 | 2025-07-30 | 0.2818 | ❌ |
| 389 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2742 | 2025-08-05 | 0.2872 | ❌ |
| 390 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2731 | 2024-07-23 | 0.0801 | ✅ |
| 391 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2722 | 2025-04-30 | 0.2111 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2716 | 2026-04-21 | 0.6330 | ❌ |
| 393 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2715 | 2025-04-14 | 0.2005 | ❌ |
| 394 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2711 | 2026-04-03 | 0.5998 | ❌ |
| 395 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2709 | 2026-02-10 | 0.5129 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2659 | 2026-08-25 | 0.9206 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2637 | 2025-10-29 | 0.3737 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2630 | 2025-09-11 | 0.3223 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2627 | 2025-10-21 | 0.3646 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2610 | 2025-08-27 | 0.3076 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2585 | 2025-12-05 | 0.4185 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2577 | 2025-10-08 | 0.3503 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2573 | 2025-12-11 | 0.4263 | ❌ |
| 404 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2571 | 2025-12-04 | 0.4173 | ❌ |
| 405 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2568 | 2025-08-05 | 0.2872 | ❌ |
| 406 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2544 | 2024-10-22 | 0.1116 | ❌ |
| 407 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2540 | 2025-10-14 | 0.3569 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2523 | 2026-01-20 | 0.4813 | ❌ |
| 409 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2501 | 2025-07-25 | 0.2774 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2499 | 2025-02-05 | 0.1604 | ❌ |
| 411 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2497 | 2026-01-19 | 0.4799 | ❌ |
| 412 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2479 | 2025-12-09 | 0.4237 | ❌ |
| 413 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2470 | 2025-06-30 | 0.2564 | ❌ |
| 414 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2460 | 2025-06-10 | 0.2407 | ❌ |
| 415 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2444 | 2025-07-10 | 0.2647 | ❌ |
| 416 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2439 | 2025-08-06 | 0.2881 | ❌ |
| 417 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2433 | 2025-11-26 | 0.4072 | ❌ |
| 418 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2433 | 2023-03-14 | 0.0000 | ✅ |
| 419 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2428 | 2026-03-16 | 0.5682 | ❌ |
| 420 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2417 | 2025-08-27 | 0.3076 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2404 | 2025-07-31 | 0.2827 | ❌ |
| 422 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2381 | 2026-05-28 | 0.7069 | ❌ |
| 423 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2372 | 2025-10-03 | 0.3450 | ❌ |
| 424 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2367 | 2025-12-08 | 0.4224 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2353 | 2026-04-02 | 0.5980 | ❌ |
| 426 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2348 | 2025-09-22 | 0.3334 | ❌ |
| 427 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2331 | 2026-08-04 | 0.8652 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2307 | 2025-04-28 | 0.2097 | ❌ |
| 429 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2300 | 2025-08-11 | 0.2926 | ❌ |
| 430 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2293 | 2025-10-28 | 0.3726 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2283 | 2024-11-18 | 0.1226 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tii.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2268 | 2026-01-04 | 0.4586 | ❌ |
| 433 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2258 | 2025-04-07 | 0.1960 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2246 | 2025-12-09 | 0.4237 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2181 | 2024-12-26 | 0.1397 | ❌ |
| 436 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2168 | 2024-12-03 | 0.1291 | ❌ |
| 437 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nanbeige.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2166 | 2026-02-11 | 0.5145 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2160 | 2025-12-12 | 0.4276 | ❌ |
| 439 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.2157 | 2025-06-20 | 0.2484 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2151 | 2026-03-06 | 0.5514 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2142 | 2025-07-15 | 0.2689 | ❌ |
| 442 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2137 | 2025-09-17 | 0.3283 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.2127 | 2025-12-05 | 0.4185 | ❌ |
| 444 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2122 | 2025-08-18 | 0.2991 | ❌ |
| 445 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2122 | 2026-03-02 | 0.5448 | ❌ |
| 446 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2096 | 2025-09-19 | 0.3304 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2096 | 2025-06-17 | 0.2461 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2080 | 2025-07-25 | 0.2774 | ❌ |
| 449 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.2071 | 2025-04-05 | 0.1947 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2059 | 2025-08-27 | 0.3076 | ❌ |
| 451 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.2049 | 2025-05-21 | 0.2258 | ❌ |
| 452 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.2045 | 2025-04-28 | 0.2097 | ❌ |
| 453 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.2043 | 2024-12-03 | 0.1291 | ❌ |
| 454 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.2012 | 2025-03-18 | 0.1836 | ❌ |
| 455 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.2009 | 2025-01-20 | 0.1520 | ❌ |
| 456 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.2002 | 2024-09-19 | 0.0992 | ❌ |
| 457 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1995 | 2025-04-28 | 0.2097 | ❌ |
| 458 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1994 | 2025-09-17 | 0.3283 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1988 | 2025-10-14 | 0.3569 | ❌ |
| 460 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1973 | 2025-04-28 | 0.2097 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1969 | 2025-06-10 | 0.2407 | ❌ |
| 462 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1929 | 2024-07-24 | 0.0804 | ❌ |
| 463 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1924 | 2025-12-02 | 0.4147 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1921 | 2025-07-09 | 0.2638 | ❌ |
| 465 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1921 | 2025-03-13 | 0.1806 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1914 | 2025-07-10 | 0.2647 | ❌ |
| 467 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1912 | 2025-04-28 | 0.2097 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1899 | 2024-10-15 | 0.1089 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1885 | 2026-03-16 | 0.5682 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1873 | 2025-10-14 | 0.3569 | ❌ |
| 471 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1862 | 2024-03-04 | 0.0450 | ❌ |
| 472 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1853 | 2025-03-17 | 0.1830 | ❌ |
| 473 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1847 | 2025-03-18 | 0.1836 | ❌ |
| 474 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1829 | 2025-07-29 | 0.2809 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1815 | 2025-04-28 | 0.2097 | ❌ |
| 476 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1809 | 2024-07-23 | 0.0801 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1807 | 2025-08-18 | 0.2991 | ❌ |
| 478 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1792 | 2025-04-28 | 0.2097 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1788 | 2025-08-11 | 0.2926 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1787 | 2026-04-02 | 0.5980 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1770 | 2026-03-02 | 0.5448 | ❌ |
| 482 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1765 | 2026-04-29 | 0.6483 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1733 | 2026-01-13 | 0.4712 | ❌ |
| 484 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1716 | 2025-09-22 | 0.3334 | ❌ |
| 485 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1709 | 2025-08-07 | 0.2890 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1698 | 2025-08-06 | 0.2881 | ❌ |
| 487 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1680 | 2024-07-23 | 0.0801 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos//img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1658 | 2026-07-24 | 0.8374 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1656 | 2025-11-20 | 0.3998 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1652 | 2024-07-18 | 0.0786 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1648 | 2025-01-20 | 0.1520 | ❌ |
| 492 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1647 | 2025-04-14 | 0.2005 | ❌ |
| 493 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1646 | 2024-12-06 | 0.1305 | ❌ |
| 494 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1644 | 2025-01-20 | 0.1520 | ❌ |
| 495 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1641 | 2025-10-30 | 0.3749 | ❌ |
| 496 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1627 | 2025-12-02 | 0.4147 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1627 | 2025-07-09 | 0.2638 | ❌ |
| 498 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1595 | 2025-08-27 | 0.3076 | ❌ |
| 499 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1592 | 2025-10-08 | 0.3503 | ❌ |
| 500 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1570 | 2025-07-15 | 0.2689 | ❌ |
| 501 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1570 | 2026-04-29 | 0.6483 | ❌ |
| 502 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1541 | 2024-12-03 | 0.1291 | ❌ |
| 503 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1537 | 2026-02-25 | 0.5366 | ❌ |
| 504 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1526 | 2025-07-07 | 0.2622 | ❌ |
| 505 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1519 | 2025-04-28 | 0.2097 | ❌ |
| 506 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1507 | 2026-03-06 | 0.5514 | ❌ |
| 507 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1493 | 2025-01-30 | 0.1572 | ❌ |
| 508 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1490 | 2025-10-28 | 0.3726 | ❌ |
| 509 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1488 | 2026-05-11 | 0.6720 | ❌ |
| 510 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1445 | 2025-04-28 | 0.2097 | ❌ |
| 511 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1418 | 2025-12-15 | 0.4315 | ❌ |
| 512 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1387 | 2025-09-22 | 0.3334 | ❌ |
| 513 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1383 | 2025-10-14 | 0.3569 | ❌ |
| 514 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1363 | 2025-03-12 | 0.1800 | ❌ |
| 515 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1342 | 2025-05-29 | 0.2317 | ❌ |
| 516 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1328 | 2025-12-02 | 0.4147 | ❌ |
| 517 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1325 | 2025-04-28 | 0.2097 | ❌ |
| 518 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1278 | 2024-12-12 | 0.1332 | ❌ |
| 519 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1270 | 2025-05-20 | 0.2251 | ❌ |
| 520 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1248 | 2025-08-14 | 0.2954 | ❌ |
| 521 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1197 | 2024-04-18 | 0.0547 | ❌ |
| 522 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1192 | 2024-09-25 | 0.1014 | ❌ |
| 523 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1173 | 2024-09-25 | 0.1014 | ❌ |
| 524 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1164 | 2026-03-02 | 0.5448 | ❌ |
| 525 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1158 | 2025-11-20 | 0.3998 | ❌ |
| 526 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1092 | 2026-01-05 | 0.4599 | ❌ |
| 527 | <img src="https://artificialanalysis.ai/img/logos//img/logos/reka.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1087 | 2025-03-10 | 0.1788 | ❌ |
| 528 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1083 | 2025-09-09 | 0.3203 | ❌ |
| 529 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1082 | 2025-09-23 | 0.3345 | ❌ |
| 530 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1073 | 2025-04-28 | 0.2097 | ❌ |
| 531 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1040 | 2025-12-11 | 0.4263 | ❌ |
| 532 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1037 | 2025-05-23 | 0.2273 | ❌ |
| 533 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.1025 | 2025-07-07 | 0.2622 | ❌ |
| 534 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.1011 | 2026-01-20 | 0.4813 | ❌ |
| 535 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0987 | 2024-02-26 | 0.0436 | ❌ |
| 536 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0985 | 2025-03-12 | 0.1800 | ❌ |
| 537 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0942 | 2025-09-02 | 0.3134 | ❌ |
| 538 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0939 | 2026-03-02 | 0.5448 | ❌ |
| 539 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0928 | 2025-11-20 | 0.3998 | ❌ |
| 540 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0918 | 2025-07-15 | 0.2689 | ❌ |
| 541 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0917 | 2025-03-13 | 0.1806 | ❌ |
| 542 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0912 | 2025-10-28 | 0.3726 | ❌ |
| 543 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0901 | 2024-09-25 | 0.1014 | ❌ |
| 544 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0890 | 2025-04-28 | 0.2097 | ❌ |
| 545 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0873 | 2026-04-29 | 0.6483 | ❌ |
| 546 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0848 | 2025-07-15 | 0.2689 | ❌ |
| 547 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0830 | 2025-10-07 | 0.3493 | ❌ |
| 548 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0804 | 2025-09-22 | 0.3334 | ❌ |
| 549 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0754 | 2024-04-23 | 0.0558 | ❌ |
| 550 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0720 | 2025-04-16 | 0.2018 | ❌ |
| 551 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0694 | 2026-01-05 | 0.4599 | ❌ |
| 552 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0687 | 2025-10-28 | 0.3726 | ❌ |
| 553 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0677 | 2025-10-28 | 0.3726 | ❌ |
| 554 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0668 | 2025-03-12 | 0.1800 | ❌ |
| 555 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0658 | 2025-07-10 | 0.2647 | ❌ |
| 556 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0652 | 2025-04-28 | 0.2097 | ❌ |
| 557 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0649 | 2024-04-18 | 0.0547 | ❌ |
| 558 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0625 | 2023-09-27 | 0.0192 | ❌ |
| 559 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0588 | 2025-06-26 | 0.2532 | ❌ |
| 560 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.0577 | 2026-09-03 | 0.9455 | ❌ |
| 561 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0570 | 2025-04-28 | 0.2097 | ❌ |
| 562 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0568 | 2024-11-26 | 0.1261 | ❌ |
| 563 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0564 | 2025-03-13 | 0.1806 | ❌ |
| 564 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0555 | 2025-09-02 | 0.3134 | ❌ |
| 565 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0512 | 2025-10-28 | 0.3726 | ❌ |
| 566 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0480 | 2024-09-25 | 0.1014 | ❌ |
| 567 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0440 | 2025-04-28 | 0.2097 | ❌ |
| 568 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0363 | 2025-06-26 | 0.2532 | ❌ |
| 569 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0359 | 2026-02-17 | 0.5239 | ❌ |
| 570 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | 2025-01-20 | 0.1520 | ❌ |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 13 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google.svg" width="18" alt="Google" /> Google | `#34A853` | 8 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 13 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 10 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 3 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且发布时间 ≤（更早），且至少一项严格更优）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.2433，即前沿左端点 GPT-4）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（指数）

横轴为发布时间指数映射：x = (a^(b*t)-1)/(a^b-1)；t 为发布时间按最早和最大映射到 [0,1]；a = 2.678，b = 3.763，用 11 品牌前沿定出；mse = 0.001561。

- **函数端点**：最早发布 → x = 0；前沿最大发布 → x = 1；
- 横轴时间标签：2024-01, 2025-01, 2026-01, 2026-09
- 中位数位置 0.573；左 165 个，右 253 个
- 前沿最大发布时间 2026-09-22 → x = 1；大于该值的模型不入图，表格中有。

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
**模型数**: 570（总体帕累托前沿 20 个；图表入图 418 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，同时点按能力从低到高连接）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.2433，前沿左端点 GPT-4 即 (0,0)），能力低于该级的 152 个模型和发布时间大于品牌前沿最大值的模型不出现在图中；横轴为发布时间（线性）。
