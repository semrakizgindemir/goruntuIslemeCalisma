import cv2
import numpy as np
# matplotlib.pyplot imported but not used, can be removed if not needed later
# import matplotlib.pyplot as plt

# --- Configuration ---
# Use a variable for the image path - makes it easier to change
image_path = r"C:\Users\kizgi\Desktop\opencv\ika_denemeler\Trafik-Tanzim-Levhalari-1.jpg"

# Define the HSV range for red. Red wraps around the HUE spectrum (0 and 180).
# You might need to tune these values based on your specific image lighting.
# These are typical ranges for red, allowing for variations in saturation (S) and value (V)
lower_red1 = (0, 50, 50)    # Lower hue range for red (0-10 or 0-15)
upper_red1 = (10, 255, 255)
lower_red2 = (170, 50, 50)  # Higher hue range for red (170-180)
upper_red2 = (180, 255, 255)

# --- Image Loading and Preprocessing ---
# Görüntüyü içe aktar
img = cv2.imread(image_path)

# Check if the image loaded successfully
if img is None:
    print(f"Error: Could not load image from {image_path}")
    exit() # Exit the script if image not found

# Apply initial Gaussian Blur to the BGR image
# Helps in reducing noise for both color segmentation and Hough Circles
blurred_bgr = cv2.GaussianBlur(img, (11, 11), 0)

# Convert the blurred image to HSV for color segmentation
hsv = cv2.cvtColor(blurred_bgr, cv2.COLOR_BGR2HSV)
# cv2.imshow("HSV Image", hsv) # Optional: show HSV image

# --- Red Color Segmentation ---
# Create masks for both red ranges
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)

# Combine the masks to get the final red mask
red_mask = cv2.bitwise_or(mask1, mask2)
# cv2.imshow("Initial Red Mask", red_mask) # Optional: show initial mask

# --- Morphological Operations ---
# Clean up the red mask using erosion and dilation to remove noise and fill gaps
# Define a kernel for morphological operations
kernel = np.ones((5,5), np.uint8) # 5x5 kernel
red_mask = cv2.erode(red_mask, kernel, iterations=2)
red_mask = cv2.dilate(red_mask, kernel, iterations=2)
cv2.imshow("Cleaned Red Mask", red_mask)

# --- Grayscale Conversion for Hough Circles ---
# Convert the original image (or blurred_bgr) to grayscale for Hough Circle Transform
# Using the original or slightly blurred BGR is common practice for Hough
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Apply Gaussian Blur specifically for Hough Circles
# This blur is often necessary to help Hough find circles accurately
gray_blurred = cv2.GaussianBlur(gray, (5, 5), 0)
# cv2.imshow('Gray Blurred for Hough', gray_blurred) # Optional: show blurred gray

# --- Hough Circle Detection ---
# Use Hough Circle Transform on the grayscale image
# Adjust parameters as needed based on the image and expected circle sizes
circles = cv2.HoughCircles(
    gray_blurred,              # Input image (grayscale, blurred)
    cv2.HOUGH_GRADIENT,        # Detection method
    dp=1,                      # Resolution ratio (1: original resolution)
    minDist=30,                # Minimum distance between the centers of detected circles
    param1=100,                # Canny edge detector high threshold (lower threshold is half of this)
    param2=30,                 # Accumulator threshold for circle detection (lower means more circles, potentially false positives)
    minRadius=10,              # Minimum circle radius
    maxRadius=100              # Maximum circle radius
)

# --- Filter Circles Based on Red Mask ---
# Create a copy of the original image to draw on
output_img = img.copy()

# If circles were found
if circles is not None:
    # Convert the circle coordinates to integers
    circles = np.uint16(np.around(circles))

    # Iterate over the found circles
    for i in circles[0, :]:
        # Get the center coordinates and radius
        center_x, center_y, radius = i[0], i[1], i[2]

        # Check if the center of the detected circle is within the red mask
        # We check the red_mask image at the circle's center coordinates (y, x)
        # A value of 255 in the mask means it's a red pixel.
        # Add a small margin check around the center for robustness, or check multiple points
        # For simplicity, we check the center and a few points around it.
        is_red_circle = False
        # Check the center point
        if red_mask[center_y, center_x] > 0: # Check if the mask pixel is white (part of red area)
             is_red_circle = True
        # Optional: Check a few points within the circle's radius near the center
        # (This adds robustness but also complexity. Checking the center is often sufficient)
        # points_to_check = [(center_x, center_y),
        #                    (center_x + radius//4, center_y),
        #                    (center_x - radius//4, center_y),
        #                    (center_x, center_y + radius//4),
        #                    (center_x, center_y - radius//4)]
        # red_points_count = 0
        # for px, py in points_to_check:
        #     # Ensure points are within image bounds
        #     if 0 <= px < red_mask.shape[1] and 0 <= py < red_mask.shape[0]:
        #          if red_mask[py, px] > 0:
        #              red_points_count += 1
        # if red_points_count >= len(points_to_check) // 2: # e.g., if at least half points are red
        #      is_red_circle = True


        # If the circle is confirmed to be red, draw it
        if is_red_circle:
            # Draw the outer circle (Green)
            cv2.circle(output_img, (center_x, center_y), radius, (0, 255, 0), 2)
            # Draw the center of the circle (Red)
            cv2.circle(output_img, (center_x, center_y), 3, (0, 0, 255), -1) # Use -1 for a filled circle
            print(f"Detected Red Circle at ({center_x}, {center_y}) with radius {radius}")


# --- Display Results ---
cv2.imshow('Detected Red Circles', output_img)

# Wait indefinitely until a key is pressed
cv2.waitKey(0)

# Destroy all OpenCV windows
cv2.destroyAllWindows()