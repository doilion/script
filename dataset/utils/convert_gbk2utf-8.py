import os
import chardet

"""
    修改对应文件的编码格式转换成utf-8
"""


def convert_to_utf8(file_path):
    with open(file_path, 'rb') as file:
        raw_data = file.read()

    result = chardet.detect(raw_data)
    encoding = result['encoding']

    if encoding is None:
        print(f"Could not detect encoding for {file_path}. Skipping.")
        return

    if encoding.lower() != 'utf-8':
        print(f"Converting {file_path} from {encoding} to utf-8")
        with open(file_path, 'r', encoding=encoding, errors='ignore') as file:
            content = file.read()

        with open(file_path, 'w', encoding='utf-8') as file:
            file.write(content)
    else:
        print(f"{file_path} is already utf-8 encoded")


def traverse_and_convert(directory_path):
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                convert_to_utf8(file_path)


if __name__ == "__main__":
    directory_path = r"F:\dataset\标注完的300"
    traverse_and_convert(directory_path)
