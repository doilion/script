import os
import shutil

"""
    复制新增加的add的数据集图片
"""
def copy_files_with_add(source_folder, target_folder):
    # 检查目标文件夹是否存在，如果不存在，则创建它
    if not os.path.exists(target_folder):
        os.makedirs(target_folder)

    # 遍历源文件夹中的所有文件
    for filename in os.listdir(source_folder):
        # 检查文件名是否包含'add'
        if 'add' in filename.lower():
            # 构建源文件和目标文件的完整路径
            source_file = os.path.join(source_folder, filename)
            target_file = os.path.join(target_folder, filename)

            # 复制文件
            shutil.copy(source_file, target_file)
            print(f"Copied {filename} to {target_folder}")

# 指定源文件夹和目标文件夹的路径
source_folder = r'E:\dataset\output'
target_folder = r'E:\dataset\output_with_add'
copy_files_with_add(source_folder, target_folder)
