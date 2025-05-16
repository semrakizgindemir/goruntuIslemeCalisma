import cv2
import pytesseract

# Tesseract yolu — kendi sistemine göre ayarla!
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def detect_sign_number(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    _, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY_INV)
    contours, _ = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for cnt in contours:
        area = cv2.contourArea(cnt)
        if area > 500:  # Tabela boyut filtresi
            x, y, w, h = cv2.boundingRect(cnt)
            roi = image[y:y+h, x:x+w]

            config = '--psm 8 -c tessedit_char_whitelist=0123456789'
            text = pytesseract.image_to_string(roi, config=config).strip()

            if text.isdigit():
                return int(text)

    return None  # Sayı bulunamazsa

# Kameradan görüntü alıp sayıyı döndür
cap = cv2.VideoCapture(0)

while True:
    ret, frame = cap.read()
    if not ret:
        break

    number = detect_sign_number(frame)
    if number is not None:
        print("Okunan sayı:", number)

    cv2.imshow("Kamera", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
