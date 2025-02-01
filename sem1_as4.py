"""Assignment 4: Working with Image Channels
Description:

Load the image example.jpg using OpenCV and Pillow.
Split the image into individual color channels (R, G, B).
Save each channel as a separate image.
Merge the channels back into a single image and save the result."""


import cv2
from PIL import Image
path = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/example.jpg"
# 1. Load the image example.jpg using OpenCV and Pillow
img = cv2.imread(path)
img_pil = Image.open(path)

# 2. Split the image into individual color channels (R, G, B)
b, g, r = cv2.split(img)

# 3. Save each channel as a separate image.
save_dir = "/Users/is/VSCode/computer_vision_hse/seminars/seminar_1/output/"
for indx, i in enumerate([b, g, r]):
    cv2.imwrite(save_dir + str(indx) + ".jpg", i)

# 4. Merge the channels back into a single image and save the result.
merged_img = cv2.merge([b, g, r])
cv2.imwrite(save_dir + "merged.jpg", merged_img)
print("done")


