**Real-Time Computer Vision Event Detection (Python)**


_Overview_
This project implements a basic real-time computer vision pipeline using Python and OpenCV. It reads video input, processes frames to detect motion-based events, sends events in real time, and stores them for later analysis.
Features
Real-time video capture (webcam or video file)
Frame processing using OpenCV (grayscale + motion detection)
Event detection with timestamp, type, and metric
Real-time event communication via WebSocket / REST API
Event storage using SQLite or JSON file
Modular, clean, and well-documented code


_Tech Stack_
Python
OpenCV
NumPy
WebSockets 
SQLite


_How It Works-_
Capture video frames using OpenCV
Apply image processing to detect motion
Trigger events when motion exceeds a threshold
Send events as JSON to a backend or interface
Store events locally for analysis


_Assumptions_
Single camera input
Simple motion-based event logic
Local storage


_Author_
Abhinav Lahare
+91 9699232638
abhinavlahare55@gmail.com
Github-https://github.com/AbhinavLahare




