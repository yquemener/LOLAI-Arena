#!/usr/bin/env python2
#-*- coding:utf8-*-
    
import threading
import bot

from time import *
from games.Prisoner import Prisoner

ROUND_TIMEOUT = 0.01


class Match(threading.Thread):
    def __init__(self, bots, game = Prisoner(), round = 50):
        """ Initialization of the game

        @param bots: list of bots
        @param round: number of round

        """

        self.import_bots(bots)
        self.round = round
        self.scores = [0]*len(bots)
        self.error=0
        self.game = game
        threading.Thread.__init__(self)

    def import_bots(self, bots):
        """Description of import_bots
        Check if bot's name correspond to files

        @param bots: list of bots

        """
        self.bots = list()
        for b in bots:
            self.bots.append(bot.Bot(b))

    def start_bots(self):
        """Description of start_bots

        Start subprocess associated to bots
    
        """
        for b in self.bots:
            b.start_bot()

    def ready(self):
        """Description of ready

        Check if bots are ready
    
        """
        for b in self.bots:
            b.ready()

    def steady(self):
        """Description of steady

        Send to bots the new round message
    
        """
        for b in self.bots:
            b.steady()

    def end_game(self):
        """Description of end_game
    
        Send end of game message to bots
        
        """
        for b in self.bots:
            b.end_game()

    def go(self):
        """Description of go

        Rules of the game
    
        """
        # Reading bots choices
        orders = {
                0:self.bots[0].get_ans(),
                1:self.bots[1].get_ans()}

        ans = self.game.oneRound(orders)

        # Send results to other bots
        self.bots[0].send_msg(ans[0]+'\n')
        self.bots[1].send_msg(ans[1]+'\n')

    def run(self):
        """ Process of the game """
        self.start_bots()

        self.ready()

        # loop rounds
        for k in range(self.round):
            # Send to bots steady message
            self.steady()
            # Rules of the game
            self.go()

        # End game message
        self.end_game()

        self.det_winner()

    def det_winner(self):
        """ Choose the winner """
        # On doit pouvoir faire mieux pour récuperer l'index du gagnant avec un l.index(max(l)).
        # Mais ya un soucis avec le cas d'égalité
        sc=self.game.getWorldState()['scores']
        if (sc[1]>sc[0]):
            self.winner = "{winner} wins!".format(winner = self.bots[1].name)
        elif (sc[1] < sc[0]):
            self.winner = "{winner} wins!".format(winner = self.bots[0].name)
        else:
            self.winner = "Draw"

    def give_results(self):
        """ Give the sum up of the game"""
        self.det_winner()
        return {'bots' : self.bots, 
                'winner' : self.winner, 
                'scores': self.game.getWorldState()['scores']}


# ----------------------
# What is run in this file

if __name__ == '__main__':

    import sys

    bots = ["AlwaysT", "AlwaysC", "Random", "Imitator", "IvBot"]
    contender=None
    if len(sys.argv)>1:
        if sys.argv[1] in bots:
            contender = sys.argv[1]

    for b1 in bots:
        if contender!=None and b1!=contender: continue
        for b2 in bots:
            match = Match([b1,b2])
            match.start()
            match.join(ROUND_TIMEOUT*200)
            if match.isAlive():
                print "Failed to answer in time"
            else:
                match.det_winner()
                print "{b1} vs {b2}: score {scores} : {winner}".format(b1 = b1, b2 = b2, scores = match.give_results()['scores'], winner=match.winner)
