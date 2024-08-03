import json
import pandas as pd

# 加载COCO数据集的JSON文件
with open(r'E:\dataset\UCIS5K\UCIS5K\anntoation\test.json') as f:
    coco = json.load(f)

# 例如，我们检查images和annotations部分
images_df = pd.DataFrame(coco['images'])
annotations_df = pd.DataFrame(coco['annotations'])

# 检查空值
print("Images DataFrame null values:")
print(images_df.isnull().sum())  # 显示每列的空值计数

print("\nAnnotations DataFrame null values:")
print(annotations_df.isnull().sum())  # 显示每列的空值计数
