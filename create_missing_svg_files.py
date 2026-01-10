#!/usr/bin/env python3
"""
创建data.js中引用但实际不存在的SVG文件
通过复制或创建符号链接的方式
"""

import os
import shutil

# 基础路径
BASE_PATH = r"\\DXP4800-SUI\personal_folder\400 Coding\NFL Strategies"

# 需要创建的文件映射: 缺失的路径 -> 源文件路径
FILE_MAPPINGS = {
    # Offense formations
    'assets/images/offense/singleback-formation.svg': 'assets/images/offense-formation/singleback-formation.svg',
    'assets/images/offense/pistol-formation.svg': 'assets/images/offense-formation/pistol-formation.svg',
    'assets/images/offense/empty-backfield.svg': 'assets/images/offense-formation/empty-backfield.svg',
    'assets/images/offense/wildcat-formation.svg': 'assets/images/offense-formation/wildcat-formation.svg',

    # Routes
    'assets/images/routes/out-route.svg': 'assets/images/passing-routes/out-route.svg',
    'assets/images/routes/post-route.svg': 'assets/images/passing-routes/post-route.svg',
    'assets/images/routes/corner-route.svg': 'assets/images/passing-routes/corner-route.svg',
    'assets/images/routes/curl-route.svg': 'assets/images/passing-routes/curl-route.svg',
    'assets/images/routes/drag-route.svg': 'assets/images/passing-routes/drag-route.svg',

    # Defense coverage
    'assets/images/defense/cover-3.svg': 'assets/images/defense-coverage/cover-3.svg',
    'assets/images/defense/cover-1.svg': 'assets/images/defense-coverage/cover-1.svg',
    'assets/images/defense/cover-0.svg': 'assets/images/defense-coverage/cover-0.svg',
    'assets/images/defense/cover-4.svg': 'assets/images/defense-coverage/cover-4.svg',
    'assets/images/defense/cover-6.svg': 'assets/images/defense-coverage/cover-6.svg',

    # Running plays
    'assets/images/running/inside-zone.svg': 'assets/images/running-plays/inside-zone.svg',
    'assets/images/running/outside-zone.svg': 'assets/images/running-plays/outside-zone.svg',
    'assets/images/running/power-run.svg': 'assets/images/running-plays/power-run.svg',
    'assets/images/running/counter-run.svg': 'assets/images/running-plays/counter-run.svg',
    'assets/images/running/draw-play.svg': 'assets/images/running-plays/draw-play.svg',
    'assets/images/running/toss-sweep.svg': 'assets/images/running-plays/toss-sweep.svg',
    'assets/images/running/trap-play.svg': 'assets/images/running-plays/trap-play.svg',
}

def create_missing_files():
    """创建缺失的文件"""
    print("="*60)
    print("创建缺失的SVG文件")
    print("="*60)

    created = 0
    already_exist = 0
    errors = 0

    for dest_rel, src_rel in FILE_MAPPINGS.items():
        dest_path = os.path.join(BASE_PATH, dest_rel)
        src_path = os.path.join(BASE_PATH, src_rel)

        # 检查目标文件是否已存在
        if os.path.exists(dest_path):
            print(f"[已存在] {dest_rel}")
            already_exist += 1
            continue

        # 检查源文件是否存在
        if not os.path.exists(src_path):
            print(f"[错误] 源文件不存在: {src_rel}")
            errors += 1
            continue

        # 确保目标目录存在
        dest_dir = os.path.dirname(dest_path)
        os.makedirs(dest_dir, exist_ok=True)

        # 复制文件
        try:
            shutil.copy2(src_path, dest_path)
            print(f"[创建] {dest_rel} <- {src_rel}")
            created += 1
        except Exception as e:
            print(f"[错误] 创建 {dest_rel} 失败: {e}")
            errors += 1

    print("\n" + "="*60)
    print(f"总结:")
    print(f"  创建: {created}")
    print(f"  已存在: {already_exist}")
    print(f"  错误: {errors}")
    print("="*60)

if __name__ == '__main__':
    create_missing_files()
