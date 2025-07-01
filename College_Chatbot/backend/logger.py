import os
from datetime import datetime

LOG_DIR = "backend/logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_event(event_type, data):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    log_line = f"[{timestamp}] {event_type.upper()}: {data}\n"
    with open(os.path.join(LOG_DIR, "server.log"), "a", encoding="utf-8") as log_file:
        log_file.write(log_line)