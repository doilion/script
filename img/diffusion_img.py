import cv2
import numpy as np
from imagededup.utils.image_utils import load_image

def add_significant_gaussian_noise(image, mean=0, var=255):
    # 'var'设置为255的最大值，以便在时间步长为最大时得到几乎全是噪声的图像
    row, col, ch = image.shape
    sigma = var ** 0.5
    gauss = np.random.normal(mean, sigma, (row, col, ch))
    gauss = gauss.reshape(row, col, ch)
    noisy = image + gauss
    noisy = np.clip(noisy, 0, 255)  # Clip the values to keep within valid image data range
    return noisy.astype(np.uint8)

def simulate_significant_diffusion(image, time_step, max_time=2000):
    # 方差现在将是时间步长的非线性函数，以便在2000步骤时产生大量的噪声
    var = (time_step / max_time) * 255  # 此时不对方差进行平方，直接线性增加
    noisy_image = add_significant_gaussian_noise(image, var=var)
    return noisy_image

def process_and_save_image_with_significant_noise(input_image_path, output_image_path, time_step):
    image = load_image(input_image_path)
    diffused_image = simulate_significant_diffusion(image, time_step)

    # 保存处理后的图片
    cv2.imwrite(output_image_path, diffused_image)

# 设置时间步长为2000，以符合注释中的说明
time_step = 2000
input_image_path = "set_f114.jpg"
output_image_path = "set_f114_itration_{}.jpg".format(time_step)

# 重新处理图片并设置时间步长为2000，应产生接近纯噪声的图片
process_and_save_image_with_significant_noise(input_image_path, output_image_path, time_step=time_step)
