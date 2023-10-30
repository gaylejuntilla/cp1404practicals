import random

AMOUNT_OF_NUMBERS = 6
MINIMUM_NUMBER = 1
MAXIMUM_NUMBER = 45

number_of_quick_picks = int(input("How many quick picks? "))
for i in range(number_of_quick_picks):
    random_numbers = []
    for j in range(AMOUNT_OF_NUMBERS):
        number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        while number in random_numbers:
            number = random.randint(MINIMUM_NUMBER, MAXIMUM_NUMBER)
        random_numbers.append(number)
    random_numbers.sort()
    print(" ".join([f"{number:3}" for number in random_numbers]))
