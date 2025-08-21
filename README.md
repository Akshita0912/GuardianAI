# 🚨 GuardianAI – Passenger & Driver Safety Framework  

GuardianAI is an AI-powered framework for **real-time passenger safety and driver health monitoring**.  
It uses **facial emotion recognition (FER)** and **speech emotion recognition (SER)** to detect distress, harassment, or fatigue.  
If risk is detected, the system automatically **alerts nearby hospitals, police stations, and emergency contacts**.  

---

## 📌 Features  
- 🎥 Real-time **face emotion detection** (fear, anger, sadness, etc.)  
- 🎤 **Voice emotion recognition** from passenger/driver audio  
- ⚡ Fully **automatic monitoring** (no button clicks needed)  
- 🚨 **Emergency alerts** sent to contacts & authorities  
- 🖥️ Tkinter UI (optional, for demo purposes)  
- 🧠 Extendable with **datasets** (AffectNet, RAVDESS) for training  

---

## 📂 Project Structure  
GuardianAI/
│── README.md # Project documentation

│── requirements.txt # Dependencies list

│── guardianai_main.py # Core script (automatic monitoring & alerting)

│── guardianai_ui.py # Optional Tkinter-based interface

│── config.py # Configuration file (contacts, API keys, settings)

│

├── models/ # Pre-trained or fine-tuned models

│ ├── face_emotion_model.h5

│ └── speech_emotion_model.h5

│

├── data/ # Datasets (AffectNet, RAVDESS, etc.)

│

├── utils/ # Helper modules

│ ├── face_detection.py

│ ├── speech_detection.py

│ ├── alert_system.py

│ └── preprocess.py

│

├── outputs/ # Logs, results, screenshots

│ ├── logs.txt

│ └── results.csv

│

└── docs/ # Documentation & diagrams

├── architecture.png

└── uml.png

---

## ⚙️ Installation  

```bash
# Clone repo
git clone https://github.com/your-username/GuardianAI.git
cd GuardianAI

# Install dependencies
pip install -r requirements.txt
