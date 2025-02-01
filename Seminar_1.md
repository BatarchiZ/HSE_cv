### **Theoretical Block: OpenCV and PIL (Pillow) Libraries in Python**

#### **1. Introduction to OpenCV and PIL Libraries**

**OpenCV (Open Source Computer Vision Library):**  
OpenCV is an open-source library designed for image and video processing, motion analysis, facial recognition, and other computer vision tasks. It supports multiple programming languages, including Python, and offers a comprehensive set of tools for working with images and videos.

**PIL (Python Imaging Library) / Pillow:**  
PIL was one of the primary libraries for image processing in Python but is no longer maintained. Pillow, a maintained fork of PIL, is now widely used. It provides convenient functions for opening, processing, and saving images in various formats.

---

#### **2. Key Features of OpenCV and Pillow**

| **Functionality**            | **OpenCV**                                                                                     | **Pillow**                                                                                     |
|------------------------------|-----------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------|
| **Image Loading**            | `cv2.imread()`                                                                               | `Image.open()`                                                                                |
| **Image Display**            | `cv2.imshow()`, `cv2.waitKey()`, `cv2.destroyAllWindows()`                                   | `image.show()`                                                                               |
| **Image Saving**             | `cv2.imwrite()`                                                                              | `image.save()`                                                                               |
| **Color Conversion**         | `cv2.cvtColor()`                                                                             | `image.convert()`                                                                            |
| **Resizing**                 | `cv2.resize()`                                                                               | `image.resize()`                                                                             |
| **Cropping**                 | Using NumPy array slicing                                                                    | Using `image.crop()`                                                                         |
| **Rotation and Transformation** | `cv2.rotate()`, `cv2.getRotationMatrix2D()`, `cv2.warpAffine()`                             | `image.rotate()`                                                                             |
| **Image Filtering**          | Filters like `cv2.GaussianBlur()`, `cv2.medianBlur()`, `cv2.bilateralFilter()`                | Built-in methods and Pillow filters                                                          |
| **Drawing on Images**        | Functions like `cv2.line()`, `cv2.circle()`, `cv2.rectangle()`, `cv2.putText()`               | `ImageDraw` methods for drawing                                                             |
| **Video Processing**         | Reading and writing video files, real-time frame processing                                  | Limited video processing capabilities (primarily for static images)                         |
| **Object Detection**         | Support for detection and recognition algorithms like cascades, HOG, SIFT, SURF, ORB, etc.   | No built-in object detection support                                                        |

---

### **Seminar 1 Assignments: Working with Images**

**Objective:** Reinforce theoretical knowledge of OpenCV and Pillow through practical assignments, mastering basic operations for loading, displaying, and saving images.

---

#### **Assignment 2: Loading and Displaying Images**

**Description:**  
1. Download the image `example.jpg` and place it in the project folder `cv_seminar1`.  
2. Write a Python script to load and display the image using OpenCV.  
3. Write a similar script to load and display the image using Pillow.  
4. Compare the image display results in OpenCV and Pillow.  

---

#### **Assignment 3: Saving Images in Different Formats**

**Description:**  
1. Load the image `example.jpg` using OpenCV and save it as a PNG file.  
2. Load the image `example.jpg` using Pillow and save it as a JPEG file.  
3. Verify the saved files.  

---

#### **Assignment 4: Working with Image Channels**

**Description:**  
1. Load the image `example.jpg` using OpenCV and Pillow.  
2. Split the image into individual color channels (R, G, B).  
3. Save each channel as a separate image.  
4. Merge the channels back into a single image and save the result.  

---

#### **Assignment 5: Resizing and Cropping Images**

**Description:**  
1. Load the image `example.jpg` using OpenCV and Pillow.  
2. Resize the image to 300x300 pixels.  
3. Crop a central region of size 200x200 pixels.  
4. Save the resulting images.  

---

#### **Assignment 6: Rotating Images at Arbitrary Angles**

**Description:**  
1. Load the image `example.jpg` using OpenCV and Pillow.  
2. Rotate the image 45 degrees clockwise.  
3. Rotate the image 45 degrees counterclockwise.  
4. Save the results.  

---

#### **Assignment 7: Adjusting Contrast and Brightness**

**Description:**  
1. Load the image `example.jpg` using OpenCV and Pillow.  
2. Increase the image contrast by 50% and brightness by 30 units.  
3. Save the modified images.  

---

#### **Assignment 8: Image Histogram and Visualization**

**Description:**  
1. Load the image `example.jpg` in grayscale using OpenCV and Pillow.  
2. Calculate the pixel intensity histogram.  
3. Visualize the histogram.  
4. Save the results.  

---

#### **Assignment 10: Converting Between OpenCV and Pillow Formats**

**Description:**  
1. Load the image `example.jpg` using OpenCV.  
2. Convert it to Pillow format, change its color space, and save it.  
3. Load the image `saved_gray_pil.png` using Pillow.  
4. Convert it back to OpenCV format, change its color space, and save it.  

---

### **Recommendations and Resources**

- **OpenCV Documentation:** [https://docs.opencv.org/](https://docs.opencv.org/)  
- **Pillow Documentation:** [https://pillow.readthedocs.io/en/stable/](https://pillow.readthedocs.io/en/stable/)  
- **Tutorials and Examples:**  
  - [OpenCV-Python Tutorials](https://docs.opencv.org/master/d6/d00/tutorial_py_root.html)  
  - [Pillow Tutorial](https://pillow.readthedocs.io/en/stable/handbook/tutorial.html)  
- **Books:**  
  - *Learning OpenCV 3* — Adrian Kaehler, Gary Bradski  
  - *Python Imaging Library Handbook* — Fredrik Lundh  