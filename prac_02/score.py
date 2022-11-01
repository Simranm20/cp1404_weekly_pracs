"""
CP1404/CP5632 - Practical 2
Fixed program to determine score status, with function
"""

# TODO: Fix this!

import random


def main():
    score = float(input("Enter score: "))
    print(results(score))
    print("Random score", results(random.randint(0, 100)))


def results(score):
    if score < 0 or score > 100:
        return "Invalid score"
    elif score >= 90:
        return "Excellent"
    elif score >= 50:
        return "Passable"
    else:
        return "Bad"


main()
