import cv2
import numpy as np

#resim oluştur
img = np.zeros((512, 512, 3), np.uint8) #siyah yapar
#img = np.ones((512, 512, 3), np.uint8) * 128 #gri yapar
#img = np.ones((512, 512, 3), np.uint8) * 255 #beyaz gri bir ekran yapar

#siyah bir resim
print(img.shape)
#cv2.imshow("image" , img)

#line çizgi
#(resim, başlangıç noktası,bitiş noktası,renk,kalınlık)
#BGR = (255,0,0) yeşil yapar
cv2.line(img , (100,100) ,(100,300), (0,255,0) ,13)

#cv2.imshow("cizgi" , img) 

#dikdortgen
# (resim,baslagıç,bitiş,renk) cv2.FILLED içini doldurmak için
cv2.rectangle(img , (0,0),(256,256),(255,0,0) , cv2.FILLED)
#cv2.imshow("dikdortgen" , img) 

#çember
#(resim, merkez  yarıçap, renk)
cv2.circle(img,(300,300), 45 ,(0,0,255),cv2.FILLED)
#cv2.imshow("cember" , img) 

#metin
# (resim,baslangıç noktası, font , kalınlığı , renk)
cv2.putText(img,"resim" , (350,350) , cv2.FONT_HERSHEY_COMPLEX ,1,(255,255,255))
cv2.imshow("metin" , img) 

cv2.waitKey(0)
cv2.destroyAllWindows()



