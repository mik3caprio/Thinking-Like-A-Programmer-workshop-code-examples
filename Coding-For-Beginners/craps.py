import random

from termcolor import colored

die_face = { 1 : unichr(0x2680),
             2 : unichr(0x2681),
             3 : unichr(0x2682),
             4 : unichr(0x2683),
             5 : unichr(0x2684),
             6 : unichr(0x2685) }

# Get the bet from the player - pass or don't pass
while True:
    player_bet = raw_input(colored("Would you like to bet pass or don't pass? (enter p or dp): ", 'green'))

    if ((player_bet == "p") or (player_bet == "dp")):
        break

player_point = 0

# Keep prompting for rolls until the game is over
while True:
    # Let the player hit return to roll the dice
    discard_input = raw_input(colored(u"Press Return to roll...", 'cyan'))

    # Roll two dice
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    result = die_1 + die_2

    if (player_point == 0):
    # It is the first roll
        if ((result == 7) or (result == 11)):
            # Check to see if roll is a natural
            if (player_bet == "p"):
                # If it is 7 or 11 and player bet pass, they win
                print colored("You rolled %d - you win!", 'green') % (result, )
            elif (player_bet == "dp"):
                # If it is 7 or 11 and player bet don't pass, they lose
                print colored("Ouch, you rolled %d and bet \"don't pass\" - you lose. Game Over.", 'red') % (result, )

            break
        elif (result in (2, 3, 12)):
            # Check to see if roll is craps
            if (player_bet == "p"):
                # If it is 2, 3, or 12 and player bet pass, they lose
                print colored("Ouch, you rolled %d and bet \"pass\" - you lose. Game Over.", 'red') % (result, )
            elif (player_bet == "dp"):
                # Player bets don't pass
                if (result in (2, 3)):
                    # If it is 2 or 3 and player bet don't pass, they win
                    print colored("You rolled %d - you win!", 'green') % (result, )
                else:
                    # Check to see if roll is a push / tie on a 12
                    print colored("You rolled %d - game is a push. Play again!", 'cyan') % (result, )

            break
        else:
            # Set the point
            player_point = result

            print u"Your first roll is %s, %s - your point is %d" % (die_face[die_1], die_face[die_2], player_point)
    else:
        print u"You rolled %s, %s - result of %d, your point is %d" % (die_face[die_1],
                                                                       die_face[die_2], result, player_point)
        # Check the roll to see if it matches
        if (result == 7):
            # Check to see if the roll is a 7
            if (player_bet == "p"):
                # If it is 7 and player bet pass, they lose
                print colored("Ouch, you rolled %d and bet \"pass\" - you lose. Game Over.", 'red') % (result, )
            elif (player_bet == "dp"):
                # If it is 7 and player bet don't pass, they win
                print colored("You rolled %d - you win!", 'green') % (result, )

            break
        elif (result == player_point):
            # The roll matches the point
            if (player_bet == "p"):
                # The player makes the point and bet pass - a win
                print colored("You rolled %d - you win!", 'green') % (result, )
            elif (player_bet == "dp"):
                # The player makes the point and bet don't pass - they lose
                print colored("Ouch, you rolled %d and bet \"don't pass\" - you lose. Game Over.", 'red') % (result, )

            break
        else:
            # No result matches point or is 7 yet - keep rolling!
            print colored("Keep rolling!", 'green')
            
