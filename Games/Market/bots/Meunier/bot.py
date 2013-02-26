#!/usr/bin/env python2
#-*- coding:utf8-*-  

# MAkes mills, buys wheat and sells flour

import sys
import json
import random

print "OK"

ins = raw_input()
myid = ins
#sys.stderr.write("My id is " + myid + "\n")
lastwheatprice = 5.0
lastflourprice = 9.9
ins = raw_input()
while ins!='Q':
    ws = json.loads(ins)
    for idx in range(len(ws[0])):
        if(ws[0][idx][0]==myid):
            mystate = ws[0][idx]
            (n, cash, wheat, flour, farms, mills) = mystate
    #sys.stderr.write("My state :"+str(mystate)+"\n")
    #sys.stderr.write("Sent :" + ins+"\n")
    orders = list()
    flour_max_price = ws[4][7]
    if flour<50 and wheat>mills*2:
        if ws[4][1]*2<=cash:
            orders.append('["buy", "mill",1]')
            
    if mills==0 and ws[4][1]<=cash:
        orders.append('["buy", "mill",1]')
            
    # compute flour price
    count=0
    avg=0
    for t in ws[3]:
        if(t[4]=="f"):
            count+=1
            avg+=t[3]    
    if count>0:
        avg/=count
    else:
        avg=lastflourprice
    flour_price = avg
    lastflourprice = avg

    factor = 1.0
    if(flour>10):
        factor = 0.9
    else:
        factor = 1.1
    # To avoid totally synchronous reactions
    factor *= random.randint(950,1050)/1000.0

    askpriceflour = factor * flour_price
    if askpriceflour>flour_max_price:
        askpriceflour=flour_max_price-0.01


    
    # compute wheat price
    count=0
    avg=0
    for t in ws[3]:
        if(t[4]=="w"):
            count+=1
            avg+=t[3]    
    if count>0:
        avg/=count
    else:
        avg=lastwheatprice

    wheat_price = avg
    lastwheatprice = wheat_price
    factor = random.randint(950,1050)/1000.0
    if wheat<mills:
        factor += 0.1
    if avg*factor>10.0:
        factor = 9.9/avg
        
    askpricewheat=wheat_price*factor
    
    wheatquantity = (cash - ws[4][1]*2)/askpricewheat
    if(wheatquantity<0):
        wheatquantity = (cash/(2*askpricewheat))
    
    if(askpriceflour>askpricewheat):
        if flour>0:
            orders.append('["sell","flour",'+str(flour)+','+str(askpriceflour)+']')
        if(mills>0) and wheatquantity>0:
            orders.append('["buy","wheat",'+str(wheatquantity)+','+str(askpricewheat)+']')


        

    sso = "[ "
    for o in orders:
        sso=sso+o+","
    sso = sso[:-1]+"]"
    #sys.stderr.write("Sent :" + sso + "\n")
    print sso
    ins = raw_input()

