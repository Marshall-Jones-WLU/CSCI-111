from breezypythongui import EasyFrame
from tkinter import PhotoImage
import random

class xxxx(EasyFrame):

    def __init__(self):
        EasyFrame.__init__(self, title = "window")
        self.firstLab = self.addLabel("Width", 0, 0)
        self.secondLab = self.addLabel("Height", 1, 0)
        self.ansLab = self.addLabel("Answer", 2, 0)
        self.widField = self.addIntegerField(value = 0, row = 0, column = 1)
        self.heightField = self.addIntegerField(value = 0, row = 1, column = 1)
        self.ansField = self.addIntegerField(value = 0, row = 2, column = 1)
        self.b = self.addButton("Calculate!", row = 3, column=0,
                                command = self.calc)

    def calc(self):
        x = self.widField.getNumber()
        y = self.heightField.getNumber()
        self.ansField.setNumber(x*y)
        
if __name__ == "__main__":
    xxxx().mainloop()
