MINIMUM_LENGTH = 5


def main():
    """check password and print asterisks"""
    password = get_password()
    print_asterisks(password)


def print_asterisks(password):
    """print asterisks"""
    print("*" * len(password))


def get_password():
    """Check password length"""
    password = input(f"Enter a password with at least {MINIMUM_LENGTH} characters: ")
    while len(password) < MINIMUM_LENGTH:
        print("password invalid")
        password = input(f"Enter a password with at least {MINIMUM_LENGTH} characters: ")
    return password


main()
