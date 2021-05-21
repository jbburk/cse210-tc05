import random

class Console:
    """A code template for a computer console. The responsibility of this 
    class of objects is to get text or numerical input and display text output.
    
    Stereotype:
        Service Provider, Interfacer

    Attributes:
        prompt (string): The prompt to display on each line.
    """
    def __init__(self):
        pass
        

    def guess(self, guess_result):
        print(guess_result)

    def display_word(self, word):
        self.hidden_word_line = ""
        for i in word:
            self.hidden_word_line += i + " "
        print(self.hidden_word_line)      

    def read(self, prompt):
        return input(prompt)
        
        """Gets text input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            string: The user's input as text.
        """
        
        

    def read_number(self, prompt):
        return float(input(prompt))
        
        """Gets numerical input from the user through the screen.

        Args: 
            self (Screen): An instance of Screen.
            prompt (string): The prompt to display to the user.

        Returns:
            float: The user's input as a float.
        """
        
        
    def write(self, text):
        print(text)
        
        """Displays the given text on the screen. 

        Args: 
            self (Screen): An instance of Screen.
            text (string): The text to display.
        """