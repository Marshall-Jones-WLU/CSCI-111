"""
Authors: Marshall Jones, Johnny Lavette, and Eric Dyer
Project 9
File: imagedemo.py

This program displays an image in a GUI with a caption about the Moon Man.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage
from tkinter.font import Font

class ImageDemo(EasyFrame):
    """Displays an image and a caption."""

    def __init__(self):
        """Sets up the window and widgets."""
        EasyFrame.__init__(self, title = "Image Demo")
        self.setResizable(False)
        imageLabel = self.addLabel(text = "",
                                   row = 0, column = 0,
                                   sticky = "NSEW")
        textLabel = self.addLabel(text = "Moon Man's silhouette stands out against the stark contrast of the beautiful Earth.",
                                  row = 1, column = 0,
                                  sticky = "NSEW")
        
        # Load the image and associate it with the image label.
        self.image = PhotoImage(file = "moon.gif")
        imageLabel["image"] = self.image

        # Set the font and color of the caption.
        font = Font(family = "Verdana", size = 12, slant = "italic")
        textLabel["font"] = font
        textLabel["foreground"] = "blue"

def main():
    """The starting point for launching the program."""
    ImageDemo().mainloop()

# Instantiates and pops up the window.
if __name__ == "__main__":
    main()
