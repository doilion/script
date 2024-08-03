import os
from PIL import Image
from tqdm import tqdm
import imagehash

"""
    用于数据集去重
"""
def remove_duplicates(folder_path):
    # 用于存储图片哈希值和文件路径的字典
    hashes = {}
    # 遍历文件夹中的所有文件
    for filename in tqdm(os.listdir(folder_path)):
        # 构建完整的文件路径
        file_path = os.path.join(folder_path, filename)
        # 打开并计算每张图片的哈希值
        with Image.open(file_path) as img:
            img_hash = imagehash.phash(img)

        # 检查哈希值是否已经存在
        if img_hash in hashes:
            # 如果存在哈希值且文件名包含'add'
            if 'add' in filename.lower():
                # 说明图片是重复的且名字中包含“add”，删除它
                print(f"Removing duplicate: {file_path}")
                os.remove(file_path)
            else:
                # 如果哈希值已存在但文件名不包含'add'，忽略该文件的删除
                continue
        else:
            # 如果哈希值不在字典中，添加它
            hashes[img_hash] = filename

# 指定你的图片文件夹路径
folder_path = r'E:\dataset\dataset-all'
remove_duplicates(folder_path)
