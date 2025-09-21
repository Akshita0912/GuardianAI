import requests
from config import EMERGENCY_CONTACTS, HOSPITAL_API, POLICE_API, LOCATION

def send_alert(face_emotion, speech_emotion):
    message = f"🚨 ALERT: Distress detected!\nFace: {face_emotion}, Voice: {speech_emotion}\nLocation: {LOCATION}"

    print("[ALERT SYSTEM] Sending alerts...")

    for contact in EMERGENCY_CONTACTS:
        print(f"📱 Notifying {contact['name']} ({contact['phone']}) -> {message}")

    try:
        requests.post(HOSPITAL_API, json={"message": message, "location": LOCATION})
        print("🏥 Hospital notified")
    except:
        print("⚠️ Failed to notify hospital")

    try:
        requests.post(POLICE_API, json={"message": message, "location": LOCATION})
        print("🚔 Police notified")
    except:
        print("⚠️ Failed to notify police")
