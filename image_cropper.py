
import os
from PIL import Image

def main():
    image_files = os.listdir(os.path.abspath('Images'))
    for file_path in image_files:
        print(file_path);
        full_path = os.path.abspath(os.path.join("Images", file_path))
        image = Image.open(full_path)

        width, height = image.size
        left = 0
        top = 15
        right = width
        bottom = height - 15

        cropped_image = image.crop((left, top, right, bottom))
        cropped_image.save(full_path)

main()