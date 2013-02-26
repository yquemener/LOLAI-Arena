#!/usr/bin/env python2
#-*- coding:utf8-*-  

# Makes farms and sell the wheat

import sys
import json
import random

def botlog(s):
    sys.stderr.write(str(s)+"\n")

def get_avg_price(transactions, default_price=5.0):
    avgw=0
    avgf=0
    countw=0
    countf=0
    for (id_buyer, id_seller, qty, price, wf) in transactions:
        if(wf=="w"):
            countw+=1
            avgw+=price
        if(wf=="f"):
            countf+=1
            avgf+=price
    if countw>0:
        avgw/=countw
    else:
        avgw = default_price
    if countf>0:
        avgf/=countf
    else:
        avgf = default_price
    return (avgw,avgf)

def send_orders(orders):
    sso = "[ "
    for o in orders:
        sso=sso+o+","
    sso = sso[:-1]+"]"
    print sso

price_belief = 5.0

# Tell the server we are ready
print "OK"

# Makes the server display a log message 
botlog("We are OK")

# Get the ID back
ins = raw_input()
myid = ins

# Get the first input
ins = raw_input()

# An input of 'Q' means that the bot must return
while ins!='Q':
    (players_state, 
            wheat_market, 
            flour_market, 
            transactions, 
            useful_stats) = json.loads(ins)

    (farm_price,
            mill_price,
            transformation_rate,
            growing_cycle,
            flour_bought_each_turn,
            farm_production,
            mill_production,
            flour_max_price) = useful_stats

    for state in players_state:
        (idx, cash, wheat, flour, farms, mill) = state
        if(idx==myid):
            mystate = state
            break
    orders = list()

    # Simple investment stratey :
    # Buy a farm if we have no stock and twice the necessary cash
    if wheat==0:
        if farm_price<=cash*2:
            orders.append('["buy", "farm",1]')
            pass
            
    # compute wheat price
    (wheat_price, flour_price) = get_avg_price(transactions, price_belief)

    # Add a random factor
    factor = random.randint(950,1050)/1000.0
    wheat_price*=factor
    price_belief = wheat_price

    # If we have few stock and a bit of cash, try to raise the prices, otherwise 
    # diminish them
    if wheat<farms*2 and cash>10:
        price_belief += random.randint(10,100)/100.0
    else:
        price_belief -= random.randint(10,100)/100.0

    # Check that the price offered is not more than the max flour price
    if price_belief>flour_max_price:
        price_belief = flour_max_price-0.1
    # Check that the price is not lower than the fixed cost of a farm
    if price_belief<1.0: 
        price_belief = 1.1

    # Try to sell all the stock
    if wheat>0:
        orders.append('["sell","wheat",'+str(wheat)+','+str(price_belief)+']')

    send_orders(orders)
    ins = raw_input()

