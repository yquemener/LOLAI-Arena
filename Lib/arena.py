#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 

# ------------------------------
# Classes
# ------------------------------ 

GAMES_PATH = "Games/"
ROUND_TIMEOUT = 0.01

class Arena():
    """ Docstring for Arena
    
    Arena links bots and games to make them play together

    """
    def __init__(self, arg):
        """ Initiate Arena """
        super(Arena, self).__init__()
        self.arg = arg
        

    def get_games(self):
        """ Docstring for get_games
        
        list of avialable games and search bots associated
        
        """
        for game in os.listdir(GAMES_PATH):
            self.games[game] = []
            self.get_bots(game)

    def get_bots(self, game_name):
        """ Docstring of get_bots
        List bot associated to the game
    
        @param game_name: the name of the game
        
        """
        if not os.path.exists(GAMES_PATH + game_name):
            raise ValueError("Could not find the game at '{game}'".format(game = GAMES_PATH + game_name))
        else:
            for bot in os.listdir(GAMES_PATH + game_name + "/"):
                self.games[game_name] += [bot]

    def play_game(self, game_name, bots, **args):
        """ Docstring of play_game
        Play the game between bots
    
        @param game: the game to play
        @param bots: bots which are going to play
        @param **args: dictionnary of paramter to give to the game
        
        """
        try:
            game = eval(game_name)(bots, **args)
            game.start()
            game.join(ROUND_TIMEOUT*200)
            return game.give_results()
        except Exception, e:
            raise e

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

