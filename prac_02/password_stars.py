MINIMUM_LENGTH = 5
password = input(f"Enter a password with at least {MINIMUM_LENGTH} characters: ")
while len(password) < MINIMUM_LENGTH:
    print("password invalid")
    password = input(f"Enter a password with at least {MINIMUM_LENGTH} characters: ")
print("*" * len(password))
