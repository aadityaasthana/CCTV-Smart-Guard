# tracker.py
import numpy as np
from sort import Sort

class Tracker:
    def __init__(self):
        self.tracker = Sort()
    def update(self, dets):
        # dets = [[x1,y1,x2,y2,conf],...]
        if len(dets) == 0:
            return []
        arr = np.array(dets)
        tracks = self.tracker.update(arr)
        # tracks: [[x1,y1,x2,y2,track_id],...]
        return tracks
