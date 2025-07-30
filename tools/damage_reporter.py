def report_damage(desc, image_path=None, log_file="logs/damage_reports.txt"):
    with open(log_file, "a", encoding="utf-8") as f:
        f.write(f"{desc}\n")
    return "Damage reported locally. Field team will review."
