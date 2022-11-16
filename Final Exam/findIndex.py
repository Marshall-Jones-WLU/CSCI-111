"""
Author: Marshall Jones
CSCI 111 Final Exam
Filename: findIndex.py

This program cretes a list of 200 random integers between 0 and 200, then
it displays the index and value of the minimum value for every 10 integers
in the list.
"""
import random

def createList(size):
    '''Creates a list of 200 random integers between 0 and 200'''
    L = []
    for i in range(size):
        L.append(random.randint(0,size))

    return L

def minIndex(L, startInd, endInd):
    '''Computes the index of the minimum value of every 10 elements
    in the list created by createList(). It then prints said index and
    its corresponding value.'''
    count = 0
    blockSize = endInd - startInd
    rows = int(len(L)/(blockSize))
    
    for i in range(rows):
        Lfragment = L[startInd:endInd]
        minValPos = Lfragment.index(min(Lfragment))
        pos = minValPos + (count*10)

        #print("\nRange: " + str(startInd) + ":" + str(endInd))
        #print(Lfragment)

        if pos < 10:
            print("Index:  ",str(pos) + ",   Corresponding Integer:",str(L[pos]))
        elif pos < 100:
            print("Index: ",str(pos) + ",   Corresponding Integer:",str(L[pos]))
        else:
            print("Index:",str(pos) + ",   Corresponding Integer:",str(L[pos]))
        
        startInd += 10
        endInd = startInd + 10
        count += 1

def main():
    '''Entry point for the program'''
    L = createList(200)
    minIndex(L, 0, 10)

if __name__ == "__main__":
    main()
