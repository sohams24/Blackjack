import constants
from os import system, name

def take_bet(chips):

    while True:
        try:
            bet_value = int(input("How much amount in $ would you like to bet: "))
        except ValueError:
            print("Invalid input. Please inter a number ")
        else:
            clear_console()
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
    constants.playing  # to control an upcoming while loop

    while True:
        choice = input("\nDo you wish to hit or stand? (H/S) ")
        if choice in ['H','h']:
            hit(deck,hand)
            break
        elif choice in ['S', 's']:
            constants.playing = False
            break
        else:
            print("Invalid input. Please enter H or S")

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

    print("\nYou busted!!!\n")
    chips.lose_bet()

def player_wins(chips):

    print("\nYou won!!!\n")
    chips.win_bet()

def dealer_busts(chips):

    print("\nDealer busted!!!\n")
    chips.win_bet()

def dealer_wins(chips):

    print("\nYou lost!!!\n")
    chips.lose_bet()

def black_jack(chips):
    print("Blackjack!!!")
    chips.black_jack()

def clear_console():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
