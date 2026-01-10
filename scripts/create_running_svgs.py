#!/usr/bin/env python3
"""
Create detailed SVG diagrams for running plays
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
  <line x1="100" y1="400" x2="700" y2="400" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>
  <text x="50" y="405" fill="#ffeb3b" font-size="14" font-weight="bold">LOS</text>

  <!-- Arrow markers -->
  <defs>
    <marker id="arrow-rb" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#ff6b35"/>
    </marker>
    <marker id="arrow-block" markerWidth="10" markerHeight="7" refX="9" refY="3.5" orient="auto">
      <polygon points="0 0, 10 3.5, 0 7" fill="#00ffff"/>
    </marker>
  </defs>'''

def svg_oline(y=400):
    """5-man offensive line"""
    positions = [(250, 'LT'), (320, 'LG'), (400, 'C'), (480, 'RG'), (550, 'RT')]
    svg = '\n  <!-- Offensive Line -->'
    for x, label in positions:
        svg += f'''
  <circle cx="{x}" cy="{y}" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">{label}</text>'''
    return svg

def svg_qb(x=400, y=440):
    """Quarterback"""
    return f'''
  <!-- Quarterback -->
  <circle cx="{x}" cy="{y}" r="22" fill="#ff6b35" stroke="#ffffff" stroke-width="3"/>
  <text x="{x}" y="{y+8}" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">QB</text>'''

def svg_rb(x, y, label='RB'):
    """Running back"""
    return f'''
  <circle cx="{x}" cy="{y}" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">{label}</text>'''

def svg_legend():
    return '''
  <!-- Legend -->
  <g transform="translate(50, 540)">
    <circle cx="0" cy="0" r="12" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
    <text x="18" y="5" fill="#ffffff" font-size="11">= 进攻</text>

    <circle cx="80" cy="0" r="12" fill="#ff6b35" stroke="#ffffff" stroke-width="2"/>
    <text x="98" y="5" fill="#ffffff" font-size="11">= 持球人</text>

    <line x1="180" y1="0" x2="220" y2="0" stroke="#ff6b35" stroke-width="3" marker-end="url(#arrow-rb)"/>
    <text x="230" y="5" fill="#ffffff" font-size="11">= 跑动路线</text>
  </g>'''

def close_svg():
    return '\n</svg>'

# === RUNNING PLAY GENERATORS ===

def create_inside_zone():
    svg = svg_base("Inside Zone", "内区跑球", "横向移动攻击A/B缝")
    svg += svg_oline(400)
    svg += svg_qb(400, 440)
    svg += svg_rb(400, 480, 'RB')

    # RB path (zone read inside)
    svg += '''
  <path d="M 400,465 L 430,430 L 460,360 L 470,300" stroke="#ff6b35" stroke-width="4" fill="none" marker-end="url(#arrow-rb)"/>'''

    # O-line zone blocking arrows
    svg += '''
  <!-- Zone blocking movements -->
  <path d="M 250,385 L 270,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <path d="M 320,385 L 340,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <path d="M 400,385 L 420,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <path d="M 480,385 L 500,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <path d="M 550,385 L 570,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>'''

    # Target zone
    svg += '''
  <rect x="380" y="320" width="120" height="60" fill="#ffeb3b" opacity="0.15" stroke="#ffeb3b" stroke-width="2" stroke-dasharray="5,5"/>
  <text x="440" y="360" text-anchor="middle" fill="#ffeb3b" font-size="11" font-weight="bold">目标区</text>'''

    svg += '''
  <text x="400" y="515" text-anchor="middle" fill="#ffffff" font-size="12">前锋横向移动创造缝隙</text>
  <text x="400" y="535" text-anchor="middle" fill="#ffeb3b" font-size="11">RB读防守选择空当</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_outside_zone():
    svg = svg_base("Outside Zone", "外区跑球", "横向延伸到边线")
    svg += svg_oline(400)
    svg += svg_qb(400, 440)
    svg += svg_rb(350, 480, 'RB')

    # RB path (zone outside)
    svg += '''
  <path d="M 350,465 L 320,430 L 260,360 L 200,300" stroke="#ff6b35" stroke-width="4" fill="none" marker-end="url(#arrow-rb)"/>'''

    # O-line zone blocking arrows (moving left)
    svg += '''
  <!-- Zone blocking movements -->
  <path d="M 250,385 L 230,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <path d="M 320,385 L 300,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <path d="M 400,385 L 380,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <path d="M 480,385 L 460,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <path d="M 550,385 L 530,370" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>'''

    svg += '''
  <text x="400" y="515" text-anchor="middle" fill="#ffffff" font-size="12">全线横向延伸到边线</text>
  <text x="400" y="535" text-anchor="middle" fill="#ffeb3b" font-size="11">制造边线空间</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_power_run():
    svg = svg_base("Power Run", "力量跑球", "拉边锋+全卫领跑")
    svg += svg_oline(400)
    svg += svg_qb(400, 440)
    svg += svg_rb(400, 480, 'RB')
    svg += svg_rb(350, 450, 'FB')

    # FB lead blocking
    svg += '''
  <path d="M 350,435 L 360,400 L 380,360 L 400,320" stroke="#00ffff" stroke-width="3" marker-end="url(#arrow-block)"/>
  <text x="330" y="390" fill="#00ffff" font-size="10">领路</text>'''

    # RB following FB
    svg += '''
  <path d="M 400,465 L 410,430 L 420,370 L 430,300" stroke="#ff6b35" stroke-width="4" fill="none" marker-end="url(#arrow-rb)"/>'''

    # Pulling guard
    svg += '''
  <path d="M 320,385 L 360,360 L 400,340" stroke="#00ffff" stroke-width="2" stroke-dasharray="4,4" marker-end="url(#arrow-block)"/>
  <text x="340" y="350" fill="#00ffff" font-size="10">拉卫</text>'''

    svg += '''
  <text x="400" y="515" text-anchor="middle" fill="#ffffff" font-size="12">FB领跑+拉卫阻挡</text>
  <text x="400" y="535" text-anchor="middle" fill="#ffeb3b" font-size="11">纯力量突破</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_counter_run():
    svg = svg_base("Counter Run", "反向跑球", "假装一侧实际反向")
    svg += svg_oline(400)
    svg += svg_qb(400, 440)
    svg += svg_rb(450, 480, 'RB')

    # Fake motion
    svg += '''
  <path d="M 450,465 L 480,450" stroke="#00ffff" stroke-width="2" stroke-dasharray="4,4" opacity="0.5"/>
  <text x="500" y="455" fill="#00ffff" font-size="10">假动作</text>'''

    # Actual run (counter direction)
    svg += '''
  <path d="M 450,465 L 420,440 L 360,380 L 300,320 L 250,280" stroke="#ff6b35" stroke-width="4" fill="none" marker-end="url(#arrow-rb)"/>'''

    # Pulling linemen
    svg += '''
  <path d="M 480,385 L 420,360 L 340,340" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <text x="420" y="350" fill="#00ffff" font-size="10">拉卫</text>'''

    svg += '''
  <text x="400" y="515" text-anchor="middle" fill="#ffffff" font-size="12">假装一侧实际反向攻击</text>
  <text x="400" y="535" text-anchor="middle" fill="#ffeb3b" font-size="11">欺骗性跑球</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_draw_play():
    svg = svg_base("Draw Play", "佯攻跑球", "假装传球实际跑球")
    svg += svg_oline(400)
    svg += svg_qb(400, 470)
    svg += svg_rb(400, 510, 'RB')

    # O-line initially pass blocking (standing)
    svg += '''
  <text x="400" y="380" text-anchor="middle" fill="#00ffff" font-size="10">传球阻挡姿势</text>'''

    # QB drop back then hand off
    svg += '''
  <path d="M 400,455 L 400,485" stroke="#ff6b35" stroke-width="3" stroke-dasharray="4,4"/>
  <text x="360" y="475" fill="#ff6b35" font-size="10">后撤</text>'''

    # RB delayed run
    svg += '''
  <path d="M 400,495 L 420,460 L 450,360 L 470,300" stroke="#ff6b35" stroke-width="4" fill="none" marker-end="url(#arrow-rb)"/>
  <text x="485" y="330" fill="#ff6b35" font-size="10">延迟跑球</text>'''

    svg += '''
  <text x="400" y="545" text-anchor="middle" fill="#ffffff" font-size="12">假装传球骗防守冲传</text>
  <text x="400" y="565" text-anchor="middle" fill="#ffeb3b" font-size="11">然后RB跑入空当</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_toss_sweep():
    svg = svg_base("Toss Sweep", "抛球横扫", "抛球给RB横扫边线")
    svg += svg_oline(400)
    svg += svg_qb(400, 440)
    svg += svg_rb(300, 460, 'RB')

    # Toss path
    svg += '''
  <path d="M 400,425 Q 350,430 320,445" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="3,3"/>
  <circle cx="330" cy="438" r="8" fill="#ffeb3b" opacity="0.5"/>
  <text x="350" y="425" fill="#ffeb3b" font-size="10">抛球</text>'''

    # RB sweep
    svg += '''
  <path d="M 300,445 L 240,410 L 180,340 L 150,280" stroke="#ff6b35" stroke-width="4" fill="none" marker-end="url(#arrow-rb)"/>'''

    # Lead blockers
    svg += '''
  <path d="M 250,385 L 220,360 L 180,330" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <path d="M 320,385 L 260,350 L 200,320" stroke="#00ffff" stroke-width="2" marker-end="url(#arrow-block)"/>
  <text x="210" y="345" fill="#00ffff" font-size="10">领路</text>'''

    svg += '''
  <text x="400" y="515" text-anchor="middle" fill="#ffffff" font-size="12">抛球给RB横扫边线</text>
  <text x="400" y="535" text-anchor="middle" fill="#ffeb3b" font-size="11">前锋领路阻挡</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

def create_trap_play():
    svg = svg_base("Trap Play", "陷阱跑球", "放进防守者再阻挡")
    svg += svg_oline(400)
    svg += svg_qb(400, 440)
    svg += svg_rb(400, 480, 'RB')

    # Let defender through
    svg += '''
  <circle cx="360" cy="370" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2" opacity="0.7"/>
  <text x="360" y="375" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">DT</text>
  <path d="M 360,355 L 360,410" stroke="#ff4444" stroke-width="2"/>
  <text x="330" y="390" fill="#ffeb3b" font-size="9">放进</text>'''

    # Trap block from pulling guard
    svg += '''
  <path d="M 480,385 L 440,360 L 380,370" stroke="#00ffff" stroke-width="3" marker-end="url(#arrow-block)"/>
  <circle cx="380" cy="370" r="10" fill="#ffeb3b" opacity="0.5"/>
  <text x="420" y="355" fill="#00ffff" font-size="10">陷阱阻挡</text>'''

    # RB path through
    svg += '''
  <path d="M 400,465 L 415,420 L 435,360 L 450,300" stroke="#ff6b35" stroke-width="4" fill="none" marker-end="url(#arrow-rb)"/>'''

    svg += '''
  <text x="400" y="515" text-anchor="middle" fill="#ffffff" font-size="12">故意放进防守者设陷阱</text>
  <text x="400" y="535" text-anchor="middle" fill="#ffeb3b" font-size="11">拉卫从侧面阻挡</text>'''

    svg += svg_legend()
    svg += close_svg()
    return svg

# === SAVE FUNCTION ===

def save_svg(filename, content):
    """Save SVG to file"""
    filepath = f'../assets/images/running/{filename}'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

# === MAIN EXECUTION ===

def main():
    """Generate all running play SVGs"""
    created = []

    plays = {
        'inside-zone': create_inside_zone,
        'outside-zone': create_outside_zone,
        'power-run': create_power_run,
        'counter-run': create_counter_run,
        'draw-play': create_draw_play,
        'toss-sweep': create_toss_sweep,
        'trap-play': create_trap_play
    }

    print("Creating running play SVGs...")
    for name, generator in plays.items():
        path = save_svg(f'{name}.svg', generator())
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal running play SVGs created: {len(created)}")
    return len(created)

if __name__ == '__main__':
    count = main()
    print(f"\n{'='*50}")
    print(f"SUCCESS! Created {count} running play SVG diagrams")
    print(f"{'='*50}")
