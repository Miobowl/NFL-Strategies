#!/usr/bin/env python3
"""
检查并创建所有缺失的SVG图像
"""

import os
import re

# 基础路径
BASE_PATH = r"\\DXP4800-SUI\personal_folder\400 Coding\NFL Strategies"
DATA_JS_PATH = os.path.join(BASE_PATH, "assets", "js", "data.js")
IMAGES_BASE = os.path.join(BASE_PATH, "assets", "images")

def extract_tactics_from_data_js():
    """从data.js中提取所有战术信息"""
    with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取所有战术对象
    tactics = []
    pattern = r"\{\s*id:\s*'([^']+)',\s*category:\s*'([^']+)',\s*nameEn:\s*'([^']*)',\s*nameCn:\s*'([^']*)'"
    matches = re.findall(pattern, content)

    for match in matches:
        tactic_id, category, name_en, name_cn = match
        tactics.append({
            'id': tactic_id,
            'category': category,
            'nameEn': name_en,
            'nameCn': name_cn
        })

    return tactics

def check_svg_exists(category, tactic_id):
    """检查SVG文件是否存在"""
    svg_path = os.path.join(IMAGES_BASE, category, f'{tactic_id}.svg')
    return os.path.exists(svg_path)

def create_svg_template(category, tactic_id, name_en, name_cn):
    """创建SVG模板"""

    # 根据类别确定SVG内容
    if category == 'offense-formation':
        return create_offense_formation_svg(tactic_id, name_en, name_cn)
    elif category == 'defense-formation':
        return create_defense_formation_svg(tactic_id, name_en, name_cn)
    elif category == 'defense-coverage':
        return create_defense_coverage_svg(tactic_id, name_en, name_cn)
    elif category == 'passing-routes':
        return create_passing_route_svg(tactic_id, name_en, name_cn)
    elif category == 'passing-concepts':
        return create_passing_concept_svg(tactic_id, name_en, name_cn)
    elif category == 'running-plays':
        return create_running_play_svg(tactic_id, name_en, name_cn)
    else:
        return create_generic_svg(name_en, name_cn)

