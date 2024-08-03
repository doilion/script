import argparse
import os
import json
import shutil
from tqdm import tqdm

def check_criteria(shapes, min_instance, min_salient, min_camouflage):
    instance_count = len(shapes)
    salient_count = sum(1 for shape in shapes if "salient" in shape['label'])
    camouflage_count = sum(1 for shape in shapes if "cam" in shape['label'])

    return (instance_count > min_instance or
            salient_count > min_salient or
            camouflage_count > min_camouflage)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="检查并复制满足条件的json文件，并记录有错误的文件名")
    parser.add_argument("-d", "--dir", default=r"D:\test\1", help="json文件所在目录")
    parser.add_argument("-o", "--out", default=r"D:\test\2", help="输出目录")
    parser.add_argument("-m", "--min", type=int, default=20, help="最小实例个数")
    parser.add_argument("-s", "--salient", type=int, default=5, help="最小显著实例个数")
    parser.add_argument("-c", "--camouflage", type=int, default=5, help="最小伪装实例个数")
    args = parser.parse_args()

    if not os.path.exists(args.out):
        os.makedirs(args.out)

    error_log_path = os.path.join(args.dir, 'logs.txt')
    with open(error_log_path, 'w') as log_file:
        for filename in tqdm(os.listdir(args.dir)):
            if not filename.endswith('.json'):
                continue

            try:
                with open(os.path.join(args.dir, filename), "r") as f:
                    labelme_json = json.load(f)

                if check_criteria(labelme_json["shapes"], args.min, args.salient, args.camouflage):
                    shutil.copy(os.path.join(args.dir, filename), os.path.join(args.out, filename))
            except json.JSONDecodeError as e:
                # 记录无法解析的文件名及错误信息
                log_file.write(f"{filename}: {str(e)}\n")
