"""
Authors: Marshall Jones & Nathan Cox
File name: queens.py
Description:
This program displays a solution to the 8 Queens puzzle. Each row has a queen, and
none of the queens are in a location where they can damage each other in accordance
to chess rules. There are 4 functions in this program. The drawBoard function draws
the chess board and the queens in each row. The nextCombination function finds each
next possible configuration. The checkBoard function works with the nextCombination
function by returning whether or not the queen's position from the nextCombination
function works according to chess rules. The main function provides the first guess
from where the nextCombination function finds the next possible answer that works.

**Edit: This program now takes a number greater than or equal to 4 from the user.
The program then creates a chess board n X n cells large. It takes a long time to run
if the input number is greater than 8.
"""
def drawBoard(config, n): #This function draws the board that corresponds to config

    vertLine = "|"
    blank = ("|" + "   ")
    q = ("|" + " Q ")
    dashedLine = ("-" * 4)

    for i in range(n+1):
        print(dashedLine * n)
        if i == (n):
            break
        a = config[i]
        b = (n-1) - a
        row = ((blank) * a) + (q) + ((blank) * b) + vertLine
        print(row)
    print(config)

def nextCombination(config, n): #This function returns the next configuration after the current config

    for i in range(1,(n+1)):
        answer = config
        if answer[-i] == (n-1):
            answer[-i] = 0
        elif answer[-i] < (n-1):
            answer[-i] += 1
            break
    return answer
    
def checkBoard(config): #This function returns whether this board is a solution

    n = 0
    for i in range(len(config)):
        for j in range(len(config)):
            if i != j:
                if config[i] == config[j]:
                    return False

    for i in range(len(config)): #this block prevents
        for j in range(len(config)):
            if i != j:
               difference = abs(j-i)
               config_dif = abs(config[j] - config [i])
               if difference == config_dif:
                   return False
                
    return True


def main(): #This is the main function
    n = int(input("Enter a number greater than or equal to 4: "))
    if n > 7:
        print("Please be patient. Your answer is loading...")

    guess = [0,0,0,0]
    for i in range(n-4):
        guess.append(0)

    while checkBoard(guess) == False:
        nextCombination(guess, n)
    drawBoard(guess, n)    


if __name__ == "__main__":
    main()
