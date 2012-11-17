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
ROUND_TIMEOUT = 0.01

class Challenge():
    """ Challenge

    """

    avialable_challenge = ['championship']

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
        # Reste le soucis de comment stocker le score des matches mirors?
        self.scores = [[0 for k in self.bots] for j in self.bots]
        snd_bot_list = list(self.bots)
        for (i,bi) in enumerate(self.bots):
            for (j,bj) in enumerate(snd_bot_list):
                game = Game([bi,bj], **args)
                game.start()
                game.join(ROUND_TIMEOUT * 200)
                results = game.give_results()
                self.scores[i][j+i] = (results['bots'][0].score, results['bots'][1].score)
                # here we write i+j because each time we remove one item in snd_bot_list
                self.scores[j+i][i] = (results['bots'][1].score, results['bots'][0].score)
            snd_bot_list.remove(bi)

    def give_res_champ(self):
        """ 
        
        Give results of the championship
        
        """
        return {'bots': self.bots, 'scores':self.scores}


        
        

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

