# Modules
from PIL import Image, ImageEnhance, ImageFilter
import os

# Paths
path1 = "./pictures"
export_path = './edited_img/'

print(path1)
print(export_path)

for file in os.listdir(path1):
    print(file)
    img = Image.open(f"{path1}/{file}")
    edit = img.filter(ImageFilter.SHARPEN)

    clean_name = os.path.splitext(file)[0]
    edit.save(f"{export_path}/{clean_name}_edited.jpg")

