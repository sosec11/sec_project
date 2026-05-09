def detect_suspicious_lines(logs):

    suspicious_keywords = ["failed", "error", "unauthorized"]

    for line in logs:
        for keyword in suspicious_keywords:

            if keyword.lower() in line.lower():

                print("[!] Suspicious activity found:")
                print(line)