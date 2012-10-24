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

class Bot(object):
    """ Bot class """
    def __init__(self, name, bots_path = BOTS_PATH):
        # Il faudra enlever BOTS_PATH!!!
        """ Initiate bot class

        @param name: the name of the bot (which correspond to the name of the folder)
        @param bots_path: path where bots are

        """
        self.check_name(name, path)
        self.score = 0
        
    def check_name(self, name, bots_path):
        """Description of check_name

        Check if the name correspond to a folder containing program
    
        @param name: the name of the bot (which correspond to the name of the folder)
        @param bots_path: path where bots are
        
        """
        if not os.path.exists(path+name):
            raise ValueError("Could not find bot '{bot}'".format(bot = bots_path + name))
        else:
            self.name = name
            self.path = bots_path + name + "/"


    def start_bot(self):
        """ Start the subprocess associated to the bot """
        self.proc = subprocess.Popen("./start", stdin=subprocess.PIPE,
                stdout=subprocess.PIPE,
                cwd=os.path.abspath(self.path))


    def ready(self):
        """ Check if the bot is ready to play """
        if self.proc.stdout.readline()!="OK\n":
            raise ValueError("Le bot {bot} n'arrive pas à ce préparer".format(bot = self.name))

    def steady(self):
        """ Annonce the beggining of the round """
        self.send_msg("A\n")

    def end_game(self):
        """ Annonce the end of the game """
        self.send_msg("Q\n")

    def send_msg(self, msg):
        """Description of send_msg
        
        Send message to the bot
    
        @param msg: the message to send
        
        """
        self.proc.stdin.write(msg)

    def get_ans(self):
        """ Get the answer of the bot """
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

