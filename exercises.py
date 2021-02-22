class Exercises:
    def __init__(self):
        self.type = ''
        self.name = ''
        self.description = ''
        self.difficulty = ""

    def __str__(self):
        return f'Type: {self.type}\nExercise: {self.name}\n{self.description}'
    
    def do_exercise(self):
        return f'Do {self.difficulty} of {self.name}'