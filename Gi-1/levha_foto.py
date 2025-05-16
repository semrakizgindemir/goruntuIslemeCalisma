import cv2
import pytesseract
import matplotlib.pyplot as plt

# Eğer Windows kullanıyorsan tesseract yolunu belirt
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_sign_number(image_path):
    # Görüntüyü oku
    image = cv2.imread(image_path)

    if image is None:
        print("Resim YÜKLENEMEDİ!")
        return None

    # Gri ton, bulanıklık, eşikleme
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(gray, (5,5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    plt.figure(), plt.imshow(thresh) , plt.title("foto") , plt.show()



    # OCR ayarları - sadece sayı algılaması için
    config = "--psm 7 -c tessedit_char_whitelist=0123456789"
    result = pytesseract.image_to_string(thresh, config=config).strip()

    
    return result

# Kullanım
image_path = r"C:\Users\kizgi\Desktop\opencv\Gi-1\levha.jpg"
detected_number = detect_sign_number(image_path)

if detected_number:
    print("Okunan Rakam:", detected_number)
else:
    print("Rakam tespit edilemedi.")
