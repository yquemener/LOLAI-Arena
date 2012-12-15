#!/usr/bin/env python2
#-*- coding:utf8-*-
    
from game import Game
from bot import Bot

from time import *

import json

ROUND_TIMEOUT = 0.01

class Player:
    def __init__(self, name):
        self.cash = 100
        self.farms = 0
        self.mills = 0
        self.wheat = 0
        self.flour = 0
        self.name = name

    def state(self):
        return [self.name, self.cash,
                self.wheat,
                self.flour,
                self.farms,
                self.mills]


class Market(Game):
    NAME = "Market"
    def __init__(self, bots, round=3000):
        """Initialization of the market game

        @param bots: list of bots
        @param round: number of round

        """
        Game.__init__(self, Market.NAME, bots)

        # Initialization of the constants of the game
        self.farm_price = 20
        self.mill_price = 85
        self.transformation_rate = 1.0
        self.growing_cycle = 100
        self.flour_bought_each_turn = 50
        self.farm_production = 1
        self.mill_transformation = 1

        # Initialization of the markets
        self.wheat_martket=list()
        self.flour_market=list()
        self.transactions_done=list()
        self.stats=list()

        self.round = int(round)
        self.players_state = dict()
        self.bots = dict()
        i = 0
        for b in bots:
            botname = b.name+str(i)
            self.bots[botname] = b
            self.players_state[botname]=Player(botname)
            i+=1

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
        # send its bot its identification
        for botname in self.bots.keys():
            self.bots[botname].send_msg(botname)

        for k in range(self.round):
            # Send to bots the state of the world 
            self.steady_bots()
            # Rules of the game
            self.go()

    def go(self):
        """Rules of the game
    
        """
        # Clear the markets
        self.flour_market = list()
        self.wheat_market = list()
        self.transactions_done=list()
        
        # Reading bots choices
        for bn in self.bots.keys():
            ans=json.loads(self.bots[bn].get_ans())
            for act in ans:
                if len(act)==3:
                    # farm/mill buy
                    if act[0]=="buy":
                        self.buy_facility(bn,act[1], act[2])
                    else:
                        self.sell_facility(bn,act[1], act[2])
                if len(act)==4:
                    # flour/wheat transaction
                    if act[1]=="flour":
                        self.flour_market.append(
                                [bn,act[0],act[2],act[3]])
                    else:
                        self.wheat_market.append(
                                [bn,act[0],act[2],act[3]])
        # Running the farms and the mills
        for bn in self.players_stat.keys():
            pl = self.players_state[bn]
            pl.wheat += pl.farms*self.farm_production
            transformed = min(pl.mills*self.mill_production, pl.wheat)
            pl.flour += transformed
            pl.wheat -= transformed

        # Running the markets

        # The flour market is easy
        self.flour_market.sort(key=lambda x:x[3])
        print self.flour_market
        tobuy = self.flour_bought_each_turn
        i=len(self.flour_market)-1
        while tobuy>0 and i>0:
            (bn, buysell; qty, price) = self.flour_market[i]
            if buysell=="sell":
                pl=self.players_stat[bn]
                if qty >= tobuy:
                    if pl.flour >= tobuy:
                        pl.flour-=tobuy
                        tobuy=0
                        pl.cash+=tobuy*price
                    else:
                        pl.cash+=pl.flour*price
                        tobuy-=pl.flour
                        pl.flour=0
                else:
                    if pl.flour>=qty:
                        pl.flour-=qty
                        pl.cash+=qty*price
                        tobuy-=qty
                    else:
                        pl.cash+=pl.flour*price
                        tobuy-=pl.flour
                        pl.flour=0
            i-=1
            
        # TODO Buy orders and done transaction to be implemented
            
        # The wheat market has a simple market maker :
        # if an asking price is lower than an offer price, the transaction
        # is made half of the way
        print self.wheat_market
        buys = list()
        sells = list()
        for o in self.wheat_market:
            if o[1]=="buy":
                buys.append([o[0],o[2],o[3]])
            else:
                sells.append([o[0],o[2],o[3]])
        sells.sort(key=lambda x:x[2])
        buys.sort(key=lambda x:-x[2])
        idxb=0
        idxs=0
        while(buys[idxb][1]>sells[idxs][1]):
            # accepted
            buyer = self.players_stat[buys[idxb][0]]
            seller = self.players_stat[sellss[idxs][0]]
            price = 0.5*(buys[idxb][2] + sells[idxb][2])
            price = 0.5*(buys[idxb][2] + sells[idxb][2])            
            if buys[idxb][1]>sells[idxs][1]:
                qty=sells[idxs][1]
            else:
                qty=buys[idxb][1]
            if buyer.cash>price*qty and seller.wheat>qty:
                buyer.cash -= price*qty
                buyer.wheat += qty
                seller.cash += price*qty
                seller.wheat -= qty

        
        # TODO Done transaction to be implemented
            
            
   
   def buy_facility(self, botname, ftype, qty):
        if ftype=="farm":
            if(self.players_state[botname].cash >=
               qty*self.farm_price):
                self.players_state[botname].cash-=qty*self.farm_price
                self.players_state[botname].farms+=qty
        if ftype=="mill":
            if(self.players_state[botname].cash >=
               qty*self.mill_price):
                self.players_state[botname].cash-=qty*self.mill_price
                self.players_state[botname].mill+=qty

   
   def sell_facility(self, botname, ftype, qty):
        if ftype=="farm":
            if(self.players_state[botname].farm >= qty):
                self.players_state[botname].farm-=qty
                self.players_state[botname].cash+=qty*self.farm_price
        if ftype=="mill":
            if(self.players_state[botname].mill >= qty):
                self.players_state[botname].mill-=qty
                self.players_state[botname].cash+=qty*self.mill_price


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

