import random
import pickle
import time

from classes import Exercise


with open('exercise_list.txt', 'rb') as f:
    exerciseDict = pickle.load(f)

currentExercise = random.choice(list(exerciseDict.values()))
print(currentExercise.do_exercise())

snoozeNb = 0

running = True
while running:
    if snoozeNb == 0:
        snooze = input('Snooze for 15 mins? (y/n)\n')
    elif snoozeNb < 4:
        snooze = input('Snooze again for 15 mins? (y/n)\n')
    else:
        print('No more snoozing!')
        print(currentExercise.do_exercise())
        input('Type anything and press enter when you are done.')
    if snooze.lower() == 'y':
        snoozeNb += 1
        currentExercise.difficultyLevel += 1
        t = 900
        while t:
            mins = t // 60
            secs = t % 60
            print(f'{mins:02}:{secs:02} remaining.', end='\r')
            time.sleep(1)
            t -= 1
        print("\nTime's up!")
        print(currentExercise.do_exercise())
        snooze = ''
    else:
        print('Good job!')
        time.sleep(2)
        running = False
