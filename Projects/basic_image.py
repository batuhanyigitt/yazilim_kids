import cv2
import numpy as np
from matplotlib import pyplot as plt
image = cv2.imread('02102.jpg')
if image is None:
    print("Boyle bir gorsel bulunamamaktadir.")
    exit()
    
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
blurred_image = cv2.GaussianBlur(gray_image, (5, 5), 0)
edges = cv2.Canny(blurred_image, 100, 200)
equalized_image = cv2.equalizeHist(gray_image)
_, binary_image = cv2.threshold(equalized_image, 127, 255, cv2.THRESH_BINARY)
contours, _ = cv2.findContours(binary_image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
contour_image = cv2.drawContours(np.copy(image), contours, -1, (0, 255, 0), 2)

plt.figure(figsize=(14, 10))

plt.subplot(3, 3, 1)
plt.title('Original Image')
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB)) 
plt.axis('off')

plt.subplot(3, 3, 2)
plt.title('Grayscale Image')
plt.imshow(gray_image, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 3)
plt.title('Blurred Image')
plt.imshow(blurred_image, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 4)
plt.title('Edge Detection')
plt.imshow(edges, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 5)
plt.title('Equalized Image')
plt.imshow(equalized_image, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 6)
plt.title('Binary Thresholding')
plt.imshow(binary_image, cmap='gray')
plt.axis('off')

plt.subplot(3, 3, 7)
plt.title('Contours Detected')
plt.imshow(cv2.cvtColor(contour_image, cv2.COLOR_BGR2RGB))  
plt.axis('off')

plt.tight_layout()
plt.show()
