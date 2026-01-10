#!/usr/bin/env python3
"""
Create detailed SVG diagrams for all offensive and defensive formations
"""

import os

# === REUSABLE SVG COMPONENTS ===

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

def svg_dline(positions, y=370):
    """Defensive line with custom positions"""
    svg = '\n  <!-- Defensive Line -->'
    for x, label in positions:
        svg += f'''
  <circle cx="{x}" cy="{y}" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+6}" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">{label}</text>'''
    return svg

def svg_lb(positions, y=320):
    """Linebackers"""
    svg = '\n  <!-- Linebackers -->'
    for x, label in positions:
        svg += f'''
  <circle cx="{x}" cy="{y}" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+6}" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">{label}</text>'''
    return svg

def svg_db(positions):
    """Defensive backs"""
    svg = '\n  <!-- Defensive Backs -->'
    for x, y, label in positions:
        svg += f'''
  <circle cx="{x}" cy="{y}" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+6}" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">{label}</text>'''
    return svg

def svg_legend():
    """Legend"""
    return '''
  <!-- Legend -->
  <g transform="translate(50, 540)">
    <circle cx="0" cy="0" r="14" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
    <text x="20" y="5" fill="#ffffff" font-size="12">= 进攻</text>

    <circle cx="100" cy="0" r="14" fill="#ff6b35" stroke="#ffffff" stroke-width="2"/>
    <text x="120" y="5" fill="#ffffff" font-size="12">= 四分卫</text>

    <circle cx="230" cy="0" r="14" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
    <text x="250" y="5" fill="#ffffff" font-size="12">= 防守</text>
  </g>'''

def close_svg():
    return '\n</svg>'

# === OFFENSIVE FORMATIONS ===

