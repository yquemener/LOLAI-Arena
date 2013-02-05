#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 

import os
from challenge import Challenge

# ------------------------------
# Classes
# ------------------------------ 

GAMES_PATH = "Games/"
BOTS_PATH = "bots/"
ROUND_TIMEOUT = 0.01


class Arena():
    """Arena links bots and games to make them play together

    """
    def __init__(self):
        """ Initiate Arena 
        
        """
        self.get_games()
        

    def get_games(self):
        """Gets the list of avialable games and search bots associated
        
        """
        self.games = {}
        for game in os.listdir(GAMES_PATH):
            self.games[game] = {}
            self.get_bots(game)
            self.get_info(game)

    def get_bots(self, game_name):
        """Gets the bot list associated to the game
    
        @param game_name: the name of the game
        
        """
        if not os.path.exists(GAMES_PATH + game_name):
            raise ValueError("Could not find the game at '{game}'".format(game=GAMES_PATH + game_name))
        else:
            self.games[game_name]["bots"] = []
            for bot in os.listdir(GAMES_PATH + game_name + "/" + BOTS_PATH):
                self.games[game_name]["bots"] += [bot]

    def get_info(self, game_name):
        """Gets requiered informations on the game
    
        @param game_name: the name of the game
        
        """
        # Importing the game 
        game_mod = __import__(game_name.lower())
        Game = getattr(game_mod, game_name)

        # updating information on the game
        self.games[game_name].update(Game.requiered_info())

#TODO: if game_name required, it should be explicitly added to args, so it should
# be in first position or be initialized and checked. There should be a better way
# to write this
    def play_game(self, **args):
        """Plays the game between bots
    
        @param **args: dictionnary of parameters to give to the game. 
        Should contain the parameter "game_name" and parameters 
        containing the string "bot" (bots that will play).
        @return: results
        
        """
        # Extracting from info
        game_name = args.pop("game_name")
        bots = []
        for b in [b for b in args if "bot" in b]:
            bots += [args.pop(b)]

        # Importing the game 
        game_mod = __import__(game_name.lower())
        Game = getattr(game_mod, game_name)

        # Creating the game
        game = Game(bots, **args)
        game.start()
        game.join(ROUND_TIMEOUT * 200)
        return game.give_results()

    def play_challenge(self, **args):
        """ Ask to challenge to organised
    
        @param **args: Dictionnary of parameters the challenge.
        Should contain the parameter "game_name"
        @return: results
                
        """
        game_name = args.pop('game_name')
        if game_name in self.games:
            bots = self.games[game_name]['bots']
        else:
            raise ValueError("{game}: unknown game".format(game = game_name))

        challenge = Challenge(game_name, bots)
        try:
            chall_type = args.pop('chall_type')
        except KeyError:
            chall_type = 'championship'
        finally:
            if  chall_type in challenge.avialable_challenge:
                getattr(challenge, chall_type)(**args)
            else:
                raise ValueError('{chal} is an unknown challenge type'.format(chal = chall_type))

        return challenge.give_res_champ()

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

