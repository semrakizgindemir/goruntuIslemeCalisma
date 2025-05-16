import pyrealsense2 as rs
import numpy as np
import cv2
import pytesseract
import time

# Tesseract yolunu ayarlayın (Senin sisteminde farklı olabilir!)
pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"

# RealSense pipeline başlat
pipeline = rs.pipeline()
config = rs.config()

config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)
pipeline.start(config)

# Son algılanan metni takip et
last_detected_text = ""

try:
    while True:
        frames = pipeline.wait_for_frames()
        color_frame = frames.get_color_frame()
        if not color_frame:
            continue

        color_image = np.asanyarray(color_frame.get_data())
        gray = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
        _, thresh = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY_INV)

        # OCR ile sayı algılama
        custom_config = r'--oem 3 --psm 6 outputbase digits'
        detected_text = pytesseract.image_to_string(thresh, config=custom_config).strip()

        # Eğer yeni bir sonuç algılanmışsa, terminale yazdır
        if detected_text != last_detected_text:
            last_detected_text = detected_text
            print(f"Algilanan: {detected_text}")  # Terminale yazdır

        # Görüntüyü göster
        cv2.imshow("RealSense Sayı Algılama", color_image)

        # Döngüde her 200 ms bekle (ekranın hızını sınırlamak için)
        time.sleep(0.2)  # 200 ms bekle

        # 'q' tuşuna basıldığında döngüyü kır
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()
