import os
from datetime import datetime

def log_unanswered(query):
    os.makedirs('data', exist_ok=True)
    log_file = "backend/data/feedback.csv"
    query_cleaned = query.strip().lower()

    if os.path.exists(log_file):
        with open(log_file, "r", encoding="utf-8") as f:
            for line in f:
                if "," in line:
                    _, existing_query = line.strip().split(",", 1)
                    if existing_query.strip().lower() == query_cleaned:
                        return 

    timestamp = datetime.now().isoformat()
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{timestamp},{query}\n")