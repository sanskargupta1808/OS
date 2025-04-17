
import time
import cv2
from controller.gesture_recognition import GestureRecognizer
from controller.eye_tracking import EyeTracker
from controller.voice_control import VoiceController
from controller.os_automation import adjust_volume, switch_tab

def main():
    cap = cv2.VideoCapture(0)
    gesture_model = GestureRecognizer()
    eye_tracker = EyeTracker()
    voice_controller = VoiceController()

    last_voice_command = ""

    while True:
        ret, frame = cap.read()
        if not ret:
            break

        gesture, frame = gesture_model.detect_gesture(frame)
        eye_status = eye_tracker.get_eye_direction(frame)

        if gesture:
            cv2.putText(frame, gesture, (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)

        if eye_status:
            cv2.putText(frame, eye_status, (10, 70), cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)

        if cv2.waitKey(1) & 0xFF == ord("v"):
            command = voice_controller.listen()
            if command:
                last_voice_command = command
                if "volume up" in command:
                    adjust_volume(80)
                elif "volume down" in command:
                    adjust_volume(30)
                elif "switch tab" in command:
                    switch_tab()

        cv2.imshow("Gesture + Eye + Voice Control", frame)
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
