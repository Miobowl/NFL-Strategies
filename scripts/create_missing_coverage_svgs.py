#!/usr/bin/env python3
"""
Create SVG diagrams for missing defense coverage schemes (short IDs)
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

def svg_legend():
    return '''
  <!-- Legend -->
  <g transform="translate(50, 540)">
    <circle cx="0" cy="0" r="12" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
    <text x="18" y="5" fill="#ffffff" font-size="11">= 进攻</text>

    <circle cx="80" cy="0" r="12" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
    <text x="98" y="5" fill="#ffffff" font-size="11">= 防守</text>

    <rect x="160" y="-8" width="40" height="16" fill="#ff4444" opacity="0.2" stroke="#ff4444" stroke-width="1"/>
    <text x="210" y="5" fill="#ffffff" font-size="11">= 覆盖区</text>
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

# === COVERAGE GENERATORS ===

def create_cover_0():
    """Cover 0 - All man, no deep safety"""
    svg = svg_base("Cover 0", "Cover 0", "全场人盯人无安全卫")

    # 5 receivers
    receivers = [(150, 350), (250, 340), (550, 340), (650, 350), (400, 360)]
    for x, y in receivers:
        svg += add_receiver(x, y)

    # 5 defenders man coverage
    defenders = [(150, 300), (250, 290), (550, 290), (650, 300), (400, 310)]
    labels = ['CB', 'NB', 'NB', 'CB', 'LB']
    for (x, y), label in zip(defenders, labels):
        svg += add_defender(x, y, label)

    # Blitzers
    svg += add_defender(300, 320, 'BLZ', 18)
    svg += add_defender(500, 320, 'BLZ', 18)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">全人盯人 - 无安全卫深区协防</text>
  <text x="400" y="500" text-anchor="middle" fill="#00ffff" font-size="11">最激进的覆盖方式</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_1():
    """Cover 1 - Man with 1 deep safety"""
    svg = svg_base("Cover 1", "Cover 1", "人盯人+单高位安全卫")

    # Receivers
    for x, y in [(150, 350), (250, 340), (550, 340), (650, 350)]:
        svg += add_receiver(x, y)

    # Man coverage
    for x, y, label in [(150, 300, 'CB'), (250, 290, 'NB'), (550, 290, 'NB'), (650, 300, 'CB')]:
        svg += add_defender(x, y, label)

    # Free Safety deep middle
    svg += add_defender(400, 180, 'FS', 18)
    svg += add_zone(300, 100, 200, 120, '深中', "#ff4444")

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">人盯人 + 1个深区安全卫</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_2():
    """Cover 2 - 2 deep safeties"""
    svg = svg_base("Cover 2", "Cover 2", "双高位安全卫")

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
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">2个深区安全卫 + 5个浅区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_3():
    """Cover 3 - 3 deep zones"""
    svg = svg_base("Cover 3", "Cover 3", "三深区防守")

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
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">3个深区 + 4个浅区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_4():
    """Cover 4 - Quarters coverage"""
    svg = svg_base("Cover 4", "Cover 4", "四分防守")

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
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">4个1/4深区防守</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_cover_6():
    """Cover 6 - Split field coverage"""
    svg = svg_base("Cover 6", "Cover 6", "半场人盯人半场区域")

    # Receivers
    for x, y in [(150, 350), (650, 350), (400, 360)]:
        svg += add_receiver(x, y)

    # Left side: Cover 2 (zone)
    svg += add_defender(200, 160, 'SS', 15)
    svg += add_zone(120, 100, 180, 150, 'C2', "#ff4444")
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
  <text x="400" y="480" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">左C2 + 右C4混合防守</text>'''

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
    """Generate missing coverage SVGs"""
    created = []

    coverages = {
        'cover-0': create_cover_0,
        'cover-1': create_cover_1,
        'cover-2': create_cover_2,
        'cover-3': create_cover_3,
        'cover-4': create_cover_4,
        'cover-6': create_cover_6
    }

    print("Creating missing defense coverage SVGs...")
    for name, generator in coverages.items():
        path = save_svg(f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal missing coverage SVGs created: {len(created)}")
    return len(created)

if __name__ == '__main__':
    count = main()
    print(f"\n{'='*50}")
    print(f"SUCCESS! Created {count} missing coverage SVG diagrams")
    print(f"{'='*50}")
