# LLM Leaderboard — 综合能力 vs 发布时间

![Pareto Analysis](output/pareto_analysis.png)

## 全部模型（综合能力从高到低，最优 = 1，最差 = 0）

共收录 **Status: All**（含已弃用）的全部模型；按重新归一化后的综合能力排序。「帕累托」项：✅ = 总体帕累托前沿模型，❌ = 被支配。图表纵轴以总体帕累托前沿第一级（y0 = 0.2371，即前沿左端点 GPT-4）为 0：综合能力 ≥ 该级的 416 个模型入图，152 个能力低于第一级的不出现在图中；发布时间大于品牌前沿最大值的模型同样不入图（表列出全部模型）。

| # | 品牌 | 模型 | 综合能力 | 发布时间 | 横轴位置 | 帕累托 |
|---|------|------|---------|-----------|-----------|------|
| 1 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (max with fallback) | 1.0000 | 2026-09-22 | 1.0000 | ✅ |
| 2 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (xhigh with fallback) | 0.9702 | 2026-09-22 | 1.0000 | ❌ |
| 3 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (max with fallback) | 0.9556 | 2026-09-01 | 0.9399 | ✅ |
| 4 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (xhigh with fallback) | 0.9419 | 2026-09-01 | 0.9399 | ❌ |
| 5 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (xhigh) | 0.9331 | 2026-09-03 | 0.9455 | ❌ |
| 6 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (max) | 0.9322 | 2026-09-03 | 0.9455 | ❌ |
| 7 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (high with fallback) | 0.9312 | 2026-09-22 | 1.0000 | ❌ |
| 8 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (max) | 0.9168 | 2026-07-24 | 0.8374 | ✅ |
| 9 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (high) | 0.9144 | 2026-09-03 | 0.9455 | ❌ |
| 10 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (high with fallback) | 0.9105 | 2026-09-01 | 0.9399 | ❌ |
| 11 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5 (with fallback) | 0.9101 | 2026-06-09 | 0.7327 | ✅ |
| 12 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (xhigh) | 0.9047 | 2026-07-24 | 0.8374 | ❌ |
| 13 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (medium with fallback) | 0.9034 | 2026-09-22 | 1.0000 | ❌ |
| 14 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (max) | 0.8953 | 2026-07-09 | 0.8010 | ❌ |
| 15 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (medium) | 0.8947 | 2026-09-03 | 0.9455 | ❌ |
| 16 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (max) | 0.8910 | 2026-09-02 | 0.9427 | ❌ |
| 17 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (high) | 0.8902 | 2026-07-24 | 0.8374 | ❌ |
| 18 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.3 (xhigh) | 0.8857 | 2026-09-02 | 0.9427 | ❌ |
| 19 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (medium with fallback) | 0.8789 | 2026-09-01 | 0.9399 | ❌ |
| 20 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (max) | 0.8616 | 2026-09-22 | 1.0000 | ❌ |
| 21 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Astra (low) | 0.8575 | 2026-09-03 | 0.9455 | ❌ |
| 22 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (max) | 0.8514 | 2026-07-16 | 0.8178 | ❌ |
| 23 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (medium) | 0.8504 | 2026-07-24 | 0.8374 | ❌ |
| 24 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (xhigh) | 0.8502 | 2026-07-09 | 0.8010 | ❌ |
| 25 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Fable 5.1 (low with fallback) | 0.8461 | 2026-09-01 | 0.9399 | ❌ |
| 26 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (xhigh) | 0.8427 | 2026-08-12 | 0.8859 | ❌ |
| 27 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (xhigh) | 0.8420 | 2026-04-23 | 0.6368 | ✅ |
| 28 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (high) | 0.8397 | 2026-08-12 | 0.8859 | ❌ |
| 29 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (high) | 0.8378 | 2026-09-02 | 0.9427 | ❌ |
| 30 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (medium) | 0.8330 | 2026-08-12 | 0.8859 | ❌ |
| 31 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (high) | 0.8309 | 2026-07-09 | 0.8010 | ❌ |
| 32 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3 (max) | 0.8297 | 2026-08-18 | 0.9018 | ❌ |
| 33 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (xhigh) | 0.8290 | 2026-09-22 | 1.0000 | ❌ |
| 34 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.6-Pro | 0.8283 | 2026-09-21 | 0.9971 | ❌ |
| 35 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (max) | 0.8266 | 2026-07-09 | 0.8010 | ❌ |
| 36 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max (0902) | 0.8266 | 2026-09-02 | 0.9427 | ❌ |
| 37 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.8 (max) | 0.8256 | 2026-05-28 | 0.7069 | ❌ |
| 38 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (xhigh) | 0.8225 | 2026-09-21 | 0.9971 | ❌ |
| 39 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (high) | 0.8188 | 2026-04-23 | 0.6368 | ❌ |
| 40 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.7 (high) | 0.8185 | 2026-09-21 | 0.9971 | ❌ |
| 41 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (high) | 0.8112 | 2026-08-13 | 0.8885 | ❌ |
| 42 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 5 Preview | 0.8108 | 2026-09-18 | 0.9883 | ❌ |
| 43 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (high) | 0.8102 | 2026-09-22 | 1.0000 | ❌ |
| 44 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (medium) | 0.8086 | 2026-09-02 | 0.9427 | ❌ |
| 45 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (medium) | 0.8077 | 2026-07-09 | 0.8010 | ❌ |
| 46 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 Max | 0.8069 | 2026-08-03 | 0.8626 | ❌ |
| 47 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5.5 (low with fallback) | 0.8016 | 2026-09-22 | 1.0000 | ❌ |
| 48 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.2 (xhigh) | 0.7966 | 2026-08-05 | 0.8677 | ❌ |
| 49 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 2.4T A95B | 0.7911 | 2026-08-12 | 0.8859 | ❌ |
| 50 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (medium) | 0.7877 | 2026-09-22 | 1.0000 | ❌ |
| 51 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (max) | 0.7847 | 2026-04-16 | 0.6236 | ✅ |
| 52 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (xhigh) | 0.7809 | 2026-03-05 | 0.5497 | ✅ |
| 53 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (max) | 0.7796 | 2026-06-30 | 0.7799 | ❌ |
| 54 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash | 0.7796 | 2026-05-19 | 0.6882 | ❌ |
| 55 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 5 (low) | 0.7773 | 2026-07-24 | 0.8374 | ❌ |
| 56 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.3-Flash | 0.7773 | 2026-08-26 | 0.9234 | ❌ |
| 57 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.5 (high) | 0.7768 | 2026-07-08 | 0.7986 | ❌ |
| 58 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (medium) | 0.7725 | 2026-04-23 | 0.6368 | ❌ |
| 59 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (max) | 0.7724 | 2026-06-16 | 0.7481 | ❌ |
| 60 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (medium) | 0.7704 | 2026-05-19 | 0.6882 | ❌ |
| 61 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.3 Codex (xhigh) | 0.7703 | 2026-02-05 | 0.5052 | ✅ |
| 62 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (xhigh) | 0.7681 | 2026-07-09 | 0.8010 | ❌ |
| 63 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (medium) | 0.7626 | 2026-08-13 | 0.8885 | ❌ |
| 64 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Pro Preview | 0.7619 | 2026-02-19 | 0.5270 | ❌ |
| 65 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark 1.1 (xhigh) | 0.7464 | 2026-07-09 | 0.8010 | ❌ |
| 66 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (low) | 0.7463 | 2026-07-09 | 0.8010 | ❌ |
| 67 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8-Flash-Next | 0.7355 | 2026-08-26 | 0.9234 | ❌ |
| 68 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.6 Flash | 0.7331 | 2026-07-21 | 0.8300 | ❌ |
| 69 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (high) | 0.7317 | 2026-07-09 | 0.8010 | ❌ |
| 70 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (max) | 0.7291 | 2026-02-05 | 0.5052 | ❌ |
| 71 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 | 0.7257 | 2026-04-07 | 0.6070 | ❌ |
| 72 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (max) | 0.7200 | 2026-07-09 | 0.8010 | ❌ |
| 73 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (low) | 0.7147 | 2026-09-22 | 1.0000 | ❌ |
| 74 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (high) | 0.7140 | 2025-11-18 | 0.3974 | ✅ |
| 75 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.8 Flash (low) | 0.7138 | 2026-09-02 | 0.9427 | ❌ |
| 76 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.7 Flash (low) | 0.7125 | 2026-08-13 | 0.8885 | ❌ |
| 77 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (medium) | 0.7121 | 2026-04-30 | 0.6503 | ❌ |
| 78 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Spark | 0.7085 | 2026-04-08 | 0.6088 | ❌ |
| 79 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.6 (low) | 0.7066 | 2026-08-12 | 0.8859 | ❌ |
| 80 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro 0813 (max) | 0.7066 | 2026-08-13 | 0.8885 | ❌ |
| 81 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (xhigh) | 0.7014 | 2025-12-11 | 0.4263 | ❌ |
| 82 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 Codex (xhigh) | 0.7009 | 2025-12-11 | 0.4263 | ❌ |
| 83 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Max Preview | 0.6999 | 2026-04-20 | 0.6311 | ❌ |
| 84 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (max) | 0.6999 | 2026-09-22 | 1.0000 | ❌ |
| 85 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Max | 0.6956 | 2026-05-19 | 0.6882 | ❌ |
| 86 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 | 0.6904 | 2026-04-20 | 0.6311 | ❌ |
| 87 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 | 0.6872 | 2026-03-10 | 0.5581 | ❌ |
| 88 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 | 0.6864 | 2025-11-24 | 0.4047 | ❌ |
| 89 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (xhigh) | 0.6856 | 2026-08-14 | 0.8912 | ❌ |
| 90 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (xhigh) | 0.6832 | 2026-07-09 | 0.8010 | ❌ |
| 91 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4.1 Flash (max) | 0.6823 | 2026-09-10 | 0.9652 | ❌ |
| 92 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.7 (Non-reasoning, high) | 0.6814 | 2026-04-16 | 0.6236 | ❌ |
| 93 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (low) | 0.6778 | 2026-04-23 | 0.6368 | ❌ |
| 94 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash Vision (max) | 0.6714 | 2026-08-21 | 0.9098 | ❌ |
| 95 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash | 0.6711 | 2025-12-17 | 0.4341 | ❌ |
| 96 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash 0731 (max) | 0.6684 | 2026-07-31 | 0.8550 | ❌ |
| 97 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (max) | 0.6667 | 2026-02-17 | 0.5239 | ❌ |
| 98 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (low) | 0.6642 | 2026-03-05 | 0.5497 | ❌ |
| 99 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (xhigh) | 0.6618 | 2026-06-30 | 0.7799 | ❌ |
| 100 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (medium) | 0.6609 | 2026-07-09 | 0.8010 | ❌ |
| 101 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 | 0.6603 | 2026-08-12 | 0.8859 | ❌ |
| 102 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K3 (low) | 0.6598 | 2026-07-16 | 0.8178 | ❌ |
| 103 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M3 | 0.6561 | 2026-06-01 | 0.7154 | ❌ |
| 104 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (low) | 0.6561 | 2026-04-30 | 0.6503 | ❌ |
| 105 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (xhigh) | 0.6553 | 2026-09-22 | 1.0000 | ❌ |
| 106 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Pro | 0.6534 | 2026-03-18 | 0.5716 | ❌ |
| 107 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 Plus | 0.6524 | 2026-04-02 | 0.5980 | ❌ |
| 108 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.7 Plus | 0.6522 | 2026-06-01 | 0.7154 | ❌ |
| 109 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (high) | 0.6489 | 2026-07-09 | 0.8010 | ❌ |
| 110 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (medium) | 0.6482 | 2025-12-11 | 0.4263 | ❌ |
| 111 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (max) | 0.6455 | 2026-04-24 | 0.6387 | ❌ |
| 112 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 | 0.6399 | 2026-04-07 | 0.6070 | ❌ |
| 113 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 Codex (high) | 0.6352 | 2025-09-23 | 0.3345 | ✅ |
| 114 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (high) | 0.6333 | 2026-04-24 | 0.6387 | ❌ |
| 115 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (high) | 0.6311 | 2026-04-30 | 0.6503 | ❌ |
| 116 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 | 0.6303 | 2026-02-11 | 0.5145 | ❌ |
| 117 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (high) | 0.6298 | 2026-09-22 | 1.0000 | ❌ |
| 118 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (high) | 0.6245 | 2025-11-13 | 0.3913 | ❌ |
| 119 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 375B A23B | 0.6242 | 2026-09-03 | 0.9455 | ❌ |
| 120 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (high) | 0.6217 | 2026-06-30 | 0.7799 | ❌ |
| 121 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.7 Code | 0.6191 | 2026-06-12 | 0.7392 | ❌ |
| 122 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex (high) | 0.6175 | 2025-11-13 | 0.3913 | ❌ |
| 123 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (xhigh) | 0.6119 | 2026-03-17 | 0.5699 | ❌ |
| 124 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni-0327 | 0.6079 | 2026-03-27 | 0.5873 | ❌ |
| 125 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (medium) | 0.6058 | 2025-08-07 | 0.2890 | ✅ |
| 126 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-VL | 0.6015 | 2026-09-10 | 0.9652 | ❌ |
| 127 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (low) | 0.5995 | 2026-07-09 | 0.8010 | ❌ |
| 128 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.6 (Non-reasoning, high) | 0.5987 | 2026-02-05 | 0.5052 | ❌ |
| 129 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5-Turbo | 0.5983 | 2026-03-15 | 0.5665 | ❌ |
| 130 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling Small | 0.5978 | 2026-07-30 | 0.8525 | ❌ |
| 131 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro | 0.5974 | 2026-04-22 | 0.6349 | ❌ |
| 132 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 | 0.5965 | 2025-07-10 | 0.2647 | ✅ |
| 133 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5 | 0.5942 | 2026-04-22 | 0.6349 | ❌ |
| 134 | <img src="https://artificialanalysis.ai/img/logos//img/logos/apodex.svg" width="18" alt="Apodex" /> Apodex | Apodex 1.1 | 0.5939 | 2026-08-30 | 0.9343 | ❌ |
| 135 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (max) | 0.5935 | 2026-04-24 | 0.6387 | ❌ |
| 136 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 4 | 0.5920 | 2026-08-06 | 0.8703 | ❌ |
| 137 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (high) | 0.5919 | 2025-08-07 | 0.2890 | ❌ |
| 138 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (medium) | 0.5917 | 2026-09-22 | 1.0000 | ❌ |
| 139 | <img src="https://artificialanalysis.ai/img/logos//img/logos/thinking_machines.svg" width="18" alt="Thinking Machines" /> Thinking Machines | Inkling | 0.5913 | 2026-07-15 | 0.8154 | ❌ |
| 140 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (high) | 0.5909 | 2026-04-24 | 0.6387 | ❌ |
| 141 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Build 0.1 0616 | 0.5889 | 2026-06-16 | 0.7481 | ❌ |
| 142 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (May 2026) | 0.5879 | 2026-05-05 | 0.6600 | ❌ |
| 143 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Opus | 0.5863 | 2025-05-22 | 0.2265 | ✅ |
| 144 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open2 250B | 0.5784 | 2026-08-12 | 0.8859 | ❌ |
| 145 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash (minimal) | 0.5771 | 2026-05-19 | 0.6882 | ❌ |
| 146 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B | 0.5769 | 2026-02-24 | 0.5350 | ❌ |
| 147 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Feb 2026) | 0.5765 | 2025-12-16 | 0.4328 | ❌ |
| 148 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (xhigh) | 0.5765 | 2026-03-17 | 0.5699 | ❌ |
| 149 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | Quasar 438B (max) | 0.5747 | 2026-08-10 | 0.8807 | ❌ |
| 150 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Omni | 0.5744 | 2026-03-19 | 0.5734 | ❌ |
| 151 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3 | 0.5738 | 2025-04-16 | 0.2018 | ✅ |
| 152 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nex_small.svg" width="18" alt="Nex AGI" /> Nex AGI | Nex-N2-Pro | 0.5737 | 2026-06-02 | 0.7175 | ❌ |
| 153 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif 3 (Beta) | 0.5714 | 2026-07-14 | 0.8130 | ❌ |
| 154 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM 5V Turbo | 0.5701 | 2026-04-01 | 0.5962 | ❌ |
| 155 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B | 0.5701 | 2026-04-22 | 0.6349 | ❌ |
| 156 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 | 0.5682 | 2026-01-27 | 0.4917 | ❌ |
| 157 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet | 0.5661 | 2025-09-29 | 0.3407 | ❌ |
| 158 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (medium) | 0.5647 | 2025-08-07 | 0.2890 | ❌ |
| 159 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Ultra | 0.5642 | 2026-06-04 | 0.7218 | ❌ |
| 160 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.1 Opus | 0.5623 | 2025-08-05 | 0.2872 | ❌ |
| 161 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, high) | 0.5606 | 2026-02-17 | 0.5239 | ❌ |
| 162 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 Thinking | 0.5602 | 2025-11-06 | 0.3830 | ❌ |
| 163 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Opus 4.5 (Non-reasoning) | 0.5581 | 2025-11-24 | 0.4047 | ❌ |
| 164 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 4.6 (Non-reasoning, low) | 0.5553 | 2026-02-17 | 0.5239 | ❌ |
| 165 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (medium) | 0.5548 | 2026-08-14 | 0.8912 | ❌ |
| 166 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B | 0.5545 | 2026-02-16 | 0.5223 | ❌ |
| 167 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.6 (Non-reasoning) | 0.5532 | 2026-04-20 | 0.6311 | ❌ |
| 168 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Pro Preview (low) | 0.5521 | 2025-11-18 | 0.3974 | ❌ |
| 169 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.5 Flash-Lite | 0.5509 | 2026-07-21 | 0.8300 | ❌ |
| 170 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (medium) | 0.5497 | 2026-06-30 | 0.7799 | ❌ |
| 171 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sktelecom_small.svg" width="18" alt="SK Telecom" /> SK Telecom | A.X-K2 | 0.5457 | 2026-08-12 | 0.8859 | ❌ |
| 172 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (medium) | 0.5454 | 2026-07-09 | 0.8010 | ❌ |
| 173 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.7 | 0.5446 | 2026-03-18 | 0.5716 | ❌ |
| 174 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3 | 0.5441 | 2026-07-06 | 0.7939 | ❌ |
| 175 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Sol (Non-reasoning) | 0.5439 | 2026-07-09 | 0.8010 | ❌ |
| 176 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 Codex mini (high) | 0.5439 | 2025-11-13 | 0.3913 | ❌ |
| 177 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon MoVA 36B A4B | 0.5412 | 2026-09-03 | 0.9455 | ❌ |
| 178 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (low) | 0.5401 | 2025-08-07 | 0.2890 | ❌ |
| 179 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview | 0.5400 | 2026-04-23 | 0.6368 | ❌ |
| 180 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B (low) | 0.5398 | 2026-08-14 | 0.8912 | ❌ |
| 181 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.5 | 0.5348 | 2026-02-12 | 0.5160 | ❌ |
| 182 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.1 (Non-reasoning) | 0.5337 | 2026-04-07 | 0.6070 | ❌ |
| 183 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Plus | 0.5334 | 2026-03-30 | 0.5926 | ❌ |
| 184 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B | 0.5297 | 2026-04-16 | 0.6236 | ❌ |
| 185 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-4.1 Flash 236B A21B | 0.5285 | 2026-07-09 | 0.8010 | ❌ |
| 186 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (Non-reasoning) | 0.5284 | 2026-06-30 | 0.7799 | ❌ |
| 187 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast | 0.5267 | 2025-11-19 | 0.3986 | ❌ |
| 188 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Sol (Non-reasoning) | 0.5252 | 2026-09-22 | 1.0000 | ❌ |
| 189 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Flash | 0.5234 | 2026-08-04 | 0.8652 | ❌ |
| 190 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano | 0.5209 | 2026-03-17 | 0.5699 | ❌ |
| 191 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (high) | 0.5204 | 2025-08-07 | 0.2890 | ❌ |
| 192 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2.1 | 0.5200 | 2025-12-23 | 0.4421 | ❌ |
| 193 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking | 0.5199 | 2026-01-26 | 0.4902 | ❌ |
| 194 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B | 0.5180 | 2026-02-24 | 0.5350 | ❌ |
| 195 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B | 0.5147 | 2026-02-24 | 0.5350 | ❌ |
| 196 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.7 Flash | 0.5143 | 2026-05-29 | 0.7090 | ❌ |
| 197 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-39A5B | 0.5117 | 2026-08-20 | 0.9071 | ❌ |
| 198 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2.5 (Non-reasoning) | 0.5095 | 2026-01-27 | 0.4917 | ❌ |
| 199 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash | 0.5083 | 2025-12-16 | 0.4328 | ❌ |
| 200 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (medium) | 0.5072 | 2026-03-17 | 0.5699 | ❌ |
| 201 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3 Flash (Non-reasoning) | 0.5027 | 2025-12-17 | 0.4341 | ❌ |
| 202 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 | 0.5022 | 2025-12-22 | 0.4408 | ❌ |
| 203 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 | 0.5000 | 2025-12-01 | 0.4135 | ❌ |
| 204 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B | 0.4990 | 2026-04-02 | 0.5980 | ❌ |
| 205 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V2 | 0.4988 | 2026-03-27 | 0.5873 | ❌ |
| 206 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5 (Non-reasoning) | 0.4986 | 2026-02-11 | 0.5145 | ❌ |
| 207 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.8 27B | 0.4980 | 2026-08-14 | 0.8912 | ❌ |
| 208 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-3.0-flash-Fin | 0.4929 | 2026-09-11 | 0.9681 | ❌ |
| 209 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (low) | 0.4929 | 2026-07-09 | 0.8010 | ❌ |
| 210 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 397B A17B (Non-reasoning) | 0.4920 | 2026-02-16 | 0.5223 | ❌ |
| 211 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash 2603 | 0.4919 | 2026-04-02 | 0.5980 | ❌ |
| 212 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (low) | 0.4908 | 2026-09-22 | 1.0000 | ❌ |
| 213 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet | 0.4903 | 2025-05-22 | 0.2265 | ❌ |
| 214 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude Sonnet 5 (low) | 0.4859 | 2026-06-30 | 0.7799 | ❌ |
| 215 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast | 0.4857 | 2025-09-19 | 0.3304 | ❌ |
| 216 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Muse Glimmer (high) | 0.4856 | 2026-08-10 | 0.8807 | ❌ |
| 217 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 (Non-reasoning) | 0.4813 | 2026-04-23 | 0.6368 | ❌ |
| 218 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 mini Reasoning (high) | 0.4788 | 2025-02-19 | 0.1680 | ✅ |
| 219 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 27B (Non-reasoning) | 0.4775 | 2026-02-24 | 0.5350 | ❌ |
| 220 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Sonnet (Non-reasoning) | 0.4772 | 2025-09-29 | 0.3407 | ❌ |
| 221 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Speciale | 0.4763 | 2025-12-01 | 0.4135 | ❌ |
| 222 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-35B-Flash | 0.4754 | 2026-05-14 | 0.6780 | ❌ |
| 223 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step 3.5 Flash | 0.4746 | 2026-02-02 | 0.5007 | ❌ |
| 224 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE 2.0 | 0.4727 | 2026-08-12 | 0.8859 | ❌ |
| 225 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.5 Instant (June 2026) | 0.4695 | 2026-06-25 | 0.7684 | ❌ |
| 226 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A+ | 0.4675 | 2026-05-20 | 0.6903 | ❌ |
| 227 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-2.6-1T | 0.4651 | 2026-05-08 | 0.6660 | ❌ |
| 228 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 (Non-reasoning) | 0.4625 | 2026-03-05 | 0.5497 | ❌ |
| 229 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax-M2 | 0.4622 | 2025-10-26 | 0.3703 | ❌ |
| 230 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Pro | 0.4613 | 2025-06-05 | 0.2369 | ❌ |
| 231 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Doubao Seed Code | 0.4590 | 2025-11-11 | 0.3889 | ❌ |
| 232 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o4-mini (high) | 0.4587 | 2025-04-16 | 0.2018 | ❌ |
| 233 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o1 | 0.4587 | 2024-12-05 | 0.1300 | ✅ |
| 234 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.5 | 0.4578 | 2026-04-29 | 0.6483 | ❌ |
| 235 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 7B | 0.4549 | 2026-09-03 | 0.9455 | ❌ |
| 236 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku | 0.4490 | 2025-10-15 | 0.3580 | ❌ |
| 237 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Pro (Non-reasoning) | 0.4478 | 2026-04-24 | 0.6387 | ❌ |
| 238 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Terra (Non-reasoning) | 0.4442 | 2026-07-09 | 0.8010 | ❌ |
| 239 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet | 0.4437 | 2025-02-24 | 0.1708 | ❌ |
| 240 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4 Sonnet (Non-reasoning) | 0.4409 | 2025-05-22 | 0.2265 | ❌ |
| 241 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (medium) | 0.4381 | 2025-11-27 | 0.4084 | ❌ |
| 242 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-5.2 (Non-reasoning) | 0.4358 | 2026-06-16 | 0.7481 | ❌ |
| 243 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) | 0.4354 | 2025-09-25 | 0.3365 | ❌ |
| 244 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat 2.0 | 0.4350 | 2026-06-29 | 0.7775 | ❌ |
| 245 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 27B (Non-reasoning) | 0.4345 | 2026-04-22 | 0.6349 | ❌ |
| 246 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp | 0.4312 | 2025-09-29 | 0.3407 | ❌ |
| 247 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kwaikat_small.svg" width="18" alt="KwaiKAT" /> KwaiKAT | KAT-Coder-Pro V1 | 0.4304 | 2025-11-11 | 0.3889 | ❌ |
| 248 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 3.1 Flash-Lite | 0.4303 | 2026-03-03 | 0.5464 | ❌ |
| 249 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.2 (Non-reasoning) | 0.4289 | 2025-12-11 | 0.4263 | ❌ |
| 250 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus | 0.4269 | 2025-09-22 | 0.3334 | ❌ |
| 251 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.7 Sonnet (Non-reasoning) | 0.4210 | 2025-02-24 | 0.1708 | ❌ |
| 252 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max Thinking (Preview) | 0.4201 | 2025-11-03 | 0.3795 | ❌ |
| 253 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (low) | 0.4198 | 2025-11-27 | 0.4084 | ❌ |
| 254 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 122B A10B (Non-reasoning) | 0.4169 | 2026-02-24 | 0.5350 | ❌ |
| 255 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash | 0.4151 | 2025-05-20 | 0.2251 | ❌ |
| 256 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (medium) | 0.4149 | 2025-10-29 | 0.3737 | ❌ |
| 257 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B | 0.4137 | 2026-03-02 | 0.5448 | ❌ |
| 258 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2.5-Pro (Non-reasoning) | 0.4101 | 2026-04-22 | 0.6349 | ❌ |
| 259 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 4.5 Haiku (Non-reasoning) | 0.4099 | 2025-10-15 | 0.3580 | ❌ |
| 260 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 0905 | 0.4073 | 2025-09-05 | 0.3163 | ❌ |
| 261 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 5.0 Thinking Preview | 0.4067 | 2025-11-13 | 0.3913 | ❌ |
| 262 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V4 Flash (Non-reasoning) | 0.4060 | 2026-04-24 | 0.6387 | ❌ |
| 263 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B (Reasoning) | 0.4060 | 2025-09-23 | 0.3345 | ❌ |
| 264 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B | 0.4049 | 2026-04-02 | 0.5980 | ❌ |
| 265 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 (Non-reasoning) | 0.4036 | 2026-03-10 | 0.5581 | ❌ |
| 266 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-2.6-1T | 0.4032 | 2026-04-23 | 0.6368 | ❌ |
| 267 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (low) | 0.3998 | 2025-11-26 | 0.4072 | ❌ |
| 268 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 (Non-reasoning) | 0.3976 | 2025-12-01 | 0.4135 | ❌ |
| 269 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.5 33B | 0.3966 | 2026-04-09 | 0.6106 | ❌ |
| 270 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B | 0.3959 | 2026-03-02 | 0.5448 | ❌ |
| 271 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tencent_small.svg" width="18" alt="Tencent" /> Tencent | Hy3-preview (Non-reasoning) | 0.3958 | 2026-04-23 | 0.6368 | ❌ |
| 272 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (high) | 0.3958 | 2025-08-07 | 0.2890 | ❌ |
| 273 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (high) | 0.3947 | 2025-10-29 | 0.3737 | ❌ |
| 274 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (medium) | 0.3938 | 2025-08-07 | 0.2890 | ❌ |
| 275 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 3.0 Tiny | 0.3930 | 2026-08-06 | 0.8703 | ❌ |
| 276 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7 (Non-reasoning) | 0.3929 | 2025-12-22 | 0.4408 | ❌ |
| 277 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (medium) | 0.3918 | 2025-11-26 | 0.4072 | ❌ |
| 278 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.20 0309 v2 (Non-reasoning) | 0.3879 | 2026-04-07 | 0.6070 | ❌ |
| 279 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.6 35B A3B (Non-reasoning) | 0.3854 | 2026-04-16 | 0.6236 | ❌ |
| 280 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B | 0.3854 | 2026-06-03 | 0.7197 | ❌ |
| 281 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 | 0.3845 | 2025-08-21 | 0.3019 | ❌ |
| 282 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5 | 0.3839 | 2025-07-28 | 0.2801 | ❌ |
| 283 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max | 0.3783 | 2025-09-23 | 0.3345 | ❌ |
| 284 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-2B | 0.3774 | 2026-09-07 | 0.9567 | ❌ |
| 285 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok Code Fast 1 | 0.3755 | 2025-08-28 | 0.3085 | ❌ |
| 286 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.3 (Non-reasoning) | 0.3754 | 2026-04-30 | 0.6503 | ❌ |
| 287 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi K2 | 0.3745 | 2025-07-11 | 0.2655 | ❌ |
| 288 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 | 0.3732 | 2025-05-28 | 0.2309 | ❌ |
| 289 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE | 0.3724 | 2025-12-31 | 0.4530 | ❌ |
| 290 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 | 0.3723 | 2025-09-30 | 0.3418 | ❌ |
| 291 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs_small.svg" width="18" alt="Inception" /> Inception | Mercury 2 | 0.3713 | 2026-02-20 | 0.5286 | ❌ |
| 292 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 31B (Non-reasoning) | 0.3692 | 2026-04-02 | 0.5980 | ❌ |
| 293 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-6 Luna (Non-reasoning) | 0.3687 | 2026-09-22 | 1.0000 | ❌ |
| 294 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Sep) (Non-reasoning) | 0.3676 | 2025-09-25 | 0.3365 | ❌ |
| 295 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.6 Luna (Non-reasoning) | 0.3653 | 2026-07-09 | 0.8010 | ❌ |
| 296 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (minimal) | 0.3650 | 2025-08-07 | 0.2890 | ❌ |
| 297 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B (Reasoning) | 0.3641 | 2025-10-21 | 0.3646 | ❌ |
| 298 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 3.7B | 0.3640 | 2026-09-03 | 0.9455 | ❌ |
| 299 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Super | 0.3636 | 2026-03-11 | 0.5597 | ❌ |
| 300 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 | 0.3630 | 2025-04-14 | 0.2005 | ❌ |
| 301 | <img src="https://artificialanalysis.ai/img/logos//img/logos/arcee_small.svg" width="18" alt="Arcee AI" /> Arcee AI | Trinity Large Thinking | 0.3624 | 2026-04-01 | 0.5962 | ❌ |
| 302 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 30B | 0.3621 | 2026-08-25 | 0.9206 | ❌ |
| 303 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.1 (Non-reasoning) | 0.3615 | 2025-11-13 | 0.3913 | ❌ |
| 304 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (low) | 0.3611 | 2025-10-29 | 0.3737 | ❌ |
| 305 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 9B (Non-reasoning) | 0.3602 | 2026-03-02 | 0.5448 | ❌ |
| 306 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash | 0.3601 | 2026-01-19 | 0.4799 | ❌ |
| 307 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6 (Non-reasoning) | 0.3566 | 2025-09-30 | 0.3418 | ❌ |
| 308 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 35B A3B (Non-reasoning) | 0.3564 | 2026-02-24 | 0.5350 | ❌ |
| 309 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3.5 Lightning | 0.3554 | 2026-08-11 | 0.8833 | ❌ |
| 310 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.5-15B-Thinker | 0.3529 | 2025-09-30 | 0.3418 | ❌ |
| 311 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B A22B 2507 | 0.3511 | 2025-07-25 | 0.2774 | ❌ |
| 312 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 Omni Flash | 0.3490 | 2026-03-30 | 0.5926 | ❌ |
| 313 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 480B | 0.3481 | 2025-07-22 | 0.2748 | ❌ |
| 314 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) | 0.3471 | 2025-09-25 | 0.3365 | ❌ |
| 315 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron Cascade 2 30B A3B | 0.3470 | 2026-03-19 | 0.5734 | ❌ |
| 316 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepcogito_small.png" width="18" alt="Deep Cogito" /> Deep Cogito | Cogito v2.1 | 0.3468 | 2025-11-18 | 0.3974 | ❌ |
| 317 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1.2 | 0.3439 | 2025-09-18 | 0.3293 | ❌ |
| 318 | <img src="https://artificialanalysis.ai/img/logos//img/logos/servicenow_small.svg" width="18" alt="ServiceNow" /> ServiceNow | Apriel-v1.6-15B-Thinker | 0.3429 | 2025-11-25 | 0.4060 | ❌ |
| 319 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 26B A4B (Non-reasoning) | 0.3418 | 2026-04-02 | 0.5980 | ❌ |
| 320 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai9stars.svg" width="18" alt="AI9Stars" /> AI9Stars | G9v3-3B | 0.3417 | 2026-07-23 | 0.8349 | ❌ |
| 321 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 3 | 0.3413 | 2025-02-19 | 0.1680 | ❌ |
| 322 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V | 0.3406 | 2025-12-08 | 0.4224 | ❌ |
| 323 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 Terminus (Non-reasoning) | 0.3399 | 2025-09-22 | 0.3334 | ❌ |
| 324 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (high) | 0.3390 | 2025-08-05 | 0.2872 | ❌ |
| 325 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 (ChatGPT) | 0.3359 | 2025-08-07 | 0.2890 | ❌ |
| 326 | <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | MiMo-V2-Flash (Non-reasoning) | 0.3313 | 2025-12-16 | 0.4328 | ❌ |
| 327 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Max (Preview) | 0.3289 | 2025-09-05 | 0.3163 | ❌ |
| 328 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 | 0.3260 | 2026-03-16 | 0.5682 | ❌ |
| 329 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.2 Exp (Non-reasoning) | 0.3227 | 2025-09-29 | 0.3407 | ❌ |
| 330 | <img src="https://artificialanalysis.ai/img/logos//img/logos/multiversecomputing_small.svg" width="18" alt="Multiverse Computing" /> Multiverse Computing | HyperNova 60B 2605 (high) | 0.3210 | 2026-05-26 | 0.7027 | ❌ |
| 331 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Sep) (Non-reasoning) | 0.3204 | 2025-09-25 | 0.3365 | ❌ |
| 332 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3.1 (Non-reasoning) | 0.3196 | 2025-08-21 | 0.3019 | ❌ |
| 333 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | North Mini Code | 0.3169 | 2026-06-09 | 0.7327 | ❌ |
| 334 | <img src="https://artificialanalysis.ai/img/logos//img/logos/bytedance_small.svg" width="18" alt="ByteDance Seed" /> ByteDance Seed | Seed-OSS-36B-Instruct | 0.3159 | 2025-08-20 | 0.3009 | ❌ |
| 335 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini (high) | 0.3135 | 2025-01-31 | 0.1577 | ❌ |
| 336 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Nov) | 0.3125 | 2024-11-20 | 0.1235 | ✅ |
| 337 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash (Non-reasoning) | 0.3104 | 2025-05-20 | 0.2251 | ❌ |
| 338 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 8B | 0.3101 | 2026-08-25 | 0.9206 | ❌ |
| 339 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 3 | 0.3093 | 2026-04-06 | 0.6052 | ❌ |
| 340 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o (Aug) | 0.3091 | 2024-08-06 | 0.0844 | ✅ |
| 341 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B 2507 | 0.3086 | 2025-07-21 | 0.2740 | ❌ |
| 342 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Think V2 | 0.3079 | 2025-12-15 | 0.4315 | ❌ |
| 343 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite | 0.3062 | 2025-06-17 | 0.2461 | ❌ |
| 344 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4.1 Fast (Non-reasoning) | 0.3025 | 2025-11-19 | 0.3986 | ❌ |
| 345 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B (Reasoning) | 0.3017 | 2025-09-11 | 0.3223 | ❌ |
| 346 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 mini (minimal) | 0.3017 | 2025-08-07 | 0.2890 | ❌ |
| 347 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 12B (Non-reasoning) | 0.3005 | 2026-06-03 | 0.7197 | ❌ |
| 348 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 235B A22B | 0.2998 | 2025-09-23 | 0.3345 | ❌ |
| 349 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano | 0.2997 | 2025-12-15 | 0.4315 | ❌ |
| 350 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | QwQ-32B | 0.2980 | 2025-03-05 | 0.1759 | ❌ |
| 351 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-1T | 0.2970 | 2025-10-13 | 0.3558 | ❌ |
| 352 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B | 0.2970 | 2026-05-25 | 0.7006 | ❌ |
| 353 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM5-1B (Non-reasoning) | 0.2968 | 2026-05-25 | 0.7006 | ❌ |
| 354 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Pixtral Large | 0.2957 | 2024-11-18 | 0.1226 | ❌ |
| 355 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Open 100B | 0.2924 | 2025-12-17 | 0.4341 | ❌ |
| 356 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 4B (Non-reasoning) | 0.2902 | 2026-03-02 | 0.5448 | ❌ |
| 357 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder Next | 0.2897 | 2026-02-03 | 0.5022 | ❌ |
| 358 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | o3-mini | 0.2896 | 2025-01-31 | 0.1577 | ❌ |
| 359 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5-Air | 0.2890 | 2025-07-28 | 0.2801 | ❌ |
| 360 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 80k | 0.2888 | 2025-06-17 | 0.2461 | ❌ |
| 361 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inceptionlabs_small.svg" width="18" alt="Inception" /> Inception | Mercury 2.5 | 0.2887 | 2026-09-08 | 0.9595 | ❌ |
| 362 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B | 0.2881 | 2026-04-03 | 0.5998 | ❌ |
| 363 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Pro Preview (Non-reasoning) | 0.2866 | 2025-11-27 | 0.4084 | ❌ |
| 364 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 nano (Non-reasoning) | 0.2863 | 2026-03-17 | 0.5699 | ❌ |
| 365 | <img src="https://artificialanalysis.ai/img/logos//img/logos/china_mobile_small.png" width="18" alt="China Mobile" /> China Mobile | JT-MINI | 0.2844 | 2026-04-15 | 0.6217 | ❌ |
| 366 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | DiffusionGemma 26B A4B | 0.2835 | 2026-06-10 | 0.7348 | ❌ |
| 367 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3 | 0.2825 | 2025-05-07 | 0.2159 | ❌ |
| 368 | <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | MiniMax M1 40k | 0.2821 | 2025-06-17 | 0.2461 | ❌ |
| 369 | <img src="https://artificialanalysis.ai/img/logos//img/logos/naver_small.webp" width="18" alt="Naver" /> Naver | HyperCLOVA X SEED Think (32B) | 0.2820 | 2025-12-26 | 0.4462 | ❌ |
| 370 | <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | Grok 4 Fast (Non-reasoning) | 0.2804 | 2025-09-19 | 0.3304 | ❌ |
| 371 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (high) | 0.2798 | 2025-12-05 | 0.4185 | ❌ |
| 372 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | K-EXAONE (Non-reasoning) | 0.2796 | 2025-12-31 | 0.4530 | ❌ |
| 373 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 0324 | 0.2784 | 2025-03-25 | 0.1878 | ❌ |
| 374 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5.4 mini (Non-reasoning) | 0.2781 | 2026-03-17 | 0.5699 | ❌ |
| 375 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro | 0.2769 | 2025-12-11 | 0.4263 | ❌ |
| 376 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 (Jan) | 0.2760 | 2025-01-20 | 0.1520 | ❌ |
| 377 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 3 | 0.2753 | 2025-12-02 | 0.4147 | ❌ |
| 378 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Maverick | 0.2740 | 2025-04-05 | 0.1947 | ❌ |
| 379 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Medium 3.1 | 0.2730 | 2025-08-12 | 0.2935 | ❌ |
| 380 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (high) | 0.2710 | 2025-08-05 | 0.2872 | ❌ |
| 381 | <img src="https://artificialanalysis.ai/img/logos//img/logos/prime-intellect_small.svg" width="18" alt="Prime Intellect" /> Prime Intellect | INTELLECT-3 | 0.2703 | 2025-11-27 | 0.4084 | ❌ |
| 382 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano Omni 30B A3B | 0.2698 | 2026-04-29 | 0.6483 | ❌ |
| 383 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-think Preview | 0.2695 | 2026-02-10 | 0.5129 | ❌ |
| 384 | <img src="https://artificialanalysis.ai/img/logos//img/logos/longcat_small.svg" width="18" alt="LongCat" /> LongCat | LongCat Flash Lite | 0.2679 | 2026-01-28 | 0.4931 | ❌ |
| 385 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B (Reasoning) | 0.2676 | 2025-10-03 | 0.3450 | ❌ |
| 386 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 | 0.2676 | 2025-07-30 | 0.2818 | ❌ |
| 387 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-20b (low) | 0.2672 | 2025-08-05 | 0.2872 | ❌ |
| 388 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 405B | 0.2661 | 2024-07-23 | 0.0801 | ✅ |
| 389 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Premier | 0.2652 | 2025-04-30 | 0.2111 | ❌ |
| 390 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling 2.6 Flash | 0.2646 | 2026-04-21 | 0.6330 | ❌ |
| 391 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 mini | 0.2645 | 2025-04-14 | 0.2005 | ❌ |
| 392 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E4B (Non-reasoning) | 0.2641 | 2026-04-03 | 0.5998 | ❌ |
| 393 | <img src="https://artificialanalysis.ai/img/logos//img/logos/trillionlabs_small.svg" width="18" alt="Trillion Labs" /> Trillion Labs | Tri-21B-Think | 0.2639 | 2026-02-10 | 0.5129 | ❌ |
| 394 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.2 3B | 0.2591 | 2026-08-25 | 0.9206 | ❌ |
| 395 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Lite (Non-reasoning) | 0.2570 | 2025-10-29 | 0.3737 | ❌ |
| 396 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Next 80B A3B | 0.2562 | 2025-09-11 | 0.3223 | ❌ |
| 397 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 32B | 0.2560 | 2025-10-21 | 0.3646 | ❌ |
| 398 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B | 0.2543 | 2025-08-27 | 0.3076 | ❌ |
| 399 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (medium) | 0.2519 | 2025-12-05 | 0.4185 | ❌ |
| 400 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-1T | 0.2511 | 2025-10-08 | 0.3503 | ❌ |
| 401 | <img src="https://artificialanalysis.ai/img/logos//img/logos/korea-telecom_small.png" width="18" alt="Korea Telecom" /> Korea Telecom | Mi:dm K 2.5 Pro Preview | 0.2507 | 2025-12-11 | 0.4263 | ❌ |
| 402 | <img src="https://artificialanalysis.ai/img/logos//img/logos/motif_small.svg" width="18" alt="Motif Technologies" /> Motif Technologies | Motif-2-12.7B | 0.2506 | 2025-12-04 | 0.4173 | ❌ |
| 403 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | gpt-oss-120b (low) | 0.2503 | 2025-08-05 | 0.2872 | ❌ |
| 404 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3.5 Haiku | 0.2479 | 2024-10-22 | 0.1116 | ❌ |
| 405 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B (Reasoning) | 0.2475 | 2025-10-14 | 0.3569 | ❌ |
| 406 | <img src="https://artificialanalysis.ai/img/logos//img/logos/stepfun_small.svg" width="18" alt="StepFun" /> StepFun | Step3 VL 10B | 0.2458 | 2026-01-20 | 0.4813 | ❌ |
| 407 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 | 0.2437 | 2025-07-25 | 0.2774 | ❌ |
| 408 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.0 Flash | 0.2435 | 2025-02-05 | 0.1604 | ❌ |
| 409 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.7-Flash (Non-reasoning) | 0.2433 | 2026-01-19 | 0.4799 | ❌ |
| 410 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral 2 | 0.2415 | 2025-12-09 | 0.4237 | ❌ |
| 411 | <img src="https://artificialanalysis.ai/img/logos//img/logos/baidu_small.svg" width="18" alt="Baidu" /> Baidu | ERNIE 4.5 300B A47B | 0.2407 | 2025-06-30 | 0.2564 | ❌ |
| 412 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Medium 1 | 0.2397 | 2025-06-10 | 0.2407 | ❌ |
| 413 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Medium | 0.2381 | 2025-07-10 | 0.2647 | ❌ |
| 414 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 | 0.2377 | 2025-08-06 | 0.2881 | ❌ |
| 415 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova 2.0 Omni (Non-reasoning) | 0.2371 | 2025-11-26 | 0.4072 | ❌ |
| 416 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4 | 0.2371 | 2023-03-14 | 0.0000 | ✅ |
| 417 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 4 (Non-reasoning) | 0.2366 | 2026-03-16 | 0.5682 | ❌ |
| 418 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 405B (Non-reasoning) | 0.2355 | 2025-08-27 | 0.3076 | ❌ |
| 419 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Coder 30B A3B | 0.2342 | 2025-07-31 | 0.2827 | ❌ |
| 420 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-8B-A1B | 0.2320 | 2026-05-28 | 0.7069 | ❌ |
| 421 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 30B A3B | 0.2312 | 2025-10-03 | 0.3450 | ❌ |
| 422 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.6V (Non-reasoning) | 0.2306 | 2025-12-08 | 0.4224 | ❌ |
| 423 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B | 0.2293 | 2026-04-02 | 0.5980 | ❌ |
| 424 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B (Reasoning) | 0.2288 | 2025-09-22 | 0.3334 | ❌ |
| 425 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-2.6B | 0.2272 | 2026-08-04 | 0.8652 | ❌ |
| 426 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B | 0.2248 | 2025-04-28 | 0.2097 | ❌ |
| 427 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V | 0.2241 | 2025-08-11 | 0.2926 | ❌ |
| 428 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL | 0.2234 | 2025-10-28 | 0.3726 | ❌ |
| 429 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Nov) | 0.2224 | 2024-11-18 | 0.1226 | ❌ |
| 430 | <img src="https://artificialanalysis.ai/img/logos//img/logos/tii_small.svg" width="18" alt="TII UAE" /> TII UAE | Falcon-H1R-7B | 0.2210 | 2026-01-04 | 0.4586 | ❌ |
| 431 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Ultra | 0.2201 | 2025-04-07 | 0.1960 | ❌ |
| 432 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small 2 | 0.2189 | 2025-12-09 | 0.4237 | ❌ |
| 433 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek V3 (Dec) | 0.2125 | 2024-12-26 | 0.1397 | ❌ |
| 434 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Pro | 0.2113 | 2024-12-03 | 0.1291 | ❌ |
| 435 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nanbeige_small.png" width="18" alt="Nanbeige" /> Nanbeige | Nanbeige4.1-3B | 0.2111 | 2026-02-11 | 0.5145 | ❌ |
| 436 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Think | 0.2105 | 2025-12-12 | 0.4276 | ❌ |
| 437 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.2 | 0.2102 | 2025-06-20 | 0.2484 | ❌ |
| 438 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 105B (high) | 0.2096 | 2026-03-06 | 0.5514 | ❌ |
| 439 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B | 0.2087 | 2025-07-15 | 0.2689 | ❌ |
| 440 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1.2 | 0.2082 | 2025-09-17 | 0.3283 | ❌ |
| 441 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2-V2 (low) | 0.2073 | 2025-12-05 | 0.4185 | ❌ |
| 442 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 | 0.2067 | 2025-08-18 | 0.2991 | ❌ |
| 443 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B | 0.2067 | 2026-03-02 | 0.5448 | ❌ |
| 444 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ring-flash-2.0 | 0.2043 | 2025-09-19 | 0.3304 | ❌ |
| 445 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemini 2.5 Flash-Lite (Non-reasoning) | 0.2042 | 2025-06-17 | 0.2461 | ❌ |
| 446 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama Nemotron Super 49B v1.5 (Non-reasoning) | 0.2026 | 2025-07-25 | 0.2774 | ❌ |
| 447 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 4 Scout | 0.2018 | 2025-04-05 | 0.1947 | ❌ |
| 448 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B | 0.2007 | 2025-08-27 | 0.3076 | ❌ |
| 449 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small (May) | 0.1997 | 2025-05-21 | 0.2258 | ❌ |
| 450 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B | 0.1993 | 2025-04-28 | 0.2097 | ❌ |
| 451 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Lite | 0.1991 | 2024-12-03 | 0.1291 | ❌ |
| 452 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B | 0.1961 | 2025-03-18 | 0.1836 | ❌ |
| 453 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 32B | 0.1957 | 2025-01-20 | 0.1520 | ❌ |
| 454 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen2.5 72B | 0.1951 | 2024-09-19 | 0.0992 | ❌ |
| 455 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B | 0.1944 | 2025-04-28 | 0.2097 | ❌ |
| 456 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-flash-2.0 | 0.1943 | 2025-09-17 | 0.3283 | ❌ |
| 457 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 8B | 0.1937 | 2025-10-14 | 0.3569 | ❌ |
| 458 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B | 0.1923 | 2025-04-28 | 0.2097 | ❌ |
| 459 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Magistral Small 1 | 0.1918 | 2025-06-10 | 0.2407 | ❌ |
| 460 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Large 2 (Jul) | 0.1880 | 2024-07-24 | 0.0804 | ❌ |
| 461 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 14B | 0.1874 | 2025-12-02 | 0.4147 | ❌ |
| 462 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 | 0.1872 | 2025-07-09 | 0.2638 | ❌ |
| 463 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Command A | 0.1872 | 2025-03-13 | 0.1806 | ❌ |
| 464 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Devstral Small | 0.1866 | 2025-07-10 | 0.2647 | ❌ |
| 465 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 235B (Non-reasoning) | 0.1863 | 2025-04-28 | 0.2097 | ❌ |
| 466 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron 70B | 0.1850 | 2024-10-15 | 0.1089 | ❌ |
| 467 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano 4B | 0.1837 | 2026-03-16 | 0.5682 | ❌ |
| 468 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B (Reasoning) | 0.1825 | 2025-10-14 | 0.3569 | ❌ |
| 469 | <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | Claude 3 Haiku | 0.1814 | 2024-03-04 | 0.0450 | ❌ |
| 470 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3.1 | 0.1806 | 2025-03-17 | 0.1830 | ❌ |
| 471 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.3 Nemotron Super 49B (Non-reasoning) | 0.1800 | 2025-03-18 | 0.1836 | ❌ |
| 472 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B A3B 2507 (Non-reasoning) | 0.1782 | 2025-07-29 | 0.2809 | ❌ |
| 473 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B | 0.1768 | 2025-04-28 | 0.2097 | ❌ |
| 474 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 70B | 0.1763 | 2024-07-23 | 0.0801 | ❌ |
| 475 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 9B V2 (Non-reasoning) | 0.1761 | 2025-08-18 | 0.2991 | ❌ |
| 476 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 32B (Non-reasoning) | 0.1746 | 2025-04-28 | 0.2097 | ❌ |
| 477 | <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | GLM-4.5V (Non-reasoning) | 0.1742 | 2025-08-11 | 0.2926 | ❌ |
| 478 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 4 E2B (Non-reasoning) | 0.1742 | 2026-04-02 | 0.5980 | ❌ |
| 479 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 2B (Non-reasoning) | 0.1724 | 2026-03-02 | 0.5448 | ❌ |
| 480 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 30B | 0.1719 | 2026-04-29 | 0.6483 | ❌ |
| 481 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3.1 32B Instruct | 0.1689 | 2026-01-13 | 0.4712 | ❌ |
| 482 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 Omni 30B A3B | 0.1672 | 2025-09-22 | 0.3334 | ❌ |
| 483 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-5 nano (minimal) | 0.1666 | 2025-08-07 | 0.2890 | ❌ |
| 484 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 4B 2507 (Non-reasoning) | 0.1655 | 2025-08-06 | 0.2881 | ❌ |
| 485 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.1 8B | 0.1637 | 2024-07-23 | 0.0801 | ❌ |
| 486 | <img src="https://artificialanalysis.ai/img/logos//img/logos/celeris.svg" width="18" alt="Celeris" /> Celeris | Celeris-1 | 0.1615 | 2026-07-24 | 0.8374 | ❌ |
| 487 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 32B Think | 0.1614 | 2025-11-20 | 0.3998 | ❌ |
| 488 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4o mini | 0.1610 | 2024-07-18 | 0.0786 | ❌ |
| 489 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Llama 70B | 0.1606 | 2025-01-20 | 0.1520 | ❌ |
| 490 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | GPT-4.1 nano | 0.1605 | 2025-04-14 | 0.2005 | ❌ |
| 491 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.3 70B | 0.1604 | 2024-12-06 | 0.1305 | ❌ |
| 492 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 14B | 0.1602 | 2025-01-20 | 0.1520 | ❌ |
| 493 | <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | Kimi Linear 48B A3B Instruct | 0.1599 | 2025-10-30 | 0.3749 | ❌ |
| 494 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 8B | 0.1586 | 2025-12-02 | 0.4147 | ❌ |
| 495 | <img src="https://artificialanalysis.ai/img/logos//img/logos/upstage_small.svg" width="18" alt="Upstage" /> Upstage | Solar Pro 2 (Non-reasoning) | 0.1585 | 2025-07-09 | 0.2638 | ❌ |
| 496 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nousresearch_small.jpg" width="18" alt="Nous Research" /> Nous Research | Hermes 4 70B (Non-reasoning) | 0.1554 | 2025-08-27 | 0.3076 | ❌ |
| 497 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba Reasoning 3B | 0.1552 | 2025-10-08 | 0.3503 | ❌ |
| 498 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | EXAONE 4.0 32B (Non-reasoning) | 0.1530 | 2025-07-15 | 0.2689 | ❌ |
| 499 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 8B | 0.1530 | 2026-04-29 | 0.6483 | ❌ |
| 500 | <img src="https://artificialanalysis.ai/img/logos//img/logos/aws_small.svg" width="18" alt="Amazon" /> Amazon | Nova Micro | 0.1502 | 2024-12-03 | 0.1291 | ❌ |
| 501 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 24B A2B | 0.1498 | 2026-02-25 | 0.5366 | ❌ |
| 502 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Large | 0.1487 | 2025-07-07 | 0.2622 | ❌ |
| 503 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B | 0.1480 | 2025-04-28 | 0.2097 | ❌ |
| 504 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam 30B (high) | 0.1469 | 2026-03-06 | 0.5514 | ❌ |
| 505 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral Small 3 | 0.1455 | 2025-01-30 | 0.1572 | ❌ |
| 506 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | NVIDIA Nemotron Nano 12B v2 VL (Non-reasoning) | 0.1452 | 2025-10-28 | 0.3726 | ❌ |
| 507 | <img src="https://artificialanalysis.ai/img/logos//img/logos/openbmb_small.svg" width="18" alt="OpenBMB" /> OpenBMB | MiniCPM-V 4.6 1.3B | 0.1450 | 2026-05-11 | 0.6720 | ❌ |
| 508 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 30B (Non-reasoning) | 0.1408 | 2025-04-28 | 0.2097 | ❌ |
| 509 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Nemotron 3 Nano (Non-reasoning) | 0.1382 | 2025-12-15 | 0.4315 | ❌ |
| 510 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H Small | 0.1351 | 2025-09-22 | 0.3334 | ❌ |
| 511 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 VL 4B | 0.1347 | 2025-10-14 | 0.3569 | ❌ |
| 512 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 27B | 0.1328 | 2025-03-12 | 0.1800 | ❌ |
| 513 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 0528 Qwen3 8B | 0.1308 | 2025-05-29 | 0.2317 | ❌ |
| 514 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Ministral 3 3B | 0.1294 | 2025-12-02 | 0.4147 | ❌ |
| 515 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 14B (Non-reasoning) | 0.1291 | 2025-04-28 | 0.2097 | ❌ |
| 516 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 | 0.1246 | 2024-12-12 | 0.1332 | ❌ |
| 517 | <img src="https://artificialanalysis.ai/img/logos//img/logos/nvidia_small.svg" width="18" alt="NVIDIA" /> NVIDIA | Llama 3.1 Nemotron Nano 4B v1.1 | 0.1238 | 2025-05-20 | 0.2251 | ❌ |
| 518 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 270M | 0.1216 | 2025-08-14 | 0.2954 | ❌ |
| 519 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 70B | 0.1167 | 2024-04-18 | 0.0547 | ❌ |
| 520 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 11B (Vision) | 0.1162 | 2024-09-25 | 0.1014 | ❌ |
| 521 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 3B | 0.1143 | 2024-09-25 | 0.1014 | ❌ |
| 522 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B | 0.1134 | 2026-03-02 | 0.5448 | ❌ |
| 523 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B Think | 0.1129 | 2025-11-20 | 0.3998 | ❌ |
| 524 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Instruct | 0.1064 | 2026-01-05 | 0.4599 | ❌ |
| 525 | <img src="https://artificialanalysis.ai/img/logos//img/logos/reka_small.svg" width="18" alt="Reka AI" /> Reka AI | Reka Flash 3 | 0.1059 | 2025-03-10 | 0.1788 | ❌ |
| 526 | <img src="https://artificialanalysis.ai/img/logos//img/logos/inclusionai_small.jpg" width="18" alt="InclusionAI" /> InclusionAI | Ling-mini-2.0 | 0.1055 | 2025-09-09 | 0.3203 | ❌ |
| 527 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 2.6B | 0.1055 | 2025-09-23 | 0.3345 | ❌ |
| 528 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 8B (Non-reasoning) | 0.1046 | 2025-04-28 | 0.2097 | ❌ |
| 529 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo2-8B | 0.1013 | 2025-12-11 | 0.4263 | ❌ |
| 530 | <img src="https://artificialanalysis.ai/img/logos//img/logos/sarvam.svg" width="18" alt="Sarvam" /> Sarvam | Sarvam M | 0.1011 | 2025-05-23 | 0.2273 | ❌ |
| 531 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai21_small.svg" width="18" alt="AI21 Labs" /> AI21 Labs | Jamba 1.7 Mini | 0.0999 | 2025-07-07 | 0.2622 | ❌ |
| 532 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-1.2B-Thinking | 0.0985 | 2026-01-20 | 0.4813 | ❌ |
| 533 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-4 Mini | 0.0962 | 2024-02-26 | 0.0436 | ❌ |
| 534 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 12B | 0.0960 | 2025-03-12 | 0.1800 | ❌ |
| 535 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 70B Instruct | 0.0918 | 2025-09-02 | 0.3134 | ❌ |
| 536 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3.5 0.8B (Non-reasoning) | 0.0915 | 2026-03-02 | 0.5448 | ❌ |
| 537 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Olmo 3 7B | 0.0904 | 2025-11-20 | 0.3998 | ❌ |
| 538 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B | 0.0895 | 2025-07-15 | 0.2689 | ❌ |
| 539 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 32B | 0.0893 | 2025-03-13 | 0.1806 | ❌ |
| 540 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 1B | 0.0889 | 2025-10-28 | 0.3726 | ❌ |
| 541 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3.2 1B | 0.0878 | 2024-09-25 | 0.1014 | ❌ |
| 542 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B | 0.0867 | 2025-04-28 | 0.2097 | ❌ |
| 543 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.1 3B | 0.0851 | 2026-04-29 | 0.6483 | ❌ |
| 544 | <img src="https://artificialanalysis.ai/img/logos//img/logos/lg_small.png" width="18" alt="LG AI Research" /> LG AI Research | Exaone 4.0 1.2B (Non-reasoning) | 0.0827 | 2025-07-15 | 0.2689 | ❌ |
| 545 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 8B A1B | 0.0809 | 2025-10-07 | 0.3493 | ❌ |
| 546 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 Micro | 0.0783 | 2025-09-22 | 0.3334 | ❌ |
| 547 | <img src="https://artificialanalysis.ai/img/logos//img/logos/microsoft_small.svg" width="18" alt="Microsoft" /> Microsoft | Phi-3 Mini | 0.0735 | 2024-04-23 | 0.0558 | ❌ |
| 548 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 3.3 8B | 0.0702 | 2025-04-16 | 0.2018 | ❌ |
| 549 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2.5-VL-1.6B | 0.0676 | 2026-01-05 | 0.4599 | ❌ |
| 550 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 1B | 0.0670 | 2025-10-28 | 0.3726 | ❌ |
| 551 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 350M | 0.0659 | 2025-10-28 | 0.3726 | ❌ |
| 552 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 4B | 0.0651 | 2025-03-12 | 0.1800 | ❌ |
| 553 | <img src="https://artificialanalysis.ai/img/logos//img/logos/liquidai_small.svg" width="18" alt="Liquid AI" /> Liquid AI | LFM2 1.2B | 0.0641 | 2025-07-10 | 0.2647 | ❌ |
| 554 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B | 0.0635 | 2025-04-28 | 0.2097 | ❌ |
| 555 | <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | Llama 3 8B | 0.0633 | 2024-04-18 | 0.0547 | ❌ |
| 556 | <img src="https://artificialanalysis.ai/img/logos//img/logos/mistral_small.png" width="18" alt="Mistral" /> Mistral | Mistral 7B | 0.0609 | 2023-09-27 | 0.0192 | ❌ |
| 557 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E4B | 0.0573 | 2025-06-26 | 0.2532 | ❌ |
| 558 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ifm_small.svg" width="18" alt="Institute of Foundation Models" /> Institute of Foundation Models | K2 Horizon 0.9B | 0.0562 | 2026-09-03 | 0.9455 | ❌ |
| 559 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 1.7B (Non-reasoning) | 0.0555 | 2025-04-28 | 0.2097 | ❌ |
| 560 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | OLMo 2 7B | 0.0553 | 2024-11-26 | 0.1261 | ❌ |
| 561 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3 1B | 0.0550 | 2025-03-13 | 0.1806 | ❌ |
| 562 | <img src="https://artificialanalysis.ai/img/logos//img/logos/swiss-ai-initiative_small.png" width="18" alt="Swiss AI Initiative" /> Swiss AI Initiative | Apertus 8B Instruct | 0.0540 | 2025-09-02 | 0.3134 | ❌ |
| 563 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ibm_small.svg" width="18" alt="IBM" /> IBM | Granite 4.0 H 350M | 0.0499 | 2025-10-28 | 0.3726 | ❌ |
| 564 | <img src="https://artificialanalysis.ai/img/logos//img/logos/ai2_small.svg" width="18" alt="Allen Institute for AI" /> Allen Institute for AI | Molmo 7B-D | 0.0468 | 2024-09-25 | 0.1014 | ❌ |
| 565 | <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | Qwen3 0.6B (Non-reasoning) | 0.0429 | 2025-04-28 | 0.2097 | ❌ |
| 566 | <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | Gemma 3n E2B | 0.0354 | 2025-06-26 | 0.2532 | ❌ |
| 567 | <img src="https://artificialanalysis.ai/img/logos//img/logos/cohere_small.svg" width="18" alt="Cohere" /> Cohere | Tiny Aya Global | 0.0350 | 2026-02-17 | 0.5239 | ❌ |
| 568 | <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | DeepSeek R1 Distill Qwen 1.5B | 0.0000 | 2025-01-20 | 0.1520 | ❌ |

