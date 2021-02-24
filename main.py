import random
import pickle
import time

from classes import Exercise, countdown


with open('exercise_list.txt', 'rb') as f:
    exerciseDict = pickle.load(f)

currentExercise = random.choice(list(exerciseDict.values()))
snoozeNb = 0
running = True

while running:
    print()
    print(currentExercise.do_exercise(), '\n')
    time.sleep(1)
    action = input('Press enter to snooze for 15 mins.\n'
                   'Type "h" for help with the exercise.\n'
                   'Type "ok" if you did the exercise.\n').lower()

    if action == '' and snoozeNb < 3:
        snoozeNb += 1
        print(f'Snooze {snoozeNb}/3.')
        currentExercise.difficultyLevel += 1
        countdown(2)

    elif action == '' and snoozeNb == 3:
        print('No more snoozing! Do the exercise now!')
        currentExercise.difficultyLevel += 1
        print(currentExercise.do_exercise(), '\n')
        input('Press enter when you have done the exercise.')
        running = False

    elif action == 'h':
        print(currentExercise.description)
        time.sleep(3)

    else:
        print('Good job!')
        time.sleep(2)
        running = False
