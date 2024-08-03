import os
import json

""" 
    此脚本用于修改因为下面类似错误导致的报错信息：
        ValueError: path is on mount 'D:', start on mount 'F:'
"""


def convert_image_path_to_absolute(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if 'imagePath' in data:
        image_path = data['imagePath']
        absolute_image_path = os.path.abspath(os.path.join(os.path.dirname(file_path), image_path))

        # 修改盘符为F:
        if absolute_image_path[1:3] == ':\\':
            absolute_image_path = 'F:' + absolute_image_path[2:]

        data['imagePath'] = absolute_image_path

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Updated {file_path}: converted imagePath to absolute path with F: drive")


def traverse_and_modify(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                convert_image_path_to_absolute(file_path)


if __name__ == "__main__":
    directory_path = r"F:\dataset\new_ucis5k\all\data"
    traverse_and_modify(directory_path)
