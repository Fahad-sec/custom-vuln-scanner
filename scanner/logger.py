import os 
from datetime import datetime

LOG_DIR = os.path.join(os.path.dirname(__file__), "..", "logs")

if not os.path.exists(LOG_DIR):
    os.makedirs(LOG_DIR)

def log(message):
    timestamp = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    line = f"{timestamp} {message}\n"
    log_file = os.path.join(LOG_DIR, "scanner.log")
    with open(log_file, "a") as f:
        f.write(line)

    print(message)


