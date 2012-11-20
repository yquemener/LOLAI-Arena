#!/usr/bin/env python2
#-*- coding:utf8-*-
    
from game import Game
from bot import Bot

from time import *

ROUND_TIMEOUT = 0.01


class Market(Game):
    NAME = "Market"
    def __init__(self, bots, round=3000):
        """Initialization of the market game

        @param bots: list of bots
        @param round: number of round

        """
        Game.__init__(self, Market.NAME, bots)
        self.round = int(round)

    def steady_bots(self):
        """Sends to bots the new round message
    
        """
        for b in self.bots:
            b.send_msg("A\n")

    # -------------------
    # Main step of the game

    def run_game(self):
        """ Process of the game 
        
        """
        for k in range(self.round):
            # Send to bots steady message
            self.steady_bots()
            # Rules of the game
            self.go()

    def go(self):
        """Rules of the game
    
        """
        # Reading bots choices
        r1 = self.bots[0].get_ans()
        r2 = self.bots[1].get_ans()

        # Send results to other bots
        self.bots[0].send_msg(r2 + '\n')
        self.bots[1].send_msg(r1 + '\n')


    def det_winner(self):
        """ Choose the winner 
        
        """

    def give_results(self):
        """Give the sum up of the gam
        
        @return: the bots and the winner
        @rtype: dictionary
        
        """
        self.det_winner()
        return {'bots': self.bots, 'winner': self.winner}


# ----------------------
# What is run in this file

if __name__ == '__main__':

    pass

