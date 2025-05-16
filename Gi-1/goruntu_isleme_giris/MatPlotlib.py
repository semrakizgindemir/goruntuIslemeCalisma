import cv2
import numpy as np
from matplotlib import pyplot as plt #görüntüyü grafik penceresinde göstermek için

img = cv2.imread("foto.png" , 0)
plt.imshow(img , cmap = "gray" , interpolation = "bicubic")
#interpolation = "bicubic" → Görüntüyü büyütme/küçültme işlemi yapılırken pürüzsüz bir geçiş sağlar
plt.xticks([])#x degerlerini gosermiyor
plt.yticks([])#y degerlerini gostermiyor
plt.show()
