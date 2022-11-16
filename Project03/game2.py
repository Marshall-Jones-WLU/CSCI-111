"""
Author: Marshall Jones
Project 3
File: game2.py

This program plays a guessing game with the user.  The program
displays a greeting and asks the user to think of a number between 1 and 100.
The computer tries to guess the number by getting hints from the user about
whether the number is larger or smaller. When the computer guesses the number
in less than 7 attempts, it wins and displays its total number of guesses.
However, if the computer exceeds 7 attempts, the user wins and the program ends.
"""


print("Welcome to the guessing game!")
print("Rules:")
print("Please pick a number between 1 and 100.")
print("When I guess, please respond with 'bigger' or 'smaller.'")
print("If I guess it right, please enter 'correct' or 'yes'")
print("If it takes me over 7 tries, you win!")

import random
myNumber = 50
lower = 1
upper = 100
count = 0

while True:
    count += 1
    print('\n')
    print("Is",myNumber,"your number?")
    userNumber = input("Enter 'bigger', 'smaller', or 'yes': ")
    if count > 7:
        print("Good game! You beat me!")
        break

    if userNumber == "smaller":
        upper = (myNumber - 1)
        myNumber = random.randint(lower, upper)
    elif userNumber == "bigger":
        lower = (myNumber +1)
        myNumber = random.randint(lower, upper)
    elif userNumber == "correct" or userNumber == "yes":
        print("HA! I beat you in", count, "tries!")
        break
    else:
        print("I don't understand you! Please enter either 'bigger', 'smaller', or 'yes'.")
