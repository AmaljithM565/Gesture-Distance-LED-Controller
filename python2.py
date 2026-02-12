import cv2
import mediapipe as mp
import serial
import time
import math

esp = serial.Serial("COM9", 115200)
time.sleep(2)

mp_hands = mp.solutions.hands
hands = mp_hands.Hands(max_num_hands=1)
mp_draw = mp.solutions.drawing_utils

cap = cv2.VideoCapture(1)

last_level = -1

MIN_DIST = 20
MAX_DIST = 200

while True:
    success, img = cap.read()
    if not success:
        break

    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    level = 0

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:

            h, w, _ = img.shape

            thumb_tip = handLms.landmark[4]
            tx, ty = int(thumb_tip.x * w), int(thumb_tip.y * h)

            index_tip = handLms.landmark[8]
            ix, iy = int(index_tip.x * w), int(index_tip.y * h)

            cv2.circle(img, (tx, ty), 10, (255, 0, 0), -1)
            cv2.circle(img, (ix, iy), 10, (255, 0, 0), -1)

            dist = math.hypot(ix - tx, iy - ty)

            if dist < MIN_DIST:
                level = 0
            else:
                level = int((dist - MIN_DIST) / (MAX_DIST - MIN_DIST) * 4)

            level = max(0, min(4, level))

            mp_draw.draw_landmarks(img, handLms, mp_hands.HAND_CONNECTIONS)

    if level != last_level:
        esp.write(f"{level}\n".encode())
        last_level = level

    cv2.imshow("Thumb-Index LED Control", img)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()
esp.close()
