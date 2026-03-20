# Request: Generate Repo-Specific Python Testing Guide PDF

## Date
2026-03-17

## What the user asked for
Generate a new PDF guide that teaches Python testing concepts using the actual test code written for the Sanskrit Book Translator repository. The PDF should have 10 chapters, each introducing a testing concept through the repo's real source and test code.

## Structure requested
1. Chapter 1: Meet the Project — overview of the app architecture, folder structure, files under test
2. Chapter 2: Test Infrastructure — pytest.ini config and conftest.py fixtures explained
3. Chapter 3: Unit Testing Pure Functions — TestCreateJob, TestGetJob, TestUpdateJob with source code
4. Chapter 4: Testing Thread Safety — TestJobStoreThreadSafety with concurrent threading
5. Chapter 5: Parametrize-Style Data Tests — TestAdaptivePollInterval boundary value tests
6. Chapter 6: Async Integration Tests — TestUploadValidation, TestSuccessfulUpload with httpx.AsyncClient
7. Chapter 7: Mocking External APIs — @patch, MagicMock, side_effect from test_large_pdf_digitization.py
8. Chapter 8: Bug-Hunting Tests — BUG #1-#7 test classes documenting known issues
9. Chapter 9: End-to-End Flow Tests — TestDigitizationFlow happy-path with multiple mocks
10. Chapter 10: Custom Markers & Running Subsets — @pytest.mark.large_pdf, @pytest.mark.slow

Each chapter should show the actual source code alongside test code with callout explanations.
