# alerting.py
import cv2, os, time

class AlertManager:
    def __init__(self, clip_dir='data/clips'):
        self.clip_dir = clip_dir
        os.makedirs(clip_dir, exist_ok=True)

    def save_clip(self, frames, event_type='Event'):
        ts = int(time.time())
        path = os.path.join(self.clip_dir, f"{event_type}_{ts}.mp4")
        h, w = frames[0].shape[:2]
        out = cv2.VideoWriter(path, cv2.VideoWriter_fourcc(*'mp4v'), 10, (w, h))
        for f in frames:
            out.write(f)
        out.release()
        return path

    def queue_event(self, event_type, clip_path):
        print(f"Event queued: {event_type}, clip: {clip_path}")
        # TODO: push to operator via webhook/Twilio/Telegram after confirmation
