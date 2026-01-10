#!/usr/bin/env python3
"""
Create SVG diagrams for missing offensive formations
"""

import os

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
    """Line of Scrimmage"""
    return f'''
  <!-- Line of Scrimmage -->
  <line x1="100" y1="{y}" x2="700" y2="{y}" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>
  <text x="50" y="{y+5}" fill="#ffeb3b" font-size="14" font-weight="bold">LOS</text>'''

def svg_oline(y=350):
    """5-man offensive line"""
    positions = [(250, 'LT'), (320, 'LG'), (400, 'C'), (480, 'RG'), (550, 'RT')]
    svg = '\n  <!-- Offensive Line -->'
    for x, label in positions:
        svg += f'''
  <circle cx="{x}" cy="{y}" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">{label}</text>'''
    return svg

def svg_qb(x=400, y=390, size=22):
    """Quarterback"""
    return f'''
  <!-- Quarterback -->
  <circle cx="{x}" cy="{y}" r="{size}" fill="#ff6b35" stroke="#ffffff" stroke-width="3"/>
  <text x="{x}" y="{y+8}" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">QB</text>'''

def svg_rb(x, y, label='RB', size=20):
    """Running back"""
    return f'''
  <circle cx="{x}" cy="{y}" r="{size}" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">{label}</text>'''

def svg_wr(x, y, size=18):
    """Wide receiver"""
    return f'''
  <circle cx="{x}" cy="{y}" r="{size}" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+6}" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">WR</text>'''

def svg_te(x, y, size=18):
    """Tight end"""
    return f'''
  <circle cx="{x}" cy="{y}" r="{size}" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+6}" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">TE</text>'''

def svg_legend():
    return '''
  <!-- Legend -->
  <g transform="translate(50, 540)">
    <circle cx="0" cy="0" r="14" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
    <text x="20" y="5" fill="#ffffff" font-size="12">= 进攻</text>

    <circle cx="100" cy="0" r="14" fill="#ff6b35" stroke="#ffffff" stroke-width="2"/>
    <text x="120" y="5" fill="#ffffff" font-size="12">= 四分卫</text>
  </g>'''

def close_svg():
    return '\n</svg>'

# === FORMATION GENERATORS ===

