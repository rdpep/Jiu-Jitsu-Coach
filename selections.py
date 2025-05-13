import sys
from dictionary import moves


def position_selection(prior_choice):
    '''Prompts for choice of position to train from. Currently only offensive options.'''

    while True:
        try:
            if prior_choice == 1:
                print('\n\nPosition:\n')
                position = int(input('1. Seated Guard\t\t2. Reverse Z-Guard\n3. Half Guard Bottom\t4. Standing\n5. Back Control\t\t6. Leg Ride\n7. Turtle\t\t8. 50/50\n9. Deep Half Guard\t10. Knee Shield Bottom\n11. Half Guard Top\t12. Knee on Belly Bottom\n13. Leg Drag\t\t14. Knee on Belly Top\n15. Butterfly Ashi\t16. Z-Guard\n'))
            else:
                sys.exit('Defense area is not yet ready. Will be released in v2.0')
        except ValueError: 
            pass

        if position in range(1,17):  # Edit whenever new positions added, checks for valid choice
            return position
        else: 
            print('Input a valid choice')


def opponent_position_selection(position_choice):
    '''Prompts for opponent's position based on prior position selection, if applicable.'''

    while True:
        valid = False   # Assumes integer validity for input is false until confirmed
        try:
            print('\n\nOpponent\'s Position:\n')
            if position_choice == 1:
                opponent_position = int(input('1. Standing\t\t2. Kneeling\n'))
                if opponent_position in [1, 2]:
                    valid = True
            elif position_choice == 2:
                opponent_position = int(input('1. Body lock\t\t2. Arm over shoulder\n'))
                if opponent_position in [1, 2]:
                    valid = True
            elif position_choice == 3:
                opponent_position = int(input('1. Inside knee down\t\t2. Inside knee up\n'))
                if opponent_position in [1, 2]:
                    valid = True
            elif position_choice == 4:
                opponent_position = int(input('1. Supine\t\t2. Standing\n'))
                if opponent_position in [1, 2]:
                    valid = True
            elif position_choice == 6:
                opponent_position = int(input('1. Leg in-between\t\t2. Leg on top\n'))
                if opponent_position in [1, 2]:
                    valid = True
            elif position_choice == 7:
                opponent_position = int(input('1. Rear Body Lock\t\t2. Leg-Between Rear Body Lock\n'))
                if opponent_position in [1, 2]:
                    valid = True
            elif position_choice == 14:
                opponent_position = int(input('1. Standard\t\t2. Reverse\n'))
                if opponent_position in [1, 2]:
                    valid = True
            elif position_choice == 15:
                opponent_position = int(input('1. Standing\t\t2. Seated\n'))
                if opponent_position in [1, 2]:
                    valid = True
            else:
                opponent_position = None
                valid = True
        except ValueError:
            pass

        if valid == True:
            return opponent_position
        else: 
            print('Input a valid choice')


def side_selection():
    '''Prompts for which side user would like to train from.'''

    while True:
        try:
            print('\n\nSide to Train:\n')
            side = int(input('1. Right\t\t2. Left\n3. Both\n'))
        except ValueError:
            pass

        if side in range(1,4):
            return side
        else: 
            print('Input a valid choice')


def finish_selection(position: int, opponent_position=None):
    '''Prompts what finish user would like to do based on positional choices made previously.'''

    while True:
        valid = False   # Assumes integer validity for input is false until confirmed
        try:
            print('\n\nFinish:\n')
            if position == 1:
                if opponent_position == 1:
                    finish = int(input('1. Takedowns\t\t2. Leg Locks\n'))
                    if finish in [1, 2]:
                        valid = True
                elif opponent_position == 2:
                    finish = int(input('1. Leg Locks\n'))
                    if finish in [1]:
                        valid = True
            elif position == 2:
                if opponent_position == 1:
                    finish = int(input('1. Leg Locks\n'))
                    if finish in [1]:
                        valid = True
                elif opponent_position == 2:
                    finish = int(input('1. Sweeps\n'))
                    if finish in [1]:
                        valid = True
            elif position == 3:
                if opponent_position == 1:
                    finish = int(input('1. Sweeps\t\t2. Back Takes\n'))
                    if finish in [1, 2]:
                        valid = True
                elif opponent_position == 2:
                    finish = int(input('1. Leg Locks\t\t2. Takedowns\n'))
                    if finish in [1, 2]:
                        valid = True
            elif position == 4:
                if opponent_position == 1:
                    finish = int(input('1. Leg Locks\n'))
                    if finish in [1]:
                        valid = True
                elif opponent_position == 2:
                    finish = int(input('1. Takedowns\t\t2. Leg Locks\n'))
                    if finish in [1, 2]:
                        valid = True
            elif position == 5:
                finish = int(input('1. Strangles\t\t2. Arm Bar\n'))
                if finish in [1, 2]:
                    valid = True
            elif position == 6:
                if opponent_position == 1:
                    finish = int(input('1. Strangles\n'))
                    if finish in [1]:
                        valid = True
                elif opponent_position == 2:
                    finish = int(input('1. Strangles\t\t2. Arm Locks\n'))
                    if finish in [1, 2]:
                        valid = True
            elif position == 7:
                if opponent_position == 1:
                    finish = int(input('1. Leg Locks\n'))
                    if finish in [1]:
                        valid = True
                elif opponent_position == 2:
                    finish = int(input('1. Leg Locks\n'))
                    if finish in [1]:
                        valid = True
            elif position == 8:
                finish = int(input('1. Leg Locks\n'))
                if finish in [1]:
                    valid = True
            elif position == 9:
                finish = int(input('1. Leg Locks\n'))
                if finish in [1]:
                    valid = True
            elif position == 10:
                finish = int(input('1. Leg Locks\n'))
                if finish in [1]:
                    valid = True
            elif position == 11:
                finish = int(input('1. Leg Locks\n'))
                if finish in [1]:
                    valid = True
            elif position == 12:
                finish = int(input('1. Leg Locks\n'))
                if finish in [1]:
                    valid = True
            elif position == 13:
                finish = int(input('1. Leg Locks\n'))
                if finish in [1]:
                    valid = True
            elif position == 14:
                if opponent_position == 1:
                    finish = int(input('1. Arm Locks\n'))
                    if finish in [1]:
                        valid = True
                elif opponent_position == 2:
                    finish = int(input('1. Leg Locks\n'))
                    if finish in [1]:
                        valid = True
            elif position == 15:
                if opponent_position in [1, 2]:
                    finish = int(input('1. Leg Locks\n'))
                    if finish in [1]:
                        valid = True
            elif position == 16:
                finish = int(input('1. Leg Locks\t\t2. Arm Locks\n3. Strangles\t\t4. Sweeps\n'))
                if finish in range(1,5):
                    valid = True
        except ValueError:
            pass

        if valid:
            return finish   # Breaks out of loop and returns finish choice, only if a valid integer option is chosen, otherwise loops again
        
        print('Input a valid choice')


def finalized_selection():
    '''This function calls upon all the prior functions and will take those return values to select the finalized list
    from the moves dictionary to return to main code.'''

    while True:
        try:
            area = int(input('Choose your area of growth\n\n1. Offense\t\t2. Defense\n'))
            if area not in [1, 2]:
                print('Input a valid choice')
            else:
                break
        except ValueError:
            print('Input a valid integer')

    position = position_selection(area)
    opponent_position = opponent_position_selection(position)
    side = side_selection()
    finish = finish_selection(position, opponent_position)

    if opponent_position == None:
        return moves[area][position][side][finish]
    else:
        return moves[area][position][opponent_position][side][finish]