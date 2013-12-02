import random

from game_library.card import *

def print_deck(this_deck):
    int_counter = 0

    for each_card in this_deck:
        int_counter += 1

        print str(int_counter) + ":" + each_card.get_card()


# First create the deck
deck = create_deck()

# Show us the deck
print_deck(deck)

print "\n"

# Shuffle the deck
random.shuffle(deck)

# Show us the shuffled deck
print_deck(deck)
