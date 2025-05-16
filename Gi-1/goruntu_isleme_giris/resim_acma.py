import cv2
import numpy as np

resim = cv2.imread("foto.png") #fotoyu cekiyor yanına sıfır koyunca siyah beyaz yaptı
cv2.imshow("image" , resim)#fotoyu gosteriyor
  
#cv2.imwrite("yeniresim.png" , resim) #resmin son halini kaydetti
print(resim)
print(resim.size)
print(resim.dtype)
print(resim.shape)

cv2.waitKey(0)#bir tusa basana kadar ekranda gorunsun diye
cv2.destroyAllWindows()#çartıya bastıgın an opencvye baglı pencereleri kapatır

 