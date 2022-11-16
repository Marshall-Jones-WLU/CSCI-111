"""
Author: Dr. Lu
File name: project4Warmup.py
"""

import random
print(random.randint(0,100))
print(random.randint(0,100))
print("ken. This is assignment 4".endswith("4"))
inputFile = open("RoTS.txt", "r")
for line in inputFile:
    print(line)
    print(len(line))
    print(line.split())
outputFile = open("numbers.txt", "w")
for number in range(1, 101):
    outputFile.write(str(number) + "/n")
outputFile.close()
