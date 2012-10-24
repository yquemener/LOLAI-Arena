#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 

import os

# ------------------------------
# Classes
# ------------------------------ 

GAMES_PATH = "Games/"
BOTS_PATH = "bots/"
ROUND_TIMEOUT = 0.01

class Arena():
    """ Docstring for Arena
    
    Arena links bots and games to make them play together

    """
    def __init__(self):
        """ Initiate Arena """
        self.get_games()
        

    def get_games(self):
        """ Docstring for get_games
        
        list of avialable games and search bots associated
        
        """
        self.games = {}
        for game in os.listdir(GAMES_PATH):
            self.games[game] = {}
            self.get_bots(game)
            self.get_info(game)

    def get_bots(self, game_name):
        """ Docstring of get_bots
        List bot associated to the game
    
        @param game_name: the name of the game
        
        """
        if not os.path.exists(GAMES_PATH + game_name):
            raise ValueError("Could not find the game at '{game}'".format(game = GAMES_PATH + game_name))
        else:
            self.games[game_name]["bots"] = []
            for bot in os.listdir(GAMES_PATH + game_name + "/" + BOTS_PATH):
                self.games[game_name]["bots"] += [bot]

    def get_info(self, game_name):
        """ Docstring of get_info
        Get requiered informations on the game
    
        @param game_name: the name of the game
        
        """
        # Importing the game 
        game_mod = __import__(game_name.lower())
        Game = getattr(game_mod, game_name)

        # updating information on the game
        self.games[game_name].update(Game.requiered_info())

    def play_game(self, game_name, bots, **args):
        """ Docstring of play_game
        Play the game between bots
    
        @param game: the game to play
        @param bots: bots which are going to play
        @param **args: dictionnary of paramter to give to the game
        
        """
        # Importing the game 
        game_mod = __import__(game_name.lower())
        Game = getattr(game_mod, game_name)

        # Creating the game
        game = Game(bots, **args)
        game.start()
        game.join(ROUND_TIMEOUT*200)
        return game.give_results()

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

