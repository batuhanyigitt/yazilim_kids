import cv2 
import numpy as np
from sklearn.cluster import KMeans
import matplotlib.pyplot as plt 
from webcolors import hex_to_name 

image_path = '02102.jpg'
image = cv2.imread(image_path)

if image is None: 
    print("HATA!: GORSEL YUKLENMEDI")
    exit()
    
#GORSELI GORUNTULEME 
plt.figure(figsize=(8, 6))
plt.imshow(cv2.cvtColor(image, cv2.COLOR_BGR2RGB))
plt.title("Orjinal Gorsel")
plt.axis('off')

#ortalama rengin hesaplanmasi 
average_color = np.mean(image, axis=(0, 1))
print(f"ortalama renk (BGR): {average_color}")


#K-Means'in calisacagi alan, dominant rengi bulabilmek icin 
def find_dominant_colors(image, k=5):
    pixels = image.reshape(-1, 3)
    kmeans = KMeans(n_clusters=k, n_init=10)
    kmeans.fit(pixels)
    dominant_colors = kmeans.cluster_centers_
    return dominant_colors

dominant_colors = find_dominant_colors(image, k=5)
print(f"dominant renklerin sayisi (BGR): {len(dominant_colors)}")
print(f"Dominant renkler (BGR):\n{dominant_colors}")
print(f"Ortalama renk (BGR): {average_color}")


canvas = np.zeros((110, 300, 3), dtype=np.uint8)
start_x = 0
for color in dominant_colors:
    end_x = start_x + 60 
    color_bgr = tuple(color)
    color_hex = "#{:02x}{:02x}{:02x}".format(color_bgr[2], color_bgr[1], color_bgr[0])
    color_name = hex_to_name(color_hex)
    cv2.rectangle(canvas, (start_x, 0), (end_x, 100), color_bgr, -1)
    start_x = end_x
    plt.text(end_x - 55, 80, color_name, fontsize=8, color='white')
    

plt.figure(figsize=(8, 2))
plt.imshow(cv2.cvtColor(canvas, cv2.COLOR_BGR2RGB))
plt.title("Dominant Renkler")
plt.axis('off')
plt.show()


