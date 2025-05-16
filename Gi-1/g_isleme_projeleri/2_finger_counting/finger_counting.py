import cv2
from mediapipe.python.solutions.hands import Hands
import mediapipe as mp

#parmak sayma
cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)


mpHand = mp.solutions.hands
hands = mpHand.Hands()
mpDraw = mp.solutions.drawing_utils

tipIds = [4,8,12,16,20]


while True:
    success ,img = cap.read()
    img_rgb = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)

    results = hands.process(img_rgb)
    #print(results.multi_hand_landmarks)

    lmList = []
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img,handLms,mpHand.HAND_CONNECTIONS)

            for id , lm in enumerate(handLms.landmark):
                h,w,c = img.shape
                cx,cy = int(lm.x * w) ,int(lm.y * h)
                lmList.append([id,cx,cy])

                #işaret uç = 8
                #if id == 8:
                 #   cv2.circle(img, (cx,cy) , 9 ,(255,0,0) , cv2.FILLED)
                #if id == 6:
                #    cv2.circle(img, (cx,cy) , 9 ,(0,0,255) , cv2.FILLED)

    
    if len(lmList)!=0:
        fingers = []

        #sağ sol el tespiti


        #bas parmak 
        if lmList[tipIds[0]][1] < lmList[tipIds[0] - 1][1]:
            fingers.append(1)
        else:
            fingers.append(0)

        #4 parmak
        for id in range(1,5):

            if lmList[tipIds[id]][2] < lmList[tipIds[id]-2][2]:
                fingers.append(1)
            else:
                fingers.append(0)

        #print(fingers)
        totalf = fingers.count(1)
        print(totalf)

        cv2.putText(img,str(totalf),(30,125),cv2.FONT_HERSHEY_COMPLEX ,10,(255,0,0),8)



    #print(lmList )


    cv2.imshow("img",img)
    cv2.waitKey(1)

    if cv2.waitKey(1)  & 0xFF == ord("q"):
        break


































































