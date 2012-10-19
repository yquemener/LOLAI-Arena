#!/usr/bin/env python2
#-*- coding:utf8-*-
    
import threading
from bot import Bot

from time import *

ROUND_TIMEOUT = 0.01


class Prisonnier(threading.Thread):
    def __init__(self, bots, round = 50):
        """ Initialization of the prisonnier

        @param bots: list of bots
        @param round: number of round

        """

        self.import_bots(bots)
        self.round = round
        self.error=0
        threading.Thread.__init__(self)

    def import_bots(self, bots):
        """Description of import_bots
        Check if bot's name correspond to files

        @param bots: list of bots

        """
        self.bots = list()
        for b in bots:
            self.bots.append(Bot(b))

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
        r1 = self.bots[0].get_ans()
        r2 = self.bots[1].get_ans()

        # Who wins
        if r1=="C" and r2=="C":
            self.bots[0].score+=5
            self.bots[1].score+=5
        elif r1=="C" and r2=="T":
            self.bots[0].score+=0
            self.bots[1].score+=10
        elif r1=="T" and r2=="C":
            self.bots[0].score+=10
            self.bots[1].score+=0
        elif r1=="T" and r2=="T":
            self.bots[0].score+=1
            self.bots[1].score+=1
        else:
            raise ValueError("Your answer doesn't correspond to the game:  r1= {r1}, r2 = {r2}".format(r1 = r1, r2 = r2))

        # Send results to other bots
        self.bots[0].send_msg(r2+'\n')
        self.bots[1].send_msg(r1+'\n')

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
        if (self.bots[1].score > self.bots[0].score):
            self.winner = "{winner} wins!".format(winner = self.bots[1].name)
        elif (self.bots[1].score < self.bots[0].score):
            self.winner = "{winner} wins!".format(winner = self.bots[0].name)
        else:
            self.winner = "Draw"

    def give_results(self):
        """ Give the sum up of the game"""
        self.det_winner()
        return {'bots' : self.bots, 'winner' : self.winner}


# ----------------------
# What is run in this file

if __name__ == '__main__':

    bots = ["AlwaysT", "AlwaysC", "Random"]
    #bots = ["Random"]
    c1 = bots[0]
    c2 = bots[1]

    for b1 in bots:
        for b2 in bots:
            prisonnier = Prisonnier([b1,b2])
            prisonnier.start()
            prisonnier.join(ROUND_TIMEOUT*200)
            if prisonnier.isAlive():
                print "Failed to answer in time"
            else:
                print "{b1} vs {b2}: score {scores}".format(b1 = b1, b2 = b2, scores = str(prisonnier.scores))
                prisonnier.det_winner()
                print prisonnier.winner


