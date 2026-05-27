from ultralytics import YOLO
import cv2

model = YOLO("yolov8s.pt")

cap = cv2.VideoCapture(0)

print(" 按 q 退出")

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法打开摄像头")
        break

    results = model(frame, verbose=False)
    annotated = results[0].plot()

    cv2.imshow("YOLO", annotated)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
