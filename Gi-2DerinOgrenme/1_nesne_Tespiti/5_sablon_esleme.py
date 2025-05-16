import cv2
import numpy as np
import matplotlib.pyplot as plt


#template matching sablon esleme
#sablon esleme ile nesne tespitinin nasıl yapılacagını ogrenecegiz
#sablon eslestirme bir sablon goruntunun konumunu daha buyuk
#bir goruntude aramak ve bulmak için bir yontemdir

#sablon goruntusunu giriş goruntusunun üzerine kaydırır ve
#şablon görüntüsünün altındaki giriş goruntusunun sablonu ve yamayı karşılaştırır

#kaydırarak şablonu bir seferde bir piksel hareket ettirmeyi kastediyoruz(soldan sağa yukardan asagıya)
#her konumda o konumdakı eslesmenin ne kadar iyi veya kotu oldugunu 
#ya da sablonun kaynak goruntunun obelirli alanına ne kadar benzer oldugunu
#temsil edecek sekilde bir metrik hesapladık

img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-2DerinOgrenme\1_nesne_Tespiti\cat.jpg" ,0)
print(img.shape)
template = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-2DerinOgrenme\1_nesne_Tespiti\cat_face.jpg" ,0)
print(template.shape)
w,h = template.shape

methods = ['cv2.TM_CCOEFF' , 'cv2.TM_CCOEFF_NORMED' , 'cv2.TM_CCORR' , 
           'cv2.TM_CCORR_NORMED' , 'cv2.TM_SQDIFF', 'cv2.TM_SQDIFF_NORMED']

for meth in methods:

    method = eval(meth) #'cv2.TM_CCOEFF' --> cv2.TM_CCOEFF normal fonksiyon haline getiriyor
    res = cv2.matchTemplate(img , template ,method)
    print(res.shape)
    min_val , max_val ,min_loc , max_loc = cv2.minMaxLoc(res)

    if method in [cv2.TM_SQDIFF ,cv2.TM_SQDIFF_NORMED] :
        top_left = min_loc
    else:
        top_left = max_loc

    bottom_right = (top_left[0] + w , top_left[1]+h)
    cv2.rectangle(img , top_left , bottom_right ,255 , 2)

    plt.figure()
    plt.subplot(121),plt.imshow(res,cmap="gray")
    plt.title("eslesen sonuc") ,plt.axis("off") 
    plt.subplot(122) , plt.imshow(img,cmap="gray")
    plt.title("tespit edilen sonuc") , plt.axis("off")
    plt.suptitle(meth)

    plt.show()












