import random

from game_library.card import *


# First create the deck
deck = create_deck()

# Shuffle the deck
random.shuffle(deck)

int_counter = 0

for each_card in deck:
    int_counter += 1

    print str(int_counter) + ":" + each_card.get_card()

