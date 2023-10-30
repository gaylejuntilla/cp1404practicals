"""
Write a complete Python program following the standard structure that uses a main and other functions.
"""

MENU = "(G)et valid score\n(P)rint result\n(S)how stars\n(Q)uit"


def main():
    """Get score and status"""
    print(MENU)
    choice = input("choice: ").upper()
    while choice != "Q":
        if choice == "G":
            score = get_valid_score()
        elif choice == "P":
            print(determine_score_status(score))
        elif choice == "S":
            print_stars(score)
        else:
            print("Invalid option")
        print("MENU")
        choice = input("choice: ").upper()
    print("Finished")


def get_valid_score():
    """Get valid score"""
    score = int(input("Score: "))
    while score < 0 or score > 100:
        print("Invalid score")
        score = int(input("Score: "))
    return score


def determine_score_status(score):
    """Determine score status"""
    if score < 50:
        return "bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def print_stars(score):
    """Print stars the size of score"""
    print("*" * score)


main()


