import cv2
import time
import mediapipe as mp

#el takibi
cap = cv2.VideoCapture(0)

mphand = mp.solutions.hands
hands = mphand.Hands()


mpdraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0

while True:
    success , img = cap.read()
    imgRGB = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

    results = hands.process(imgRGB)
    print(results.multi_hand_landmarks) #eli gorene kadar none donuyor el gorunce koordinatları yazıyor

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpdraw.draw_landmarks(img,handLms,mphand.HAND_CONNECTIONS)


        for id , lm in enumerate(handLms.landmark):
            print(id, lm)
            h , w , c = img.shape

            cx , cy = int(lm.x*w) , int(lm.y*h) ,

            #bilek
            if id == 4:
                cv2.circle(img,(cx,cy) ,9 ,(255,0,0), cv2.FILLED)


    #fps
    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime 

    cv2.putText(img,"FPS=" + str(int(fps)) , (10,75), cv2.FONT_HERSHEY_PLAIN,3,(255,0,0),5)

    cv2.imshow("img",img)
    cv2.waitKey(1)
    
    if cv2.waitKey(1)  & 0xFF == ord("q"):
        break














































