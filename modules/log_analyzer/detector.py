from .patterns import SUSPICIOUS_KEYWORDS
from utils.display import print_warning

def detect_suspicious_lines(logs):
    suspicious_count = 0

    for line in logs:
        for keyword, severity in SUSPICIOUS_KEYWORDS.items():
            if keyword.lower() in line.lower():

                suspicious_count += 1

                print_warning("[!] Suspicious activity found:")
                print(f"SEVERITY: {severity}")
                print(line)

                break