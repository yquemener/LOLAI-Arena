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
    HIST_ATTR = ["account", "bet"]
    def __init__(self, bots, hist_attr = HIST_ATTR):
        """ Initiate Calebasse 
        
        @param bots: list of bots name (str)
        @param hist_attr: list of attributes with history 

        """
        Game.__init__(self, Calebasse.NAME, bots,hist_attr )
        

        # Initial "money" (100 is arbitrary)
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
            bot.send_msg(bot.uuid)
            if bot.get_ans() != "OK":
                raise ValueError("The bot {bot} isn't happy with his given uuid!".format(bot=bot.name))

    def run_game(self):
        """ run_game
        
        """
        # The game finish when there is only one player left
        while len([b for b in self.bots if b.account > 0]) > 1:
            self.steady_bots()
            self.round()

        self.end_game()

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
        bets_pattern = """(\d+)""" # Why do we use parenthesis?
        for b in self.bots:
            # While the bet of the player is not possible, Calebasse ask it again
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
                    b.bet = 0
                else:
                    b.bet = int(res.group())
                # Can't more than you have
                wait_for_good_bet = 1 - (b.bet <= b.account)
            # # Storing bets
            # bets[b.uuid] = bet
            # # takeoff the bet from his account
            # b.account -= bet
            b.send_msg("Accepted")

        # Bets values
        bets = {b.uuid:b.bet for b in self.bots}
        # Cash price
        price = sum([b.bet for b in self.bots])
        # Drawing
        choice = int((1+price) * random.random())
        # print "---------------------"
        # print "Price: {price} \t choice = {choice}".format(price = price, choice = choice)
        winner = 0
        start = 0
        for b in self.bots:
            start += b.bet
            # print "{name} ({uuid}), start {start}".format(name = b.name, uuid = b.uuid[:5], start = start)
            if (choice <= start) and not(winner):
                b.account += price - b.bet
                winner = b
            else:
                b.account -= b.bet

        # Sending everything to bots
        for b in self.bots:
            b.send_msg(json.dumps(bets))
            b.send_msg(winner.uuid)

        # print "Winner: {name} ({uuid})".format(name = winner.name, uuid = winner.uuid[:5])
        

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

        plot_accounts = {"name": "Accounts", "from_bots": "account"}
        plot_bets= {"name": "Bets", "from_bots": "bet"}

        winner = "The winner is {win}".format(win = self.winner.name)

        return {'game_name' : self.NAME, 'bots': self.bots, "comments" : [winner], "attributes" : [], "plots" : [plot_accounts, plot_bets]}

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

