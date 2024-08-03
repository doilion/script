import os
import shutil
import random

"""
    对数据集进行一个划分
"""

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)


def split_dataset(directory_path, train_ratio=0.8, train_dir='train', test_dir='test'):
    # 获取目录下所有的文件
    files = [f for f in os.listdir(directory_path) if os.path.isfile(os.path.join(directory_path, f))]

    # 打乱文件列表
    random.shuffle(files)

    # 计算训练集和测试集的大小
    train_size = int(len(files) * train_ratio)
    train_files = files[:train_size]
    test_files = files[train_size:]

    # 创建训练集和测试集文件夹
    train_path = os.path.join(directory_path, train_dir)
    test_path = os.path.join(directory_path, test_dir)

    create_dir(train_path)
    create_dir(test_path)

    # 移动文件到训练集文件夹
    for file in train_files:
        src = os.path.join(directory_path, file)
        dst = os.path.join(train_path, file)
        shutil.move(src, dst)
        print(f"Moved {file} to {train_path}")

    # 移动文件到测试集文件夹
    for file in test_files:
        src = os.path.join(directory_path, file)
        dst = os.path.join(test_path, file)
        shutil.move(src, dst)
        print(f"Moved {file} to {test_path}")


if __name__ == "__main__":
    directory_path = r"F:\dataset\new_ucis5k\all\data"
    split_dataset(directory_path)
