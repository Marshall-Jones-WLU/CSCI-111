"""
Authors: Marshall Jones, Johnny Lavette, and Eric Dyer
Project 9
Filename: towers.py

This program displays the configurations for the Towers of Hanoi problem in a GUI.
It begins by showing the first configuration. The user can navigate through each
step with a "Next Configuration" button, a "Previous Configuration" button, or they
can "Jump" to a specified configuration.
"""

from breezypythongui import EasyFrame
from tkinter import PhotoImage

class Towers(EasyFrame):
        def __init__(self, configNumber = 0):
                """Set up the window, label, and buttons."""
                EasyFrame.__init__(self, title = "Towers of Hanoi",
                                   background = "white")
                self.setSize(1050, 400)
                
                # Instance variable to track the current picture.
                self.currentPicture = 0
                
                # configuration image
                configImage = self.addLabel(text = "",
                                            row = 0, column = 1)
                
                # input buttons
                self.previousButton = self.addButton(text = "Previous Configuration",
                                                     row = 1, column = 0,
                                                     command = self.previousConfig)
                self.nextButton = self.addButton(text = "Next Configuation",
                                                 row = 1, column = 2,
                                                 command = self.nextConfig)

                # jump button, text, and input field
                self.jumpButton = self.addButton(text = "Jump",
                                                 row = 1, column = 1,
                                                 command = self.jumpTo)
                
                self.inputField = self.addIntegerField(value = "",
                                                       row = 2, column = 1, sticky = "NS")
                
                self.image = PhotoImage(file = "./towerPics/0000.gif")
                configImage["image"] = self.image
                
        def previousConfig(self):
                """Sends user to the previous configuration of the puzzle"""

                self.currentPicture -= 1
                configNumber = int(self.currentPicture)

                if configNumber < 0:
                        self.messageBox(title = "Error",
                                        message = "No previous configuration exists.")

                configImage = self.addLabel(text = "",
                                            row = 0, column = 1)

                if configNumber < 10:
                        configuration = str(0) + str(configNumber)
                else:
                        configuration = str(configNumber)

                self.image = PhotoImage(file = "./towerPics/00" + configuration + ".gif")
                configImage["image"] = self.image

        def nextConfig(self):
                """Sends user to the next configuration of the puzzle"""
                
                self.currentPicture += 1
                configNumber = int(self.currentPicture)
                
                if configNumber > 63:
                        self.messageBox(title = "Error",
                                        message = "You have reached the final configuration.\nThere is no next configuration.")
                configImage = self.addLabel(text = "",
                                            row = 0, column = 1)

                if configNumber < 10:
                        configuration = str(0) + str(configNumber)
                else:
                        configuration = str(configNumber)

                self.image = PhotoImage(file = "./towerPics/00" + configuration + ".gif")
                configImage["image"] = self.image

        def jumpTo(self):
                """Jumps user to the specified configuration of the puzzle"""
                
                configNumber = self.inputField.getNumber()
                
                if configNumber < 0 or configNumber > 63:
                        self.messageBox(title = "Error",
                                        message = "No configuration exists below 0 or above 63.")

                self.currentPicture = configNumber
                configImage = self.addLabel(text = "",
                                            row = 0, column = 1)

                if configNumber < 10:
                        configuration = str(0) + str(configNumber)
                else:
                        configuration = str(configNumber)

                self.image = PhotoImage(file = "./towerPics/00" + configuration + ".gif")
                configImage["image"] = self.image
        

def main():
    """Entry point for the application."""
    Towers().mainloop()

if __name__ == "__main__":
    main()
