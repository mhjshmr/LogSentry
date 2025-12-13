import re

def parse_auth_log(log_file):
    events = []

    with open(log_file, "r") as f:
        for line in f:
            # Failed login
            failed_match = re.search(
                r"Failed password.*from (\d+\.\d+\.\d+\.\d+)", line
            )
            if failed_match:
                events.append({
                    "ip": failed_match.group(1),
                    "status": "failed",
                    "raw": line.strip()
                })
                continue

            # Successful login
            success_match = re.search(
                r"Accepted password.*from (\d+\.\d+\.\d+\.\d+)", line
            )
            if success_match:
                events.append({
                    "ip": success_match.group(1),
                    "status": "success",
                    "raw": line.strip()
                })

    return events
