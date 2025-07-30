def send_message(status, user_id, log_file="logs/status_log.txt"):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{user_id}: {status}\n")
    return "Message saved locally (peer-to-peer not yet implemented)."