def create_shotgun_formation():
    """Same as shotgun.svg but with id shotgun-formation"""
    svg = svg_header("Shotgun Formation", "霰弹枪阵型", "QB后方5-7码接球")
    svg += svg_los(350)
    svg += svg_oline(350)
    svg += svg_qb(400, 430, 24)

    # Distance indicator
    svg += '''
  <line x1="390" y1="355" x2="390" y2="425" stroke="#00ffff" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="350" y="390" fill="#00ffff" font-size="12" font-weight="bold">5-7码</text>'''

    # RB
    svg += svg_rb(450, 430, 'RB')

    # WRs and TE
    svg += svg_wr(120, 350)
    svg += svg_wr(680, 350)
    svg += svg_te(620, 360)

    svg += '''
  <text x="400" y="490" text-anchor="middle" fill="#ffeb3b" font-size="12">QB深位接球 - 更好视野</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_i_formation():
    svg = svg_header("I Formation", "I字阵型", "经典跑球阵型")
    svg += svg_los(400)
    svg += svg_oline(400)
    svg += svg_qb(400, 440)

    # I formation (QB, FB, RB in line)
    svg += svg_rb(400, 490, 'FB')
    svg += svg_rb(400, 530, 'RB')

    # I shape indicator
    svg += '''
  <line x1="390" y1="450" x2="390" y2="540" stroke="#00ffff" stroke-width="3" stroke-dasharray="5,5" opacity="0.6"/>
  <text x="360" y="495" fill="#00ffff" font-size="14" font-weight="bold">I字形</text>'''

    # WRs
    svg += svg_wr(150, 400)
    svg += svg_wr(650, 400)

    svg += '''
  <text x="400" y="560" text-anchor="middle" fill="#ffffff" font-size="12">三人直线排列</text>
  <text x="400" y="580" text-anchor="middle" fill="#ffeb3b" font-size="11">FB领路阻挡</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_spread_offense():
    svg = svg_header("Spread Offense", "展开进攻", "4-5个外接手")
    svg += svg_los(350)
    svg += svg_oline(350)
    svg += svg_qb(400, 430, 24)

    # Spread out receivers
    svg += svg_wr(120, 350)
    svg += svg_wr(280, 360)
    svg += svg_wr(520, 360)
    svg += svg_wr(680, 350)

    # RB as receiver
    svg += '''
  <circle cx="460" cy="430" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="460" y="436" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">RB</text>'''

    # Spread indicator
    svg += '''
  <line x1="120" y1="330" x2="680" y2="330" stroke="#00ffff" stroke-width="2" stroke-dasharray="5,5" opacity="0.5"/>
  <text x="400" y="320" text-anchor="middle" fill="#00ffff" font-size="13">横向展开</text>'''

    svg += '''
  <text x="400" y="490" text-anchor="middle" fill="#ffffff" font-size="12">4-5个接球手展开</text>
  <text x="400" y="510" text-anchor="middle" fill="#ffeb3b" font-size="11">拉开防守空间</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_singleback_formation():
    svg = svg_header("Singleback Formation", "单后卫阵型", "1RB多变化")
    svg += svg_los(400)
    svg += svg_oline(400)
    svg += svg_qb(400, 440)
    svg += svg_rb(400, 490, 'RB')

    # TE and WRs
    svg += svg_te(620, 400)
    svg += svg_wr(150, 400)
    svg += svg_wr(680, 400)

    # Slot
    svg += '''
  <circle cx="560" cy="410" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="560" y="416" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">SL</text>'''

    svg += '''
  <text x="400" y="525" text-anchor="middle" fill="#ffffff" font-size="12">单后卫多接球手</text>
  <text x="400" y="545" text-anchor="middle" fill="#ffeb3b" font-size="11">传跑平衡</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_pistol_formation():
    """Same as pistol but with id pistol-formation"""
    svg = svg_header("Pistol Formation", "手枪阵型", "QB中距离RB后方")
    svg += svg_los(350)
    svg += svg_oline(350)
    svg += svg_qb(400, 410, 22)

    # RB directly behind QB (pistol key)
    svg += svg_rb(400, 460, 'RB')

    # Distance indicator
    svg += '''
  <line x1="380" y1="355" x2="380" y2="405" stroke="#00ffff" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="350" y="380" fill="#00ffff" font-size="12" font-weight="bold">3码</text>'''

    # WRs
    svg += svg_wr(150, 350)
    svg += svg_wr(650, 350)
    svg += svg_te(590, 360)

    svg += '''
  <text x="400" y="495" text-anchor="middle" fill="#ffffff" font-size="12">QB中距离+RB后方</text>
  <text x="400" y="515" text-anchor="middle" fill="#ffeb3b" font-size="11">Shotgun和Under Center混合</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_empty_backfield():
    svg = svg_header("Empty Backfield", "空后场阵型", "无跑卫全接球手")
    svg += svg_los(350)
    svg += svg_oline(350)
    svg += svg_qb(400, 430, 24)

    # 5 receivers, no RB
    svg += svg_wr(120, 350)
    svg += svg_wr(280, 360)
    svg += svg_wr(520, 360)
    svg += svg_wr(680, 350)
    svg += svg_te(600, 365)

    # Empty backfield indicator
    svg += '''
  <rect x="350" y="450" width="100" height="80" fill="none" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="400" y="490" text-anchor="middle" fill="#ffeb3b" font-size="13" font-weight="bold">空后场</text>'''

    svg += '''
  <text x="400" y="540" text-anchor="middle" fill="#ffffff" font-size="12">5个接球手 - 无跑卫</text>
  <text x="400" y="560" text-anchor="middle" fill="#ffeb3b" font-size="11">纯传球阵型</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_wildcat_formation():
    """Same as wildcat but with id wildcat-formation"""
    svg = svg_header("Wildcat Formation", "野猫阵型", "RB接直接传球")
    svg += svg_los(350)
    svg += svg_oline(350)

    # RB at QB position
    svg += '''
  <circle cx="400" cy="390" r="24" fill="#ff6b35" stroke="#ffffff" stroke-width="3"/>
  <text x="400" y="398" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">RB</text>'''

    # QB as receiver
    svg += '''
  <circle cx="300" cy="360" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="300" y="366" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">QB</text>'''

    # Other RB
    svg += svg_rb(450, 390, 'RB')

    # WRs
    svg += svg_wr(150, 350)
    svg += svg_wr(680, 350)

    svg += '''
  <text x="400" y="440" text-anchor="middle" fill="#ffffff" font-size="12">RB接直接传球</text>
  <text x="400" y="460" text-anchor="middle" fill="#ffeb3b" font-size="11">跑球威胁最大</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

# === SAVE FUNCTION ===

def save_svg(filename, content):
    """Save SVG to file"""
    filepath = f'../assets/images/offense-formation/{filename}'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

# === MAIN EXECUTION ===

def main():
    """Generate missing offensive formation SVGs"""
    created = []

    formations = {
        'shotgun-formation': create_shotgun_formation,
        'i-formation': create_i_formation,
        'spread-offense': create_spread_offense,
        'singleback-formation': create_singleback_formation,
        'pistol-formation': create_pistol_formation,
        'empty-backfield': create_empty_backfield,
        'wildcat-formation': create_wildcat_formation
    }

    print("Creating missing offensive formation SVGs...")
    for name, generator in formations.items():
        path = save_svg(f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal missing formation SVGs created: {len(created)}")
    return len(created)

if __name__ == '__main__':
    count = main()
    print(f"\n{'='*50}")
    print(f"SUCCESS! Created {count} missing formation SVG diagrams")
    print(f"{'='*50}")
