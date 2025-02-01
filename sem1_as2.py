import cv2
from PIL import Image
print("hello world")

"""Assignment 2: Loading and Displaying Images
Description:

Download the image example.jpg and place it in the project folder cv_seminar1.
Write a Python script to load and display the image using OpenCV.
Write a similar script to load and display the image using Pillow.
Compare the image display results in OpenCV and Pillow."""

# 1. Write a Python script to load and display the image using OpenCV.
path ="/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/example.jpg"
img = cv2.imread(path)

window_name = 'image'
cv2.imshow(window_name, img)
cv2.waitKey(0)
cv2.destroyAllWindows()

# 2. Write a similar script to load and display the image using Pillow
image = Image.open(path)
image.show()

# 3. Compare the image display results in OpenCV and Pillow.
# Closable window in pillow. OpenCV more code and need to specify how it will be closed
