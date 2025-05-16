import cv2
import numpy as np

yakala = cv2.VideoCapture("video.mp4")

while(yakala.isOpened()):
    deger , kare = yakala.read()
    gray = cv2.cvtColor(kare , cv2.COLOR_BGR2GRAY)
    cv2.imshow("kare" , gray)

    #hızlandırılmıs olmasının nedeni waitkey(1) ekranda 1 ms beklemesı gerekıyor
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

yakala.release()
cv2.destroyAllWindows()
