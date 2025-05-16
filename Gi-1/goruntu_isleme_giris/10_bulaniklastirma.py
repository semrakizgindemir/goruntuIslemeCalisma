"""
ORTLAMA BULANIKLASTIRMA
bir goruntunun normalleştirilmiş bir kutu filtresiyle sarilmasiyla yapilir
cekirdek alani altindaki tum piksellerin ortalamasini alir 
ve bu ortalamayi merkezi oge ile yer degistirir
"""
"""
GAUSS BULANIKLASTIRMA
lutu filtresi yerine gauss cekirdeği kullanilir
pozitif ve tek olmasi gereken cekirdeğin genişliginive yuksekligini belirtir
sigmaX sigmaY x ve y yonlerindeki standart sapmayı belirtmeliyiz
"""
"""
MEDYAN BULANIKLASTIRMA
cekirdek alani ve altindaki tum piksellerin medyanini alir 
ve merkezi oge bu medyan degerle degistirilir
tuz biber goruntusune karsi oldukca etkili

"""
import cv2
import matplotlib.pyplot as plt
import numpy as np

#blurring(detayı azaltır gürültüyü engeller)
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-1\nyc.jpg") 
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()

"""
ortalama bulanıklaştırma yöntemi
kutu filtre alanı altındaki tüm piksellerin ortalamasını alıyorduk
ortalama alıyoruz ve merkezi ogenin yerine yerlestiriyoruz
"""

dst2 = cv2.blur(img , ksize = (3,3))
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("ortalama blur"),plt.show()

"""
gausian blur
ortalamasını almak yerine bu kutucukların içerisinde 
x ve y yönlerinde sigma değerleri yazarak kutucukların
2 boyutlu bir gaus olmasını saglıyoruz kutucukların  üzerindeki değerlere göre işlemler yapılıyor  
"""

gb = cv2.GaussianBlur(img , ksize=(3,3) ,sigmaX=7)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("gauss blur"),plt.show()

"""
medyan blur
ksize ı 3 olan bir filtre belirlenir kutucukların içindeki piksellerin medyanı alınıyor
"""
mb = cv2.medianBlur(img , ksize=3)
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("median blur"),plt.show()

def gaussianNoise(image):
    row,col,ch = img.shape
    mean = 0
    var = 0.05
    sigma = var**0.5

    gauss = np.random.normal(mean,sigma,(row,col,ch))
    gauss = gauss.reshape(row,col,ch)
    noisy = image + gauss
    return noisy


#gürültüyü ekleyebilmek için 0 255 aarsından 0 1 arasına tasıyoruz
#içeaktar normaliz et
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\Gi-1\nyc.jpg") 
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)/255 #normalize edildi
plt.figure(),plt.imshow(img),plt.axis("off"),plt.title("orijinal"),plt.show()

gaussianNoiseimage = gaussianNoise(img)
plt.figure(),plt.imshow(gaussianNoiseimage),plt.axis("off"),plt.title("gauss noisy"),plt.show()

#gauss blur
gb2 = cv2.GaussianBlur(gaussianNoiseimage , ksize=(3,3) ,sigmaX=7)
plt.figure(),plt.imshow(gb2),plt.axis("off"),plt.title("gauss blur  yapıldı"),plt.show()


#tuz karabiber gurultusu olusturup giderme

def saltPepperNoise(image):
    row,col,ch = image.shape
    s_vs_p = 0.5 # Beyaz (salt) ve siyah (pepper) oranı
    amount = 0.004 # Gürültü oranı
    noisy = np.copy(image) # Orijinal görüntünün kopyası oluşturuluyor

    #salt beyaz
    num_salt = np.ceil(amount * image.size * s_vs_p) #Kaç tane beyaz (salt) piksel olacağını hesaplıyor. 
    coords = [np.random.randint(0, i  , int (num_salt)) for i in image.shape[:2]] #np.random.randint(0, i  , int (num_salt)) baslangıc bitiş ve kac tane deger uretilecek
    noisy[tuple(coords)] = (255,255,255) # Seçilen koordinatlara beyaz (255,255,255) ata

    #pepper siyah
    num_pepper = np.ceil(amount * image.size * (1- s_vs_p)) #siyah noktaların sayısını hesapla
    coords = [np.random.randint(0, i  , int(num_pepper)) for i in image.shape[:2]] #rastgele koordinatlar üret
    noisy[tuple(coords)] = (0,0,0) #seçilen koordinatlara siyah ata
 
    return noisy

spimage = saltPepperNoise(img)
plt.figure(),plt.imshow(spimage),plt.axis("off"),plt.title("sp image"),plt.show()

mb2 = cv2.medianBlur((spimage).astype(np.float32) , ksize= 3)
plt.figure(),plt.imshow(mb2),plt.axis("off"),plt.title("with median blur"),plt.show()

#opencvde ondalıklı sayılar float32 olarak isteniyor



