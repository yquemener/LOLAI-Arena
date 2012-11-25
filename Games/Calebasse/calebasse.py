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
    def __init__(self, arg):
        """ Initiate Calebasse """
        super(Calebasse, self).__init__()
        self.arg = arg
        

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

