"""
Author: Marshall Jones
File name: random_writer.py
Description:
This program outputs random integers to a text file. It prompts the
user for a file name, the largest number that should be generated,
and the number of integers to generate.
"""

name = input("What is the name of the file that you'd like to edit? ")
upper = int(input("What is the largest possible number that you would like to generate? "))
n = int(input("How many integers do you want to generate? "))

import random

f = open(name + ".txt", 'w')
for count in range(n):
    number = random.randint(1, upper)
    f.write(str(number) + " ")
    if count == n:
        break
f.close()
