import cv2
import matplotlib.pyplot as plt

#resmi içe aktar
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-1\manzara2.jpg")
img = cv2.cvtColor(img , cv2.COLOR_RGB2GRAY)
plt.figure()
plt.imshow(img , cmap = "gray")#siyah beyaz gorebilmek için colormapi değiştiriyoruz
plt.axis("off")
plt.show()

#thresh= 60 bunun üzerindekileri beyaz yapıyor 255
#eşikleme thrash_binary eşik türlerinde kullanılacak max ve min degerleri arasında açıyor ya da kapatıyor
_, thresh_img =  cv2.threshold(img , thresh= 60, maxval = 255 , type = cv2.THRESH_BINARY)
plt.figure()
plt.imshow(thresh_img , cmap = "gray")
plt.axis("off")
plt.show()

#thresh_img = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 11, 8)
#gaussian daha iyi 


#adaptif tresholding uyarlamalı eşik değeri
#farklı miktarlarda ısık alan yerler için kullanılıyor
#or: dagın yarısının yok olmaması için
#255 = max value 
#cv2.ADAPTIVE_THRESH_MEAN_C = uyarlanabilri eşikleme algoritması için
#11 block size
thresh_img2 = cv2.adaptiveThreshold(img, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY,11,8 )

plt.figure()
plt.imshow(thresh_img2 , cmap = "gray")
plt.axis("off")
plt.show()

