"""
Authors: Marshall Jones, Johnny Lavette, and Eric Dyer
Project 9
File: helloworld.py

This program prints "Hello world!" in a GUI with
red, size 24, courier font text.
"""

from breezypythongui import EasyFrame
from tkinter.font import Font

class HelloWorld(EasyFrame):
    """Displays a greeting in a window."""

    def __init__(self):
        """Sets up the window and the label."""
        EasyFrame.__init__(self)
        self.setResizable(True)
        textLabel = self.addLabel(text = "Hello world!",
                                  row = 0, column = 0,)

        # Set the font and color of the text
        font = Font(family = "courier", size = 24)
        textLabel["font"] = font
        textLabel["foreground"] = "red"

def main():
    """The starting point for launching the program."""
    HelloWorld().mainloop()


# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
