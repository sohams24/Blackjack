import constants

class Hand:
    def __init__(self):
        self.cards = []  # start with an empty list as we did in the Deck class
        self.value = 0   # start with zero value
        self.aces = 0    # add an attribute to keep track of aces

    def add_card(self,new_card):
        if new_card.rank == "Ace":
            self.aces += 1
        self.cards.append(new_card)
        new_card_rank = new_card.rank
        new_card_value = constants.values[new_card_rank]
        self.value += new_card_value


    def adjust_for_ace(self):
        if self.value>21 and self.aces>0:
            self.value -= 10
            self.aces -= 1

    def __str__(self):
        str1 = ""
        for card in self.cards:
            str1 += card.__str__() + "\n"
        str1 += "\nValue: {}".format(self.value)
        return str1
