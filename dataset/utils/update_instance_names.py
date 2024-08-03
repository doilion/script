import os
import json


def update_instance_names(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    if 'shapes' in data:
        for shape in data['shapes']:
            shape['label'] = 'foreground'

        with open(file_path, 'w', encoding='utf-8') as file:
            json.dump(data, file, indent=4, ensure_ascii=False)
        print(f"Updated instance names in {file_path}")


def traverse_and_update(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                update_instance_names(file_path)


if __name__ == "__main__":
    directory_path =  r"F:\dataset\new_ucis5k\all\test"
    traverse_and_update(directory_path)
