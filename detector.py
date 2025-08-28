# detector.py
from ultralytics import YOLO
import cv2

class Detector:
    def __init__(self, model_path='yolov8n.pt'):
        self.model = YOLO(model_path)
    def detect_persons(self, frame, conf_thres=0.35):
        res = self.model(frame)[0]
        boxes = []
        for box in res.boxes:
            if int(box.cls[0]) == 0 and float(box.conf[0]) > conf_thres:
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                boxes.append([x1,y1,x2,y2,float(box.conf[0])])
        return boxes
    def blur_faces(self, frame):
        # naive: blur all person boxes for privacy
        res = self.model(frame)[0]
        for box in res.boxes:
            if int(box.cls[0]) == 0:
                x1,y1,x2,y2 = map(int, box.xyxy[0])
                face = frame[y1:y2, x1:x2]
                frame[y1:y2, x1:x2] = cv2.GaussianBlur(face, (51,51), 0)
        return frame
