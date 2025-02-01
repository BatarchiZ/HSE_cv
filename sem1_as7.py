"""
Assignment 7: Adjusting Contrast and Brightness
Description:

Load the image example.jpg using OpenCV and Pillow.
Increase the image contrast by 50% and brightness by 30 units.
Save the modified images.
"""
import cv2
from PIL import Image
import numpy as np
# 1. Load the image example.jpg using OpenCV and Pillow.
path = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/example.jpg"
img = cv2.imread(path)

# 2. Increase the image contrast by 50% and brightness by 30 units.
contrast = 1.5
brightness = 30
img_altered = cv2.addWeighted(img, contrast, np.zeros(img.shape, img.dtype), 0, brightness)

# 3. Save the modified images.
output_dir = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/output/"
cv2.imwrite(output_dir + "bright_contrast.jpg", img)

print("done")
