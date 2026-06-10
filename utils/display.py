def print_banner():

    print("=== Security Analyzer Toolkit ===")

def print_menu():

    print("1. Log Analyzer")
    print("2. Password Checker")
    print("3. Hash Generator")
    print("4. IOC Extractor")

def print_warning(message):

    print(f"\033[91m{message}\033[0m")


def print_success(message):

    print(f"\033[92m{message}\033[0m")