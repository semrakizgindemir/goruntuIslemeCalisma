import cv2
import numpy as np


# 3 daire ile ortak merkeze gore nisan alma
# Görüntüyü yükle
img = cv2.imread(r"C:\Users\kizgi\Desktop\opencv\ika_denemeler\hedef.png")  # Hedefin bulunduğu görsel
img = cv2.resize(img, (640, 480))  # İşlem kolaylığı için yeniden boyutlandır
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
blur = cv2.GaussianBlur(gray, (7, 7), 0)

# Hough Circle ile daireleri bul
circles = cv2.HoughCircles(
    blur,
    cv2.HOUGH_GRADIENT,
    dp=1.2,
    minDist=1,
    param1=100,
    param2=50,
    minRadius=84,
    maxRadius=252
)

frame_center = (img.shape[1] // 2, img.shape[0] // 2)
cv2.circle(img, frame_center, 4, (0, 255, 0), -1)  # Görüntü merkezini yeşil nokta olarak çiz

if circles is not None and len(circles[0]) >= 3:
    circles = np.uint16(np.around(circles))
    
    # En küçük 3 daireyi al (yarıçapa göre sırala)
    sorted_circles = sorted(circles[0, :], key=lambda x: x[2])
    selected_circles = sorted_circles[:3]

    # Ortak merkezi hesapla
    sum_x = sum(circle[0] for circle in selected_circles)
    sum_y = sum(circle[1] for circle in selected_circles)
    avg_x = int(sum_x / 3)
    avg_y = int(sum_y / 3)

    # Tüm daireleri ve ortak merkezi çiz
    for c in selected_circles:
        cv2.circle(img, (c[0], c[1]), c[2], (255, 0, 0), 2)
        cv2.circle(img, (c[0], c[1]), 3, (0, 0, 255), -1)

    cv2.circle(img, (avg_x, avg_y), 5, (0, 255, 255), -1)
    cv2.putText(img, "Ortak Merkez", (avg_x + 10, avg_y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 2)

    # Nişan doğruluğu: görüntü merkezi ile hedef merkezi farkı
    dx = avg_x - frame_center[0]
    dy = avg_y - frame_center[1]

    yön = ""
    if abs(dx) < 10 and abs(dy) < 10:
        yön = "HEDEF MERKEZDE - ATIS!"
    else:
        if dx > 10:
            yön += "SAĞA "
        elif dx < -10:
            yön += "SOLA "
        if dy > 10:
            yön += "AŞAĞI "
        elif dy < -10:
            yön += "YUKARI "

    print(f"Nişan Sapması → dx: {dx}, dy: {dy} → {yön}")
    cv2.putText(img, yön, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 0, 0), 2)

else:
    print("3 daire algılanamadı.")

# Sonuç görüntüsünü göster
cv2.imshow("Nişan Sistemi", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
