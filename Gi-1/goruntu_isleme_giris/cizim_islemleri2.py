import cv2 
import numpy as np


img = cv2.imread("foto.png" )
img2 = cv2.rectangle(img , (15,15) , (880,275),(0,255,0),5)
img3 = cv2.circle(img2,(450,150),40,(0,0,255),-1) #-1 koyunca içi dolu oluyor 
cv2.imshow("image3",img3)

font = cv2.FONT_HERSHEY_COMPLEX 
img4 = cv2.putText(img3 , "vmkjmgl" ,(20,150),font,4,(255,255,255),4,cv2.LINE_AA)
cv2.imshow("image4" , img4)
cv2.waitKey(0)
cv2.destroyAllWindows()



