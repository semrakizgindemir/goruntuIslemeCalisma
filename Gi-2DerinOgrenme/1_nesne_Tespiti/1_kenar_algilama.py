import cv2
import matplotlib.pyplot as plt
import numpy as np

#nesneleri blurlayarak kenar tespitini daha iyi yapıyoruz 
#istenmeyen kısımlar blurlanarak kenar olarak cıkmıyor

#resmi içe aktar
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-2DerinOgrenme\1_nesne_Tespiti\london.jpg",0)
plt.figure(),plt.imshow(img,cmap="gray") , plt.axis("off")

edges = cv2.Canny(image = img , threshold1=0 , threshold2=255)
#threshold kullanılmadıgı için kenarı olmayan seyler de kenarlı algılanmış mesela deniz
plt.figure(),plt.imshow(edges,cmap="gray") , plt.axis("off")

med_val = np.median(img)
print(med_val)

low = int(max(0,(1-0.33)*med_val))
high = int(min(255,(1+0.33)*med_val))

print(low)
print(high)

edges = cv2.Canny(image = img , threshold1=low , threshold2=high)
plt.figure(),plt.imshow(edges,cmap="gray") , plt.axis("off")

#blur
blured_img = cv2.blur(img , ksize= (3,3  ))
plt.figure(),plt.imshow(blured_img,cmap="gray") , plt.axis("off")

med_val = np.median(blured_img)
print(med_val)

print(low)
print(high)

edges = cv2.Canny(image = blured_img , threshold1=low , threshold2=high)
plt.figure(),plt.imshow(edges,cmap="gray") , plt.axis("off")







plt.show()


















































