import cv2
import matplotlib.pyplot as plt

# Load an image
image_path = 'your_image.jpg'  # Replace with your image file
image = cv2.imread(image_path)

# Display the original image
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title('Original Image')
plt.axis('off')
plt.show()

