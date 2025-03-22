# Description: This script is used to run the YOLO model on a webcam feed. 
# It will display the webcam feed with bounding boxes around detected faces.

import cv2
from ultralytics import YOLO

# Load your trained model
model = YOLO('/Users/nathandeanon/Documents/CVProject/runs/detect/train7/weights/best.pt') 

# Open webcam (0 is the default camera)
cap = cv2.VideoCapture(1)

# Set frame width and height (optional)
cap.set(3, 640)  # Width
cap.set(4, 480)  # Height

while True:
    ret, frame = cap.read()
    if not ret:
        break


# Run inference with a lower confidence threshold
    results = model(frame, conf=0.5)

    #Debug: Print bounding box info
    boxes = results[0].boxes
    if boxes is not None and len(boxes) > 0:
        print("✅ Detections found:")
        for box in boxes:
            print(f" - Class: {int(box.cls[0])}, Confidence: {box.conf[0]:.2f}, Box: {box.xyxy[0].tolist()}")
    else:
        print("❌ No detections in this frame.")


    # Run YOLO inference on the frame
    results = model(frame)

    # Visualize the results
    annotated_frame = results[0].plot()

    # Display the frame
    cv2.imshow("YOLO Face Detection", annotated_frame)

    # Exit on pressing 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and close all windows
cap.release()
cv2.destroyAllWindows()