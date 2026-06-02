from .patterns import SUSPICIOUS_KEYWORDS
from utils.display import print_warning
from datetime import datetime

def detect_suspicious_lines(logs):
    if suspicious_count == 0:
        print("Risk level: LOW")
    elif suspicious_count <= 3:
        print("Risk level: MEDIUM")
    else:
        print("Risk level: HIGH")

        for line in logs:
            for keyword, severity in SUSPICIOUS_KEYWORDS.items():
                if keyword.lower() in line.lower():

                    suspicious_count += 1
                    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    print(f"Detection time: {current_time}")
                    print_warning("[!] Suspicious activity found:")
                    print(f"SEVERITY: {severity}")
                    print(line)

                    break