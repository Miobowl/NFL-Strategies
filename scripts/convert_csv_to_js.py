#!/usr/bin/env python3
"""
Convert CSV tactics data to JavaScript format for NFL Strategies website
"""

import csv
import json
import re

# Category mapping from CSV to website categories
CATEGORY_MAP = {
    'Coverage': 'defense-coverage',
    'Formation': 'mixed-formation',  # Will split into offense/defense later
    'Passing Concept': 'passing-concepts',
    'Passing Route': 'passing-routes'
}

# Difficulty mapping based on complexity
DIFFICULTY_MAP = {
    'beginner': ['Cover Two Zone', 'Cover Three', 'I Formation', 'Shotgun', 'Go Route', 'Slant Route', 'Flat Route', 'Hitch Route'],
    'advanced': ['Cover Zero', 'Cover Six', '46 Bear', 'Wildcat', 'Stop and Go', 'Option Route']
}

def determine_difficulty(name):
    """Determine difficulty level based on name or complexity"""
    if any(term in name for term in DIFFICULTY_MAP['beginner']):
        return 'beginner'
    elif any(term in name for term in DIFFICULTY_MAP['advanced']):
        return 'advanced'
    else:
        return 'intermediate'

def split_list_field(field_text):
    """Split text into list by semicolons or sentence breaks"""
    if not field_text or field_text.strip() == '':
        return []

    # Split by semicolons first
    items = field_text.split(';')

    # If no semicolons, split by periods
    if len(items) == 1:
        items = field_text.split('.')

    # Clean up each item
    items = [item.strip() for item in items if item.strip()]

    return items[:5]  # Limit to 5 items

def create_slug(name):
    """Create URL-friendly slug from name"""
    slug = name.lower()
    slug = re.sub(r'[^\w\s-]', '', slug)
    slug = re.sub(r'[-\s]+', '-', slug)
    return slug

def determine_formation_type(name, key_features):
    """Determine if formation is offense or defense"""
    offense_keywords = ['QB', 'running back', 'receiver', 'tailback', 'fullback', 'RB', 'WR', 'TE']
    defense_keywords = ['linemen', 'linebacker', 'defensive back', 'DL', 'LB', 'DB', 'safety', 'corner']

    text = (name + ' ' + key_features).lower()

    offense_count = sum(1 for keyword in offense_keywords if keyword.lower() in text)
    defense_count = sum(1 for keyword in defense_keywords if keyword.lower() in text)

    if defense_count > offense_count:
        return 'defense-formation'
    else:
        return 'offense-formation'

def convert_csv_to_tactics(csv_file_path):
    """Convert CSV file to tactics data structure"""
    tactics = []

    with open(csv_file_path, 'r', encoding='utf-8') as csvfile:
        reader = csv.DictReader(csvfile)

        for row in reader:
            name = row['Name']
            category = row['Category']

            # Map category
            js_category = CATEGORY_MAP.get(category, 'other')

            # For formations, determine if offense or defense
            if js_category == 'mixed-formation':
                js_category = determine_formation_type(name, row['Key Features'])

            # Create tactic object
            tactic = {
                'id': create_slug(name),
                'category': js_category,
                'nameEn': name,
                'nameCn': '',  # Will be added manually
                'videoSource': f'https://www.youtube.com/watch?v=source{row["Source"]}',
                'videoTimestamp': '0:00',
                'description': row['Key Features'],
                'advantages': split_list_field(row['Advantages']),
                'weaknesses': split_list_field(row['Disadvantages']),
                'counters': split_list_field(row.get('Common Usage/Context', '')),
                'situations': split_list_field(row.get('Common Usage/Context', '')),
                'difficulty': determine_difficulty(name),
                'image': f'assets/images/{js_category}/{create_slug(name)}.svg'
            }

            tactics.append(tactic)

    return tactics

def format_as_js(tactics):
    """Format tactics list as JavaScript code"""
    js_code = "// Generated from CSV data\nconst csvTactics = [\n"

    for tactic in tactics:
        js_code += "  {\n"
        js_code += f"    id: '{tactic['id']}',\n"
        js_code += f"    category: '{tactic['category']}',\n"

        name_en = tactic['nameEn'].replace("'", "\\'")
        js_code += f"    nameEn: '{name_en}',\n"
        js_code += f"    nameCn: '',\n"
        js_code += f"    videoSource: '{tactic['videoSource']}',\n"
        js_code += f"    videoTimestamp: '{tactic['videoTimestamp']}',\n"

        description = tactic['description'].replace("'", "\\'").replace('\n', ' ')
        js_code += f"    description: '{description}',\n"

        # Format arrays
        js_code += f"    advantages: {json.dumps(tactic['advantages'], ensure_ascii=False)},\n"
        js_code += f"    weaknesses: {json.dumps(tactic['weaknesses'], ensure_ascii=False)},\n"
        js_code += f"    counters: {json.dumps(tactic['counters'], ensure_ascii=False)},\n"
        js_code += f"    situations: {json.dumps(tactic['situations'], ensure_ascii=False)},\n"
        js_code += f"    difficulty: '{tactic['difficulty']}',\n"
        js_code += f"    image: '{tactic['image']}'\n"
        js_code += "  },\n"

    js_code += "];\n"

    return js_code

def print_statistics(tactics):
    """Print statistics about the tactics"""
    from collections import Counter

    categories = Counter(t['category'] for t in tactics)
    difficulties = Counter(t['difficulty'] for t in tactics)

    print(f"\n=== STATISTICS ===")
    print(f"Total tactics: {len(tactics)}")
    print(f"\nBy category:")
    for category, count in categories.items():
        print(f"  {category}: {count}")
    print(f"\nBy difficulty:")
    for difficulty, count in difficulties.items():
        print(f"  {difficulty}: {count}")

if __name__ == '__main__':
    csv_path = '../Reference/Football Formations, Coverages, and Passing Concepts Breakdown - Table 1.csv'
    output_path = '../assets/js/csv_tactics.js'

    print("Converting CSV to JavaScript...")
    tactics = convert_csv_to_tactics(csv_path)

    print_statistics(tactics)

    js_code = format_as_js(tactics)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(js_code)

    print(f"\nOutput written to: {output_path}")
    print("\nNext steps:")
    print("1. Review the generated file")
    print("2. Add Chinese names (nameCn)")
    print("3. Create SVG diagrams for each tactic")
    print("4. Merge with existing data.js")
