
# Define what a card is; each card has a name, a point value, and a suit

    # Return the card's name and suit for printing

    # Return the card's name

    # Return the card's point value



# Create a deck of cards

    # Use a double ended queue structured list for the deck

    # For each suit, create a card with each of the name and point entries



# Select the top card from the deck



# Calculate the points for a hand

    # Check to see if hand got dealt an Ace and whether 11 points or 1 point

    # For each card, add together all the points

        # Check for Aces, get the name of the card

    # How to determine if Aces are worth 1 or 11
    # A - 1 or 11
    # AA - 2 or 12
    # AAA - 3 or 13
    # AAAA - 4 or 14

    # Add 10 points to the total if it doesn't bust the hand



# First create the deck

# Shuffle the deck

# Print a welcome message

# Deal two cards to the player

# Deal two cards to the dealer

# Play the game until the player or dealer finish

    # Check to see if input is hit or stand

        # If hit, deal a card

            # Check to see if player busts

            # Check to see if player wins

        # If stand, player is done, deal dealer's cards

            # Dealer must hit if points are <= 16 and must stand on > 16

                # Dealer must hit

                    # Check to see if dealer busts

                    # If dealer gets 21, house wins

                # Dealer has to stand, check to see who wins

                    # Player wins with more points

                    # Or there is a tie

                    # Or the dealer wins with more points

    # Or maybe there is bad input
