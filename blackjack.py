import random

from collections import deque


# Define what a card is; each card has a name, a point value, and a suit
class Card:
    def __init__(self, this_card_name, this_card_points, this_card_suit):
        self.card_name = this_card_name
        self.card_points = this_card_points
        self.card_suit = this_card_suit

    # Return the card's name and suit for printing
    def get_card(self):
        return unicode(self.card_name) + self.card_suit

    # Return the card's name
    def get_name(self):
        return unicode(self.card_name)

    # Return the card's point value
    def get_points(self):
        return self.card_points


# Create a deck of cards
def create_deck():
    suit_list = [unichr(0x2665), unichr(0x2666), unichr(0x2663), unichr(0x2660)]
    name_points_dict = {"A":1, "2":2, "3":3, "4":4, "5":5, "6":6, "7":7, "8":8, "9":9, "10":10, "J":10, "Q":10, "K":10}

    # Use a double ended queue structured list for the deck
    deck_list = deque([])

    # For each suit, create a card with each of the name and point entries
    for each_suit in suit_list:
        for each_entry in name_points_dict.keys():
            new_card = Card(each_entry, name_points_dict[each_entry], each_suit)
            deck_list.append(new_card)

    return deck_list


# Select the top card from the deck
def deal(this_deck):
    dealt_card = this_deck.popleft()

    return dealt_card


# Calculate the points for a hand
def calculate_points(this_hand):
    # Check to see if hand got dealt an Ace and whether 11 points or 1 point
    total_points = 0
    int_ace_count = 0

    # For each card, add together all the points
    for each_card in this_hand:
        total_points += each_card.get_points()

        # Check for Aces, get the name of the card
        this_card_name = each_card.get_name()

        if (this_card_name == "A"):
            int_ace_count += 1

    # How to determine if Aces are worth 1 or 11
    # A - 1 or 11
    # AA - 2 or 12
    # AAA - 3 or 13
    # AAAA - 4 or 14

    if (int_ace_count > 0):
        # Add 10 points to the total if it doesn't bust the hand
        if ((total_points + 10) <= 21):
            total_points += 10

    return total_points



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
