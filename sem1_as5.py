"""
Assignment 5: Resizing and Cropping Images
Description:

Load the image example.jpg using OpenCV and Pillow.
Resize the image to 300x300 pixels.
Crop a central region of size 200x200 pixels.
Save the resulting images.
"""


import cv2
import numpy as np
# 1. Load the image example.jpg using OpenCV and Pillow.
path = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/example.jpg"
img = cv2.imread(path)

# 2. Resize the image to 300x300 pixels.
img_resized = cv2.resize(img, (300, 300))

# 3. Crop a central region of size 200x200 pixels.
img_cropped = img_resized - np.pad(img_resized[50:250, 50:250, :], ((50, 50), (50, 50), (0, 0)), mode='constant', constant_values=0)

# 4. Save the resulting images.
save_dir = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/output/"
cv2.imwrite(save_dir + 'cropped.jpg', img_cropped)
print("done")





