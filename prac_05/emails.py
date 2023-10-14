"""Email to name program"""


def main():
    """Create and display dictionary of emails and names"""
    email_to_name = {}
    email = input("Email: ").lower()
    while email != "":
        name = get_email_name(email)
        check = input(f"Is your name {name}? (Y/n) ").upper()
        if check != "Y" and check != "":
            name = input("Name: ")
        email_to_name[email] = name
        email = input("Email: ").lower()

    for email, name in email_to_name.items():
        print(f"{name} ({email})")


def get_email_name(email):
    """Extract name from email address"""
    name_part = email.split("@")[0]
    name = " ".join(name_part.title().split("."))
    return name


main()

