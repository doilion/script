"""
    对于图片类型进行转换，全部转换成jpg格式的图片
"""

import os
from PIL import Image

def convert_and_rename_images(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    files = sorted(os.listdir(input_folder))
    count = 282
    supported_formats = ('.webp', '.png', '.bmp', '.tiff', '.jpeg', '.jpg', '.gif')

    for file in files:
        file_path = os.path.join(input_folder, file)
        if os.path.isfile(file_path) and file.lower().endswith(supported_formats):
            try:
                with Image.open(file_path) as img:
                    output_file_name = f"add_{count:05d}.jpg"
                    output_file_path = os.path.join(output_folder, output_file_name)
                    img.convert('RGB').save(output_file_path, "JPEG")
                    print(f"Converted and saved {file} as {output_file_name}")
                    count += 1
            except Exception as e:
                print(f"Could not process file {file}: {e}")

input_folder = r'E:\dataset\collect'
output_folder = r'E:\dataset\output'
convert_and_rename_images(input_folder, output_folder)
