"""
Assignment 10: Converting Between OpenCV and Pillow Formats
Description:

Load the image example.jpg using OpenCV.
Convert it to Pillow format, change its color space, and save it.
Load the image saved_gray_pil.png using Pillow.
Convert it back to OpenCV format, change its color space, and save it.
"""

import cv2
from PIL import Image, ImageOps 
import numpy as np

# 1. Load the image example.jpg using OpenCV.
path = '/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/example.jpg'
img = cv2.imread(path)

# 2. Convert it to Pillow format, change its color space, and save it.
img_convertcolor = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
img_PIL = Image.fromarray(img_convertcolor)
img_PIL = img_PIL.convert('L') 

output_dir = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/output/"
img_PIL.save(output_dir + "saved_gray_pil.png")

# 3. Load the image saved_gray_pil.png using Pillow.
img = Image.open(output_dir + "saved_gray_pil.png")

# 4. Convert it back to OpenCV format, change its color space ??? it is gray already innit, and save it.
img = np.array(img)
img = img[:, :]
cv2.imwrite(output_dir + "task10.jpg", img)
print("done")
