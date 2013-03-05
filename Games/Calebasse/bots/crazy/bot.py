#!/usr/bin/env python2
#-*- coding:utf8-*-  
import json
import sys

# The bot is initialized
print "OK"

sys.stderr.write("Inite\n")

# Getting his id
uuid = raw_input()
sys.stderr.write("UUID\n")

# Ready to start
print "OK"
sys.stderr.write("Ready\n")



while raw_input()!='Q':
    # get accounts
    accounts =json.loads(raw_input()) 

    # go to bets
    while raw_input() != "Accepted":
        print account[uuid]

    # Get bets of everybody
    bets = json.loads(raw_input())

    # Get the winner
    winner = json.loads(raw_input())
