def _to_minutes(time_str):
    parts = time_str.split(":")
    hours = int(parts[0])
    minutes = int(parts[1])
    return hours * 60 + minutes


def write_long_session_users(filename):
    with open(filename, "r", encoding="utf-8") as input_file, open(
        "output.txt", "w", encoding="utf-8"
    ) as output_file:
        for line in input_file:
            cleaned = line.strip()
            if not cleaned:
                continue

            parts = cleaned.split(", ")
            username = parts[0]
            login_minutes = _to_minutes(parts[1])
            logout_minutes = _to_minutes(parts[2])

            if logout_minutes - login_minutes >= 60:
                output_file.write(username + "\n")