from game.console import Console
from game.jumper import Jumper
from game.word import Word

class Director:
    """A code template for a person who directs the game. The responsibility of 
    this class of objects is to control the sequence of play.
    
    Stereotype:
        Controller

    Attributes:
        console (Console): An instance of the class of objects known as Console.
        keep_playing (boolean): Whether or not the game can continue.
        jumper (Jumper): An instance of the class of objects known as Jumper.
        word (Word): An instance of the class of objects known as Word.
    """

    def __init__(self):
        """The class constructor.
        
        Args:
            self (Director): an instance of Director.
        """
        self.console = Console()
        self.jumper = Jumper()
        self.keep_playing = True
        self.word = Word()
        
    def start_game(self):
        """Starts the game loop to control the sequence of play.
        
        Args:
            self (Director): an instance of Director.
        """
        while self.keep_playing:
            self.get_inputs()
            self.do_updates()
            self.do_outputs()

    def get_inputs(self):
        """Gets the inputs at the beginning of each round of play. In this case,
        that means moving the jumper to a new location.

        Args:
            self (Director): An instance of Director.
        """
        
        
    def do_updates(self):
        """Updates the important game information for each round of play. In 
        this case, that means the word watches the jumper.

        Args:
            self (Director): An instance of Director.
        """
        

    def do_outputs(self):
        """Outputs the important game information for each round of play. In 
        this case, that means the word provides a hint.

        Args:
            self (Director): An instance of Director.
        """
