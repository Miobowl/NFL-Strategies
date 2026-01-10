#!/usr/bin/env python3
"""
Batch create detailed SVG diagrams for all tactics
"""

import os

# Common SVG components
def svg_header(title_en, title_cn, subtitle=""):
    """Create SVG header with title"""
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
  </text>'''

def svg_los(y=350):
    """Line of scrimmage"""
    return f'''
  <!-- Line of Scrimmage -->
  <line x1="100" y1="{y}" x2="700" y2="{y}" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>
  <text x="50" y="{y+5}" fill="#ffeb3b" font-size="14" font-weight="bold">LOS</text>'''

def svg_oline(y=350):
    """Standard 5-man offensive line"""
    return f'''
  <!-- Offensive Line -->
  <circle cx="250" cy="{y}" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="250" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">LT</text>

  <circle cx="320" cy="{y}" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="320" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">LG</text>

  <circle cx="400" cy="{y}" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">C</text>

  <circle cx="480" cy="{y}" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="480" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RG</text>

  <circle cx="550" cy="{y}" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="550" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RT</text>'''

def svg_qb(x=400, y=390, size=22):
    """Quarterback"""
    return f'''
  <!-- Quarterback -->
  <circle cx="{x}" cy="{y}" r="{size}" fill="#ff6b35" stroke="#ffffff" stroke-width="3"/>
  <text x="{x}" y="{y+8}" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">QB</text>'''

def svg_legend():
    """Legend"""
    return '''
  <!-- Legend -->
  <g transform="translate(50, 540)">
    <circle cx="0" cy="0" r="14" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
    <text x="20" y="5" fill="#ffffff" font-size="12">= 进攻</text>

    <circle cx="100" cy="0" r="14" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
    <text x="120" y="5" fill="#ffffff" font-size="12">= 防守</text>
  </g>'''

