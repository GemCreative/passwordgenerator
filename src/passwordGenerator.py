import random
import string

# ========================
# da password generator!!!
# ========================

def generate_password(length):
    if length < 5:
        raise ValueError("Length must be at least 5 to meet all requirements.")

    upper = random.choice(string.ascii_uppercase)
    lowers = [random.choice(string.ascii_lowercase) for _ in range(2)]
    digit = random.choice(string.digits)
    symbol = random.choice("!@#$%^&*")

    remaining_length = length - 5
    all_chars = string.ascii_letters + string.digits + "!@#$%^&*"
    remaining = [random.choice(all_chars) for _ in range(remaining_length)]

    password_chars = [upper] + lowers + [digit, symbol] + remaining
    random.shuffle(password_chars)

    return "".join(password_chars)

print("===================================")
print("Welcome to Gem's Password Generator!")
print("===================================")

while True:
    length = int(input("Enter the desired password length: "))
    try:
        password = generate_password(length)
        print("Your new password is:", password)
    except ValueError as e:
        print(e)

    roe = input("Enter r to make a new password or e to exit: ").lower()
    if roe == "e":
        break

