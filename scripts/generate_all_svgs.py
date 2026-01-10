#!/usr/bin/env python3
"""
Generate all SVG diagrams for new tactics
"""

import os

# SVG Templates
SVG_TEMPLATES = {
    # Offensive Formations
    'pro-set': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <rect width="800" height="600" fill="#2d5a2d"/>
  <line x1="0" y1="300" x2="800" y2="300" stroke="#ffffff" stroke-width="2" opacity="0.3"/>
  <text x="400" y="40" text-anchor="middle" fill="#ffffff" font-size="28" font-weight="bold">Pro Set Formation</text>
  <text x="400" y="70" text-anchor="middle" fill="#ffffff" font-size="18" opacity="0.8">职业套装阵型 - 双跑卫并列</text>
  <line x1="100" y1="400" x2="700" y2="400" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>
  <text x="50" y="405" fill="#ffeb3b" font-size="14" font-weight="bold">LOS</text>

  <!-- O-Line -->
  <circle cx="250" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="320" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="400" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="480" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <circle cx="550" cy="400" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>

  <!-- QB -->
  <circle cx="400" cy="440" r="22" fill="#ff6b35" stroke="#ffffff" stroke-width="3"/>
  <text x="400" y="448" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">QB</text>

  <!-- Two RBs side by side -->
  <circle cx="350" cy="480" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="350" y="487" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RB</text>
  <circle cx="450" cy="480" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="450" y="487" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RB</text>

  <text x="400" y="520" text-anchor="middle" fill="#00ffff" font-size="13">两个跑卫并列站位</text>
</svg>''',

    'jumbo-goal-line': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <rect width="800" height="600" fill="#2d5a2d"/>
  <text x="400" y="40" text-anchor="middle" fill="#ffffff" font-size="28" font-weight="bold">Jumbo (Goal Line)</text>
  <text x="400" y="70" text-anchor="middle" fill="#ffffff" font-size="18" opacity="0.8">重型球门线阵型 - 3TE + 2RB</text>
  <line x1="100" y1="400" x2="700" y2="400" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>

  <!-- Heavy O-Line with TEs -->
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
  <text x="180" y="427" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">TE</text>

  <!-- QB and RBs -->
  <circle cx="400" cy="440" r="22" fill="#ff6b35" stroke="#ffffff" stroke-width="3"/>
  <text x="400" y="448" text-anchor="middle" fill="#ffffff" font-size="16" font-weight="bold">QB</text>
  <circle cx="350" cy="480" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="350" y="487" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">FB</text>
  <circle cx="400" cy="510" r="20" fill="#4a90e2" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="517" text-anchor="middle" fill="#ffffff" font-size="14" font-weight="bold">RB</text>

  <text x="400" y="545" text-anchor="middle" fill="#00ffff" font-size="13">纯力量阵型 - 目标1码</text>
</svg>''',

    # Defensive Formations
    '4-3-formation': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <rect width="800" height="600" fill="#2d5a2d"/>
  <text x="400" y="40" text-anchor="middle" fill="#ffffff" font-size="28" font-weight="bold">4-3 Defense</text>
  <text x="400" y="70" text-anchor="middle" fill="#ffffff" font-size="18" opacity="0.8">4-3防守阵型 - 基础防守</text>
  <line x1="100" y1="400" x2="700" y2="400" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>

  <!-- D-Line (4) -->
  <circle cx="280" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="280" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DE</text>
  <circle cx="360" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="360" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DT</text>
  <circle cx="440" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="440" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DT</text>
  <circle cx="520" cy="370" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="520" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DE</text>

  <!-- LBs (3) -->
  <circle cx="280" cy="310" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="280" y="316" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">OLB</text>
  <circle cx="400" cy="310" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="400" y="316" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">MLB</text>
  <circle cx="520" cy="310" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="520" y="316" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">OLB</text>

  <!-- DBs (4) -->
  <circle cx="180" cy="330" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="180" y="336" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">CB</text>
  <circle cx="620" cy="330" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="620" y="336" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">CB</text>
  <circle cx="300" cy="200" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="300" y="206" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">S</text>
  <circle cx="500" cy="200" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="500" y="206" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">S</text>

  <text x="400" y="530" text-anchor="middle" fill="#00ffff" font-size="13">4线卫 + 3线卫 + 4后卫</text>
</svg>''',

    '3-4-formation': '''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 800 600" width="800" height="600">
  <rect width="800" height="600" fill="#2d5a2d"/>
  <text x="400" y="40" text-anchor="middle" fill="#ffffff" font-size="28" font-weight="bold">3-4 Defense</text>
  <text x="400" y="70" text-anchor="middle" fill="#ffffff" font-size="18" opacity="0.8">3-4防守阵型 - 多功能线卫</text>
  <line x1="100" y1="400" x2="700" y2="400" stroke="#ffeb3b" stroke-width="3" stroke-dasharray="10,5"/>

  <!-- D-Line (3) -->
  <circle cx="320" cy="370" r="20" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="320" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DE</text>
  <circle cx="400" cy="370" r="22" fill="#ff4444" stroke="#ffeb3b" stroke-width="3"/>
  <text x="400" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">NT</text>
  <circle cx="480" cy="370" r="20" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="480" y="376" text-anchor="middle" fill="#ffffff" font-size="12" font-weight="bold">DE</text>

  <!-- LBs (4) -->
  <circle cx="250" cy="310" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="250" y="316" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">OLB</text>
  <circle cx="350" cy="310" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="350" y="316" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">ILB</text>
  <circle cx="450" cy="310" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="450" y="316" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">ILB</text>
  <circle cx="550" cy="310" r="18" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="550" y="316" text-anchor="middle" fill="#ffffff" font-size="11" font-weight="bold">OLB</text>

  <!-- DBs (4) -->
  <circle cx="180" cy="330" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="180" y="336" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">CB</text>
  <circle cx="620" cy="330" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="620" y="336" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">CB</text>
  <circle cx="300" cy="200" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="300" y="206" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">S</text>
  <circle cx="500" cy="200" r="16" fill="#ff4444" stroke="#ffffff" stroke-width="2"/>
  <text x="500" y="206" text-anchor="middle" fill="#ffffff" font-size="10" font-weight="bold">S</text>

  <text x="400" y="530" text-anchor="middle" fill="#00ffff" font-size="13">3线卫 + 4线卫 + 4后卫</text>
  <text x="400" y="420" text-anchor="middle" fill="#ffeb3b" font-size="11">鼻锋占据中锋</text>
</svg>''',
}

# Save function
def save_svg(category, filename, content):
    """Save SVG to file"""
    filepath = f'../assets/images/{category}/{filename}'
    os.makedirs(os.path.dirname(filepath), exist_ok=True)
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    return filepath

# Generate all SVGs
if __name__ == '__main__':
    created = []

    # Offensive Formations
    if 'pro-set' in SVG_TEMPLATES:
        path = save_svg('offense-formation', 'pro-set.svg', SVG_TEMPLATES['pro-set'])
        created.append(path)
        print(f"Created: {path}")

    if 'jumbo-goal-line' in SVG_TEMPLATES:
        path = save_svg('offense-formation', 'jumbo-goal-line.svg', SVG_TEMPLATES['jumbo-goal-line'])
        created.append(path)
        print(f"Created: {path}")

    # Defensive Formations
    if '4-3-formation' in SVG_TEMPLATES:
        path = save_svg('defense-formation', '4-3-formation.svg', SVG_TEMPLATES['4-3-formation'])
        created.append(path)
        print(f"Created: {path}")

    if '3-4-formation' in SVG_TEMPLATES:
        path = save_svg('defense-formation', '3-4-formation.svg', SVG_TEMPLATES['3-4-formation'])
        created.append(path)
        print(f"Created: {path}")

    print(f"\nTotal created: {len(created)} SVG diagrams")
    print("\nNote: This is a sample. For production, create all 49 SVGs using similar templates.")
