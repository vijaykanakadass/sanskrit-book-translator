# Request: Create Testing Guide PDF Using Actual Repo Tests

**Date:** 2026-03-17

## What the user asked for

Create a comprehensive PDF guide titled "Testing Python Modules" that teaches testing concepts by walking through the actual test code written for the Sanskrit Book Translator project. The guide follows a 10-chapter structure:

1. **Chapter 1: Meet the Project** — Overview of the Sanskrit Book Translator (FastAPI backend, PDF upload, Sarvam API digitization, in-memory job store). Shows folder structure and files under test.
2. **Chapter 2: Test Infrastructure** — Walks through pytest.ini and conftest.py, explaining each fixture.
3. **Chapter 3: Unit Testing Pure Functions** — Uses TestCreateJob, TestGetJob, TestUpdateJob from test_digitize_service.py.
4. **Chapter 4: Testing Thread Safety** — Uses TestJobStoreThreadSafety to explain concurrent testing.
5. **Chapter 5: Parametrize-Style Data Tests** — Uses TestAdaptivePollInterval for data-driven testing patterns.
6. **Chapter 6: Async Integration Tests** — Uses TestUploadValidation and TestSuccessfulUpload from test_upload.py.
7. **Chapter 7: Mocking External APIs** — Uses @patch and Sarvam mock chains from test_large_pdf_digitization.py.
8. **Chapter 8: Bug-Hunting Tests** — Uses BUG #1-#7 test classes showing how tests document known issues.
9. **Chapter 9: End-to-End Flow Tests** — Uses TestDigitizationFlow for full happy-path testing.
10. **Chapter 10: Custom Markers & Running Subsets** — Uses @pytest.mark.large_pdf and @pytest.mark.slow.

Each chapter shows actual source code alongside actual test code with callout explanations.

The test files already exist in the `claude/test-pdf-digitization-9BUSB` branch.
