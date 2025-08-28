# app.py
import time, os, json, argparse
import cv2
from detector import Detector
from tracker import Tracker
from pose import PoseAnalyzer
from alerting import AlertManager
from collections import deque

# Load config
parser = argparse.ArgumentParser()
parser.add_argument('--config', default='config.json')
args = parser.parse_args()
with open(args.config) as f:
    cfg = json.load(f)

cap = cv2.VideoCapture(cfg['camera_source'])

det = Detector()
trk = Tracker()
pose = PoseAnalyzer()
alert_mgr = AlertManager(cfg['clip_dir'])

# Circular frame buffer for last N seconds
frame_buffer = deque(maxlen=300)  # about 10s @30fps

while True:
    ret, frame = cap.read()
    if not ret:
        time.sleep(0.5)
        continue

    frame_buffer.append(frame.copy())

    boxes = det.detect_persons(frame)  # returns list of [x1,y1,x2,y2,conf]
    tracks = trk.update(boxes)

    for t in tracks:
        x1,y1,x2,y2,tid = map(int, t)
        crop = frame[y1:y2, x1:x2]
        landmarks = pose.estimate(crop)
        event = pose.evaluate_rules(tid, landmarks, (x1,y1,x2,y2))
        if event:
            # save clip from buffer
            clip_path = alert_mgr.save_clip(list(frame_buffer), event_type=event)
            alert_mgr.queue_event(event, clip_path)

    # Optional: show blurred live view for demo
    display = frame.copy()
    if cfg.get('blur_faces_by_default', True):
        display = det.blur_faces(display)
    cv2.imshow('CCTV Smart Guard', display)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
