# Sources

Raw source materials used to populate `contacts.json`. Kept for provenance tracking and future verification.

## Directory Structure

```
sources/
├── {country}/
│   └── {source_description}_{date}.{ext}
```

## Naming Convention

- `pauseai_au_2025-12-21.txt` — PauseAI Australia research, dated
- `dfat_org_chart_2026-01.pdf` — Official document snapshot
- `oecd_gpai_members_2026-01.json` — API/data export

## Source Quality Notes

Sources vary in reliability:
- **Official government sites**: High confidence, verify currency
- **LLM-generated research**: Treat as leads requiring verification (e.g., ChatGPT predictions)
- **News articles**: Date-sensitive, roles may have changed
- **Personal communications**: Note date and context

Always cross-reference against official sources before adding to `contacts.json`.
