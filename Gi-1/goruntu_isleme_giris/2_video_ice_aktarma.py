import cv2
import time

#video ismi
video_name = "video.mp4"

#video içe aktar : capture , cap

cap = cv2.VideoCapture(video_name)

print("genişlik : " , cap.get(3))
print("yükseklik : " , cap.get(4))

if cap.isOpened() == False:
    print("hata")

while True : 
    ret , frame = cap.read()

    if ret == True:
        time.sleep(0.01)#kullanamzsak cok hızlı akar
        cv2.imshow("video" , frame)

    else:
        break

    if cv2.waitKey(1)  & 0xFF == ord("q"):
        break

cap.release()#stop capture
cv2.destroyAllWindows()


