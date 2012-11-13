#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 
import os
import subprocess


# ------------------------------
# Classes
# ------------------------------ 
BOTS_PATH = "Games/Prisonnier/bots/"
#TODO: Il faudra enlever BOTS_PATH!!!
        

class Bot(object):
    """Bot class
    
    """
    def __init__(self, name, bots_path=BOTS_PATH):
        """Initiates bot class

        @param name: the name of the bot (which correspond to the name of the folder)
        @param bots_path: path where bots are

        """
        self.check_name(name, bots_path)
        self.score = 0
        
    def check_name(self, name, bots_path):
        """Checks if the name correspond to a folder containing program
    
        @param name: the name of the bot (which correspond to the name of the folder)
        @param bots_path: path where bots are
        
        """
        if not os.path.exists(bots_path + name):
            raise ValueError("Could not find bot '{bot}'".format(bot=bots_path + name))
        else:
            self.name = name
            self.path = bots_path + name + os.sep

    def start_bot(self):
        """Starts the subprocess associated to the bot 
        
        """
        self.proc = subprocess.Popen("./start", stdin=subprocess.PIPE,
									 stdout=subprocess.PIPE,
									 cwd=os.path.abspath(self.path))

    def ready(self):
        """Checks if the bot is ready to play or raise an error.
        
        """
        if self.proc.stdout.readline() != "OK\n":
            raise ValueError("Le bot {bot} n'arrive pas à se préparer".format(bot=self.name))

    def send_msg(self, msg):
        """Sends message to the bot
    
        @param msg: the message to send
        
        """
        self.proc.stdin.write(msg)

#TODO: rename get_ans to get_answer!!!
    def get_ans(self):
        """Gets the answer of the bot
        
        @return: the bot's answer
        
        """
        return self.proc.stdout.readline().rstrip()


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

