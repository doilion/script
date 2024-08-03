import os
import json

"""
    此脚本用于去除实例名称种不含有cam的实例
        可以修改成其它的变成通用型脚本
"""
def remove_non_cam_shapes(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if 'shapes' in data:
        original_shape_count = len(data['shapes'])
        data['shapes'] = [shape for shape in data['shapes'] if 'cam' in shape['label'].lower()]
        new_shape_count = len(data['shapes'])

        if original_shape_count != new_shape_count:
            with open(file_path, 'w', encoding='utf-8') as file:
                json.dump(data, file, indent=4, ensure_ascii=False)
            print(f"Updated {file_path}: removed {original_shape_count - new_shape_count} shapes")


def traverse_and_modify(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                remove_non_cam_shapes(file_path)


if __name__ == "__main__":
    directory_path = r"F:\dataset\标注完的300"
    traverse_and_modify(directory_path)
