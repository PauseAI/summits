# Research Methodology

## Overview

For each country, we aim to identify:
1. The ministry/department responsible for AI policy
2. Named contacts (ministers, secretaries, advisors)
3. Contact information (official emails, not personal)
4. Summit participation history
5. Whether they have a national AI Safety Institute

## Research Steps

### Step 1: Identify the Lead Ministry

Search patterns:
- `"[Country] Ministry of Technology AI policy"`
- `"[Country] Ministry of Digital Affairs"`
- `"[Country] Ministry of Economy digital strategy"`
- `"[Country] national AI strategy office"`

Common ministry names by region:
- **Europe**: Ministry of Digital Affairs, Ministry of Economy, Ministry of Science
- **Asia**: Ministry of Science and ICT (Korea), Ministry of Economy (Japan), MeitY (India)
- **Americas**: Varies widely - often split across multiple agencies
- **MENA**: Often Ministry of Communications or dedicated digital authority

### Step 2: Find Named Contacts

Priority order:
1. Minister/Secretary (political appointee)
2. Permanent Secretary/Deputy (senior civil servant)
3. Director of AI/Digital Policy
4. Head of AI Safety Institute (if exists)
5. GPAI national delegate (if findable)

Search patterns:
- `"[Country] [Ministry name] AI policy director"`
- `"[Country] AI Safety Summit 2024 delegation"`
- `"[Country] GPAI delegate representative"`

### Step 3: Verify Summit Participation

Check declaration signatory lists:
- Bletchley 2023: gov.uk declaration page
- Seoul 2024: Search for "Seoul AI Safety Summit declaration signatories"
- Paris 2025: Search for "Paris AI Action Summit statement signatories"

Record:
- `signed` - Signed the declaration
- `attended` - Attended but didn't sign
- `declined` - Explicitly declined
- `absent` - Did not participate
- `unknown` - Can't determine

### Step 4: Check for AI Safety Institute

Search: `"[Country] AI Safety Institute" OR "[Country] national AI safety"`

Known institutes (as of Jan 2026):
- UK: AI Safety Institute (AISI)
- US: US AI Safety Institute (USAISI) - under NIST, status uncertain post-Trump
- Japan: AI Safety Institute Japan
- Canada: Canadian AI Safety Institute (announced 2024)
- France: Part of INRIA
- Singapore: AI Safety workstream under IMDA

### Step 5: Find Contact Information

Priority sources (in order):
1. Official government website contact pages
2. Ministry press office contacts
3. Published consultation response addresses
4. OECD/GPAI listed contacts

**Do not use:**
- Personal email addresses
- LinkedIn scraped data
- Unofficial sources

### Step 6: Document Sources

Every piece of information needs:
- Source URL
- Date accessed
- Confidence level (high/medium/low)

## Country File Template

Use `data/countries/_template.md` - copy and fill in for each country.

## Quality Checklist

Before marking a country as "complete":
- [ ] Lead ministry identified with source
- [ ] At least one named contact with title
- [ ] Official contact email (even if generic ministry address)
- [ ] Summit participation for all three summits checked
- [ ] AI Safety Institute status confirmed
- [ ] All sources documented with dates
- [ ] Information less than 12 months old

## Handling Edge Cases

### No findable contacts
Record what you searched, mark as "needs_escalation" in PROGRESS.md. Some countries genuinely don't have dedicated AI policy structures.

### Multiple relevant ministries
List primary ministry first, note others in the country file. Common for larger countries to split AI across tech, economy, and security ministries.

### Recent government changes
Note the date of last election/transition. Political appointees change; permanent secretaries usually don't.

### Non-GPAI countries with AI activity
Include if they participated in summits (e.g., China, UAE at Bletchley). Use same methodology.

## Automation Opportunities

Some data can be partially automated:
- OECD AI dashboard has structured policy data
- GPAI member list is stable and published
- Summit signatory lists are in structured documents

Scripts in `/scripts` handle these where possible. Manual research fills gaps.
