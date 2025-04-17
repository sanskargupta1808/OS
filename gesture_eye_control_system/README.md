
# 👁️✋🗣️ Gesture, Eye & Voice Control System (macOS Assistive App)

This system fuses gesture recognition, eye tracking, and voice commands to create a hands-free, intelligent assistive tool. Designed for accessibility and OS-level automation on macOS.

---

## Features

- ✋ Real-time hand gesture detection (MediaPipe)
- 👁️ Eye-tracking using dlib + facial landmarks
- 🗣️ Voice command detection via microphone
- 🎛️ OS automation for:
  - Volume control
  - Tab switching
- 🖥️ macOS AppleScript integration (cross-platform adaptable)

---

## Setup Instructions

1. **Install dependencies**
```bash
pip install -r requirements.txt
```

2. **Download dlib landmark model**
[shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

3. **Run the app**
```bash
python main.py
```

- Press `v` to trigger voice listening
- Say things like:
  - "volume up"
  - "volume down"
  - "switch tab"

---

## Use Cases

- Accessibility tools for users with limited mobility
- Touchless media and system control
- Smart home or robotics integrations

---

## Author

**Sanskar Gupta**  
AI & Robotics, VIT Chennai

---

## License

MIT
