#EROZYON
#temel fikri sadece toprak erozyonu gibidir 
# ön plandaki nesnenin sınırlarını asındırır 

#GENİŞLEME
#erozyonun tam tersidir 
#görüntüdeki beyaz bölgeyi arttırır

#AÇMA 
#erozyon + genişlemedir
#gürültünün giderilmesine faydalıdır

#KAPATMA 
#açmanın tam tersidir
#geniişleme + erozyon
#ön plandaki nesnelerin içindeki küçük delikleri veya
#nesne üzerindeki küçük siyah noktaları kapatmak için kullanıslıdır

#MORFOLOJİK GRADYAN
#bir görüntünün genişlemesi ve erozyonu arasındaki farktır

import cv2
import numpy as np
from matplotlib import pyplot as plt

#resmi içe aktar
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-1\logo.jpg",0)
plt.figure() , plt.imshow(img , cmap = "gray") , plt.axis("off") ,plt.title("orijinal logo") ,plt.show()

#EROZYON
kernel = np.ones((5,5) , dtype = np.uint8)#kernel arttıkca erozyon 
result = cv2.erode(img, kernel, iterations = 4) #iterations parametresi erozyon işleminin 4 kez tekrarlanmasını saglar 
#Her beyaz pikselin, kernel tarafından incelenip küçültülmesini sağlar.
plt.figure() , plt.imshow(result , cmap = "gray") , plt.axis("off") ,plt.title("erzoyonlu logo") ,plt.show()

#GENİŞLEME (DİLATİON)
result2 = cv2.dilate(img , kernel,iterations = 1)
plt.figure() , plt.imshow(result2 , cmap = "gray") , plt.axis("off") ,plt.title("genişlemiş logo") ,plt.show()

#WHİTE NOİSE
whitenoise = np.random.randint(0,2,size = img.shape[:2])
whitenoise = whitenoise*255
#Çarpmazsak (0-1 değerleri)	Bulanık / yarı saydam görüntü oluşabilir.
#Çarparsak (0-255 değerleri)	Net bir siyah-beyaz gürültü görüntüsü olur.
plt.figure() , plt.imshow(whitenoise, cmap = "gray") , plt.axis("off") ,plt.title("white noise logo") ,plt.show()

noise_img = whitenoise + img #gürültüyü orijinal resme ekliyoruz
plt.figure() , plt.imshow(noise_img, cmap = "gray") , plt.axis("off") ,plt.title("img with white noise logo") ,plt.show()

#AÇILMA
#beyaz gürültüyü azaltmak için kullanılır
opening = cv2.morphologyEx(noise_img.astype(np.float32) , cv2.MORPH_OPEN , kernel)
plt.figure() , plt.imshow(opening, cmap = "gray") , plt.axis("off") ,plt.title("açılma logo") ,plt.show()


#BLACK NOİSE
blacknoise = np.random.randint(0,2,size = img.shape[:2])
blacknoise = blacknoise* -255
plt.figure() , plt.imshow(blacknoise, cmap = "gray") , plt.axis("off") ,plt.title("black noise logo") ,plt.show()

blacknoiseimg = blacknoise + img
blacknoiseimg[blacknoiseimg <= -245]=0
blacknoiseimg = np.clip(blacknoiseimg , 0,255)
plt.figure() , plt.imshow(blacknoiseimg, cmap = "gray") , plt.axis("off") ,plt.title("black noise img logo") ,plt.show()

#KAPATMA
#siyah gürültüyü azaltmak için kullanılır
closing = cv2.morphologyEx(blacknoiseimg.astype(np.uint8) , cv2.MORPH_CLOSE , kernel)
plt.figure() , plt.imshow(closing , cmap ="gray" ) ,plt.axis("off") , plt.title("kapama") , plt.show()

#gradient = nesne tespitinde kullanılıyor
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)
plt.figure() , plt.imshow(gradient,cmap ="gray" ) ,plt.axis("off") , plt.title("gradyan"),plt.show()

 





