#!/usr/bin/env python2
#-*- coding:utf8-*-  

# Makes mills, buys wheat and sells flour

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

import sys
import json
import random

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
        (idx, cash, wheat, flour, farms, mills) = state
        if(idx==myid):
            mystate = state
            break

    # compute wheat price
    (wheat_price, flour_price) = get_avg_price(transactions, price_belief)

    orders = list()

    # Simple investment strategy : if we have twice the necessary cash, 
    # more wheat we can process in 2 turns and not an oversized stock of
    # flour, we buy one new mill
    if flour<50 and wheat>mills*2:
        if mill_price*2<=cash:
            orders.append('["buy", "mill",1]')
            
    # Also buy a mill if we don't have one
    if mills==0 and mill_price<=cash:
        orders.append('["buy", "mill",1]')
            
    lastflourprice = flour_price

    factor = 1.0
    # If we have too much flour, try to lower the price to sell it more quickly,
    # otherwise, raise the price
    if(flour>10):
        factor = 0.9
    else:
        factor = 1.1
    # Add some randomness to avoid totally synchronous reactions
    factor *= random.randint(950,1050)/1000.0

    askpriceflour = factor * flour_price
    
    # Make sure to not ask more than the maximum price for flour
    if askpriceflour>flour_max_price:
        askpriceflour=flour_max_price-0.01


    lastwheatprice = wheat_price
    # Add some randomness to avoid totally synchronous reactions
    factor = random.randint(950,1050)/1000.0
    # If we have less wheat than we can process, raise the price we are
    # ready to pay
    if wheat<mills:
        factor += 0.1
    askpricewheat=wheat_price*factor

    # Make sure we are not buying for more that the maximum flour price
    if askpricewheat>flour_max_price:
        askpricewheat = 9.9
        
    
    # We buy enough wheat to keep enough cash to buy two mills
    wheatquantity = (cash - mill_price*2)/askpricewheat
    # If that means zero, we just buy half what we can buy
    if(wheatquantity<0):
        wheatquantity = (cash/(2*askpricewheat))
    
    if(askpriceflour>askpricewheat):
        if flour>0:
            orders.append('["sell","flour",'+str(flour)+','+str(askpriceflour)+']')
        if(mills>0) and wheatquantity>0:
            orders.append('["buy","wheat",'+str(wheatquantity)+','+str(askpricewheat)+']')
    
    send_orders(orders)

    ins = raw_input()

