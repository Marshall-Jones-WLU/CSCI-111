"""
Authors: Marshall Jones, Johnny Lavette, and Eric Dyer
Project 9
File: ninecells.py 

This programs generates a GUI with 9 cells and their positions in text format.
"""

from breezypythongui import EasyFrame

class LayoutDemo(EasyFrame):
    """Displays labels in the window's quadrants."""

    def __init__(self):
        """Sets up the window and the labels."""
        EasyFrame.__init__(self)
        for Column in range(3):
            for Row in range(3):
                self.addLabel(text = "(" + str(Row) + ", " + str(Column) + ")",
                              row = Row, column = Column, sticky = "NSEW")
        #self.addLabel(text = "(0, 0)", row = 0, column = 0)
        #self.addLabel(text = "(0, 1)", row = 0, column = 1)
        #self.addLabel(text = "(1, 0)", row = 1, column = 0)
        #self.addLabel(text = "(1, 1)", row = 1, column = 1)

def main():
    """The starting point for launching the program."""
    LayoutDemo().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
