#!/usr/bin/env python3
"""
Merge existing data.js (with Chinese translations) with csv_tactics.js
"""

import json
import re

def extract_tactics_from_js(js_content):
    """Extract tactics array from JavaScript file"""
    # Find the tactics array
    match = re.search(r'tactics:\s*\[(.*?)\]\s*[};]', js_content, re.DOTALL)
    if not match:
        return []

    tactics_str = '[' + match.group(1) + ']'

    # Parse each tactic object manually since it's JavaScript, not JSON
    tactics = []
    current = {}
    in_tactic = False
    in_array = False
    array_name = ''
    array_content = []

    lines = tactics_str.split('\n')
    for line in lines:
        line = line.strip()

        if line.startswith('{') and not in_tactic:
            in_tactic = True
            current = {}
        elif line.startswith('}') and in_tactic and not in_array:
            if current:
                tactics.append(current)
            in_tactic = False
        elif in_tactic:
            # Handle arrays
            if '[' in line and not in_array:
                match = re.match(r'(\w+):\s*\[(.*)', line)
                if match:
                    array_name = match.group(1)
                    rest = match.group(2).strip()
                    if ']' in rest:
                        # Single line array
                        array_str = rest.split(']')[0]
                        items = re.findall(r"['\"]([^'\"]*)['\"]", array_str)
                        current[array_name] = items
                    else:
                        in_array = True
                        array_content = []
                        items = re.findall(r"['\"]([^'\"]*)['\"]", rest)
                        array_content.extend(items)
            elif in_array:
                if ']' in line:
                    # End of array
                    items = re.findall(r"['\"]([^'\"]*)['\"]", line.split(']')[0])
                    array_content.extend(items)
                    current[array_name] = array_content
                    in_array = False
                    array_name = ''
                    array_content = []
                else:
                    items = re.findall(r"['\"]([^'\"]*)['\"]", line)
                    array_content.extend(items)
            else:
                # Handle simple key: value pairs
                match = re.match(r"(\w+):\s*['\"]([^'\"]*)['\"],?", line)
                if match:
                    current[match.group(1)] = match.group(2)

    return tactics

def read_existing_data():
    """Read existing data.js with Chinese translations"""
    with open('../assets/js/data.js', 'r', encoding='utf-8') as f:
        content = f.read()
    return extract_tactics_from_js(content)

def read_csv_tactics():
    """Read CSV-generated tactics"""
    with open('../assets/js/csv_tactics.js', 'r', encoding='utf-8') as f:
        content = f.read()
    return extract_tactics_from_js(content)

def merge_tactics(existing, csv_tactics):
    """Merge tactics, preferring existing Chinese translations"""
    # Create a mapping of existing tactics by ID
    existing_map = {t.get('id'): t for t in existing if t.get('id')}

    merged = []
    processed_ids = set()

    # First, add all existing tactics (they have Chinese translations)
    for tactic in existing:
        tactic_id = tactic.get('id')
        if tactic_id:
            merged.append(tactic)
            processed_ids.add(tactic_id)

    # Then add new tactics from CSV that don't exist
    for tactic in csv_tactics:
        tactic_id = tactic.get('id')
        if tactic_id and tactic_id not in processed_ids:
            merged.append(tactic)
            processed_ids.add(tactic_id)

    return merged

def format_tactic_as_js(tactic):
    """Format a single tactic as JavaScript object string"""
    lines = ["    {"]

    # Add simple fields
    for key in ['id', 'category', 'nameEn', 'nameCn']:
        if key in tactic:
            value = tactic[key].replace("'", "\\'")
            lines.append(f"      {key}: '{value}',")

    # Add video fields
    for key in ['videoSource', 'videoTimestamp']:
        if key in tactic:
            value = tactic[key].replace("'", "\\'")
            lines.append(f"      {key}: '{value}',")

    # Add description
    if 'description' in tactic:
        value = tactic['description'].replace("'", "\\'").replace('\n', ' ')
        lines.append(f"      description: '{value}',")

    # Add arrays
    for key in ['advantages', 'weaknesses', 'counters', 'situations']:
        if key in tactic:
            items = tactic[key]
            if items:
                items_str = json.dumps(items, ensure_ascii=False, indent=8)
                lines.append(f"      {key}: {items_str},")
            else:
                lines.append(f"      {key}: [],")

    # Add difficulty and image
    for key in ['difficulty', 'image']:
        if key in tactic:
            value = tactic[key].replace("'", "\\'")
            lines.append(f"      {key}: '{value}'")

    lines.append("    }")

    return '\n'.join(lines)

