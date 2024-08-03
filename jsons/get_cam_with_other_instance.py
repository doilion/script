import os
import json
from tqdm import tqdm

def find_and_copy_files_with_cam_labels(source_directory, target_directory):
    """
    遍历指定目录，找出所有标注实例名称中含有 'cam' 的 JSON 文件，并将这些文件复制到目标目录。
    同时，保留这些 JSON 文件中的所有标签。
    :param source_directory: 要搜索的源目录
    :param target_directory: 复制到的目标目录
    :return: None
    """
    # 确保目标目录存在，如果不存在则创建
    if not os.path.exists(target_directory):
        os.makedirs(target_directory)

    # 遍历源目录中的所有文件
    for root, dirs, files in tqdm(os.walk(source_directory)):
        for file in files:
            if file.endswith('.json'):
                file_path = os.path.join(root, file)
                # 读取 JSON 文件内容
                with open(file_path, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                    # 检查是否存在包含 'cam' 的标签
                    shapes_with_cam = [shape for shape in data.get('shapes', []) if 'mollusk' in shape.get('label', '')]

                    # 如果存在含 'cam' 的标签，则复制文件
                    if shapes_with_cam:
                        target_file_path = os.path.join(target_directory, file)
                        # 将原始 JSON 数据写入新位置
                        with open(target_file_path, 'w', encoding='utf-8') as f_target:
                            json.dump(data, f_target, indent=4)
                        print(f"Copied '{file_path}' to '{target_file_path}'")

# 使用示例
source_directory = r'D:\dataset\all'  # 替换为实际的源目录路径
target_directory = r'D:\dataset\test-qs'  # 替换为实际的目标目录路径
find_and_copy_files_with_cam_labels(source_directory, target_directory)
