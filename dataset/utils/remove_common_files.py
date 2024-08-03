import os

def remove_common_files(dir1, dir2):
    files_in_dir2 = set(os.listdir(dir2))

    for file_name in os.listdir(dir1):
        if file_name in files_in_dir2:
            file_path = os.path.join(dir1, file_name)
            os.remove(file_path)
            print(f"Removed {file_path}")

if __name__ == "__main__":
    dir1 = r"F:\dataset\new_ucis5k\all\check_data\Visualization"
    dir2 = r"F:\dataset\new_ucis5k\all\check_data\check"

    remove_common_files(dir1, dir2)
