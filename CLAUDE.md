# CLAUDE.md - Project Context for Claude Code

## Project: AI Summit Government Contacts Database

### Owner
Anthony Bailey, Software Lead, PauseAI (volunteer)
- Based in Edinburgh, Scotland
- 17 years Amazon SDE experience (recommendations, ads safety)
- Left Amazon 2024 to work on AI safety advocacy full-time
- Engaged to Julie, wedding May 23, 2026

### Purpose
Build comprehensive database of government contacts responsible for AI policy across nations participating in international AI summits. Supports PauseAI's advocacy for international AI safety coordination and treaty-based risk management.

### Why This Matters
- No shared contact database exists in AI x-risk advocacy space
- Established orgs (CLTR, FLI, GovAI) guard contacts as proprietary
- PauseAI needs this for India AI Impact Summit engagement (Feb 19-20, 2026)
- Building it ourselves, then soliciting collaborators

### Key Data Sources
- GPAI: 44 members, Secretariat at gpai@oecd.org, dashboard at oecd.ai/en/dashboards/overview
- AI Safety Summits: Bletchley 2023, Seoul 2024, Paris 2025, India 2026
- Per-country ministry websites, national AI strategy documents

### Tech Stack
- Python 3.x for scripts
- openpyxl for spreadsheet generation
- requests/BeautifulSoup for scraping (where appropriate)
- JSON for intermediate data storage
- Git for version control

### Repository Structure
```
PauseAI/summits/
├── CLAUDE.md              # This file - read first
├── README.md              # Public-facing project description
├── METHODOLOGY.md         # How to research each country
├── PROGRESS.md            # Checklist of countries done/pending
├── data/
│   ├── contacts.json      # Canonical contact data
│   ├── contacts.xlsx      # Generated spreadsheet (from JSON)
│   ├── summits.json       # Summit participation tracking
│   └── countries/         # Per-country research notes
│       ├── _template.md
│       ├── australia.md
│       └── ...
├── scripts/
│   ├── generate_xlsx.py   # JSON → spreadsheet
│   ├── validate.py        # Check for completeness/staleness
│   └── oecd_fetch.py      # Pull from OECD dashboard
└── outreach/
    ├── gpai_email_draft.md
    └── ea_forum_post_draft.md
```

### Working With This Repo

#### Adding a new country
1. Copy `data/countries/_template.md` to `data/countries/{country}.md`
2. Follow research methodology in METHODOLOGY.md
3. Add findings to `data/contacts.json`
4. Update PROGRESS.md checklist
5. Run `python scripts/validate.py` to check completeness

#### Regenerating spreadsheet
```bash
python scripts/generate_xlsx.py
```

#### Research priority
1. Tier 1 (major AI powers): USA, China, UK, EU, Japan, South Korea, India
2. Tier 2 (governance-active): Canada, France, Germany, Singapore, Australia, Netherlands
3. Tier 3 (potential swing): Brazil, UAE, Saudi Arabia, Indonesia, South Africa
4. Tier 4: All remaining GPAI/OECD members

### Data Schema

#### contacts.json
```json
{
  "countries": {
    "united_kingdom": {
      "name": "United Kingdom",
      "region": "Europe",
      "gpai_member": true,
      "oecd_member": true,
      "summits": {
        "bletchley_2023": "signed",
        "seoul_2024": "signed",
        "paris_2025": "declined"
      },
      "ai_safety_institute": true,
      "contacts": [
        {
          "name": "Peter Kyle",
          "title": "Secretary of State for Science, Innovation and Technology",
          "organization": "DSIT",
          "email": "enquiries@dsit.gov.uk",
          "role_type": "minister",
          "source_url": "https://www.gov.uk/...",
          "verified_date": "2026-01-11",
          "notes": "Cabinet-level, leads AI policy"
        }
      ]
    }
  }
}
```

#### summits.json
```json
{
  "bletchley_2023": {
    "name": "AI Safety Summit 2023",
    "location": "Bletchley Park, UK",
    "dates": "2023-11-01/02",
    "declaration": "Bletchley Declaration",
    "signatories": ["australia", "brazil", ...],
    "non_signatories_attended": []
  }
}
```

### Important Context

#### UK-specific (since Anthony is UK-based)
- DSIT = Department for Science, Innovation and Technology (main AI policy dept)
- AI Policy Directorate within DSIT (absorbed Office for AI)
- UK AISI = AI Safety Institute (under DSIT)
- General contact: enquiries@dsit.gov.uk
- AI-specific: ai@digital.cabinet-office.gov.uk

#### India Summit 2026
- Feb 19-20, 2026, New Delhi
- Framing shifted from "safety" to "impact"
- Key working group: "Safe and Trusted AI"
- Indian contacts: S. Krishnan (IT Secretary), Shreeppriya Gopalakrishnan (IndiaAI)
- UK/US declined to sign Paris declaration - context for engagement

#### What NOT to do
- Don't scrape personal emails from LinkedIn
- Don't spam contacts - this is for targeted, professional outreach
- Don't store sensitive personal data beyond professional roles
- Don't access YouTube URLs (always fail in this environment)

### Commands for Common Tasks

```bash
# Validate all country files
python scripts/validate.py --all

# Check which countries are incomplete
python scripts/validate.py --incomplete

# Generate fresh spreadsheet
python scripts/generate_xlsx.py --output data/contacts.xlsx

# Fetch latest from OECD (if implemented)
python scripts/oecd_fetch.py --update
```

### Questions to Resolve (track decisions here)
- [ ] PauseAI-branded or broader coalition resource?
- [ ] Public repo or private until populated?
- [ ] License for data sharing?
- [ ] Minimum viable version for India Summit?
