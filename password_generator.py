import random
import string

def check_strength(password):
    length = len(password)
    has_upper = any(char.isupper() for char in password)
    has_lower = any(char.islower() for char in password)
    has_digit = any(char.isdigit() for char in password)
    has_symbol = any(char in string.punctuation for char in password)
    
    score = sum([has_upper, has_lower, has_digit, has_symbol])
    
    if length >= 12 and score == 4:
        return "Bohat Strong Password hai! 🔥"
    elif length >= 8 and score >= 3:
        return "Theek-thaak Strong Password hai. 👍"
    else:
        return "Kamzor (Weak) Password hai, mazeed secure banayein. ⚠️"

def generate_password(length=12):
    characters = string.ascii_letters + string.digits + string.punctuation
    password = ''.join(random.choice(characters) for i in range(length))
    return password

print("--- Secure Password Generator & Checker ---")
try:
    user_length = int(input("Enter password length (e.g., 10 or 12): "))
    if user_length < 6:
        print("Password length kam az kam 6 characters honi chahiye.")
    else:
        secure_password = generate_password(user_length)
        print(f"\nAapka Generated Password yeh hai: {secure_password}")
        
        # Strength check karna
        result = check_strength(secure_password)
        print(f"Password Status: {result}")
        
except ValueError:
    print("Barah-e-karam sirf numbers enter karein!")