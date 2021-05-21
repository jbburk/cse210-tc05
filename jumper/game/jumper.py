import random

class Jumper:
    """The responsibility of this class of objects is to establish parachute 
    and remove lines from parachute with incorrect guesses.
    
    Stereotype:

    
    Attributes:
        
    """
    def __init__(self):
        self.parachuter = ["	 ___    ", "	/___\    ", "	\   /   ", "	 \ /   ", "	  0   ", "	 /|\  ", "	 / \   ", "    ^^^^^^^^^^^^^^"]

    def wrong_guess(self):
        self.parachuter.pop(0)

    def game_over(self):
        self.parachuter[0] = "	  X   "

    def display_para(self):
        print()
        for i in self.parachuter:
            print(i)
        


    """Code taken from the Solo Checkpoint Hunter.py to use as a reference

    def __init__(self):
        self.location = random.randint(1, 1000)
        self.distance = [0, 0] # start with two so get_message always works
    
    def get_message(self):
        message = "\nI'm hunting wabbits!"
        if self.distance[-1] == 0:
            message = "\nWhy, you wascally wabbit!"
        elif self.distance[-1] > self.distance[-2]:
            message = "\nShhh. Be vewy vewy quiet."
        elif self.distance[-1] < self.distance[-2]:
            message = "\nSay your pwayers, wabbit!"
        return message

    def move(self, location):
        distance = abs(self.location - location)
        self.distance.append(distance)
        self.location = location
    """