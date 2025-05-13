'''This will be the mode setting that will ask for offense or defense or both, then out of ALL of those skill options, 
randomly select one and repeat until manually exited from code loop'''

from dictionary import blitz_moves
import sys

def blitz_area():
    '''Prompts user for choice of offense, defense, or both'''

    while True:
        try:
            print('Area to train:\n')
            blitz_area = int(input('1. Offense\t\t2. Defense\n3. Both\n'))
            if blitz_area not in range(1,4):
                print('Enter valid choice')
            else:
                return blitz_area
        except ValueError:
            pass

def blitz_category():
    '''This prompts the user to select a specific category they would like to blitz train, or all'''

    while True:
        try:
            print('Categories:\n')
            blitz_category = int(input('1. Leg Locks\t\t2. Arm Locks\n3. Strangles\t\t4. Positional Advancements\n5. ALL\n'))
            if blitz_category not in range(1,6):
                print('Enter valid choice')
            else:
                return blitz_category
        except ValueError:
            pass


def finalized_blitz():
    b_area = blitz_area()
    b_category = blitz_category()

    if b_area in [2,3]:
        sys.exit('Defense has not yet been built out. Once v2.2 is completed, defense and both will be added.')  # Remove once defense is added, v2.2

    return blitz_moves[b_area][b_category]
    
