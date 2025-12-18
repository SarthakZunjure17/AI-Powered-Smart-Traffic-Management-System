import cv2
import os
import uuid
from ultralytics import YOLO

# ================= CONFIG =================
MODEL_PATH = "runs/detect/train/weights/last.pt"
CONF_THRESHOLD = 0.5
OUTPUT_DIR = "output"
EMERGENCY_CLASSES = ["ambulance", "police", "fire brigade"]
# =========================================

os.makedirs(OUTPUT_DIR, exist_ok=True)

print("🔄 Loading YOLO model...")
model = YOLO(MODEL_PATH)
print("✅ Model loaded")


def analyze_video(video_path):
    cap = cv2.VideoCapture(video_path)

    if not cap.isOpened():
        raise Exception("❌ Could not open video")

    width = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    fps = cap.get(cv2.CAP_PROP_FPS)
    if fps == 0 or fps is None:
        fps = 25  # SAFE DEFAULT
        print("⚠ FPS was 0, using fallback:", fps)

    output_filename = f"{uuid.uuid4().hex}.mp4"
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    # Browser-compatible codec
    fourcc = cv2.VideoWriter_fourcc(*"avc1")
    out = cv2.VideoWriter(output_path, fourcc, fps, (width, height))

    emergency_detected = False
    detected_class = "N/A"
    best_confidence = 0.0

    frame_count = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        frame_count += 1

        # 🔥 SPEED BOOST: skip frames
        if frame_count % 2 != 0:
            out.write(frame)
            continue

        results = model(frame, conf=CONF_THRESHOLD, verbose=False)[0]

        for box in results.boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])
            label = results.names[cls_id]

            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)

            if label in EMERGENCY_CLASSES:
                emergency_detected = True
                detected_class = label
                best_confidence = max(best_confidence, conf)
                color = (0, 0, 255)
                text = f"{label.upper()} {conf:.2f}"
            else:
                color = (0, 255, 0)
                text = f"{label} {conf:.2f}"

            cv2.rectangle(frame, (x1, y1), (x2, y2), color, 3)
            cv2.putText(
                frame,
                text,
                (x1, max(30, y1 - 10)),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.7,
                color,
                2,
            )

        if emergency_detected:
            cv2.putText(
                frame,
                "🚦 SIGNAL PRIORITY ACTIVATED",
                (30, 50),
                cv2.FONT_HERSHEY_DUPLEX,
                1,
                (0, 0, 255),
                2,
            )

        out.write(frame)

    cap.release()
    out.release()

    # 🔍 VERIFY OUTPUT
    size_mb = os.path.getsize(output_path) / (1024 * 1024)
    print(f"🎬 Output video saved: {output_filename} ({size_mb:.2f} MB)")

    return {
        "emergency": emergency_detected,
        "vehicle_type": detected_class if emergency_detected else "N/A",
        "confidence": round(best_confidence, 2),
        "signal": "GREEN SIGNAL FOR EMERGENCY LANE" if emergency_detected else "NORMAL SIGNAL",
        "output_video": f"/output/{output_filename}",
    }
