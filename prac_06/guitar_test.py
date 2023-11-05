from guitar import Guitar


def main():
    """Test last two methods of Guitar class"""
    guitar = Guitar("Gibson L-5 CES", 1922, 16035.40)
    other_guitar = Guitar("Another Guitar", 2013, 12456.30)
    print(f"{guitar.name} get_age() - Expected 101. Got {guitar.get_age()}")
    print(f"{other_guitar.name} get_age() - Expected 10. Got {other_guitar.get_age()}")
    print(f"{guitar.name} is_vintage() - Expected True. Got {guitar.is_vintage()}")
    print(f"{other_guitar.name} is_vintage() - Expected False. Got {other_guitar.is_vintage()}")


main()
