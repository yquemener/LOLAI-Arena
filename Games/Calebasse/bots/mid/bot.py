#!/usr/bin/env python2
#-*- coding:utf8-*-  

import json
import sys

# The bot is initialized
print "OK"

# Getting his id
uuid = raw_input()

# Ready to start
print "OK"


playing = raw_input()
while (playing!='Q'):
    # get accounts
    accounts_raw = raw_input()
    accounts = json.loads(accounts_raw)
    
    # go to bets
    ready = raw_input()
    while (ready != "Accepted"):
        # This player gives all he has
        print int(accounts[uuid]/2)
        ready = raw_input()
        
    # Get bets of everybody
    bets_raw = raw_input()
    bets = json.loads(bets_raw)

    # Get the winner
    winner_r = raw_input()

    playing = raw_input()

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
