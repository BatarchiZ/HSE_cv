
"""Assignment 3: Saving Images in Different Formats
Description:

Load the image example.jpg using OpenCV and save it as a PNG file.
Load the image example.jpg using Pillow and save it as a JPEG file.
Verify the saved files."""

import cv2
from PIL import Image
path = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/example.jpg"
# 1. Load the image example.jpg using OpenCV and save it as a PNG file.
img = cv2.imread(path)
save_path = "output/example.png"
cv2.imwrite(save_path, img)

# 2. Load the image example.jpg using Pillow and save it as a JPEG file.
img = Image.open(path)
save_path = "output/example.jpg"
img.save(save_path)

