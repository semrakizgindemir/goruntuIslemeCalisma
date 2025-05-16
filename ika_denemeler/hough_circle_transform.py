import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü içe aktar
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\ika_denemeler\Trafik-Tanzim-Levhalari-1.jpg")
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültü azaltmak için bulanıklaştır
blur = cv2.GaussianBlur(gray, (5, 5), 0)
edges = cv2.Canny(blur, threshold1=100, threshold2=200)
plt.figure(), plt.imshow(edges, cmap="gray"), plt.title("Kenarlar"), plt.axis("off")
plt.show()


# Hough Circle Transform
circles = cv2.HoughCircles(
    edges, 
    cv2.HOUGH_GRADIENT, 
    dp=1,              # Çözünürlük oranı (1: orijinal çözünürlük)
    minDist=20,        # İki daire arasındaki minimum mesafe
    param1=100,        # Canny edge detection üst eşiği
    param2=45 ,         # Merkez algılama eşiği (düşükse daha çok daire bulur)
    minRadius=25,      # Minimum daire yarıçapı
    maxRadius=60      # Maksimum daire yarıçapı
)

# Eğer daire bulunduysa çiz
if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        # Daireyi çiz
        cv2.circle(img, (i[0], i[1]), i[2], (0, 255, 0), 2)
        # Merkez noktasını işaretle
        cv2.circle(img, (i[0], i[1]), 2, (0, 0, 255), 3)

# Sonuçları göster
cv2.imshow('Detected Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
