"""
Author: Ken Lambert
Editor: Marshall Jones
Project 3
File: game.py

This program plays a guessing game with the user.  The program
displays a greeting and thinks of a number between 1 and 100.
The user inputs guesses until a guess equals the number. If user's
guess is too large or too small, the computer replies with a hint
to that effect.  When the user guesses the number in less than 7
attempts, the program displays the total number of guesses. However,
if the user exceeds 7 attempts, they lose the game and the program ends.
"""

import random

myNumber = random.randint(1, 100)
count = 0
while True:
    count += 1
    userNumber = int(input("Enter your guess: "))
    if count > 7:
        print("You lose! You've exceeded 7 attempts!")
        break
    
    if userNumber < myNumber:
        print("Too small!")
    elif userNumber > myNumber:
        print("Too large!")
    else:
        print("You've got it in", count, "tries!")
        break
