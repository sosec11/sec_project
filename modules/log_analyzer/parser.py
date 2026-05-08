def analyze_logs(file_path):
    suspicious_keywords = ["failed", "error", "unauthorized"]

    try:
        with open(file_path, "r") as file:
            logs = file.readlines()

        for line in logs:
            for keyword in suspicious_keywords:
                if keyword.lower() in line.lower():
                    print("[!] Suspicious activity found:")
                    print(line)

    except FileNotFoundError:
        print("File not found.")