# LogSentry – Security Log Analysis & Alerting Tool

LogSentry is a Python-based SOC/Blue Team tool designed to analyze authentication logs and detect suspicious activity.
<p>
It parses logs, detects brute-force attacks, suspicious IPs, and privilege escalation events, calculates a risk score, and generates a professional incident report for actionable response.</p>

<br>

<div align="center">
  <img src="https://github.com/mhjshmr/LogSentry/blob/main/logs/LogSentry%20Generated%20Report.png" alt="Generated Log Analysis Report" width="500">
</div>


## Overview

LogSentry helps security students, system administrators, and SOC analysts understand real-world attacks by analyzing multiple indicators in authentication logs.
<p>The tool focuses on clarity and explainability, making it suitable for academic use, SOC training, and cybersecurity learning.</p>

## Features

### Log Parsing & Event Extraction
- Supports Linux `auth.log` and similarly structured logs.
- Extracts events relevant to:
     - Brute-force login attempts
     - Low-and-slow distributed attacks
     - Suspicious IP activity
     - Privilege escalation

### Brute-Force Detection
- High-volume login attempts → HIGH severity.
- Low-and-slow attempts → LOW severity.
- SOC enhancement: 2+ low-and-slow IPs automatically escalate to MEDIUM risk, detecting distributed credential stuffing.
  
### Suspicious IP Detection
- Detects unusual login patterns and repeated attempts.
- Flags potential reconnaissance or compromise attempts.

### Privilege Escalation Detection
- Detects commands executed with elevated privileges (e.g., `sudo`) that could indicate system compromise.

### Risk Scoring System

- Weighted scoring:
     - High brute-force: 50 points/IP
     - Low-and-slow brute-force: 15 points/IP
     - Suspicious IP: 20 points/IP
     - Privilege escalation: 50 points/event
- Automatically assigns risk level (LOW, MEDIUM, HIGH) based on SOC-style rules.

### Reporting

- Generates detailed, human-readable incident reports.
- Includes:
     - Threat summary
     - Detailed event listing
     - Recommendations for mitigation
- Highlights multiple low-and-slow IPs for distributed attacks.
- Supports saving reports with a custom filename.

## Getting Started

### Prerequisites

- Python 3.x

### Installation

Clone the repository:
```bash
git clone https://github.com/mhjshmr/LogSentry.git
cd LogSentry
```

### Usage
Run the tool on a log file:
```bash
python app.py --log logs/auth_sample.log
```
Follow prompts to optionally save the report.

## How It Works

Analysis Flow
1. Parse authentication logs
2. Detect brute-force login attempts
3. Identify suspicious IP activity
4. Detect privilege escalation events
5. Calculate risk score & risk level
6. Generate structured SOC-style report

## Best Practices

- Monitor risk scores continuously for high-volume attacks.
- Investigate multiple low-and-slow IPs for distributed attacks.
- Review privilege escalation events carefully.
- Use reports as a starting point for incident response, not as final verdicts.
  
## Security Considerations

- This tool uses heuristic analysis, not machine learning.
- Risk scores are indicative, not definitive.
- Designed for educational and SOC training purposes.
- Real-world deployment should integrate live monitoring and alerting.

## Technical Details

- Language: Python 3.x
- Libraries Used: `argparse`, `re`, `datetime`, `os` (standard library)
- Modular architecture:
     - `parsers/` → log parsing
     - `detectors/` → brute-force, suspicious IP, privilege escalation detection
     - `utils/` → risk scoring, report generation
- Pure Python implementation, easily extensible. 

## Core Functions

- `parse_auth_log()` – Parses Linux-style authentication logs
- `detect_bruteforce()` – Detects high-volume and low-and-slow brute-force attempts
- `detect_suspicious_ips()` – Flags suspicious IP activity
- `detect_privilege_escalation()` – Detects elevated commands
- `calculate_risk()` – Computes weighted risk score & assigns risk level
- `generate_report()` – Creates structured, SOC-ready incident report

## Use Case

- Academic cybersecurity projects
- SOC analyst training
- Security monitoring simulations
- Blue Team awareness exercises

## References

- Linux Authentication Logs (`auth.log`) documentation
- SOC & Blue Team best practices
<br><br>

**Stay alert. Detect early. Respond fast. 🔐**
