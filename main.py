from modules.log_analyzer.parser import read_logs
from modules.log_analyzer.detector import detect_suspicious_lines
from modules.password_checker.password_checker import check_password_strength
from modules.hash_generator.hash_generator import generate_hashes
from utils.display import print_banner, print_menu

print_banner()
print_menu()

choice = input("Choose an option: ")


if choice == "1":

    path = input("Enter log file path: ")

    logs = read_logs(path)

    detect_suspicious_lines(logs)


elif choice == "2":

    password = input("Enter a password: ")

    score, strength, feedback = check_password_strength(password)

    print(f"\nPassword score: {score}/6")
    print(f"Strength: {strength}")

    if feedback:
        print("\nRecommendations:")

        for advice in feedback:
            print("-", advice)

else:
    print("Invalid option.")