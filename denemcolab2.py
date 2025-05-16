from ultralytics import YOLO
import cv2
import matplotlib.pyplot as plt

# Modeli yükle
model = YOLO(r"C:\Users\kizgi\Desktop\opencv\ika_denemeler\best (2).pt")

# Görseli yükle
img_path = r"C:\Users\kizgi\Desktop\opencv\ika_denemeler\indir.jpeg"
results = model(img_path, conf=0.25, save=False)

# Görseli cv2 ile oku (çünkü yukarıda path ile model çalıştı)
img = cv2.imread(img_path)

# İlk sonuç nesnesini al
result = results[0]

# Tüm box'ları al
boxes = result.boxes

for box in boxes:
    x1, y1, x2, y2 = box.xyxy[0].int().tolist()
    conf = box.conf[0].item()
    cls = int(box.cls[0].item())

    # Dikdörtgen çiz
    cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 0), 2)
    cv2.putText(img, f"{cls} {conf:.2f}", (x1, y1 - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 0, 0), 2)

# Görüntüyü göster
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,6))
plt.imshow(img_rgb)
plt.axis("off")
plt.title("Tespit Edilen Objeler")
plt.show()

