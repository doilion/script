import os
import json


def update_file_names_in_coco_json(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if 'images' in data:
        for image in data['images']:
            # 提取最后的文件名部分
            image['file_name'] = os.path.basename(image['file_name'])

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Updated file names in {file_path}")


if __name__ == "__main__":
    file_path = r"F:\dataset\new_ucis5k\all\train_coco\annotations.json"
    update_file_names_in_coco_json(file_path)
