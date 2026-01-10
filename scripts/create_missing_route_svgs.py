#!/usr/bin/env python3
"""
Create SVG diagrams for missing passing routes
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

def create_go_route():
    svg = svg_base("Go Route (Fly)", "直线冲刺路线", "全速直线深入")

    svg += add_receiver_start(650, 400)

    # Straight vertical route
    svg += '''
  <path d="M 650,385 L 650,120" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(650, 120)

    # Distance marker
    svg += '''
  <line x1="630" y1="400" x2="630" y2="120" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="610" y="260" fill="#ffeb3b" font-size="12" font-weight="bold">20+码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">全速直线深入边线</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">速度型接球手</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_slant_route():
    svg = svg_base("Slant Route", "斜插路线", "向内斜切45度")

    svg += add_receiver_start(650, 400)

    # Slant route (45 degree angle)
    svg += '''
  <path d="M 650,385 L 650,350 L 500,280" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(500, 280)

    # Angle indicator
    svg += '''
  <path d="M 650,350 L 670,350 L 670,330" stroke="#ffeb3b" stroke-width="1" opacity="0.5"/>
  <text x="680" y="340" fill="#ffeb3b" font-size="10">45°</text>'''

    # Distance
    svg += '''
  <line x1="630" y1="400" x2="630" y2="280" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="610" y="340" fill="#ffeb3b" font-size="12" font-weight="bold">5-8码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">向前5码后斜切内侧</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">快速传球首选</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_out_route():
    svg = svg_base("Out Route", "外切路线", "直冲后外切")

    svg += add_receiver_start(500, 400)

    # Out route
    svg += '''
  <path d="M 500,385 L 500,300 L 620,300" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(620, 300)

    # 90 degree indicator
    svg += '''
  <rect x="500" y="300" width="15" height="15" fill="none" stroke="#ffeb3b" stroke-width="1" opacity="0.5"/>
  <text x="520" y="320" fill="#ffeb3b" font-size="10">90°</text>'''

    # Distance markers
    svg += '''
  <line x1="480" y1="400" x2="480" y2="300" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="460" y="350" fill="#ffeb3b" font-size="12" font-weight="bold">8-12码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">向前8-12码后外切</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">攻击平层防守</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_post_route():
    svg = svg_base("Post Route", "中柱路线", "深入后切向球门柱")

    svg += add_receiver_start(650, 400)

    # Post route (angle toward goal post)
    svg += '''
  <path d="M 650,385 L 650,250 L 480,140" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(480, 140)

    # Goal post indicator
    svg += '''
  <line x1="400" y1="0" x2="400" y2="100" stroke="#ffeb3b" stroke-width="3" opacity="0.5"/>
  <text x="410" y="60" fill="#ffeb3b" font-size="11">球门柱</text>'''

    # Distance
    svg += '''
  <line x1="630" y1="400" x2="630" y2="140" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="610" y="270" fill="#ffeb3b" font-size="12" font-weight="bold">15-20码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">深入后斜切向球门柱</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">攻击深中区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_corner_route():
    svg = svg_base("Corner Route", "角落路线", "深入后外切角落")

    svg += add_receiver_start(550, 400)

    # Corner route
    svg += '''
  <path d="M 550,385 L 550,220 L 680,160" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(680, 160)

    # Corner zone highlight
    svg += '''
  <rect x="600" y="100" width="120" height="100" fill="#ffeb3b" opacity="0.1" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="660" y="150" text-anchor="middle" fill="#ffeb3b" font-size="11">角落区</text>'''

    # Distance
    svg += '''
  <line x1="530" y1="400" x2="530" y2="160" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="510" y="280" fill="#ffeb3b" font-size="12" font-weight="bold">15码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">深入15码后外切角落</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">攻击边线深区</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_curl_route():
    svg = svg_base("Curl Route", "回卷路线", "深入后回转面向QB")

    svg += add_receiver_start(650, 400)

    # Curl route
    svg += '''
  <path d="M 650,385 L 650,240" stroke="#00ffff" stroke-width="4" fill="none"/>
  <circle cx="650" cy="240" r="12" fill="#ff6b35" opacity="0.5"/>
  <path d="M 650,228 L 650,270" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>
  <text x="670" y="250" fill="#ff6b35" font-size="10">转身</text>'''

    svg += add_receiver_end(650, 270)

    # Distance
    svg += '''
  <line x1="630" y1="400" x2="630" y2="240" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="610" y="320" fill="#ffeb3b" font-size="12" font-weight="bold">10-15码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">深入10-15码回转面向QB</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">找空当坐下</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_drag_route():
    svg = svg_base("Drag Route", "拖曳路线", "浅层横向拖曳")

    svg += add_receiver_start(200, 400)

    # Drag route (shallow cross)
    svg += '''
  <path d="M 200,385 L 200,350 L 580,320" stroke="#00ffff" stroke-width="4" fill="none" marker-end="url(#route-arrow)"/>'''

    svg += add_receiver_end(580, 320)

    # Dragging zone
    svg += '''
  <rect x="180" y="310" width="420" height="50" fill="#ffeb3b" opacity="0.1" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="400" y="365" text-anchor="middle" fill="#ffeb3b" font-size="11">拖曳层</text>'''

    # Distance
    svg += '''
  <line x1="180" y1="400" x2="180" y2="320" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="3,3" opacity="0.6"/>
  <text x="160" y="360" fill="#ffeb3b" font-size="12" font-weight="bold">3-5码</text>'''

    svg += '''
  <text x="400" y="480" text-anchor="middle" fill="#ffffff" font-size="12">浅层横向穿越场地</text>
  <text x="400" y="500" text-anchor="middle" fill="#ffeb3b" font-size="11">拖出线卫制造空当</text>'''

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
    """Generate missing route SVGs"""
    created = []

    routes = {
        'go-route': create_go_route,
        'slant-route': create_slant_route,
        'out-route': create_out_route,
        'post-route': create_post_route,
        'corner-route': create_corner_route,
        'curl-route': create_curl_route,
        'drag-route': create_drag_route
    }

    print("Creating missing passing route SVGs...")
    for name, generator in routes.items():
        path = save_svg(f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal missing route SVGs created: {len(created)}")
    return len(created)

if __name__ == '__main__':
    count = main()
    print(f"\n{'='*50}")
    print(f"SUCCESS! Created {count} missing route SVG diagrams")
    print(f"{'='*50}")
