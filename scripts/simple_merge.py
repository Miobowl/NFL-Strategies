#!/usr/bin/env python3
"""
Simple merge: Read both JS files and combine tactics arrays
"""

import re
import json

# Read existing data.js
with open('../assets/js/data.js', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Read csv_tactics.js
with open('../assets/js/csv_tactics.js', 'r', encoding='utf-8') as f:
    csv_content = f.read()

# Extract existing tactics IDs that have Chinese names
existing_ids = set(re.findall(r"id:\s*'([^']+)'", data_content))

print(f"Found {len(existing_ids)} existing tactics with Chinese translations")
print("Existing IDs:", sorted(existing_ids))

# Extract all CSV tactics
csv_tactics_match = re.search(r'const csvTactics = \[(.*)\];', csv_content, re.DOTALL)
if csv_tactics_match:
    csv_tactics_str = csv_tactics_match.group(1)
    # Split by tactic objects
    csv_ids = set(re.findall(r"id:\s*'([^']+)'", csv_tactics_str))
    print(f"\nFound {len(csv_ids)} CSV tactics")

    # Find new tactics
    new_ids = csv_ids - existing_ids
    print(f"\nNew tactics to add: {len(new_ids)}")
    print("New IDs:", sorted(new_ids))

    # Print category distribution of new tactics
    from collections import Counter
    categories = re.findall(r"category:\s*'([^']+)'", csv_tactics_str)
    cat_counter = Counter(categories)
    print("\nNew tactics by category:")
    for cat, count in sorted(cat_counter.items()):
        print(f"  {cat}: {count}")
