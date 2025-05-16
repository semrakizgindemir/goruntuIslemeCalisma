import numpy as np
import matplotlib.pyplot as plt
import cv2


img=cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-1\foto.png",0)
cv2.imshow("original",img)
plt.figure(), plt.imshow(img,cmap="gray") , plt.title("foto") , plt.show()
print(img.shape)

imgresized=cv2.resize(img,(480,320))
plt.figure(), plt.imshow(imgresized,cmap="gray") , plt.title("foto") , plt.show()

cv2.putText(img,"CICEK" , (320,180) , cv2.FONT_HERSHEY_SIMPLEX ,1,(255,0,0))
plt.figure(), plt.imshow(img, cmap="gray") , plt.title("yazılı foto") , plt.show()

