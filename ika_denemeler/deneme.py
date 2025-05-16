import cv2
import numpy as np
import matplotlib.pyplot as plt

# Görüntüyü içe aktar
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\ika_denemeler\Trafik-Tanzim-Levhalari-1.jpg")
blurred = cv2.GaussianBlur(img,(11,11),0)
#hsv
hsv = cv2.cvtColor(blurred , cv2.COLOR_BGR2HSV)
cv2.imshow("hsv" , hsv)

redLower = (150, 30 , 30)
redUpper = (180, 255, 255)
#kırmızı için maske oluştur
mask = cv2.inRange(hsv , redLower ,redUpper)
cv2.imshow("mask image" , mask)

#maskenin etrafında kalan gürültüleri sil
mask  = cv2.erode(mask , None , iterations = 2)
mask = cv2.dilate(mask , None ,iterations = 2)
cv2.imshow("mask + erozyon ve genişleme" , mask)

#kontur ekleme
(contours,_) = cv2.findContours(mask.copy() , cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)
center = None




gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gaussianblur = cv2.GaussianBlur(gray,ksize=(5,5) ,sigmaX=7)

if len(contours) > 0:

    # Hough Circle Transform
    circles = cv2.HoughCircles(
        gray, 
        cv2.HOUGH_GRADIENT, 
        dp=1,              # Çözünürlük oranı (1: orijinal çözünürlük)
        minDist=25,        # İki daire arasındaki minimum mesafe
        param1=100,        # Canny edge detection üst eşiği
        param2=45 ,         # Merkez algılama eşiği (düşükse daha çok daire bulur)
        minRadius=1,      # Minimum daire yarıçapı
        maxRadius=80      # Maksimum daire yarıçapı
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

cv2.imshow('gaussianblur ', gaussianblur)

cv2.imshow('Detected Circles', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
