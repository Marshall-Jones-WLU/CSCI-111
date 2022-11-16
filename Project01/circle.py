"""
Author: Ken Lambert
Project 1
File name: circle.py

This program prompts the user for the radius of a circle and
computes and prints the circle's area.

"""

import math

radius = float(input("Enter the radius of a circle: "))
area = math.pi * radius ** 2
print("The area of the circle is", area)
