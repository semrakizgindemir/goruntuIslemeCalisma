import cv2
import numpy as np
import pytesseract

# Tesseract yolunu belirt (Windows kullanıyorsan gerekebilir)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Görüntüyü yükle
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\ika_denemeler\images.jpg")
img = cv2.resize(img, (960, 540))  # İşlem hızını artırmak için yeniden boyutlandır

# Gaussian blur ile yumuşatma
blurred = cv2.GaussianBlur(img, (5, 5), 0)

# HSV renk uzayına çevir
hsv = cv2.cvtColor(blurred, cv2.COLOR_BGR2HSV)

# Kırmızı renk aralığı (2 ayrı aralık kullanılır)
lower_red1 = np.array([0, 70, 50])
upper_red1 = np.array([10, 255, 255])
lower_red2 = np.array([170, 70, 50])
upper_red2 = np.array([180, 255, 255])

# Maskeleri oluştur ve birleştir
mask1 = cv2.inRange(hsv, lower_red1, upper_red1)
mask2 = cv2.inRange(hsv, lower_red2, upper_red2)
red_mask = cv2.bitwise_or(mask1, mask2)

# Kenar bulma (Canny)
edges = cv2.Canny(red_mask, 100, 200)

# Hough Circle ile daire tespiti
circles = cv2.HoughCircles(edges, cv2.HOUGH_GRADIENT, dp=1, minDist=30,
                           param1=100, param2=25, minRadius=10, maxRadius=50)

if circles is not None:
    circles = np.uint16(np.around(circles))
    for i in circles[0, :]:
        x, y, r = i
        # Daire çiz
        cv2.circle(img, (x, y), r, (0, 255, 0), 2)

        # Dairenin içini crop et
        margin = 5  # güvenlik payı
        x1 = max(x - r + margin, 0)
        y1 = max(y - r + margin, 0)
        x2 = min(x + r - margin, img.shape[1])
        y2 = min(y + r - margin, img.shape[0])
        roi = img[y1:y2, x1:x2]

        # OCR için hazırlık
        gray_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2GRAY)
        thresh = cv2.threshold(gray_roi, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)[1]

        # OCR ayarı (sadece rakam)
        config = "--psm 10 -c tessedit_char_whitelist=0123456789"
        number = pytesseract.image_to_string(thresh, config=config).strip()

        print(f"Bulunan Sayı: {number}")

        # Görsele sonucu yaz
        cv2.putText(img, number, (x - 10, y - r - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (0, 0, 0), 2)

# Sonuç göster
cv2.imshow("Tespit Edilen Tabelalar", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
