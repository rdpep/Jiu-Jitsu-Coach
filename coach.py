'''
This is the main file to run that will simulate a coach
calling out different moves for the user to drill, based
on their selections
'''
import random
import time
import pyttsx3
from built_drill_tree import drill_tree

is_blitz = False
engine = pyttsx3.init()
rate = engine.getProperty('rate')
voices = engine.getProperty('voices')
engine.setProperty('rate', rate-30)
engine.setProperty('voice', voices[14].id)

def run_training(node):
    '''
    Traverses through drill tree prompting the user
    with decisions based on that node level.
    Exits once a leaf is reached, indicating drills reached. 
    '''
    global is_blitz
    while not node.is_leaf():
        print(node.prompt)
        options = list(node.options.keys())
        for i, option in enumerate(options, start=1):
            print(f'{i}. {option}')
        try:
            choice = int(input('Select option: ')) - 1      # Validation check until valid input
            if options[choice] == 'BLITZ':
                is_blitz = True
        except (ValueError, IndexError):
            print('Enter a valid input.\n')
            continue
        node = node.options[options[choice]]    # Returns str option from options list to use as key in .options dict


    if is_blitz:
        blitz_encouragement = [
            'You\'re doing great! Keep training',
            'Another rep, come on!',
            'Strive to be the best you can be!',
            'Do it again, but better',
            'Anything within your capacity will not make you grow!'
        ]

        engine.setProperty('rate', rate-25)
        engine.say('BLITZ MODE ENGAGED')
        engine.runAndWait()
        time.sleep(5)

        i = 0
        while True:   # Will intentionally loop forever until user enters "ctrl+c" to exit out of program
            engine.say(random.choice(node.drills))
            engine.runAndWait()
            time.sleep(11)
           
            if i in [7, 14, 21, 23, 38, 50]:
                engine.say(random.choice(blitz_encouragement))
                engine.runAndWait()
                time.sleep(1)

            engine.say('Reset.')
            engine.runAndWait()
            time.sleep(4)
            i += 1


    engine.say('Loading training simulation')   # Specialized mode, runs for 8 reps
    engine.runAndWait()
    time.sleep(5)
    i = 0
    while i < 7:
        if i > 0:
            engine.say('Reset.')
            engine.runAndWait()

        time.sleep(5)
        engine.say(random.choice(node.drills))
        engine.runAndWait()
    
        time.sleep(11)
        i += 1
    
    engine.say('Training simulation complete.')
    engine.runAndWait()

if __name__ == '__main__':
    run_training(drill_tree)
