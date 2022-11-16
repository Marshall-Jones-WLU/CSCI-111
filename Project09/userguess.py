"""
Editors: Marshall Jones, Johnny Lavette, and Eric Dyer
Project 9
Filename: userguess.py

This program lays out the user interface for a GUI-based guessing game
and completes the game logic. The user guesses the computer's number.
If the user can't guess it in 7 attempts, they receive a condescending
message via a pop-up box.
"""

import random
from breezypythongui import EasyFrame

class UserGuess(EasyFrame):
    """Plays a guessing game with the user."""

    def __init__(self):
        """Sets up the window,widgets, and data."""
        EasyFrame.__init__(self, title = "Guessing Game")

        self.myNumber = random.randint(1, 100)
        self.count = 0
        greeting = "Guess a number between 1 and 100"
        self.hintLabel = self.addLabel(text = greeting,
                                       row = 0, column = 0,
                                       sticky = "NSEW",
                                       columnspan = 2)
        self.addLabel(text = "Your guess", row = 1, column = 0)
        self.guessField = self.addIntegerField(0, row = 1,
                                               column = 1)
        self.nextButton = self.addButton(text = "Next", row = 2,
                                         column = 0,
                                         command = self.nextGuess)
        self.newButton = self.addButton(text = "New game", row = 2,
                                        column = 1,
                                        command = self.newGame)

    def nextGuess(self):
        """Processes the user's next guess."""
        self.count += 1
        guess = self.guessField.getNumber()
        eighthGuess = "You are a bloody awful guesser.\nBetter luck next time, nimwit!"

        if self.count > 7:
            self.messageBox(title = "YOU LOSE, DUMMY!",
                            message = eighthGuess)

        elif guess == self.myNumber:
            self.hintLabel["text"] = "You've guessed it in " + \
                                     str(self.count) + " attempts!"
            self.nextButton["state"] = "disabled"
        elif guess < self.myNumber:
            self.hintLabel["text"] = "Sorry, too small!"
        else:
            self.hintLabel["text"] = "Sorry, too large!"

    def newGame(self):
        """Resets the GUI to its original state."""
        self.myNumber = random.randint(1, 100)
        self.count = 0
        greeting = "Guess a number between 1 and 100"
        self.hintLabel["text"] = greeting
        self.guessField.setNumber(0)
        self.nextButton["state"] = "normal"

def main():
    """Instantiate and pop up the window."""
    UserGuess().mainloop()

if __name__ == "__main__":
    main()
