import argparse
from pathlib import Path
from PIL import Image
from torchvision.transforms import functional as trans_fn
from tqdm import tqdm

def resize_and_convert(img, scale_factor=2, resample=Image.BICUBIC):
    """
    Resize the image by a scale factor using bicubic resampling and return the result.
    The new size is calculated by multiplying the original size by the scale factor,
    ensuring the width and height are correctly scaled.
    """
    # Get the current size of the image
    width, height = img.size  # PIL uses (width, height) order

    # Calculate the new dimensions
    new_width = int(width * scale_factor)
    new_height = int(height * scale_factor)

    # Resize the image using the new dimensions
    img = img.resize((new_width, new_height), resample)
    return img


def process_image(file_path, out_dir, scale_factor=2):
    """
    Load an LR image, upscale it, and save the SR image in JPEG format with the same filename.
    """
    img = Image.open(file_path)
    img = img.convert('RGB')  # Ensure image is in RGB format
    sr_img = resize_and_convert(img, scale_factor=scale_factor, resample=Image.BICUBIC)

    # Construct SR image filename using the same filename as the LR image
    sr_filename = file_path.name
    sr_img.save(out_dir / sr_filename, 'JPEG')  # Save in JPEG format

def upscale_images(lr_dir, sr_dir, scale_factor=2):
    """
    Upscale all images in the lr_dir and save them to sr_dir, showing a progress bar.
    """
    lr_dir = Path(lr_dir)
    sr_dir = Path(sr_dir)
    sr_dir.mkdir(parents=True, exist_ok=True)

    lr_images = list(lr_dir.glob("*.jpg"))  # Collect all .jpg files in the lr_dir
    for lr_img_path in tqdm(lr_images, desc="Processing Images"):  # Wrap the loop with tqdm for the progress bar
        process_image(lr_img_path, sr_dir, scale_factor=scale_factor)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description="Upscale LR images to SR images using bicubic resampling.")
    parser.add_argument("-l", '--lr_dir', type=str, required=True, help="Directory containing LR images.")
    parser.add_argument("-s", '--sr_dir', type=str, required=True, help="Directory to save upscaled SR images.")
    parser.add_argument('--scale_factor', type=int, default=2, help="Factor by which images will be upscaled.")

    args = parser.parse_args()

    upscale_images(args.lr_dir, args.sr_dir, args.scale_factor)
