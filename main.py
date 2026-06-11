from modules.log_analyzer.parser import read_logs
from modules.log_analyzer.detector import detect_suspicious_lines
from modules.password_checker.password_checker import check_password_strength
from modules.hash_generator.hash_generator import generate_hashes
from modules.ioc_extractor.ioc_extractor import extract_iocs
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
        
elif choice == "3":
    text = input("Enter text to hash: ")
        
    md5hash, sha256_hash = generate_hashes(text)

    print(f"\nMD5:{md5hash}")
    print(f"SHA256: {sha256_hash}")

elif choice == "4":

    text = input("Enter text to analyze: ")

    ips, emails, urls = extract_iocs(text)

    if not ips and not emails and not urls:

        print("\nNo IOCs found.")
else:

    print("\nIOCs found:")

    print("\nIP addresses:")
    for ip in ips:
        print("-", ip)

    print("\nEmails:")
    for email in emails:
        print("-", email)

    print("\nURLs:")
    for url in urls:
        print("-", url)

    else:
        print("Invalid option.")