#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 

# ------------------------------
# Classes
# ------------------------------ 

class Game():
    """ Docstring for Game
    
   Meta-class which future games will herites. It defines main caractéristiques of games 

    """
    def __init__(self,name, folder):
        """ Initiate Game 
    
        @param name: Name of the game
        @param folder: folder where the game is
        
        """
        self.name = name
        self.folder = folder

    def import_bots(self):
        """ Docstring for import_bots
        
        Import bots which should be in self.folder/bots/
        
        """
        pass
        
    def send_bot(self, bot, msg):
        """ Docstring of send_bot
        
        Send to the bot a message
    
        @param bot: the bot (form?)
        @param msg: the message string
        
        """
        pass


    def get_ans(self, bot):
        """ Docstring of get_ans
        
        Get the answer of the bot
    
        @param bot: the bot
        
        """
        pass

    def main(self):
        """ Docstring for main
        
        Let the game going on
        
        """
        pass

    def start_bot(self):
        """ Docstring for start_bot
        
        Start bots
        
        """
        pass

    def ready_bot(self):
        """ Docstring for ready_bot
        
        Send the ready message to bots
        
        """
        pass

    def end_bot(self):
        """ Docstring for end_bot
        
        Send the end of the game message to bots
        
        """
        pass

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

