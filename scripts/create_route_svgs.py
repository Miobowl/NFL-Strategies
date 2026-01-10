#!/usr/bin/env python3
"""
Create detailed SVG diagrams for all passing routes
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
    <marker id="route-arrow" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#00ffff"/>
    </marker>
  </defs>'''

def add_receiver_start(x, y):
    """Receiver starting position"""
    return f'''
  <circle cx="{x}" cy="{y}" r="14" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+5}" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">WR</text>'''

def add_receiver_end(x, y):
    """Receiver ending position"""
    return f'''
  <circle cx="{x}" cy="{y}" r="12" fill="#00ffff" stroke="#ffffff" stroke-width="2" opacity="0.7"/>'''

def svg_legend():
    return '''
  <!-- Legend -->
  <g transform="translate(50, 540)">
    <circle cx="0" cy="0" r="12" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
    <text x="18" y="5" fill="#ffffff" font-size="11">= 起始位置</text>

    <line x1="100" y1="0" x2="150" y2="0" stroke="#00ffff" stroke-width="3" marker-end="url(#route-arrow)"/>
    <text x="160" y="5" fill="#ffffff" font-size="11">= 路线</text>

    <circle cx="250" cy="0" r="10" fill="#00ffff" stroke="#ffffff" stroke-width="2" opacity="0.7"/>
    <text x="268" y="5" fill="#ffffff" font-size="11">= 接球点</text>
  </g>'''

def close_svg():
    return '\n</svg>'

# === ROUTE GENERATORS ===

def create_flat_route():
    svg = svg_base("Flat Route", "平层路线", "短距离横向路线")

    # Starting position
    svg += add_receiver_start(600, 400)

    # Route path
    svg += '''
  <path d="M 600,385 L 600,340 L 500,340" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    # End position
    svg += add_receiver_end(500, 340)

    # Labels
    svg += '''
  <text x="550" y="320" text-anchor="middle" fill="#00ffff" font-size="14" font-weight="bold">Flat</text>
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">向内3-5码后横向</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">快速短传选择</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_comeback_route():
    svg = svg_base("Comeback Route", "回马枪路线", "深入后回转")

    svg += add_receiver_start(650, 400)

    # Route path
    svg += '''
  <path d="M 650,385 L 650,180 L 680,180" stroke="#00ffff" stroke-width="4" fill="none"/>
  <circle cx="680" cy="180" r="8" fill="#00ffff" opacity="0.5"/>
  <path d="M 680,180 L 650,200" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(650, 200)

    # Distance marker
    svg += '''
  <line x1="630" y1="400" x2="630" y2="200" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="610" y="300" fill="#ffeb3b" font-size="12" font-weight="bold">12-15码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">深入12-15码后回转</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">对抗软区防守</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_hitch_route():
    svg = svg_base("Hitch Route", "急停路线", "快速急停回身")

    svg += add_receiver_start(650, 400)

    # Route path
    svg += '''
  <path d="M 650,385 L 650,320" stroke="#00ffff" stroke-width="4" fill="none"/>
  <circle cx="650" cy="320" r="10" fill="#ff6b35" opacity="0.7"/>
  <path d="M 650,320 L 650,340" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(650, 340)

    # Distance marker
    svg += '''
  <line x1="630" y1="400" x2="630" y2="340" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="610" y="370" fill="#ffeb3b" font-size="12" font-weight="bold">5-8码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">向前5-8码急停回身</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">最快速的传球选择</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_dig_route():
    svg = svg_base("Dig Route", "挖掘路线", "深入后内切")

    svg += add_receiver_start(650, 400)

    # Route path
    svg += '''
  <path d="M 650,385 L 650,250 L 400,250" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(400, 250)

    # Distance marker
    svg += '''
  <line x1="630" y1="400" x2="630" y2="250" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="610" y="325" fill="#ffeb3b" font-size="12" font-weight="bold">10-15码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">深入10-15码后内切</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">攻击中区弱点</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_wheel_route():
    svg = svg_base("Wheel Route", "轮式路线", "弧线深入")

    svg += add_receiver_start(620, 400)

    # Route path (wheel curve)
    svg += '''
  <path d="M 620,385 Q 550,350 500,340 Q 450,330 450,250 L 450,150" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(450, 150)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">弧线向内后深入边线</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">跑卫常用路线</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_seam_route():
    svg = svg_base("Seam Route", "接缝路线", "攻击深中接缝")

    svg += add_receiver_start(500, 400)

    # Route path
    svg += '''
  <path d="M 500,385 L 450,350 L 420,130" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(420, 130)

    # Seam zone highlight
    svg += '''
  <rect x="350" y="100" width="100" height="250" fill="#ffeb3b" opacity="0.15" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="400" y="220" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">接缝区</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">攻击安全卫之间的接缝</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">TE和Slot常用</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_option_route():
    svg = svg_base("Option Route", "选择路线", "读防守决定")

    svg += add_receiver_start(600, 400)

    # Decision point
    svg += '''
  <circle cx="600" cy="300" r="16" fill="#ff6b35" opacity="0.7"/>
  <text x="600" y="305" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">?</text>'''

    # Option A: Inside
    svg += '''
  <path d="M 600,385 L 600,315" stroke="#00ffff" stroke-width="3" fill="none"/>
  <path d="M 600,285 L 500,250" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#route-arrow)" opacity="0.7"/>
  <text x="540" y="240" fill="#00ffff" font-size="11">选项A</text>'''

    # Option B: Outside
    svg += '''
  <path d="M 600,285 L 680,250" stroke="#00ffff" stroke-width="3" fill="none" marker-end="url(#route-arrow)" opacity="0.7"/>
  <text x="660" y="240" fill="#00ffff" font-size="11">选项B</text>'''

    svg += add_receiver_end(500, 250)
    svg += add_receiver_end(680, 250)

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">根据防守覆盖做出选择</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">WR和QB需默契</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_stop_and_go():
    svg = svg_base("Stop and Go", "急停再启动", "假装急停后深入")

    svg += add_receiver_start(650, 400)

    # Route with fake stop
    svg += '''
  <path d="M 650,385 L 650,320" stroke="#00ffff" stroke-width="4" fill="none"/>
  <circle cx="650" cy="320" r="12" fill="#ff6b35" opacity="0.7"/>
  <text x="650" y="325" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">假停</text>
  <path d="M 650,308 L 650,140" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(650, 140)

    # Distance markers
    svg += '''
  <line x1="630" y1="400" x2="630" y2="320" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.4"/>
  <text x="610" y="360" fill="#ffeb3b" font-size="10">5-7码</text>
  <line x1="670" y1="320" x2="670" y2="140" stroke="#00ffff" stroke-width="2" stroke-dasharray="3,3" opacity="0.4"/>
  <text x="690" y="230" fill="#00ffff" font-size="10">深入</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">假装Hitch后深入</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">欺骗性路线</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

# === SAVE FUNCTION ===

def save_svg(filename, content):
    """Save SVG to file"""
    filepath = f'../assets/images/passing-routes/{filename}'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

# === MAIN EXECUTION ===

def main():
    """Generate all route SVGs"""
    created = []

    routes = {
        'flat-route': create_flat_route,
        'comeback-route': create_comeback_route,
        'hitch-route': create_hitch_route,
        'dig-route': create_dig_route,
        'wheel-route': create_wheel_route,
        'seam-route': create_seam_route,
        'option-route': create_option_route,
        'stop-and-go': create_stop_and_go
    }

    print("Creating passing route SVGs...")
    for name, generator in routes.items():
        path = save_svg(f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal route SVGs created: {len(created)}")
    return len(created)

if __name__ == '__main__':
    count = main()
    print(f"\n{'='*50}")
    print(f"SUCCESS! Created {count} route SVG diagrams")
    print(f"{'='*50}")
