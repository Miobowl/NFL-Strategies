#!/usr/bin/env python3
"""
Add Chinese translations to tactics
"""

# Chinese name mappings
chinese_names = {
    # Offensive Formations
    't-formation': 'T字阵型',
    'single-back-ace': '单后卫ACE阵型',
    'pro-set': '职业套装阵型',
    'shotgun': '霰弹枪阵型',
    'pistol': '手枪阵型',
    'spread': '展开阵型',
    'wildcat': '野猫阵型',
    'jumbo-goal-line': '重型球门线阵型',

    # Defensive Formations
    '6-2-formation': '6-2防守阵型',
    '5-3-formation': '5-3防守阵型',
    '5-2-eagle': '5-2老鹰阵型',
    '4-4-formation': '4-4防守阵型',
    '3-4-formation': '3-4防守阵型',
    '4-3-formation': '4-3防守阵型',
    '46-bear': '46熊式防守',
    'nickel-formation': '镍币防守(5后卫)',
    'dime-formation': '一角硬币防守(6后卫)',

    # Defense Coverage
    'cover-zero': 'Cover 0全场人盯人',
    'cover-one': 'Cover 1人盯人',
    'cover-one-robber': 'Cover 1抢断式',
    'cover-two-zone': 'Cover 2区域防守',
    'cover-two-man': 'Cover 2人盯人',
    'cover-two-buzz': 'Cover 2冲锋式',
    'tampa-2': 'Tampa 2防守',
    'cover-three': 'Cover 3防守',
    'cover-three-cloud': 'Cover 3云式',
    'cover-three-buzz': 'Cover 3冲锋式',
    'cover-four-quarters': 'Cover 4四分防守',
    'cover-six': 'Cover 6混合防守',

    # Passing Routes
    'flat-route': '平层路线',
    'comeback-route': '回马枪路线',
    'hitch-route': '急停路线',
    'dig-route': '挖掘路线',
    'wheel-route': '轮式路线',
    'seam-route': '接缝路线',
    'option-route': '选择路线',
    'stop-and-go': '急停再启动',

    # Passing Concepts
    'mesh-concept': '网格概念',
    'levels-concept': '层次概念',
    'flood-concept': '洪水概念',
    'smash-concept': '粉碎概念',
    'y-cross': 'Y字交叉',
    'four-verticals': '四垂直路线',
    'stick-concept': '棍棒概念',
    'drive-concept': '驱动概念',
    'dagger-concept': '匕首概念',
    'slant-flat': '斜插平层组合',
    'double-china': '双中路切入',
    'shallow-cross': '浅层交叉'
}

# Read the file
with open('../assets/js/data.js', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace empty nameCn with Chinese names
for tactic_id, chinese_name in chinese_names.items():
    # Find the pattern: id: 'tactic-id', ... nameCn: '',
    import re
    # Use a more specific pattern to match the exact tactic
    pattern = f"(id: '{tactic_id}',\s+category: '[^']+',\s+nameEn: '[^']+',\s+nameCn: )''"
    replacement = f"\\1'{chinese_name}'"
    content = re.sub(pattern, replacement, content)

# Write back
with open('../assets/js/data.js', 'w', encoding='utf-8') as f:
    f.write(content)

print(f"Successfully added {len(chinese_names)} Chinese translations!")
print("\nTranslations added for:")
for category in ['Offensive Formations', 'Defensive Formations', 'Defense Coverage', 'Passing Routes', 'Passing Concepts']:
    print(f"\n{category}:")
    count = 0
    for key in chinese_names:
        if (category == 'Offensive Formations' and 'formation' in key and key not in ['nickel-formation', 'dime-formation', '3-4-formation', '4-3-formation', '4-4-formation', '5-2-eagle', '5-3-formation', '6-2-formation', '46-bear']) or \
           (category == 'Defensive Formations' and key in ['nickel-formation', 'dime-formation', '3-4-formation', '4-3-formation', '4-4-formation', '5-2-eagle', '5-3-formation', '6-2-formation', '46-bear']) or \
           (category == 'Defense Coverage' and 'cover' in key or 'tampa' in key) or \
           (category == 'Passing Routes' and 'route' in key) or \
           (category == 'Passing Concepts' and 'concept' in key or key in ['y-cross', 'four-verticals', 'slant-flat', 'double-china', 'shallow-cross']):
            print(f"  {key}: {chinese_names[key]}")
            count += 1
    print(f"  Total: {count}")
