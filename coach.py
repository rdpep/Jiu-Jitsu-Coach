'''This is the main program that will be run and loop over the moves and speak them out.'''

import random
import time
import pyttsx3
import selections
import blitz_mode


def main():
    '''
    Main function that takes original mode decisions, 
    then executes the speech to text for the randomly selected move calls
    '''
    
    while True:
        try:
            mode = int(input('Select training mode:\n\n1. Specialized\t\t2. BLITZ\n'))
            if mode not in [1, 2]:
                print('Input a valid choice')
            else: 
                break
        except ValueError:
            pass

    if mode == 1:   # If Specialized training mode was chosen
        moves_list = selections.finalized_selection()

        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        voices = engine.getProperty('voices')
        engine.setProperty('rate', rate-30)
        engine.setProperty('voice', voices[14].id)
        engine.say('Loading training simulation')
        engine.runAndWait()

        i = 0
        while i < 7:  
            if i > 0:
                engine.say('Reset.')
                engine.runAndWait()

            time.sleep(5)
            engine.say(random.choice(moves_list))
            engine.runAndWait()
       
            time.sleep(11)
            i += 1
       
        engine.say('Training simulation complete.')
        engine.runAndWait()

    elif mode == 2:   # If BLITZ training mode was chosen
        blitz_list = blitz_mode.finalized_blitz()

        blitz_encouragement = ['Focus',
                            'This is where you are right now, focus your attention here', 
                            'Success is a few simple disciplines practiced every day',
                            'He who waits receives nothing',
                            'Again',
                            'Build yourself',
                            'Push harder',
                            'Make yourself a weapon',
                            'No half-assing here',
                            'I know you got more in you, prove it']

        engine = pyttsx3.init()
        rate = engine.getProperty('rate')
        voices = engine.getProperty('voices')
        engine.setProperty('rate', rate-25)
        engine.setProperty('voice', voices[14].id)
        engine.say('BLITZ MODE ENGAGED')
        engine.runAndWait()
        time.sleep(5)

        i = 0
        while True:   # Will intentionally loop forever until user enters "ctrl+c" to exit out of program
            engine.say(random.choice(blitz_list))
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

       

if __name__ == '__main__':
    main()