import cv2

img = cv2.imread("foto.png")
print("resim boyutu : " , img.shape)
#cv2.imshow("orijinal" , img)


img_resized = cv2.resize(img, (30,30))
print("resized img shape : " ,img_resized.shape)
cv2.imshow("orijinal" , img_resized)


#kırp      genişlik x  yükseklik y ekseni 0 dan girilene kadar piksel alıyor
imgcropped = img[:200   ,   0:300]
cv2.imshow("kirpilmis resim : " , imgcropped) 

cv2.waitKey(0)
cv2.destroyAllWindows()

