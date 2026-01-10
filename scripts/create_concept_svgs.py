#!/usr/bin/env python3
"""
Create detailed SVG diagrams for all passing concepts
"""

import os

def svg_base(title_en, title_cn, subtitle=""):
    """Base SVG structure"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <!-- Background -->
  <rect width="800" height="600" fill="#2d5a2d"/>

  <!-- Field lines -->
  <line x1="0" y1="300" x2="800" y2="300" stroke="#ffffff" stroke-width="2" opacity="0.3"/>
  <line x1="400" y1="0" x2="400" y2="600" stroke="#ffffff" stroke-width="2" opacity="0.3"/>

  <!-- Yard markers -->
  <line x1="0" y1="450" x2="800" y2="450" stroke="#ffffff" stroke-width="1" opacity="0.2"/>
  <line x1="0" y1="350" x2="800" y2="350" stroke="#ffffff" stroke-width="1" opacity="0.2"/>
  <line x1="0" y1="250" x2="800" y2="250" stroke="#ffffff" stroke-width="1" opacity="0.2"/>
  <line x1="0" y1="150" x2="800" y2="150" stroke="#ffffff" stroke-width="1" opacity="0.2"/>

  <!-- Title -->
  <text x="400" y="40" text-anchor="middle" fill="#ffffff" font-size="28" font-weight="bold" font-family="Arial">
    {title_en}
  </text>
  <text x="400" y="70" text-anchor="middle" fill="#ffffff" font-size="18" font-family="Arial" opacity="0.8">
    {title_cn}{' - ' + subtitle if subtitle else ''}
  </text>

  <!-- Line of Scrimmage -->
  <line x1="100" y1="400" x2="700" y2="400" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>
  <text x="50" y="405" fill="#ffeb3b" font-size="14" font-weight="bold">LOS</text>

  <!-- Arrow markers -->
  <defs>
    <marker id="arrow1" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#00ffff"/>
    </marker>
    <marker id="arrow2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ff6b35"/>
    </marker>
    <marker id="arrow3" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#4a90e2"/>
    </marker>
    <marker id="arrow4" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#9b59b6"/>
    </marker>
  </defs>'''

def add_wr(x, y, label):
    """Add WR with label"""
    return f'''
  <circle cx="{x}" cy="{y}" r="12" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+4}" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">{label}</text>'''

def svg_legend():
    return '''
  <!-- Legend -->
  <g transform="translate(50, 540)">
    <circle cx="0" cy="0" r="10" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
    <text x="16" y="5" fill="#ffffff" font-size="10">= 接球手</text>

    <line x1="80" y1="0" x2="120" y2="0" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow1)"/>
    <text x="130" y="5" fill="#ffffff" font-size="10">= 路线</text>
  </g>'''

def close_svg():
    return '\n</svg>'

# === CONCEPT GENERATORS ===

def create_mesh():
    svg = svg_base("Mesh Concept", "网格概念", "交叉路线")

    # WRs
    svg += add_wr(200, 400, 'X')
    svg += add_wr(600, 400, 'Z')

    # Mesh routes (crossing)
    svg += '''
  <path d="M 200,385 L 200,340 L 500,280" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <path d="M 600,385 L 600,340 L 300,280" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>'''

    # Crossing point
    svg += '''
  <circle cx="400" cy="310" r="20" fill="#ffeb3b" opacity="0.2"/>
  <text x="400" y="315" text-anchor="middle" fill="#ffeb3b" font-size="11" font-weight="bold">交叉点</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">两个接球手交叉路线</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">制造覆盖冲突</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_levels():
    svg = svg_base("Levels Concept", "层次概念", "三层进攻")

    # 3 WRs
    svg += add_wr(180, 400, 'X')
    svg += add_wr(400, 400, 'Y')
    svg += add_wr(620, 400, 'Z')

    # Routes at different depths
    svg += '''
  <path d="M 180,385 L 180,330 L 250,330" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <text x="220" y="320" fill="#00ffff" font-size="10">浅层5码</text>

  <path d="M 400,385 L 400,250 L 450,250" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>
  <text x="430" y="240" fill="#ff6b35" font-size="10">中层12码</text>

  <path d="M 620,385 L 620,150" stroke="#4a90e2" stroke-width="3" fill="none" marker-end="url(#arrow3)"/>
  <text x="640" y="170" fill="#4a90e2" font-size="10">深层20码</text>'''

    # Depth lines
    svg += '''
  <line x1="100" y1="330" x2="700" y2="330" stroke="#00ffff" stroke-width="1" stroke-dasharray="5,5" opacity="0.3"/>
  <line x1="100" y1="250" x2="700" y2="250" stroke="#ff6b35" stroke-width="1" stroke-dasharray="5,5" opacity="0.3"/>
  <line x1="100" y1="150" x2="700" y2="150" stroke="#4a90e2" stroke-width="1" stroke-dasharray="5,5" opacity="0.3"/>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">三个不同深度的路线</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">攻击所有深度</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_flood():
    svg = svg_base("Flood Concept", "洪水概念", "三打二淹没")

    # 3 WRs on one side
    svg += add_wr(600, 400, 'X')
    svg += add_wr(560, 410, 'Y')
    svg += add_wr(520, 400, 'Z')

    # Routes flooding one side
    svg += '''
  <path d="M 600,385 L 600,340 L 530,340" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <text x="550" y="325" fill="#00ffff" font-size="10">Flat</text>

  <path d="M 560,395 L 540,250" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>
  <text x="520" y="240" fill="#ff6b35" font-size="10">Corner</text>

  <path d="M 520,385 L 500,160" stroke="#4a90e2" stroke-width="3" fill="none" marker-end="url(#arrow3)"/>
  <text x="480" y="170" fill="#4a90e2" font-size="10">Vertical</text>'''

    # Flood zone
    svg += '''
  <rect x="450" y="120" width="200" height="250" fill="#ffeb3b" opacity="0.1" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="550" y="200" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">淹没区</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">3个路线淹没一侧</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">制造人数优势</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_smash():
    svg = svg_base("Smash Concept", "粉碎概念", "高低组合")

    # 2 WRs
    svg += add_wr(650, 400, 'X')
    svg += add_wr(610, 410, 'Y')

    # Routes
    svg += '''
  <path d="M 650,385 L 650,340 L 580,340" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <text x="600" y="325" fill="#00ffff" font-size="11" font-weight="bold">Flat (低)</text>

  <path d="M 610,395 L 590,200" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>
  <text x="560" y="210" fill="#ff6b35" font-size="11" font-weight="bold">Corner (高)</text>'''

    # Coverage split
    svg += '''
  <circle cx="600" cy="270" r="30" fill="#ffeb3b" opacity="0.2"/>
  <text x="600" y="275" text-anchor="middle" fill="#ffeb3b" font-size="11" font-weight="bold">读CB</text>
  <text x="680" y="270" fill="#ffffff" font-size="10">高→Flat</text>
  <text x="680" y="285" fill="#ffffff" font-size="10">低→Corner</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">高低路线撕裂CB</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">制造2选1</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_y_cross():
    svg = svg_base("Y-Cross", "Y字交叉", "TE交叉路线")

    # WRs and TE
    svg += add_wr(180, 400, 'X')
    svg += add_wr(620, 400, 'Z')
    svg += '''
  <circle cx="550" cy="410" r="12" fill="#ff6b35" stroke="#ffffff" stroke-width="2"/>
  <text x="550" y="414" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">Y</text>'''

    # Routes
    svg += '''
  <path d="M 180,385 L 180,160" stroke="#4a90e2" stroke-width="3" fill="none" marker-end="url(#arrow3)"/>
  <path d="M 620,385 L 620,250 L 560,250" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <path d="M 550,395 L 500,360 L 350,280" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">TE交叉到对侧</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">拖曳线卫</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_four_verticals():
    svg = svg_base("Four Verticals", "四垂直路线", "垂直延伸")

    # 4 WRs
    svg += add_wr(180, 400, '1')
    svg += add_wr(340, 400, '2')
    svg += add_wr(460, 400, '3')
    svg += add_wr(620, 400, '4')

    # 4 vertical routes
    colors = ['#00ffff', '#ff6b35', '#4a90e2', '#9b59b6']
    markers = ['arrow1', 'arrow2', 'arrow3', 'arrow4']
    xs = [180, 340, 460, 620]

    for i, (x, color, marker) in enumerate(zip(xs, colors, markers)):
        depth = 140 + (i % 2) * 30
        svg += f'''
  <path d="M {x},385 L {x},{depth}" stroke="{color}" stroke-width="3" fill="none" marker-end="url(#{marker})"/>'''

    # Stress zones
    svg += '''
  <text x="260" y="200" fill="#ffeb3b" font-size="10">接缝</text>
  <text x="400" y="200" fill="#ffeb3b" font-size="10">接缝</text>
  <text x="540" y="200" fill="#ffeb3b" font-size="10">接缝</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">四条垂直路线</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">压迫深区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_stick():
    svg = svg_base("Stick Concept", "棍棒概念", "中距离控制")

    # WRs
    svg += add_wr(200, 400, 'X')
    svg += add_wr(550, 410, 'Y')
    svg += add_wr(650, 400, 'Z')

    # Routes
    svg += '''
  <path d="M 200,385 L 200,330 L 280,330" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <text x="250" y="320" fill="#00ffff" font-size="10">5码Stick</text>

  <path d="M 550,395 L 520,280" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>
  <text x="500" y="270" fill="#ff6b35" font-size="10">Seam</text>

  <path d="M 650,385 L 650,340 L 580,340" stroke="#4a90e2" stroke-width="3" fill="none" marker-end="url(#arrow3)"/>
  <text x="600" y="355" fill="#4a90e2" font-size="10">Flat</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">Stick + Seam + Flat组合</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">高成功率概念</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_drive():
    svg = svg_base("Drive Concept", "驱动概念", "斜插+平层")

    # WRs
    svg += add_wr(200, 400, 'X')
    svg += add_wr(600, 400, 'Z')

    # Routes
    svg += '''
  <path d="M 200,385 L 250,280" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <text x="230" y="270" fill="#00ffff" font-size="11" font-weight="bold">Drive</text>

  <path d="M 600,385 L 600,340 L 500,340" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>
  <text x="530" y="325" fill="#ff6b35" font-size="11" font-weight="bold">Flat</text>'''

    # Read zone
    svg += '''
  <rect x="200" y="260" width="350" height="100" fill="#ffeb3b" opacity="0.15" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="375" y="310" text-anchor="middle" fill="#ffeb3b" font-size="11">读LB</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">斜插+平层攻击LB</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">简单有效</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_dagger():
    svg = svg_base("Dagger Concept", "匕首概念", "双Dig组合")

    # WRs
    svg += add_wr(180, 400, 'X')
    svg += add_wr(620, 400, 'Z')

    # Dig routes
    svg += '''
  <path d="M 180,385 L 180,280 L 350,280" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <text x="270" y="270" fill="#00ffff" font-size="11">Dig 1</text>

  <path d="M 620,385 L 620,250 L 450,250" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>
  <text x="530" y="240" fill="#ff6b35" font-size="11">Dig 2</text>'''

    # Crossing point
    svg += '''
  <circle cx="400" cy="265" r="25" fill="#ffeb3b" opacity="0.2"/>
  <text x="400" y="220" text-anchor="middle" fill="#ffeb3b" font-size="11" font-weight="bold">交汇中区</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">两个Dig路线</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">攻击中区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_slant_flat():
    svg = svg_base("Slant Flat", "斜插平层组合", "快速组合")

    # WRs
    svg += add_wr(200, 400, 'X')
    svg += add_wr(600, 400, 'Z')

    # Routes
    svg += '''
  <path d="M 200,385 L 280,320" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <text x="250" y="310" fill="#00ffff" font-size="11" font-weight="bold">Slant</text>

  <path d="M 600,385 L 600,340 L 520,340" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>
  <text x="550" y="325" fill="#ff6b35" font-size="11" font-weight="bold">Flat</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">快速斜插+平层</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">3步传球</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_double_china():
    svg = svg_base("Double China", "双中路切入", "双Slant变体")

    # WRs
    svg += add_wr(180, 400, 'X')
    svg += add_wr(620, 400, 'Z')

    # Routes
    svg += '''
  <path d="M 180,385 L 300,280" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <text x="250" y="270" fill="#00ffff" font-size="11">China 1</text>

  <path d="M 620,385 L 500,280" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>
  <text x="550" y="270" fill="#ff6b35" font-size="11">China 2</text>'''

    # Converging point
    svg += '''
  <circle cx="400" cy="280" r="30" fill="#ffeb3b" opacity="0.2"/>
  <text x="400" y="285" text-anchor="middle" fill="#ffeb3b" font-size="11" font-weight="bold">会聚</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">两个内切中路</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">制造混乱</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_shallow_cross():
    svg = svg_base("Shallow Cross", "浅层交叉", "浅层拖曳")

    # WRs
    svg += add_wr(180, 400, 'X')
    svg += add_wr(620, 400, 'Z')

    # Routes
    svg += '''
  <path d="M 180,385 L 180,350 L 550,310" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#arrow1)"/>
  <text x="370" y="300" fill="#00ffff" font-size="11">Shallow</text>

  <path d="M 620,385 L 620,250" stroke="#ff6b35" stroke-width="3" fill="none" marker-end="url(#arrow2)"/>
  <text x="640" y="270" fill="#ff6b35" font-size="11">Clear</text>'''

    # Shallow zone
    svg += '''
  <rect x="150" y="300" width="500" height="60" fill="#ffeb3b" opacity="0.15" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="400" y="385" text-anchor="middle" fill="#ffeb3b" font-size="10">浅层拖曳区</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">浅层横向拖曳</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">拖出LB</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

# === SAVE FUNCTION ===

def save_svg(filename, content):
    """Save SVG to file"""
    filepath = f'../assets/images/passing-concepts/{filename}'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

# === MAIN EXECUTION ===

def main():
    """Generate all concept SVGs"""
    created = []

    concepts = {
        'mesh-concept': create_mesh,
        'levels-concept': create_levels,
        'flood-concept': create_flood,
        'smash-concept': create_smash,
        'y-cross': create_y_cross,
        'four-verticals': create_four_verticals,
        'stick-concept': create_stick,
        'drive-concept': create_drive,
        'dagger-concept': create_dagger,
        'slant-flat': create_slant_flat,
        'double-china': create_double_china,
        'shallow-cross': create_shallow_cross
    }

    print("Creating passing concept SVGs...")
    for name, generator in concepts.items():
        path = save_svg(f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal concept SVGs created: {len(created)}")
    return len(created)

if __name__ == '__main__':
    count = main()
    print(f"\n{'='*50}")
    print(f"SUCCESS! Created {count} concept SVG diagrams")
    print(f"{'='*50}")
