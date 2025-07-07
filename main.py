from monitor import log_system_usage
from backup import backup_folder

log_system_usage()

# 🔁 Define folders (customize this as needed)
source = "C:/Users/Au/Documents/ImportantFiles"  # Change this path
destination = "C:/Users/Au/Documents/Backups"    # Change this path

backup_folder(source, destination)
