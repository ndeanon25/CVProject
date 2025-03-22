# Description: This script is used to test the webcam. 
# It opens the webcam and displays the video feed in a window. 
# Press 'q' to exit the window.

import cv2

cap = cv2.VideoCapture(1)

if not cap.isOpened():
    print("❌ Cannot open webcam")
    exit()

while True:
    ret, frame = cap.read()
    if not ret:
        print("❌ Can't receive frame. Exiting...")
        break

    cv2.imshow('Webcam Test', frame)

    if cv2.waitKey(1) == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()