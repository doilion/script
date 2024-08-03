import os
import shutil
from PIL import Image
from pathlib import Path
from tqdm import tqdm

def convert_to_jpg(source_path, dest_path):
    # 创建目标文件夹，如果不存在的话
    os.makedirs(dest_path, exist_ok=True)
    # 初始化图片编号
    img_number = 278

    # 遍历源文件夹
    for root, dirs, files in tqdm(os.walk(source_path)):
        for file in files:
            # 检查文件是否为图片格式
            if file.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
                # 构建完整的文件路径
                full_file_path = os.path.join(root, file)
                # 读取图片
                with Image.open(full_file_path) as img:
                    # 转换图片到JPG格式
                    rgb_img = img.convert('RGB')
                    # 构建目标文件名和路径
                    dest_file_path = os.path.join(dest_path, f"{str(img_number).zfill(5)}.jpg")
                    # 保存图片
                    rgb_img.save(dest_file_path, 'JPEG')
                    # 更新图片编号
                    img_number += 1

# 源文件夹和目标文件夹路径
source_folder = r'D:\code\script\dataset\downloaded_images'
destination_folder = r'E:\dataset\output'

# 调用函数
convert_to_jpg(source_folder, destination_folder)