# SVG Templates for each formation type
FORMATIONS = {
    'pistol': lambda: f'''{svg_header("Pistol Formation", "手枪阵型", "QB后方3-4码")}
{svg_los(350)}
{svg_oline(350)}
{svg_qb(400, 410, 22)}

  <!-- Distance marker -->
  <line x1="390" y1="355" x2="390" y2="405" stroke="#00ffff" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="350" y="385" fill="#00ffff" font-size="12" font-weight="bold">3-4码</text>

  <!-- Running Back behind QB -->
  <circle cx="400" cy="460" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="467" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RB</text>

  <!-- Wide Receivers -->
  <circle cx="120" cy="350" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="120" y="356" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">WR</text>

  <circle cx="680" cy="350" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="680" y="356" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">WR</text>

  <!-- Key Features -->
  <g transform="translate(540, 130)">
    <rect x="-10" y="-10" width="240" height="130" fill="#000000" opacity="0.85" rx="8"/>
    <text x="0" y="10" fill="#ffffff" font-size="13" font-weight="bold">Pistol 要点:</text>
    <text x="0" y="30" fill="#ffffff" font-size="10">✓ 结合Shotgun视野</text>
    <text x="0" y="46" fill="#ffffff" font-size="10">✓ 保留I型下坡冲力</text>
    <text x="0" y="62" fill="#ffffff" font-size="10">✓ 适合Zone Read战术</text>
    <text x="0" y="78" fill="#ffffff" font-size="10">✓ 需要移动型QB</text>
    <text x="0" y="94" fill="#ffffff" font-size="10">✓ 现代创新阵型</text>
  </g>
{svg_legend()}
</svg>''',

    'spread': lambda: f'''{svg_header("Spread Formation", "展开阵型", "4外接手强迫防守展开")}
{svg_los(350)}
{svg_oline(350)}
{svg_qb(400, 430, 22)}

  <!-- Running Back -->
  <circle cx="450" cy="430" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="450" y="437" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RB</text>

  <!-- 4 Wide Receivers spread out -->
  <circle cx="100" cy="350" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="100" y="356" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">WR</text>

  <circle cx="180" cy="360" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="180" y="366" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">SL</text>

  <circle cx="620" cy="360" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="620" y="366" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">SL</text>

  <circle cx="700" cy="350" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="700" y="356" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">WR</text>

  <!-- Width indicators -->
  <line x1="100" y1="330" x2="700" y2="330" stroke="#00ffff" stroke-width="2" stroke-dasharray="5,5" opacity="0.5"/>
  <text x="400" y="310" text-anchor="middle" fill="#00ffff" font-size="12">全场宽度展开</text>

  <!-- Key Features -->
  <g transform="translate(540, 140)">
    <rect x="-10" y="-10" width="240" height="120" fill="#000000" opacity="0.85" rx="8"/>
    <text x="0" y="10" fill="#ffffff" font-size="13" font-weight="bold">Spread 要点:</text>
    <text x="0" y="30" fill="#ffffff" font-size="10">✓ 4-5个接球手</text>
    <text x="0" y="46" fill="#ffffff" font-size="10">✓ 强迫防守展开</text>
    <text x="0" y="62" fill="#ffffff" font-size="10">✓ 创造1对1机会</text>
    <text x="0" y="78" fill="#ffffff" font-size="10">⚠ 保护QB压力大</text>
  </g>
{svg_legend()}
</svg>''',

    'wildcat': lambda: f'''{svg_header("Wildcat Formation", "野猫阵型", "直接开球给RB")}
{svg_los(350)}
{svg_oline(350)}

  <!-- Direct snap to RB -->
  <circle cx="400" cy="410" r="24" fill="#4a90e2" stroke="#00ff00" stroke-width="3"/>
  <text x="400" y="418" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">RB</text>

  <!-- Snap arrow -->
  <defs>
    <marker id="snapArrow" markerWidth="10" markerHeight="10" refX="9" refY="3" orient="auto">
      <polygon points="0 0, 10 3, 0 6" fill="#00ff00"/>
    </marker>
  </defs>
  <line x1="400" y1="360" x2="400" y2="390" stroke="#00ff00" stroke-width="3" marker-end="url(#snapArrow)"/>
  <text x="420" y="380" fill="#00ff00" font-size="11" font-weight="bold">直接开球</text>

  <!-- QB/WR position (optional) -->
  <circle cx="180" cy="360" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="180" y="366" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">WR</text>

  <circle cx="620" cy="360" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="620" y="366" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">WR</text>

  <!-- Fullback -->
  <circle cx="350" cy="440" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="350" y="447" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">FB</text>

  <!-- Key Features -->
  <g transform="translate(540, 140)">
    <rect x="-10" y="-10" width="240" height="120" fill="#000000" opacity="0.85" rx="8"/>
    <text x="0" y="10" fill="#ffffff" font-size="13" font-weight="bold">Wildcat 要点:</text>
    <text x="0" y="30" fill="#ffffff" font-size="10">✓ RB直接接球</text>
    <text x="0" y="46" fill="#ffffff" font-size="10">✓ 多一个阻挡者</text>
    <text x="0" y="62" fill="#ffffff" font-size="10">✓ 出其不意</text>
    <text x="0" y="78" fill="#ffffff" font-size="10">⚠ 传球能力有限</text>
  </g>
{svg_legend()}
</svg>''',
}

