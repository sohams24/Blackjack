import random
import Global
from Card import Card

class Deck:

    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in Global.suits:
            for rank in Global.ranks:
                self.deck.append(Card(suit,rank))

    def __str__(self):
        str1 = ""
        str1 += "The deck has {} cards".format(len(self.deck))
        return str1

    def shuffle(self):
        random.shuffle(self.deck)

    def deal(self):
        return self.deck.pop(0)



# test_deck = Deck()
# print(test_deck)


# test_deck.shuffle()
# print(test_deck)
