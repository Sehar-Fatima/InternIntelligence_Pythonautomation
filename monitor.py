import psutil
from datetime import datetime

def log_system_usage():
    now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    cpu = psutil.cpu_percent(interval=1)
    memory = psutil.virtual_memory().percent
    disk = psutil.disk_usage('/').percent

    log_line = f"[{now}] CPU: {cpu}% | Memory: {memory}% | Disk: {disk}%"
    
    with open("system_log.txt", "a") as f:
        f.write(log_line + "\n")

    print(log_line)
