# 008 — Reference projects identified for pattern reuse

**Date:** 2026-03-05
**Status:** Accepted

## Context
Needed proven patterns for translation, PDF processing, and bilingual presentation rather than building everything from scratch.

## Decision
Two external reference projects (read-only, not to be modified) will be used as pattern sources:

### 1. `D:\AI_ML\VideoTranslation_Sarvam\`
- **Reuse:** Sarvam AI SDK integration, text translation with chunking, rate limiting, LLM quality correction
- **Key files:** `translate_text.py`, `correct_srt.py`, `sanskrit_learn_module.html`

### 2. `D:\WebApps\DocumentTranslation\`
- **Reuse:** Exponential backoff (4s→8s→16s→32s), parallel chunk processing, state persistence/resume, PDF splitting, structural parsing (act/section/prologue detection), language classification (Devanagari ratio), bilingual React reader
- **Key files:** `digitize.py`, `extract_bilingual.py`, `split_pdf.py`, `ReactProject/`

## Reasoning
These projects were built by the same developer, use the same Sarvam AI platform, and solve adjacent problems (video translation, manuscript digitization). Reusing their patterns avoids reinventing retry logic, chunking, structural parsing, and bilingual presentation.
