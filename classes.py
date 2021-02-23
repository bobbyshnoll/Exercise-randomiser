class Exercise:
    def __init__(self):
        self.type = ''
        self.name = ''
        self.description = ''
        self.basereps = 0
        self.difficultyLevel = 0
        self.difficultyFactor = 0

    def __str__(self):
        return f'{self.name}\nType: {self.type}\nExercise: {self.name}\n{self.description}'
    
    def do_exercise(self):
        reps = self.basereps + self.difficultyLevel * self.difficultyFactor
        if self.type.lower() == 'reps':
            return f'Do {reps} reps of {self.name.lower()}'
        elif self.type.lower() == 'timed':
            return f'Do {reps} seconds of {self.name.lower()}'
        elif self.type.lower() == 'special':
            return f'{self.description}'

    def add_difficulty(self):
        self.difficultyLevel += 1

def new_ex():
    newEx = Exercise()
    newEx.name = str(input('Exercise name:\n'))
    newEx.type = str(input('Exercise type (reps or timed):\n'))
    
    ok = False
    while not ok:
        if newEx.type.lower() == 'reps':
            ok = True
            newEx.basereps = int(input('How many reps for beginners:\n'))
            newEx.difficultyFactor = int(input('How many reps should be added for every difficuly level increase?\n'))
        elif newEx.type.lower() == 'timed':
            ok = True
            newEx.basereps = int(input('How long for beginners (in seconds):\n'))
            newEx.difficultyFactor = int(input('How much time should be added for every difficuly level increase (in seconds)?\n'))
        elif newEx.type.lower() == 'special':
            ok = True
            newEx.basereps = int(input('How many?\n'))
            newEx.difficultyFactor = 0
        else:
            print('\nUnrecognized type, try again.\n')
            newEx.type = str(input('Exercise type (reps or timed):\n'))

    newEx.description = str(input('Describe the exercise:\n'))
    return newEx