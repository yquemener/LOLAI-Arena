#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 

# ------------------------------
# Classes
# ------------------------------ 

GAMES_PATH = "Games/"
BOTS_PATH = "bots/"

class Challenge():
    """ Challenge

    """
    def __init__(self, game, bots):
        """ Initiate Challenge
        
        @param game: the name of the game
        @param bots: list of bots

        """
        self.game = game
        self.bots = bots

    def championship(self, **args):
        """ 
        
        Championship organise a championship between bots. Which means that every body will play against everybdy
        
        @param **args: dictionnary of parameters to give to the game. 

        """
        # Importing the game 
        game_mod = __import__(self.game.lower())
        Game = getattr(game_mod, self.game)

        # Pour le moment on n'organise que des matchs 1v1 faudrait l'étendre aux jeux nvn
        self.scores = [[0]*len(self.bots)]*self.bots
        snd_bot_list = list(self.bots)
        for (i,bi) in enumerate(self.bots):
            for (j,bj) in enumerate(snd_bot_list):
                game = Game([bi,bj], **args)
                game.start()
                game.join(ROUND_TIMEOUT * 200)
                results = game.give_results()
                scores[i,j] = [b.score for b in results]
                scores[j,i] = score[i,j]

    def give_res_champ(self):
        """ 
        
        Give results of the championship
        
        """
        return self.score


        
        

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

