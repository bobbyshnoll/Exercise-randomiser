""" 
Run this module to add or delete exercises in the exercise_list.txt file.
"""

import pickle
import time
from classes import (Exercise, new_ex)


exerciseDict = {}
with open('exercise_list.txt', 'rb') as f:
    exerciseDict = pickle.load(f)


running = True
while running:
    print('\nAvailable exercises:\n')
    for i in exerciseDict.keys():
        print(exerciseDict[i], '\n')
    
    time.sleep(2)

    action = input('\nWhat do you want to do?\nTo add a new exercise, type "add"\nTo delete an exercise, type "del"\nTo quit the exercise creator, type "q"\n')
    if action.lower() == 'add':
        newex = new_ex()
        exerciseDict[newex.name] = newex

    elif action.lower() == 'del':
        complete = False
        
        while not complete:
            print('\nHere is your exercise list:')
            for i in exerciseDict.keys():
                print(exerciseDict[i].name, end = " | ")
            toDel = input('\nWhich exercise do you want to delete?\n')
            if toDel not in exerciseDict.keys():
                print('Unrecognized exercise, try again.\n')
            elif exerciseDict[toDel].type == 'special':
                print('This one has to stay, darling!')
                time.sleep(2)
                complete = True
            else:
                print('\n\n\nAre you sure you want to delete this:\n')
                print(exerciseDict[toDel])
                if input('y/n\n').lower() == 'y':
                    del exerciseDict[toDel]
                    print(f'{toDel} has been deleted!')
                    time.sleep(2)
                else:
                    print("Ok then, we're keeping it!")
                    time.sleep(2)
                complete = True

    elif action.lower() == 'q':
        running = False

    else:
        print('Unrecognized command, try again.')
        time.sleep(2)


with open('exercise_list.txt', 'wb') as f:
    pickle.dump(exerciseDict, f)