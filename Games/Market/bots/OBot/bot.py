#!/usr/bin/env python2
#-*- coding:utf8-*-  

import sys

print "OK"

ins = raw_input()
if ins!='Q':
    print '[["buy", "farm",1], ["buy", "mill", 1]]'

while ins!='Q':
    sys.stderr.write("Sent :" + ins+"\n")
    print '[]'
    ins = raw_input()
