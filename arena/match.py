#!/usr/bin/env python2
#-*- coding:utf8-*-
    
import os
import threading
import subprocess

from time import *

BOTS_PATH = "../bots/"
ROUND_TIMEOUT = 0.01


class Match(threading.Thread):
    def __init__(self, bots, round = 50):
        """ Initialization of the game

        @param bots: list of bots
        @param round: number of round

        """

        self.import_bots(bots)
        self.round = round
        self.scores = [0]*len(bots)
        self.error=0
        threading.Thread.__init__(self)

    def import_bots(self, bots):
        """Description of import_bots
        Check if bot's name correspond to files

        @param bots: list of bots

        """
        self.bots = list()
        for b in bots:
            if not os.path.exists(BOTS_PATH+b):
                raise ValueError("Could not find bot '{bot}'".format(bot = b))
            else:
                self.bots.append(bot.Bot(b))

    def ready(self):
        """Description of ready

        Check if bots are ready
    
        """
        if self.p[0].stdout.readline()!="OK\n":
            # Pas très joli tout ça!
            # Faut changer le nom de l'erreur
            # et géré le cas où il y aura plus de joueurs
            # ça sera mieux fait quand la classe bot sera en place
            raise ValueError("{bot} can't be initialised".format(bot = self.bots[0]))
        if self.p[1].stdout.readline()!="OK\n":
            raise ValueError("{bot} can't be initialised".format(bot = self.bots[1]))

    def steady(self):
        """Description of steady

        Send to bots starting message
    
        """
        self.p[0].stdin.write("A\n")
        self.p[1].stdin.write("A\n")

    def go(self):
        """Description of go

        Rules of the game
    
        """
        # Reading bots choices
        r1 = self.p[0].stdout.readline().rstrip()
        r2 = self.p[1].stdout.readline().rstrip()

        # Who wins
        if r1=="C" and r2=="C":
            self.scores[0]+=5
            self.scores[1]+=5
        elif r1=="C" and r2=="T":
            self.scores[0]+=0
            self.scores[1]+=10
        elif r1=="T" and r2=="C":
            self.scores[0]+=10
            self.scores[1]+=0
        elif r1=="T" and r2=="T":
            self.scores[0]+=1
            self.scores[1]+=1
        else:
            raise ValueError("Your answer doesn't correspond to the game:  r1= {r1}, r2 = {r2}".format(r1 = r1, r2 = r2))

        # Send results to other bots
        self.p[0].stdin.write(r2+'\n')
        self.p[1].stdin.write(r1+'\n')

    def run(self):
        """ Process of the game """
        self.p = list()

        self.p.append(subprocess.Popen("./start", stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         cwd=os.path.abspath(BOTS_PATH+self.bots[0]+"/")))
        self.p.append(subprocess.Popen("./start", stdin=subprocess.PIPE,
                                         stdout=subprocess.PIPE,
                                         cwd=os.path.abspath(BOTS_PATH+self.bots[1]+"/")))
        self.ready()

        # loop rounds
        for k in range(self.round):
            # Send to bots steady message
            self.steady()
            # Rules of the game
            self.go()

        # End game message
        self.p[0].stdin.write("Q\n")
        self.p[1].stdin.write("Q\n")

        self.det_winner()

    def det_winner(self):
        """ Choose the winner """
        # On doit pouvoir faire mieux pour récuperer l'index du gagnant avec un l.index(max(l)).
        # Mais ya un soucis avec le cas d'égalité
        if(self.scores[1]>self.scores[0]):
            self.winner = "{winner} wins!".format(winner = self.bots[1])
        elif(self.scores[1]<self.scores[0]):
            self.winner = "{winner} wins!".format(winner = self.bots[0])
        else:
            self.winner = "Draw"

    def give_results(self):
        """ Give the sum up of the game"""
        self.det_winner()
        return {'bots' : self.bots, 'scores' : self.scores, 'winner' : self.winner}


# ----------------------
# What is run in this file

if __name__ == '__main__':

    bots = ["AlwaysT", "AlwaysC", "Random"]
    #bots = ["Random"]
    c1 = bots[0]
    c2 = bots[1]

    for b1 in bots:
        for b2 in bots:
            match = Match([b1,b2])
            match.start()
            match.join(ROUND_TIMEOUT*200)
            if match.isAlive():
                print "Failed to answer in time"
            else:
                print "{b1} vs {b2}: score {scores}".format(b1 = b1, b2 = b2, scores = str(match.scores))
                match.det_winner()
                print match.winner