def generate_merged_js(merged_tactics):
    """Generate the complete data.js content"""
    js_content = """// NFL Strategies - Tactics Data
// 橄榄球战术数据

const tacticsData = {
  // 战术分类
  categories: [
    { id: 'offense-formation', name: '进攻阵型', icon: '🏈' },
    { id: 'passing-routes', name: '传球路线', icon: '📍' },
    { id: 'passing-concepts', name: '传球概念', icon: '🎯' },
    { id: 'defense-coverage', name: '防守覆盖', icon: '🛡️' },
    { id: 'defense-formation', name: '防守阵型', icon: '⚔️' },
    { id: 'running-plays', name: '跑球战术', icon: '💨' }
  ],

  // 战术数据
  tactics: [
"""

    # Group tactics by category
    categories = [
        ('offense-formation', '进攻阵型 (Offensive Formations)'),
        ('defense-formation', '防守阵型 (Defensive Formations)'),
        ('defense-coverage', '防守覆盖 (Defensive Coverage)'),
        ('passing-routes', '传球路线 (Passing Routes)'),
        ('passing-concepts', '传球概念 (Passing Concepts)'),
        ('running-plays', '跑球战术 (Running Plays)')
    ]

    for cat_id, cat_name in categories:
        cat_tactics = [t for t in merged_tactics if t.get('category') == cat_id]
        if cat_tactics:
            js_content += f"\n    // ========== {cat_name} ==========\n"
            for i, tactic in enumerate(cat_tactics):
                js_content += format_tactic_as_js(tactic)
                if i < len(cat_tactics) - 1 or cat_id != categories[-1][0]:
                    js_content += ","
                js_content += "\n"

    js_content += """  ]
};

// 辅助函数
const TacticsDataHelper = {
  // 根据ID获取战术
  getTacticById: function(id) {
    return tacticsData.tactics.find(t => t.id === id);
  },

  // 根据分类获取战术
  getTacticsByCategory: function(categoryId) {
    if (categoryId === 'all') {
      return tacticsData.tactics;
    }
    return tacticsData.tactics.filter(t => t.category === categoryId);
  },

  // 根据难度获取战术
  getTacticsByDifficulty: function(difficulty) {
    if (difficulty === 'all') {
      return tacticsData.tactics;
    }
    return tacticsData.tactics.filter(t => t.difficulty === difficulty);
  },

  // 获取分类名称
  getCategoryName: function(categoryId) {
    const category = tacticsData.categories.find(c => c.id === categoryId);
    return category ? category.name : '';
  },

  // 获取分类图标
  getCategoryIcon: function(categoryId) {
    const category = tacticsData.categories.find(c => c.id === categoryId);
    return category ? category.icon : '';
  },

  // 搜索战术
  searchTactics: function(query) {
    if (!query || query.trim() === '') {
      return tacticsData.tactics;
    }

    const lowerQuery = query.toLowerCase().trim();
    return tacticsData.tactics.filter(tactic => {
      const nameEnMatch = tactic.nameEn.toLowerCase().includes(lowerQuery);
      const nameCnMatch = tactic.nameCn && tactic.nameCn.toLowerCase().includes(lowerQuery);
      const descMatch = tactic.description.toLowerCase().includes(lowerQuery);

      return nameEnMatch || nameCnMatch || descMatch;
    });
  }
};
"""

    return js_content

if __name__ == '__main__':
    print("Reading existing data.js...")
    existing = read_existing_data()
    print(f"Found {len(existing)} existing tactics")

    print("\nReading CSV tactics...")
    csv_tactics = read_csv_tactics()
    print(f"Found {len(csv_tactics)} CSV tactics")

    print("\nMerging tactics...")
    merged = merge_tactics(existing, csv_tactics)
    print(f"Merged total: {len(merged)} tactics")

    print("\nGenerating merged data.js...")
    js_content = generate_merged_js(merged)

    print("\nWriting to data_merged.js...")
    with open('../assets/js/data_merged.js', 'w', encoding='utf-8') as f:
        f.write(js_content)

    print(f"\nSuccess! Created data_merged.js with {len(merged)} tactics")

    # Print statistics
    from collections import Counter
    categories = Counter(t.get('category') for t in merged)
    difficulties = Counter(t.get('difficulty') for t in merged)
    with_chinese = sum(1 for t in merged if t.get('nameCn'))

    print(f"\n=== STATISTICS ===")
    print(f"Total tactics: {len(merged)}")
    print(f"With Chinese translation: {with_chinese}")
    print(f"Without Chinese: {len(merged) - with_chinese}")
    print(f"\nBy category:")
    for category, count in sorted(categories.items()):
        print(f"  {category}: {count}")
    print(f"\nBy difficulty:")
    for difficulty, count in sorted(difficulties.items()):
        print(f"  {difficulty}: {count}")
