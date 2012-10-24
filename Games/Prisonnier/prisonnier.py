#!/usr/bin/env python2
#-*- coding:utf8-*-
    
from game import Game
from bot import Bot

from time import *

ROUND_TIMEOUT = 0.01


class Prisonnier(Game):
    NAME = "Prisonnier"
    def __init__(self, bots, round = 50):
        """ Initialization of the prisonnier

        @param bots: list of bots
        @param round: number of round

        """

        Game.__init__(self, Prisonnier.NAME, bots)
        self.round = round

    def steady_bots(self):
        """Description of steady_bots

        Send to bots the new round message
    
        """
        for b in self.bots:
            b.send_msg("A\n")

    # -------------------
    # Main step of the game - adapted to prisonnier

    def run_game(self):
        """ Process of the game """
        for k in range(self.round):
            # Send to bots steady message
            self.steady_bots()
            # Rules of the game
            self.go()

    def go(self):
        """Description of go

        Rules of the game
    
        """
        # Reading bots choices
        r1 = self.bots[0].get_ans()
        r2 = self.bots[1].get_ans()

        # Distribute points
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

    pass

