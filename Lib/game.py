#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 
import threading
from bot import Bot

# ------------------------------
# Classes
# ------------------------------ 

GAMES_PATH = "Games/"
GAMES_PATH = "bots/"

class Game(threading.Thread):
    """ Docstring for Game
    
   Meta-class which future games will herites. It defines main caractéristiques of games 

    """
    def __init__(self,name):
        """ Initiate Game 
    
        @param name: Name of the game
        @param folder: folder where the game is
        
        """
        self.name = name
        self.folder = GAMES_PATH + self.name
        threading.Thread.__init__(self)

    def check_name(self, name):
        """ Docstring of check_name
        
        Check if the name correspond to a folder containing the game
    
        @param name: name of the game
        
        """
        if not os.path.exists(GAMES_PATH + name):
            raise ValueError("Could not find the game at '{game}'".format(game = GAMES_PATH + name))
        else:
            self.name = name
            self.path = GAMES_PATH + name + "/"
            self.bots_path = self.path + BOTS_PATH

    def import_bots(self, bots):
        """ Docstring for import_bots
        
        Import bots which should be in self.bots_path
        
        """
        self.bots = {} 
        for b in bots:
            self.bots[b] = Bot(b, self.bots)
        
    def main(self):
        """ Docstring for main
        
        Let the game going on
        
        """
        pass

    def det_winner(self):
        """ Docstring for det_winner
        
        Determine the winner
        
        """
        # Soucis! Tous les jeux ne se terminent pas de la même façon! Certain sont left to die et d'autres se jouent au score!
        pass

    # -------------------
    # Communication with bots

    def send_bot(self, bot, msg):
        """ Docstring of send_bot
        
        Send to the bot a message
    
        @param bot: the bot name
        @param msg: the message string
        
        """
        try:
            self.bots[bot].send(msg)
        except Exception, e:
            raise e

    def get_ans(self, bot):
        """ Docstring of get_ans
        
        Get the answer of the bot
    
        @param bot: the bot
        
        """
        try:
            self.bots[bot].get_ans()
        except Exception, e:
            raise e

    def start_bots(self):
        """ Docstring for start_bots
        
        Start bots
        
        """
        for bot in self.bots.values():
            bot.start_bot()

    def ready_bots(self):
        """ Docstring for ready_bots
        
        Send the ready message to bots
        
        """
        for bot in self.bots.values():
            bot.ready()

    def end_bots(self):
        """ Docstring for end_bots
        
        Send the end of the game message to bots
        
        """
        for bot in self.bots.values():
            bot.end_game()

# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    pass


# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

