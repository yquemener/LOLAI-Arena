#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 
from game import Game
from bot import Bot

from time import *

ROUND_TIMEOUT = 0.01

# ------------------------------
# Classes
# ------------------------------ 

class Calebasse(Game):
    NAME = "Calebasse"
    def __init__(self, bots):
        """ Initiate Calebasse 
        
        @param bots: list of bots

        """
        Game.__init__(self, Calebasse.NAME, bots)


    def ready_bots(self):
        """ 
        
        Send the ready message to bots and their id
        
        """
        # Classical ready message
        Game.ready_bots()

        # Their id
        for bot in self.bots:
            bot.send_msg(bot.id)
            if bot.get_ans() != "OK\n":
                raie ValueError("The bot {bot} isn't happy with his given id!".format(bot=bot.name))


    def run_game(self):
        """ run_game
        
        """

        # The game finish when there is only one player left
        while len([b for b in self.bots if b.pocket >0]) > 1:
            self.round()

        self.end()


    def det_winner(self):
        """ det_winner
        """
        if len([b for b in self.bots if b.pocket >0]) == 1:
            self.winner = [b for b in self.bots if b.pocket >0][0]
        else:
            raise ValueError("There is more than one player")

        

# ------------------------------
# Fonctions
# ------------------------------ 

# ------------------------------
# Bloc principal
# ------------------------------

if __name__ == '__main__':
    pass

# ------------------------------
# Fin du programme
# ------------------------------

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 

