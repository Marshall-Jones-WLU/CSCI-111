"""
Author: Marshall Jones, Johnny Lavette, and Eric Dyer
Project 7
Filename: flowers.py

This program defines some functions to draw geometric
shapes in turtle graphics.
The main function creates a flower comprised of multiple polygons
pivoted around a point.
"""

import random
from turtle import Turtle

def drawSquare(t, length):
    """Draws a square with length."""
    for count in range(4):
        t.forward(length)
        t.left(90)

def drawPentagon(t, length):
    """Draws a pentagon with length."""
    for count in range(5):
        t.forward(length)
        t.left(72)

def drawPolygon(t, length, sides):
    """Draws a polygon with a given length and number of sides"""
    for count in range(sides):
        t.forward(length)
        t.left(360/sides)

def drawFlower(t, length, sides, n = 6):
    """Draws a flower with length."""
    for count in range(n):
        drawPolygon(t, length, sides)
        t.left(360/n)

def main():
    """This is run only when F5 is pressed from IDLE or when
    this file is run as a script in a terminal window."""
    
    length = int(input("Length of polygon side? "))
    sides = int(input("Number of sides on polygon? "))
    n = int(input("Number of polygons in flower? "))
    
    t = Turtle()
    t.hideturtle()
    t.speed(0)
    t.pencolor("blue")

    drawFlower(t, length, sides, n)
    
##    drawSquare(t, 50)
##    drawPentagon(t, 50)
##    for sides in range(3, 7):     # Draw triangle, square, pentagon, hexagon
##        drawPolygon(t, 50, sides)
##    drawPolygon(t, 50, 8)                 # Draw octagon
##    drawFlower(t, 50)                   # Flower with 4 squares
##    drawFlower(t, 50, 10)               # Flower with 10 squares
##    drawFlower(t, 50, 6, drawPentagon)  # Draw Flower with 6 pentagons
    input("Stall until user hits a button...")
    
if __name__ == "__main__":
    main()
