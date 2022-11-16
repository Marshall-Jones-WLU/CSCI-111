from breezypythongui import EasyFrame
from tkinter import PhotoImage
import random

class HelloWindow(EasyFrame):
    def __init__(self):
        EasyFrame.__init__(self, title = "window")
        self.b = self.addButton("Mouse 2!", row = 1, column=1,
                                command = self.calc)
        self.a = self.addButton("Mouse 1!", row = 1, column=0,
                                command = self.calc1)

        self.pic = PhotoImage(file = "mouse.gif")

        self.img = self.addLabel("", 0, 0)
        self.img['image'] = self.pic

    ###Code?
    def calc(self):
        self.pic = PhotoImage(file = "mouse2.gif")
        self.img['image'] = self.pic

    def calc1(self):
        self.pic = PhotoImage(file = "mouse.gif")
        self.img['image'] = self.pic
        
        
if __name__ == "__main__":
    HelloWindow().mainloop()
