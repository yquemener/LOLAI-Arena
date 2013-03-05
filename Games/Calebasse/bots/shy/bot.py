#!/usr/bin/env python2
#-*- coding:utf8-*-  
import json

# The bot is initialized
print "OK"

# Getting his id
uuid = raw_input()

# Ready to start
print "OK"

while raw_input()!='Q':
    # get accounts
    s=raw_input()
    print "__",s
    accounts =json.loads(s) 

    # go to bets
    while raw_input() != "Accepted":
        print min(accounts[uuid],5)

    # Get bets of everybody
    s=raw_input()
    print "__",s
    bets = json.loads(s)

    # Get the winner
    winner = json.loads(raw_input())

