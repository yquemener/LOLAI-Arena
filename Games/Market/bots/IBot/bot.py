#!/usr/bin/env python2
#-*- coding:utf8-*-  

import sys
import json

print "OK"

ins = raw_input()
myid = ins
#sys.stderr.write("My id is " + myid + "\n")

if ins!='Q':
    print '[["buy", "farm",1], ["buy", "mill", 1]]'

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
    if ws[4][0]+ws[4][1]<=cash:
        orders.append('["buy", "farm",1]')
        orders.append('["buy", "mill",1]')
    if flour>0:
        orders.append('["sell","flour",'+str(flour)+','+str(flour_max_price-1)+']')

    sso = "[ "
    for o in orders:
        sso=sso+o+","
    sso = sso[:-1]+"]"
    #sys.stderr.write("Sent :" + sso + "\n")
    print sso
    ins = raw_input()
