
import cv2
import mediapipe as mp

class GestureRecognizer:
    def __init__(self):
        self.hands = mp.solutions.hands.Hands(min_detection_confidence=0.7)
        self.mp_draw = mp.solutions.drawing_utils

    def detect_gesture(self, frame):
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = self.hands.process(frame_rgb)
        gesture = None

        if results.multi_hand_landmarks:
            for hand_landmarks in results.multi_hand_landmarks:
                gesture = "Hand Detected"
                self.mp_draw.draw_landmarks(frame, hand_landmarks, mp.solutions.hands.HAND_CONNECTIONS)
        return gesture, frame
