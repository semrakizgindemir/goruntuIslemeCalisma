#görüntü histogramı
#dijital görüntüdeki  ton dağılımının grafiksel bir temsili 
#olarak işlev gören bir histogram türüdür 
#her bir ton değeri için piksel sayısını içerir
#belirli bir görüntü için histograma bakılarak ton dagılımı anlasılabilir
import cv2
import matplotlib.pyplot as plt
import numpy as np

#resmi içe aktar 
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-1\foto.png")
imgvis= cv2.cvtColor(img, cv2.COLOR_BGR2RGB) 
plt.figure(), plt.imshow(imgvis) , plt.title("foto") , plt.show()

print(img.shape)

img_hist = cv2.calcHist([img] , channels = [0], mask= None,histSize=[256],ranges=[0,256])
print(img_hist.shape)
plt.figure(),plt.plot(img_hist),plt.title("Histogram"),plt.show()

color = ("b" , "g","r")
plt.figure()
for i , c in enumerate(color):
    hist=cv2.calcHist([img] , channels = [i], mask= None,histSize=[256],ranges=[0,256])
    plt.plot(hist,color = c)



#maskeleme ekullanılarak yapma olan img ile yaptım
print(img.shape)
mask = np.zeros(img.shape[:2], np.uint8)
plt.figure() ,plt.imshow(mask,cmap="gray"),plt.show()

mask[250:300 , 150:300] = 255
plt.figure(), plt.imshow(mask,cmap="gray"),plt.show()

maskedimgvis= cv2.bitwise_and(imgvis,imgvis,mask=mask)
plt.figure() ,plt.imshow(maskedimgvis,cmap="gray"),plt.show()


maskedimg = cv2.bitwise_and(imgvis,imgvis,mask=mask) 
maskedimghist= cv2.calcHist([img] , channels = [2], mask= mask,histSize=[256],ranges=[0,256])
plt.figure() ,plt.plot(maskedimghist),plt.show()
#histogram eşitleme 
#kontrastı (karşıtlık) arttırmaya yarıyor
img2 = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-1\grifoto.jpg" ,0)
plt.figure(), plt.imshow(img2,cmap="gray") , plt.title("foto") , plt.show()
 

img2hist=cv2.calcHist([img2] , channels = [0], mask= None,histSize=[256],ranges=[0,256])
plt.figure() ,plt.plot(img2hist),plt.show()

eq_hist=cv2.equalizeHist(img2)
plt.figure() ,plt.imshow(eq_hist,cmap="gray"),plt.show()

eqimg2hist=cv2.calcHist([eq_hist] , channels = [0], mask= None,histSize=[256],ranges=[0,256])
plt.figure() ,plt.plot(eqimg2hist),plt.show()

