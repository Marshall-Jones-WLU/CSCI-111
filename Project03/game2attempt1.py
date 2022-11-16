"""
Author: Ken Lambert
Editor: Marshall Jones
Project 3
File: game.py

This program plays a guessing game with the user.  The program
displays a greeting and asks the user to think of a number between 1 and 100.
The user inputs guesses until a guess equals the number. If user's
guess is too large or too small, the computer replies with a hint
to that effect.  When the user guesses the number in less than 7
attempts, the program displays the total number of guesses. However,
if the user exceeds 7 attempts, they lose the game and the program ends.
"""

import random
myNumber = 50
count = 0

print("Welcome to the guessing game!")
print("Rules:")
print("Please pick a number between 1 and 100.")
print("When I guess, please respond with 'bigger' or 'smaller.'")
print("If I guess it right, please enter 'correct' or 'yes'")
print("If it takes me over 7 tries, you win!")
a = input("Enter 'go' when you've got your number: ")

while True:
    if a == "go" or "Go" or "GO":
        userAnswer = input(print("Is your number",myNumber,"?")) #first guess
    else:
        print("Enter 'go' to begin this program")

    if userAnswer == "bigger":
        myNumber = int(myNumber + myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #second guess possibility1
    elif userAnswer == "smaller":
        myNumber = int(myNumber - myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #second guess possibility2

    if userAnswer == "bigger":
        myNumber = int(myNumber + myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #third guess possibility1
    elif userAnswer == "smaller":
        myNumber = int(myNumber - myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #third guess possibility2

    if userAnswer == "bigger":
        myNumber = int(myNumber + myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #fourth guess possibility1
    elif userAnswer == "smaller":
        myNumber = int(myNumber - myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #fourth guess possibility2

    if userAnswer == "bigger":
        myNumber = int(myNumber + myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #fifth guess possibility1
    elif userAnswer == "smaller":
        myNumber = int(myNumber - myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #fifth guess possibility2

    if userAnswer == "bigger":
        myNumber = int(myNumber + myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #sixth guess possibility1
    elif userAnswer == "smaller":
        myNumber = int(myNumber - myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #sixth guess possibility2

    if userAnswer == "bigger":
        myNumber = int(myNumber + myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #seventh guess possibility1
    elif userAnswer == "smaller":
        myNumber = int(myNumber - myNumber//2)
        userAnswer = input(print("Is your number",myNumber,"?")) #seventh guess possibility2

    if userAnswer == 'no':
        userAnswer = input(print("Is my number 'bigger' or 'smaller' than yours? "))
    elif userAnswer == 'yes' or 'correct':
        print("Woohoo! I win!")
        break
    elif userAnswer != "bigger" or "smaller":
        userAnswer = input(print("Please enter a proper response. I only understand 'bigger' or 'smaller.'"))
    else:
        print("Good game! I lose. :(")


#myNumber = random.randint(1, 100)
#count = 0
#while True:
#    count += 1
#    userNumber = int(input("Enter your guess: "))
#    if count > 7:
#        print("You lose! You've exceeded 7 attempts!")
#        break
    
#    if userNumber < myNumber:
#        print("Too small!")
#    elif userNumber > myNumber:
#        print("Too large!")
#    else:
#        print("You've got it in", count, "tries!")
#        break