## 品牌帕累托前沿连线（仅体现在图中）

以下十一个品牌在图中拥有单独的帕累托连线（较窄宽度，品牌主题色，图层高于总体灰色连线）。表中数量为**入图顶点数**——品牌前沿上低于总体前沿第一级的顶点同样不入图（本表与图例一致）：

| 品牌 | 主题色 | 品牌前沿模型数（入图） |
|------|--------|--------------|
| <img src="https://artificialanalysis.ai/img/logos//img/logos/anthropic_small.svg" width="18" alt="Anthropic" /> Anthropic | `#cc785c` | 11 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/openai_small.svg" width="18" alt="OpenAI" /> OpenAI | `#1f1f1f` | 13 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/meta_small.svg" width="18" alt="Meta" /> Meta | `#0089f4` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/zai_small.svg" width="18" alt="Z AI" /> Z AI | `#1c7ff8` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/google_small.svg" width="18" alt="Google" /> Google | `#34A853` | 8 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/spacexai.svg" width="18" alt="SpaceXAI" /> SpaceXAI | `#736cd3` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/kimi.jpg" width="18" alt="Kimi" /> Kimi | `#047AFE` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/alibaba_small.svg" width="18" alt="Alibaba" /> Alibaba | `#ff7018` | 13 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/deepseek_small.svg" width="18" alt="DeepSeek" /> DeepSeek | `#2243e6` | 10 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/minimax_small.svg" width="18" alt="MiniMax" /> MiniMax | `#EB3568` | 6 |
| <img src="https://artificialanalysis.ai/img/logos//img/logos/xiaomi_small.svg" width="18" alt="Xiaomi" /> Xiaomi | `#ff6900` | 3 |

