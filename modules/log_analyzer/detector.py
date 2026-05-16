from .patterns import SUSPICIOUS_KEYWORDS

def detect_suspicious_lines(logs):
    suspicious_count = 0

    for line in logs:
        for keyword, severity in SUSPICIOUS_KEYWORDS.items():
            if keyword.lower() in line.lower():
                suspicious_count += 1
                print("[!] Suspicious activity found:")
                print("SEVERITY: {severity}")
                print(line)
                break

    print(f"\nAnalysis completed.")
    print(f"Suspicious events detected: {suspicious_count}")