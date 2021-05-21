import random

class Word:
    """The responsibility of this class of objects is to get a word, 
    encrypt the word, and revel correct letters guessed
    
    Stereotype:
    
    Attributes:
    """
    def __init__(self):
        self.word



    """Code taken from Solo Checkpoint Rabbit.py to use as a reference
    def __init__(self):
        self.location = random.randint(1, 1000)
        self.distance = [0, 0] # start with two so get_hint always works
    
    def get_hint(self):
        hint = "(-.-) Maybe I'll take a nap."
        if self.distance[-1] == 0:
            hint = "(;.;) You found me!"
        elif self.distance[-1] > self.distance[-2]:
            hint = "(^.^) Getting colder!"
        elif self.distance[-1] < self.distance[-2]:
            hint = "(>.<) Getting warmer!"
        return hint
        
    def watch(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)
    """