"""Assignment 8: Image Histogram and Visualization
Description:

Load the image example.jpg in grayscale using OpenCV and Pillow.
Calculate the pixel intensity histogram.
Visualize the histogram.
Save the results.
"""

import cv2 
from PIL import Image
import matplotlib.pyplot as plt

# 0. Load the image example.jpg in grayscale using OpenCV and Pillow.
path = '/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/example.jpg'
img = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
img_reshaped = img.reshape(-1)

# 1. Calculate the pixel intensity histogram.
fig, ax = plt.subplots()
ax.hist(img_reshaped)

# 2. Visualize the histogram.
plt.show()

# 3. Save the results.
output_dir ='/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/output/'
fig.savefig(output_dir + 'hist.png')

