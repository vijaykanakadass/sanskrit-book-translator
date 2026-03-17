# Decisions

**Date:** 2026-03-17

## Decision 1: Test Framework Choice

**Context:** No tests existed in the project. Needed a test framework for Python/FastAPI.

**Decision:** Use pytest + httpx + pytest-asyncio.

**Alternatives considered:**
- `unittest` — built-in but more verbose, less popular for FastAPI projects
- `ward` — modern but less ecosystem support

**Reason:** pytest is the de facto standard for Python testing. httpx provides async test client for FastAPI. pytest-asyncio enables async test functions.

## Decision 2: PDF Generation for Tests

**Context:** Need valid PDFs of various sizes for testing.

**Decision:** Use `reportlab` to generate PDFs programmatically in fixtures.

**Alternatives considered:**
- Include static PDF files in the repo — inflexible, hard to parameterize sizes
- Use `fpdf2` — less mature than reportlab

**Reason:** reportlab is battle-tested, allows generating PDFs of any size/content dynamically.

## Decision 3: Bug-Detection Test Pattern

**Context:** Need tests that confirm bugs exist (TDD: red tests first).

**Decision:** Write tests that assert the *absence* of safeguards (e.g., "no timeout keyword found in source"). These tests PASS now (confirming the bugs exist) and will FAIL once the bugs are fixed — which is the correct TDD signal.

**Reason:** This pattern lets us run the full suite green today, while clearly documenting every issue. When fixes are applied, these specific tests will flip to failures, indicating the fix was applied and the test assertion needs to be updated to validate the new behavior.
