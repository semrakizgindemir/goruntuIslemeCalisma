import cv2

yakala =cv2.VideoCapture("video.mp4")
print(yakala.get(cv2.CAP_PROP_FRAME_HEIGHT))
print(yakala.get(cv2.CAP_PROP_FRAME_WIDTH))


while(yakala.isOpened()):

    ret , frame = yakala.read()
    frame = cv2.rectangle(frame,(1000,400),(1200,500),(0,255,0))
    cv2.imshow("video",frame)

    if cv2.waitKey(10) & 0xFF ==ord("q"):
        break

yakala.release()
cv2.destroyAllWindows()

