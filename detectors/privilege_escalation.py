def detect_privilege_escalation(log_file):
    suspicious_commands = [
        "/bin/bash",
        "/bin/sh",
        "/etc/passwd",
        "/etc/shadow",
        "useradd",
        "usermod",
        "chmod",
        "chown"
    ]

    events = []

    with open(log_file, "r") as f:
        for line in f:
            if "sudo:" in line:
                for cmd in suspicious_commands:
                    if cmd in line:
                        events.append(line.strip())
                        break

    return events
