import cv2 
import numpy as np
from sklearn.cluster import KMeans 

image_path = '02102.jpg'
image = cv2.imread(image_path)

if image is None: 
    print("Error")
    exit()
    
average_color = np.average(image, axis=(0, 1))
print(f"Average color (BGR) : {average_color}")

def find_dominat_color(image, k=5):
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)
    dominat_colors = kmeans.cluster_centers_
    return dominat_colors
    
dominant_colors = find_dominat_color(image, k=5)
print(f"Dominant colors (BGR): \n{dominant_colors}")

gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gray_image, threshold1=30, threshold2=70)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
num_objects = len(contours)
print(f"Number of objects in the image: {num_objects}")