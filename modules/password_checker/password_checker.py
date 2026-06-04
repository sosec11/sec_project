from .patterns import COMMON_PASSWORDS, SPECIAL_CHARACTERS


def check_password_strength(password):

    score = 0
    feedback = []

    if password.lower() in COMMON_PASSWORDS:
        feedback.append("This password is too common")
    else:
        score += 1

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Password is too short (minimum 8 characters)")

    if any(char.isupper() for char in password):
        score += 1
    else:
        feedback.append("Add at least one uppercase letter")

    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Add at least one lowercase letter")

    if any(char.isdigit() for char in password):
        score += 1
    else:
        feedback.append("Add at least one digit")

    if any(char in SPECIAL_CHARACTERS for char in password):
        score += 1
    else:
        feedback.append("Add at least one special character")

    if score <= 2:
        strength = "Weak"

    elif score <= 4:
        strength = "Medium"

    else:
        strength = "Strong"

    return score, strength, feedback
    
    if score <= 2:
        strength = "Weak"
    elif score <= 4:
        strength = "Medium"
    else:
        strength = "Strong"

    return score, strength, feedback