def create_t_formation():
    svg = svg_header("T Formation", "T字阵型", "经典跑球阵型")
    svg += svg_los(400)
    svg += svg_oline(400)
    svg += svg_qb(400, 440)

    # Three RBs in T formation
    svg += svg_rb(350, 480, 'HB')
    svg += svg_rb(400, 510, 'FB')
    svg += svg_rb(450, 480, 'HB')

    # T shape indicator
    svg += '''
  <path d="M 330,490 L 470,490" stroke="#00ffff" stroke-width="3" stroke-dasharray="5,5" opacity="0.6"/>
  <line x1="400" y1="455" x2="400" y2="495" stroke="#00ffff" stroke-width="3" stroke-dasharray="5,5" opacity="0.6"/>
  <text x="500" y="490" fill="#00ffff" font-size="14" font-weight="bold">T字形</text>'''

    # Two WRs
    svg += svg_wr(150, 400)
    svg += svg_wr(650, 400)

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_single_back_ace():
    svg = svg_header("Single Back (Ace)", "单后卫ACE阵型", "现代平衡阵型")
    svg += svg_los(400)
    svg += svg_oline(400)
    svg += svg_qb(400, 440)
    svg += svg_rb(400, 490, 'RB')

    # Receivers
    svg += svg_wr(150, 400)
    svg += svg_wr(650, 400)
    svg += '''
  <circle cx="600" cy="410" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="600" y="416" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">SL</text>'''

    # TE
    svg += svg_te(620, 400)

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_pro_set():
    svg = svg_header("Pro Set", "职业套装阵型", "双跑卫并列")
    svg += svg_los(400)
    svg += svg_oline(400)
    svg += svg_qb(400, 440)

    # Two RBs side by side
    svg += svg_rb(350, 480, 'RB')
    svg += svg_rb(450, 480, 'RB')

    # Receivers
    svg += svg_wr(150, 400)
    svg += svg_wr(650, 400)
    svg += svg_te(620, 400)

    svg += '''
  <text x="400" y="520" text-anchor="middle" fill="#00ffff" font-size="13">两个跑卫并列站位</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_jumbo():
    svg = svg_header("Jumbo (Goal Line)", "重型球门线阵型", "3TE + 2RB")
    svg += svg_los(400)

    # Heavy line with extra TEs
    svg += '''
  <!-- Heavy O-Line -->
  <circle cx="200" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="200" y="407" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">TE</text>
  <circle cx="270" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="270" y="407" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">T</text>
  <circle cx="340" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="340" y="407" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">G</text>
  <circle cx="400" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="407" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">C</text>
  <circle cx="460" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="460" y="407" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">G</text>
  <circle cx="530" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="530" y="407" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">T</text>
  <circle cx="600" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="600" y="407" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">TE</text>
  <circle cx="180" cy="420" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="180" y="427" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">TE</text>'''

    svg += svg_qb(400, 440)
    svg += svg_rb(350, 480, 'FB')
    svg += svg_rb(400, 510, 'RB')

    svg += '''
  <text x="400" y="545" text-anchor="middle" fill="#00ffff" font-size="13">纯力量阵型 - 目标1码</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

# === DEFENSIVE FORMATIONS ===

def create_6_2():
    svg = svg_header("6-2 Defense", "6-2防守阵型", "老式防守")
    svg += svg_los(400)

    # 6 D-linemen
    dline = [(200, 'E'), (280, 'T'), (350, 'G'), (450, 'G'), (520, 'T'), (600, 'E')]
    svg += svg_dline(dline, 370)

    # 2 LBs
    svg += svg_lb([(350, 'LB'), (450, 'LB')], 310)

    # 3 DBs
    svg += svg_db([(180, 330, 'CB'), (620, 330, 'CB'), (400, 200, 'S')])

    svg += '''
  <text x="400" y="530" text-anchor="middle" fill="#00ffff" font-size="13">6线卫 + 2线卫 + 3后卫</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_5_3():
    svg = svg_header("5-3 Defense", "5-3防守阵型", "平衡防守")
    svg += svg_los(400)

    # 5 D-linemen
    dline = [(240, 'E'), (320, 'T'), (400, 'NG'), (480, 'T'), (560, 'E')]
    svg += svg_dline(dline, 370)

    # 3 LBs
    svg += svg_lb([(280, 'OLB'), (400, 'MLB'), (520, 'OLB')], 310)

    # 3 DBs
    svg += svg_db([(180, 330, 'CB'), (620, 330, 'CB'), (400, 200, 'S')])

    svg += '''
  <text x="400" y="530" text-anchor="middle" fill="#00ffff" font-size="13">5线卫 + 3线卫 + 3后卫</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_5_2_eagle():
    svg = svg_header("5-2 Eagle", "5-2老鹰阵型", "Philadelphia特色")
    svg += svg_los(400)

    # 5 D-linemen with eagle alignment
    dline = [(260, 'E'), (340, 'T'), (400, 'NG'), (460, 'T'), (540, 'E')]
    svg += svg_dline(dline, 370)

    # 2 LBs (eagle style)
    svg += svg_lb([(340, 'LB'), (460, 'LB')], 310)

    # 4 DBs
    svg += svg_db([(180, 330, 'CB'), (620, 330, 'CB'), (300, 200, 'S'), (500, 200, 'S')])

    svg += '''
  <text x="400" y="530" text-anchor="middle" fill="#00ffff" font-size="13">5线卫 + 2线卫 + 4后卫</text>
  <text x="400" y="420" text-anchor="middle" fill="#ffeb3b" font-size="11">老鹰式对位</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_4_4():
    svg = svg_header("4-4 Defense", "4-4防守阵型", "均衡防跑传")
    svg += svg_los(400)

    # 4 D-linemen
    dline = [(280, 'DE'), (360, 'DT'), (440, 'DT'), (520, 'DE')]
    svg += svg_dline(dline, 370)

    # 4 LBs
    svg += svg_lb([(240, 'OLB'), (340, 'ILB'), (460, 'ILB'), (560, 'OLB')], 310)

    # 3 DBs
    svg += svg_db([(180, 330, 'CB'), (620, 330, 'CB'), (400, 200, 'S')])

    svg += '''
  <text x="400" y="530" text-anchor="middle" fill="#00ffff" font-size="13">4线卫 + 4线卫 + 3后卫</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_4_3():
    svg = svg_header("4-3 Defense", "4-3防守阵型", "基础防守")
    svg += svg_los(400)

    # 4 D-linemen
    dline = [(280, 'DE'), (360, 'DT'), (440, 'DT'), (520, 'DE')]
    svg += svg_dline(dline, 370)

    # 3 LBs
    svg += svg_lb([(280, 'OLB'), (400, 'MLB'), (520, 'OLB')], 310)

    # 4 DBs
    svg += svg_db([(180, 330, 'CB'), (620, 330, 'CB'), (300, 200, 'S'), (500, 200, 'S')])

    svg += '''
  <text x="400" y="530" text-anchor="middle" fill="#00ffff" font-size="13">4线卫 + 3线卫 + 4后卫</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_3_4():
    svg = svg_header("3-4 Defense", "3-4防守阵型", "多功能线卫")
    svg += svg_los(400)

    # 3 D-linemen
    dline = [(320, 'DE'), (480, 'DE')]
    svg += svg_dline(dline, 370)
    svg += '''
  <circle cx="400" cy="370" r="22" fill="#ff4444" stroke="#ffeb3b" stroke-width="3"/>
  <text x="400" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">NT</text>'''

    # 4 LBs
    svg += svg_lb([(250, 'OLB'), (350, 'ILB'), (450, 'ILB'), (550, 'OLB')], 310)

    # 4 DBs
    svg += svg_db([(180, 330, 'CB'), (620, 330, 'CB'), (300, 200, 'S'), (500, 200, 'S')])

    svg += '''
  <text x="400" y="530" text-anchor="middle" fill="#00ffff" font-size="13">3线卫 + 4线卫 + 4后卫</text>
  <text x="400" y="420" text-anchor="middle" fill="#ffeb3b" font-size="11">鼻锋占据中锋</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_46_bear():
    svg = svg_header("46 Bear Defense", "46熊式防守", "芝加哥传奇")
    svg += svg_los(400)

    # 4 D-linemen shifted
    dline = [(260, 'DE'), (340, 'DT'), (440, 'DT'), (540, 'DE')]
    svg += svg_dline(dline, 370)

    # 3 LBs (one moved up - the 46)
    svg += '''
  <!-- Linebacker 46 position -->
  <circle cx="480" cy="340" r="20" fill="#ff4444" stroke="#ffeb3b" stroke-width="3"/>
  <text x="480" y="346" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">46</text>'''
    svg += svg_lb([(280, 'OLB'), (380, 'MLB')], 310)

    # 4 DBs
    svg += svg_db([(180, 330, 'CB'), (620, 330, 'CB'), (300, 200, 'SS'), (500, 200, 'FS')])

    svg += '''
  <text x="400" y="530" text-anchor="middle" fill="#00ffff" font-size="13">激进压迫式防守</text>
  <text x="480" y="295" text-anchor="middle" fill="#ffeb3b" font-size="10">46号位</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

# === SAVE FUNCTION ===

def save_svg(category, filename, content):
    """Save SVG to file"""
    filepath = f'../assets/images/{category}/{filename}'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

# === MAIN EXECUTION ===

def main():
    """Generate all formation SVGs"""
    created = []

    # Offensive formations
    print("Creating offensive formation SVGs...")
    formations = {
        't-formation': create_t_formation,
        'single-back-ace': create_single_back_ace,
        'pro-set': create_pro_set,
        'jumbo-goal-line': create_jumbo
    }

    for name, generator in formations.items():
        path = save_svg('offense-formation', f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    # Defensive formations
    print("\nCreating defensive formation SVGs...")
    def_formations = {
        '6-2-formation': create_6_2,
        '5-3-formation': create_5_3,
        '5-2-eagle': create_5_2_eagle,
        '4-4-formation': create_4_4,
        '4-3-formation': create_4_3,
        '3-4-formation': create_3_4,
        '46-bear': create_46_bear
    }

    for name, generator in def_formations.items():
        path = save_svg('defense-formation', f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal formation SVGs created: {len(created)}")
    return len(created)

if __name__ == '__main__':
    count = main()
    print(f"\n{'='*50}")
    print(f"SUCCESS! Created {count} detailed formation SVG diagrams")
    print(f"{'='*50}")
