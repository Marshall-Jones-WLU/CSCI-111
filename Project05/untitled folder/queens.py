"""
Authors: Marshall Jones & Nathan Cox
File name: queens.py
This program displays a solution to the 8 Queens puzzle.
"""
def drawBoard(config): #This function draws the board that corresponds to config
    vertLine = "|"
    blank = ("|" + "   ")
    q = ("|" + " Q ")
    dashedLine = ("-"*33)

    for i in range(9):
        print(dashedLine)
        if i == 8:
            break
        a = config[i]
        b = 7 - a
        row = ((blank) * a) + (q) + ((blank) * b) + vertLine
        print(row)
    print(config)

def nextCombination(config): #This function returns the next configuration after the current config
                            #Input: config
                            #Output: the next config
    for i in range(1,9):
        answer = config
        if answer[-i] == 7:
            answer[-i] = 0
        elif answer[-i] < 7:
            answer[-i] += 1
            break

        #return answer

    #answer = [0, 0, 0, 0, 0, 0, 0, 1]
    return answer
    
def checkBoard(config): #This function returns whether this board is a solution
    '''
    If any contents in the list config are the same value, it does not work and is false.
    If any contents in the list config are + or - n values from i, it is diagonal and false.
    If anything else, it is true
    Output: True or False
    '''
    n = 0
    for i in range(len(config)):
        for j in range(len(config)):
            if i != j:
                if config[i] == config[j]:
                    return False
        '''if config[i] == config[i +- n]:
            return False
        else:
            return True'''


def main(): #This is the main function

    guess = [0,0,0,0,0,0,0,0]

    nextCombination(guess)
    checkBoard(guess)
    if False:
        main()
    elif True:
        drawBoard(guess)
    
if __name__ == "__main__":
    main()
