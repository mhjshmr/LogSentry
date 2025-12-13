def calculate_risk(bruteforce, suspicious_ips, privilege_events):
    score = 0

    high_bf_count = len(bruteforce.get("high", []))
    low_bf_count = len(bruteforce.get("low", []))

    # Calculate base score
    score += high_bf_count * 50
    score += low_bf_count * 15
    score += len(suspicious_ips) * 20
    score += len(privilege_events) * 50

    # SOC improvement: multiple low-and-slow IPs → escalate risk
    if low_bf_count >= 2 and score < 40:
        risk_level = "MEDIUM"
    elif score >= 100:
        risk_level = "HIGH"
    elif score >= 40:
        risk_level = "MEDIUM"
    else:
        risk_level = "LOW"

    return score, risk_level
