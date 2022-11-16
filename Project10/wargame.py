"""
Author: Marshall Jones, Johnny Lavette, Eric Dyer
File: wargame.py
Project 10

Module for playing the game of War
"""

from cards import Deck, Card
import random
import gc

class WarGame(object):
    """Plays the game of War."""

    def __init__(self, p1 = None, p2 = None):
        """Sets up the two players, the war pile, the deck, and the
        game state."""
        self.players = (None, p1, p2)
        self.playerCards = [None, list(), list()]
        self.playedCards =[]
        self.warPile = []
        self.gameState = ""
        self.deck = Deck()
        self.deck.shuffle()
        self.steps = 0

    def __str__(self):
        """Returns the game state."""
        return self.gameState

    def deal(self):
        """Deals 26 cards to each player."""
        while not self.deck.isEmpty():
            card = self.deck.deal()
            self.players[1].addToUnplayedPile(card)
            self.playerCards[1].append(card)
            card = self.deck.deal()
            self.playerCards[2].append(card)
            self.players[2].addToUnplayedPile(card)

    def step(self):
        """Makes one move in the game, and returns the two cards
        played."""

        #On even turns, the first player goes first
        if self.steps%2==0:
            turnplayer = 1
            otherplayer = 2
        else:
            turnplayer = 2
            otherplayer = 1
        
        #The getCard method of a player takes in a parameter which shows the PREVIOUS CARD PLAYED during this turn.
        #The player going first gets NONE, the player going 2nd gets whichever card the first player played
        card1 = self.players[turnplayer].getCard(None) #Show the player NONE since no card played yet
        
        #Let's make sure that the card being played actually exists and isn't already been played!
        if all(map(lambda card: not card1.sameCard(card), self.playerCards[turnplayer])) or any(map(lambda card: card1.sameCard(card), self.playedCards)):
            raise Exception("Player {} made an illegal move playing {}. Either that card has already been played or that player doesn't have the card".format(turnplayer,card1))
            
        self.warPile.append(card1)
        self.playedCards.append(card1)
        card2 = self.players[otherplayer].getCard(card1.copy())    #Show the other player a copy of the card played by the initial player (no TAMPERING!)
        
        if all(map(lambda card: not card2.sameCard(card), self.playerCards[otherplayer])) or any(map(lambda card: card2.sameCard(card), self.playedCards)):
            raise Exception("Player {} made an illegal move playing {}. Either that card has already been played or that player doesn't have the card".format(turnplayer,card1))
        
        self.warPile.append(card2)
        self.playedCards.append(card2)
        self.players[turnplayer].observe(card2.copy())    #Tells the turnplayer what card the otherplayer played

        self.gameState = "Player {}: {} \nPlayer {}: {}".format(turnplayer,card1,otherplayer,card2)
        if card2 < card1:
            self.transferCards(self.players[turnplayer])
            self.gameState += "\nCards go to Player {}\n".format(turnplayer)
        elif card1 < card2:
            self.transferCards(self.players[otherplayer])
            self.gameState += "\nCards go to Player {}\n".format(otherplayer)
        else:
            self.gameState += "\nCards split\n"
            self.transferCards(self.players[turnplayer],1)
            self.transferCards(self.players[otherplayer])
        self.steps += 1
        return (card1, card2)

    def transferCards(self, player, limit = 0):
        """Transfers cards from the war pile to the player's
        winnings pile."""
        while len(self.warPile) > limit:
            player.addToWinningsPile(self.warPile.pop())

    def winner(self):
        """Returns None if there is no winner yet or if there is a tie.  Otherwise,
        returns the player number who won """
        if self.players[1].isDone() or self.players[2].isDone():
            count1 = self.players[1].winningsCount()
            count2 = self.players[2].winningsCount()
            if count1 + count2 > 52:
                raise Exception("Winnings don't add up!")
            if count1 > count2:
                return 1
            elif count2 > count1:
                return 2
            else:
                return -1
        else:
            return None

    def winnerText(self):
        """Returns None if there is no winner yet.  Otherwise,
        returns a string indicating the player who won with each
        player's number of cards, or a tie.
        """
        if self.players[1].isDone() or self.players[2].isDone():
            count1 = self.players[1].winningsCount()
            count2 = self.players[2].winningsCount()
            if count1 + count2 > 52:
                raise Exception("Winnings don't add up!")
            if count1 > count2:
                return "Player 1 wins, " + str(count1) + " to " +\
                       str(count2) +"!"

            elif count2 > count1:
                return "Player 2 wins, " + str(count2) + " to " +\
                       str(count1) +"!"
            else:
                return "The game ends in a tie!"
        else:
            return None
        

##You will modify the code starting here
class Player(object):
    """Represents a War game player."""

    def __init__(self):
        """Sets up the player's unplayed and winnings piles."""
        self.unplayed = []
        self.winnings = []

    def __str__(self):
        """Returns a description of the player's winnings pile."""
        for x in len(self.winnings):
            return self.winnings[x]
    
    def playerName(self):
        return "Anonymous Player"

    def addToUnplayedPile(self, card):
        """Adds card to the player's unplayed pile."""
        self.unplayed.append(card)

    def addToWinningsPile(self, card):
        """Adds card to the player's winnings pile."""
        self.winnings.append(card)

    def getCard(self, opponent_play):
        """Removes and returns a card from the player's unplayed pile."""
        """DO NOT DO ANYTHING WITH OPPONENT_PLAY HERE! That's just telling you what card the opponent played!"""
        return self.unplayed.pop()

    def isDone(self):
        """Returns True if the player's unplayed pile is empty,
        or False otherwise."""
        if len(self.unplayed) == 0:
            return True
        else:
            return False

    def winningsCount(self):
        """Returns the number of cards in the player's winnings pile."""
        n = len(self.winnings)
        return n

    def observe(self, opponent_play):
        """This method is called to tell the player that a new card has been played by the opponent"""
        """You don't need to do anything with this"""
        pass
        

class Cheater(Player):
    """Represents a War Game Cheater"""

    def getCard(self, opponent_play):
        """This method allows the player to cheat since
        he can see the opponent's play before he plays
        his hand."""
        higherNumbers = []
        for i in range(len(self.unplayed)):
            if self.unplayed[i] > opponent_play:
                higherNumbers.append(self.unplayed[i])

        if opponent_play == type(None):
            """in case cheater is player 1"""
            big = self.unplayed.index(max(self.unplayed))
            return self.unplayed.pop(big)
            
        elif len(higherNumbers) < 1:
            """if cheater has no higher cards than player"""
            small = self.unplayed.index(min(self.unplayed))
            return self.unplayed.pop(small)
        
        else:
            """cheater plays the smallest card he has that's still
            larger than the other player's"""
            bestPlay = self.unplayed.index(min(higherNumbers))
            return self.unplayed.pop(bestPlay)
