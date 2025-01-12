# Virtual Mouse Using Computer Vision

This project implements a virtual mouse using computer vision, enabling users to control their mouse pointer and perform actions like clicking using hand gestures. The system leverages OpenCV, MediaPipe, and PyAutoGUI for hand tracking and mouse control.

## Features
- **Hand Tracking**: Uses MediaPipe to detect and track hand landmarks in real-time.
- **Mouse Pointer Control**: Maps the index finger's movement to the screen to control the mouse pointer.
- **Click Gestures**: Simulates mouse clicks when the thumb and index finger form a pinch gesture.

## Prerequisites
Ensure the following Python libraries are installed:
- `opencv-python`
- `mediapipe`
- `pyautogui`
  
You can install these libraries using pip:
```bash
pip install opencv-python mediapipe pyautogui
