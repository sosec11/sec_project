def print_banner():

    print("=== Security Analyzer Toolkit ===")

def print_menu():

    print("1. Log Analyzer")
    print("2. Password Checker")
    print("3. Hash Generator")
    print("4. IOC Extractor")
    print("5. IOC File Analyzer")

    def print_iocs(ips, emails, urls):

        if not ips and not emails and not urls:
            print("\nNo IOCs found.")
        return

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

def print_warning(message):

    print(f"\033[91m{message}\033[0m")


def print_success(message):

    print(f"\033[92m{message}\033[0m")