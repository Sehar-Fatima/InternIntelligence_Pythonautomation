import schedule
import time
from monitor import log_system_usage
from backup import backup_folder

# Set folders (make sure they exist)
source = "C:/Users/Au/Documents/ImportantFiles"
destination = "C:/Users/Au/Documents/Backups"

# Define task
def job():
    print("🔁 Running scheduled task...")
    log_system_usage()
    backup_folder(source, destination)

# Run every 1 minute for testing
schedule.every(1).minutes.do(job)

print("📅 Scheduler started. Waiting for next run...")

while True:
    schedule.run_pending()
    time.sleep(1)
