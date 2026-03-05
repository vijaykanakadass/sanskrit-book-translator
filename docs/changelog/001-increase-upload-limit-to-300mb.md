# 001 — Increase Upload Limit to 300MB

**Date:** 2026-03-05

## What changed
Client-side PDF upload size limit increased from 50MB to 300MB.

## Why
Sanskrit book PDFs — especially scanned manuscripts — can be very large. 50MB was too restrictive. The Sarvam Document Intelligence API docs don't specify a file size limit, so we raised the client-side guard to 300MB to accommodate large books.

## Files affected
- `client/src/components/PdfUploader.jsx` — changed `MAX_SIZE_MB` from `50` to `300`
