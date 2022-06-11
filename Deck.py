import random
import constants
from Card import Card

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in constants.suits:
            for rank in constants.ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        str1 = ""
        str1 += "The deck has {} cards".format(len(self.deck))
        return str1

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)
