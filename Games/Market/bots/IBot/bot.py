#!/usr/bin/env python2
#-*- coding:utf8-*-  

import sys
import json
import random

print "OK"

ins = raw_input()
myid = ins
#sys.stderr.write("My id is " + myid + "\n")

ins = raw_input()
while ins!='Q':
    ws = json.loads(ins)
    for idx in range(len(ws[0])):
        if(ws[0][idx][0]==myid):
            mystate = ws[0][idx]
            (n, cash, wheat, flour, farms, mill) = mystate
    #sys.stderr.write("My state :"+str(mystate)+"\n")
    #sys.stderr.write("Sent :" + ins+"\n")
    orders = list()
    flour_max_price = ws[4][7]
    if wheat<50 and flour<50:
        if ws[4][0]+ws[4][1]<=cash:
            orders.append('["buy", "farm",1]')
            orders.append('["buy", "mill",1]')
            pass
            
    # compute flour price
    count=0
    avg=0
    for t in ws[3]:
        count+=1
        avg+=t[2]
    if count>0:
        avg/=count
    else:
        avg=9
    factor = random.randint(950,1050)/1000.0
    if avg*factor>10.0:
        factor = 9.9/avg
    if flour>0:
        orders.append('["sell","flour",'+str(flour)+','+str(avg*factor)+']')

    sso = "[ "
    for o in orders:
        sso=sso+o+","
    sso = sso[:-1]+"]"
    #sys.stderr.write("Sent :" + sso + "\n")
    print sso
    ins = raw_input()

