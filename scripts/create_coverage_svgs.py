#!/usr/bin/env python3
"""
Create detailed SVG diagrams for all defense coverage schemes
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

  <!-- Title -->
  <text x="400" y="40" text-anchor="middle" fill="#ffffff" font-size="28" font-weight="bold" font-family="Arial">
    {title_en}
  </text>
  <text x="400" y="70" text-anchor="middle" fill="#ffffff" font-size="18" font-family="Arial" opacity="0.8">
    {title_cn}{' - ' + subtitle if subtitle else ''}
  </text>

  <!-- Line of Scrimmage -->
  <line x1="100" y1="350" x2="700" y2="350" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>
  <text x="50" y="355" fill="#ffeb3b" font-size="14" font-weight="bold">LOS</text>'''

def add_zone(x, y, width, height, label, color="#ff4444"):
    """Add coverage zone"""
    return f'''
  <rect x="{x}" y="{y}" width="{width}" height="{height}" fill="{color}" opacity="0.2" stroke="{color}" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="{x + width//2}" y="{y + height//2 + 5}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">{label}</text>'''

def add_defender(x, y, label, size=16):
    """Add defender"""
    return f'''
  <circle cx="{x}" cy="{y}" r="{size}" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+5}" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">{label}</text>'''

def add_receiver(x, y):
    """Add offensive receiver"""
    return f'''
  <circle cx="{x}" cy="{y}" r="12" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+4}" text-anchor="middle" fill="#ffffff" font-size="9" font-weight="bold">WR</text>'''

def add_coverage_arrow(x1, y1, x2, y2, color="#ff4444"):
    """Add coverage assignment arrow"""
    return f'''
  <line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{color}" stroke-width="2" stroke-dasharray="3,3" opacity="0.6" marker-end="url(#arrowhead)"/>'''

def svg_legend():
    return '''
  <!-- Legend -->
  <g transform="translate(50, 540)">
    <circle cx="0" cy="0" r="12" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
    <text x="18" y="5" fill="#ffffff" font-size="11">= 进攻</text>

    <circle cx="80" cy="0" r="12" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
    <text x="98" y="5" fill="#ffffff" font-size="11">= 防守</text>

    <line x1="160" y1="0" x2="200" y2="0" stroke="#ff4444" stroke-width="2" stroke-dasharray="3,3"/>
    <text x="210" y="5" fill="#ffffff" font-size="11">= 覆盖责任</text>
  </g>'''

def close_svg():
    return '''
  <!-- Arrow marker -->
  <defs>
    <marker id="arrowhead" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ff4444" opacity="0.6"/>
    </marker>
  </defs>
</svg>'''

# === COVERAGE SCHEMES ===

def create_cover_zero():
    svg = svg_base("Cover Zero", "Cover 0全场人盯人", "无安全卫协防")

    # 5 receivers
    receivers = [(150, 350), (250, 340), (550, 340), (650, 350), (400, 360)]
    for x, y in receivers:
        svg += add_receiver(x, y)

    # 5 defenders man coverage
    defenders = [(150, 300), (250, 290), (550, 290), (650, 300), (400, 310)]
    labels = ['CB', 'NB', 'NB', 'CB', 'LB']
    for (x, y), label in zip(defenders, labels):
        svg += add_defender(x, y, label)
        svg += add_coverage_arrow(x, y, receivers[defenders.index((x, y))][0], receivers[defenders.index((x, y))][1])

    # Blitzers
    svg += add_defender(300, 320, 'BLZ', 18)
    svg += add_defender(500, 320, 'BLZ', 18)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">全人盯人 - 无安全卫</text>
  <text x="400" y="500" text-anchor="middle" fill="#00ffff" font-size="11">高风险高回报</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_one():
    svg = svg_base("Cover One", "Cover 1人盯人", "单高位安全卫")

    # 5 receivers
    receivers = [(150, 350), (250, 340), (550, 340), (650, 350), (400, 360)]
    for x, y in receivers:
        svg += add_receiver(x, y)

    # 4 defenders man coverage
    defenders = [(150, 300), (250, 290), (550, 290), (650, 300)]
    labels = ['CB', 'NB', 'NB', 'CB']
    for (x, y), label in zip(defenders, labels):
        svg += add_defender(x, y, label)

    # Free Safety deep middle
    svg += add_defender(400, 180, 'FS', 18)
    svg += add_zone(300, 100, 200, 120, '深中', "#ff4444")

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">人盯人 + 1个深区协防</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_one_robber():
    svg = svg_base("Cover One Robber", "Cover 1抢断式", "中区游走抢断")

    # Receivers
    for x, y in [(150, 350), (250, 340), (550, 340), (650, 350)]:
        svg += add_receiver(x, y)

    # Man coverage
    for x, y, label in [(150, 300, 'CB'), (250, 290, 'NB'), (550, 290, 'NB'), (650, 300, 'CB')]:
        svg += add_defender(x, y, label)

    # Free Safety
    svg += add_defender(400, 180, 'FS', 18)

    # Robber (LB lurking middle)
    svg += add_defender(400, 260, 'ROB', 18)
    svg += add_zone(320, 220, 160, 100, 'Robber', "#ffeb3b")

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">抢断者游走中区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_two_zone():
    svg = svg_base("Cover Two Zone", "Cover 2区域防守", "双高位安全卫")

    # Receivers
    for x, y in [(150, 350), (650, 350), (400, 360)]:
        svg += add_receiver(x, y)

    # 2 deep safeties
    svg += add_defender(280, 160, 'SS', 16)
    svg += add_defender(520, 160, 'FS', 16)
    svg += add_zone(150, 100, 240, 150, '深左', "#ff4444")
    svg += add_zone(410, 100, 240, 150, '深右', "#ff4444")

    # 5 underneath zones
    for x, label in [(150, 'CB'), (280, 'OLB'), (400, 'MLB'), (520, 'OLB'), (650, 'CB')]:
        svg += add_defender(x, 300, label, 14)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">2深区 + 5浅区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_two_man():
    svg = svg_base("Cover Two Man", "Cover 2人盯人", "双高位+人盯人")

    # Receivers
    for x, y in [(150, 350), (250, 340), (550, 340), (650, 350)]:
        svg += add_receiver(x, y)

    # Man coverage
    for x, y, label in [(150, 300, 'CB'), (250, 290, 'NB'), (550, 290, 'NB'), (650, 300, 'CB')]:
        svg += add_defender(x, y, label)

    # 2 deep safeties
    svg += add_defender(280, 160, 'SS', 16)
    svg += add_defender(520, 160, 'FS', 16)
    svg += add_zone(150, 100, 240, 150, '深左', "#ff4444")
    svg += add_zone(410, 100, 240, 150, '深右', "#ff4444")

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">2深区 + 人盯人</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_tampa_2():
    svg = svg_base("Tampa 2", "Tampa 2防守", "中线卫深区")

    # Receivers
    for x, y in [(150, 350), (650, 350), (400, 360)]:
        svg += add_receiver(x, y)

    # 2 safeties
    svg += add_defender(260, 160, 'SS', 16)
    svg += add_defender(540, 160, 'FS', 16)

    # MLB drops deep (Tampa 2 key)
    svg += add_defender(400, 200, 'MLB', 16)
    svg += '''
  <path d="M 400,320 L 400,220" stroke="#00ffff" stroke-width="3" marker-end="url(#arrow-cyan)"/>'''

    # Zones
    svg += add_zone(150, 100, 180, 150, '深左', "#ff4444")
    svg += add_zone(350, 100, 100, 150, '深中', "#00ffff")
    svg += add_zone(470, 100, 180, 150, '深右', "#ff4444")

    # Underneath
    for x, label in [(150, 'CB'), (280, 'OLB'), (520, 'OLB'), (650, 'CB')]:
        svg += add_defender(x, 300, label, 14)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">MLB后撤深中区</text>
  <defs>
    <marker id="arrow-cyan" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#00ffff"/>
    </marker>
  </defs>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_three():
    svg = svg_base("Cover Three", "Cover 3防守", "三深区防守")

    # Receivers
    for x, y in [(150, 350), (400, 360), (650, 350)]:
        svg += add_receiver(x, y)

    # 3 deep defenders
    svg += add_defender(200, 160, 'CB', 15)
    svg += add_defender(400, 160, 'FS', 15)
    svg += add_defender(600, 160, 'CB', 15)

    # 3 deep zones
    svg += add_zone(120, 100, 180, 150, '深左', "#ff4444")
    svg += add_zone(320, 100, 160, 150, '深中', "#ff4444")
    svg += add_zone(500, 100, 180, 150, '深右', "#ff4444")

    # 4 underneath
    for x, label in [(250, 'OLB'), (360, 'MLB'), (440, 'MLB'), (550, 'OLB')]:
        svg += add_defender(x, 300, label, 14)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">3深区 + 4浅区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_four():
    svg = svg_base("Cover Four (Quarters)", "Cover 4四分防守", "四深区防守")

    # Receivers
    for x, y in [(150, 350), (650, 350)]:
        svg += add_receiver(x, y)

    # 4 deep defenders
    for x, label in [(200, 'CB'), (340, 'SS'), (460, 'FS'), (600, 'CB')]:
        svg += add_defender(x, 160, label, 15)

    # 4 deep zones
    svg += add_zone(120, 100, 140, 150, '1/4', "#ff4444")
    svg += add_zone(280, 100, 120, 150, '1/4', "#ff4444")
    svg += add_zone(420, 100, 120, 150, '1/4', "#ff4444")
    svg += add_zone(560, 100, 120, 150, '1/4', "#ff4444")

    # 3 underneath
    for x, label in [(280, 'OLB'), (400, 'MLB'), (520, 'OLB')]:
        svg += add_defender(x, 300, label, 14)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">4个1/4深区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_six():
    svg = svg_base("Cover Six", "Cover 6混合防守", "半场人盯人半场区域")

    # Receivers
    for x, y in [(150, 350), (650, 350), (400, 360)]:
        svg += add_receiver(x, y)

    # Left side: Cover 2 (zone)
    svg += add_defender(200, 160, 'SS', 15)
    svg += add_zone(120, 100, 180, 150, 'C2左', "#ff4444")
    svg += add_defender(150, 300, 'CB', 14)

    # Right side: Cover 4 (quarters)
    svg += add_defender(500, 160, 'FS', 15)
    svg += add_defender(600, 160, 'CB', 15)
    svg += add_zone(450, 100, 120, 150, 'C4', "#00ffff")
    svg += add_zone(590, 100, 90, 150, 'C4', "#00ffff")

    # Middle
    for x, label in [(300, 'OLB'), (400, 'MLB'), (550, 'OLB')]:
        svg += add_defender(x, 300, label, 14)

    # Divider
    svg += '''
  <line x1="400" y1="100" x2="400" y2="380" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="8,4"/>
  <text x="250" y="130" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">Cover 2</text>
  <text x="550" y="130" text-anchor="middle" fill="#00ffff" font-size="12" font-weight="bold">Cover 4</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">左C2 + 右C4混合</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_two_buzz():
    svg = svg_base("Cover Two Buzz", "Cover 2冲锋式", "OLB冲锋SS下沉")

    # Receivers
    for x, y in [(150, 350), (650, 350), (400, 360)]:
        svg += add_receiver(x, y)

    # 2 deep safeties
    svg += add_defender(280, 160, 'SS', 16)
    svg += add_defender(520, 160, 'FS', 16)
    svg += add_zone(150, 100, 240, 150, '深左', "#ff4444")
    svg += add_zone(410, 100, 240, 150, '深右', "#ff4444")

    # OLB buzz (blitz)
    svg += add_defender(240, 340, 'BZ', 16)
    svg += '''
  <path d="M 240,320 L 240,365" stroke="#ffeb3b" stroke-width="3" marker-end="url(#arrow-yellow)"/>'''

    # Other defenders
    for x, label in [(150, 'CB'), (400, 'MLB'), (550, 'OLB'), (650, 'CB')]:
        svg += add_defender(x, 300, label, 14)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">OLB冲锋+SS替补</text>
  <defs>
    <marker id="arrow-yellow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ffeb3b"/>
    </marker>
  </defs>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_three_cloud():
    svg = svg_base("Cover Three Cloud", "Cover 3云式", "CB平层覆盖")

    # Receivers
    for x, y in [(150, 350), (650, 350), (400, 360)]:
        svg += add_receiver(x, y)

    # 3 deep
    svg += add_defender(200, 160, 'CB', 15)
    svg += add_defender(400, 160, 'FS', 15)
    svg += add_defender(600, 160, 'CB', 15)

    # Deep zones
    svg += add_zone(120, 100, 180, 150, '深', "#ff4444")
    svg += add_zone(320, 100, 160, 150, '深', "#ff4444")
    svg += add_zone(500, 100, 180, 150, '深', "#ff4444")

    # CBs also cover flats (cloud)
    svg += add_zone(100, 280, 100, 60, '云', "#00ffff")
    svg += add_zone(600, 280, 100, 60, '云', "#00ffff")

    # Underneath
    for x, label in [(280, 'OLB'), (400, 'MLB'), (520, 'OLB')]:
        svg += add_defender(x, 300, label, 14)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">CB兼顾深区和平层</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_three_buzz():
    svg = svg_base("Cover Three Buzz", "Cover 3冲锋式", "OLB冲锋SS替补")

    # Receivers
    for x, y in [(150, 350), (650, 350), (400, 360)]:
        svg += add_receiver(x, y)

    # 3 deep (SS replaces OLB)
    svg += add_defender(200, 160, 'CB', 15)
    svg += add_defender(400, 160, 'FS', 15)
    svg += add_defender(600, 160, 'SS', 15)

    # Deep zones
    svg += add_zone(120, 100, 180, 150, '深', "#ff4444")
    svg += add_zone(320, 100, 160, 150, '深', "#ff4444")
    svg += add_zone(500, 100, 180, 150, '深', "#ff4444")

    # OLB blitz
    svg += add_defender(560, 340, 'BZ', 16)
    svg += '''
  <path d="M 560,320 L 560,365" stroke="#ffeb3b" stroke-width="3" marker-end="url(#arrow-yellow2)"/>'''

    # Underneath
    for x, label in [(280, 'OLB'), (400, 'MLB'), (650, 'CB')]:
        svg += add_defender(x, 300, label, 14)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">OLB冲锋+SS深区替补</text>
  <defs>
    <marker id="arrow-yellow2" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ffeb3b"/>
    </marker>
  </defs>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

# === SAVE FUNCTION ===

def save_svg(filename, content):
    """Save SVG to file"""
    filepath = f'../assets/images/defense-coverage/{filename}'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

# === MAIN EXECUTION ===

def main():
    """Generate all coverage SVGs"""
    created = []

    coverages = {
        'cover-zero': create_cover_zero,
        'cover-one': create_cover_one,
        'cover-one-robber': create_cover_one_robber,
        'cover-two-zone': create_cover_two_zone,
        'cover-two-man': create_cover_two_man,
        'cover-two-buzz': create_cover_two_buzz,
        'tampa-2': create_tampa_2,
        'cover-three': create_cover_three,
        'cover-three-cloud': create_cover_three_cloud,
        'cover-three-buzz': create_cover_three_buzz,
        'cover-four-quarters': create_cover_four,
        'cover-six': create_cover_six
    }

    print("Creating defense coverage SVGs...")
    for name, generator in coverages.items():
        path = save_svg(f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal coverage SVGs created: {len(created)}")
    return len(created)

if __name__ == '__main__':
    count = main()
    print(f"\n{'='*50}")
    print(f"SUCCESS! Created {count} coverage SVG diagrams")
    print(f"{'='*50}")
