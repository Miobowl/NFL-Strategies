#!/usr/bin/env python3
"""
验证data.js中的image路径是否都存在对应的SVG文件
"""

import os
import re

# 基础路径
BASE_PATH = r"\\DXP4800-SUI\personal_folder\400 Coding\NFL Strategies"
DATA_JS_PATH = os.path.join(BASE_PATH, "assets", "js", "data.js")

def extract_image_paths():
    """从data.js中提取所有image路径"""
    with open(DATA_JS_PATH, 'r', encoding='utf-8') as f:
        content = f.read()

    # 提取所有 image: 'path' 的路径
    pattern = r"image:\s*'([^']+)'"
    matches = re.findall(pattern, content)

    return matches

def check_files():
    """检查所有image路径对应的文件是否存在"""
    print("="*60)
    print("验证 data.js 中的 SVG 图像路径")
    print("="*60)

    image_paths = extract_image_paths()
    print(f"\n找到 {len(image_paths)} 个图像路径\n")

    missing = []
    existing = []

    for img_path in image_paths:
        full_path = os.path.join(BASE_PATH, img_path)

        if os.path.exists(full_path):
            existing.append(img_path)
            print(f"  [OK] {img_path}")
        else:
            missing.append(img_path)
            print(f"  [MISSING] {img_path}")

    print("\n" + "="*60)
    print(f"总结:")
    print(f"  存在: {len(existing)}/{len(image_paths)}")
    print(f"  缺失: {len(missing)}/{len(image_paths)}")
    print("="*60)

    if missing:
        print("\n缺失的文件:")
        for path in missing:
            print(f"  - {path}")

if __name__ == '__main__':
    check_files()
