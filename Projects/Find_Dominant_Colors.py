import cv2
import numpy as np 
from sklearn.cluster import KMeans


image_path = "02102.jpg"
image = cv2.imread(image_path)

if image is None:
    print("HATA VAR GORSEL YOK, BU GORSEL NEREDE!")
    exit()
    
average_color = np.average(image, axis=(0, 1))
print(f"Average colors (BGR): \n{average_color}")

def rengi_bul(image, k=5):
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)
    dominant_colors = kmeans.cluster_centers_
    return dominant_colors

dominant_colors = rengi_bul(image, k=5)
print(f"Dominant renkler(BGR): \n{dominant_colors}")

gorsel_rengi = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
edges = cv2.Canny(gorsel_rengi, threshold1=30, threshold2=70)
contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
num_objects = len(contours)
print(f"gorselde bulunan obje sayisi: {num_objects}")