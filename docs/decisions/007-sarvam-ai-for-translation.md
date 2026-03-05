# 007 — Sarvam AI for translation service

**Date:** 2026-03-05
**Status:** Accepted

## Context
Needed to choose a translation service for Sanskrit-to-English translation. The developer has an existing Sarvam AI integration from a prior video translation project (D:\AI_ML\VideoTranslation_Sarvam) with working scripts.

## Decision
Use Sarvam AI as the translation service:
- **Text translation:** `mayura:v1` model via `client.text.translate()`
- **LLM refinement:** `sarvam-m` model via `client.chat.completions()` for quality correction
- **Python SDK:** `sarvamai` package
- **Source language:** `sa-IN` (Sanskrit), **Target:** `en-IN` (English)

## Reasoning
- Developer already has a working Sarvam AI subscription and API key
- Proven scripts exist for Sanskrit text translation with chunking and rate limiting
- Sarvam supports Sanskrit (`sa-IN`) as a source language natively
- The `mayura:v1` model handles formal/colloquial translation modes
- LLM-based quality correction (formal → colloquial refinement) is already proven in the reference scripts

## Reference scripts (read-only, not to be modified)
- `D:\AI_ML\VideoTranslation_Sarvam\translate_text.py` — plain text translation with chunking
- `D:\AI_ML\VideoTranslation_Sarvam\correct_srt.py` — LLM-based quality correction
- `D:\AI_ML\VideoTranslation_Sarvam\sanskrit_learn_module.html` — interactive web view template
