import tkinter as tk
from tkinter import messagebox
from monitor import log_system_usage
from backup import backup_folder

# Customize your folders here
SOURCE_FOLDER = "C:/Users/Au/Documents/ImportantFiles"
BACKUP_FOLDER = "C:/Users/Au/Documents/Backups"

def run_monitor():
    log_system_usage()
    status_label.config(text="✅ System monitoring done.")
    messagebox.showinfo("Done", "System info logged successfully!")

def run_backup():
    backup_folder(SOURCE_FOLDER, BACKUP_FOLDER)
    status_label.config(text="✅ Backup completed.")
    messagebox.showinfo("Done", "Backup created successfully!")

# Create GUI window
window = tk.Tk()
window.title("System Management Tool")
window.geometry("400x250")

# Title
title = tk.Label(window, text="🛠️ System Management Tool", font=("Arial", 16))
title.pack(pady=10)

# Monitor Button
monitor_btn = tk.Button(window, text="📊 Run System Monitoring", command=run_monitor, width=30)
monitor_btn.pack(pady=10)

# Backup Button
backup_btn = tk.Button(window, text="💾 Run File Backup", command=run_backup, width=30)
backup_btn.pack(pady=10)

# Status Label
status_label = tk.Label(window, text="Status: Waiting...", fg="blue")
status_label.pack(pady=20)

# Run the app
window.mainloop()
