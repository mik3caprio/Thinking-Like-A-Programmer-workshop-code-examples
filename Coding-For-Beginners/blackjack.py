import random

from termcolor import colored
from game_library.card import *


# First create the deck
deck = create_deck()

# Shuffle the deck
random.shuffle(deck)

dealer_hand = []
player_hand = []

dealer_total = 0
player_total = 0

bool_player_done = False

# Print a welcome message
print colored(u"Welcome to blackjack! Highest to 21 wins. Dealing for you...", 'green')

# Deal two cards to the player
player_card = deal(deck)
player_hand.append(player_card)
player_total = calculate_points(player_hand)

print colored(u"You have: " + player_card.get_card(), 'cyan')

player_card = deal(deck)
player_hand.append(player_card)
player_total = calculate_points(player_hand)

print colored(u"You have: " + player_card.get_card() + u" , total of " + unicode(player_total), 'cyan')

# Deal two cards to the dealer
print colored(u"Now dealing for the dealer...", 'cyan')

dealer_card = deal(deck)
dealer_hand.append(dealer_card)
dealer_total = calculate_points(dealer_hand)

print colored(u"Dealer deals one card up, dealer has: " + dealer_card.get_card() + u" , total of " + unicode(dealer_total), 'cyan')

dealer_card = deal(deck)
dealer_hand.append(dealer_card)
dealer_total = calculate_points(dealer_hand)

print colored(u"Dealer deals another card down.", 'cyan')

# Play the game until the player or dealer finish
while True:
    if (not bool_player_done):
        player_action = raw_input("Do you want to hit or stand? (h or s): ")
    else:
        player_action = "s"

    # Check to see if input is hit or stand
    if ((player_action == "h") and (not bool_player_done)):
        # If hit, deal a card
        player_card = deal(deck)
        player_hand.append(player_card)
        player_total = calculate_points(player_hand)

        print colored(u"Player dealt: " + player_card.get_card() + u" , total of " + unicode(player_total), 'cyan')

        if (player_total > 21):
            # Check to see if player busts
            print colored("Busted! Game over.", 'red')
            break
        elif (player_total == 21):
            # Check to see if player wins
            print colored("Player has 21!", 'green')
            bool_player_done = True
    elif (player_action == "s"):
        # If stand, player is done, deal dealer's cards
        string_dealer = u"Dealer reveals his cards: "

        for each_card in dealer_hand:
            string_dealer += each_card.get_card() + u" , "

        dealer_total = calculate_points(dealer_hand)
        string_dealer += u"total of " + unicode(dealer_total)

        print colored(string_dealer, 'cyan')

        while True:
            # Dealer must hit if points are <= 16 must stand on > 16
            if (dealer_total <= 16):
                # Dealer must hit
                print colored("Dealer hits...", 'cyan')

                dealer_card = deal(deck)
                dealer_hand.append(dealer_card)
                dealer_total = calculate_points(dealer_hand)

                print colored(u"Dealer has: " + dealer_card.get_card() + u" , total of " + unicode(dealer_total), 'cyan')

                if (dealer_total > 21):
                    # Check to see if dealer busts
                    print colored("Dealer busted! Player wins!!", 'green')
                    break
                elif (dealer_total == 21):
                    # If dealer gets 21, house wins
                    print colored("Dealer wins! Game over.", 'red')
                    break
            else:
                # Dealer has to stand, check to see who wins
                print colored("Dealer stands.", 'cyan')

                if (player_total > dealer_total):
                    # Player wins with more points
                    print colored("Player wins with %s!!" % (str(player_total), ), 'green')
                elif (player_total == dealer_total):
                    # Or there is a tie
                    print colored("Push! Looks like a tie - Game over.", 'cyan')
                else:
                    # Or the dealer wins with more points
                    print colored("Dealer wins with %s! Game over." % (str(dealer_total), ), 'red')

                break

        break
    else:
        # Or maybe there is bad input
        print colored("Bad input! Must be h or s to hit or stand respectively.", 'red')
        continue
