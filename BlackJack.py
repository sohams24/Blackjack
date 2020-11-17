from Card import Card
from Deck import Deck
from Hand import Hand
from Chips import Chips
from Helper_functions import take_bet, hit, hit_or_stand, show_some, show_all, player_busts, player_wins, dealer_busts, dealer_wins, push, black_jack, clear

import Global

game_on = True
while game_on:
    clear_output()
    # Print an opening statement
    print("Welcome to blackjack!")
    new_deck = Deck()
    new_deck.shuffle()

    # Set up the Player's chips
    chips = Chips()
    betting = True
    bankrupt = False
    print("Your chip total: {}.".format(chips.total))

    while betting:

        busted = False
        blackjack = False
        # Create & shuffle the deck
        new_deck = Deck()
        new_deck.shuffle()

        player = Hand()
        dealer = Hand()

        busted = False

        # Prompt the Player for their bet
        take_bet(chips)

        # deal two cards to each player
        for count in range(2):
            player.add_card(new_deck.deal())
            dealer.add_card(new_deck.deal())

        player.adjust_for_ace()

        if player.value==21:
            black_jack(chips)
            Global.playing = False
            blackjack = True


        # Show cards (but keep one dealer card hidden)
        show_some(player,dealer)

        Global.playing = True

        while Global.playing and not blackjack:  # recall this variable from our hit_or_stand function
            # Prompt for Player to Hit or Stand
            hit_or_stand(new_deck,player)

            clear()

            # Show cards (but keep one dealer card hidden)
            show_some(player,dealer)

            # If player's hand meets 21, run black_jack() and break out of loop
            if player.value==21:
                black_jack(chips)
                Global.playing = False
                blackjack = True

            # If player's hand exceeds 21, run player_busts() and break out of loop
            elif player.value>21:
                player_busts(chips)
                Global.playing = False
                busted = True

            else:
                pass

        if not (busted or blackjack):
            # If Player hasn't busted and there was no blackjack, play Dealer's hand until Dealer reaches 17
            while dealer.value<17:
                hit(new_deck,dealer)

            # Show all cards
            show_all(player,dealer)

            # Run different winning scenarios
            if dealer.value>21:
                dealer_busts(chips)

            elif player.value>dealer.value:
                player_wins(chips)

            elif dealer.value>player.value:
                dealer_wins(chips)

            elif dealer.value == player.value:
                push(chips)

            else:
                pass


        # Inform Player of their chips total
        print("\nYour chip total is ${}".format(chips.total))
        if chips.total<10:
            print("You have chips worth less than $10. Please Get more chips to continue playing.")
            betting = False
            bankrupt= True

        while not bankrupt:
            bet_again = input("Do you wish to bet again? (Y/N)")
            if bet_again in ['Y','y']:
                break
            elif bet_again in ['N','n']:
                betting = False
                break
            else:
                print("Invalid input. Please enter Y or N")


    # Ask to play again
    while True:
        play_again = input("\nDo you wish to start a new game? (Y/N)")
        if play_again in ['Y','y']:
            break
        elif play_again in ['N','n']:
            game_on = False
            break
        else:
            print("\nInvalid input. Please enter Y or N")
