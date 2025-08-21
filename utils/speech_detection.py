import numpy as np
import librosa
import tensorflow as tf
import os

# Load pre-trained speech emotion model
MODEL_PATH = "models/speech_emotion_model.h5"
if os.path.exists(MODEL_PATH):
    model = tf.keras.models.load_model(MODEL_PATH)
    emotions = ["neutral","calm","happy","sad","angry","fear","disgust","surprise"]
else:
    model = None
    emotions = []

def extract_features(y, sr):
    mfcc = librosa.feature.mfcc(y=y, sr=sr, n_mfcc=40)
    mfcc_scaled = np.mean(mfcc.T, axis=0)
    return np.expand_dims(mfcc_scaled, axis=0)

def detect_speech_emotion(y, sr):
    if model is None:
        return "neutral", 0.0
    features = extract_features(y, sr)
    preds = model.predict(features, verbose=0)
    idx = np.argmax(preds)
    return emotions[idx], preds[0][idx]
