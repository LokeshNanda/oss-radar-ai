# Product Requirements

## Functional Requirements

- Fetch top 10 repositories created in last 7 days.
- Sort by stars descending.
- Avoid reprocessing repositories.
- Generate structured markdown analysis.
- Update homepage automatically.
- Deploy weekly via GitHub Actions.

## LLM Output Must Include

- Executive Summary (3 lines)
- Problem it solves
- Target audience
- Why it is trending
- Architecture insights
- Enterprise relevance
- Suggested experiments

Tone:
Senior architect. Analytical. No hype.

---

## Non-Functional Requirements

- Use environment variables for secrets
- Modular code
- Clean logging
- Error handling
- Deterministic output
- Cost control
