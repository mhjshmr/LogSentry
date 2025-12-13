from collections import Counter

def detect_bruteforce(events, threshold=5):
    ip_counter = Counter()

    for event in events:
        if event.get("status") == "failed":
            ip_counter[event.get("ip")] += 1

    brute_ips = [ip for ip, count in ip_counter.items() if count >= threshold]

    # Low-and-slow detection (important!)
    slow_attack_ips = [ip for ip, count in ip_counter.items() if 2 <= count < threshold]

    return {
        "high": brute_ips,
        "low": slow_attack_ips
    }
