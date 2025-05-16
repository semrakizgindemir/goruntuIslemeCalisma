import cv2
import matplotlib.pyplot as plt
from ultralytics import YOLO

model = YOLO("yolov8n.pt")#build a new model from yaml
print(model)

#karmasık bir sahnede belirtilen hedefi tespit etmek için etkili bir yontemdir
#birden cok nesne yerine tek nesneleri algılar
#dagınık bir goruntu zuerinde belirli bir kisiyi tanıyabilir 
#ancak baska herhangi kişiyi tanıyamaz

#ozellik eslestirme
#brute-force eşleştiricisi bir goruntudeki bir ozelliğin tanımlayıcısını 
#baska bir goruntunun diğer tum ozellikleriyle eşleştirir ve mesafeye gore eslestirmeyi dondurur
#tum ozellikleriyle eşleşmeyi kontorl etitği için yavaştır


#ölçek değişmez ozellik dönüşümü anahtar noktaları ilk olarak 
#bir dizi referans goruntuden cıkarılır ve saklanır
#yeni goruntudeki her bir ozelliği bu saklanan veri ile ayrı ayrı
#karşılaştırarak ve öznitelik vektörlerinin Oklid mesafesine dayalı olarak
#aday eslestirme ozelliklerini bularak yeni bir goruntude bir nesne tanınır.



#ana goruntuyu içe aktar
chos = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-2DerinOgrenme\1_nesne_Tespiti\chocolates.jpg" ,0)
plt.figure() , plt.imshow(chos , cmap="gray") , plt.axis("off")

#aranacak olan goruntu
cho = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-2DerinOgrenme\1_nesne_Tespiti\nestle.jpg" , 0)
plt.figure() , plt.imshow(cho , cmap="gray") , plt.axis("off")

#orb tanımlayıcı 
#goruntu ve aradıgımız nesne arasındaki anahtar nokteları tespit edecek 
#kose kenar gibi nesneye ait ozellikler

orb = cv2.ORB_create()

#anahtar nokta tespiti
kp1 , des1 = orb.detectAndCompute(cho , None)
kp2 , des2 = orb.detectAndCompute(chos , None)

#brute force eşleştiricisi
bf = cv2.BFMatcher(cv2.NORM_HAMMING)
#noktaları eşleştir
matches = bf.match(des1 , des2)

#mesafeye gore sırala
matches = sorted(matches ,key=lambda x: x.distance)

#eşlesen resimleri gorselleştir

plt.figure()
img_match = cv2.drawMatches(cho , kp1 , chos, kp2 ,matches[:20] , None ,flags = 2)
plt.imshow(img_match) , plt.title("orb"), plt.axis("off")


#sift tanımlayıcısıyla yapma orbden iyi
sift = cv2.SIFT_create()

#bf
bf = cv2.BFMatcher()

#anahtar nokta tespiti sift ile
kp1 , des1 = sift.detectAndCompute(cho , None)
kp2 , des2 = sift.detectAndCompute(chos , None)

matches = bf.knnMatch(des1,des2,k=2)

guzel_eslesme = []

for match1 , match2 in matches :
    if match1.distance < 0.75*match2.distance:
        guzel_eslesme.append([match1])

plt.figure()
sift_matches = cv2.drawMatchesKnn(cho , kp1 , chos, kp2 , guzel_eslesme ,None ,flags=2)

plt.imshow(sift_matches) ,plt.title("sift"),  plt.axis("off")



plt.show()








