import cv2
import numpy as np

img = np.zeros((512,512,3),np.uint8)
cv2.imshow("pencere adı" , img)

#baslangıc koordinatları ,bitiş koordinatları,renk kodu
img2 = cv2.line(img , (0,0) , (512,512) , (255,0,0))
cv2.imshow("çizgi" , img2)

cv2.waitKey(0)
cv2.destroyAllWindows()


