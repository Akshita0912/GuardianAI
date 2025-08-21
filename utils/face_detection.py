import cv2
from fer import FER

detector = FER(mtcnn=True)

def detect_face_emotion(frame):
    emotions = detector.detect_emotions(frame)
    if emotions:
        top_emotion, score = detector.top_emotion(frame)
        return top_emotion, score
    return "neutral", 0.0
