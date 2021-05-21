import random
import os


class Word:
    """The responsibility of this class of objects is to get a word, 
    encrypt the word, and revel correct letters guessed
    
    Stereotype:
    
    Attributes:
    """
    def __init__(self):
        self.word = []
        self.hidden = []
        self.wrong_guesses = 0
        self.wrong_list =[]
        self.wordList = []
        self.word_file_location = os.getcwd() + "/cse210-tc05/jumper/game/words.txt"
        with open(self.word_file_location) as word_file:
            word_file_lines = word_file.readlines()
            for line in word_file_lines:
                line = line.strip("\n")
                self.wordList.append()


    def get_word(self):
        self.word = list(random.choice(self.wordList))
        
    def hide_word(self):
        for char in self.word:
            self.hidden.append("_ ")

    def check_guess(self, guess):
        if guess not in self.hidden:
            if guess in self.word:
                for i in range(0, len(self.word)):
                    if self.word[i] == guess:
                        self.hidden[i] = guess
                return "you got it"
            else:
                if guess in self.wrong_list:
                    return "You already guessed that"
                else:
                    self.wrong_guesses += 1
                    self.wrong_list.append(guess)
                    return "you suck"

        else:
            return "You've already guessed that"

    def check_game(self):
        if self.wrong_guesses == 5:
            print("Sorry, you suck")
            return "Loss"
        if "_ " not in self.hidden:
            print("Congrats, you got it")
            return "Win"
        
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