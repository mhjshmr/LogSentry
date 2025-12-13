import argparse
import os

from parsers.auth_parser import parse_auth_log
from detectors.bruteforce import detect_bruteforce
from detectors.suspicious_ip import detect_suspicious_ips
from detectors.privilege_escalation import detect_privilege_escalation
from utils.risk_score import calculate_risk
from utils.report import generate_report


def main():
    # -----------------------------
    # CLI Argument for log file
    # -----------------------------
    parser = argparse.ArgumentParser(
        description="LogSentry – Security Log Analysis & Alerting Tool"
    )
    parser.add_argument(
        "--log",
        required=True,
        help="Full path to the log file to analyze"
    )

    args = parser.parse_args()
    LOG_FILE = args.log

    # Check if file exists
    if not os.path.exists(LOG_FILE):
        print("[!] Log file not found. Please check the path.")
        return

    print(f"[*] Parsing log file: {LOG_FILE}")

    # -----------------------------
    # Parse logs & run detectors
    # -----------------------------
    events = parse_auth_log(LOG_FILE)
    bruteforce = detect_bruteforce(events)
    suspicious_ips = detect_suspicious_ips(events)
    privilege_events = detect_privilege_escalation(LOG_FILE)

    # -----------------------------
    # Calculate risk score & generate report
    # -----------------------------
    risk_score, risk_level = calculate_risk(
        bruteforce,
        suspicious_ips,
        privilege_events
    )

    report = generate_report(
        bruteforce,
        suspicious_ips,
        privilege_events,
        risk_score,
        risk_level
    )

    # Print report to console
    print("\n" + report)

    # -----------------------------
    # Save report interactively
    # -----------------------------
    os.makedirs("reports", exist_ok=True)

    save_choice = input("\nDo you want to save the report? (y/n): ").strip().lower()

    if save_choice == "y":
        default_file = "incident_report.txt"
        file_name = input(f"Enter report file name (default: {default_file}): ").strip()

        if not file_name:
            file_name = default_file

        if not file_name.endswith(".txt"):
            file_name += ".txt"

        file_path = os.path.join("reports", file_name)

        # Use UTF-8 to handle Unicode characters like ⚠
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(report)

        print(f"\n[+] Report saved to {file_path}")

    else:
        print("\n[!] Report not saved")


if __name__ == "__main__":
    main()
