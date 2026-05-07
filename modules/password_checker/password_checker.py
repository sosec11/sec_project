def check_password_strength(password):
    score = 0
    feedback = []

    if len(password) >= 8:
        score += 1
    else:
        feedback.append("Le mot de passe est trop court (min 8 caractères)")
    if any(char.islower() for char in password):
        score += 1
    else:
        feedback.append("Ajoute des lettres minuscules")
