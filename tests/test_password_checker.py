from modules.password_checker.password_checker import check_password_strength

score, strength, feedback = check_password_strength("Password123!")

assert score >= 5
assert strength in ["Medium", "Strong"]

print("Password checker test passed")