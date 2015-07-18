#!/usr/bin/env python
"""This code plays a number guessing game with the user. It randomly
generates a number then continuously prompts the user to enter a
number; each time it compares the guess to the generated number and
gives a hint back to the user until the user guesses the number."""

import random

# Choose a random number
the_number = random.randint(1, 100)

# Keep prompting for input until the game is over
while True:
    number_guess = raw_input("Guess an integer between 1 and 100: ")

    # Check to see if input is a number
    if number_guess.isdigit():
        # Convert number to an integer
        number_guess = int(number_guess)

        # Check to see if it is an integer between 1 and 100 inclusive
        if number_guess < 1 or number_guess > 100:
            print "Bad guess! Must be a number between 1 and 100."
            continue
        else:
            # If it is a good number guess, but not the right number, give hints
            if the_number < number_guess:
                # Give lower hint
                print "Guess lower!"
            elif number_guess < the_number:
                # Give higher hint
                print "Guess higher!"
            else:
                # The number equals the guess!
                print "You got it!!"
                break
    else:
        # Return an error
        print "Bad guess! Must be an INTEGER NUMBER between 1 and 100."
        continue
