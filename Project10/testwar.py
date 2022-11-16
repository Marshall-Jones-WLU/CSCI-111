"""
Author: Marshall Jones, Johnny Lavette, Eric Dyer
File: testwar.py
Project 10

A simple terminal-based test driver for a game of War.
"""

from wargame import WarGame,Player,Cheater
import random

def playMany(n = 100):
   """Terminal-based trace of n games of War,
   with a statistical report as the output"""
   p1Wins = 0
   p2Wins = 0
   ties = 0
   
   for i in range(n):
      p1 = Player()
      p2 = Player()
      game = WarGame(p1,p2)
      game.deal()
      while not game.winner():
         game.step()

      winner = game.winner()
      if winner == 1:
         p1Wins += 1
      elif winner == 2:
         p2Wins += 1
      elif winner == -1:
         ties += 1

   print("Player 1 Win Count: ",p1Wins)
   print("Player 2 Win Count: ",p2Wins)
   print("Tie Count:          ",ties)
'''
   if p1Wins > p2Wins:
      champ = p1Wins
   elif p2Wins > p1Wins:
      champ = p2Wins
   else:
      print("Something has gone terribly wrong!")
   percentWins = champ / (p1Wins + p2Wins + ties)
   print("\nWinner's ratio:     ",percentWins)
'''

def playManyCheater(n = 100):
   """Terminal-based trace of n games of War,
   played by a cheater and with a statistical
   report as the output"""
   p1Wins = 0
   p2Wins = 0
   ties = 0
   
   for i in range(n):
      p1 = Player()
      p2 = Cheater()
      game = WarGame(p1,p2)
      game.deal()
      while not game.winner():
         game.step()

      winner = game.winner()
      if winner == 1:
         p1Wins += 1
      elif winner == 2:
         p2Wins += 1
      elif winner == -1:
         ties += 1

   print("Player 1 Win Count: ",p1Wins)
   print("Player 2 Win Count: ",p2Wins)
   print("Tie Count:          ",ties)

   if p1Wins > p2Wins:
      champ = p1Wins
   elif p2Wins > p1Wins:
      champ = p2Wins
   else:
      print("Something has gone terribly wrong!")
   percentWins = champ / (p1Wins + p2Wins + ties)
   print("\nWinner's ratio:     ",percentWins)

def main():
   """Terminal-based trace of a game of War."""
   p1 = Player()
   p2 = Player()
   game = WarGame(p1,p2)
   game.deal()
   while not game.winner():
      game.step()
      print(game)
   print(game.winnerText())
    
if __name__ == "__main__":
    #main()
    #playMany(10000)
    playManyCheater(10000)
