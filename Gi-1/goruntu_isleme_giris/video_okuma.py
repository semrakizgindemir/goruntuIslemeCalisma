import cv2
import numpy as np

#cap
yakala = cv2.VideoCapture(0)#0 varsayılan webcamı ifade eder

while(True): #ret , frame
    #yakala.read() → Kameradan bir görüntü alır ve iki değer döndürür
    deger , kare = yakala.read() #videoyu okuyup her seferinde tek bir kare okur ve bunu kareye atar
    # 0 ya da 1 deger atıyor
    cv2.imshow("kare" , kare)#kareyi her seferinde gosteriyoruz
    # Klavyeden 'q' tuşuna basılınca döngüyü kır ve programı kapat
    if cv2.waitKey(1) & 0xFF == ord("q") :
        break
    

yakala.release() #kamera baglantısını kapatır
cv2.destroyAllWindows()#opencv pencerelerini kapatır