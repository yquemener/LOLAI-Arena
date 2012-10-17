#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 

# ------------------------------
# Classes
# ------------------------------ 

class Bot(object):
    """Classe représentant un bot"""
    def __init__(self, name):
        self.name = name
        
    def start_proc(self):
        """Démmare le processus asocié à ce bot"""
        self.proc = subprocess.Popen("./start", stdin=subprocess.PIPE, stdout=subprocess.PIPE,cwd=os.path.abspath(BOTS_PATH+self.bots[0]+"/")))

    def pres(self):
        """Lance le message pour dire au bot de se préparer"""
        if self.proc.stdout.readline()!="OK\n":
            raise ValueError("Le bot {bot} n'arrive pas à ce préparer".format(bot = self.name))

    def feu(self):
        """ Anonce le début du match"""
        self.proc.stdin.write("A\n")

    def stop(self):
        """Anonce la fin du match"""
        self.proc.stdin.write("Q\n")

    def get_ans(self):
        """Récupère la réponse du bot"""
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

