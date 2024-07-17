
#installed numpy-2.0.0 opencv-python-4.10.0.84

import cv2
import numpy as np

# Define the image path
image_path = r'C:/Users/SpeCtron/Downloads/Pipes/image022.jpg'

# Read the image in color mode
img = cv2.imread(image_path, cv2.IMREAD_COLOR)

# Check if image is loaded successfully
if img is None:
    print("Error opening image:", image_path)
    exit()

# Convert the image to grayscale
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply blurring (optional, adjust kernel size if needed)
gray_blurred = cv2.blur(gray, (3, 3))  # You can adjust the kernel size here (e.g., (5, 5))

# Detect circles using Hough transform
detected_circles = cv2.HoughCircles(gray_blurred, cv2.HOUGH_GRADIENT, 1, 20, param1=50, param2=30, minRadius=1, maxRadius=40)

# Draw detected circles (if any)
if detected_circles is not None:
    # Assuming circles are in detected_circles[0] and each circle is a list with (x, y, r)
    circles = detected_circles[0]  # Assuming circles are in detected_circles[0]
    for pt in circles:
        x, y, r = pt[0], pt[1], pt[2]  # Assuming center coordinates at indices 0 and 1, radius at index 2

        # Ensure x and y are integers before passing to cv2.circle
        x_int = int(x)
        y_int = int(y)

        # Convert radius to integer and check its value
        r_int = int(r)
        print("Center:", (x_int, y_int), "Radius:", r_int)

        # Draw the circle with the converted integer radius
        cv2.circle(img, (x_int, y_int), r_int, (0, 255, 0), 2)
        cv2.circle(img, (x_int, y_int), 1, (0, 0, 255), 3)

# Display the image with detected circles
cv2.imshow("Detected Circles", img)

# Wait for a key press to close the window
cv2.waitKey(0)

# Close all windows
cv2.destroyAllWindows()
