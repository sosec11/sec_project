def detect_suspicious_lines(logs):
    suspicious_keywords = ["failed", "error", "unauthorized"]
    suspicious_count = 0

    for line in logs:
        for keyword in suspicious_keywords:
            if keyword.lower() in line.lower():
                suspicious_count += 1
                print("[!] Suspicious activity found:")
                print(line)
                break

    print(f"\nAnalysis completed.")
    print(f"Suspicious events detected: {suspicious_count}")