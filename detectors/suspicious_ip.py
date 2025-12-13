from collections import Counter

def detect_suspicious_ips(events, threshold=3):
    """
    Flags IPs with repeated failed login attempts
    """
    ip_counter = Counter()

    for event in events:
        if event["status"] == "failed":
            ip_counter[event["ip"]] += 1

    suspicious_ips = [
        ip for ip, count in ip_counter.items()
        if count >= threshold
    ]

    return suspicious_ips
