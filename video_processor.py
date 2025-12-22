import cv2

class VideoProcessor:
    def __init__(self, source=0):
        self.cap = cv2.VideoCapture(source)
        self.prev_frame = None

    def get_frame(self):
        ret, frame = self.cap.read()
        if not ret:
            return None, None

        gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
        gray = cv2.GaussianBlur(gray, (21, 21), 0)

        motion_value = 0
        if self.prev_frame is not None:
            diff = cv2.absdiff(self.prev_frame, gray)
            _, thresh = cv2.threshold(diff, 25, 255, cv2.THRESH_BINARY)
            motion_value = cv2.countNonZero(thresh)

        self.prev_frame = gray
        return frame, motion_value
