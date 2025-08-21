import tkinter as tk
import threading
from guardianai_main import monitor_system

def start_monitoring():
    thread = threading.Thread(target=monitor_system, daemon=True)
    thread.start()

root = tk.Tk()
root.title("GuardianAI – Safety Monitor")
root.geometry("400x200")

label = tk.Label(root, text="🚨 GuardianAI – Safety & Health Monitor", font=("Arial", 14))
label.pack(pady=20)

start_button = tk.Button(root, text="Start Monitoring", command=start_monitoring, font=("Arial", 12))
start_button.pack(pady=10)

exit_button = tk.Button(root, text="Exit", command=root.destroy, font=("Arial", 12))
exit_button.pack(pady=10)

root.mainloop()
