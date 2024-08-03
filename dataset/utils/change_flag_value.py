import os
import json

"""
    此脚本用于修改json文件存在的flags字段为null导致labelme无法打开的情况
    主要是用于此 将 null值 修改为 {}
"""
def fix_flags_in_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if 'shapes' in data:
        for shape in data['shapes']:
            if shape.get('flags') is None:
                shape['flags'] = {}

    with open(file_path, 'w', encoding='utf-8') as file:
        json.dump(data, file, indent=4, ensure_ascii=False)

def traverse_and_fix(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                fix_flags_in_json(file_path)
                print(f"Fixed file: {file_path}")

if __name__ == "__main__":
    directory_path = r"F:\dataset\标注完的300"
    traverse_and_fix(directory_path)
