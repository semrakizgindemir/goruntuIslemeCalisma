import cv2
import numpy as np

# Hedef görüntüsünü oku (kamera yerine fotoğraf üzerinden gösteriyorum)
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\ika_denemeler\hedef.png")  # Bu kısmı kamerayla değiştirebilirsin
img = cv2.resize(img, (640, 480))
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# Gürültü azaltmak için bulanıklaştır
blurred = cv2.GaussianBlur(gray, (9, 9), 2)

# Hough Circle ile daireleri bul
circles = cv2.HoughCircles(
    blurred,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=1,
    param1=100,
    param2=50,
    minRadius=84,
    maxRadius=252
)

frame_center = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(img, frame_center, 3, (0, 255, 0), -1)  # Görüntü merkezini çiz

if circles is not None:
    circles = np.uint16(np.around(circles))

    # En büyük daireyi seç (dış daireyi temsil eder)
    largest_circle = max(circles[0, :], key=lambda x: x[2])
    x, y, r = largest_circle
    cv2.circle(img, (x, y), r, (255, 0, 0), 2)  # Daireyi çiz
    cv2.circle(img, (x, y), 3, (0, 0, 255), -1)  # Merkezini işaretle

    dx = x - frame_center[0]
    dy = y - frame_center[1]

    # Basit yönlendirme komutu üretimi
    yön = ""
    if abs(dx) < 10 and abs(dy) < 10:
        yön = "HEDEF MERKEZDE - ATIŞ YAP!"
    else:
        if dx > 10:
            yön += "SAĞA "
        elif dx < -10:
            yön += "SOLA "
        if dy > 10:
            yön += "AŞAĞI "
        elif dy < -10:
            yön += "YUKARI "

    print(f"Hedef ile fark (dx: {dx}, dy: {dy}) → Komut: {yön}")
    cv2.putText(img, yön, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

else:
    print("Daire tespit edilemedi.")

# Görüntüyü göster
cv2.imshow("Hedefe Nişan", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
