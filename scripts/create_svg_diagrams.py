#!/usr/bin/env python3
"""
Generate SVG diagrams for new tactics based on existing templates
"""

import os

# SVG template base
def create_svg_base(title_en, title_cn, width=800, height=600):
    """Create base SVG structure"""
    return f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" width="{width}" height="{height}">
  <!-- Background -->
  <rect width="{width}" height="{height}" fill="#2d5a2d"/>

  <!-- Field lines -->
  <line x1="0" y1="{height//2}" x2="{width}" y2="{height//2}" stroke="#ffffff" stroke-width="2" opacity="0.3"/>
  <line x1="{width//2}" y1="0" x2="{width//2}" y2="{height}" stroke="#ffffff" stroke-width="2" opacity="0.3"/>

  <!-- Title -->
  <text x="{width//2}" y="40" text-anchor="middle" fill="#ffffff" font-size="28" font-weight="bold" font-family="Arial">
    {title_en}
  </text>
  <text x="{width//2}" y="70" text-anchor="middle" fill="#ffffff" font-size="18" font-family="Arial" opacity="0.8">
    {title_cn}
  </text>'''

def create_los(y=400):
    """Create Line of Scrimmage"""
    return f'''
  <!-- Line of Scrimmage -->
  <line x1="100" y1="{y}" x2="700" y2="{y}" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>
  <text x="50" y="{y+5}" fill="#ffeb3b" font-size="14" font-weight="bold">LOS</text>'''

def create_offensive_line(y=400):
    """Create standard 5-man offensive line"""
    positions = [
        (250, 'LT'),
        (320, 'LG'),
        (400, 'C'),
        (480, 'RG'),
        (550, 'RT')
    ]
    svg = '\n  <!-- Offensive Line -->'
    for x, label in positions:
        svg += f'''
  <circle cx="{x}" cy="{y}" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+7}" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">{label}</text>'''
    return svg

def create_defensive_line_4_3(y=370):
    """Create 4-3 defensive line"""
    positions = [
        (300, 'DE'),
        (370, 'DT'),
        (430, 'DT'),
        (500, 'DE')
    ]
    svg = '\n  <!-- Defensive Line (4 players) -->'
    for x, label in positions:
        svg += f'''
  <circle cx="{x}" cy="{y}" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+6}" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">{label}</text>'''
    return svg

def create_linebackers_4_3(y=320):
    """Create linebackers for 4-3"""
    positions = [
        (280, 'OLB'),
        (400, 'MLB'),
        (520, 'OLB')
    ]
    svg = '\n  <!-- Linebackers -->'
    for x, label in positions:
        svg += f'''
  <circle cx="{x}" cy="{y}" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="{x}" y="{y+6}" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">{label}</text>'''
    return svg

def create_legend():
    """Create legend"""
    return '''
  <!-- Legend -->
  <g transform="translate(50, 540)">
    <circle cx="0" cy="0" r="14" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
    <text x="22" y="5" fill="#ffffff" font-size="13">= 进攻</text>

    <circle cx="100" cy="0" r="14" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
    <text x="122" y="5" fill="#ffffff" font-size="13">= 防守</text>
  </g>'''

def close_svg():
    """Close SVG tag"""
    return '\n</svg>'

# Create offensive formation SVGs
def create_t_formation():
    svg = create_svg_base("T Formation", "T字阵型 - 经典跑球阵型")
    svg += create_los(400)
    svg += create_offensive_line(400)

    # QB under center
    svg += '''
  <!-- Quarterback -->
  <circle cx="400" cy="440" r="22" fill="#ff6b35" stroke="#ffffff" stroke-width="3"/>
  <text x="400" y="448" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">QB</text>'''

    # Three RBs in T formation
    svg += '''
  <!-- Running Backs in T shape -->
  <circle cx="350" cy="480" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="350" y="487" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RB</text>

  <circle cx="400" cy="510" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="517" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">FB</text>

  <circle cx="450" cy="480" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="450" y="487" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RB</text>'''

    # T shape indicator
    svg += '''
  <path d="M 330,490 L 470,490" stroke="#00ffff" stroke-width="3" stroke-dasharray="5,5" opacity="0.6"/>
  <line x1="400" y1="455" x2="400" y2="495" stroke="#00ffff" stroke-width="3" stroke-dasharray="5,5" opacity="0.6"/>
  <text x="500" y="490" fill="#00ffff" font-size="14" font-weight="bold">T字形</text>'''

    svg += create_legend()
    svg += close_svg()
    return svg

def create_single_back_ace():
    svg = create_svg_base("Single Back (Ace)", "单后卫ACE阵型 - 现代平衡阵型")
    svg += create_los(400)
    svg += create_offensive_line(400)

    # QB under center
    svg += '''
  <!-- Quarterback -->
  <circle cx="400" cy="440" r="22" fill="#ff6b35" stroke="#ffffff" stroke-width="3"/>
  <text x="400" y="448" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">QB</text>'''

    # Single RB
    svg += '''
  <!-- Running Back -->
  <circle cx="400" cy="490" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="497" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RB</text>'''

    # Receivers
    svg += '''
  <!-- Wide Receivers -->
  <circle cx="150" cy="400" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="150" y="406" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">WR</text>

  <circle cx="650" cy="400" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="650" y="406" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">WR</text>

  <!-- Slot Receiver -->
  <circle cx="600" cy="420" r="18" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="600" y="426" text-anchor="middle" fill="#ffffff" font-size="13" font-weight="bold">SL</text>
  <text x="620" y="455" fill="#00ffff" font-size="11">槽位接球手</text>'''

    svg += create_legend()
    svg += close_svg()
    return svg

# Save SVGs
def save_svg(filename, content):
    """Save SVG to file"""
    filepath = f'../assets/images/offense-formation/{filename}'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    print(f"Created: {filepath}")

if __name__ == '__main__':
    # Create offensive formation SVGs
    print("Creating offensive formation SVGs...")
    save_svg('t-formation.svg', create_t_formation())
    save_svg('single-back-ace.svg', create_single_back_ace())

    print("\nDone! Created 2 SVG diagrams as examples.")
    print("More SVGs can be generated using the same pattern.")
