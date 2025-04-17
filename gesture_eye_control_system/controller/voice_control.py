
import speech_recognition as sr

class VoiceController:
    def __init__(self):
        self.recognizer = sr.Recognizer()

    def listen(self):
        with sr.Microphone() as source:
            print("[🎙️] Listening for command...")
            audio = self.recognizer.listen(source)
            try:
                command = self.recognizer.recognize_google(audio)
                print(f"[🔊] You said: {command}")
                return command.lower()
            except sr.UnknownValueError:
                print("[⚠️] Could not understand audio")
            except sr.RequestError as e:
                print(f"[❌] Speech service error: {e}")
            return None
