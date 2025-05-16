import cv2
import matplotlib.pyplot as plt
import numpy as np


#resmi ie aktar
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-2DerinOgrenme\1_nesne_Tespiti\sudoku.jpg",  0)
img = np.float32(img)
print(img.shape)
plt.figure(),plt.imshow(img,cmap="gray"),plt.axis("off")

#köşeyi tespit etmek için
#harris corner detection
#blocksiz = komşuluk boyutu (ne kadar komşusuna bakacagımızı belirliyor)    
#ksize = kutucugun boyutu k = harris dedektorundeki free parametrelerden birisi(buyudukce renk acılıyor )
dst = cv2.cornerHarris(img , blockSize=2 , ksize=3 , k=0.04)
plt.figure(),plt.imshow(dst,cmap="gray"),plt.axis("off")

#tespit ettiği noktaları genişlet
dst = cv2.dilate(dst,None)
img[dst > 0.2*dst.max()] = 1
plt.figure(),plt.imshow(dst,cmap="gray"),plt.axis("off")

#shi tomasi detection
""""
Shi-Tomasi, temel olarak şuna bakar:
Bir pikselin etrafinda küçük bir pencere kaydırılır.
Bu pencere sağa, sola, yukarı ve aşağı kaydırıldığında:
Görüntüdeki intensite (parlaklık) değişimi ölçülür.
Eğer pencere kaydırıldığında her yönde büyük değişim varsa,
bu nokta: köşedir
"""

img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-2DerinOgrenme\1_nesne_Tespiti\sudoku.jpg",  0)
img = np.float32(img)
print(img.shape) 
#100=kaç tane köşe istediğimiz 0.01=quality level 10 = iki köşe arasındaki min distance
corners = cv2.goodFeaturesToTrack(img , 120 , 0.01 , 10)
corners = np.int64(corners) 
for i in corners:
    x,y = i.ravel()
    cv2.circle(img , (x,y) , 3 , (125,125,125) , cv2.FILLED)

plt.figure(),plt.imshow(img),plt.axis("off")







plt.show()





