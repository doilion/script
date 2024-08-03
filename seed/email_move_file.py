import os
import shutil

# 源目录和目标目录
source_dir = r'C:\Users\DELL\Desktop\1'
target_dir = r'C:\Users\DELL\Desktop\网安实验'

# 递归遍历目录并将文件复制到目标目录中
def copy_files(src, dst):
    for item in os.listdir(src):
        item_path = os.path.join(src, item)
        if os.path.isfile(item_path):
            shutil.copy(item_path, dst)
        elif os.path.isdir(item_path):
            copy_files(item_path, dst)

# 创建目标目录
if not os.path.exists(target_dir):
    os.makedirs(target_dir)

# 开始拷贝文件
copy_files(source_dir, target_dir)

print('文件提取完成，已将所有文件复制到目标目录中。')