## 评分方法

1. **20项评估指标**各自线性归一化到 [0,1]
   （AA Intelligence Index、GPQA Diamond、Humanity's Last Exam、MMMU Pro、IFBench Instruction Following、SciCode Coding、CritPt Physics、AA-LCR Long Context、AA Omniscience Index、AA-Omniscience Accuracy、AA-Omniscience Non-Hallucination、GDPval-AA Normalized、AA Analyst Agent、APEX-Agents-AA、ITBench-SRE、τ²-Bench Telecom、τ³-Bench Banking、Terminal-Bench Hard、Terminal-Bench 2.1、Terminal-Bench 4.0）
   > V18（2026-09-12）：AA 更新了基准列——新增 AA Analyst Agent、τ³-Bench Banking、Terminal-Bench 2.1 / 4.0 四项；AA Agentic Index 与 AA Coding Index 已从 AA 的数据源中移除，相应剔除。指标数由 18 → 20。
2. **综合能力值** = 所有有效归一化分数的算术平均
3. **综合能力再归一化**：线性映射到 [0,1]，性能最好的模型 = 1，最差的模型 = 0
4. **Pareto前沿** = 不被任何其他模型支配的模型（综合能力 ≥ 且发布时间 ≤（更早），且至少一项严格更优）
5. **模型范围** = Status: All（含已弃用模型；缺少足够评估数据者不参与排名）
6. **图表纵轴基线（V17）**：图表的 y = 0 取总体帕累托前沿的第一级（最低能力；本例 y0 = 0.2371，即前沿左端点 GPT-4）；综合能力低于该级的模型不出现在图表中（表格不受影响）。图中纵坐标 chart_y = (能力 - y0)/(1 - y0)，因此前沿左端点恰好落在 (0, 0)、最优模型恰好为 y = 1。该过滤在横轴映射构建之前完成


