# AI Summit Government Contacts Project - Briefing Document

## Project Owner
Anthony Bailey, Software Lead, PauseAI (volunteer position)

## Purpose
Build a comprehensive database of government contacts responsible for AI policy/governance across nations participating in international AI summits (Bletchley → Seoul → Paris → India 2026).

This resource supports PauseAI's advocacy goal: engaging government delegations to advance international AI safety coordination, including treaty-based approaches to managing risks from advanced AI systems.

## Why This Doesn't Already Exist
- Established orgs (CLTR, FLI, GovAI) guard their contact lists as proprietary access
- No infrastructure for coordination in the AI x-risk advocacy space
- Asked on AI Safety Comms Discord in December 2024 - "deafening silence"
- Each org works bilaterally with 1-2 governments, not multilaterally

## Key Data Sources

### Multilateral frameworks
- **GPAI**: 44 member countries, Secretariat at gpai@oecd.org
  - Full member list: https://oecd.ai/en/about/about-gpai
  - National AI policies dashboard: https://oecd.ai/en/dashboards/overview
- **OECD**: 38 members (significant overlap with GPAI)
- **AI Safety Summits**: Bletchley (28+EU), Seoul, Paris, India 2026

### Summit-specific
- **India AI Impact Summit**: February 19-20, 2026, New Delhi
  - Main site: impact.indiaai.gov.in (often inaccessible)
  - Key working group: "Safe and Trusted AI"
  - Indian organizers: S. Krishnan (IT Secretary), Shreeppriya Gopalakrishnan (IndiaAI)

### Per-country research pattern
For each nation, identify:
1. Ministry responsible for AI policy (usually Digital/Technology/Economy/Science)
2. National AI strategy office (if exists)
3. Named individuals: Minister, Deputy/Secretary, AI Advisor
4. Contact email (ministry general contact if no direct)
5. Summit participation history (Bletchley/Seoul/Paris/signed declarations?)
6. AI Safety Institute (if established)

## Spreadsheet Structure

### Sheet 1: Nations - AI Summits
| Column | Description |
|--------|-------------|
| Nation | Country name |
| Region | Geographic region |
| Bletchley 2023 | Y/N/P (signed/no/participated) |
| Seoul 2024 | Y/N/P |
| Paris 2025 | Y/N/P |
| AISI Network | Has national AI Safety Institute? |
| GPAI Member | Y/N |
| OECD Member | Y/N |
| Notes | Key context |

### Sheet 2: Contacts
| Column | Description |
|--------|-------------|
| Nation | Country name |
| Role | Minister/Secretary/Advisor/Delegate |
| Name | Full name |
| Title | Official title |
| Organization | Ministry/Agency |
| Email | Contact email |
| Source | URL where found |
| Date Verified | When last checked |
| Notes | Context |

### Sheet 3: Pre-Summit Events
Tracking side events, ministerial meetings, working groups

### Sheet 4: Strategy Notes
Campaign planning, messaging approaches, coalition opportunities

## Priority Countries

### Tier 1 - Major AI powers
- USA, China, UK, EU (as bloc), Japan, South Korea, India

### Tier 2 - Active in governance
- Canada, France, Germany, Singapore, Australia, Netherlands

### Tier 3 - Potential swing votes
- Brazil, UAE, Saudi Arabia, Indonesia, South Africa, Nigeria

### Tier 4 - Complete coverage
- All remaining GPAI/OECD members

## Research Methodology

### For each country:
1. Search "[Country] Ministry of [Technology/Digital/Economy] AI policy"
2. Search "[Country] national AI strategy office contact"
3. Check OECD AI dashboard for listed strategies/contacts
4. Search "[Country] AI Safety Summit delegation 2024"
5. Search for named individuals from summit press coverage
6. Record sources and dates for all information

### Validation
- Prefer government .gov domains
- Cross-reference names against LinkedIn/official bios
- Note when information is stale (>12 months)
- Flag countries with no findable contacts

## What Has Been Done (as of January 11, 2026)

### Completed
- Framework design for spreadsheet
- Initial population with ~44 GPAI member countries
- Verification that gpai@oecd.org is correct Secretariat contact
- Draft email to GPAI Secretariat requesting focal point guidance
- Research into why no shared database exists in advocacy space

### In Progress
- Systematic country-by-country contact research
- Building out Bletchley/Seoul/Paris signatory tracking

### Not Started
- Actual outreach to GPAI Secretariat
- Per-country markdown research notes
- Automation scripts for OECD dashboard
- EA Forum / public solicitation for collaborators

## Instructions for Future Chat Sessions

### If continuing spreadsheet research:
1. Pick a country or region not yet completed
2. Follow research methodology above
3. Add findings to spreadsheet
4. Note sources and dates
5. Update PROGRESS tracking

### If setting up Claude Code repo:
1. Create repo structure as specified above
2. Initialize with existing spreadsheet
3. Create country_template.md for research notes
4. Build PROGRESS.md checklist from GPAI member list
5. Consider scripts for OECD dashboard scraping

### If doing outreach:
1. Send email to gpai@oecd.org (draft exists)
2. Post resource request to EA Forum / AI Safety spaces
3. Frame as: "I've started this, who wants to help?"

## Key Context for Claude

- User is deeply familiar with AI x-risk space, PauseAI operations
- Prefers direct communication, no hedging
- Working on this voluntarily alongside wedding planning (May 2026)
- Located in Edinburgh, fiancée Julie in Wales
- Has 17 years Amazon experience - understands systems/data
- Frustrated by fragmentation in AI safety advocacy coordination

## Files Location

- Spreadsheet: Should be in /mnt/user-data/outputs/ after creation
- This briefing: To be saved for reference
- Any Claude Code repo: Suggest GitHub under PauseAI org

## Questions to Resolve

1. Should this be a PauseAI-branded resource or broader coalition?
2. Who else might contribute? (FLI UK Policy Advocate? CLTR contacts?)
3. What's the minimum viable version for India Summit engagement?
4. How to handle countries with no public contact info?