# Defensive formations
DEF_FORMATIONS = {
    'nickel-formation': lambda: f'''{svg_header("Nickel Defense", "镍币防守", "5后卫专防传球")}
{svg_los(400)}

  <!-- D-Line (4) -->
  <circle cx="280" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="280" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DE</text>

  <circle cx="360" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="360" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DT</text>

  <circle cx="440" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="440" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DT</text>

  <circle cx="520" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="520" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DE</text>

  <!-- Linebackers (2) -->
  <circle cx="340" cy="310" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="340" y="316" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">LB</text>

  <circle cx="460" cy="310" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="460" y="316" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">LB</text>

  <!-- DBs (5) - Nickel package -->
  <circle cx="180" cy="340" r="16" fill="#ff4444" stroke="#ffeb3b" stroke-width="2"/>
  <text x="180" y="346" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">CB</text>

  <circle cx="280" cy="260" r="16" fill="#ff4444" stroke="#ffeb3b" stroke-width="2"/>
  <text x="280" y="266" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">NI</text>
  <text x="280" y="245" fill="#ffeb3b" font-size="10">镍币CB</text>

  <circle cx="400" cy="220" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="226" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">FS</text>

  <circle cx="520" cy="260" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="520" y="266" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">SS</text>

  <circle cx="620" cy="340" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="620" y="346" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">CB</text>

  <!-- Formation label -->
  <g transform="translate(580, 480)">
    <rect x="0" y="0" width="200" height="80" fill="#000000" opacity="0.8" rx="8" stroke="#ffeb3b" stroke-width="2"/>
    <text x="100" y="30" text-anchor="middle" fill="#ffeb3b" font-size="28" font-weight="bold">4-2-5</text>
    <text x="100" y="55" text-anchor="middle" fill="#ffffff" font-size="14">Nickel Defense</text>
  </g>

  <!-- Key Features -->
  <g transform="translate(50, 100)">
    <rect x="-10" y="-10" width="260" height="130" fill="#000000" opacity="0.85" rx="8"/>
    <text x="0" y="10" fill="#ffffff" font-size="13" font-weight="bold">Nickel 要点:</text>
    <text x="0" y="30" fill="#ffffff" font-size="10">✓ 5后卫专防槽位接球手</text>
    <text x="0" y="46" fill="#ffffff" font-size="10">✓ NFL 65%战术使用</text>
    <text x="0" y="62" fill="#ffffff" font-size="10">✓ 应对3外接手阵型</text>
    <text x="0" y="78" fill="#ffffff" font-size="10">⚠ 防跑相对较弱</text>
  </g>
{svg_legend()}
</svg>''',

    'dime-formation': lambda: f'''{svg_header("Dime Defense", "一角硬币防守", "6后卫终极传球防守")}
{svg_los(400)}

  <!-- D-Line (4) -->
  <circle cx="280" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="280" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DE</text>

  <circle cx="360" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="360" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DT</text>

  <circle cx="440" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="440" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DT</text>

  <circle cx="520" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="520" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DE</text>

  <!-- MLB (1) -->
  <circle cx="400" cy="320" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="326" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">MLB</text>

  <!-- DBs (6) - Dime package -->
  <circle cx="160" cy="340" r="16" fill="#ff4444" stroke="#ffeb3b" stroke-width="2"/>
  <text x="160" y="346" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">CB</text>

  <circle cx="260" cy="280" r="16" fill="#ff4444" stroke="#ffeb3b" stroke-width="2"/>
  <text x="260" y="286" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">NI</text>

  <circle cx="320" cy="220" r="16" fill="#ff4444" stroke="#ffeb3b" stroke-width="2"/>
  <text x="320" y="226" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">SS</text>

  <circle cx="480" cy="220" r="16" fill="#ff4444" stroke="#ffeb3b" stroke-width="2"/>
  <text x="480" y="226" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">FS</text>

  <circle cx="540" cy="280" r="16" fill="#ff4444" stroke="#ffeb3b" stroke-width="2"/>
  <text x="540" y="286" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">DI</text>
  <text x="540" y="265" fill="#ffeb3b" font-size="9">Dime</text>

  <circle cx="640" cy="340" r="16" fill="#ff4444" stroke="#ffeb3b" stroke-width="2"/>
  <text x="640" y="346" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">CB</text>

  <!-- Formation label -->
  <g transform="translate(580, 480)">
    <rect x="0" y="0" width="200" height="80" fill="#000000" opacity="0.8" rx="8" stroke="#ffeb3b" stroke-width="2"/>
    <text x="100" y="30" text-anchor="middle" fill="#ffeb3b" font-size="28" font-weight="bold">4-1-6</text>
    <text x="100" y="55" text-anchor="middle" fill="#ffffff" font-size="14">Dime Defense</text>
  </g>

  <!-- Key Features -->
  <g transform="translate(50, 110)">
    <rect x="-10" y="-10" width="260" height="120" fill="#000000" opacity="0.85" rx="8"/>
    <text x="0" y="10" fill="#ffffff" font-size="13" font-weight="bold">Dime 要点:</text>
    <text x="0" y="30" fill="#ffffff" font-size="10">✓ 6后卫覆盖所有接球手</text>
    <text x="0" y="46" fill="#ffffff" font-size="10">✓ 3rd & long专用</text>
    <text x="0" y="62" fill="#ffffff" font-size="10">✓ 两分钟防守</text>
    <text x="0" y="78" fill="#ffffff" font-size="10">⚠ 极弱防跑</text>
  </g>
{svg_legend()}
</svg>''',
}

def save_svg(category, filename, content):
    """Save SVG file"""
    filepath = f'../assets/images/{category}/{filename}'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

def main():
    """Generate all detailed SVGs"""
    created = []

    print("Creating detailed offensive formation SVGs...")
    for name, generator in FORMATIONS.items():
        path = save_svg('offense-formation', f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print("\nCreating detailed defensive formation SVGs...")
    for name, generator in DEF_FORMATIONS.items():
        path = save_svg('defense-formation', f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal detailed SVGs created: {len(created)}")
    return len(created)

if __name__ == '__main__':
    count = main()
    print(f"\n{'='*50}")
    print(f"SUCCESS! Created {count} detailed SVG diagrams")
    print(f"{'='*50}")
