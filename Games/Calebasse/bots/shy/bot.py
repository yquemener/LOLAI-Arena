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
sys.stderr.write("{uuid} receives as playing {playing}\n".format(uuid=uuid, playing = playing))
while (playing!='Q'):
    # get accounts
    accounts_raw = raw_input()
    sys.stderr.write("{uuid} receives {accounts_r}\n".format(uuid=uuid, accounts_r = accounts_raw))
    accounts = json.loads(accounts_raw)
    
    # go to bets
    ready = raw_input()
    sys.stderr.write("{uuid} receives 'ready' {ready}\n".format(uuid=uuid, ready=ready))
    while (ready != "Accepted"):
        # This player gives never more than 5
        print min(accounts[uuid],5)
        ready = raw_input()
        sys.stderr.write("{uuid} receives 'ready' {ready}\n".format(uuid=uuid, ready=ready))
        
    # Get bets of everybody
    bets_raw = raw_input()
    sys.stderr.write("{uuid} receives bets of everybody {bets_r}\n".format(uuid=uuid, bets_r=bets_raw))
    bets = json.loads(bets_raw)

    # Get the winner
    winner_r = raw_input()
    sys.stderr.write("{uuid} receives the winner {winner}\n".format(uuid=uuid, winner=winner_r))

    playing = raw_input()
    sys.stderr.write("{uuid} receives as playing {playing}\n".format(uuid=uuid, playing = playing))

# -----------------------------
# Reglages pour 'vim'
# vim:set autoindent expandtab tabstop=4 shiftwidth=4:
# cursor: 16 del 
