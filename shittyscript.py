from PIL import Image, ImageFile
import os
from math import floor

ImageFile.LOAD_TRUNCATED_IMAGES = True

# INSTALLATION
# place this script into your stable-diffusion-webui folder

# USING
# enter both the path to the images you wish to resize and the path you would like to save them to
# ensure your path is inbetween the quotations and uses double backslashes
# save this file
# open a command prompt in your stable-diffusion-webui folder and enter .\venv\scripts\activate
# next enter python shittyscript.py
# the script will then proceed to do its thing


path = ""  # path for file containing training images, ensure you use double \\
save = ""  # path for file to save processed images, ensure you use double \\
imgformat = "png"  # change to "jpg" if you want to save as .jpg instead


print('loading images from directory')
for file in os.listdir(path):
    if file.endswith(('jpg', 'png')):
        image = path + "\\" + file
        img = Image.open(image)
        print(img)
        width = img.size[0]
        height = img.size[1]
        print(width)
        print(height)
        new_width = 64 * floor(width / 64)
        new_height = 64 * floor(height / 64)
        size = (new_width, new_height)
        print(size)
        img = img.resize(size, 1)
        print(img.resize)
        img.save(save + "\\" + file, imgformat)
        print(img.save)
