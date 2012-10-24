#!/usr/bin/env python2
#-*- coding:utf8-*-  

# This bot is an imitator that begins with cooperatio, betrays on the last
# and betrays any partner who betrayed more than thress times.

import sys

rounds=1
totalT=0
print "OK"
keeprunning=raw_input()

ans="C"
while keeprunning!='Q':

    if rounds==50 or totalT>3:
        print 'T'
    else:
        print ans
    ans=raw_input()
    keeprunning=raw_input()
    if(ans=='T'): totalT+=1
    rounds+=1
