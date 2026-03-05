# 002 — Supabase for database and storage

**Date:** 2026-03-05
**Status:** Accepted

## Context
Needed a database to store books and translations, and file storage for uploaded PDFs. Options considered: SQLite, PostgreSQL, MongoDB, Supabase.

## Decision
Use Supabase — a hosted PostgreSQL service that also provides file storage, auth, and real-time features.

## Reasoning
Developer chose Supabase. It bundles PostgreSQL + file storage + auth in one service with a generous free tier, reducing infrastructure setup. The client and admin SDKs (`@supabase/supabase-js`) are straightforward to use.
