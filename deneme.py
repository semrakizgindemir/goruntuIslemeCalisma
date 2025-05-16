

import cv2
import matplotlib.pyplot as plt
from inference_sdk import InferenceHTTPClient

# Roboflow API
CLIENT = InferenceHTTPClient(
    api_url="https://detect.roboflow.com",
    api_key="r4YlrEzeBmvhi6udx5K2"
)

# Görsel yolu
img_path = r"C:\Users\kizgi\Desktop\opencv\ika_denemeler\84415b06c31771e834df88b0ae195939.jpeg"

# Roboflow'dan tahmin al
result = CLIENT.infer(img_path, model_id="traffic-sign-detection-3yjuv/2")

# Görseli oku
img = cv2.imread(img_path)

# Her tahmin için dikdörtgen çiz
for pred in result["predictions"]:
    x = int(pred["x"])
    y = int(pred["y"])
    w = int(pred["width"])
    h = int(pred["height"])
    conf = pred["confidence"]
    label = pred["class"]

    # Dikdörtgenin köşeleri
    top_left = (x - w//2, y - h//2)
    bottom_right = (x + w//2, y + h//2)

    # Daire etrafına dikdörtgen çiz
    cv2.rectangle(img, top_left, bottom_right, (0, 255, 0), 2)
    # Üstüne sınıf adı ve güven skorunu yaz
    cv2.putText(img, f"{label} {conf:.2f}", (top_left[0], top_left[1] - 10),
                cv2.FONT_HERSHEY_SIMPLEX, 0.6, (0, 255, 0), 2)

# Sonucu göster
img_rgb = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.figure(figsize=(10,6))
plt.imshow(img_rgb)
plt.axis("off")
plt.title("Tespit Edilen Daireler")
plt.show()