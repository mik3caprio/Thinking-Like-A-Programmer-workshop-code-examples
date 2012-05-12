import random

# Get the bet from the player - pass or don't pass
while True:
    player_bet = raw_input("Would you like to bet pass or don't pass? (enter p or dp): ")

    if ((player_bet == "p") or (player_bet == "dp")):
        break

player_point = 0

# Keep prompting for rolls until the game is over
while True:
    # Let the player hit return to roll the dice
    discard_input = raw_input("Press Return to roll...")

    # Roll two dice
    die_1 = random.randint(1, 6)
    die_2 = random.randint(1, 6)

    result = die_1 + die_2

    # If it is the first roll, and it is not 7 or 11, declare the point
    if (player_point == 0):
        if ((result == 7) or (result == 11)):
            if (player_bet == "p"):
                # If it is 7 or 11 on the first roll and player bet pass, they win
                print "You rolled %d - you win!" % (result, )
            elif (player_bet == "dp"):
                # If it is 7 or 11 and player bet don't pass, they lose
                print "Ouch, you rolled %d and bet \"don't pass\" - you lose. Game Over." % (result, )

            break
        else:
            # Set the point
            player_point = result

            print "You rolled %d, %d - your point is %d" % (die_1, die_2, player_point)
    else:
        print "You rolled %d, %d - result of %d, your point is %d" % (die_1, die_2, result, player_point)

        # Check the result to see if it matches the point
        if ((result == 7) or (result == 11)):
            if (player_bet == "p"):
                # If it is 7 or 11 and player bet pass, they lose
                print "Ouch, you rolled %d and bet \"pass\" - you lose. Game Over." % (result, )
            elif (player_bet == "dp"):
                # If it is 7 or 11 and player bet don't pass, they win
                print "You rolled %d - you win!" % (result, )
                
            break
        elif (result == player_point):
            # The result matches the point
            if (player_bet == "p"):
                # The player makes the point and bet pass - a win
                print "You rolled %d - you win!" % (result, )
            elif (player_bet == "dp"):
                # The player makes the point and bet don't pass - they lose
                print "Ouch, you rolled %d and bet \"don't pass\" - you lose. Game Over." % (result, )

            break
        else:
            # No result matches point or is 7, 11 yet - keep rolling!
            print "Keep rolling!"
