# Request

The three independent doc folders (plans, decisions, changelog) have separate numbering that doesn't let an AI retrace the chronological flow. Every interaction with Claude involves a request, plan, decisions, and implementation — can that be captured as the natural unit of documentation?

User decided: replace all three folders with a single `docs/interactions/` structure where each numbered folder contains separate files for request, plan, decisions, changes, and outcome.
