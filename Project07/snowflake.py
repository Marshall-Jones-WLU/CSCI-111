"""
Author: Marshall Jones, Johnny Lavette, and Eric Dyer
Project 7
Filename: snowflake.py

This program draws a snowflake at level 2 and with side lengths of 200.
It also has lines in the main function that can be activated by deleting
the '#' signs. These lines allow the program to produce a snowflake with
a variable number of levels and length of sides.
"""

import random
import sys
from turtle import Turtle

def drawSide(t, length, level):
    """Draws a side of the snowflake"""
    if level==0:
        t.forward(length)
    else:
        drawSide(t, length/3, level-1)
        t.left(60)
        drawSide(t, length/3, level-1)
        t.right(120)
        drawSide(t, length/3, level-1)
        t.left(60)
        drawSide(t, length/3, level-1)

def drawSnowflake(t, length, level):
    '''
    Draws the snowflake
    
    Don't touch this function! All work is in drawSide!
    '''
    t.fillcolor('red')
    t.begin_fill()
    
    drawSide(t, length, level)
    t.right(120)
    drawSide(t, length, level)
    t.right(120)
    drawSide(t, length, level)
    
    t.end_fill()

def main():
    #level = int(input("Level? "))
    #if level > 4:
    #    print("\nWe recommend that you use a length greater than 200 \nif you want a level greater than 4.\n")
    #length = int(input("Length of sides? "))
    level = 2
    length = 200
    
    t = Turtle()
    t.screen.colormode(255)     #Lets us use colors from 0 to 255
    
    t.screen.setup(500,500)
    t.speed(0)
    t.hideturtle()
    
    x = t.screen.window_width()// 4
    y = t.screen.window_height() // 4
    
    #Move the turtle to the starting location
    t.up()
    t.goto(-x,y)
    t.down()
    
    #Draws the Snowflake
    drawSnowflake(t,length, level)
    
    # Stop the fly-by window in the terminal
    input("Hit Enter!!!!")

if __name__ == "__main__":
    main()
