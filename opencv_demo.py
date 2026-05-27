import cv2

cap = cv2.VideoCapture(0)

print("按 'q' 退出，按 'g' 切换灰度/彩色")

gray_mode = False

while True:
    ret, frame = cap.read()
    if not ret:
        print("无法打开摄像头")
        break

    if gray_mode:
        display = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        display = cv2.cvtColor(display, cv2.COLOR_GRAY2BGR)
    else:
        display = frame

    h, w = display.shape[:2]
    cv2.putText(display, f"{'GRAY' if gray_mode else 'COLOR'} | {w}x{h}",
                (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

    cv2.imshow("OpenCV Demo", display)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break
    elif key == ord('g'):
        gray_mode = not gray_mode

cap.release()
cv2.destroyAllWindows()
