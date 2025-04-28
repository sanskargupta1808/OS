# Eye-Tracking Based Operating System

> A revolutionary hands-free operating system interface driven entirely by eye-tracking and blink detection.

---

## 🚀 Project Overview

The **Eye-Tracking Based Operating System** enables users to interact with their computer systems without physical touch — using only **eye movement** and **blinking gestures**.  
This accessibility-focused project aims to assist individuals with disabilities, support hands-free environments, and redefine human-computer interaction.

Key capabilities include:
- Eye gaze-based **cursor movement**
- **Blink-based clicks** (single/double blink for left/right click)
- Lightweight, real-time performance
- Works with any standard webcam (no specialized hardware needed)

---

## 🎯 Features

- **Real-Time Eye Tracking**: Follows user's gaze to control mouse pointer on screen.
- **Blink Detection**:
  - Single blink → Left Click
  - Double blink → Right Click
- **Customizable Sensitivity**: Adjust blink detection thresholds and cursor speed.
- **Cross-Platform Support**: Works on Windows, MacOS, and Linux (Python-based).
- **Lightweight Interface**: Minimal resource consumption, runs efficiently on standard hardware.

---

## 🛠️ Tech Stack

| Technology | Purpose |
|:-----------|:--------|
| Python | Core programming language |
| OpenCV | Eye detection, frame processing |
| Dlib / Mediapipe | Facial landmarks (eye regions) |
| PyAutoGUI | Mouse control (move/click) |
| NumPy | Mathematical operations |
| Tkinter / PyQt5 (Optional) | GUI settings panel |

---

## 📷 System Architecture
Webcam Feed
    ↓
Face Detection
    ↓
Eye Region Extraction
    ↓
Pupil Tracking + Blink Detection
    ↓
Cursor Movement & Click Simulation



✨ Author

Sanskar Gupta
Student | ML Engineer | Vision Systems Enthusiast
