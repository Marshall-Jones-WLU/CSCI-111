"""
Author: Marshall Jones, Johnny Lavette, and Eric Dyer
File: cards.py
Project 10

Module for playing cards, with classes Card and Deck
""" 

import random

class Card(object):
    """ A card object with a suit and rank."""

    RANKS = tuple(range(1, 14))

    SUITS = ('Spades', 'Hearts', 'Diamonds', 'Clubs')

    def __init__(self, rank, suit):
        """Creates a card with the given rank and suit."""
        if not (rank in Card.RANKS):
            raise RuntimeError('Rank must be in ' + str(Card.RANKS))
        if not (suit in Card.SUITS):
            raise RuntimeError('Suit must be in ' + str(Card.SUITS))
        self.rank = rank
        self.suit = suit
        
    def __str__(self):
        """Returns the string representation of a card."""
        if self.rank == 1:
            rank = 'Ace'
        elif self.rank == 11:
            rank = 'Jack'
        elif self.rank == 12:
            rank = 'Queen'
        elif self.rank == 13:
            rank = 'King'
        else:
            rank = self.rank
        return str(rank) + ' of ' + self.suit
    
    def copy(self):
        return Card(self.rank, self.suit)
        
    def sameCard(self, other):
        return self.rank == other.rank and self.suit == other.suit
        
    # Comparator Methods:
    def __lt__(self, other):
        """Less-than comparator method"""
        if type(self) != type(other):
            return False
        elif self.rank != 1 and self.rank < other.rank:
            return True
        elif other.rank == 1 and self.rank != 1:
            return True
        else:
            return False

    def __ne__(self, other):
        """Not-equal comparator method"""
        if type(self) != type(other):
            return False
        elif self.rank != other.rank:
            return True
        else:
            return False
    
    def __gt__(self, other):
        """Greater-than comparator method"""
        if type(self) != type(other):
            return False
        elif other.rank != 1 and self.rank > other.rank:
            return True
        elif self.rank == 1 and other.rank != 1:
            return True
        else:
            return False

    def __eq__(self, other):
        """Equal-to comparator method"""
        if type(self) != type(other):
            return False
        elif self.rank == other.rank:
            return True
        else:
            return False


class Deck(object):
    """A deck object containing 52 cards."""
    def __init__(self):
        """Creates a full deck of 52 cards"""
        self.cards = []
        for suit in Card.SUITS:
            for rank in Card.RANKS:
                c = Card(rank, suit)
                self.cards.append(c)

    def __len__(self):
        """Returns the number of cards still in the deck"""
        return len(self.cards)

    def deal(self):
        """Deals a card from the deck. In other words, it removes
        the top card from the list and returns the card or None if
        the deck is empty"""
        if len(self) == 0:
            return None
        else:
            return self.cards.pop(0)

    def isEmpty(self):
        """Asks if the deck is empty"""
        if len(self) == 0:
            return True
        else:
            return False

    def shuffle(self):
        """Shuffles the deck"""
        random.shuffle(self.cards)

    def __str__(self):
        """Returns the string representation of the deck"""
        result = ""
        for c in self.cards:
            result = result + str(c) + '\n'
        return result
