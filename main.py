# Description: This script is used to train the YOLO model on a custom dataset.
# It will save the best weights in the 'runs/train' directory.

import cv2
from ultralytics import YOLO


model = YOLO('yolov8n.pt') #load model


results = model.train(data = "config.yaml", epochs = 75) #train model