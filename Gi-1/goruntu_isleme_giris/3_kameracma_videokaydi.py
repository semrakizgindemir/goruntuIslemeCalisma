import cv2

#capture
cap = cv2.VideoCapture(0)
width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(width , height)

#video kaydet
#fourcc windows için , çerçeveleri sıkıştırmak için dört karakterli codec kodu 
#20 frame for second video akışının hızı saniyede göreceğimiz frame sayısıi
#en son çerçevenin boyutları

writer = cv2.VideoWriter("video_kaydi.mp4" , cv2.VideoWriter.fourcc(*"DIVX"),20,(width,height))

while True:
    ret , frame = cap.read()
    cv2.imshow("video" , frame)

    #save 
    writer.write(frame)
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break
cap.release()
writer.release()
cv2.destroyAllWindows()







