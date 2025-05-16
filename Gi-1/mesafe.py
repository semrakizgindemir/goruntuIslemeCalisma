import pyrealsense2 as rs
import numpy as np
import cv2

# RealSense pipeline başlat
pipeline = rs.pipeline()
config = rs.config()

# Renk ve derinlik akışlarını aç
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

# Başlat
pipeline.start(config)

try:
    while True:
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        color_frame = frames.get_color_frame()

        if not depth_frame or not color_frame:
            continue

        depth_image = np.asanyarray(depth_frame.get_data())
        color_image = np.asanyarray(color_frame.get_data())

        # Bir nokta seçelim (örnek: ekranın ortası)
        x = int(depth_image.shape[1] / 2)
        y = int(depth_image.shape[0] / 2)

        # Bu noktadaki mesafeyi al
        distance = depth_frame.get_distance(x, y)

        # Görüntü üzerine yaz
        cv2.circle(color_image, (x, y), 5, (0, 0, 255), -1)
        cv2.putText(color_image, f"{distance:.2f} meters",
                    (x-50, y-10), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

        # Ekranda göster
        cv2.imshow("RealSense Mesafe Olcer", color_image)

        # Çıkış için 'q' tuşuna bas
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    pipeline.stop()
    cv2.destroyAllWindows()
