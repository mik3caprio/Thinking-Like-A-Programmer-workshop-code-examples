import random

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
print u"Welcome to blackjack! Highest to 21 wins. Dealing for you..."

# Deal two cards to the player
player_card = deal(deck)
player_hand.append(player_card)
player_total = calculate_points(player_hand)

print u"You have: " + player_card.get_card()

player_card = deal(deck)
player_hand.append(player_card)
player_total = calculate_points(player_hand)

print u"You have: " + player_card.get_card() + u", total of " + unicode(player_total)

# Deal two cards to the dealer
print u"Now dealing for the dealer..."

dealer_card = deal(deck)
dealer_hand.append(dealer_card)
dealer_total = calculate_points(dealer_hand)

print u"Dealer deals one card up, dealer has: " + dealer_card.get_card() + u", total of " + unicode(dealer_total)

dealer_card = deal(deck)
dealer_hand.append(dealer_card)
dealer_total = calculate_points(dealer_hand)

print u"Dealer deals another card down."

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

        print u"Player dealt: " + player_card.get_card() + u", total of " + unicode(player_total)

        if (player_total > 21):
            # Check to see if player busts
            print "Busted! Game over."
            break
        elif (player_total == 21):
            # Check to see if player wins
            print "Player has 21!"
            bool_player_done = True
    elif (player_action == "s"):
        # If stand, player is done, deal dealer's cards
        string_dealer = u"Dealer reveals his cards: "

        for each_card in dealer_hand:
            string_dealer += each_card.get_card() + u", "

        dealer_total = calculate_points(dealer_hand)
        string_dealer += u"total of " + unicode(dealer_total)

        print string_dealer

        while True:
            # Dealer must hit if points are <= 16 must stand on > 16
            if (dealer_total <= 16):
                # Dealer must hit
                print "Dealer hits..."

                dealer_card = deal(deck)
                dealer_hand.append(dealer_card)
                dealer_total = calculate_points(dealer_hand)

                print u"Dealer has: " + dealer_card.get_card() + u", total of " + unicode(dealer_total)

                if (dealer_total > 21):
                    # Check to see if dealer busts
                    print "Dealer busted! Player wins!!"
                    break
                elif (dealer_total == 21):
                    # If dealer gets 21, house wins
                    print "Dealer wins! Game over."
                    break
            else:
                # Dealer has to stand, check to see who wins
                print "Dealer stands."

                if (player_total > dealer_total):
                    # Player wins with more points
                    print "Player wins with %s!!" % (str(player_total), )
                elif (player_total == dealer_total):
                    # Or there is a tie
                    print "Push! Looks like a tie - Game over."
                else:
                    # Or the dealer wins with more points
                    print "Dealer wins with %s! Game over." % (str(dealer_total), )

                break

        break
    else:
        # Or maybe there is bad input
        print "Bad input! Must be h or s to hit or stand respectively."
        continue
