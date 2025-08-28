# pose.py
import mediapipe as mp
import numpy as np
import cv2

mp_pose = mp.solutions.pose

class PoseAnalyzer:
    def __init__(self):
        self.pose = mp_pose.Pose(min_detection_confidence=0.5)
        self.history = {}  # track_id -> positions

    def estimate(self, crop):
        try:
            img = cv2.cvtColor(crop, cv2.COLOR_BGR2RGB)
            res = self.pose.process(img)
            return res.pose_landmarks
        except Exception:
            return None

    def evaluate_rules(self, track_id, landmarks, bbox):
        # landmarks: mediapipe results or None
        # bbox: (x1,y1,x2,y2)
        # Returns event string or None
        if track_id not in self.history:
            self.history[track_id] = {'y': [], 't': 0}
        if landmarks:
            # use hip y as proxy height
            l = landmarks.landmark
            left_hip = l[mp_pose.PoseLandmark.LEFT_HIP.value].y
            right_hip = l[mp_pose.PoseLandmark.RIGHT_HIP.value].y
            hip = (left_hip + right_hip) / 2
            self.history[track_id]['y'].append(hip)
            if len(self.history[track_id]['y']) > 10:
                self.history[track_id]['y'].pop(0)
            # simple fall detection: large var in hip positions
            if max(self.history[track_id]['y']) - min(self.history[track_id]['y']) > 0.25:
                return 'FallDetected'
        return None
