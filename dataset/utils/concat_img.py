import os
from PIL import Image

def create_dir(directory):
    if not os.path.exists(directory):
        os.makedirs(directory)

def concatenate_images(img1_path, img2_path, output_path):
    img1 = Image.open(img1_path)
    img2 = Image.open(img2_path)

    # 获取图像尺寸
    width1, height1 = img1.size
    width2, height2 = img2.size

    # 创建新图像，宽度是两幅图像宽度之和，高度取最大值
    new_img = Image.new('RGB', (width1 + width2, max(height1, height2)))

    # 将两幅图像粘贴到新图像上
    new_img.paste(img1, (0, 0))
    new_img.paste(img2, (width1, 0))

    new_img.save(output_path)
    print(f"Saved concatenated image to {output_path}")

def process_directories(dir1, dir2, output_dir):
    create_dir(output_dir)

    for file_name in os.listdir(dir1):
        if file_name in os.listdir(dir2):
            img1_path = os.path.join(dir1, file_name)
            img2_path = os.path.join(dir2, file_name)
            output_path = os.path.join(output_dir, file_name)
            concatenate_images(img1_path, img2_path, output_path)

if __name__ == "__main__":
    dir1 = r"F:\dataset\new_ucis5k\all\check_data\JPEGImages"
    dir2 = r"F:\dataset\new_ucis5k\all\check_data\Visualization"
    output_dir = r"F:\dataset\new_ucis5k\all\check_data\check"

    process_directories(dir1, dir2, output_dir)
