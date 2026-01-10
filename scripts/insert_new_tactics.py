#!/usr/bin/env python3
"""
Insert only NEW tactics from csv_tactics.js into data.js
"""

import re

# Read existing data.js
with open('../assets/js/data.js', 'r', encoding='utf-8') as f:
    data_content = f.read()

# Read csv_tactics.js
with open('../assets/js/csv_tactics.js', 'r', encoding='utf-8') as f:
    csv_content = f.read()

# Extract existing tactics IDs
existing_ids = set(re.findall(r"id:\s*'([^']+)',", data_content))
print(f"Existing tactics: {len(existing_ids)}")

# Extract CSV tactics
csv_tactics_match = re.search(r'const csvTactics = \[(.*)\];', csv_content, re.DOTALL)
csv_tactics_str = csv_tactics_match.group(1).strip()

# Split into individual tactic objects
tactics = []
current_tactic = []
brace_count = 0
in_tactic = False

for line in csv_tactics_str.split('\n'):
    stripped = line.strip()

    if stripped == '{':
        in_tactic = True
        brace_count = 1
        current_tactic = [line]
    elif in_tactic:
        current_tactic.append(line)
        if stripped.startswith('{'):
            brace_count += 1
        elif stripped == '},':
            brace_count -= 1
            if brace_count == 0:
                tactics.append('\n'.join(current_tactic))
                current_tactic = []
                in_tactic = False

print(f"CSV tactics parsed: {len(tactics)}")

# Filter for only NEW tactics
new_tactics = []
for tactic_str in tactics:
    # Extract ID from this tactic
    id_match = re.search(r"id:\s*'([^']+)'", tactic_str)
    if id_match:
        tactic_id = id_match.group(1)
        if tactic_id not in existing_ids:
            new_tactics.append(tactic_str)

print(f"New tactics to add: {len(new_tactics)}")

# Group new tactics by category
categories = {
    'defense-coverage': [],
    'defense-formation': [],
    'offense-formation': [],
    'passing-concepts': [],
    'passing-routes': []
}

for tactic_str in new_tactics:
    cat_match = re.search(r"category:\s*'([^']+)'", tactic_str)
    if cat_match:
        category = cat_match.group(1)
        if category in categories:
            categories[category].append(tactic_str)

# Prepare the new tactics section to insert
new_tactics_section = "\n    // ========== 以下为CSV新增战术 (需添加中文翻译) ==========\n\n"

category_names = {
    'defense-coverage': '新增防守覆盖 (Additional Coverage)',
    'defense-formation': '新增防守阵型 (Additional Defensive Formations)',
    'offense-formation': '新增进攻阵型 (Additional Offensive Formations)',
    'passing-concepts': '传球概念 (Passing Concepts)',
    'passing-routes': '新增传球路线 (Additional Passing Routes)'
}

for cat_id in ['offense-formation', 'defense-formation', 'defense-coverage', 'passing-routes', 'passing-concepts']:
    if categories[cat_id]:
        new_tactics_section += f"    // ========== {category_names[cat_id]} ==========\n"
        for i, tactic in enumerate(categories[cat_id]):
            new_tactics_section += tactic
            if i < len(categories[cat_id]) - 1 or cat_id != 'passing-concepts':
                new_tactics_section += ","
            new_tactics_section += "\n"

# Find the position to insert (right before the closing of tactics array)
insert_point = data_content.rfind('    }\n  ]\n};')

if insert_point == -1:
    print("Error: Could not find insertion point")
    exit(1)

# Move past the last tactic's closing brace
insert_point = data_content.rfind('}', 0, insert_point) + 1

# Insert the new tactics
new_content = data_content[:insert_point] + ',' + new_tactics_section + '\n  ' + data_content[insert_point+1:]

# Write to new file
with open('../assets/js/data_extended.js', 'w', encoding='utf-8') as f:
    f.write(new_content)

print(f"\nSuccess! Created data_extended.js")
print(f"Total tactics now: {len(existing_ids) + len(new_tactics)}")
print("\nNext steps:")
print("1. Review data_extended.js")
print("2. Add Chinese translations for new tactics (look for nameCn: '')")
print("3. Create SVG diagrams for new tactics")
print("4. Rename data_extended.js to data.js when ready")
