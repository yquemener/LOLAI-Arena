#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 

# ------------------------------
# Classes
# ------------------------------ 

class Bot(object):
    """ Bot class """
    def __init__(self, name):
        """ Initiate bot class

        @param name: the name of the bot (which correspond to the name of the folder)

        """
        self.check_name(name)
        
    def check_name(self, name):
        """Description of check_name
        Check if the name correspond to a folder containing program
    
        @param name
        
        """
        if not os.path.exists(BOTS_PATH+b):
            raise ValueError("Could not find bot '{bot}'".format(bot = b))
        else:
            self.bots.append(bot.Bot(b))

    def start_proc(self):
        """ Start the subprocess associated to the bot """
        self.proc = subprocess.Popen("./start", stdin=subprocess.PIPE, stdout=subprocess.PIPE,cwd=os.path.abspath(BOTS_PATH+self.bots[0]+"/")))

    def ready(self):
        """ Check if the bot is ready to play """
        if self.proc.stdout.readline()!="OK\n":
            raise ValueError("Le bot {bot} n'arrive pas à ce préparer".format(bot = self.name))

    def steady(self):
        """ Annonce the beggining of the round """
        self.proc.stdin.write("A\n")

    def end_game(self):
        """ Annonce the end of the game """
        self.proc.stdin.write("Q\n")

    def get_ans(self):
        """ Get the answer of the bot """
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

