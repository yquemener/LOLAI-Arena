#!/usr/bin/env python2
#-*- coding:utf8-*-  

import sys
import json

print "OK"

ins = raw_input()
myid = ins
sys.stderr.write("My id is " + myid + "\n")

if ins!='Q':
    print '[["buy", "farm",1], ["buy", "mill", 1]]'

ins = raw_input()
while ins!='Q':
    ws = json.loads(ins)
    for idx in range(len(ws[0])):
        if(ws[0][idx][0]==myid):
            mystate = ws[0][idx]
            (n, cash, wheat, flour, farms, mill) = mystate
    sys.stderr.write("My state :"+str(mystate)+"\n")
    #sys.stderr.write("Sent :" + ins+"\n")
    if flour>0:
        print '[["sell", "flour", '+str(flour)+', 10]]'
    ins = raw_input()
