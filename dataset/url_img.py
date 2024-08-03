import requests
from bs4 import BeautifulSoup
import os
from urllib.parse import urljoin, urlparse
from PIL import Image
from io import BytesIO

def fetch_images(url, folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    images = soup.find_all('img')  # 搜索所有图片标签

    for i, img in enumerate(images):
        src = img.get('src')
        if not src.startswith('https'):  # 确保src是完整的URL
            src = urljoin(url, src)

        # 跳过data:image/svg+xml
        if src.startswith('data:'):
            print(f"Skipping non-downloadable image {src}")
            continue

        try:
            image_response = requests.get(src)
            image_response.raise_for_status()  # 确保请求成功
            img_format = Image.open(BytesIO(image_response.content)).format.lower()
            if not img_format:
                continue

            # 获取原始图片格式并以该格式保存
            output_file_name = f"image_{i:05d}.{img_format}"
            output_file_path = os.path.join(folder_path, output_file_name)

            with open(output_file_path, 'wb') as file:
                file.write(image_response.content)
            print(f"Downloaded and saved {src} as {output_file_name}")

        except Exception as e:
            print(f"Could not download {src}: {e}")

# 使用示例
url = 'https://www.pinterest.com/pin/crocodile-fishbyjoerglingnau--335096028532260032/'
folder_path = './downloaded_images'
fetch_images(url, folder_path)
