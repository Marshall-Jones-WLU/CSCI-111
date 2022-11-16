"""
Author: KL & KL
File: testcard.py
Project 10

A simple terminal-based test driver for cards.
"""

from cards import Card

def main():
   """
   Creates some cards and tests them!
   assert(...) will just crash if the ... evaluates to False!
   """
   
   for suit in Card.SUITS:
      for rank in Card.RANKS:
         card = Card(rank, suit)
         print(card)
         
         
   #Make some cards and check that comparisons work
   card1 = Card(5,"Hearts")
   card2 = Card(7,"Hearts")
   card3 = Card(5,"Hearts")
   card4 = Card(1,"Hearts")  #Remember, ACES are supposed to be HIGH!
   card5 = Card(1,"Hearts")  #Remember, ACES are supposed to be HIGH!
   card6 = Card(1,"Clubs")
   assert(card1 < card2)
   assert(card2 != card1)
   assert(card1 == card3)
   
   #Now test comparing to invalid things
   assert(not (card1 == None))
   assert(not (card1 == "hello world"))
   assert(not (card2 < -235132478401273598))
   
   #Now test cases involving aces.
   assert(card4 > card2) #ACES should be higher than everything!
   assert(not (card4 > card5))  #ACES should be same rank
   assert(card6 > card1)
   
if __name__ == "__main__":
   main()
