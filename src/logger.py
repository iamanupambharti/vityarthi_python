from datetime import datetime
import os

LOG_FOLDER = "logs"

def _get_log_file_path():
    today = datetime.now().strftime("%Y-%m-%d")
    return os.path.join(LOG_FOLDER, f"{today}.log")

def _write_log(message_type, message):

    if not os.path.exists(LOG_FOLDER):
        os.makedirs(LOG_FOLDER)

    log_file = _get_log_file_path()

    with open(log_file, "a", encoding="utf-8") as f:
        timestamp = datetime.now().strftime("%H:%M:%S")
        f.write(f"[{timestamp}] [{message_type}] {message}\n")

def log_info(message):
    _write_log("INFO", message)

def log_error(message):
    _write_log("ERROR", message)
