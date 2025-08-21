import cv2
import sounddevice as sd
import numpy as np
import librosa
import threading
import time
from utils.face_detection import detect_face_emotion
from utils.speech_detection import detect_speech_emotion
from utils.alert_system import send_alert
from config import ALERT_THRESHOLD

def monitor_system():
    cap = cv2.VideoCapture(0)
    print("[INFO] GuardianAI started monitoring automatically...")

    while True:
        # --- FACE EMOTION ---
        ret, frame = cap.read()
        if not ret:
            break
        face_emotion, face_score = detect_face_emotion(frame)

        # --- SPEECH EMOTION ---
        def record_audio():
            duration = 3
            fs = 22050
            audio = sd.rec(int(duration * fs), samplerate=fs, channels=1, dtype='float32')
            sd.wait()
            y = np.squeeze(audio)
            return detect_speech_emotion(y, fs)

        speech_emotion, speech_score = record_audio()

        # --- DECISION ---
        if (face_score > ALERT_THRESHOLD and face_emotion in ["angry","fear","sad"]) \
           or (speech_score > ALERT_THRESHOLD and speech_emotion in ["angry","fear","sad"]):
            print(f"[ALERT] Distress detected! Face: {face_emotion} ({face_score:.2f}), Voice: {speech_emotion} ({speech_score:.2f})")
            send_alert(face_emotion, speech_emotion)
            time.sleep(5)  # Avoid spamming alerts

        # Show window (can be hidden in real deployment)
        cv2.imshow("GuardianAI Monitoring", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    monitor_system()
