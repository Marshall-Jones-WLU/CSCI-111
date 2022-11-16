"""
Author: Marshall Jones
CSCI 111 Final Exam
Filename: dice_game.py

This program simulates 3000 total games of dice (with 20 sided die) and
displays the number of wins that Kunal has.
"""

import random

class DiceGame(object):

   def __init__(self):
      self.players = {}
      self.wins = {}

   def addPlayer(self, player, ID):
      '''Adds an additional player to the DiceGame, using the
      corresponding ID. Also adds an entry for their win count too!'''
      self.players[ID] = player
      self.resetWins(ID)

   def resetWins(self, ID):
      '''Resets the number of wins for the player with that ID to
      0 wins.'''
      self.wins[ID] = 0
      
   def playGame(self, ID1, ID2):
       '''Plays the game between the player with ID1 as player1 and
       the player with ID2 as player2. Each player rolls two dice, the
       one with the larger sum is the winner. If it is a tie, then
       player1 is the winner.'''
       ID1Roll = DicePlayer.roll(self)
       ID2Roll = DicePlayer.roll(self)
       if ID1Roll > ID2Roll:
          self.wins[ID1] += 1
       elif ID1Roll < ID2Roll:
          self.wins[ID2] += 1
       else:
          self.wins[ID1] += 1

   def winCount(self, ID1):
       '''Returns the number of wins that the player with the ID1 has.'''
       return self.wins[ID1]

class DicePlayer(object):
    def __init__(self, name):
        '''Constructs a player with the given name'''
        self.playerName = name
        
    def roll(self):
        '''Rolls a d20 and returns the value of the roll. A d20 is a
        20-sided die with sides that go from 1 to 20.'''
        roll1 = random.randint(1,20)
        roll2 = random.randint(1,20)
        rollSum = roll1 + roll2
        return rollSum
        
        
def main():
    #Creates three players
    p1 = DicePlayer("Kefu")
    p2 = DicePlayer("Kunal")
    p3 = DicePlayer("Kevin")
    
    #Creates a dice game and adds the three players with an ID each
    d = DiceGame()
    d.addPlayer(p1, 1138)
    d.addPlayer(p2, 421)
    d.addPlayer(p3, 1024)
    
    #Plays a bunch of games
    for i in range(1000):
        d.playGame(421, 1138)
        d.playGame(421, 1024)
        d.playGame(1024, 1138)

    #Displays wins for Kunal
    print("Kunal won",d.winCount(421),"times! Well done, Kunal.")
    
if __name__ == "__main__":
    main()
