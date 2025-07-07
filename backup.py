import os
import shutil
from datetime import datetime

def backup_folder(source_folder, backup_folder):
    if not os.path.exists(source_folder):
        print(f"❌ Source folder does not exist: {source_folder}")
        return

    if not os.path.exists(backup_folder):
        os.makedirs(backup_folder)

    timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
    destination = os.path.join(backup_folder, f"backup_{timestamp}")

    shutil.copytree(source_folder, destination)

    print(f"✅ Backup completed at {destination}")
