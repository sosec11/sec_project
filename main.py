from modules.log_analyzer.parser import read_logs
from modules.log_analyzer.detector import detect_suspicious_lines

from modules.password_checker.password_checker import check_password_strength


print("=== Security Analyzer Toolkit ===")
print("1. Log Analyzer")
print("2. Password Checker")

choice = input("Choose an option: ")


if choice == "1":
    
    path = input("Enter log file path: ")

    logs = read_logs(path)

    detect_suspicious_lines(logs)


elif choice == "2":

    password = input("Enter a password: ")

    score, feedback = check_password_strength(password)

    print(f"\nPassword score: {score}/6")

    if feedback:
        print("\nRecommendations:")

        for advice in feedback:
            print("-", advice)

else:
    print("Invalid option.")