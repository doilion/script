import os

"""
    用于对目录下面的所有文件进行一个重命名
"""

def rename_json_files(directory_path, prefix='train_'):
    json_files = [f for f in os.listdir(directory_path) if f.endswith('.json')]
    json_files.sort()  # Ensure the files are processed in a consistent order

    for i, old_name in enumerate(json_files, start=1):
        new_name = f"{prefix}{i:04d}.json"
        old_path = os.path.join(directory_path, old_name)
        new_path = os.path.join(directory_path, new_name)

        os.rename(old_path, new_path)
        print(f"Renamed {old_name} to {new_name}")


if __name__ == "__main__":
    directory_path = r"F:\dataset\new_ucis5k\all\train"
    rename_json_files(directory_path)
