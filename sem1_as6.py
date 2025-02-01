"""
Assignment 6: Rotating Images at Arbitrary Angles
Description:

Load the image example.jpg using OpenCV and Pillow.
Rotate the image 45 degrees clockwise.
Rotate the image 45 degrees counterclockwise.
Save the results.
"""

import cv2
import numpy as np
# 1. Load the image example.jpg using OpenCV and Pillow.

path = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/example.jpg"
img = cv2.imread(path)

def rotate_image(image, angle):
  image_center = tuple(np.array(image.shape[1::-1]) / 2)
  rot_mat = cv2.getRotationMatrix2D(image_center, angle, 1.0)
  result = cv2.warpAffine(image, rot_mat, image.shape[1::-1], flags=cv2.INTER_LINEAR)
  return result

# 2. Rotate the image 45 degrees clockwise.
img_clockwise = rotate_image(img, 45)

# 3. Rotate the image 45 degrees counterclockwise.
img_anticlockwise = rotate_image(img, 315)

output_dir = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/output/"
for indx, i in enumerate([img_clockwise, img_anticlockwise]):
  cv2.imwrite(output_dir + str(indx) + "_rotation.jpg", i)

print("done")