def create_offense_formation_svg(tactic_id, name_en, name_cn):
    """创建进攻阵型SVG"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <style>
      .field {{ fill: #2d5016; stroke: white; stroke-width: 2; }}
      .line {{ stroke: white; stroke-width: 2; fill: none; }}
      .player-offense {{ fill: #ff6b6b; stroke: #c92a2a; stroke-width: 2; }}
      .player-qb {{ fill: #ffd93d; stroke: #f59f00; stroke-width: 2; }}
      .player-rb {{ fill: #4ecdc4; stroke: #0b7285; stroke-width: 2; }}
      .player-wr {{ fill: #a78bfa; stroke: #6d28d9; stroke-width: 2; }}
      .label {{ font-family: Arial, sans-serif; font-size: 14px; fill: white; text-anchor: middle; }}
      .title {{ font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: white; text-anchor: middle; }}
    </style>
  </defs>

  <!-- Field -->
  <rect class="field" x="0" y="0" width="800" height="600"/>

  <!-- Yard Lines -->
  <line class="line" x1="0" y1="300" x2="800" y2="300"/>
  <line class="line" x1="400" y1="0" x2="400" y2="600"/>

  <!-- Title -->
  <text class="title" x="400" y="40">{name_en}</text>
  <text class="label" x="400" y="65">{name_cn}</text>

  <!-- Offensive Line (5 players) -->
  <circle class="player-offense" cx="350" cy="300" r="15"/>
  <text class="label" x="350" y="335">LT</text>

  <circle class="player-offense" cx="380" cy="300" r="15"/>
  <text class="label" x="380" y="335">LG</text>

  <circle class="player-offense" cx="410" cy="300" r="15"/>
  <text class="label" x="410" y="335">C</text>

  <circle class="player-offense" cx="440" cy="300" r="15"/>
  <text class="label" x="440" y="335">RG</text>

  <circle class="player-offense" cx="470" cy="300" r="15"/>
  <text class="label" x="470" y="335">RT</text>

  <!-- QB -->
  <circle class="player-qb" cx="410" cy="350" r="15"/>
  <text class="label" x="410" y="385">QB</text>

  <!-- Wide Receivers -->
  <circle class="player-wr" cx="250" cy="300" r="15"/>
  <text class="label" x="250" y="335">WR</text>

  <circle class="player-wr" cx="570" cy="300" r="15"/>
  <text class="label" x="570" y="335">WR</text>

  <!-- Running Back -->
  <circle class="player-rb" cx="410" cy="400" r="15"/>
  <text class="label" x="410" y="435">RB</text>
</svg>'''

def create_defense_formation_svg(tactic_id, name_en, name_cn):
    """创建防守阵型SVG"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <style>
      .field {{ fill: #2d5016; stroke: white; stroke-width: 2; }}
      .line {{ stroke: white; stroke-width: 2; fill: none; }}
      .player-dl {{ fill: #3b82f6; stroke: #1e40af; stroke-width: 2; }}
      .player-lb {{ fill: #06b6d4; stroke: #0e7490; stroke-width: 2; }}
      .player-db {{ fill: #8b5cf6; stroke: #5b21b6; stroke-width: 2; }}
      .label {{ font-family: Arial, sans-serif; font-size: 14px; fill: white; text-anchor: middle; }}
      .title {{ font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: white; text-anchor: middle; }}
    </style>
  </defs>

  <!-- Field -->
  <rect class="field" x="0" y="0" width="800" height="600"/>

  <!-- Yard Lines -->
  <line class="line" x1="0" y1="300" x2="800" y2="300"/>
  <line class="line" x1="400" y1="0" x2="400" y2="600"/>

  <!-- Title -->
  <text class="title" x="400" y="40">{name_en}</text>
  <text class="label" x="400" y="65">{name_cn}</text>

  <!-- Defensive Line -->
  <circle class="player-dl" cx="360" cy="280" r="15"/>
  <text class="label" x="360" y="265">DE</text>

  <circle class="player-dl" cx="390" cy="280" r="15"/>
  <text class="label" x="390" y="265">DT</text>

  <circle class="player-dl" cx="430" cy="280" r="15"/>
  <text class="label" x="430" y="265">DT</text>

  <circle class="player-dl" cx="460" cy="280" r="15"/>
  <text class="label" x="460" y="265">DE</text>

  <!-- Linebackers -->
  <circle class="player-lb" cx="340" cy="230" r="15"/>
  <text class="label" x="340" y="215">OLB</text>

  <circle class="player-lb" cx="410" cy="230" r="15"/>
  <text class="label" x="410" y="215">MLB</text>

  <circle class="player-lb" cx="480" cy="230" r="15"/>
  <text class="label" x="480" y="215">OLB</text>

  <!-- Defensive Backs -->
  <circle class="player-db" cx="300" cy="180" r="15"/>
  <text class="label" x="300" y="165">CB</text>

  <circle class="player-db" cx="380" cy="150" r="15"/>
  <text class="label" x="380" y="135">SS</text>

  <circle class="player-db" cx="440" cy="150" r="15"/>
  <text class="label" x="440" y="135">FS</text>

  <circle class="player-db" cx="520" cy="180" r="15"/>
  <text class="label" x="520" y="165">CB</text>
</svg>'''

def create_defense_coverage_svg(tactic_id, name_en, name_cn):
    """创建防守覆盖SVG"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <style>
      .field {{ fill: #2d5016; stroke: white; stroke-width: 2; }}
      .line {{ stroke: white; stroke-width: 2; fill: none; }}
      .zone {{ fill: rgba(59, 130, 246, 0.3); stroke: #3b82f6; stroke-width: 2; }}
      .player-db {{ fill: #8b5cf6; stroke: #5b21b6; stroke-width: 2; }}
      .player-lb {{ fill: #06b6d4; stroke: #0e7490; stroke-width: 2; }}
      .coverage-arrow {{ stroke: #fbbf24; stroke-width: 3; fill: none; marker-end: url(#arrowhead); }}
      .label {{ font-family: Arial, sans-serif; font-size: 14px; fill: white; text-anchor: middle; }}
      .title {{ font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: white; text-anchor: middle; }}
    </style>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#fbbf24"/>
    </marker>
  </defs>

  <!-- Field -->
  <rect class="field" x="0" y="0" width="800" height="600"/>

  <!-- Yard Lines -->
  <line class="line" x1="0" y1="450" x2="800" y2="450"/>

  <!-- Title -->
  <text class="title" x="400" y="40">{name_en}</text>
  <text class="label" x="400" y="65">{name_cn}</text>

  <!-- Coverage Zones -->
  <rect class="zone" x="50" y="100" width="200" height="300"/>
  <rect class="zone" x="300" y="100" width="200" height="300"/>
  <rect class="zone" x="550" y="100" width="200" height="300"/>

  <!-- Defensive Backs -->
  <circle class="player-db" cx="150" cy="150" r="15"/>
  <text class="label" x="150" y="135">CB</text>

  <circle class="player-db" cx="400" cy="120" r="15"/>
  <text class="label" x="400" y="105">S</text>

  <circle class="player-db" cx="650" cy="150" r="15"/>
  <text class="label" x="650" y="135">CB</text>

  <!-- Linebackers -->
  <circle class="player-lb" cx="300" cy="350" r="15"/>
  <text class="label" x="300" y="385">LB</text>

  <circle class="player-lb" cx="500" cy="350" r="15"/>
  <text class="label" x="500" y="385">LB</text>
</svg>'''

def create_passing_route_svg(tactic_id, name_en, name_cn):
    """创建传球路线SVG"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <style>
      .field {{ fill: #2d5016; stroke: white; stroke-width: 2; }}
      .line {{ stroke: white; stroke-width: 2; fill: none; }}
      .route {{ stroke: #fbbf24; stroke-width: 4; fill: none; marker-end: url(#arrowhead); }}
      .player-wr {{ fill: #a78bfa; stroke: #6d28d9; stroke-width: 2; }}
      .player-qb {{ fill: #ffd93d; stroke: #f59f00; stroke-width: 2; }}
      .label {{ font-family: Arial, sans-serif; font-size: 14px; fill: white; text-anchor: middle; }}
      .title {{ font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: white; text-anchor: middle; }}
    </style>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#fbbf24"/>
    </marker>
  </defs>

  <!-- Field -->
  <rect class="field" x="0" y="0" width="800" height="600"/>

  <!-- Yard Lines -->
  <line class="line" x1="0" y1="500" x2="800" y2="500"/>

  <!-- Title -->
  <text class="title" x="400" y="40">{name_en}</text>
  <text class="label" x="400" y="65">{name_cn}</text>

  <!-- QB -->
  <circle class="player-qb" cx="400" cy="520" r="15"/>
  <text class="label" x="400" y="555">QB</text>

  <!-- WR at start position -->
  <circle class="player-wr" cx="300" cy="500" r="15"/>
  <text class="label" x="300" y="535">WR</text>

  <!-- Route path (example - vertical) -->
  <path class="route" d="M 300 485 L 300 150"/>
</svg>'''

def create_passing_concept_svg(tactic_id, name_en, name_cn):
    """创建传球概念SVG"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <style>
      .field {{ fill: #2d5016; stroke: white; stroke-width: 2; }}
      .line {{ stroke: white; stroke-width: 2; fill: none; }}
      .route1 {{ stroke: #fbbf24; stroke-width: 3; fill: none; marker-end: url(#arrowhead1); }}
      .route2 {{ stroke: #f472b6; stroke-width: 3; fill: none; marker-end: url(#arrowhead2); }}
      .route3 {{ stroke: #34d399; stroke-width: 3; fill: none; marker-end: url(#arrowhead3); }}
      .player-wr {{ fill: #a78bfa; stroke: #6d28d9; stroke-width: 2; }}
      .player-qb {{ fill: #ffd93d; stroke: #f59f00; stroke-width: 2; }}
      .label {{ font-family: Arial, sans-serif; font-size: 14px; fill: white; text-anchor: middle; }}
      .title {{ font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: white; text-anchor: middle; }}
    </style>
    <marker id="arrowhead1" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#fbbf24"/>
    </marker>
    <marker id="arrowhead2" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#f472b6"/>
    </marker>
    <marker id="arrowhead3" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#34d399"/>
    </marker>
  </defs>

  <!-- Field -->
  <rect class="field" x="0" y="0" width="800" height="600"/>

  <!-- Yard Lines -->
  <line class="line" x1="0" y1="500" x2="800" y2="500"/>

  <!-- Title -->
  <text class="title" x="400" y="40">{name_en}</text>
  <text class="label" x="400" y="65">{name_cn}</text>

  <!-- QB -->
  <circle class="player-qb" cx="400" cy="520" r="15"/>
  <text class="label" x="400" y="555">QB</text>

  <!-- WR1 -->
  <circle class="player-wr" cx="200" cy="500" r="12"/>
  <path class="route1" d="M 200 488 L 200 150"/>

  <!-- WR2 -->
  <circle class="player-wr" cx="350" cy="500" r="12"/>
  <path class="route2" d="M 350 488 L 350 300 L 500 250"/>

  <!-- WR3 -->
  <circle class="player-wr" cx="600" cy="500" r="12"/>
  <path class="route3" d="M 600 488 L 600 150"/>
</svg>'''

def create_running_play_svg(tactic_id, name_en, name_cn):
    """创建跑球战术SVG"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <style>
      .field {{ fill: #2d5016; stroke: white; stroke-width: 2; }}
      .line {{ stroke: white; stroke-width: 2; fill: none; }}
      .run-path {{ stroke: #4ecdc4; stroke-width: 5; fill: none; marker-end: url(#arrowhead); }}
      .block-arrow {{ stroke: #ff6b6b; stroke-width: 3; fill: none; marker-end: url(#blockarrow); }}
      .player-offense {{ fill: #ff6b6b; stroke: #c92a2a; stroke-width: 2; }}
      .player-qb {{ fill: #ffd93d; stroke: #f59f00; stroke-width: 2; }}
      .player-rb {{ fill: #4ecdc4; stroke: #0b7285; stroke-width: 2; }}
      .player-defense {{ fill: #3b82f6; stroke: #1e40af; stroke-width: 2; }}
      .label {{ font-family: Arial, sans-serif; font-size: 14px; fill: white; text-anchor: middle; }}
      .title {{ font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: white; text-anchor: middle; }}
    </style>
    <marker id="arrowhead" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#4ecdc4"/>
    </marker>
    <marker id="blockarrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#ff6b6b"/>
    </marker>
  </defs>

  <!-- Field -->
  <rect class="field" x="0" y="0" width="800" height="600"/>

  <!-- Yard Lines -->
  <line class="line" x1="0" y1="400" x2="800" y2="400"/>

  <!-- Title -->
  <text class="title" x="400" y="40">{name_en}</text>
  <text class="label" x="400" y="65">{name_cn}</text>

  <!-- Offensive Line -->
  <circle class="player-offense" cx="350" cy="400" r="12"/>
  <circle class="player-offense" cx="380" cy="400" r="12"/>
  <circle class="player-offense" cx="410" cy="400" r="12"/>
  <circle class="player-offense" cx="440" cy="400" r="12"/>
  <circle class="player-offense" cx="470" cy="400" r="12"/>

  <!-- QB -->
  <circle class="player-qb" cx="410" cy="440" r="12"/>
  <text class="label" x="410" y="470">QB</text>

  <!-- RB -->
  <circle class="player-rb" cx="410" cy="480" r="12"/>
  <text class="label" x="410" y="510">RB</text>

  <!-- Defensive players -->
  <circle class="player-defense" cx="380" cy="360" r="10"/>
  <circle class="player-defense" cx="440" cy="360" r="10"/>

  <!-- Run path -->
  <path class="run-path" d="M 410 470 L 450 300 L 500 200"/>
</svg>'''

def create_generic_svg(name_en, name_cn):
    """创建通用SVG模板"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600">
  <defs>
    <style>
      .field {{ fill: #2d5016; stroke: white; stroke-width: 2; }}
      .line {{ stroke: white; stroke-width: 2; fill: none; }}
      .label {{ font-family: Arial, sans-serif; font-size: 14px; fill: white; text-anchor: middle; }}
      .title {{ font-family: Arial, sans-serif; font-size: 24px; font-weight: bold; fill: white; text-anchor: middle; }}
    </style>
  </defs>

  <!-- Field -->
  <rect class="field" x="0" y="0" width="800" height="600"/>

  <!-- Yard Lines -->
  <line class="line" x1="0" y1="300" x2="800" y2="300"/>
  <line class="line" x1="400" y1="0" x2="400" y2="600"/>

  <!-- Title -->
  <text class="title" x="400" y="280">{name_en}</text>
  <text class="label" x="400" y="310">{name_cn}</text>
</svg>'''

def save_svg(category, tactic_id, svg_content):
    """保存SVG文件"""
    category_path = os.path.join(IMAGES_BASE, category)

    # 确保目录存在
    os.makedirs(category_path, exist_ok=True)

    svg_file_path = os.path.join(category_path, f'{tactic_id}.svg')

    with open(svg_file_path, 'w', encoding='utf-8') as f:
        f.write(svg_content)

    return svg_file_path

def main():
    print("="*60)
    print("检查并创建缺失的SVG图像")
    print("="*60)

    # 提取战术信息
    print("\n从 data.js 提取战术信息...")
    tactics = extract_tactics_from_data_js()
    print(f"找到 {len(tactics)} 个战术")

    # 检查缺失的SVG
    missing_svgs = []
    for tactic in tactics:
        if not check_svg_exists(tactic['category'], tactic['id']):
            missing_svgs.append(tactic)

    print(f"\n发现 {len(missing_svgs)} 个缺失的SVG")

    if not missing_svgs:
        print("\n所有战术都已有SVG图像!")
        return

    # 按类别分组显示
    by_category = {}
    for tactic in missing_svgs:
        cat = tactic['category']
        if cat not in by_category:
            by_category[cat] = []
        by_category[cat].append(tactic)

    print("\n缺失的SVG按类别:")
    for cat, tactics_list in sorted(by_category.items()):
        print(f"\n  [{cat}] - {len(tactics_list)} 个:")
        for t in tactics_list:
            print(f"    - {t['id']} ({t['nameEn']} / {t['nameCn']})")

    # 询问是否创建
    print("\n" + "="*60)
    response = input("是否创建这些缺失的SVG? (y/n): ").strip().lower()

    if response != 'y':
        print("已取消")
        return

    # 创建SVG
    print("\n开始创建SVG...")
    created = 0

    for tactic in missing_svgs:
        svg_content = create_svg_template(
            tactic['category'],
            tactic['id'],
            tactic['nameEn'],
            tactic['nameCn']
        )

        svg_path = save_svg(tactic['category'], tactic['id'], svg_content)
        print(f"  ✓ 创建: {svg_path}")
        created += 1

    print("\n" + "="*60)
    print(f"完成! 共创建 {created} 个SVG文件")
    print("="*60)

if __name__ == '__main__':
    main()
