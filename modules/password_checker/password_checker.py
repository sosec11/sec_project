from .patterns import COMMON_PASSWORDS, SPECIAL_CHARACTERS

def check_password_strength(password):
    score = 0
    feedback = []

    COMMON_PASSWORDS
    if password.lower() in common_passwords:
        feedback.append("Ce mot de passe est trop commun")
    else:
        score += 1