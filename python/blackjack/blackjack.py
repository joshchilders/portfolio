import random
import time


class card:
    def __init__(self, suit, face, value):
        self.suit = suit
        self.face = face
        self.value = value
        
    def __str__(self):
        return f"|{self.face}\u00B7{self.suit}|"

def main():

    deck = []
    playerHand = []
    dealerHand = []

    # Create the deck
    deck = create_suits(deck, "\u2660")
    deck = create_suits(deck, "\u2665")
    deck = create_suits(deck, "\u2663")
    deck = create_suits(deck, "\u2666")

    random.shuffle(deck)

    # Deal a new hand
    # deal_hand(deck, hand, dealerHand)

    # Keep dealing new hands until player exits
    play = True
    while play:

        # Deal initial hands
        deal = True
        while deal:
            deal_card(deck, playerHand)
            deal_card(deck, dealerHand)
            if len(dealerHand) > 1:
                deal = False

        # Print cards to terminal
        print()
        print_hand(playerHand)
        print()
        first = True
        for card in dealerHand:
            if first:
                first = False
                print("| \u00B7 |", end="")
            else:
                print(f"{card}", end="")
        print()

        # Ask player for new card
        bust = False
        while True:
            print()
            userInput = input("Hit? ").lower()
            if userInput == "n":
                break
            elif userInput == "y":
                deal_card(deck, playerHand)
                print()
                print_hand(playerHand)
                print()
                first = True
                for card in dealerHand:
                    if first:
                        first = False
                        print("| \u00B7 |", end="")
                    else:
                        print(f"{card}", end="")
                print()
                if calculate_hand_value(playerHand) > 21:
                    bust = True
                    print()
                    print("==== BUST ====")
                    print()
                    break

        if bust == False:
            print()
            print_hand(playerHand)
            print_hand(dealerHand)
            while calculate_hand_value(dealerHand) < 16:
                time.sleep(2)
                deal_card(deck, dealerHand)
                print()
                print_hand(playerHand)
                print_hand(dealerHand)
                time.sleep(1)
            if calculate_hand_value(dealerHand) > 21:
                print()
                print("=== DEALER BUST ===")
                print()
            elif calculate_hand_value(dealerHand) > calculate_hand_value(playerHand):
                print()
                print("=== DEALER WINS ===")
                print()
            elif calculate_hand_value(dealerHand) < calculate_hand_value(playerHand):
                print()
                print("=== YOU WIN ===")
                print()
            elif calculate_hand_value(dealerHand) == calculate_hand_value(playerHand):
                print()
                print("=== IT'S A TIE ===")
                print()
        
        # Shuffle hands back into deck
        for card in playerHand:
            deck.append(card)
        for card in dealerHand:
            deck.append(card)

        playerHand.clear()
        dealerHand.clear()

        random.shuffle(deck)
        
        # Ask if player wants to keep playing
        userInput = input("New hand? ").lower()
        if userInput == "y":
            play = True
        else:
            play = False


def create_suits(deck, suit):

    for i in range(1, 14):
        if i == 1:
            face = "A"
            value = 11
        elif i == 10:
            face = 0
            value = 10
        elif i == 11:
            face = "J"
            value = 10
        elif i == 12:
            face = "Q"
            value = 10
        elif i == 13:
            face = "K"
            value = 10
        else:
            face = i
            value = i
        newCard = card(suit, face, value)
        deck.append(newCard)

    return deck


def deal_card(deck, hand):

    topCard = deck[0]
    deck.pop(0)
    hand.append(topCard)

    return hand


def print_hand(hand):

    for card in hand:
        print(f"{card}", end="")
    print()
    return


def calculate_hand_value(hand):

    value = 0
    for card in hand:
        value += card.value
    
    # Handle aces (1 or 11)
    if value > 21:
        for card in hand:
            if card.face == "A":
                value -= 10

    return value


def deal_hand(deck, hand, dealerHand):

    # Shuffle the deck
    random.shuffle(deck)

    deal = True

    for i in range(2):
        topCard = deck[0]
        deck.pop(0)
        hand.append(topCard)
        topCard = deck[0]
        deck.pop(0)
        dealerHand.append(topCard)
    
    for card in hand:
        print(f"|{card}|", end="")
    print()
    first = True
    for card in dealerHand:
        if first:
            first = False
            print("| \u00B7 |", end="")
        else:
            print(f"|{card}|", end="")
    print()

    return

main()