#!/usr/bin/env python3
"""
Check which tactics are missing SVG diagrams
"""

import os
import re

# Read data.js and extract tactic IDs
def extract_tactic_ids(data_js_path):
    with open(data_js_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Find all id: 'xxx' patterns
    ids = re.findall(r"id:\s*'([^']+)'", content)

    # Organize by category
    tactics_by_category = {}

    # Extract tactics with their categories
    tactic_pattern = r"\{\s*id:\s*'([^']+)',\s*category:\s*'([^']+)'"
    matches = re.findall(tactic_pattern, content)

    for tactic_id, category in matches:
        if category not in tactics_by_category:
            tactics_by_category[category] = []
        tactics_by_category[category].append(tactic_id)

    return tactics_by_category

# Check which SVGs exist
def check_existing_svgs(base_path, category, tactic_ids):
    existing = []
    missing = []

    for tactic_id in tactic_ids:
        svg_path = os.path.join(base_path, category, f'{tactic_id}.svg')
        if os.path.exists(svg_path):
            existing.append(tactic_id)
        else:
            missing.append(tactic_id)

    return existing, missing

def main():
    data_js_path = '../assets/js/data.js'
    images_base = '../assets/images'

    print("分析 data.js 中的战术...")
    tactics_by_cat = extract_tactic_ids(data_js_path)

    print(f"\n战术总数: {sum(len(v) for v in tactics_by_cat.values())}")
    print("\n各分类战术数量:")
    for cat, tactics in sorted(tactics_by_cat.items()):
        print(f"  {cat}: {len(tactics)}")

    print("\n" + "="*60)
    print("检查SVG文件...")
    print("="*60)

    all_missing = []
    total_existing = 0

    for category, tactic_ids in sorted(tactics_by_cat.items()):
        existing, missing = check_existing_svgs(images_base, category, tactic_ids)
        total_existing += len(existing)

        print(f"\n[{category}]")
        print(f"  存在: {len(existing)}/{len(tactic_ids)}")

        if missing:
            print(f"  缺失: {len(missing)}")
            for tid in missing:
                print(f"    - {tid}")
                all_missing.append((category, tid))

    print("\n" + "="*60)
    print(f"总结:")
    print(f"  已有SVG: {total_existing}")
    print(f"  缺失SVG: {len(all_missing)}")
    print("="*60)

    if all_missing:
        print(f"\n需要创建的{len(all_missing)}个SVG:")
        for cat, tid in all_missing:
            print(f"  {cat}/{tid}.svg")

    return all_missing

if __name__ == '__main__':
    missing = main()