## 横轴映射（指数）

横轴为发布时间指数映射：x = (a^(b*t)-1)/(a^b-1)；t 为发布时间按最早和最大映射到 [0,1]；a = 2.678，b = 3.763，用 11 品牌前沿定出；mse = 0.001561。

- **函数端点**：最早发布 → x = 0；前沿最大发布 → x = 1；
- 横轴时间标签：2024-01, 2025-01, 2026-01, 2026-09
- 中位数位置 0.572；左 165 个，右 251 个
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
**模型数**: 568（总体帕累托前沿 20 个；图表入图 416 个）  

## 图表说明（黑底）

（V17 起本说明置于文末，图表之后直接跟随模型表格。）

图表说明：**灰色实线** = 总体帕累托前沿；**彩色细线** = 十一个品牌的单独帕累托前沿（品牌主题色，图层高于总体连线；暗色品牌元素带窄白边；顶点按（横轴位置、能力升序）连接，同时点按能力从低到高连接）；品牌前沿模型圆点同样使用品牌颜色。模型名称/思考程度标注优先骑在连线之上（点的左/右两侧皆可，同一条线段可容纳两个标签——各贴各的点；文字与连线平行、中轴线重合，连线仅在文字两侧绘制）；骑线位被其他标签占据时自动「让位」——占用者挪到自己的另一个骑线位，双方都保持骑线；实在骑不上线时按四级优先依次退让（V16）：离点最近位置的上方/下方平行偏移 → 点的两条连线延长线上就近 → 两连线夹角扇区内就近。标签规则（V13/V15）：品牌前沿模型共享的前导块按「最长有效切点」剔除 —— 切点止于分界符，或止于字母且其后紧跟数字（如 Claude Opus 5 → Opus 5、GPT-5.6 Sol → 5.6 Sol、Kimi K2.6 → 2.6、Qwen3.8 Max → 3.8 Max、MiMo-V2.5 → 2.5、MiniMax-M2.1 → 2.1）；(non-reasoning) 简写为 (non)；同一模型在品牌连线上相邻出现 2 次以上时仅性能最低者保留全名、相邻较高者只标思考程度，不相邻的重复出现保留全名（每次重新计算）；标签位置与序列同向（V15）——品牌前沿上越靠右上的模型，其标签重心必须同时更靠右且更靠上（两分量都 >= 0，至少是 (0,0)，仅其一非负不算合格；初始放置违反时自动就近重摆，单标签无解（被前后邻居夹死）时按窗口级联重排整体挪动，均不产生新的重叠）。纵轴 y = 0 为总体帕累托前沿第一级（y0 = 0.2371，前沿左端点 GPT-4 即 (0,0)），能力低于该级的 152 个模型和发布时间大于品牌前沿最大值的模型不出现在图中；横轴为发布时间（线性）。
