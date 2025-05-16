import cv2
import numpy as np
import matplotlib.pyplot as plt
from collections import deque


#belrli renklerde bukunan nesnelerin
#tespitini kontur bulma yontemiyle yapma
#konturlar aynı renk veya yogunluga sahip 
#tüm sürekli noktaları birleştiren bir eğri olarak açıklanablir
#konturlar şekil analizi, nesne algılama ve tanıma için kullanışlı bir araçtır

#nesne merkezie depolayacak veri tipi
buffer_size = 16
pts = deque(maxlen = buffer_size)

#mavi renk aralığı(h = ton s = saturation doygunluk v = parlaklık)
blueLower = (84, 98 ,0)
blueUpper = (179, 255, 255)

#capture
cap = cv2.VideoCapture(0)
cap.set(3,960)
cap.set(4,480)

while   True: 
    success , imgoriginal = cap.read()
    
    if success:
        #blur detayını azaltıcaz
        blurred = cv2.GaussianBlur(imgoriginal,(11,11),0)

        #hsv
        hsv = cv2.cvtColor(blurred , cv2.COLOR_BGR2HSV)
        cv2.imshow("hsv" , hsv)


        #mavi için maske oluştur
        mask = cv2.inRange(hsv , blueLower ,blueUpper)
        cv2.imshow("mask image" , mask)

        #maskenin etrafında kalan gürültüleri sil
        mask  = cv2.erode(mask , None , iterations = 2)
        mask = cv2.dilate(mask , None ,iterations = 2)
        cv2.imshow("mask + erozyon ve genişleme" , mask)

        #kontur ekleme
        (contours,_) = cv2.findContours(mask.copy() , cv2.RETR_EXTERNAL ,cv2.CHAIN_APPROX_SIMPLE)
        center = None

        if len(contours) > 0:

            #en buyuk konturu al 
            c = max (contours, key = cv2.contourArea)

            #dikdortgene çevir
            rect = cv2.minAreaRect(c)
 
            ((x,y) , (width,height) ,rotation ) = rect

            s = "x : {} , y: {} , width: {} , height: {} , rotation: {}".format(np.round(x) , np.round(y), np.round(width), np.round(height), np.round(rotation))
            print(s)

            #kutucuk
            box = cv2.boxPoints(rect)
            box = np.int64(box)

            #goruntu momenti : bir goruntunun yarıcap alan agırlık merkezi vb gibi belirli 
            #ozelliklerini bulabılecegımız goruntu piksel yogunluklarının agırlıklı ortalamasıdır
            #goruntunun merkezini bulmamıza yarayan yapı
            m = cv2.moments(c)
            center = (int(m["m10"]/m["m00"]) , int(m["m01"]/m["m00"]) )
            #konturu çizdir
            cv2.drawContours(imgoriginal , [box] , 0 ,(0,255,255) ,2)
            #merkeze bir tane nokta çizelim pembe
            cv2.circle(imgoriginal , center , 5, (255,0,255) , -1)
            #bilgileri ekrana yazdır
            cv2.putText(imgoriginal , s , (50,50) , cv2.FONT_HERSHEY_COMPLEX_SMALL , 1 , (255,255,255) , 2)

            #deque
            pts.appendleft(center) 
            for i in range (1,len(pts)):
                if pts[i-1] is None or pts[i] is None : continue
                cv2.line(imgoriginal , pts[i-1] , pts[i] , (0,255,0),3)



            cv2.imshow("orijinal tespit" , imgoriginal)










    if cv2.waitKey(1) & 0xFF ==ord("q") : break










