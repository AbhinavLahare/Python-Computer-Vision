import cv2
import asyncio
import time

from video_processor import VideoProcessor
from event_manager import detect_motion
from database import EventDatabase
from websocket_client import WebSocketClient

video = VideoProcessor(0)
db = EventDatabase()
ws = WebSocketClient()

prev_time = time.time()

while True:
    frame, motion_value = video.get_frame()
    if frame is None:
        break

    event = detect_motion(motion_value)
    if event:
        db.insert_event(event)
        print("Event detected:", event)

    # FPS
    curr_time = time.time()
    fps = int(1 / (curr_time - prev_time))
    prev_time = curr_time

    cv2.putText(frame, f"FPS: {fps}", (10,30),
                cv2.FONT_HERSHEY_SIMPLEX, 1, (0,255,0), 2)

    cv2.imshow("Motion Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
