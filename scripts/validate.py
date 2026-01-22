#!/usr/bin/env python3
"""
Validate contacts data for completeness and freshness.

Usage:
    python validate.py --all           # Check all countries
    python validate.py --incomplete    # Show only incomplete countries
    python validate.py --stale         # Show countries with old data (>12 months)
"""

import json
import argparse
from pathlib import Path
from datetime import datetime, timedelta


def load_contacts():
    """Load contacts.json"""
    data_dir = Path(__file__).parent.parent / "data"
    with open(data_dir / "contacts.json", "r") as f:
        return json.load(f)


def check_country(country_key: str, country: dict) -> dict:
    """
    Check a country for completeness.
    Returns dict with status and issues.
    """
    issues = []
    
    # Required fields
    if not country.get("name"):
        issues.append("Missing country name")
    
    if not country.get("region"):
        issues.append("Missing region")
    
    # Lead ministry
    ministry = country.get("lead_ministry", {})
    if not ministry:
        issues.append("Missing lead ministry")
    elif not ministry.get("name"):
        issues.append("Missing ministry name")
    elif not ministry.get("general_email"):
        issues.append("Missing ministry contact email")
    
    # Contacts
    contacts = country.get("contacts", [])
    if not contacts:
        issues.append("No contacts listed")
    else:
        has_minister = any(c.get("role_type") == "minister" for c in contacts)
        has_official = any(c.get("role_type") == "official" for c in contacts)
        
        if not has_minister and not has_official:
            issues.append("No minister or senior official contact")
        
        # Check for stale data
        for contact in contacts:
            verified = contact.get("verified_date")
            if verified:
                try:
                    verified_date = datetime.strptime(verified, "%Y-%m-%d")
                    if datetime.now() - verified_date > timedelta(days=365):
                        issues.append(f"Stale: {contact.get('name')} verified {verified}")
                except ValueError:
                    issues.append(f"Invalid date format for {contact.get('name')}")
    
    # Summit participation
    summits = country.get("summits", {})
    if not summits.get("bletchley_2023"):
        issues.append("Missing Bletchley 2023 status")
    if not summits.get("seoul_2024"):
        issues.append("Missing Seoul 2024 status")
    if not summits.get("paris_2025"):
        issues.append("Missing Paris 2025 status")
    
    # Determine status
    if not issues:
        status = "complete"
    elif len(issues) <= 2:
        status = "partial"
    else:
        status = "incomplete"
    
    return {
        "status": status,
        "issues": issues,
        "contact_count": len(contacts)
    }


def main():
    parser = argparse.ArgumentParser(description="Validate contacts data")
    parser.add_argument("--all", action="store_true", help="Show all countries")
    parser.add_argument("--incomplete", action="store_true", help="Show only incomplete")
    parser.add_argument("--stale", action="store_true", help="Show countries with stale data")
    parser.add_argument("--country", "-c", help="Check specific country")
    args = parser.parse_args()
    
    contacts = load_contacts()
    countries = contacts.get("countries", {})
    
    if args.country:
        if args.country in countries:
            result = check_country(args.country, countries[args.country])
            print(f"\n{args.country}: {result['status']}")
            for issue in result['issues']:
                print(f"  - {issue}")
        else:
            print(f"Country '{args.country}' not found")
        return
    
    # Summary stats
    complete = 0
    partial = 0
    incomplete = 0
    
    print("\n" + "=" * 60)
    print("VALIDATION REPORT")
    print("=" * 60)
    
    for country_key, country in sorted(countries.items()):
        result = check_country(country_key, country)
        
        if result['status'] == 'complete':
            complete += 1
            if args.all:
                print(f"✅ {country.get('name', country_key)}")
        elif result['status'] == 'partial':
            partial += 1
            if args.all or args.incomplete:
                print(f"🟡 {country.get('name', country_key)}")
                for issue in result['issues']:
                    print(f"   - {issue}")
        else:
            incomplete += 1
            if args.all or args.incomplete:
                print(f"❌ {country.get('name', country_key)}")
                for issue in result['issues']:
                    print(f"   - {issue}")
    
    print("\n" + "-" * 60)
    print(f"Complete:   {complete}")
    print(f"Partial:    {partial}")
    print(f"Incomplete: {incomplete}")
    print(f"Total:      {len(countries)}")
    print("-" * 60)


if __name__ == "__main__":
    main()
