import cv2 
import numpy as np
resim = cv2.imread("foto.png" , 0)
a = cv2.waitKey(0)
cv2.imshow("image" , resim)
a = cv2.waitKey(0)
if a == 27: #27 esc tusuna esit
    cv2.destroyAllWindows()
elif a == ord("s"):
    cv2.imwrite("opencv_s_tusu.png" , resim)


