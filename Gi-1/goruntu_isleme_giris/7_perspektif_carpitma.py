import cv2
import numpy as np

#resmi içe aktarma 
img = cv2.imread("kart.jpg")
cv2.imshow("orijinal" , img)

width = 400
height = 500

pts1 = np.float32([[626,80],[294,517],[995,239],[661,679]])
pts2 = np.float32([[0,0],[0,height],[width,0],[width,height]])
matrix = cv2.getPerspectiveTransform(pts1,pts2)
print(matrix)

#nihai donusturulmus resim
imgout = cv2.warpPerspective(img,matrix,(width,height))
cv2.imshow("nihairesim" , imgout)

cv2.waitKey(0)
cv2.destroyAllWindows()

