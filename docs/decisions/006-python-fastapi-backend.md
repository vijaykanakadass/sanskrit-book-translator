# 006 — Python + FastAPI for backend (replacing Express)

**Date:** 2026-03-05
**Status:** Accepted
**Supersedes:** [001-react-vite-express-stack.md](001-react-vite-express-stack.md) (backend portion)

## Context
The app needs to parse Sanskrit book PDFs, potentially do OCR on scanned pages, and interface with AI translation services. Python has a significantly stronger ecosystem for all of these: `pdfplumber`/`PyMuPDF` for PDF handling, `pytesseract`/`EasyOCR` for OCR, and `indic-nlp-library` for Indic language processing.

## Decision
Replace the Express (JavaScript) backend with FastAPI (Python). The React + Vite frontend remains unchanged. The frontend proxies `/api` requests to the FastAPI server on port 3001.

## Reasoning
- Python PDF libraries (`pdfplumber`, `PyMuPDF`) are more capable than JS alternatives (`pdf-parse`)
- OCR tools are Python-native (`pytesseract`, `EasyOCR`)
- Sanskrit/Indic NLP tools are Python-only
- AI SDKs (Claude, OpenAI) have first-class Python support
- FastAPI is modern, fast, and structurally similar to Express — easy to learn
- Developer knows both Python and JS
