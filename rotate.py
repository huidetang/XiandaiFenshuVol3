import glob
from os import getcwd
from os.path import join

from PIL import Image

def rotate(path):
    image = Image.open(path)
    rotated_image = image.rotate(90, expand=True)
    return rotated_image

def bundle_rotate(dir):
    path_list = []
    for ext in ('*.gif', '*.png', '*.jpg', '*.jpeg'):
        path_list.extend(glob.glob(join(dir, ext)))

    for i in path_list:
        print(i)
        img = rotate(i)
        img.save(i)
        print(i)
    return

image_path = getcwd() + "/images"
print(image_path)
bundle_rotate(image_path)
