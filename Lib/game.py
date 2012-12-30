#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 
import threading
import os

from bot import Bot

# ------------------------------
# Classes
# ------------------------------ 

GAMES_PATH = "Games/"
BOTS_PATH = "bots/"

class Game(threading.Thread):
    """ Docstring for Game
    
   Meta-class which future games will herites. It defines main caractéristiques of games 

    """
    def __init__(self,name, bots):
        """ Initiate Game 
    
        @param name: Name of the game
        @param folder: folder where the game is
        
        """
        self.check_name(name)
        self.folder = GAMES_PATH + self.game_name
        self.import_bots(bots)
        print "__init__" + str(self.bots)

        threading.Thread.__init__(self)
        
    def run(self):
        """ Docstring for main
        
        Let the game going on
        (requiered by threading)
        
        """
        print "run",self.bots
        self.init_game()
        self.run_game()
        self.end_game()

    # -------------------
    # Main step of the game

    def init_game(self):
        """ Docstring for init_game
        
        Initialise game
        
        """
        print self.bots
        self.start_bots()
        self.ready_bots()

    def run_game(self):
        """ Docstring for run_game
        
        Run the game
        
        """
        pass    

    def end_game(self):
        """ Docstring for end_game
        
        End the game
        
        """
        self.end_bots()

        # Attention non déclaré pour le moment
        self.det_winner()

    # -------------------
    # Communication with bots

    def start_bots(self):
        """ Docstring for start_bots
        
        Start bots
        
        """
        print "self.bots = "+str(self.bots)
        for bot in self.bots:
            print bot
            bot.start_bot()

    def ready_bots(self):
        """ Docstring for ready_bots
        
        Send the ready message to bots
        
        """
        for bot in self.bots:
            bot.ready()

    def end_bots(self):
        """ Docstring for end_bots
        
        Send the end of the game message to bots
        
        """
        for bot in self.bots:
            bot.send_msg("Q\n")
        
    # -------------------
    # Description of the game

    @classmethod
    def requiered_info(self):
        """ Docstring for requiered_info
        
        Return requiered informations for the game such number of players, number of rounds....
        
        """
        return {"players":2}

    @classmethod
    def rules(self):
        """ Docstring for rules
        
        Return the rules of the game
        
        """
        pass

    # -------------------
    # Other methods

    def check_name(self, name):
        """ Docstring of check_name
        
        Check if the name correspond to a folder containing the game
        And set name, path and bots_path
    
        @param name: name of the game
        
        """
        if not os.path.exists(GAMES_PATH + name):
            raise ValueError("Could not find the game at '{game}'".format(game = GAMES_PATH + name))
        else:
            # We can't call this attribute name because of threading
            self.game_name = name
            self.path = GAMES_PATH + self.game_name + "/"
            self.bots_path = self.path + BOTS_PATH

    def import_bots(self, bots):
        """ Docstring for import_bots
        
        Import bots which should be in self.bots_path

        @param bots: list of games name
        
        """
        self.bots = [] 
        for b in bots:
            self.bots += [Bot(b, self.bots_path)]
    def det_winner(self):
        """ Docstring for det_winner
        
        Choose the winner
        
        """
        pass

# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    pass


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

