import cv2
import pandas as pd

#içe aktarma
img = cv2.imread("foto.png" , 0)#siyah beyaz

#görselleştir
cv2.imshow("ilk resim" , img)

k = cv2.waitKey(0) &0xFF

if k==27:
    cv2.destroyAllWindows()
elif k == ord('s'):
    cv2.imwrite("foto_gray.png" , img)
    cv2.destroyAllWindows()










