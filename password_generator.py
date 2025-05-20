import secrets
import string

def generate_password():
    lowercase_letters = string.ascii_lowercase
    uppercase_letters = string.ascii_uppercase
    digits = string.digits
    # Using string.punctuation for special characters, but this can be customized.
    # Consider if all of these are desirable, or if some might cause issues in certain systems.
    special_characters = r"!@#$%^&*()-_=+[]{}|;:'\",.<>/?~"

    # Determine password length
    password_length = secrets.choice(range(18, 23)) # 18 to 22 characters

    # Ensure at least one character from each set
    guaranteed_chars = [
        secrets.choice(lowercase_letters),
        secrets.choice(uppercase_letters),
        secrets.choice(digits),
        secrets.choice(special_characters)
    ]

    # Combine all character sets for the remaining characters
    all_chars = lowercase_letters + uppercase_letters + digits + special_characters

    # Fill the rest of the password
    remaining_length = password_length - len(guaranteed_chars)
    password_chars = guaranteed_chars + [secrets.choice(all_chars) for _ in range(remaining_length)]

    # Shuffle the password characters to ensure randomness
    secrets.SystemRandom().shuffle(password_chars) # Use SystemRandom for shuffle as well for consistency

    return "".join(password_chars)

if __name__ == '__main__':
    # Example usage:
    password = generate_password()
    print(f"Generated password: {password}")
    print(f"Password length: {len(password)}")
    # Verification (optional, for testing during development)
    print(f"Contains lowercase: {any(c in string.ascii_lowercase for c in password)}")
    print(f"Contains uppercase: {any(c in string.ascii_uppercase for c in password)}")
    print(f"Contains digit: {any(c in string.digits for c in password)}")
    # Adjust the special character set here if it was changed above
    print(f"Contains special: {any(c in r'!@#$%^&*()-_=+[]{}|;:'\",.<>/?~' for c in password)}")
