"""
Author: Marshall Jones, Johnny Lavette, and Eric Dyer
Project 7
Filename: mondrian.py

This program displays a Mondrian-like painting with 
the user's input level.  The program obtains the level 
from a command-line argument.  Thus,

python3 mondrian.py 6

draws a painting at level 6.
"""

import random
import sys
from turtle import Turtle

def drawRectangle(t, x1, y1, x2, y2):
    """Draws a rectangle with the given corner points
    in a random color."""
    red = random.randint(0, 255)
    green = random.randint(0, 255)
    blue = random.randint(0, 255)
    t.pencolor(red, green, blue)
    t.fillcolor(red, green, blue)
    t.begin_fill()
    t.up()
    t.goto(x1, y1)
    t.down()
    t.goto(x2, y1)
    t.goto(x2, y2)
    t.goto(x1, y2)
    t.goto(x1, y1)
    t.end_fill()


def mondrian(t, x1, y1, x2, y2, level):
    """Draws a Mondrian painting at the given level."""
    if level > 0:
        drawRectangle(t, x1, y1, x2, y2)

        vertical = random.randint(1, 2)
   
        if vertical == 1:   # Vertical split
            sub = random.randint(1, 2)
            if sub == 1:
                mondrian(t, x1, y1, (x2 - x1) / 3 + x1, y2,
                         level - 1)
                mondrian(t, (x2 - x1) / 3 + x1, y1, x2, y2, 
                         level - 1)
            else:
                mondrian(t, x1, y1, 2*(x2 - x1) / 3 + x1, y2,
                         level - 1)
                mondrian(t, 2*(x2 - x1) / 3 + x1, y1, x2, y2, 
                         level - 1)

        else:               # Horizontal split
            sub = random.randint(1,2)
            if sub == 1:
                mondrian(t, x1, y1, x2, (y2 - y1) / 3 + y1, 
                         level - 1)
                mondrian(t, x1, (y2 - y1) / 3 + y1, x2, y2, 
                         level - 1)
            else:
                mondrian(t, x1, y1, x2, 2*(y2 - y1) / 3 + y1, 
                         level - 1)
                mondrian(t, x1, 2*(y2 - y1) / 3 + y1, x2, y2, 
                         level - 1)

def main():
    level = 3
    
    t = Turtle()
    t.screen.colormode(255)		#Lets us use colors from 0 to 255
    
    t.speed(0)
    t.hideturtle()
    
    x = t.screen.window_width() // 2 - 20
    y = t.screen.window_height() // 2 - 20

    if level > 6:
        t.screen.tracer(0)
        mondrian(t, -x, y, x, -y, level)
        t.screen.update()
    else:
        mondrian(t, -x, y, x, -y, level)

    #drawRectangle(t, x1, y1, x2, y2)
    
    # Stop the fly-by window in the terminal
    input("Press enter to quit: ")
    
if __name__ == "__main__":
    main()
