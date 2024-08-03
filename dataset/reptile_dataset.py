from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
import requests

def download_image(image_url, folder_path, count):
    response = requests.get(image_url)
    if response.status_code == 200:
        with open(os.path.join(folder_path, f'image_{count}.jpg'), 'wb') as f:
            f.write(response.content)

def fetch_google_images(query, num_images, download_path):
    if not os.path.exists(download_path):
        os.makedirs(download_path)

    # 设置WebDriver路径
    driver = webdriver.Chrome(executable_path='path_to_chromedriver')  # 更新为你的Chromedriver路径
    driver.get('https://www.google.com')

    # 找到搜索框，输入查询并提交
    box = driver.find_element_by_name('q')
    box.send_keys(query + ' images')
    box.send_keys(Keys.ENTER)

    # 跳转到图片标签
    images_link = driver.find_elements_by_link_text('Images')
    if images_link:
        images_link[0].click()
    else:
        return  # 如果没有找到图片链接则返回

    # 滚动加载更多图片
    last_height = driver.execute_script('return document.body.scrollHeight')
    while len(driver.find_elements_by_css_selector('img')) < num_images:
        driver.execute_script('window.scrollTo(0, document.body.scrollHeight)')
        time.sleep(3)  # 等待页面加载
        new_height = driver.execute_script('return document.body.scrollHeight')
        if new_height == last_height:
            break
        last_height = new_height

    # 下载图片
    images = driver.find_elements_by_css_selector('img')
    for count, img in enumerate(images[:num_images]):
        src = img.get_attribute('src')
        try:
            download_image(src, download_path, count)
        except Exception as e:
            print(f"Failed to download image {count}: {e}")

    driver.quit()

# 使用示例
query = "underwater camouflage"
num_images = 10
download_path = './downloaded_images'
fetch_google_images(query, num_images, download_path)
