# Blackjack
This project executes a simple logic of the Blackjack game.

The game follows the following steps.

1)    Create a deck of 52 cards.
2)    Shuffle the deck.
3)    Ask the Player for their bet.
4)    Make sure that the Player's bet does not exceed their available chips.
5)    Deal two cards to the Dealer and two cards to the Player.
6)    Show only one of the Dealer's cards, the other remains hidden.
7)    Show both of the Player's cards.
8)    Ask the Player if they wish to Hit, and take another card.
9)    If the Player's hand doesn't Bust (go over 21), ask if they'd like to Hit again.
10)   If a Player Stands, play the Dealer's hand. The dealer will always Hit until the Dealer's value meets or exceeds 17.
11)   Determine the winner and adjust the Player's chips accordingly.
12)   Ask the Player if they'd like to play again.

Instructions to run the project:
1)  Clone this repository on your local machine.
2)  Run the file "BlackJack.py".

Global.py:
This file declares the global tuples and dictonaries for the Suits, Ranks and the respective Rank values. It also has a global switch "playing" which is True while the game is ON.

Card.py:
This file contains the "Card" class. A card has two attributes, the suit to which it belongs, and it's rank.

Deck.py:
This file contains the "Deck" class. A standard deck of playing cards has four suits (Hearts, Diamonds, Spades and Clubs) and thirteen ranks (2 through 10, then the face cards Jack, Queen, King and Ace) for a total of 52 cards per deck. Jacks, Queens and Kings all have a rank of 10. Aces have a rank of either 11 or 1 as needed to reach 21 without busting. The Deck class holds all the 52 Card objects in a list, which can be shuffled.

Hand.py:
This file contains the "Hand" class. It holds Card objects dealt from the Deck. It addition to that, it is also used to calculate the value of those cards using the "values" dictionary defined in Global.py. It may also need to adjust for the value of Aces when appropriate.

Chips.py:
This file contains the "Chips" class. This class keeps track of a player's starting chips, bets, and ongoing winnings.

Helper_functions.py:
This file contains all the functions that carry out the different tasks such as taking bets, asking the player whether to "Hit" or "Stand" and carrying out those actions, functions to display the dealer cards, and functions to handle the end of game scenarios.

BlackJack.py:
This file contains the main logic of the game that makes use of the global variable and instances of all the classes mentioned above, and calls the appropriate helper_functions wherever required.




