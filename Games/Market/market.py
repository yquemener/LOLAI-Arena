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
        self.score = 0

    def state(self):
        return [self.name, self.cash,
                self.wheat,
                self.flour,
                self.farms,
                self.mills]

    def dstate(self):
        return {'name':self.name, 
                 'cash':self.cash,
                 'wheat':self.wheat,
                 'flour':self.flour,
                 'farms':self.farms,
                 'mills':self.mills}

    def __str__(self):
        return str(self.dstate())

    def __repr__(self):
        return str(self.dstate())


class Market(Game):
    NAME = "Market"
    HIST_ATTR = ["wheat_price", "flour_price"]
    # Initialization of the constants of the game
    farm_price = 20
    mill_price = 85
    transformation_rate = 1.0
    growing_cycle = 1
    flour_bought_each_turn = 50
    farm_production = 1
    mill_production = 1
    flour_max_price = 10
    farm_cost = 1
    mill_cost = 1

    def __init__(self, bots, round=300, hist_attr=HIST_ATTR):
        """Initialization of the market game

        @param bots: list of bots
        @param round: number of round

        """
        Game.__init__(self, Market.NAME, bots, hist_attr)


        # Initialization of the markets
        self.wheat_market=list()
        self.flour_market=list()
        self.transactions_done=list()
        self.stats=[self.farm_price,
                    self.mill_price,
                    self.transformation_rate,
                    self.growing_cycle,
                    self.flour_bought_each_turn,
                    self.farm_production,
                    self.mill_production,
                    self.flour_max_price]


        self.round = int(round)
        self.players_state = dict()
        self.stats_charts = {"flour_price" : [],
                             "wheat_price" : []}
        self.botsid = dict()
        i = 0
        for b in self.bots:
            botname = b.name+"_"+str(i)
            self.botsid[botname] = b
            self.players_state[botname]=Player(botname)
            i+=1


    def world_state(self):
        players = list()
        for p in self.players_state.values():
            players.append(p.state())
            
        return [players, 
                self.wheat_market, 
                self.flour_market, 
                self.transactions_done,
                self.stats]
        
    def steady_bots(self):
        """Sends to bots the new round message
    
        """
        ws = self.world_state()
        msg=json.dumps(ws)
        
        for b in self.bots:
            b.send_msg(msg)

    # -------------------
    # Main step of the game

    def run_game(self):
        """ Process of the game 
        
        """
        # send its bot its identification
        for botname in self.botsid.keys():
            self.botsid[botname].send_msg(botname)

        for k in range(self.round):
            # Send to bots the state of the world 
            self.steady_bots()
            # Rules of the game
            self.go()
            # Store stats
            avgf=countf=avgw=countw=0
            for t in self.transactions_done:
                if t[4]=="f":
                    countf+=1
                    avgf+=t[3]
                else:
                    countw+=1
                    avgw+=t[3]
                    
            if countw>0:
                avgw/=countw
            else:
                avgw=0
            if countf>0:
                avgf/=countf
            else:
                avgf=0
            self.flour_price = avgf
            self.wheat_price = avgw

    def go(self):
        """Rules of the game
    
        """
        # Clear the markets
        self.flour_market = list()
        self.wheat_market = list()
        self.transactions_done=list()
        
        # Reading bots choices
        for bn in self.botsid.keys():
            s=self.botsid[bn].get_ans()
            ans=json.loads(s)
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
        for bn in self.players_state.keys():
            pl = self.players_state[bn]
            pl.wheat += pl.farms*self.farm_production
            transformed = min(pl.mills*self.mill_production, pl.wheat)
            pl.flour += transformed
            pl.wheat -= transformed
            pl.cash -= pl.farms*self.farm_cost
            pl.cash -= pl.mills*self.mill_cost

        # Running the markets
        """print
        print "Flour market : "
        print self.flour_market"""
        
        # The flour market is easy
        self.flour_market.sort(key=lambda x:-x[3])
        tobuy = self.flour_bought_each_turn
        i=len(self.flour_market)-1
        while tobuy>0 and i>=0 and self.flour_market[i][3] <= self.flour_max_price:
            (bn, buysell, qty, price) = self.flour_market[i]
            if buysell=="sell":
                pl=self.players_state[bn]
                if qty >= tobuy:
                    if pl.flour >= tobuy:
                        pl.cash+=tobuy*price
                        self.transactions_done.append([-1,bn,tobuy,price,'f'])
                        pl.flour-=tobuy
                        tobuy=0
                    else:
                        pl.cash+=pl.flour*price
                        self.transactions_done.append([-1,bn,pl.flour,price,'f'])
                        tobuy-=pl.flour
                        pl.flour=0
                else:
                    if pl.flour>=qty:
                        pl.cash+=qty*price
                        self.transactions_done.append([-1,bn,qty,price,'f'])
                        pl.flour-=qty
                        tobuy-=qty
                    else:
                        pl.cash+=pl.flour*price
                        self.transactions_done.append([-1,bn,pl.flour,price,'f'])
                        tobuy-=pl.flour
                        pl.flour=0
            i-=1
            
        # TODO Buy orders and done transaction to be implemented
            
        # The wheat market has a simple market maker :
        # if an asking price is lower than an offer price, the transaction
        # is made half of the way
        buys = list()
        sells = list()

        for o in self.wheat_market:
            if o[1]=="buy":
                buys.append([o[0],o[2],o[3]])
            else:
                sells.append([o[0],o[2],o[3]])
        """print
        print "Wheat market : "
        print "  Buy orders:\n",buys
        print "  Sell orders:\n",sells"""
        
        sells.sort(key=lambda x:x[2])
        buys.sort(key=lambda x:-x[2])
        idxb=0
        idxs=0
        while(idxb<len(buys) and idxs<len(sells) and buys[idxb][2]>sells[idxs][2]):
            # accepted
            buyer = self.players_state[buys[idxb][0]]
            seller = self.players_state[sells[idxs][0]]
            price = 0.5*(buys[idxb][2] + sells[idxs][2])
            if buys[idxb][1]>sells[idxs][1]:
                qty=sells[idxs][1]
            else:
                qty=buys[idxb][1]
            if buyer.cash>price*qty and seller.wheat>qty:
                buyer.cash -= price*qty
                buyer.wheat += qty
                seller.cash += price*qty
                seller.wheat -= qty
            if qty>=buys[idxb][1]:
                idxb+=1
            else:
                buys[idxb][1]-=qty
            if qty>=sells[idxs][1]:
                idxs+=1
            else:
                sells[idxs][1]-=qty
            self.transactions_done.append([-1, -1, qty, price,'w'])
            
        # Eliminating bankrupted bots    
        
        eliminated = list()
        for bn in self.players_state.keys():
            pl = self.players_state[bn]
            if(pl.cash<0):
                eliminated.append(bn)

        for e in eliminated:
            self.players_state.pop(e)
            self.botsid.pop(e)
   

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
                self.players_state[botname].mills+=qty

   
    def sell_facility(self, botname, ftype, qty):
        if ftype=="farm":
            if(self.players_state[botname].farms >= qty):
                self.players_state[botname].farms-=qty
                self.players_state[botname].cash+=qty*self.farm_price
        if ftype=="mill":
            if(self.players_state[botname].mills >= qty):
                self.players_state[botname].mills-=qty
                self.players_state[botname].cash+=qty*self.mill_price


    def det_winner(self):
        """ Choose the winner 
        
        """
        bestscore=-1
        bestname=""
        for k in self.players_state.keys():
            p=self.players_state[k]
            score = p.cash+p.mills*self.mill_price+p.farms*self.farm_price
            self.botsid[k].score=score
            if bestscore<score:
                bestscore = score
                bestame = k
        self.winner=bestname

    def give_results(self):
        """Give the sum up of the game
        
        @return: the bots and the winner
        @rtype: dictionary
        
        """
        self.det_winner()

        plot_accounts = {"name": "Accounts", "from_bots": "account"}
        plot_bets= {"name": "Bets", "from_bots": "bet"}

        winner = "The winner is {win}".format(win = self.winner)

        return {'game_name' : self.NAME, 'bots': self.bots, "comments" : [winner], "attributes" : ["cash"], "plots" : []}




# ----------------------
# What is run in this file

if __name__ == '__main__':

    pass

