#!/usr/bin/env python3
"""
Create placeholder SVGs for all new tactics
"""

import os
import json

# List of all tactics that need SVGs
tactics_needing_svgs = {
    'offense-formation': [
        ('t-formation', 'T Formation', 'T字阵型'),
        ('single-back-ace', 'Single Back (Ace)', '单后卫ACE阵型'),
        ('pro-set', 'Pro Set', '职业套装阵型'),
        ('shotgun', 'Shotgun', '霰弹枪阵型'),
        ('pistol', 'Pistol', '手枪阵型'),
        ('spread', 'Spread', '展开阵型'),
        ('wildcat', 'Wildcat', '野猫阵型'),
        ('jumbo-goal-line', 'Jumbo (Goal Line)', '重型球门线阵型'),
    ],
    'defense-formation': [
        ('6-2-formation', '6-2 Formation', '6-2防守阵型'),
        ('5-3-formation', '5-3 Formation', '5-3防守阵型'),
        ('5-2-eagle', '5-2 Eagle', '5-2老鹰阵型'),
        ('4-4-formation', '4-4 Formation', '4-4防守阵型'),
        ('3-4-formation', '3-4 Formation', '3-4防守阵型'),
        ('4-3-formation', '4-3 Formation', '4-3防守阵型'),
        ('46-bear', '46 Bear', '46熊式防守'),
        ('nickel-formation', 'Nickel Formation', '镍币防守(5后卫)'),
        ('dime-formation', 'Dime Formation', '一角硬币防守(6后卫)'),
    ],
    'defense-coverage': [
        ('cover-zero', 'Cover Zero', 'Cover 0全场人盯人'),
        ('cover-one', 'Cover One', 'Cover 1人盯人'),
        ('cover-one-robber', 'Cover One Robber', 'Cover 1抢断式'),
        ('cover-two-zone', 'Cover Two Zone', 'Cover 2区域防守'),
        ('cover-two-man', 'Cover Two Man', 'Cover 2人盯人'),
        ('cover-two-buzz', 'Cover Two Buzz', 'Cover 2冲锋式'),
        ('tampa-2', 'Tampa 2', 'Tampa 2防守'),
        ('cover-three', 'Cover Three', 'Cover 3防守'),
        ('cover-three-cloud', 'Cover Three Cloud', 'Cover 3云式'),
        ('cover-three-buzz', 'Cover Three Buzz', 'Cover 3冲锋式'),
        ('cover-four-quarters', 'Cover Four (Quarters)', 'Cover 4四分防守'),
        ('cover-six', 'Cover Six', 'Cover 6混合防守'),
    ],
    'passing-routes': [
        ('flat-route', 'Flat Route', '平层路线'),
        ('comeback-route', 'Comeback Route', '回马枪路线'),
        ('hitch-route', 'Hitch Route', '急停路线'),
        ('dig-route', 'Dig Route', '挖掘路线'),
        ('wheel-route', 'Wheel Route', '轮式路线'),
        ('seam-route', 'Seam Route', '接缝路线'),
        ('option-route', 'Option Route', '选择路线'),
        ('stop-and-go', 'Stop and Go', '急停再启动'),
    ],
    'passing-concepts': [
        ('mesh-concept', 'Mesh Concept', '网格概念'),
        ('levels-concept', 'Levels Concept', '层次概念'),
        ('flood-concept', 'Flood Concept', '洪水概念'),
        ('smash-concept', 'Smash Concept', '粉碎概念'),
        ('y-cross', 'Y-Cross', 'Y字交叉'),
        ('four-verticals', 'Four Verticals', '四垂直路线'),
        ('stick-concept', 'Stick Concept', '棍棒概念'),
        ('drive-concept', 'Drive Concept', '驱动概念'),
        ('dagger-concept', 'Dagger Concept', '匕首概念'),
        ('slant-flat', 'Slant Flat', '斜插平层组合'),
        ('double-china', 'Double China', '双中路切入'),
        ('shallow-cross', 'Shallow Cross', '浅层交叉'),
    ]
}

def create_placeholder_svg(title_en, title_cn, category_icon=''):
    """Create a placeholder SVG"""
    # Category-specific icons/descriptions
    category_descriptions = {
        'offense-formation': '进攻阵型',
        'defense-formation': '防守阵型',
        'defense-coverage': '防守覆盖',
        'passing-routes': '传球路线',
        'passing-concepts': '传球概念'
    }

    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <!-- Background -->
  <rect width="800" height="600" fill="#2d5a2d"/>

  <!-- Field lines -->
  <line x1="0" y1="300" x2="800" y2="300" stroke="#ffffff" stroke-width="2" opacity="0.3"/>
  <line x1="400" y1="0" x2="400" y2="600" stroke="#ffffff" stroke-width="2" opacity="0.3"/>

  <!-- Title -->
  <text x="400" y="200" text-anchor="middle" fill="#ffffff" font-size="32" font-weight="bold" font-family="Arial">
    {title_en}
  </text>
  <text x="400" y="250" text-anchor="middle" fill="#ffffff" font-size="24" font-family="Arial" opacity="0.8">
    {title_cn}
  </text>

  <!-- Icon/Emoji if needed -->
  <text x="400" y="320" text-anchor="middle" fill="#ffffff" font-size="80" opacity="0.3">
    {category_icon}
  </text>

  <!-- Placeholder note -->
  <text x="400" y="400" text-anchor="middle" fill="#ffeb3b" font-size="14" font-style="italic">
    SVG diagram coming soon
  </text>
  <text x="400" y="425" text-anchor="middle" fill="#ffeb3b" font-size="14" font-style="italic">
    详细图解制作中...
  </text>

  <!-- Border -->
  <rect x="10" y="10" width="780" height="580" fill="none" stroke="#ffffff" stroke-width="2" opacity="0.2" rx="10"/>
</svg>'''

def create_all_placeholders():
    """Create placeholder SVGs for all tactics"""
    total_created = 0

    for category, tactics_list in tactics_needing_svgs.items():
        # Category icons
        icons = {
            'offense-formation': '🏈',
            'defense-formation': '⚔️',
            'defense-coverage': '🛡️',
            'passing-routes': '📍',
            'passing-concepts': '🎯'
        }

        for tactic_id, name_en, name_cn in tactics_list:
            filename = f'{tactic_id}.svg'
            filepath = f'../assets/images/{category}/{filename}'

            # Skip if file already exists
            if os.path.exists(filepath):
                print(f"Skipped (already exists): {filepath}")
                continue

            # Create directory if needed
            os.makedirs(os.path.dirname(filepath), exist_ok=True)

            # Generate SVG
            svg_content = create_placeholder_svg(name_en, name_cn, icons.get(category, ''))

            # Write file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(svg_content)

            print(f"Created: {filepath}")
            total_created += 1

    return total_created

if __name__ == '__main__':
    print("Creating placeholder SVG diagrams...\n")
    count = create_all_placeholders()
    print(f"\n✓ Created {count} placeholder SVG diagrams")
    print(f"✓ Total tactics with SVGs: {sum(len(v) for v in tactics_needing_svgs.values())}")
    print("\nNote: These are placeholders. You can replace them with detailed diagrams later.")
