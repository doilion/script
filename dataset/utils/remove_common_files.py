import os

def remove_files_with_common_prefix(dir1, dir2):
    # 获取dir2中所有文件的前缀集合
    prefix_set = {os.path.splitext(f)[0] for f in os.listdir(dir2)}

    # 遍历dir1中的文件
    for file_name in os.listdir(dir1):
        prefix = os.path.splitext(file_name)[0]
        # 检查前缀是否在dir2的前缀集合中
        if prefix not in prefix_set:
            file_path = os.path.join(dir1, file_name)
            os.remove(file_path)
            print(f"Removed {file_path}")

if __name__ == "__main__":
    dir1 = r"F:\dataset\new_ucis5k\all\train_json"
    dir2 = r"F:\dataset\new_ucis5k\all\train"

    remove_files_with_common_prefix(dir1, dir2)