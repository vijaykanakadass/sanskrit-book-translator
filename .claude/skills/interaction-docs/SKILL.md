---
name: interaction-docs
description: >
  Use this skill for EVERY task — before writing any code, create an interaction folder
  in docs/interactions/ and record the request, plan, decisions, changes, and outcome.
  This ensures full traceability so the codebase can be recreated from docs alone.
user-invocable: false
---

# Interaction Documentation Workflow

**Guiding principle:** The `docs/` folder is the single source of truth. Every interaction — from request through outcome — must be recorded in enough detail that the entire codebase could be re-created from `docs/` alone, by a developer (or AI) who has never seen the code. When in doubt, include more detail, not less. Never condense or summarize — the user can always summarize later with LLMs.

## Interaction Folder Structure

Every task is recorded as a numbered interaction in `docs/interactions/NNN-short-description/`. Each interaction folder contains up to six files:

| File | Purpose | Required? |
|------|---------|-----------|
| `request.md` | What the user asked for | Always |
| `plan.md` | The approach designed before implementation | For non-trivial tasks |
| `decisions.md` | Choices made during this interaction (with full context, alternatives, trade-offs) | When choices were made |
| `changes.md` | Files created, modified, or deleted, and why | Always |
| `outcome.md` | What was actually built, verification results | Always |
| `paper-trail.md` | Summary table: which files exist in this folder and a one-line summary of each | Always (written last) |

## Rules

1. **Interaction folder** — Create `docs/interactions/NNN-description/` for every task. Number sequentially based on the last folder. Even small config changes get an interaction folder.
2. **Request** — Record what the user asked for in `request.md` before starting work.
3. **Blueprint** — Plan before coding. For non-trivial tasks, write the full plan to `plan.md` and get user approval before implementing.
4. **Plan detail** — Plans must include: context (why), approach (step by step), files to modify/create, and verification steps. Keep full detail — architecture decisions, API shapes, component structure, data flow. Do not condense.
5. **Green Light** — Get approval before implementing. Present the plan and wait for user confirmation.
6. **Decisions** — Record every choice in `decisions.md` within the interaction folder. Include: date, status, context, decision, alternatives considered with reasons for rejection, and consequences. Keep full detail.
7. **Changes** — Record all file changes in `changes.md` — what was created, modified, or deleted, and why.
8. **Outcome** — After implementation, write `outcome.md` noting what was actually built and verification results.
9. **Paper Trail** — At the end of every task, write `paper-trail.md` inside the interaction folder with a summary table listing each file and a one-line description. Also report to the user which interaction folder was created or updated.

## SDK and API Integration Documentation

When a plan involves integrating a third-party SDK or external API, the plan and/or decisions docs **must** record the exact API contract. LLMs cannot reliably guess uncommon SDK interfaces — they will default to common patterns (e.g., stateless ID-based APIs) which may be wrong.

Record the following for every SDK integration:

### Method signatures
Show the exact call pattern, not just a description of what happens:
```
# GOOD — exact signatures, recreating LLM can copy this
job = client.document_intelligence.create_job(language="sa-IN", output_format="html")
job.upload_file(tmp_path)
job.start()
status = job.get_status()
job.download_output(zip_path)

# BAD — describes what happens but not how
# "Create a job, upload the file, start it, poll for status, download output"
```

### Return types and attribute names
Document what objects are returned and what attributes/methods they have:
```
# get_status() returns object with .job_state (NOT .status)
# .job_state values: "Completed", "PartiallyCompleted", "Failed" (capitalized)
# download_output(path) writes ZIP to file path, does NOT return bytes
```

### API pattern
State explicitly whether the SDK uses:
- **Stateful object pattern:** `job = create(); job.method()` — methods on the returned object
- **Stateless ID pattern:** `id = create(); client.method(id=id)` — pass ID back to client methods
- **Builder pattern:** `client.thing().with_x().with_y().execute()`

### Package version
Pin the SDK version so the recreating agent installs the same version:
```
sarvamai==0.3.1
```

### Configuration
Document env vars, auth patterns, and initialization:
```
client = SarvamAI(api_subscription_key=settings.SARVAM_API_KEY)
# Env var: SARVAM_API_KEY
```
