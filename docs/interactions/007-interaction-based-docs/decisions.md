# Decisions

## Interaction-based documentation structure

**Date:** 2026-03-05
**Status:** Accepted

### Context
The project had three independent doc folders (`plans/`, `decisions/`, `changelog/`) each with their own numbering sequences. `plans/005`, `decisions/009`, and `changelog/001` gave no indication of chronological order or relationships. An AI or developer trying to re-create the project from docs alone couldn't determine what happened when, or which plan triggered which decisions.

The user observed that every Claude interaction naturally follows the same pattern: request → plan → decisions → implementation → outcome. This is the natural unit of documentation.

### Options considered

#### 1. Master timeline file (`docs/TIMELINE.md`)
- A chronological index with global sequence numbers (G001, G002...) linking to entries across all three folders
- Cross-references (`## Related` sections) in each entry
- **Rejected because:** adds a fourth thing to maintain, creates a layer on top rather than fixing the underlying structure, still requires jumping between folders to understand one task

#### 2. Keep separate folders + add cross-references
- Add `## Related` sections to each entry linking to related entries in other folders
- **Rejected because:** doesn't solve the ordering problem, relationships are many-to-many and messy, requires discipline to maintain bidirectional links

#### 3. Interaction-based structure (chosen)
- Replace all three folders with `docs/interactions/NNN-description/`
- Each folder contains: `request.md`, `plan.md`, `decisions.md`, `changes.md`, `outcome.md`
- **Chosen because:** matches the natural flow of work, everything related to one task is co-located, reading folders in order gives the full chronological story, no cross-referencing needed

### Decision
Replace `docs/plans/`, `docs/decisions/`, and `docs/changelog/` with a single `docs/interactions/` structure. Each interaction is a numbered folder containing separate files for request, plan, decisions, changes, and outcome.

### Naming
User specifically chose "interaction" over "session" — a session implies a long-running context with multiple interactions, while an interaction is a single task from request to outcome.

### Consequences
- Natural chronological ordering — folder 001 through NNN tells the story in order
- Everything related to one task is co-located — no jumping between folders
- Not every interaction needs all five files — small tasks can skip plan.md or decisions.md
- The structure is self-documenting — reading the folder names gives a high-level project history
- Migrating existing content requires consolidating 16 entries into 6 interaction folders
