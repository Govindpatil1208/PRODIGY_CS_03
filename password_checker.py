import re

def check_password_strength(password):
    length_error = len(password) < 8
    uppercase_error = re.search(r"[A-Z]", password) is None
    lowercase_error = re.search(r"[a-z]", password) is None
    digit_error = re.search(r"[0-9]", password) is None
    special_char_error = re.search(r"[!@#$%^&*(),.?\":{}|<>]", password) is None

    errors = {
        "Minimum 8 characters": not length_error,
        "At least one uppercase letter": not uppercase_error,
        "At least one lowercase letter": not lowercase_error,
        "At least one number": not digit_error,
        "At least one special character": not special_char_error
    }

    print("\nPassword Analysis:")
    for rule, passed in errors.items():
        print(f"{'✔' if passed else '✖'} {rule}")

    score = sum(errors.values())

    if score == 5:
        print("\n✅ Password Strength: Strong")
    elif 3 <= score < 5:
        print("\n⚠️ Password Strength: Medium")
    else:
        print("\n❌ Password Strength: Weak")

# === Main Program ===
print("=== Password Strength Checker ===")
password = input("Enter your password: ")
check_password_strength(password)
