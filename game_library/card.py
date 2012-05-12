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
