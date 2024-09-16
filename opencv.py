import cv2
import numpy as np

def color_detection(image_path, target_color_lower, target_color_upper):
    # Read the image
    img = cv2.imread(image_path)

    # Convert the image from BGR to HSV color space
    hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)

    # Define the color range to detect
    lower_bound = np.array(target_color_lower, dtype=np.uint8)
    upper_bound = np.array(target_color_upper, dtype=np.uint8)

    # Create a mask for the specified color range
    mask = cv2.inRange(hsv, lower_bound, upper_bound)

    # Bitwise AND to extract the color from the original image
    result = cv2.bitwise_and(img, img, mask=mask)

    # Display the original image and the result
    cv2.namedWindow('Original Image', cv2.WINDOW_NORMAL)
    cv2.namedWindow('Color Detection Result', cv2.WINDOW_NORMAL)

    cv2.imshow('Original Image', img)
    cv2.imshow('Color Detection Result', result)

    # Resize the windows for better resolution (adjust the dimensions as needed)
    cv2.resizeWindow('Original Image', 800, 600)
    cv2.resizeWindow('Color Detection Result', 800, 600)

    cv2.waitKey(0)
    cv2.destroyAllWindows()

color_detection('S.png', [0, 100, 100], [10, 255, 255])