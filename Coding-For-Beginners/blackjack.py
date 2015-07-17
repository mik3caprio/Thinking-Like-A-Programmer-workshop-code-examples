#!/usr/bin/env python
"""This code plays a blackjack game with the user. It follows all the basic
rules of the blackjack card game. An external game library with an object
oriented card implementation is imported."""

import random
import sys

from termcolor import colored
from game_library.card import create_deck, deal, calculate_points


# First create the deck
DECK = create_deck()

# Shuffle the deck
random.shuffle(DECK)

DEALER_HAND = []
PLAYER_HAND = []

DEALER_TOTAL = 0
PLAYER_TOTAL = 0

BOOL_PLAYER_DONE = False

# Print a welcome message
print colored(u"Welcome to blackjack! Highest to 21 wins. Dealing for you...",
              'green')

# Deal two cards to the player
PLAYER_CARD = deal(DECK)
PLAYER_HAND.append(PLAYER_CARD)
PLAYER_TOTAL = calculate_points(PLAYER_HAND)

print colored(u"You have: " + PLAYER_CARD.get_card(), 'cyan')

PLAYER_CARD = deal(DECK)
PLAYER_HAND.append(PLAYER_CARD)
PLAYER_TOTAL = calculate_points(PLAYER_HAND)

print colored(u"You have: " + PLAYER_CARD.get_card() + u" , total of " + \
    unicode(PLAYER_TOTAL), 'cyan')

# It's possible the player can be dealt 21, if so don't give dealer cards
PLAYER_TOTAL = calculate_points(PLAYER_HAND)

if PLAYER_TOTAL == 21:
    # Exit the program if 21 is dealt on the first hand
    print colored("Player wins with %s!!" % (str(PLAYER_TOTAL), ), 'green')
    sys.exit()
else:
    # Else deal two cards to the dealer
    print colored(u"Now dealing for the dealer...", 'cyan')

    DEALER_CARD = deal(DECK)
    DEALER_HAND.append(DEALER_CARD)
    DEALER_TOTAL = calculate_points(DEALER_HAND)

    print colored(u"Dealer deals one card up, dealer has: " + \
        DEALER_CARD.get_card() + u" , total of " + unicode(DEALER_TOTAL), \
        'cyan')

    DEALER_CARD = deal(DECK)
    DEALER_HAND.append(DEALER_CARD)
    DEALER_TOTAL = calculate_points(DEALER_HAND)

    print colored(u"Dealer deals another card down.", 'cyan')

# Play the game until the player or dealer finish
while True:
    if not BOOL_PLAYER_DONE:
        PLAYER_ACTION = raw_input("\nDo you want to hit or stand? (h or s): ")
    else:
        PLAYER_ACTION = "s"

    # Check to see if input is hit or stand
    if PLAYER_ACTION == "h" and not BOOL_PLAYER_DONE:
        # If hit, deal a card
        PLAYER_CARD = deal(DECK)
        PLAYER_HAND.append(PLAYER_CARD)
        PLAYER_TOTAL = calculate_points(PLAYER_HAND)

        print colored(u"Player dealt: " + PLAYER_CARD.get_card() + u" , total \
of " + unicode(PLAYER_TOTAL), 'cyan')

        if PLAYER_TOTAL > 21:
            # Check to see if player busts
            print colored("Busted! Game over.", 'red')
            break
        elif PLAYER_TOTAL == 21:
            # Check to see if player wins
            print colored("Player has 21!", 'green')
            BOOL_PLAYER_DONE = True
    elif PLAYER_ACTION == "s":
        # If stand, player is done, deal dealer's cards
        STRING_DEALER = u"Dealer reveals his cards: "

        for each_card in DEALER_HAND:
            STRING_DEALER += each_card.get_card() + u" , "

        DEALER_TOTAL = calculate_points(DEALER_HAND)
        STRING_DEALER += u"total of " + unicode(DEALER_TOTAL)

        print colored(STRING_DEALER, 'cyan')

        while True:
            # Dealer must hit if points are <= 16 must stand on > 16
            if DEALER_TOTAL <= 16:
                # Dealer must hit
                print colored("Dealer hits...", 'cyan')

                DEALER_CARD = deal(DECK)
                DEALER_HAND.append(DEALER_CARD)
                DEALER_TOTAL = calculate_points(DEALER_HAND)

                print colored(u"Dealer has: " + DEALER_CARD.get_card() + u" , \
total of " + unicode(DEALER_TOTAL), 'cyan')

                if DEALER_TOTAL > 21:
                    # Check to see if dealer busts
                    print colored("Dealer busted! Player wins!!", 'green')
                    break
                elif DEALER_TOTAL == 21:
                    # If dealer gets 21, house wins
                    print colored("Dealer wins! Game over.", 'red')
                    break
            else:
                # Dealer has to stand, check to see who wins
                print colored("Dealer stands.", 'cyan')

                if PLAYER_TOTAL > DEALER_TOTAL:
                    # Player wins with more points
                    print colored("Player wins with %s!!" % \
                        (str(PLAYER_TOTAL), ), 'green')
                elif PLAYER_TOTAL == DEALER_TOTAL:
                    # Or there is a tie
                    print colored("Push! Looks like a tie - Game over.", 'cyan')
                else:
                    # Or the dealer wins with more points
                    print colored("Dealer wins with %s! Game over." % \
                        (str(DEALER_TOTAL), ), 'red')

                break

        break
    else:
        # Or maybe there is bad input
        print colored("Bad input! Must be h or s to hit or stand respectively.",
                      'red')
        continue
