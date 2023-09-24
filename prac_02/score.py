"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    """Get users score and print status"""
    score = float(input("Enter score: "))
    print(determine_grade_status(score))
    print(determine_grade_status(random.randint(0, 100)))


def determine_grade_status(score):
    """determine score status"""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


main()

