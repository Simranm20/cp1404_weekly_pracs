"""
CP1404/CP5632 Practical 4
Quick pick program
"""

import random

ARG = [1, 45, 6]

userinput = int(input("How many quick picks? "))
if userinput < 0:
    print("Enter Number Greater than 0")
    userinput = int(input("How many quick picks? "))
else:
    for i in range(userinput):
        quickpick = []
        for j in range(ARG[2]):
            number = random.randint(ARG[0], ARG[1])
            while number in quickpick:
                number = random.randint(ARG[0], ARG[1])
            quickpick.append(number)
        quickpick.sort()

        print(" ".join(f"{number:3}" for number in quickpick))
