def check_password_strength(password):
    score = 0
    feedback = []

    common_passwords = ["password", "123456", "azerty", "qwerty", "admin", "letmein"]

    if password.lower() in common_passwords:
        feedback.append("Ce mot de passe est trop commun")
    else:
        score += 1