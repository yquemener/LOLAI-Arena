#!/usr/bin/env python
#-*- coding:utf8-*-

# ------------------------------
# Imports
# ------------------------------ 
from game import Game
from bot import Bot
import sys
import random

from time import *
import json
import re

ROUND_TIMEOUT = 0.01

# ------------------------------
# Classes
# ------------------------------ 

class Calebasse(Game):
    NAME = "Calebasse"
    def __init__(self, bots):
        """ Initiate Calebasse 
        
        @param bots: list of bots name (str)

        """
        Game.__init__(self, Calebasse.NAME, bots)
        

        # Initial "money" (100 est arbitraire pour le moment)
        for b in self.bots:
            b.account = 100


    def ready_bots(self):
        """ 
        
        Send the ready message to bots and their uuid
        
        """
        # Classical ready message
        Game.ready_bots(self)

        # Their uuid
        for bot in self.bots:
            bot.send_msg(bot.uuid+"\n")
            if bot.get_ans() != "OK":
                raise ValueError("The bot {bot} isn't happy with his given uuid!".format(bot=bot.name))

    def run_game(self):
        """ run_game
        
        """
        # The game finish when there is only one player left
        while len([b for b in self.bots if b.account >0]) > 1:
            self.steady_bots()
            self.round()

        self.end()

    def steady_bots(self):
        """Sends to bots the new round message
    
        """
        for b in self.bots:
            b.send_msg("A")

    def round(self ):
        """ On round of the game
        
        """
        acounts = self.get_accounts()
        # Bets of players
        bets = {}
        bets_pattern = """(\d+)"""
        for b in self.bots:
            wait_for_good_bet = 1
            while wait_for_good_bet:
                # Sending accounts
                b.send_msg(json.dumps(acounts))
                # Wait fot bet
                b.send_msg("bet?")
                res = b.get_ans()
                # Analyse answer
                res = re.search(bets_pattern, res)
                if res==None:
                    bet = 0
                else:
                    bet = int(res.group())
                # Can't more than you have
                wait_for_good_bet = 1 - (bet <= b.account)
            # Storing bets
            bets[b.uuid] = bet
            # takeoff the bet from his account
            b.account -= bet
            b.send_msg("Accepted")

        # Drawing
        print "bets.values =", bets.values()
        choice = int((1+sum(bets.values())) * random.random())
        start = 0
        for uuid in bets.keys():
            start += bets[uuid]
            print start, choice
            if choice <= start:
                winner = [b for b in  self.bots if b.uuid==uuid][0]
                break
        
        # Rewarding the winner
        winner.account += sum(bets.values())

        # Sending everything to bots
        for b in self.bots:
            b.send_msg(json.dumps(bets))
            b.send_msg(winner.uuid)
        

    def det_winner(self):
        """ det_winner
        """
        if len([b for b in self.bots if b.account >0]) == 1:
            self.winner = [b for b in self.bots if b.account >0][0]
        else:
            raise ValueError("There is more than one player left")


    def give_results(self):
        """Give the sum up of the gam
        
        @return: the bots and the winner
        @rtype: dictionary
        
        """
        self.det_winner()
        return {'bots': self.bots, 'winner': self.winner}

    # --------------------------
    # Few getters
    # --------------------------

    def get_accounts(self):
        """ Return a dictionnary of bot's account
        """
        return {b.uuid:b.account for b in self.bots}

    # -------------------
    # Description of the game

    @classmethod
    def requiered_info(self):
        """Gets requiered informations for the game such as
        number of players, number of rounds....
        
        @return: number of players and of rounds
        @rtype: dictionary
        
        """
        return {"players": 2}

    @classmethod
    def rules(self):
        """Gets the rules of the game
        
        """
        pass
        


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

