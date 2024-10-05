import tkinter as tk
from tkinter import messagebox
import time
import threading
from datetime import datetime

# Create the main application window
root = tk.Tk()
root.title("Alarm Clock")
root.geometry("400x250")

# Define the alarm date and time input fields
date_label = tk.Label(root, text="Set Alarm Date (YYYY-MM-DD):", font=("Helvetica", 14))
date_label.pack(pady=10)

date_entry = tk.Entry(root, font=("Helvetica", 14))
date_entry.pack(pady=10)

time_label = tk.Label(root, text="Set Alarm Time (HH:MM):", font=("Helvetica", 14))
time_label.pack(pady=10)

time_entry = tk.Entry(root, font=("Helvetica", 14))
time_entry.pack(pady=10)

# Define the function to check the alarm
def check_alarm(alarm_datetime):
    while True:
        current_datetime = datetime.now().strftime("%Y-%m-%d %H:%M")
        if current_datetime == alarm_datetime:
            messagebox.showinfo("Alarm", "It's time to wake up")
            break
        time.sleep(1)

# Define the function to set the alarm
def set_alarm():
    alarm_date = date_entry.get()
    alarm_time = time_entry.get()
    alarm_datetime = f"{alarm_date} {alarm_time}"
    alarm_thread = threading.Thread(target=check_alarm, args=(alarm_datetime,))
    alarm_thread.start()

# Add a button to set the alarm
set_alarm_button = tk.Button(root, text="Set Alarm", font=("Helvetica", 14), command=set_alarm)
set_alarm_button.pack(pady=10)

# Run the main application loop
root.mainloop()
