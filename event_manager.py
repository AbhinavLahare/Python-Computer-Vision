import time

MOTION_THRESHOLD = 5000

def detect_motion(motion_value):
    if motion_value > MOTION_THRESHOLD:
        return {
            "timestamp": time.strftime("%Y-%m-%d %H:%M:%S"),
            "type": "motion_detected",
            "value": motion_value
        }
    return None
