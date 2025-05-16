import cv2
import numpy as np

#resmi içe aktar
img = cv2.imread("foto.png")
cv2.imshow("orijinal" , img)

#yatay yan yana ekleme yapacak
hor = np.hstack((img ,img))
cv2.imshow("horizontal" , hor)

#dikey alt alta ekleme yapacak
ver = np.vstack((img,img))
cv2.imshow("vertical" , ver)
  


cv2.waitKey(0)
cv2.destroyAllWindows()
