import Global
from os import system, name

def take_bet(chips):

    while True:
        try:
            bet_value = int(input("How much amount in $ would you like to bet: "))
        except ValueError:
            print("Invalid input. Please inter a number ")
        else:
            clear_output()
            if bet_value>chips.total:
                print("Insufficient chips. Please bet a lower value")
            elif bet_value<10:
                print("The minimum bet is $10.")
            else:
                chips.bet = bet_value
                break


def hit(deck,hand):
    new_card = deck.deal()
    hand.add_card(new_card)
    hand.adjust_for_ace()



def hit_or_stand(deck,hand):
    global playing# to control an upcoming while loop

    while True:
        choice = input("\nDo you wish to hit or stand? (H/S) ")
        if choice in ['H','h']:
            hit(deck,hand)
            break
        elif choice in ['S', 's']:
            Global.playing = False
            break
        else:
            print("Invalid input. Please enter H or S")


# test_deck = Deck()
# test_hand = Hand()
# hit_or_stand(test_deck, test_hand)

# print(test_deck)

# print(test_hand)


def show_some(player,dealer):

    print("Your cards:")
    for card in player.cards:
        print(card)
    print("Value: {}".format(player.value))
    print("\n")
    print("Dealers cards:")
    print(dealer.cards[0])
    print("\n")


def show_all(player,dealer):

    print("PLayers cards:")
    for card in player.cards:
        print(card)
    print("Value: {}".format(player.value))
    print("\n")
    print("Dealers cards:")
    for card in dealer.cards:
        print(card)
    print("Value: {}".format(dealer.value))
    print("\n")



def player_busts(chips):

#     clear_output()
    print("\nYou busted!!!\n")
    chips.lose_bet()

def player_wins(chips):

#     clear_output()
    print("\nYou won!!!\n")
    chips.win_bet()

def dealer_busts(chips):

#     clear_output()
    print("\nDealer busted!!!\n")
    chips.win_bet()

def dealer_wins(chips):

#     clear_output()
    print("\nYou lost!!!\n")
    chips.lose_bet()

def push(chips):

#     clear_output()
    print("\nTie!!!\n")


def black_jack(chips):
    print("Blackjack!!!")
    chips.black_jack()

def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')

