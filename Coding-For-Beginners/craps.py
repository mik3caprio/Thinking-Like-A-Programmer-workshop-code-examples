#!/usr/bin/env python
"""This code plays a craps game with the user. It follows all the basic
rules of the dice throwing game."""

import random

from termcolor import colored

DIE_FACE = {1 : unichr(0x2680),
            2 : unichr(0x2681),
            3 : unichr(0x2682),
            4 : unichr(0x2683),
            5 : unichr(0x2684),
            6 : unichr(0x2685)}

# Get the bet from the player - pass or don't pass
while True:
    PLAYER_BET = raw_input(colored("Would you like to bet pass or don't pass? \
(enter p or dp): ", 'green'))

    if PLAYER_BET == "p" or PLAYER_BET == "dp":
        break

PLAYER_POINT = 0

# Keep prompting for rolls until the game is over
while True:
    # Let the player hit return to roll the dice
    DISCARD_INPUT = raw_input(colored(u"\nPress Return to roll...", 'cyan'))

    # Roll two dice
    DIE_1 = random.randint(1, 6)
    DIE_2 = random.randint(1, 6)

    RESULT = DIE_1 + DIE_2

    if PLAYER_POINT == 0:
        # It is the first roll
        if RESULT == 7 or RESULT == 11:
            # Check to see if roll is a natural
            if PLAYER_BET == "p":
                # If it is 7 or 11 and player bet pass, they win
                print colored("You rolled %d - you win!", 'green') % (RESULT, )
            elif PLAYER_BET == "dp":
                # If it is 7 or 11 and player bet don't pass, they lose
                print colored("Ouch, you rolled %d and bet \"don't pass\" - \
you lose. Game Over.", 'red') % (RESULT, )

            break
        elif RESULT in (2, 3, 12):
            # Check to see if roll is craps
            if PLAYER_BET == "p":
                # If it is 2, 3, or 12 and player bet pass, they lose
                print colored("Ouch, you rolled %d and bet \"pass\" - you lose.\
Game Over.", 'red') % (RESULT, )
            elif PLAYER_BET == "dp":
                # Player bets don't pass
                if RESULT in (2, 3):
                    # If it is 2 or 3 and player bet don't pass, they win
                    print colored("You rolled %d - you win!", 'green') % \
                        (RESULT, )
                else:
                    # Check to see if roll is a push / tie on a 12
                    print colored("You rolled %d - game is a push. Play \
again!", 'cyan') % (RESULT, )

            break
        else:
            # Set the point
            PLAYER_POINT = RESULT

            print u"Your first roll is %s, %s - your point is %d" % \
                (DIE_FACE[DIE_1], DIE_FACE[DIE_2], PLAYER_POINT)
    else:
        print u"You rolled %s, %s - result of %d, your point is %d" % \
            (DIE_FACE[DIE_1], DIE_FACE[DIE_2], RESULT, PLAYER_POINT)
        # Check the roll to see if it matches
        if RESULT == 7:
            # Check to see if the roll is a 7
            if PLAYER_BET == "p":
                # If it is 7 and player bet pass, they lose
                print colored("Ouch, you rolled %d and bet \"pass\" - you \
lose. Game Over.", 'red') % (RESULT, )
            elif PLAYER_BET == "dp":
                # If it is 7 and player bet don't pass, they win
                print colored("You rolled %d - you win!", 'green') % \
                    (RESULT, )

            break
        elif RESULT == PLAYER_POINT:
            # The roll matches the point
            if PLAYER_BET == "p":
                # The player makes the point and bet pass - a win
                print colored("You rolled %d - you win!", 'green') % (RESULT, )
            elif PLAYER_BET == "dp":
                # The player makes the point and bet don't pass - they lose
                print colored("Ouch, you rolled %d and bet \"don't pass\" - you \
lose. Game Over.", 'red') % (RESULT, )

            break
        else:
            # No result matches point or is 7 yet - keep rolling!
            print colored("Keep rolling!", 'green')
